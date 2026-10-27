#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — outil de pilotage du dossier projet (bibliothèque standard uniquement).

Tout ce qui est mécanique passe par ce script pour ne pas coûter de tokens :
matrice de couverture, registres, jalons, journal des agents, cohérence des
interactions, traçabilité, tableau de bord.

Usage : python3 cortex.py <commande> [options]   (python3 cortex.py aide)
"""
import argparse
import csv
import datetime as _dt
import glob
import json
import os
import re
import sys
import unicodedata

RACINE_PLUGIN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GABARITS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "gabarits"))
JALONS_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "jalons.json"))

TYPES = ["site", "ecommerce", "mobile", "saas", "niche", "erp"]
MODES = ["eclair", "standard", "integral"]
# Niveau d'autonomie du chef d'orchestre (voir references/autonomie.md). « autonome » ajoute l'étiquette du même
# nom, qui fait entrer dans la matrice les contrôles propres à ce niveau.
AUTONOMIES = ["accompagne", "delegue", "autonome"]
JALONS = ["J0", "J1", "J2", "J3", "J4", "J5", "J6", "J7"]
STATUTS = ["a-faire", "en-cours", "fait", "non-applicable", "risque-accepte"]
CLOS = {"fait", "non-applicable", "risque-accepte"}
CRITICITES = ["bloquant", "majeur", "mineur"]

ARBORESCENCE = [
    "00-pilotage/registres", "00-pilotage/reunions", "00-pilotage/audits", "00-pilotage/plans",
    "01-decouverte/sources", "02-cadrage",
    "03-conception/specifications/sfd", "03-conception/architecture/adr",
    "03-conception/design/workflows", "03-conception/design/interactions",
    "03-conception/design/maquettes", "03-conception/securite",
    "03-conception/juridique", "03-conception/tests", "03-conception/marketing",
    "04-realisation/journaux", "04-realisation/revues",
    "05-validation", "06-lancement", "07-exploitation",
]

COL_COUVERTURE = ["id", "domaine", "jalon", "criticite", "controle", "preuve_attendue",
                  "reference", "statut", "preuve", "note", "maj"]

REGISTRES = {
    "decisions": ("DEC", ["id", "date", "jalon", "titre", "type", "decision", "motifs",
                          "options_ecartees", "decideur", "reunion", "statut"]),
    "risques": ("RSQ", ["id", "date", "jalon", "titre", "domaine", "cause", "impact",
                        "probabilite", "score", "parade", "proprietaire", "statut"]),
    "constats": ("AUD", ["id", "date", "jalon", "source", "gravite", "domaine", "constat",
                         "preuve", "responsable", "recommandation", "decision", "statut"]),
    "anomalies": ("ANO", ["id", "date", "jalon", "titre", "severite", "cas_de_test", "lot",
                          "description", "responsable", "statut"]),
    "actions": ("ACT", ["id", "date", "jalon", "action", "responsable", "echeance",
                        "origine", "statut"]),
    "changements": ("CHG", ["id", "date", "jalon", "titre", "demandeur", "impact", "decision", "statut"]),
}
DEFAUTS = {
    "decisions": {"type": "2", "statut": "prise"},
    "risques": {"statut": "ouvert"},
    "constats": {"statut": "ouvert", "gravite": "majeur"},
    "anomalies": {"statut": "ouverte", "severite": "majeure"},
    "actions": {"statut": "ouverte"},
    "changements": {"statut": "demande"},
}
OUVERTS = {
    "decisions": {"a-valider"},
    "risques": {"ouvert"},
    "constats": {"ouvert", "en-correction", "conteste"},
    "anomalies": {"ouverte"},
    "actions": {"ouverte"},
    "changements": {"demande", "a-l-etude"},
}
GRAVITES = ("bloquant", "majeur", "mineur", "observation")
SEVERITES = ("bloquante", "majeure", "mineure")


def normaliser(type_registre, donnees):
    """Ramène gravité, sévérité et statut à leur forme canonique, pour que les jalons les reconnaissent."""
    if type_registre == "constats" and "gravite" in donnees:
        g = sans_accent(donnees["gravite"])
        trouve = [ref for ref in GRAVITES if g.startswith(ref[:6])]
        if not trouve:
            erreur("gravité inconnue « %s ». Valeurs : %s" % (donnees["gravite"], ", ".join(GRAVITES)))
        donnees["gravite"] = trouve[0]
    if type_registre == "anomalies" and "severite" in donnees:
        g = sans_accent(donnees["severite"])
        trouve = [ref for ref in SEVERITES if g.startswith(ref[:5])]
        if not trouve:
            erreur("sévérité inconnue « %s ». Valeurs : %s" % (donnees["severite"], ", ".join(SEVERITES)))
        donnees["severite"] = trouve[0]
    if "statut" in donnees:
        donnees["statut"] = sans_accent(donnees["statut"]).replace(" ", "-")
    return donnees
COL_JOURNAL = ["date", "jalon", "vague", "agent", "modele", "tokens", "duree_s", "om", "statut"]


# --------------------------------------------------------------------------- utilitaires
def aujourdhui():
    return _dt.date.today().isoformat()


def sans_accent(texte):
    return "".join(c for c in unicodedata.normalize("NFD", texte or "") if unicodedata.category(c) != "Mn").lower()


def erreur(msg, code=2):
    print("ERREUR : " + msg, file=sys.stderr)
    sys.exit(code)


def trouver_dossier(chemin):
    """Remonte depuis `chemin` (ou le répertoire courant) jusqu'au dossier qui contient 00-pilotage/cortex.json."""
    depart = os.path.abspath(chemin or os.getcwd())
    courant = depart
    while True:
        if os.path.isfile(os.path.join(courant, "00-pilotage", "cortex.json")):
            return courant
        parent = os.path.dirname(courant)
        if parent == courant:
            erreur("aucun dossier projet Dan-Cortex trouvé à partir de %s (lancer d'abord « init », ou préciser --dossier)." % depart)
        courant = parent


def lire_config(dossier):
    with open(os.path.join(dossier, "00-pilotage", "cortex.json"), encoding="utf-8") as f:
        return json.load(f)


def ecrire_config(dossier, config):
    with open(os.path.join(dossier, "00-pilotage", "cortex.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def lire_csv(chemin):
    if not os.path.isfile(chemin):
        return []
    with open(chemin, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def ecrire_csv(chemin, colonnes, lignes):
    os.makedirs(os.path.dirname(chemin), exist_ok=True)
    with open(chemin, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=colonnes, delimiter=";", extrasaction="ignore")
        w.writeheader()
        for ligne in lignes:
            w.writerow({c: ligne.get(c, "") for c in colonnes})


def court(texte, n=110):
    texte = " ".join((texte or "").split())
    return texte if len(texte) <= n else texte[: n - 1] + "…"


def liste_arg(valeur):
    return [v.strip().lower() for v in (valeur or "").split(",") if v.strip()]


def rang_jalon(j):
    j = (j or "").upper()
    return JALONS.index(j) if j in JALONS else 99


# --------------------------------------------------------------------------- checklists du plugin
RE_ID_CONTROLE = re.compile(r"^[A-Z]{3}-\d{3}$")


def cellules(ligne):
    ligne = ligne.strip()
    if not ligne.startswith("|"):
        return None
    return [c.strip() for c in ligne.strip("|").split("|")]


def charger_checklists():
    """Lit toutes les checklists du plugin : skills/*/references/checklist-*.md."""
    items, vus = [], {}
    motif = os.path.join(RACINE_PLUGIN, "skills", "*", "references", "checklist-*.md")
    for chemin in sorted(glob.glob(motif)):
        with open(chemin, encoding="utf-8") as f:
            for n, ligne in enumerate(f, 1):
                c = cellules(ligne)
                if not c or len(c) < 8 or not RE_ID_CONTROLE.match(c[0]):
                    continue
                item = {
                    "id": c[0], "domaine": c[0][:3], "jalon": c[1].upper(), "criticite": sans_accent(c[2]),
                    "types": c[3].lower(), "conditions": c[4].lower(), "controle": c[5],
                    "preuve_attendue": c[6], "reference": c[7], "source": os.path.relpath(chemin, RACINE_PLUGIN),
                    "ligne": n,
                }
                if item["id"] in vus:
                    item["doublon"] = vus[item["id"]]
                vus[item["id"]] = "%s:%d" % (item["source"], n)
                items.append(item)
    return items


def applicable(item, types, tags):
    t = item["types"]
    if t not in ("tous", "tout", "*", ""):
        if not set(liste_arg(t)) & set(types):
            return False
    cond = item["conditions"]
    if cond in ("-", "", "aucune", "tous"):
        return True
    for alternative in cond.split(","):
        requis = [x.strip() for x in alternative.split("+") if x.strip()]
        if requis and all(r in tags for r in requis):
            return True
    return False


def chemin_couverture(dossier):
    return os.path.join(dossier, "00-pilotage", "couverture.csv")


CRITICITES_PAR_MODE = {"eclair": {"bloquant"}, "standard": {"bloquant", "majeur"},
                       "integral": {"bloquant", "majeur", "mineur"}}


def retenu(item, config):
    """Un contrôle entre dans la matrice s'il s'applique au projet, si son jalon est dans le périmètre de la
    mission, et si sa criticité est couverte par le mode (éclair : bloquants ; standard : bloquants et majeurs)."""
    if item.get("doublon") or not applicable(item, config["types"], config["tags"]):
        return False
    if rang_jalon(item["jalon"]) > rang_jalon(config.get("perimetre", "J7")):
        return False
    return item["criticite"] in CRITICITES_PAR_MODE.get(config.get("mode", "standard"), CRITICITES_PAR_MODE["standard"])


def hors_matrice(config):
    """Contrôles applicables au projet mais laissés hors matrice par le mode ou le périmètre."""
    return [i for i in charger_checklists()
            if not i.get("doublon") and applicable(i, config["types"], config["tags"]) and not retenu(i, config)]


def synchroniser_couverture(dossier, config):
    existants = {l["id"]: l for l in lire_csv(chemin_couverture(dossier))}
    ajoutes = 0
    for item in charger_checklists():
        if not retenu(item, config):
            continue
        if item["id"] in existants:
            for cle in ("jalon", "criticite", "controle", "preuve_attendue", "reference"):
                existants[item["id"]][cle] = item[cle]
            continue
        existants[item["id"]] = {
            "id": item["id"], "domaine": item["domaine"], "jalon": item["jalon"], "criticite": item["criticite"],
            "controle": item["controle"], "preuve_attendue": item["preuve_attendue"],
            "reference": item["reference"], "statut": "a-faire", "preuve": "", "note": "", "maj": "",
        }
        ajoutes += 1
    lignes = sorted(existants.values(), key=lambda l: (l["domaine"], l["id"]))
    ecrire_csv(chemin_couverture(dossier), COL_COUVERTURE, lignes)
    return ajoutes, len(lignes)


# --------------------------------------------------------------------------- init
def accorder_etiquette_autonomie(config):
    """L'étiquette « autonome » suit le niveau d'autonomie : elle fait entrer ou sortir les contrôles qui s'y
    rattachent. Renvoie True si les étiquettes ont changé."""
    tags = [t for t in config.get("tags", []) if t != "autonome"]
    if config.get("autonomie") == "autonome":
        tags.append("autonome")
    change = tags != config.get("tags", [])
    config["tags"] = tags
    return change


def cmd_init(a):
    dossier = os.path.abspath(a.dossier)
    types = liste_arg(a.types)
    for t in types:
        if t not in TYPES:
            erreur("type inconnu « %s ». Types possibles : %s" % (t, ", ".join(TYPES)))
    if not types:
        erreur("préciser au moins un type avec --types (%s)" % ", ".join(TYPES))
    if a.mode not in MODES:
        erreur("mode inconnu « %s ». Modes possibles : %s" % (a.mode, ", ".join(MODES)))
    if a.autonomie not in AUTONOMIES:
        erreur("autonomie inconnue « %s ». Niveaux possibles : %s" % (a.autonomie, ", ".join(AUTONOMIES)))
    perimetre = (a.perimetre or "J7").upper()
    if perimetre not in JALONS:
        erreur("périmètre inconnu « %s » (J1 à J7)" % perimetre)
    fichier_config = os.path.join(dossier, "00-pilotage", "cortex.json")
    if os.path.isfile(fichier_config) and not a.force:
        erreur("un projet Dan-Cortex existe déjà dans %s (utiliser « couverture resync » pour changer types ou étiquettes, ou --force)." % dossier)
    for sous in ARBORESCENCE:
        os.makedirs(os.path.join(dossier, sous), exist_ok=True)
    config = {
        "nom": a.nom, "types": types, "tags": liste_arg(a.tags), "mode": a.mode, "perimetre": perimetre,
        "autonomie": a.autonomie, "cree_le": aujourdhui(), "jalon": "J0", "vague": 0, "note": "",
        "jalons_franchis": [],
    }
    accorder_etiquette_autonomie(config)
    ecrire_config(dossier, config)
    for nom, (_, colonnes) in REGISTRES.items():
        chemin = os.path.join(dossier, "00-pilotage", "registres", nom + ".csv")
        if not os.path.isfile(chemin):
            ecrire_csv(chemin, colonnes, [])
    chemin_journal = os.path.join(dossier, "00-pilotage", "journal-agents.csv")
    if not os.path.isfile(chemin_journal):
        ecrire_csv(chemin_journal, COL_JOURNAL, [])
    chemin_lecons = os.path.join(dossier, "00-pilotage", "lecons.md")
    if not os.path.isfile(chemin_lecons):
        with open(chemin_lecons, "w", encoding="utf-8") as f:
            f.write("# Leçons du projet\n\nTrois lignes par jalon franchi : ce qui a marché, ce qui a coûté, "
                    "ce qu'on change.\n")
    for gabarit, cible in (("fiche-projet.md", "00-pilotage/fiche-projet.md"),
                           ("organigramme.md", "00-pilotage/organigramme.md")):
        source, destination = os.path.join(GABARITS, gabarit), os.path.join(dossier, cible)
        if os.path.isfile(source) and not os.path.isfile(destination):
            with open(source, encoding="utf-8") as f:
                contenu = f.read()
            contenu = (contenu.replace("{{NOM}}", a.nom).replace("{{TYPES}}", ", ".join(types))
                       .replace("{{TAGS}}", ", ".join(config["tags"]) or "aucune")
                       .replace("{{MODE}}", a.mode).replace("{{PERIMETRE}}", perimetre)
                       .replace("{{AUTONOMIE}}", a.autonomie)
                       .replace("{{DATE}}", aujourdhui()))
            with open(destination, "w", encoding="utf-8") as f:
                f.write(contenu)
    _, total = synchroniser_couverture(dossier, config)
    print("Projet « %s » créé dans %s" % (a.nom, dossier))
    print("Types : %s | Étiquettes : %s | Mode : %s | Périmètre : jusqu'à %s | Autonomie : %s"
          % (", ".join(types), ", ".join(config["tags"]) or "aucune", a.mode, perimetre, a.autonomie))
    print("Matrice de couverture : %d contrôles applicables (00-pilotage/couverture.csv)" % total)
    reste = hors_matrice(config)
    if reste:
        print("Hors matrice (mode %s, périmètre %s) : %d contrôles applicables de moindre criticité ou de jalons "
              "ultérieurs. Les intégrer : etat --set mode=… ou perimetre=…, puis couverture resync." % (a.mode, perimetre, len(reste)))
    print("Suite : compléter 00-pilotage/fiche-projet.md, composer l'équipe, puis lancer la première vague.")


# --------------------------------------------------------------------------- couverture
def filtrer_couverture(lignes, a):
    res = []
    domaines = [d.upper() for d in liste_arg(getattr(a, "domaine", None))]
    statuts = liste_arg(getattr(a, "statut", None))
    crits = liste_arg(getattr(a, "criticite", None))
    jalon = getattr(a, "jalon", None)
    for l in lignes:
        if domaines and l["domaine"] not in domaines:
            continue
        if statuts and l["statut"] not in statuts:
            continue
        if crits and l["criticite"] not in crits:
            continue
        if jalon and rang_jalon(l["jalon"]) > rang_jalon(jalon):
            continue
        res.append(l)
    return res


def cmd_couverture(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    lignes = lire_csv(chemin_couverture(dossier))
    if a.action == "stats":
        sel = filtrer_couverture(lignes, a)
        if not sel:
            print("Aucun contrôle pour ce filtre.")
            return
        clos = sum(1 for l in sel if l["statut"] in CLOS)
        print("Couverture : %d/%d contrôles traités (%d %%)" % (clos, len(sel), round(100 * clos / len(sel))))
        par = {}
        for l in sel:
            d = par.setdefault(l["domaine"], {"total": 0, "clos": 0, "bloquants": 0})
            d["total"] += 1
            if l["statut"] in CLOS:
                d["clos"] += 1
            elif l["criticite"] == "bloquant":
                d["bloquants"] += 1
        for dom in sorted(par):
            d = par[dom]
            print("  %s : %d/%d traités, %d bloquant(s) restant(s)" % (dom, d["clos"], d["total"], d["bloquants"]))
        return
    if a.action == "liste":
        sel = filtrer_couverture(lignes, a)
        for l in sel[: a.max]:
            if a.court:
                print("%s %s" % (l["id"], court(l["controle"], 90)))
            else:
                print("%s [%s %s] %s — %s | preuve attendue : %s"
                      % (l["id"], l["jalon"], l["criticite"], l["statut"], court(l["controle"], 140),
                         court(l["preuve_attendue"], 70)))
        if len(sel) > a.max:
            print("… %d autres (affiner le filtre ou augmenter --max)" % (len(sel) - a.max))
        print("%d contrôle(s)." % len(sel))
        return
    if a.action == "maj":
        if not a.ids or not a.nouveau:
            erreur("usage : couverture maj <ID[,ID…]> --nouveau <statut> [--preuve chemin] [--note texte]")
        if a.nouveau not in STATUTS:
            erreur("statut inconnu « %s ». Statuts : %s" % (a.nouveau, ", ".join(STATUTS)))
        if a.nouveau == "fait" and not a.preuve:
            erreur("un contrôle « fait » exige --preuve (chemin du livrable, du test ou de la source).")
        if a.nouveau == "non-applicable" and not a.note:
            erreur("un contrôle « non-applicable » exige --note (le motif).")
        if a.nouveau == "risque-accepte" and not a.note:
            erreur("un contrôle « risque-accepte » exige --note (qui accepte le risque, et pourquoi).")
        index = {l["id"]: l for l in lignes}
        ids = [i.strip().upper() for i in a.ids.split(",") if i.strip()]
        inconnus = [i for i in ids if i not in index]
        if inconnus:
            erreur("identifiant(s) absent(s) de la matrice : %s" % ", ".join(inconnus))
        for i in ids:
            index[i].update({"statut": a.nouveau, "preuve": a.preuve or index[i]["preuve"],
                             "note": a.note or index[i]["note"], "maj": aujourdhui()})
        ecrire_csv(chemin_couverture(dossier), COL_COUVERTURE, lignes)
        print("%d contrôle(s) passé(s) à « %s »." % (len(ids), a.nouveau))
        return
    if a.action == "ajouter":
        if not a.domaine or not a.controle:
            erreur("usage : couverture ajouter --domaine XXX --controle \"…\" [--jalon Jn] [--criticite …] [--preuve-attendue …]")
        dom = a.domaine.upper()[:3]
        nums = [int(l["id"][4:]) for l in lignes if l["id"].startswith(dom + "-") and l["id"][4:].isdigit()]
        nouveau = "%s-%03d" % (dom, max([899] + nums) + 1)
        lignes.append({"id": nouveau, "domaine": dom, "jalon": (a.jalon or config.get("jalon", "J3")).upper(),
                       "criticite": (liste_arg(a.criticite) or ["majeur"])[0], "controle": a.controle,
                       "preuve_attendue": a.preuve_attendue or "", "reference": "spécifique au projet",
                       "statut": "a-faire", "preuve": "", "note": "", "maj": aujourdhui()})
        ecrire_csv(chemin_couverture(dossier), COL_COUVERTURE, sorted(lignes, key=lambda l: (l["domaine"], l["id"])))
        print("Contrôle %s ajouté." % nouveau)
        return
    if a.action == "resync":
        if a.types:
            config["types"] = liste_arg(a.types)
        if a.tags is not None:
            config["tags"] = liste_arg(a.tags)
        accorder_etiquette_autonomie(config)
        ecrire_config(dossier, config)
        ajoutes, total = synchroniser_couverture(dossier, config)
        print("Matrice resynchronisée : %d contrôle(s) ajouté(s), %d au total." % (ajoutes, total))
        return
    erreur("action inconnue pour couverture : %s" % a.action)


# --------------------------------------------------------------------------- registres
def paires(arguments):
    res = {}
    for arg in arguments or []:
        if "=" not in arg:
            erreur("argument attendu au format cle=valeur, reçu « %s »" % arg)
        cle, valeur = arg.split("=", 1)
        res[cle.strip().lower()] = valeur.strip()
    return res


def cmd_registre(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    if a.type not in REGISTRES:
        erreur("registre inconnu « %s ». Registres : %s" % (a.type, ", ".join(REGISTRES)))
    prefixe, colonnes = REGISTRES[a.type]
    chemin = os.path.join(dossier, "00-pilotage", "registres", a.type + ".csv")
    lignes = lire_csv(chemin)
    donnees = normaliser(a.type, paires(a.champs))
    inconnus = [c for c in donnees if c not in colonnes]
    if inconnus:
        erreur("champ(s) inconnu(s) pour %s : %s. Champs : %s" % (a.type, ", ".join(inconnus), ", ".join(colonnes[1:])))
    if a.action == "ajouter":
        nums = [int(l["id"].split("-")[1]) for l in lignes if l["id"].split("-")[-1].isdigit()]
        ligne = {c: "" for c in colonnes}
        ligne.update(DEFAUTS.get(a.type, {}))
        ligne.update(donnees)
        ligne["id"] = "%s-%03d" % (prefixe, max([0] + nums) + 1)
        ligne["date"] = ligne.get("date") or aujourdhui()
        ligne["jalon"] = ligne.get("jalon") or config.get("jalon", "")
        if a.type == "risques":
            try:
                ligne["score"] = str(int(ligne.get("impact") or 0) * int(ligne.get("probabilite") or 0))
            except ValueError:
                erreur("impact et probabilite doivent être des entiers de 1 à 5.")
        lignes.append(ligne)
        ecrire_csv(chemin, colonnes, lignes)
        print("%s enregistré." % ligne["id"])
        return
    if a.action == "maj":
        if not a.id:
            erreur("usage : registre %s maj <ID> cle=valeur …" % a.type)
        cible = [l for l in lignes if l["id"] == a.id.upper()]
        if not cible:
            erreur("%s introuvable dans le registre %s." % (a.id, a.type))
        cible[0].update(donnees)
        if a.type == "risques":
            try:
                cible[0]["score"] = str(int(cible[0].get("impact") or 0) * int(cible[0].get("probabilite") or 0))
            except ValueError:
                pass
        ecrire_csv(chemin, colonnes, lignes)
        print("%s mis à jour." % a.id.upper())
        return
    if a.action == "liste":
        sel = [l for l in lignes if all(sans_accent(l.get(c, "")) == sans_accent(v) for c, v in donnees.items())]
        if a.ouverts:
            sel = [l for l in sel if l.get("statut") in OUVERTS[a.type]]
        principal = {"decisions": "titre", "risques": "titre", "constats": "constat",
                     "anomalies": "titre", "actions": "action", "changements": "titre"}[a.type]
        secondaire = {"decisions": "decision", "risques": "parade", "constats": "recommandation",
                      "anomalies": "description", "actions": "responsable", "changements": "impact"}[a.type]
        niveau = {"decisions": "type", "risques": "score", "constats": "gravite",
                  "anomalies": "severite", "actions": "echeance", "changements": "decision"}[a.type]
        for l in sel[: a.max]:
            print("%s [%s %s | %s] %s — %s" % (l["id"], l.get("jalon", ""), l.get(niveau, ""), l.get("statut", ""),
                                               court(l.get(principal, ""), 90), court(l.get(secondaire, ""), 90)))
        if len(sel) > a.max:
            print("… %d autres" % (len(sel) - a.max))
        print("%d entrée(s)." % len(sel))
        return
    erreur("action inconnue pour registre : %s" % a.action)


# --------------------------------------------------------------------------- journal des agents
def cmd_journal(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    chemin = os.path.join(dossier, "00-pilotage", "journal-agents.csv")
    lignes = lire_csv(chemin)
    if a.action == "ajouter":
        if not a.agent:
            erreur("usage : journal ajouter --agent <nom> [--modele m] [--tokens n] [--duree s] [--om ref]")
        lignes.append({"date": aujourdhui(), "jalon": config.get("jalon", ""), "vague": str(config.get("vague", "")),
                       "agent": a.agent, "modele": a.modele or "", "tokens": str(a.tokens or 0),
                       "duree_s": str(a.duree or 0), "om": a.om or "", "statut": a.statut_agent or "termine"})
        ecrire_csv(chemin, COL_JOURNAL, lignes)
        print("Journal : %s enregistré." % a.agent)
        try:
            plafond = int(float(config.get("plafond_tokens") or 0))
        except ValueError:
            plafond = 0
        if plafond:
            total = sum(int(float(l.get("tokens") or 0)) for l in lignes)
            part = round(100 * total / plafond)
            if part >= 100:
                print("PLAFOND ATTEINT : %d %% du plafond de tokens du projet. S'arrêter et rendre compte à l'utilisateur." % part)
            elif part >= 80:
                print("ALERTE : %d %% du plafond de tokens du projet consommés." % part)
        return
    if a.action == "bilan":
        if not lignes:
            print("Journal vide.")
            return

        def somme(cle):
            tot = {}
            for l in lignes:
                t = tot.setdefault(l.get(cle) or "?", [0, 0])
                t[0] += 1
                t[1] += int(float(l.get("tokens") or 0))
            return tot
        total = sum(int(float(l.get("tokens") or 0)) for l in lignes)
        print("Consommation : %d lancements d'agents, %s tokens" % (len(lignes), format(total, ",").replace(",", " ")))
        for titre, cle in (("Par jalon", "jalon"), ("Par modèle", "modele"), ("Par agent", "agent")):
            print(titre + " :")
            for nom, (n, tok) in sorted(somme(cle).items(), key=lambda kv: -kv[1][1])[:12]:
                print("  %s : %d lancement(s), %s tokens" % (nom, n, format(tok, ",").replace(",", " ")))
        return
    erreur("action inconnue pour journal : %s" % a.action)


# --------------------------------------------------------------------------- documents
RE_TITRE = re.compile(r"^#\s+(.+)$", re.M)


def documents_projet(dossier):
    res = []
    for racine, _, fichiers in os.walk(dossier):
        rel = os.path.relpath(racine, dossier).replace(os.sep, "/")
        if rel.startswith(("00-pilotage/registres", ".git", "node_modules", "code")) or "/journaux" in rel:
            continue
        if not re.match(r"^0[0-7]-", rel):
            continue
        for nom in sorted(fichiers):
            if nom.endswith(".md"):
                res.append(os.path.join(racine, nom))
    return sorted(res)


def synthese_de(texte):
    m = re.search(r"^##\s+Synth[èe]se\s*$", texte, re.M | re.I)
    if not m:
        return None
    reste = texte[m.end():]
    fin = re.search(r"^##?\s+", reste, re.M)
    bloc = reste[: fin.start()] if fin else reste
    lignes = [l.strip(" -*\t") for l in bloc.strip().splitlines() if l.strip()]
    return lignes[0] if lignes else ""


EXEMPTES = ("tableau-de-bord.md", "index-documents.md", "navigation.md", "fiche-projet.md", "organigramme.md")


def cmd_docs(a):
    dossier = trouver_dossier(a.dossier)
    docs = documents_projet(dossier)
    if a.action == "verifier":
        fautifs = []
        for chemin in docs:
            if os.path.basename(chemin) in EXEMPTES or "/reunions/" in chemin.replace(os.sep, "/") \
                    or "/sources/" in chemin.replace(os.sep, "/"):
                continue
            with open(chemin, encoding="utf-8", errors="replace") as f:
                tete = "".join(f.readlines()[:45])
            if synthese_de(tete) is None:
                fautifs.append(os.path.relpath(chemin, dossier))
        if fautifs:
            print("%d document(s) sans section « ## Synthèse » dans les 45 premières lignes :" % len(fautifs))
            for f_ in fautifs[:40]:
                print("  " + f_)
            sys.exit(1)
        print("Tous les documents (%d) commencent par une synthèse." % len(docs))
        return
    if a.action == "index":
        lignes = ["# Index des documents", "", "Généré par `cortex.py docs index` le %s. Ne pas modifier à la main." % aujourdhui(),
                  "", "| Document | Titre | Mots | Modifié | Synthèse (première ligne) |", "|---|---|---|---|---|"]
        for chemin in docs:
            if os.path.basename(chemin) == "index-documents.md":
                continue
            with open(chemin, encoding="utf-8", errors="replace") as f:
                texte = f.read()
            titre = RE_TITRE.search(texte)
            modif = _dt.date.fromtimestamp(os.path.getmtime(chemin)).isoformat()
            lignes.append("| %s | %s | %d | %s | %s |" % (
                os.path.relpath(chemin, dossier).replace(os.sep, "/"),
                court(titre.group(1) if titre else "(sans titre)", 60).replace("|", "/"),
                len(texte.split()), modif, court(synthese_de(texte) or "—", 140).replace("|", "/")))
        cible = os.path.join(dossier, "00-pilotage", "index-documents.md")
        with open(cible, "w", encoding="utf-8") as f:
            f.write("\n".join(lignes) + "\n")
        print("Index écrit : 00-pilotage/index-documents.md (%d documents)." % (len(lignes) - 6))
        return
    erreur("action inconnue pour docs : %s" % a.action)


# --------------------------------------------------------------------------- interactions
RE_EC = re.compile(r"\bEC-\d{3}\b")
RE_EL = re.compile(r"^EL-(\d{3})-\d{2,3}$")
ETATS_REQUIS = ["chargement", "erreur"]
TYPES_SANS_ETATS = ("modale", "statique", "externe", "confirmation", "dialogue")


def lire_interactions(base):
    ecrans, elements, doublons = {}, [], []
    fichiers = sorted(glob.glob(os.path.join(base, "**", "*.md"), recursive=True))
    for chemin in fichiers:
        if os.path.basename(chemin) == "navigation.md":
            continue
        with open(chemin, encoding="utf-8", errors="replace") as f:
            for n, ligne in enumerate(f, 1):
                c = cellules(ligne)
                if not c:
                    continue
                if re.match(r"^EC-\d{3}$", c[0]) and len(c) >= 7:
                    if c[0] in ecrans:
                        doublons.append(c[0])
                    ecrans[c[0]] = {"id": c[0], "nom": c[1], "type": sans_accent(c[2]), "roles": c[3],
                                    "entree": sans_accent(c[4]).startswith("oui"),
                                    "terminal": sans_accent(c[5]).startswith("oui"), "etats": sans_accent(c[6]),
                                    "source": "%s:%d" % (os.path.basename(chemin), n)}
                elif RE_EL.match(c[0]) and len(c) >= 7:
                    if any(e["id"] == c[0] for e in elements):
                        doublons.append(c[0])
                    elements.append({"id": c[0], "ecran": "EC-" + RE_EL.match(c[0]).group(1), "element": c[1],
                                     "type": c[2], "action": c[3], "conditions": c[4], "reaction": c[5],
                                     "destination": c[6], "erreurs": c[7] if len(c) > 7 else "",
                                     "workflow": c[8] if len(c) > 8 else "",
                                     "source": "%s:%d" % (os.path.basename(chemin), n)})
    return ecrans, elements, doublons


def analyser_interactions(ecrans, elements, doublons):
    erreurs, alertes = [], []
    vide = ("", "-", "—", "?", "tbd", "a definir", "à définir")
    if not ecrans:
        erreurs.append("aucun écran (lignes « | EC-001 | … ») trouvé")
        return erreurs, alertes
    for d in sorted(set(doublons)):
        erreurs.append("identifiant en double : %s" % d)
    sortants = {e: set() for e in ecrans}
    entrants = {e: 0 for e in ecrans}
    nb_elements = {e: 0 for e in ecrans}
    for el in elements:
        if el["ecran"] not in ecrans:
            erreurs.append("%s rattaché à un écran non défini (%s) [%s]" % (el["id"], el["ecran"], el["source"]))
            continue
        nb_elements[el["ecran"]] += 1
        if sans_accent(el["reaction"]) in vide:
            erreurs.append("%s « %s » : réaction du système non décrite [%s]" % (el["id"], court(el["element"], 40), el["source"]))
        if sans_accent(el["destination"]) in vide:
            erreurs.append("%s « %s » : destination non décrite [%s]" % (el["id"], court(el["element"], 40), el["source"]))
        for cible in RE_EC.findall(el["destination"]):
            if cible not in ecrans:
                erreurs.append("%s mène à %s, écran non défini [%s]" % (el["id"], cible, el["source"]))
            else:
                if cible != el["ecran"]:
                    entrants[cible] += 1
                sortants[el["ecran"]].add(cible)
        if sans_accent(el["workflow"]) in vide:
            alertes.append("%s sans workflow de rattachement" % el["id"])
    entrees = [e for e, v in ecrans.items() if v["entree"]]
    if not entrees:
        erreurs.append("aucun écran marqué comme point d'entrée (colonne Entrée = oui)")
    for e, v in sorted(ecrans.items()):
        if nb_elements[e] == 0 and not v["terminal"]:
            erreurs.append("%s « %s » : cul-de-sac (aucun élément interactif et non terminal)" % (e, v["nom"]))
        if not v["entree"] and entrants[e] == 0:
            erreurs.append("%s « %s » : écran orphelin (aucune interaction n'y mène)" % (e, v["nom"]))
        if v["etats"] not in ("n/a", "na", "-", "sans objet") and not any(t in v["type"] for t in TYPES_SANS_ETATS):
            manquants = [x for x in ETATS_REQUIS if x not in v["etats"]]
            if manquants:
                alertes.append("%s « %s » : état(s) non spécifié(s) : %s" % (e, v["nom"], ", ".join(manquants)))
    atteints, pile = set(entrees), list(entrees)
    while pile:
        for suivant in sortants.get(pile.pop(), ()):
            if suivant not in atteints:
                atteints.add(suivant)
                pile.append(suivant)
    for e in sorted(set(ecrans) - atteints):
        if entrants[e] > 0:
            erreurs.append("%s « %s » : inatteignable depuis les points d'entrée" % (e, ecrans[e]["nom"]))
    return erreurs, alertes


def base_interactions(dossier, chemin):
    return os.path.abspath(chemin) if chemin else os.path.join(dossier, "03-conception", "design", "interactions")


def cmd_interactions(a):
    dossier = trouver_dossier(a.dossier)
    base = base_interactions(dossier, a.chemin)
    ecrans, elements, doublons = lire_interactions(base)
    if a.action == "verifier":
        erreurs, alertes = analyser_interactions(ecrans, elements, doublons)
        print("Interactions : %d écran(s), %d élément(s) interactif(s)." % (len(ecrans), len(elements)))
        for titre, liste in (("ERREURS", erreurs), ("ALERTES", alertes)):
            if liste:
                print("%s (%d) :" % (titre, len(liste)))
                for l in liste[: a.max]:
                    print("  - " + l)
                if len(liste) > a.max:
                    print("  … %d autres" % (len(liste) - a.max))
        if erreurs:
            sys.exit(1)
        print("Aucun cul-de-sac, aucun écran orphelin, aucune destination indéfinie.")
        return
    if a.action == "graphe":
        if not ecrans:
            erreur("aucun écran trouvé dans %s" % base)
        lignes = ["# Carte de navigation", "", "Générée par `cortex.py interactions graphe` le %s." % aujourdhui(), "",
                  "```mermaid", "flowchart LR"]
        for e, v in sorted(ecrans.items()):
            nom = v["nom"].replace('"', "'")
            forme = '%s(["%s<br/>%s"])' if v["entree"] else ('%s[["%s<br/>%s"]]' if v["terminal"] else '%s["%s<br/>%s"]')
            lignes.append("  " + forme % (e.replace("-", ""), e, nom))
        vus = set()
        for el in elements:
            for cible in RE_EC.findall(el["destination"]):
                if cible in ecrans and el["ecran"] in ecrans and cible != el["ecran"]:
                    etiquette = court(el["element"], 28).replace('"', "'").replace("|", "/")
                    cle = (el["ecran"], cible, etiquette)
                    if cle not in vus:
                        vus.add(cle)
                        lignes.append('  %s -->|"%s"| %s' % (el["ecran"].replace("-", ""), etiquette, cible.replace("-", "")))
        lignes += ["```", ""]
        cible = os.path.join(base, "navigation.md")
        with open(cible, "w", encoding="utf-8") as f:
            f.write("\n".join(lignes))
        print("Carte de navigation écrite : %s (%d écrans, %d transitions)." % (os.path.relpath(cible, dossier), len(ecrans), len(vus)))
        return
    erreur("action inconnue pour interactions : %s" % a.action)


# --------------------------------------------------------------------------- traçabilité
GENRES = ["EXNF", "EX", "FN", "RG", "WF", "CT"]
RE_REF = re.compile(r"\b(EXNF|EX|FN|RG|WF|CT)-\d{3,4}\b")
AVAL = {"EX": ["FN", "RG", "WF"], "FN": ["RG", "WF"], "RG": ["CT"], "WF": ["CT"], "EXNF": ["CT"]}
LIBELLE = {"EX": "exigence fonctionnelle", "EXNF": "exigence non fonctionnelle", "FN": "fonction",
           "RG": "règle de gestion", "WF": "workflow", "CT": "cas de test"}


def analyser_tracabilite(dossier):
    """Relève où chaque identifiant est défini (première cellule d'une ligne de tableau, ou titre de section)
    et à quels autres identifiants il est relié (même ligne, ou corps de la section qu'il titre)."""
    definis, liens, references = {}, {}, {}
    for chemin in documents_projet(dossier):
        rel = os.path.relpath(chemin, dossier).replace(os.sep, "/")
        if not rel.startswith(("02-", "03-", "05-")):
            continue
        portee = None  # (identifiant, niveau du titre)
        with open(chemin, encoding="utf-8", errors="replace") as f:
            for n, ligne in enumerate(f, 1):
                titre = re.match(r"^(#{1,6})\s+(.*)$", ligne)
                if titre:
                    niveau = len(titre.group(1))
                    if portee and niveau <= portee[1]:
                        portee = None
                    m = re.match(r"^((?:EXNF|EX|FN|RG|WF|CT)-\d{3,4})\b", titre.group(2))
                    if m:
                        portee = (m.group(1), niveau)
                        definis.setdefault(m.group(1), "%s:%d" % (rel, n))
                refs = [m.group(0) for m in RE_REF.finditer(ligne)]
                if not refs:
                    continue
                c = cellules(ligne)
                if c and RE_REF.fullmatch(c[0] or ""):
                    definis.setdefault(c[0], "%s:%d" % (rel, n))
                    for r in refs:
                        if r != c[0]:
                            liens.setdefault(c[0], set()).add(r)
                if portee:
                    for r in refs:
                        if r != portee[0]:
                            liens.setdefault(portee[0], set()).add(r)
                for r in refs:
                    references.setdefault(r, "%s:%d" % (rel, n))
    return definis, liens, references


def genre(identifiant):
    return identifiant.split("-")[0]


def cmd_tracabilite(a):
    dossier = trouver_dossier(a.dossier)
    definis, liens, references = analyser_tracabilite(dossier)
    if not definis:
        print("Aucun identifiant tracé (EX-, FN-, RG-, WF-, CT-) trouvé : rien à vérifier pour l'instant.")
        return
    compte = {g: sum(1 for d in definis if genre(d) == g) for g in GENRES}
    print("Traçabilité : " + ", ".join("%d %s" % (compte[g], g) for g in GENRES if compte[g]))
    couverts = {}
    for tete, cibles in liens.items():
        for cible in cibles:
            couverts.setdefault(cible, set()).add(genre(tete))
    erreurs, alertes = [], []
    for amont, avals in AVAL.items():
        if not any(compte[x] for x in avals):
            continue  # l'étage aval n'existe pas encore : pas d'erreur à ce stade
        manquants = sorted(d for d in definis if genre(d) == amont and not (couverts.get(d, set()) & set(avals)))
        if manquants:
            msg = "%d %s sans %s : %s" % (len(manquants), LIBELLE[amont] + ("s" if len(manquants) > 1 else ""),
                                          " ni ".join(LIBELLE[x] for x in avals), ", ".join(manquants[: a.max]))
            (alertes if amont == "EXNF" else erreurs).append(msg + (" …" if len(manquants) > a.max else ""))
    ecrans, elements, _ = lire_interactions(base_interactions(dossier, None))
    if elements and compte["CT"]:
        cites_el, cites_wf = set(), set()
        for tete, cibles in liens.items():
            if genre(tete) == "CT":
                cites_wf |= {c for c in cibles if genre(c) == "WF"}
        for chemin in documents_projet(dossier):
            with open(chemin, encoding="utf-8", errors="replace") as f:
                for ligne in f:
                    c = cellules(ligne)
                    if c and re.fullmatch(r"CT-\d{3,4}", c[0] or ""):
                        cites_el |= set(re.findall(r"EL-\d{3}-\d{2,3}", ligne))
        non_couverts = sorted(el["id"] for el in elements
                              if el["id"] not in cites_el and not (set(RE_REF.findall(el["workflow"])) and
                                                                   {m.group(0) for m in RE_REF.finditer(el["workflow"])} & cites_wf))
        if non_couverts:
            alertes.append("%d élément(s) interactif(s) dont ni l'identifiant ni le workflow n'est couvert par un cas de test : %s%s"
                           % (len(non_couverts), ", ".join(non_couverts[: a.max]), " …" if len(non_couverts) > a.max else ""))
    fantomes = sorted(r for r in references if r not in definis)
    if fantomes:
        erreurs.append("%d identifiant(s) cité(s) mais jamais défini(s) : %s%s"
                       % (len(fantomes), ", ".join(fantomes[: a.max]), " …" if len(fantomes) > a.max else ""))
    for titre, liste in (("ERREURS", erreurs), ("ALERTES", alertes)):
        if liste:
            print("%s :" % titre)
            for l in liste:
                print("  - " + l)
    if erreurs:
        sys.exit(1)
    print("Chaîne exigences → fonctions → règles et workflows → cas de test : complète.")


# --------------------------------------------------------------------------- jalons
def charger_jalons():
    if not os.path.isfile(JALONS_JSON):
        return {}
    with open(JALONS_JSON, encoding="utf-8") as f:
        return json.load(f)


def exigence_applicable(ex, config):
    if ex.get("modes") and config["mode"] not in ex["modes"]:
        return False
    if ex.get("types") and not set(ex["types"]) & set(config["types"]):
        return False
    if ex.get("tags") and not set(ex["tags"]) & set(config["tags"]):
        return False
    return True


def document_present(dossier, motif):
    for chemin in glob.glob(os.path.join(dossier, motif), recursive=True):
        if os.path.isfile(chemin) and os.path.getsize(chemin) > 300:
            return True
    return False


def manques_jalon(dossier, config, jalon):
    bloquants, alertes = [], []
    definition = charger_jalons().get(jalon, {})
    for ex in definition.get("documents", []):
        if exigence_applicable(ex, config) and not document_present(dossier, ex["chemin"]):
            bloquants.append("document manquant ou quasi vide : %s" % ex["chemin"])
    lignes = lire_csv(chemin_couverture(dossier))
    for l in lignes:
        if rang_jalon(l["jalon"]) > rang_jalon(jalon) or l["statut"] in CLOS:
            continue
        msg = "contrôle %s (%s) non traité : %s" % (l["id"], l["criticite"], court(l["controle"], 90))
        if l["criticite"] == "bloquant" or (l["criticite"] == "majeur" and config["mode"] != "eclair"):
            bloquants.append(msg)
        else:
            alertes.append(msg)
    reg = os.path.join(dossier, "00-pilotage", "registres")
    for l in lire_csv(os.path.join(reg, "constats.csv")):
        if l.get("statut") in OUVERTS["constats"] and sans_accent(l.get("gravite", "")).startswith("bloquant"):
            bloquants.append("constat bloquant ouvert %s : %s" % (l["id"], court(l.get("constat", ""), 90)))
    for l in lire_csv(os.path.join(reg, "decisions.csv")):
        if l.get("statut") == "a-valider" and l.get("type") == "1":
            bloquants.append("décision de type 1 à valider par l'utilisateur : %s %s" % (l["id"], court(l.get("titre", ""), 80)))
    if rang_jalon(jalon) >= rang_jalon("J4"):
        for l in lire_csv(os.path.join(reg, "anomalies.csv")):
            if l.get("statut") == "ouverte" and sans_accent(l.get("severite", "")).startswith("bloquant"):
                bloquants.append("anomalie bloquante ouverte %s : %s" % (l["id"], court(l.get("titre", ""), 80)))
    if "interactions" in definition.get("controles", []):
        ecrans, elements, doublons = lire_interactions(base_interactions(dossier, None))
        erreurs, _ = analyser_interactions(ecrans, elements, doublons)
        if erreurs:
            bloquants.append("matrice d'interactions : %d erreur(s) (lancer « interactions verifier »)" % len(erreurs))
    return bloquants, alertes


def cmd_jalon(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    jalon = (a.jalon or config.get("jalon") or "J1").upper()
    if jalon not in JALONS:
        erreur("jalon inconnu « %s » (J1 à J7)" % jalon)
    bloquants, alertes = manques_jalon(dossier, config, jalon)
    if a.action == "verifier":
        if bloquants:
            print("JALON %s : NON FRANCHISSABLE — %d manque(s) bloquant(s)" % (jalon, len(bloquants)))
            for b in bloquants[: a.max]:
                print("  - " + b)
            if len(bloquants) > a.max:
                print("  … %d autres" % (len(bloquants) - a.max))
        else:
            print("JALON %s : FRANCHISSABLE" % jalon)
        if alertes:
            print("%d point(s) non bloquant(s) restant(s) (couverture liste --jalon %s --statut a-faire)." % (len(alertes), jalon))
        sys.exit(2 if bloquants else 0)
    if a.action == "franchir":
        if bloquants and not a.force:
            erreur("jalon %s non franchissable (%d manque(s) bloquant(s)). Corriger, ou passer en force avec "
                   "--force \"motif et nom de celui qui décide\"." % (jalon, len(bloquants)))
        config.setdefault("jalons_franchis", []).append(
            {"jalon": jalon, "date": aujourdhui(), "force": a.force or "", "manques": len(bloquants)})
        suivant = JALONS[min(JALONS.index(jalon) + 1, len(JALONS) - 1)]
        config["jalon"], config["vague"] = suivant, 0
        ecrire_config(dossier, config)
        print("Jalon %s franchi%s. Jalon courant : %s." % (jalon, " en force" if a.force and bloquants else "", suivant))
        return
    erreur("action inconnue pour jalon : %s" % a.action)


# --------------------------------------------------------------------------- état et tableau de bord
def resume_etat(dossier, config):
    lignes = lire_csv(chemin_couverture(dossier))
    clos = sum(1 for l in lignes if l["statut"] in CLOS)
    reg = os.path.join(dossier, "00-pilotage", "registres")
    ouverts = {nom: [l for l in lire_csv(os.path.join(reg, nom + ".csv")) if l.get("statut") in OUVERTS[nom]]
               for nom in REGISTRES}
    journal = lire_csv(os.path.join(dossier, "00-pilotage", "journal-agents.csv"))
    tokens = sum(int(float(l.get("tokens") or 0)) for l in journal)
    return lignes, clos, ouverts, journal, tokens


def cmd_etat(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    modifs = paires(a.set)
    if modifs:
        for cle, valeur in modifs.items():
            if cle == "jalon":
                valeur = valeur.upper()
                if valeur not in JALONS:
                    erreur("jalon inconnu « %s »" % valeur)
            if cle == "vague":
                valeur = int(valeur)
            if cle == "mode" and valeur not in MODES:
                erreur("mode inconnu « %s »" % valeur)
            if cle == "autonomie" and valeur not in AUTONOMIES:
                erreur("autonomie inconnue « %s ». Niveaux possibles : %s" % (valeur, ", ".join(AUTONOMIES)))
            if cle == "perimetre":
                valeur = valeur.upper()
                if valeur not in JALONS:
                    erreur("périmètre inconnu « %s »" % valeur)
            config[cle] = valeur
        etiquettes_changees = accorder_etiquette_autonomie(config)
        ecrire_config(dossier, config)
        if etiquettes_changees:
            ajoutes, _ = synchroniser_couverture(dossier, config)
            print("Étiquette « autonome » mise à jour : %d contrôle(s) ajouté(s) à la couverture." % ajoutes)
    lignes, clos, ouverts, journal, tokens = resume_etat(dossier, config)
    jalon = config.get("jalon", "J0")
    print("Projet : %s | types : %s | étiquettes : %s | mode : %s | périmètre : %s | autonomie : %s"
          % (config["nom"], ", ".join(config["types"]), ", ".join(config["tags"]) or "aucune", config["mode"],
             config.get("perimetre", "J7"), config.get("autonomie", "accompagne")))
    print("Dossier : %s" % dossier)
    print("Jalon courant : %s | vague : %s | jalons franchis : %s"
          % (jalon, config.get("vague", 0), ", ".join(j["jalon"] for j in config.get("jalons_franchis", [])) or "aucun"))
    if config.get("note"):
        print("Note de reprise : %s" % config["note"])
    if lignes:
        print("Couverture : %d/%d contrôles traités (%d %%)" % (clos, len(lignes), round(100 * clos / len(lignes))))
    reste = hors_matrice(config)
    if reste:
        print("Hors matrice (mode %s, périmètre %s) : %d contrôles applicables non examinés."
              % (config["mode"], config.get("perimetre", "J7"), len(reste)))
    cible = jalon if jalon != "J0" else "J1"
    bloquants, alertes = manques_jalon(dossier, config, cible)
    print("Vers le jalon %s : %d manque(s) bloquant(s), %d point(s) non bloquant(s)." % (cible, len(bloquants), len(alertes)))
    for b in bloquants[:8]:
        print("  - " + b)
    if len(bloquants) > 8:
        print("  … %d autres (jalon verifier %s)" % (len(bloquants) - 8, cible))
    print("Ouverts : %s" % ", ".join("%d %s" % (len(v), k) for k, v in ouverts.items()))
    provisoires = [l for l in lire_csv(os.path.join(dossier, "00-pilotage", "registres", "decisions.csv"))
                   if l.get("statut") == "provisoire"]
    if provisoires:
        print("Décisions provisoires à confirmer par l'utilisateur : %s"
              % ", ".join("%s %s" % (l["id"], court(l.get("titre", ""), 50)) for l in provisoires[:6]))
    for act in ouverts["actions"][:6]:
        print("  action %s : %s (%s)" % (act["id"], court(act.get("action", ""), 90), act.get("responsable", "")))
    print("Agents lancés : %d | tokens journalisés : %s" % (len(journal), format(tokens, ",").replace(",", " ")))


def cmd_tableau(a):
    dossier = trouver_dossier(a.dossier)
    config = lire_config(dossier)
    lignes, clos, ouverts, journal, tokens = resume_etat(dossier, config)
    jalon = config.get("jalon", "J0")
    out = ["# Tableau de bord — %s" % config["nom"], "",
           "Généré par `cortex.py tableau-de-bord` le %s." % aujourdhui(), "",
           "| | |", "|---|---|",
           "| Types | %s |" % ", ".join(config["types"]),
           "| Étiquettes | %s |" % (", ".join(config["tags"]) or "aucune"),
           "| Mode | %s |" % config["mode"],
           "| Jalon courant | %s (vague %s) |" % (jalon, config.get("vague", 0)),
           "| Jalons franchis | %s |" % (", ".join("%s le %s" % (j["jalon"], j["date"]) for j in config.get("jalons_franchis", [])) or "aucun"),
           "| Couverture | %d/%d contrôles traités |" % (clos, len(lignes)),
           "| Agents lancés | %d, %s tokens journalisés |" % (len(journal), format(tokens, ",").replace(",", " ")),
           "", "## Couverture par domaine", "", "| Domaine | Traités | Total | Bloquants restants |", "|---|---|---|---|"]
    par = {}
    for l in lignes:
        d = par.setdefault(l["domaine"], [0, 0, 0])
        d[1] += 1
        if l["statut"] in CLOS:
            d[0] += 1
        elif l["criticite"] == "bloquant":
            d[2] += 1
    for dom in sorted(par):
        out.append("| %s | %d | %d | %d |" % (dom, par[dom][0], par[dom][1], par[dom][2]))
    cible = jalon if jalon != "J0" else "J1"
    bloquants, _ = manques_jalon(dossier, config, cible)
    out += ["", "## Manques bloquants vers %s" % cible, ""]
    out += ["- " + b for b in bloquants[:30]] or ["Aucun."]
    titres = {"decisions": ("Décisions à valider", "titre"), "risques": ("Risques ouverts", "titre"),
              "constats": ("Constats d'audit ouverts", "constat"), "anomalies": ("Anomalies ouvertes", "titre"),
              "actions": ("Actions ouvertes", "action"),
              "changements": ("Demandes de changement ouvertes", "titre")}
    for nom, (titre, champ) in titres.items():
        out += ["", "## %s (%d)" % (titre, len(ouverts[nom])), ""]
        tri = ouverts[nom]
        if nom == "risques":
            tri = sorted(tri, key=lambda l: -int(l.get("score") or 0))
        out += ["- %s — %s" % (l["id"], court(l.get(champ, ""), 140)) for l in tri[:15]] or ["Aucun."]
    chemin = os.path.join(dossier, "00-pilotage", "tableau-de-bord.md")
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("Tableau de bord écrit : 00-pilotage/tableau-de-bord.md")


# --------------------------------------------------------------------------- contrôle du plugin
def cmd_plugin(a):
    items = charger_checklists()
    erreurs = []
    for it in items:
        if it.get("doublon"):
            erreurs.append("%s en double (%s:%d et %s)" % (it["id"], it["source"], it["ligne"], it["doublon"]))
        if it["jalon"] not in JALONS[1:]:
            erreurs.append("%s : jalon invalide « %s » (%s:%d)" % (it["id"], it["jalon"], it["source"], it["ligne"]))
        if it["criticite"] not in CRITICITES:
            erreurs.append("%s : criticité invalide « %s » (%s:%d)" % (it["id"], it["criticite"], it["source"], it["ligne"]))
        if it["types"] not in ("tous",) and not set(liste_arg(it["types"])) <= set(TYPES):
            erreurs.append("%s : type(s) invalide(s) « %s » (%s:%d)" % (it["id"], it["types"], it["source"], it["ligne"]))
        if len(it["controle"]) < 15:
            erreurs.append("%s : contrôle trop court (%s:%d)" % (it["id"], it["source"], it["ligne"]))
    par = {}
    for it in items:
        par[it["domaine"]] = par.get(it["domaine"], 0) + 1
    print("Checklists du plugin : %d contrôles — %s" % (len(items), ", ".join("%s %d" % kv for kv in sorted(par.items()))))
    if a.etiquettes:
        tags = {}
        for it in items:
            for alt in it["conditions"].split(","):
                for t in alt.split("+"):
                    if t.strip() and t.strip() not in ("-",):
                        tags[t.strip()] = tags.get(t.strip(), 0) + 1
        print("Étiquettes utilisées : " + ", ".join("%s (%d)" % kv for kv in sorted(tags.items())))
    if erreurs:
        print("ERREURS (%d) :" % len(erreurs))
        for e in erreurs[:60]:
            print("  - " + e)
        sys.exit(1)
    print("Format des checklists : correct.")


# --------------------------------------------------------------------------- interface
AIDE = """Dan-Cortex — commandes
  init --dossier D --nom "N" --types t1,t2 [--tags a,b] [--mode eclair|standard|integral] [--perimetre Jn]
       [--autonomie accompagne|delegue|autonome]
  etat [--set cle=valeur …]                      état du projet et prochains manques (jalon, vague, note, mode,
                                                 autonomie)
  tableau-de-bord                                écrit 00-pilotage/tableau-de-bord.md
  couverture stats|liste [--domaine X] [--jalon Jn] [--statut s] [--criticite c] [--court] [--max N]
  couverture maj ID[,ID] --nouveau fait|non-applicable|risque-accepte|en-cours [--preuve P] [--note N]
  couverture ajouter --domaine XXX --controle "…" [--jalon Jn] [--criticite c] [--preuve-attendue "…"]
  couverture resync [--types …] [--tags …]
  registre decisions|risques|constats|anomalies|actions|changements ajouter cle=valeur …
  registre <type> maj ID cle=valeur …   |   registre <type> liste [cle=valeur] [--ouverts] [--max N]
  journal ajouter --agent A [--modele M] [--tokens N] [--duree S] [--om REF]   |   journal bilan
  docs verifier | docs index
  interactions verifier|graphe [--chemin dossier]
  tracabilite verifier
  jalon verifier|franchir [Jn] [--force "motif"]
  plugin verifier [--etiquettes]                 contrôle le format des checklists du plugin
Toutes les commandes acceptent --dossier (par défaut : le dossier courant ou l'un de ses parents)."""


def main():
    p = argparse.ArgumentParser(prog="cortex.py", add_help=True, description="Pilotage d'un dossier projet Dan-Cortex")
    sp = p.add_subparsers(dest="commande")

    def commun(parser):
        parser.add_argument("--dossier", default=None)
        parser.add_argument("--max", type=int, default=40)

    s = sp.add_parser("aide")
    s = sp.add_parser("init")
    s.add_argument("--dossier", required=True)
    s.add_argument("--nom", required=True)
    s.add_argument("--types", required=True)
    s.add_argument("--tags", default="")
    s.add_argument("--mode", default="standard")
    s.add_argument("--perimetre", default="J7")
    s.add_argument("--autonomie", default="accompagne")
    s.add_argument("--force", action="store_true")
    s = sp.add_parser("etat")
    commun(s)
    s.add_argument("--set", nargs="*", default=[])
    s = sp.add_parser("tableau-de-bord")
    commun(s)
    s = sp.add_parser("couverture")
    s.add_argument("action", choices=["stats", "liste", "maj", "ajouter", "resync"])
    s.add_argument("ids", nargs="?")
    commun(s)
    s.add_argument("--domaine")
    s.add_argument("--jalon")
    s.add_argument("--statut")
    s.add_argument("--criticite")
    s.add_argument("--court", action="store_true")
    s.add_argument("--nouveau")
    s.add_argument("--preuve")
    s.add_argument("--note")
    s.add_argument("--controle")
    s.add_argument("--preuve-attendue", dest="preuve_attendue")
    s.add_argument("--types")
    s.add_argument("--tags")
    s = sp.add_parser("registre")
    s.add_argument("type")
    s.add_argument("action", choices=["ajouter", "maj", "liste"])
    s.add_argument("champs", nargs="*")
    commun(s)
    s.add_argument("--ouverts", action="store_true")
    s = sp.add_parser("journal")
    s.add_argument("action", choices=["ajouter", "bilan"])
    commun(s)
    s.add_argument("--agent")
    s.add_argument("--modele")
    s.add_argument("--tokens", type=float)
    s.add_argument("--duree", type=float)
    s.add_argument("--om")
    s.add_argument("--statut-agent", dest="statut_agent")
    s = sp.add_parser("docs")
    s.add_argument("action", choices=["verifier", "index"])
    commun(s)
    s = sp.add_parser("interactions")
    s.add_argument("action", choices=["verifier", "graphe"])
    commun(s)
    s.add_argument("--chemin")
    s = sp.add_parser("tracabilite")
    s.add_argument("action", choices=["verifier"])
    commun(s)
    s = sp.add_parser("jalon")
    s.add_argument("action", choices=["verifier", "franchir"])
    s.add_argument("jalon", nargs="?")
    commun(s)
    s.add_argument("--force")
    s = sp.add_parser("plugin")
    s.add_argument("action", choices=["verifier"])
    s.add_argument("--etiquettes", action="store_true")

    a, reste = p.parse_known_args()
    if a.commande == "registre":
        # Avant Python 3.13, argparse écarte les champs cle=valeur placés après une option
        # (« registre decisions ajouter --dossier D titre=… ») : on les rend aux champs, dans l'ordre.
        a.champs += [x for x in reste if not x.startswith("-")]
        reste = [x for x in reste if x.startswith("-")]
    if reste:
        p.error("arguments non reconnus : %s" % " ".join(reste))
    if a.commande in (None, "aide"):
        print(AIDE)
        return
    if a.commande == "registre" and a.action == "maj":
        if not a.champs:
            erreur("usage : registre <type> maj <ID> cle=valeur …")
        a.id, a.champs = a.champs[0], a.champs[1:]
    {"init": cmd_init, "etat": cmd_etat, "tableau-de-bord": cmd_tableau, "couverture": cmd_couverture,
     "registre": cmd_registre, "journal": cmd_journal, "docs": cmd_docs, "interactions": cmd_interactions,
     "tracabilite": cmd_tracabilite, "jalon": cmd_jalon, "plugin": cmd_plugin}[a.commande](a)


if __name__ == "__main__":
    main()
