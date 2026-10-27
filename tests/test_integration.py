"""Le pôle robustesse-agents est bien branché dans Dan-Cortex."""
import csv
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "dan-cortex" / "skills" / "robustesse-agents" / "scripts" / "robustesse.py"
CORTEX = ROOT / "dan-cortex" / "skills" / "lancer-projet" / "scripts" / "cortex.py"
REGLAGES = ROOT / "dan-cortex" / "skills" / "robustesse-agents" / "assets" / "reglages-autonomes.json"


def load_cortex():
    spec = importlib.util.spec_from_file_location("cortex_script", CORTEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LauncherTests(unittest.TestCase):
    def test_runs_in_isolated_mode(self):
        proc = subprocess.run([sys.executable, "-I", str(LAUNCHER), "--version"],
                              capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("ccal", proc.stdout)

    def test_live_evaluation_requires_opt_in(self):
        proc = subprocess.run([sys.executable, "-I", str(LAUNCHER), "evaluate"],
                              capture_output=True, text=True, check=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--live", proc.stderr)


class ChecklistTests(unittest.TestCase):
    def setUp(self):
        self.cortex = load_cortex()
        self.rob = [i for i in self.cortex.charger_checklists() if i["domaine"] == "ROB"]

    def test_rob_controls_are_loaded_without_duplicates(self):
        self.assertGreaterEqual(len(self.rob), 10)
        self.assertFalse([i["id"] for i in self.rob if i.get("doublon")])

    def test_ia_tag_gates_product_controls(self):
        sans_ia = {i["id"] for i in self.rob if self.cortex.applicable(i, ["saas"], [])}
        avec_ia = {i["id"] for i in self.rob if self.cortex.applicable(i, ["saas"], ["ia"])}
        self.assertEqual(sans_ia, {"ROB-001", "ROB-002", "ROB-003"})
        self.assertNotIn("ROB-004", sans_ia)
        self.assertIn("ROB-010", avec_ia)
        self.assertTrue(sans_ia < avec_ia)


def cortex(*args):
    return subprocess.run([sys.executable, "-I", str(CORTEX), *args], capture_output=True, text=True, check=False)


class AutonomyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dossier = Path(self.tmp.name) / "projet"

    def tearDown(self):
        self.tmp.cleanup()

    def config(self):
        return json.loads((self.dossier / "00-pilotage" / "cortex.json").read_text(encoding="utf-8"))

    def couverture(self):
        with open(self.dossier / "00-pilotage" / "couverture.csv", encoding="utf-8-sig", newline="") as f:
            return {row["id"] for row in csv.DictReader(f, delimiter=";")}

    def init(self, *extra):
        proc = cortex("init", "--dossier", str(self.dossier), "--nom", "Essai", "--types", "saas",
                      "--mode", "integral", *extra)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return proc

    def test_default_level_is_accompagne(self):
        self.init()
        self.assertEqual(self.config()["autonomie"], "accompagne")
        self.assertNotIn("autonome", self.config()["tags"])
        self.assertNotIn("ROB-004", self.couverture())

    def test_autonome_adds_tag_and_controls(self):
        self.init("--autonomie", "autonome")
        self.assertIn("autonome", self.config()["tags"])
        self.assertTrue({"ROB-004", "ROB-005", "ROB-006"} <= self.couverture())
        fiche = (self.dossier / "00-pilotage" / "fiche-projet.md").read_text(encoding="utf-8")
        self.assertIn("Autonomie : autonome", fiche)
        self.assertIn("Autorisations permanentes", fiche)

    def test_switching_level_later_resyncs_coverage(self):
        self.init()
        proc = cortex("etat", "--dossier", str(self.dossier), "--set", "autonomie=autonome")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("ROB-004", self.couverture())
        proc = cortex("etat", "--dossier", str(self.dossier), "--set", "autonomie=accompagne")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertNotIn("autonome", self.config()["tags"])

    def test_resync_keeps_autonome_tag(self):
        self.init("--autonomie", "autonome", "--tags", "ia")
        proc = cortex("couverture", "resync", "--dossier", str(self.dossier), "--tags", "ia,comptes")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("autonome", self.config()["tags"])

    def test_unknown_level_is_rejected(self):
        proc = cortex("init", "--dossier", str(self.dossier), "--nom", "Essai", "--types", "saas",
                      "--autonomie", "sans-limite")
        self.assertNotEqual(proc.returncode, 0)

    def test_provisional_decisions_are_listed(self):
        self.init("--autonomie", "autonome")
        proc = cortex("registre", "decisions", "ajouter", "titre=Choix de la pile", "type=1",
                      "decideur=chef d'orchestre", "statut=provisoire", "--dossier", str(self.dossier))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        proc = cortex("etat", "--dossier", str(self.dossier))
        self.assertIn("Décisions provisoires", proc.stdout)


class AutonomousSettingsTests(unittest.TestCase):
    def test_template_has_no_high_finding(self):
        proc = subprocess.run([sys.executable, "-I", str(LAUNCHER), "audit-config", "--path", str(REGLAGES)],
                              capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertNotIn("[HIGH]", proc.stdout)

    def test_template_keeps_sandbox_and_no_bypass(self):
        data = json.loads(REGLAGES.read_text(encoding="utf-8"))
        self.assertTrue(data["sandbox"]["enabled"])
        self.assertNotIn(data["permissions"]["defaultMode"], ("bypassPermissions", "dontAsk"))


class RegistreArgumentsTests(unittest.TestCase):
    """--dossier peut se placer n'importe où, quelle que soit la version de Python."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dossier = str(Path(self.tmp.name) / "projet")
        proc = cortex("init", "--dossier", self.dossier, "--nom", "Essai", "--types", "saas")
        self.assertEqual(proc.returncode, 0, proc.stderr)

    def tearDown(self):
        self.tmp.cleanup()

    def decisions(self):
        chemin = Path(self.dossier) / "00-pilotage" / "registres" / "decisions.csv"
        with open(chemin, encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f, delimiter=";"))

    def test_dossier_before_fields(self):
        proc = cortex("registre", "decisions", "ajouter", "--dossier", self.dossier, "titre=Avant", "type=2")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(self.decisions()[0]["titre"], "Avant")

    def test_dossier_between_fields_keeps_order(self):
        proc = cortex("registre", "decisions", "ajouter", "titre=Milieu", "--dossier", self.dossier, "type=2")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        ligne = self.decisions()[0]
        self.assertEqual((ligne["titre"], ligne["type"]), ("Milieu", "2"))

    def test_update_with_dossier_before_id(self):
        cortex("registre", "decisions", "ajouter", "titre=X", "--dossier", self.dossier)
        proc = cortex("registre", "decisions", "maj", "--dossier", self.dossier, "DEC-001", "statut=validee")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(self.decisions()[0]["statut"], "validee")

    def test_unknown_option_still_rejected(self):
        proc = cortex("registre", "decisions", "ajouter", "titre=X", "--inconnue", "--dossier", self.dossier)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("--inconnue", proc.stderr)


if __name__ == "__main__":
    unittest.main()
