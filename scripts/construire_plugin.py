#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — construit l'archive distribuable dist/dan-cortex.plugin (bibliothèque standard uniquement).

L'archive contient les fichiers du dossier dan-cortex/ suivis par Git (ou, hors d'un dépôt Git, tous ses
fichiers sauf caches et artefacts de build), à la racine de l'archive, triés, avec une date fixe. La
construction est déterministe (mêmes fichiers source, même liste et mêmes données) ; la vérification compare
le *contenu* de l'archive (noms et données), car les octets compressés par zlib peuvent varier d'un
environnement à l'autre (version ou build de la bibliothèque), ce qui rendrait une comparaison binaire
instable d'une machine de CI à l'autre.

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
# Limites de l'import par « Téléverser un plugin » (application Claude). Profondeur : message d'erreur constaté le
# 23/11/2026, « Zip file contains path more than 12 folders deep » ; on garde un segment de marge (11 segments au
# plus, fichier compris, depuis la racine de l'archive). Nombre de fichiers, taille et dossier bin/ : limites
# annoncées par l'éditeur, à vérifier sur sa documentation à chaque version.
PROFONDEUR_MAX = 11
FICHIERS_MAX = 5000
TAILLE_MAX = 200 * 1024 * 1024


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


def ecarts_aux_limites(entrees):
    """Écarts aux limites d'import pour une liste (chemin relatif à la racine du plugin, taille en octets)."""
    ecarts = []
    fichiers = [(c, n) for c, n in entrees if not c.endswith("/")]
    profonds = sorted(c for c, _ in entrees if len(c.rstrip("/").split("/")) > PROFONDEUR_MAX)
    if profonds:
        ecarts.append("%d chemin(s) de plus de %d segments, dont %s" % (len(profonds), PROFONDEUR_MAX, profonds[0]))
    if len(fichiers) > FICHIERS_MAX:
        ecarts.append("%d fichiers, plus de %d" % (len(fichiers), FICHIERS_MAX))
    taille = sum(n for _, n in fichiers)
    if taille > TAILLE_MAX:
        ecarts.append("%d octets décompressés, plus de %d" % (taille, TAILLE_MAX))
    if any(c.split("/")[0] == "bin" for c, _ in entrees):
        ecarts.append("un dossier bin/ à la racine du plugin")
    if ".claude-plugin/plugin.json" not in {c for c, _ in fichiers}:
        ecarts.append(".claude-plugin/plugin.json absent de la racine")
    return ecarts


def ecarts_de_l_archive(octets):
    """Écarts aux limites d'import d'une archive déjà construite."""
    with zipfile.ZipFile(io.BytesIO(octets)) as archive:
        return ecarts_aux_limites([(i.filename, i.file_size) for i in archive.infolist()])


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


def contenu(octets):
    """Liste ordonnée (nom, données) de l'archive, indépendante de la compression et des métadonnées."""
    with zipfile.ZipFile(io.BytesIO(octets)) as archive:
        return [(nom, archive.read(nom)) for nom in sorted(archive.namelist())]


def main():
    p = argparse.ArgumentParser(prog="construire_plugin.py", description=__doc__.splitlines()[0])
    p.add_argument("--verifier", action="store_true", help="vérifier que l'archive est à jour, sans l'écrire")
    p.add_argument("--sortie", default=SORTIE, help="chemin de l'archive, relatif à la racine du dépôt")
    a = p.parse_args()
    cible = os.path.join(RACINE, a.sortie)
    octets = construire()
    nombre = len(fichiers_du_plugin())
    ecarts = ecarts_de_l_archive(octets)
    if ecarts:
        print("Archive refusée à l'import :\n- " + "\n- ".join(ecarts))
        sys.exit(1)
    if a.verifier:
        actuel = open(cible, "rb").read() if os.path.isfile(cible) else b""
        a_jour = bool(actuel) and contenu(actuel) == contenu(octets)
        if actuel and ecarts_de_l_archive(actuel):
            print("%s refusée à l'import :\n- %s" % (a.sortie, "\n- ".join(ecarts_de_l_archive(actuel))))
            sys.exit(1)
        if not a_jour:
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
