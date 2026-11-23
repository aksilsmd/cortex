"""Le plugin reste importable par « Téléverser un plugin » : profondeur, nombre de fichiers, taille, pas de bin/.

Constat du 23/11/2026 (docs/audit-coherence-2026-11-22.md, A29) : l'import refusait l'archive avec « Zip file
contains path more than 12 folders deep ». On garde un segment de marge : 11 segments au plus, fichier compris.
"""
import importlib.util
import io
import subprocess
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "dan-cortex"
ARCHIVE = ROOT / "dist" / "dan-cortex.plugin"
SCRIPT = ROOT / "scripts" / "construire_plugin.py"
PROFONDEUR_MAX = 11
FICHIERS_MAX = 5000
TAILLE_MAX = 200 * 1024 * 1024


def charger():
    spec = importlib.util.spec_from_file_location("construire_plugin", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def suivis():
    sortie = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "dan-cortex"],
                            capture_output=True, check=True).stdout
    return [c.decode("utf-8")[len("dan-cortex/"):] for c in sortie.split(b"\0") if c]


class ArchivePluginTests(unittest.TestCase):
    def test_limites_du_script_inchangees(self):
        build = charger()
        self.assertEqual((build.PROFONDEUR_MAX, build.FICHIERS_MAX, build.TAILLE_MAX),
                         (PROFONDEUR_MAX, FICHIERS_MAX, TAILLE_MAX))

    def test_fichiers_suivis_dans_les_limites(self):
        chemins = suivis()
        self.assertTrue(chemins)
        trop_profonds = [c for c in chemins if len(c.split("/")) > PROFONDEUR_MAX]
        self.assertEqual(trop_profonds, [], "chemins de plus de %d segments depuis dan-cortex/" % PROFONDEUR_MAX)
        self.assertLessEqual(len(chemins), FICHIERS_MAX)
        self.assertLessEqual(sum((PLUGIN / c).stat().st_size for c in chemins if (PLUGIN / c).is_file()),
                             TAILLE_MAX)
        self.assertNotIn("bin", {c.split("/")[0] for c in chemins})
        self.assertIn(".claude-plugin/plugin.json", chemins)

    def test_archive_construite_dans_les_limites(self):
        self.assertTrue(ARCHIVE.is_file())
        with zipfile.ZipFile(io.BytesIO(ARCHIVE.read_bytes())) as archive:
            infos = archive.infolist()
        fichiers = [i for i in infos if not i.is_dir()]
        self.assertEqual([i.filename for i in infos if len(i.filename.rstrip("/").split("/")) > PROFONDEUR_MAX], [])
        self.assertLessEqual(len(fichiers), FICHIERS_MAX)
        self.assertLessEqual(sum(i.file_size for i in fichiers), TAILLE_MAX)
        self.assertLessEqual(ARCHIVE.stat().st_size, TAILLE_MAX)
        self.assertNotIn("bin", {i.filename.split("/")[0] for i in infos})
        self.assertIn(".claude-plugin/plugin.json", {i.filename for i in fichiers})
        self.assertEqual(charger().ecarts_de_l_archive(ARCHIVE.read_bytes()), [])

    def test_le_controle_detecte_un_chemin_trop_profond(self):
        build = charger()
        profond = "/".join(["d"] * PROFONDEUR_MAX) + "/f.md"
        ecarts = build.ecarts_aux_limites([(".claude-plugin/plugin.json", 10), (profond, 1), ("bin/x", 1)])
        self.assertEqual(len(ecarts), 2)
        self.assertEqual(build.ecarts_aux_limites([(".claude-plugin/plugin.json", 10)]), [])


if __name__ == "__main__":
    unittest.main()
