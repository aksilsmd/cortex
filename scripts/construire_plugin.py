#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — construit l'archive distribuable dist/dan-cortex.plugin (bibliothèque standard uniquement).

L'archive est reproductible : mêmes fichiers source, mêmes octets. Elle contient les fichiers du dossier
dan-cortex/ suivis par Git (ou, hors d'un dépôt Git, tous ses fichiers sauf caches et artefacts de build),
à la racine de l'archive, triés, avec une date fixe.

Usage :
  python3 scripts/construire_plugin.py              reconstruit dist/dan-cortex.plugin
  python3 scripts/construire_plugin.py --verifier   échoue (code 1) si l'archive n'est pas à jour
"""
import argparse
import io
import os
import subprocess
import sys
import zipfile

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLUGIN = "dan-cortex"
SORTIE = os.path.join("dist", "dan-cortex.plugin")
DATE_FIXE = (1980, 1, 1, 0, 0, 0)
EXCLUS = ("__pycache__", ".egg-info", ".DS_Store", ".pyc", ".in_use")


def exclu(chemin):
    return any(marque in partie for partie in chemin.split("/") for marque in EXCLUS)


def fichiers_du_plugin(racine=RACINE, utiliser_git=True):
    """Chemins relatifs à dan-cortex/, en notation POSIX et triés."""
    base = os.path.join(racine, PLUGIN)
    if not os.path.isfile(os.path.join(base, ".claude-plugin", "plugin.json")):
        raise SystemExit("Manifeste introuvable : %s/.claude-plugin/plugin.json" % base)
    chemins = None
    if utiliser_git:
        try:
            sortie = subprocess.run(["git", "-C", racine, "ls-files", "-z", PLUGIN],
                                    capture_output=True, check=True).stdout
            chemins = [c.decode("utf-8")[len(PLUGIN) + 1:] for c in sortie.split(b"\0") if c]
        except (OSError, subprocess.CalledProcessError):
            chemins = None
    if not chemins:
        chemins = []
        for dossier, sous, noms in os.walk(base):
            sous[:] = [s for s in sous if not exclu(s)]
            for nom in noms:
                chemins.append(os.path.relpath(os.path.join(dossier, nom), base).replace(os.sep, "/"))
    return sorted(c for c in chemins if not exclu(c) and os.path.isfile(os.path.join(base, c)))


def construire(racine=RACINE, utiliser_git=True):
    """Renvoie les octets de l'archive."""
    base = os.path.join(racine, PLUGIN)
    fichiers = fichiers_du_plugin(racine, utiliser_git)
    dossiers = sorted({"/".join(f.split("/")[:i]) + "/" for f in fichiers for i in range(1, f.count("/") + 1)})
    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w") as archive:
        for d in dossiers:
            info = zipfile.ZipInfo(d, DATE_FIXE)
            info.external_attr = (0o40755 << 16) | 0x10
            archive.writestr(info, b"")
        for f in fichiers:
            chemin = os.path.join(base, f)
            info = zipfile.ZipInfo(f, DATE_FIXE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if os.access(chemin, os.X_OK) else 0o100644) << 16
            with open(chemin, "rb") as source:
                archive.writestr(info, source.read(), compresslevel=9)
    return tampon.getvalue()


def main():
    p = argparse.ArgumentParser(prog="construire_plugin.py", description=__doc__.splitlines()[0])
    p.add_argument("--verifier", action="store_true", help="vérifier que l'archive est à jour, sans l'écrire")
    p.add_argument("--sortie", default=SORTIE, help="chemin de l'archive, relatif à la racine du dépôt")
    a = p.parse_args()
    cible = os.path.join(RACINE, a.sortie)
    octets = construire()
    nombre = len(fichiers_du_plugin())
    if a.verifier:
        actuel = open(cible, "rb").read() if os.path.isfile(cible) else b""
        if actuel != octets:
            print("%s n'est pas à jour : lancer « python3 scripts/construire_plugin.py »." % a.sortie)
            sys.exit(1)
        print("%s à jour (%d fichiers)." % (a.sortie, nombre))
        return
    os.makedirs(os.path.dirname(cible), exist_ok=True)
    with open(cible, "wb") as f:
        f.write(octets)
    print("%s construit : %d fichiers, %d octets." % (a.sortie, nombre, len(octets)))


if __name__ == "__main__":
    main()
