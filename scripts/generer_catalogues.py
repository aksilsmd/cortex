#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — génère docs/catalogue-skills.md et docs/catalogue-agents.md (bibliothèque standard uniquement).

Produit aussi les deux cartes SVG qui en dépendent : docs/images/carte-skills.svg et docs/images/carte-poles.svg.

Les catalogues sont lus dans les en-têtes des fichiers dan-cortex/skills/*/SKILL.md et dan-cortex/agents/*.md :
ils ne se modifient jamais à la main. Un skill qui n'est rangé dans aucune famille fait échouer la génération,
pour que le catalogue reste complet.

Usage :
  python3 scripts/generer_catalogues.py              réécrit les deux catalogues
  python3 scripts/generer_catalogues.py --verifier   échoue (code 1) si un catalogue n'est pas à jour
"""
import argparse
import math
import re
import sys
from xml.sax.saxutils import escape
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PLUGIN = RACINE / "dan-cortex"
DOCS = RACINE / "docs"

# Familles de skills, dans l'ordre d'affichage. Chaque skill du plugin doit figurer une fois.
FAMILLES = [
    ("Pilotage et décision", ["lancer-projet", "accueil-recueil", "reunion-decision", "audit-general",
                              "execution-resiliente", "vigilance-discernement"]),
    ("Besoin et marché", ["recueil-besoin", "veille-marche", "specifications"]),
    ("Design et expérience", ["maquettes-parcours", "design-apple", "mouvement-interface", "conception-interface",
                              "fabrique-themes", "design-affiche"]),
    ("Architecture et réalisation", ["architecture-normes", "usine-logicielle", "cartographie-graphe",
                                     "boite-outils-it", "crm-twenty", "webapp-testing"]),
    ("Sécurité et confiance", ["securite-protection", "robustesse-agents", "confidentialite-traces"]),
    ("Droit, finance et mise sur le marché", ["juridique-conformite", "budget-finance", "marketing-commercial",
                                              "lancement-exploitation"]),
    ("Contenus et langues", ["atelier-ecriture", "traduction-interpretariat", "communication-interne"]),
    ("Documents et médias", ["docx", "pdf", "pptx", "xlsx", "algorithmic-art", "slack-gif-creator",
                             "brand-guidelines"]),
    ("Écosystème Claude", ["claude-api", "mcp-builder", "skill-creator", "web-artifacts-builder",
                           "academy-guide"]),
]

# Pôle d'un agent : sa section dans l'organigramme du réseau (source unique, tenue à la main).
ORGANIGRAMME = PLUGIN / "skills" / "lancer-projet" / "references" / "organigramme.md"
NIVEAUX = {"inherit": "A — jugement", "sonnet": "B — production", "haiku": "C — collecte"}
ENTETE = "<!-- Fichier généré par scripts/generer_catalogues.py : ne pas modifier à la main. -->\n"


def entete_yaml(texte):
    """Lit l'en-tête YAML simple d'un fichier Markdown : scalaires, blocs |/>, listes de chaînes."""
    if not texte.startswith("---\n"):
        return {}
    bloc = texte[4:].split("\n---", 1)[0].splitlines()
    donnees, cle, i = {}, None, 0
    while i < len(bloc):
        ligne = bloc[i]
        m = re.match(r"^([A-Za-z][\w-]*):\s?(.*)$", ligne)
        if m:
            cle, valeur = m.group(1), m.group(2).strip()
            if valeur in ("|", "|-", ">", ">-", "|+", ">+"):
                morceaux = []
                while i + 1 < len(bloc) and (bloc[i + 1].startswith((" ", "\t")) or not bloc[i + 1].strip()):
                    i += 1
                    morceaux.append(bloc[i].strip())
                donnees[cle] = " ".join(m for m in morceaux if m)
            elif valeur == "":
                donnees[cle] = []
            elif valeur.startswith("[") and valeur.endswith("]"):
                donnees[cle] = [v.strip().strip('"').strip("'") for v in valeur[1:-1].split(",") if v.strip()]
            else:
                donnees[cle] = valeur.strip('"').strip("'")
        elif ligne.lstrip().startswith("- ") and cle and isinstance(donnees.get(cle), list):
            donnees[cle].append(ligne.lstrip()[2:].strip().strip('"').strip("'"))
        elif cle and isinstance(donnees.get(cle), str) and ligne.startswith((" ", "\t")):
            donnees[cle] += " " + ligne.strip()
        i += 1
    return donnees


def cellule(texte, limite=230):
    texte = re.sub(r"\s+", " ", texte.replace("|", "\\|")).strip()
    if len(texte) > limite:
        texte = texte[:limite].rsplit(" ", 1)[0].rstrip(",;:.") + " …"
    return texte


def origine(dossier, entete):
    licence = entete.get("license", "")
    if not (dossier / "LICENSE.txt").is_file():
        return "Dan-Cortex"
    if licence.startswith("Apache-2.0"):
        return "traduit d'Anthropic (Apache-2.0)"
    return "copié d'Anthropic (Apache-2.0)"


def compter(dossier, sous):
    return sum(1 for p in dossier.rglob("*") if p.is_file() and sous in p.relative_to(dossier).parts[:1]
               and "__pycache__" not in p.parts)


def lire_skills():
    skills = {}
    for dossier in sorted(p for p in (PLUGIN / "skills").iterdir() if p.is_dir()):
        entete = entete_yaml((dossier / "SKILL.md").read_text(encoding="utf-8"))
        skills[dossier.name] = {
            "description": entete.get("description", ""),
            "origine": origine(dossier, entete),
            "references": compter(dossier, "references") + compter(dossier, "assets"),
            "scripts": compter(dossier, "scripts"),
        }
    return skills


def lire_agents():
    agents = []
    for fichier in sorted((PLUGIN / "agents").glob("*.md")):
        entete = entete_yaml(fichier.read_text(encoding="utf-8"))
        skills = entete.get("skills") or []
        agents.append({
            "nom": entete.get("name", fichier.stem),
            "description": re.sub(r"^Dan-Cortex\s*·\s*", "", entete.get("description", "")),
            "modele": entete.get("model", ""),
            "effort": entete.get("effort", ""),
            "outils": entete.get("tools") or [],
            "skills": skills,
        })
    poles, ordre = lire_organigramme()
    absents = sorted(a["nom"] for a in agents if a["nom"] not in poles)
    if absents:
        raise SystemExit("Agents absents de l'organigramme (%s) : %s"
                         % (ORGANIGRAMME.relative_to(RACINE).as_posix(), absents))
    for a in agents:
        a["pole"] = poles[a["nom"]]
    return agents, ordre


def lire_organigramme():
    """Associe chaque agent à son pôle d'après les sections « ### <pôle> » de l'organigramme."""
    texte = ORGANIGRAMME.read_text(encoding="utf-8")
    section = texte.split("\n## 2.", 1)[1].split("\n## 3.", 1)[0]
    poles, ordre, pole = {}, [], None
    for ligne in section.splitlines():
        m = re.match(r"^### (.+?)(?: \(|$)", ligne)
        if m:
            pole = m.group(1).strip()
            ordre.append(pole)
            continue
        m = re.match(r"^\| `([a-z0-9-]+)` \|", ligne)
        if m and pole:
            poles[m.group(1)] = pole
    return poles, ordre


def catalogue_skills(skills):
    ranges = [s for _, noms in FAMILLES for s in noms]
    manquants = sorted(set(skills) - set(ranges))
    inconnus = sorted(set(ranges) - set(skills))
    doublons = sorted({s for s in ranges if ranges.count(s) > 1})
    if manquants or inconnus or doublons:
        raise SystemExit("Familles à mettre à jour dans scripts/generer_catalogues.py — sans famille : %s ; "
                         "inconnus : %s ; en double : %s" % (manquants, inconnus, doublons))
    lignes = [ENTETE, "# Catalogue des skills", "",
              "%d skills, rangés en %d familles. Chaque skill s'appelle par `/dan-cortex:<nom>` dans Claude Code "
              "ou dans l'application Claude. Les descriptions sont celles des fichiers `SKILL.md` (celles des skills "
              "copiés d'Anthropic sont restées en anglais)." % (len(skills), len(FAMILLES)), "",
              "Origines : %d écrits pour Dan-Cortex, %d traduits d'Anthropic, %d copiés d'Anthropic sans "
              "modification (licence Apache-2.0, voir [`dan-cortex/NOTICE.md`](../dan-cortex/NOTICE.md))." % tuple(
                  sum(1 for s in skills.values() if s["origine"].startswith(o))
                  for o in ("Dan-Cortex", "traduit", "copié")), "",
              "![Carte des skills par famille](images/carte-skills.svg)", "", "## Sommaire", ""]
    for famille, noms in FAMILLES:
        ancre = re.sub(r"[^\w\- ]", "", famille.lower()).replace(" ", "-")
        lignes.append("- [%s](#%s) (%d)" % (famille, ancre, len(noms)))
    for famille, noms in FAMILLES:
        lignes += ["", "## %s" % famille, "",
                   "| Commande | Rôle | Origine | Références | Scripts |", "|---|---|---|---:|---:|"]
        for nom in noms:
            s = skills[nom]
            lignes.append("| [`/dan-cortex:%s`](../dan-cortex/skills/%s/SKILL.md) | %s | %s | %d | %d |" % (
                nom, nom, cellule(s["description"]), s["origine"], s["references"], s["scripts"]))
    total_ref = sum(s["references"] for s in skills.values())
    total_scr = sum(s["scripts"] for s in skills.values())
    lignes += ["", "## Totaux", "",
               "| Élément | Nombre |", "|---|---:|",
               "| Skills | %d |" % len(skills),
               "| Fichiers de référence et gabarits (`references/`, `assets/`) | %d |" % total_ref,
               "| Fichiers sous `scripts/` | %d |" % total_scr, ""]
    return "\n".join(lignes)


def catalogue_agents(agents, ordre):
    par_pole = {}
    for a in agents:
        par_pole.setdefault(a["pole"], []).append(a)
    niveaux = {n: sum(1 for a in agents if a["modele"] == m) for m, n in NIVEAUX.items()}
    lignes = [ENTETE, "# Catalogue des agents", "",
              "%d agents experts, rangés par pôle selon l'[organigramme du réseau]"
              "(../dan-cortex/skills/lancer-projet/references/organigramme.md). Type d'agent à lancer : "
              "`dan-cortex:<nom>`. Fiches complètes dans [`dan-cortex/agents/`](../dan-cortex/agents/)."
              % len(agents), "",
              "| Niveau | Modèle | Rôle | Agents |", "|---|---|---|---:|",
              "| A — jugement | celui de la session (`inherit`) | arbitrer, concevoir, auditer | %d |"
              % niveaux["A — jugement"],
              "| B — production | `sonnet` | analyser, rédiger, développer, tester | %d |" % niveaux["B — production"],
              "| C — collecte | `haiku` | collecter, exécuter, vérifier une liste | %d |" % niveaux["C — collecte"],
              "", "![Carte des pôles](images/carte-poles.svg)", "", "## Sommaire", ""]
    poles = [p for p in ordre if p in par_pole]
    for pole in poles:
        ancre = re.sub(r"[^\w\- ]", "", pole.lower()).replace(" ", "-")
        lignes.append("- [%s](#%s) (%d)" % (pole, ancre, len(par_pole[pole])))
    for pole in poles:
        lignes += ["", "## %s" % pole, "",
                   "| Agent | Mission | Niveau | Effort | Outils | Skills préchargés |", "|---|---|---|---|---|---|"]
        for a in par_pole[pole]:
            lignes.append("| [`%s`](../dan-cortex/agents/%s.md) | %s | %s | %s | %s | %s |" % (
                a["nom"], a["nom"], cellule(a["description"], 160), NIVEAUX.get(a["modele"], a["modele"]),
                a["effort"], ", ".join(a["outils"]) or "—", ", ".join("`%s`" % s for s in a["skills"]) or "—"))
    lignes.append("")
    return "\n".join(lignes)


# --- Cartes SVG -------------------------------------------------------------------------------------------
ENCRE, GRIS, FOND = "#0F172A", "#475569", "#FFFFFF"
COULEURS_ORIGINE = {"Dan-Cortex": "#1D4ED8", "traduit": "#0F766E", "copié": "#B45309"}
POLICE = "font-family=\"system-ui, -apple-system, 'Segoe UI', Roboto, Ubuntu, sans-serif\""


def svg(largeur, hauteur, titre, description, corps):
    return ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 %d %d\" width=\"%d\" height=\"%d\" "
            "role=\"img\" aria-labelledby=\"titre desc\" %s>\n"
            "  <!-- Généré par scripts/generer_catalogues.py : ne pas modifier à la main. -->\n"
            "  <title id=\"titre\">%s</title>\n  <desc id=\"desc\">%s</desc>\n"
            "  <rect width=\"100%%\" height=\"100%%\" fill=\"%s\"/>\n%s</svg>\n"
            % (largeur, hauteur, largeur, hauteur, POLICE, escape(titre), escape(description), FOND, corps))


def texte(x, y, contenu, taille=14, couleur=ENCRE, graisse="normal", ancre="start"):
    return ("  <text x=\"%g\" y=\"%g\" font-size=\"%d\" fill=\"%s\" font-weight=\"%s\" text-anchor=\"%s\">%s</text>\n"
            % (x, y, taille, couleur, graisse, ancre, escape(contenu)))


def carte_skills(skills):
    colonnes, larg, marge, haut_ligne = 3, 372, 24, 24
    lignes_max = max(len(noms) for _, noms in FAMILLES)
    haut_carte = 52 + lignes_max * haut_ligne + 12
    rangees = math.ceil(len(FAMILLES) / colonnes)
    largeur = colonnes * larg + (colonnes + 1) * marge
    hauteur = 96 + rangees * (haut_carte + marge) + 40
    corps = texte(marge, 44, "Carte des skills par famille", 26, graisse="700")
    corps += texte(marge, 72, "%d skills · %d familles · commande : /dan-cortex:<nom>" % (len(skills), len(FAMILLES)),
                   15, GRIS)
    for i, (famille, noms) in enumerate(FAMILLES):
        x = marge + (i % colonnes) * (larg + marge)
        y = 96 + (i // colonnes) * (haut_carte + marge)
        corps += ("  <g>\n  <rect x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\" rx=\"12\" fill=\"#F8FAFC\" "
                  "stroke=\"#CBD5E1\"/>\n" % (x, y, larg, haut_carte))
        corps += texte(x + 16, y + 32, "%s (%d)" % (famille, len(noms)), 17, graisse="700")
        corps += "  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" stroke=\"#CBD5E1\"/>\n" % (
            x + 16, y + 44, x + larg - 16, y + 44)
        for j, nom in enumerate(noms):
            cy = y + 52 + j * haut_ligne + 16
            couleur = next(c for o, c in COULEURS_ORIGINE.items() if skills[nom]["origine"].startswith(o))
            corps += "  <rect x=\"%d\" y=\"%d\" width=\"10\" height=\"10\" rx=\"2\" fill=\"%s\"/>\n" % (
                x + 18, cy - 10, couleur)
            corps += texte(x + 38, cy, nom, 15)
        corps += "  </g>\n"
    y = hauteur - 22
    x = marge
    for libelle, cle in (("écrit pour Dan-Cortex", "Dan-Cortex"), ("traduit d'Anthropic", "traduit"),
                         ("copié d'Anthropic sans modification", "copié")):
        corps += "  <rect x=\"%d\" y=\"%d\" width=\"12\" height=\"12\" rx=\"2\" fill=\"%s\"/>\n" % (
            x, y - 11, COULEURS_ORIGINE[cle])
        corps += texte(x + 20, y, libelle, 14, GRIS)
        x += 30 + len(libelle) * 8
    description = "Les %d skills de Dan-Cortex rangés en %d familles : %s. La couleur indique l'origine du skill." % (
        len(skills), len(FAMILLES), " ; ".join("%s (%s)" % (f, ", ".join(n)) for f, n in FAMILLES))
    return svg(largeur, hauteur, "Carte des skills de Dan-Cortex par famille", description, corps)


def carte_poles(agents, ordre):
    par_pole = {}
    for a in agents:
        par_pole[a["pole"]] = par_pole.get(a["pole"], 0) + 1
    poles = [p for p in ordre if p in par_pole]
    largeur, hauteur, cx, cy = 1240, 900, 620, 480
    rx, ry, lb, hb = 480, 360, 212, 60
    corps = texte(32, 48, "Carte des pôles", 26, graisse="700")
    corps += texte(32, 76, "%d agents experts répartis en %d pôles autour du chef d'orchestre" % (
        len(agents), len(poles)), 15, GRIS)
    noeuds = []
    for i, pole in enumerate(poles):
        # Décalage d'un demi-pas : aucun pôle pile en haut, pour que les étiquettes ne se chevauchent pas.
        angle = -math.pi / 2 + 2 * math.pi * (i + 0.5) / len(poles)
        noeuds.append((pole, cx + rx * math.cos(angle), cy + ry * math.sin(angle)))
    for _, x, y in noeuds:
        corps += "  <line x1=\"%d\" y1=\"%d\" x2=\"%.0f\" y2=\"%.0f\" stroke=\"#94A3B8\" stroke-width=\"1.5\"/>\n" % (
            cx, cy, x, y)
    corps += "  <circle cx=\"%d\" cy=\"%d\" r=\"104\" fill=\"#1E3A8A\"/>\n" % (cx, cy)
    corps += texte(cx, cy - 10, "Chef d'orchestre", 20, "#FFFFFF", "700", "middle")
    corps += texte(cx, cy + 16, "lancer-projet", 15, "#DBEAFE", ancre="middle")
    corps += texte(cx, cy + 40, "vagues parallèles", 14, "#DBEAFE", ancre="middle")
    for pole, x, y in noeuds:
        corps += ("  <rect x=\"%.0f\" y=\"%.0f\" width=\"%d\" height=\"%d\" rx=\"10\" fill=\"#EFF6FF\" "
                  "stroke=\"#1D4ED8\" stroke-width=\"1.5\"/>\n" % (x - lb / 2, y - hb / 2, lb, hb))
        corps += texte(x, y - 4, pole, 15, graisse="700", ancre="middle")
        n = par_pole[pole]
        corps += texte(x, y + 18, "%d agent%s" % (n, "s" if n > 1 else ""), 14, GRIS, ancre="middle")
    description = "Le chef d'orchestre au centre, relié aux %d pôles : %s." % (
        len(poles), " ; ".join("%s, %d agents" % (p, par_pole[p]) for p in poles))
    return svg(largeur, hauteur, "Carte des pôles de Dan-Cortex", description, corps)


def cibles():
    skills, (agents, ordre) = lire_skills(), lire_agents()
    return {DOCS / "catalogue-skills.md": catalogue_skills(skills),
            DOCS / "catalogue-agents.md": catalogue_agents(agents, ordre),
            DOCS / "images" / "carte-skills.svg": carte_skills(skills),
            DOCS / "images" / "carte-poles.svg": carte_poles(agents, ordre)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--verifier", action="store_true", help="échoue si un catalogue n'est pas à jour")
    args = parser.parse_args(argv)
    retard = []
    for chemin, contenu in cibles().items():
        actuel = chemin.read_text(encoding="utf-8") if chemin.is_file() else None
        if actuel == contenu:
            continue
        if args.verifier:
            retard.append(chemin.relative_to(RACINE).as_posix())
        else:
            chemin.write_text(contenu, encoding="utf-8")
            print("écrit : %s" % chemin.relative_to(RACINE).as_posix())
    if retard:
        print("Catalogues en retard : %s — lancer python3 scripts/generer_catalogues.py" % ", ".join(retard))
        return 1
    if args.verifier:
        print("Catalogues à jour.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
