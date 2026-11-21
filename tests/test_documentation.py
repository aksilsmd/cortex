"""La documentation est à jour : catalogues générés, schémas SVG valides, liens relatifs résolus, chiffres exacts."""
import re
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "dan-cortex"
IMAGES = ROOT / "docs" / "images"
SVG = "{http://www.w3.org/2000/svg}"
# Documents maison dont les liens sont contrôlés (les skills copiés d'Anthropic sont hors périmètre).
DOCUMENTS = (sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md"))
             + sorted((ROOT / ".github").rglob("*.md")) + [PLUGIN / "README.md", PLUGIN / "NOTICE.md"])


def lire(chemin):
    return chemin.read_text(encoding="utf-8")


class CataloguesTests(unittest.TestCase):
    def test_catalogues_a_jour(self):
        proc = subprocess.run([sys.executable, "-I", str(ROOT / "scripts" / "generer_catalogues.py"), "--verifier"],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


class SchemasTests(unittest.TestCase):
    def setUp(self):
        self.svgs = sorted(IMAGES.glob("*.svg"))

    def test_schemas_attendus(self):
        noms = {p.stem for p in self.svgs}
        for attendu in ("banniere", "carte-poles", "jalons", "vague-agents", "cycle-reunion", "carte-skills"):
            self.assertIn(attendu, noms)

    def test_svg_valides_et_accessibles(self):
        for svg in self.svgs:
            with self.subTest(svg=svg.name):
                racine = ET.parse(svg).getroot()
                self.assertEqual(racine.tag, SVG + "svg")
                self.assertTrue(racine.get("viewBox"))
                self.assertEqual(racine.get("role"), "img")
                titre, desc = racine.find(SVG + "title"), racine.find(SVG + "desc")
                self.assertTrue(titre is not None and titre.text.strip())
                self.assertTrue(desc is not None and desc.text.strip())
                self.assertNotIn("<script", lire(svg))

    def test_chaque_svg_reference_avec_texte_alternatif(self):
        textes = "\n".join(lire(p) for p in DOCUMENTS)
        for svg in self.svgs:
            with self.subTest(svg=svg.name):
                markdown = re.findall(r"!\[([^\]]*)\]\([^)]*%s\)" % re.escape(svg.name), textes)
                html = re.findall(r'<img[^>]*src="[^"]*%s"[^>]*alt="([^"]*)"|<img[^>]*alt="([^"]*)"[^>]*src="[^"]*%s"'
                                  % (re.escape(svg.name), re.escape(svg.name)), textes)
                alts = markdown + [a or b for a, b in html]
                self.assertTrue(alts, "%s n'est référencé nulle part" % svg.name)
                self.assertTrue(all(a.strip() for a in alts), "texte alternatif vide pour %s" % svg.name)


class LiensTests(unittest.TestCase):
    def test_liens_relatifs_resolus(self):
        motif = re.compile(r"\]\(([^)\s]+)\)|(?:src|href)=\"([^\"]+)\"")
        for doc in DOCUMENTS:
            texte = re.sub(r"```.*?```", "", lire(doc), flags=re.S)
            for m in motif.finditer(texte):
                cible = (m.group(1) or m.group(2)).split("#", 1)[0]
                if not cible or re.match(r"^[a-z][a-z0-9+.-]*:", cible):
                    continue
                with self.subTest(document=doc.relative_to(ROOT).as_posix(), cible=cible):
                    self.assertTrue((doc.parent / cible).exists())


class ChiffresTests(unittest.TestCase):
    def setUp(self):
        self.readme = lire(ROOT / "README.md")
        self.agents = len(list((PLUGIN / "agents").glob("*.md")))
        self.skills = len([p for p in (PLUGIN / "skills").iterdir() if p.is_dir()])
        self.controles = sum(len(re.findall(r"(?m)^\| [A-Z]{3}-\d{3} \|", lire(p)))
                             for p in PLUGIN.glob("skills/*/references/checklist-*.md"))

    def test_badges(self):
        self.assertIn("badge/agents-%d-" % self.agents, self.readme)
        self.assertIn("badge/contr%%C3%%B4les-%d-" % self.controles, self.readme)
        self.assertIn("| Agents | %d |" % self.agents, lire(PLUGIN / "README.md"))

    def test_francais_et_anglais_alignes(self):
        francais, anglais = self.readme.split("## In English", 1)
        self.assertIn("**%d agents experts**" % self.agents, francais)
        self.assertIn("**%d contrôles**" % self.controles, francais)
        self.assertIn("**%d expert agents**" % self.agents, anglais)
        self.assertIn("**%d skills**" % self.skills, anglais)
        self.assertIn("**%d controls**" % self.controles, anglais)

    def test_aucun_autre_compte_d_agents_ou_de_skills(self):
        for doc in (ROOT / "README.md", PLUGIN / "README.md", ROOT / "docs" / "architecture.md"):
            texte = lire(doc)
            with self.subTest(document=doc.relative_to(ROOT).as_posix()):
                for n in re.findall(r"\b(\d+) (?:agents experts|expert agents)\b", texte):
                    self.assertEqual(int(n), self.agents)
                for n in re.findall(r"\b(\d+) skills\b", texte):
                    self.assertEqual(int(n), self.skills)


if __name__ == "__main__":
    unittest.main()
