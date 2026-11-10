"""Le paquet universel est à jour, complet, et son noyau tient dans la limite d'instructions la plus basse."""
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNIVERSEL = ROOT / "dan-cortex" / "universel"
REFERENCES = ROOT / "dan-cortex" / "skills" / "accueil-recueil" / "references"


class UniverselTests(unittest.TestCase):
    def test_noyau_sous_la_limite(self):
        self.assertLessEqual(len((UNIVERSEL / "DAN-CORTEX-NOYAU.md").read_text(encoding="utf-8")), 8000)

    def test_noyau_porte_les_gestes_obligatoires(self):
        noyau = (UNIVERSEL / "DAN-CORTEX-NOYAU.md").read_text(encoding="utf-8")
        for attendu in ("Salue", "en vrac", "(recommandé)", "Je ne sais pas, décide pour moi", "Reformulation",
                        "Exploration", "Entretien approfondi", "Cahier des charges", "Étude de marché",
                        "Étude de réalisation", "À vous de décider", "à vérifier", "ÉTAT DU PROJET"):
            with self.subTest(attendu=attendu):
                self.assertIn(attendu, noyau)

    def test_paquet_a_jour(self):
        avant = {p: p.read_bytes() for p in UNIVERSEL.rglob("*") if p.is_file()}
        fait = subprocess.run([sys.executable, str(ROOT / "scripts" / "construire_universel.py")],
                              capture_output=True, text=True)
        self.assertEqual(fait.returncode, 0, fait.stderr)
        apres = {p: p.read_bytes() for p in UNIVERSEL.rglob("*") if p.is_file()}
        self.assertEqual(avant, apres, "relancer scripts/construire_universel.py et valider le résultat")

    def test_dix_fichiers_de_connaissance_au_plus(self):
        fichiers = list((UNIVERSEL / "connaissances").glob("*.md"))
        self.assertEqual(len(fichiers), len(list(REFERENCES.glob("*.md"))))
        self.assertLessEqual(len(fichiers), 10)

    def test_skill_portable_valide(self):
        texte = (UNIVERSEL / "skill" / "dan-cortex" / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(texte.startswith("---\nname: dan-cortex\ndescription: "))
        for ref in (UNIVERSEL / "skill" / "dan-cortex" / "references").glob("*.md"):
            self.assertIn("references/%s" % ref.name, texte)


if __name__ == "__main__":
    unittest.main()
