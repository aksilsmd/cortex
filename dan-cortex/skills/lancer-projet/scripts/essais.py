#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — lance une commande de test ou de build et n'affiche que l'essentiel.

La sortie complète part dans un fichier journal ; le terminal (donc le contexte
de l'agent) ne reçoit qu'un résumé : code de retour, durée, lignes d'échec.
C'est le principal levier d'économie de tokens pendant la réalisation.

Usage :
  python3 essais.py [--journal chemin.log] [--max 40] [--delai 900] -- <commande> [arguments…]
Exemples :
  python3 essais.py -- npm test
  python3 essais.py --journal 04-realisation/journaux/api.log -- pytest -q tests/api
"""
import os
import re
import subprocess
import sys
import time

MOTIFS = re.compile(
    r"(\bFAIL(ED|URE)?\b|\bERROR\b|\bError\b|\berror\b|✗|✘|×|AssertionError|Traceback|Exception|panic:|"
    r"\bnot ok\b|expected .* (to|but)|Expected|Received|TS\d{4}|\bE\s{3}|échec|erreur)")
RESUME = re.compile(r"(\d+\s+(passed|failed|skipped|errors?|tests?|passing|failing|pending)|Tests?:\s|Test Suites:|"
                    r"^OK\b|^Ran \d+ tests?|coverage|Couverture|\bTOTAL\b)", re.I)


def main():
    args = sys.argv[1:]
    journal, maxi, delai = None, 40, 900
    while args and args[0] != "--":
        if args[0] == "--journal" and len(args) > 1:
            journal, args = args[1], args[2:]
        elif args[0] == "--max" and len(args) > 1:
            maxi, args = int(args[1]), args[2:]
        elif args[0] == "--delai" and len(args) > 1:
            delai, args = int(args[1]), args[2:]
        else:
            break
    if args and args[0] == "--":
        args = args[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    if not journal:
        dossier = os.path.join("04-realisation", "journaux") if os.path.isdir("04-realisation") else "."
        os.makedirs(dossier, exist_ok=True)
        journal = os.path.join(dossier, "essais-%s.log" % time.strftime("%Y%m%d-%H%M%S"))
    else:
        os.makedirs(os.path.dirname(os.path.abspath(journal)), exist_ok=True)
    debut = time.time()
    try:
        proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=delai)
        sortie, code = proc.stdout.decode("utf-8", errors="replace"), proc.returncode
    except subprocess.TimeoutExpired as e:
        sortie = (e.stdout or b"").decode("utf-8", errors="replace") + "\n[délai dépassé : %d s]" % delai
        code = 124
    except FileNotFoundError:
        print("COMMANDE INTROUVABLE : %s" % args[0])
        sys.exit(127)
    duree = time.time() - debut
    with open(journal, "w", encoding="utf-8") as f:
        f.write("$ %s\n\n%s" % (" ".join(args), sortie))
    lignes = [re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", l).rstrip() for l in sortie.splitlines()]
    resume = [l.strip() for l in lignes if RESUME.search(l)][-4:]
    etat = "OK" if code == 0 else "ÉCHEC"
    print("%s (code %d, %.1f s, %d lignes) — journal complet : %s" % (etat, code, duree, len(lignes), journal))
    for l in resume:
        print("  " + l[:200])
    if code != 0:
        gardees, vus = [], set()
        for i, l in enumerate(lignes):
            if MOTIFS.search(l):
                for j in range(max(0, i - 1), min(len(lignes), i + 3)):
                    if j not in vus and lignes[j].strip():
                        vus.add(j)
                        gardees.append(lignes[j][:220])
        if not gardees:
            gardees = [l[:220] for l in lignes[-15:] if l.strip()]
        print("Lignes utiles (%d sur %d) :" % (min(len(gardees), maxi), len(gardees)))
        for l in gardees[:maxi]:
            print("  " + l)
        if len(gardees) > maxi:
            print("  … la suite est dans le journal (lire seulement la partie utile, avec une recherche ciblée).")
    sys.exit(code)


if __name__ == "__main__":
    main()
