#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dan-Cortex — robustesse des agents : point d'entrée du paquet ccal (bibliothèque standard uniquement).

Audit des réglages Claude Code, export du corpus de scénarios, évaluation live sur accord explicite.

Usage : python3 robustesse.py audit-config | scenarios | evaluate --live   (python3 robustesse.py --help)
"""
import os
import sys

# Le dossier du script n'est pas sur sys.path sous « python3 -I » : on l'ajoute pour trouver le paquet ccal.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ccal.cli import main  # noqa: E402

if __name__ == "__main__":
    main()
