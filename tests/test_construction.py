"""Le build de dist/dan-cortex.plugin est reproductible, complet et à jour."""
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "construire_plugin.py"


def charger():
    spec = importlib.util.spec_from_file_location("construire_plugin", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ConstructionTests(unittest.TestCase):
    def setUp(self):
        self.build = charger()

    def test_reproductible(self):
        self.assertEqual(self.build.construire(), self.build.construire())

    def test_contenu_egal_aux_fichiers_suivis(self):
        suivis = subprocess.run(["git", "-C", str(ROOT), "ls-files", "dan-cortex"],
                                capture_output=True, text=True, check=True).stdout.split()
        attendus = sorted(p[len("dan-cortex/"):] for p in suivis)
        archive = zipfile.ZipFile(io.BytesIO(self.build.construire()))
        fichiers = sorted(n for n in archive.namelist() if not n.endswith("/"))
        self.assertEqual(fichiers, attendus)
        self.assertIn(".claude-plugin/plugin.json", fichiers)
        for skill in ("execution-resiliente", "confidentialite-traces", "robustesse-agents"):
            self.assertIn("skills/%s/SKILL.md" % skill, fichiers)

    def test_caches_exclus_hors_git(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / "dan-cortex"
            (base / ".claude-plugin").mkdir(parents=True)
            (base / ".claude-plugin" / "plugin.json").write_text('{"name": "dan-cortex"}', encoding="utf-8")
            (base / "skills" / "x" / "__pycache__").mkdir(parents=True)
            (base / "skills" / "x" / "SKILL.md").write_text("---\nname: x\n---\n", encoding="utf-8")
            (base / "skills" / "x" / "__pycache__" / "a.pyc").write_bytes(b"\0")
            (base / "skills" / "x" / "paquet.egg-info").mkdir()
            (base / "skills" / "x" / "paquet.egg-info" / "PKG-INFO").write_text("x", encoding="utf-8")
            fichiers = self.build.fichiers_du_plugin(tmp, utiliser_git=False)
            self.assertEqual(fichiers, [".claude-plugin/plugin.json", "skills/x/SKILL.md"])

    def test_archive_du_depot_a_jour(self):
        proc = subprocess.run([sys.executable, "-I", str(SCRIPT), "--verifier"], capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
