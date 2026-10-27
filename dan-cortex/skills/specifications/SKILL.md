---
name: specifications
description: >
  Pôle Besoin et spécifications de Dan-Cortex : note de cadrage, cahier des charges (EX-, EXNF-), spécifications générales (FN-), détaillées (RG-) et techniques. À utiliser pour « rédige le cahier des charges », « exigences », « spécifications fonctionnelles », « règles de gestion », « SFD ».
---

# Besoin et spécifications — pôle Besoin et spécifications

Ce pôle transforme une intention en documents sur lesquels on peut contractualiser, construire et recetter. Sa règle d'or : **une exigence qui ne se mesure pas ne se livre pas.** Chaque ligne se termine par un critère d'acceptation, et chaque identifiant descend jusqu'à un cas de test.

## Principes

1. **Quatre niveaux, quatre lecteurs.** Le cahier des charges dit *quoi et pourquoi* (MOA, direction). La SFG dit *quelles fonctions, pour qui* (MOA, MOE, UX). La SFD dit *exactement comment ça se comporte* (développeur, testeur). Les spécifications techniques disent *comment le système parle aux autres* (MOE, intégrateurs). Mélanger les niveaux rend chaque document illisible et invérifiable.
2. **Une exigence = un sujet, un verbe, un seuil.** « Rapide », « ergonomique », « sécurisé », « intuitif » sans valeur chiffrée et sans méthode de mesure sont interdits : ils ne se recettent pas et deviennent un litige.
3. **Dire quoi, pas comment.** Le cahier des charges et la SFG ne prescrivent ni technologie ni écran, sauf contrainte réelle justifiée. La solution se choisit en architecture, pas dans le besoin.
4. **Chaque identifiant se définit une fois et se cite partout.** `EX-`/`EXNF-` → `FN-` → `RG-`/`WF-` → `CT-`. Le script lit la chaîne ; une rupture est une erreur, pas un détail.
5. **Les cas d'exception valent les cas nominaux.** Donnée absente, droit insuffisant, double envoi, service tiers indisponible : les oublier, c'est laisser le développeur les inventer.
6. **Un module de SFD se suffit à lui-même.** Il est écrit en essaim, une instance par module : tout ce qu'il faut pour le comprendre y figure ou y est cité par identifiant.
7. **Le non-fonctionnel est du fonctionnel chiffré.** Chaque exigence non fonctionnelle se rattache à une caractéristique d'ISO/IEC 25010:2023, avec métrique, seuil, conditions de mesure et méthode de vérification.
8. **L'incertitude est écrite.** Hypothèse, question ouverte, point « à confirmer par la MOA » : jamais une règle inventée pour boucher un trou.

## Méthode

1. **Cadrer** : mission, gouvernance, périmètre, critères de succès et d'arrêt (`references/note-de-cadrage.md`).
2. **Exprimer le besoin** : exigences `EX-` et `EXNF-` vérifiables, priorisées, avec leur critère d'acceptation (`references/cahier-des-charges.md`, `references/exigences-non-fonctionnelles.md`).
3. **Structurer** : acteurs, fonctions `FN-`, processus, objets métier dans la SFG (`references/sfg.md`).
4. **Détailler par module** : règles `RG-`, cas nominaux et d'exception, données, messages, droits (`references/sfd.md`).
5. **Spécifier le technique** : contrats d'interface, traitements, formats, erreurs, paramétrage (`references/specs-techniques.md`).
6. **Tracer et vérifier** : `python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/cortex.py tracabilite verifier` ; corriger jusqu'à zéro erreur (`references/tracabilite.md`).
7. **Se relire** avec la liste de contrôles `SPC-` (`references/checklist-specifications.md`).

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Note de cadrage | `02-cadrage/note-de-cadrage.md` | |
| Cahier des charges | `02-cadrage/cahier-des-charges.md` | `EX-`, `EXNF-` |
| Spécifications fonctionnelles générales | `03-conception/specifications/sfg.md` | `FN-` |
| Spécifications fonctionnelles détaillées | `03-conception/specifications/sfd/<module>.md` | `RG-` |
| Spécifications techniques | `03-conception/specifications/specs-techniques.md` | `RG-` techniques, contrats `IF-` |

Chaque document commence par `## Synthèse` (périmètre, nombre d'identifiants, questions ouvertes, résultat du script).

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/note-de-cadrage.md` | avant d'écrire la note de cadrage |
| `${CLAUDE_SKILL_DIR}/references/cahier-des-charges.md` | avant d'exprimer le besoin, de rédiger ou de prioriser des exigences |
| `${CLAUDE_SKILL_DIR}/references/exigences-non-fonctionnelles.md` | pour chiffrer et faire vérifier une exigence non fonctionnelle |
| `${CLAUDE_SKILL_DIR}/references/sfg.md` | avant de rédiger la SFG |
| `${CLAUDE_SKILL_DIR}/references/sfd.md` | avant de rédiger le module d'une SFD |
| `${CLAUDE_SKILL_DIR}/references/specs-techniques.md` | avant de spécifier une interface, un traitement, un format |
| `${CLAUDE_SKILL_DIR}/references/tracabilite.md` | dès qu'un identifiant est créé, et avant de rendre : formats lus par le script |
| `${CLAUDE_SKILL_DIR}/references/checklist-specifications.md` | en fin de rédaction, pour se relire |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

Vocabulaire : MOA (maîtrise d'ouvrage, porte le besoin), MOE (maîtrise d'œuvre, réalise), AMOA (assistance à MOA), recette (VABF en test, VSR en production). En agile, un récit utilisateur correspond à une `EX-` ; ses critères d'acceptation, à la colonne finale ; un scénario Gherkin, à un `CT-`.

## Garde-fous

- Ne jamais écrire une exigence que le client n'a pas exprimée ni qu'une source ne justifie : la marquer « hypothèse » avec sa source ou la poser en question ouverte.
- Le pôle ne tranche ni le périmètre de la première version, ni les priorités en conflit, ni un arbitrage coût–fonction : il les présente avec leurs options au comité de cadrage.
- Les exigences réglementaires (données personnelles, accessibilité, paiement, secteur régulé) sont rédigées par le pôle mais « à valider » par le juriste-numerique ; elles préparent le travail d'un professionnel, elles ne le remplacent pas.
- Les normes citées (ISO/IEC 25010:2023, ISO/IEC/IEEE 29148, NF EN 16271) servent de repère de méthode ; leur texte exact est à consulter avant toute clause contractuelle.
