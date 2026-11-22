"""Les documents racontent le même plugin que ses fichiers : version, compteurs, renvois, fiches d'agents.

Chaque test vise une classe d'écart relevée par l'audit du 22/11/2026 (docs/audit-coherence-2026-11-22.md).
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "dan-cortex"
BIBLIOTHEQUE = PLUGIN / "bibliotheque"
# Copies fidèles d'anthropics/skills : leur texte ne se modifie pas, il est hors périmètre.
COPIES_ANTHROPIC = {"academy-guide", "algorithmic-art", "brand-guidelines", "claude-api", "docx", "mcp-builder",
                    "pdf", "pptx", "skill-creator", "slack-gif-creator", "web-artifacts-builder",
                    "webapp-testing", "xlsx"}


def lire(chemin):
    return chemin.read_text(encoding="utf-8")


def entete(chemin):
    """En-tête YAML simple d'une fiche : scalaires et listes (« - x » ou « [x, y] »)."""
    valeurs, cle = {}, None
    for ligne in lire(chemin).split("\n---", 1)[0].splitlines()[1:]:
        m = re.match(r"^([A-Za-z]+):\s*(.*)$", ligne)
        if m:
            cle, val = m.groups()
            if val.startswith("["):
                val = [x.strip().strip('"') for x in val[1:-1].split(",") if x.strip()]
            valeurs[cle] = val if val else []
        elif ligne.startswith("- ") and cle:
            valeurs[cle].append(ligne[2:].strip().strip('"'))
    return valeurs


def fichiers_maison():
    """Markdown écrits pour Dan-Cortex dans le plugin (ni bibliothèque, ni copies d'Anthropic)."""
    for f in sorted(PLUGIN.rglob("*.md")):
        parties = f.relative_to(PLUGIN).parts
        if parties[0] == "bibliotheque" or (parties[0] == "skills" and parties[1] in COPIES_ANTHROPIC):
            continue
        yield f


class VersionTests(unittest.TestCase):
    def test_resume_anglais_a_la_bonne_version(self):
        version = json.loads(lire(PLUGIN / ".claude-plugin" / "plugin.json"))["version"]
        anglais = lire(ROOT / "README.md").split("## In English", 1)[1]
        self.assertEqual(re.findall(r"current: (\d+\.\d+\.\d+)", anglais), [version])

    def test_publier_une_version_cite_les_cinq_endroits(self):
        section = lire(ROOT / "CONTRIBUTING.md").split("## 7.", 1)[1]
        for endroit in ("plugin.json", "marketplace.json", "pyproject.toml", "CHANGELOG.md", "badge"):
            self.assertIn(endroit, section)


class BibliothequeTests(unittest.TestCase):
    def setUp(self):
        self.total = len(list(BIBLIOTHEQUE.rglob("SKILL.md")))
        self.sources = sorted(p.name for p in BIBLIOTHEQUE.iterdir() if p.is_dir())

    def test_compteur_de_la_bibliotheque_partout_le_meme(self):
        motif = re.compile(r"\b(\d+) (?:compétences tierces|compétences vendorisées|skills tiers|skills vendorisés"
                           r"|vendored third-party skills)\b|\| Skills vendorisés[^|]*\| (\d+) \|"
                           r"|bibliothèque de <strong>(\d+) compétences</strong>|utilise (\d+) compétences"
                           r"|Y ranger (\d+) compétences")
        documents = [ROOT / "README.md", ROOT / "AGENTS.md", PLUGIN / "README.md",
                     PLUGIN / ".claude-plugin" / "plugin.json", ROOT / "docs" / "architecture.md",
                     ROOT / "docs" / "bibliotheque.md", ROOT / "docs" / "images" / "carte-depot.svg",
                     ROOT / "docs" / "images" / "chargement-a-la-demande.svg"]
        vus = 0
        for doc in documents:
            for groupes in motif.findall(lire(doc)):
                n = int(next(g for g in groupes if g))
                vus += 1
                with self.subTest(document=doc.relative_to(ROOT).as_posix()):
                    self.assertEqual(n, self.total)
        self.assertGreater(vus, 6, "le contrôle du compteur de la bibliothèque ne voit presque rien")

    def test_chaque_source_a_licence_et_notice(self):
        for source in self.sources:
            with self.subTest(source=source):
                self.assertTrue((BIBLIOTHEQUE / source / "LICENSE").is_file())
                self.assertTrue((BIBLIOTHEQUE / source / "NOTICE.md").is_file())

    def test_licence_annoncee_conforme_au_fichier(self):
        index = lire(BIBLIOTHEQUE / "README.md")
        for source in self.sources:
            licence = lire(BIBLIOTHEQUE / source / "LICENSE")
            attendu = "Apache-2.0" if "Apache License" in licence else "MIT" if "MIT License" in licence else None
            ligne = next(l for l in index.splitlines() if l.startswith("| `%s/`" % source))
            with self.subTest(source=source):
                self.assertIsNotNone(attendu)
                self.assertIn(attendu, ligne.rsplit("|", 2)[-2])
                self.assertIn(attendu, lire(BIBLIOTHEQUE / source / "NOTICE.md"))

    def test_chaque_pivot_dans_l_architecture(self):
        index = lire(BIBLIOTHEQUE / "README.md")
        pivots = set(re.findall(r"`([a-z0-9-]+)`", "".join(l.split("|")[3] for l in index.splitlines()
                                                          if l.startswith("| `"))))
        section = lire(ROOT / "docs" / "architecture.md").split("La bibliothèque à la demande", 1)[1]
        self.assertTrue(pivots)
        for pivot in pivots:
            with self.subTest(pivot=pivot):
                self.assertTrue((PLUGIN / "skills" / pivot / "SKILL.md").is_file())
                self.assertIn("| `%s` |" % pivot, section)


class InventaireTests(unittest.TestCase):
    def test_inventaire_du_plugin(self):
        texte = lire(PLUGIN / "README.md")
        references = [p for p in PLUGIN.glob("skills/*/*/**/*")
                      if p.is_file() and p.relative_to(PLUGIN).parts[2] in ("references", "assets")]
        scripts = [p for p in PLUGIN.glob("skills/*/scripts/**/*")
                   if p.is_file() and "__pycache__" not in p.parts
                   and p.relative_to(PLUGIN).parts[1] not in COPIES_ANTHROPIC]
        self.assertIn("| Fichiers de référence et gabarits | %d |" % len(references), texte)
        self.assertIn("| Scripts maison | %d |" % len(scripts), texte)

    def test_carte_du_depot_compte_les_skills(self):
        skills = len([p for p in (PLUGIN / "skills").iterdir() if p.is_dir()])
        carte = lire(ROOT / "docs" / "images" / "carte-depot.svg")
        for n in re.findall(r"\b(\d+) skills\b", carte):
            self.assertEqual(int(n), skills)


class RenvoisTests(unittest.TestCase):
    def test_chemins_des_skills_et_du_plugin_resolus(self):
        motif = re.compile(r"\$\{CLAUDE_(SKILL_DIR|PLUGIN_ROOT)\}/([A-Za-z0-9_./-]+)")
        vus = 0
        for f in fichiers_maison():
            parties = f.relative_to(PLUGIN).parts
            for variable, cible in motif.findall(lire(f)):
                cible = cible.rstrip(".")
                if variable == "SKILL_DIR":
                    if parties[0] != "skills":
                        continue
                    base = PLUGIN / "skills" / parties[1]
                else:
                    base = PLUGIN
                vus += 1
                with self.subTest(fichier=f.relative_to(ROOT).as_posix(), cible=cible):
                    self.assertTrue((base / cible).exists())
        self.assertGreater(vus, 100)

    def test_agents_et_skills_cites_existent(self):
        noms = {p.stem for p in (PLUGIN / "agents").glob("*.md")}
        noms |= {p.name for p in (PLUGIN / "skills").iterdir() if p.is_dir()}
        documents = list(fichiers_maison()) + [ROOT / "README.md", ROOT / "AGENTS.md"]
        documents += sorted((ROOT / "docs").glob("*.md"))
        for f in documents:
            for nom in re.findall(r"dan-cortex:([a-z0-9-]+)", lire(f)):
                with self.subTest(fichier=f.relative_to(ROOT).as_posix(), nom=nom):
                    self.assertIn(nom, noms)


class AgentsTests(unittest.TestCase):
    def test_outils_par_agent_suit_les_fiches(self):
        tableau = lire(PLUGIN / "skills" / "lancer-projet" / "references" / "outils-par-agent.md")
        lignes = re.findall(r"^\| `([a-z0-9-]+)` \| [^|]+ \| [ABC], `(\w+)`, effort (\w+) \| ([^|]+) \| ([^|]+) \|",
                            tableau, re.M)
        fiches = {p.stem: entete(p) for p in (PLUGIN / "agents").glob("*.md")}
        self.assertEqual(sorted(l[0] for l in lignes), sorted(fiches))
        for nom, modele, effort, skills, outils in lignes:
            fiche = fiches[nom]
            attendus = fiche.get("skills") or []
            with self.subTest(agent=nom):
                self.assertEqual((modele, effort), (fiche["model"], fiche["effort"]))
                self.assertEqual([o.strip() for o in outils.split(",")], fiche["tools"])
                self.assertEqual([] if skills.strip() == "aucun" else re.findall(r"`([a-z0-9-]+)`", skills),
                                 attendus)

    def test_niveau_de_l_organigramme_conforme_a_la_fiche(self):
        niveaux = {"A": ("inherit", "high"), "B": ("sonnet", "medium"), "C": ("haiku", "low")}
        organigramme = lire(PLUGIN / "skills" / "lancer-projet" / "references" / "organigramme.md")
        lignes = re.findall(r"^\| `([a-z0-9-]+)` \| ([ABC]) \|", organigramme, re.M)
        self.assertEqual(len(lignes), len(list((PLUGIN / "agents").glob("*.md"))))
        for nom, niveau in lignes:
            fiche = entete(PLUGIN / "agents" / ("%s.md" % nom))
            with self.subTest(agent=nom):
                self.assertEqual(fiche["name"], nom)
                self.assertEqual((fiche["model"], fiche["effort"]), niveaux[niveau])


if __name__ == "__main__":
    unittest.main()
