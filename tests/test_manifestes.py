"""Manifestes, documentation et skills racontent la même version et le même contenu."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "dan-cortex"


def lire(chemin):
    return chemin.read_text(encoding="utf-8")


class ManifestesTests(unittest.TestCase):
    def setUp(self):
        self.plugin = json.loads(lire(PLUGIN / ".claude-plugin" / "plugin.json"))
        self.marketplace = json.loads(lire(ROOT / ".claude-plugin" / "marketplace.json"))
        self.entree = next(p for p in self.marketplace["plugins"] if p["name"] == self.plugin["name"])

    def test_versions_concordent(self):
        version = self.plugin["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertEqual(self.entree["version"], version)
        self.assertEqual(self.marketplace["metadata"]["version"], version)
        premiere = re.search(r"^## (\d+\.\d+\.\d+)", lire(ROOT / "CHANGELOG.md"), re.M).group(1)
        self.assertEqual(premiere, version, "la première entrée du CHANGELOG doit être la version publiée")
        self.assertIn("badge/version-%s-" % version, lire(ROOT / "README.md"))

    def test_source_marketplace_existe(self):
        self.assertEqual((ROOT / self.entree["source"]).resolve(), PLUGIN.resolve())

    def test_mots_cles_sans_doublon(self):
        for mots in (self.plugin["keywords"], self.entree["keywords"]):
            self.assertEqual(len(mots), len(set(mots)))

    def test_changelog_sans_entree_en_double(self):
        versions = re.findall(r"^## (\d+\.\d+\.\d+)", lire(ROOT / "CHANGELOG.md"), re.M)
        self.assertEqual(len(versions), len(set(versions)))


class SkillsTests(unittest.TestCase):
    def setUp(self):
        self.dossiers = sorted(p for p in (PLUGIN / "skills").iterdir() if p.is_dir())

    def test_chaque_skill_se_charge(self):
        for dossier in self.dossiers:
            with self.subTest(skill=dossier.name):
                texte = lire(dossier / "SKILL.md")
                self.assertTrue(texte.startswith("---\n"))
                entete = texte.split("\n---", 1)[0]
                self.assertRegex(entete, r"(?m)^name: %s$" % re.escape(dossier.name))
                self.assertRegex(entete, r"(?m)^description: \S")

    def test_nouveaux_skills_presents(self):
        noms = {d.name for d in self.dossiers}
        self.assertTrue({"execution-resiliente", "confidentialite-traces"} <= noms)

    def test_compte_des_skills_dans_la_documentation(self):
        n = len(self.dossiers)
        self.assertIn("badge/skills-%d-" % n, lire(ROOT / "README.md"))
        self.assertIn("| Skills | %d |" % n, lire(PLUGIN / "README.md"))

    def test_chaque_skill_est_documente(self):
        racine, plugin = lire(ROOT / "README.md"), lire(PLUGIN / "README.md")
        for dossier in self.dossiers:
            if dossier.name == "lancer-projet":
                continue
            with self.subTest(skill=dossier.name):
                self.assertIn("/dan-cortex:%s" % dossier.name, racine)
                self.assertIn("/dan-cortex:%s" % dossier.name, plugin)


class RenvoisTests(unittest.TestCase):
    def test_renvois_entre_skills_resolus(self):
        motif = re.compile(r"\$\{CLAUDE_SKILL_DIR\}/(\.\./[A-Za-z0-9_./-]+)")
        vus = 0
        for skill_md in sorted((PLUGIN / "skills").glob("*/SKILL.md")):
            for cible in motif.findall(lire(skill_md)):
                vus += 1
                with self.subTest(skill=skill_md.parent.name, cible=cible):
                    chemin = (skill_md.parent / cible).resolve()
                    # « ../../agents/<nom>.md » est un modèle : seul son dossier doit exister.
                    self.assertTrue(chemin.is_dir() if cible.endswith("/") else chemin.is_file())
        self.assertGreater(vus, 0)

    def test_nouveaux_skills_branches_dans_le_chef_d_orchestre(self):
        texte = lire(PLUGIN / "skills" / "lancer-projet" / "SKILL.md")
        for skill in ("execution-resiliente", "confidentialite-traces"):
            self.assertIn("${CLAUDE_SKILL_DIR}/../%s/SKILL.md" % skill, texte)


if __name__ == "__main__":
    unittest.main()
