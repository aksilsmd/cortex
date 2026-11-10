#!/usr/bin/env python3
"""Assemble le paquet universel de Dan-Cortex à partir du skill accueil-recueil.

Produit dans dan-cortex/universel/ :
  - DAN-CORTEX-COMPLET.md : noyau + toutes les références, en un seul fichier à joindre ou coller ;
  - connaissances/*.md     : les références, une par fichier (10 au plus) ;
  - skill/dan-cortex/      : dossier de skill portable (SKILL.md + references/).
Vérifie que le noyau tient dans 8 000 caractères (limite d'instructions la plus basse rencontrée).
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent / "dan-cortex"
SOURCE = RACINE / "skills" / "accueil-recueil" / "references"
UNIVERSEL = RACINE / "universel"
NOYAU = UNIVERSEL / "DAN-CORTEX-NOYAU.md"
ORDRE = ["parcours", "entretien", "exploration", "livrables", "etude-realisation", "outils-quand", "mode-universel"]
LIMITE_NOYAU = 8000
LIMITE_FICHIERS = 10


def construire() -> int:
    noyau = NOYAU.read_text(encoding="utf-8")
    if len(noyau) > LIMITE_NOYAU:
        print(f"ERREUR : noyau de {len(noyau)} caractères, limite {LIMITE_NOYAU}", file=sys.stderr)
        return 1
    manquants = [n for n in ORDRE if not (SOURCE / f"{n}.md").is_file()]
    if manquants:
        print(f"ERREUR : références absentes : {manquants}", file=sys.stderr)
        return 1
    if len(ORDRE) > LIMITE_FICHIERS:
        print("ERREUR : trop de fichiers de connaissance", file=sys.stderr)
        return 1

    connaissances = UNIVERSEL / "connaissances"
    skill = UNIVERSEL / "skill" / "dan-cortex"
    for dossier in (connaissances, skill):
        if dossier.exists():
            shutil.rmtree(dossier)
    connaissances.mkdir(parents=True)
    (skill / "references").mkdir(parents=True)

    parties = [noyau.rstrip(), "\n\n---\n\n# Annexes de méthode\n"]
    for i, nom in enumerate(ORDRE, start=1):
        texte = (SOURCE / f"{nom}.md").read_text(encoding="utf-8")
        # Les renvois propres au plugin Claude n'ont pas de sens ailleurs : on les neutralise.
        texte = texte.replace("`lancer-projet/references/", "`").replace("`robustesse-agents/references/", "`")
        (connaissances / f"{i:02d}-{nom}.md").write_text(texte, encoding="utf-8")
        (skill / "references" / f"{nom}.md").write_text(texte, encoding="utf-8")
        parties.append(f"\n\n<!-- annexe {i} : {nom} -->\n\n{texte.rstrip()}")

    (UNIVERSEL / "DAN-CORTEX-COMPLET.md").write_text("".join(parties) + "\n", encoding="utf-8")

    corps = noyau.split("\n", 1)[1].lstrip()
    entete = (
        "---\n"
        "name: dan-cortex\n"
        'description: "Dan-Cortex : accueille l\'utilisateur, recueille son besoin même brut, le reformule et le fait '
        "valider, explore le domaine (web, GitHub), propose, mène l'entretien à réponses suggérées, puis produit "
        "cahier des charges, étude de marché, conception, planning, stratégie de test et étude de réalisation (IA ou "
        "entreprise tierce, budget, gains). À utiliser pour toute idée ou tout projet numérique à cadrer, même si "
        'l\'utilisateur débute."\n'
        "---\n\n# Dan-Cortex\n\n"
    )
    renvoi = (
        "\n\n## Références\n"
        + "".join(f"- `references/{n}.md`\n" for n in ORDRE)
        + "\nLire la référence de l'étape en cours avant de l'exécuter.\n"
    )
    (skill / "SKILL.md").write_text(entete + corps.rstrip() + renvoi, encoding="utf-8")
    print(f"noyau : {len(noyau)} caractères ; complet : {len(''.join(parties))} ; {len(ORDRE)} annexes")
    return 0


if __name__ == "__main__":
    sys.exit(construire())
