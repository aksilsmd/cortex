---
name: usine-logicielle
description: >
  Pôle Réalisation et qualité de Dan-Cortex : construit le code lot par lot en autonomie, puis enchaîne tests unitaires, fonctionnels, d'API, de bout en bout, recette, sécurité et intrusion, avec corrections. À utiliser pour coder, développer, tester, recetter, corriger, « construis le produit ».
---

# Usine logicielle — pôle Réalisation et qualité

Ce pôle transforme des spécifications validées en code livré, testé et conforme aux normes, sans que l'utilisateur ait à surveiller. Sa règle d'or : **aucun lot n'est « terminé » sur la parole de son auteur : il l'est quand des outils et un autre agent l'ont constaté.**

## Principes

1. **Contrat d'abord, code ensuite.** Les interfaces entre lots sont écrites et figées avant le premier développement : sans elles, les lots parallèles divergent et l'intégration coûte plus que le code.
2. **Un lot, un agent, des fichiers dont il est seul propriétaire.** Aucun conflit de fusion, aucun développeur n'a besoin de lire le code d'un autre.
3. **Le test précède le code.** Les critères d'acceptation exécutables viennent des cas `CT-` et des règles `RG-` ; un test écrit après coup épouse le code au lieu de le contrôler.
4. **Les outils jugent avant les modèles.** Format, analyse statique, types, tests et règles d'architecture passent avant toute relecture : un défaut mécanique ne justifie jamais des tokens de revue.
5. **Celui qui code ne se relit pas.** `relecteur-code` lit des différences avec un contexte neuf ; il constate, il ne corrige pas.
6. **Les tests ne se modifient pas pour passer.** Affaiblir une assertion ou un seuil pour obtenir le vert est un changement de comportement : il se justifie par écrit et se revoit.
7. **De petits lots, rapidement vérifiés.** Un volume de changements élevé sans retour rapide dégrade la stabilité (DORA 2025) : plafonner la taille des différences.
8. **Toute commande passe par `essais.py`.** Seules les lignes d'échec entrent dans le contexte ; c'est le premier levier d'économie de tokens (`references/sobriete-code.md`).

## Méthode

1. **Préparer** : lots, contrats, propriété des fichiers, graphe, incréments (`references/decoupage-lots.md`).
2. **Construire un lot** : tests unitaires puis code, contrôles automatiques, revue des différences, tests du lot, correction, non-régression (`references/boucle-build-test.md`).
3. **Tester par niveau** : unitaire, composant, API, contrat, bout en bout, performance, accessibilité (`references/tests-par-niveau.md`).
4. **Recetter** : campagne du cahier de recette, anomalies, procès-verbal (`references/recette.md`).
5. **Contrôler le tout** (`references/checklist-realisation.md`, `references/checklist-tests.md`).

## Chaîne complète : qui fait quoi

| Étape | Agent | Résultat |
|---|---|---|
| Harnais, jeux de données, cas de test | `concepteur-tests` | tests prêts à exécuter |
| Tests unitaires puis code d'un lot | `developpeur-backend`, `developpeur-frontend`, `developpeur-mobile`, `integrateur` | lot livré, journal de build |
| Revue des différences | `relecteur-code` (avec `gardien-des-normes`) | note de revue |
| Tests fonctionnels, d'API, de bout en bout du lot | `automaticien-tests`, rejoués par `executant-tests` | suites vertes |
| Sécurité automatisée du lot (code, dépendances, secrets) | `auditeur-securite`, skill `securite-protection` | constats au registre |
| Correction | développeur d'origine, repris | lot corrigé, non-régression rejouée |
| Recette globale | `recetteur` | `05-validation/pv-recette.md` |
| Performance et accessibilité | `automaticien-tests`, `expert-accessibilite` | rapports |
| Tests de sécurité complets, puis intrusion | `auditeur-securite`, `testeur-intrusion` (autorisation écrite d'abord) | rapports, contre-tests |

Les tests de sécurité et d'intrusion suivent le skill `securite-protection`, et les essais de robustesse des fonctions d'IA le skill `robustesse-agents` ; ce pôle les place dans la chaîne et rejoue la non-régression après chaque correction.

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Lots, contrats, dépendances, ordre | `04-realisation/lots.md` | `LOT-` |
| Code et tests unitaires | dépôt du projet (`code/` ou chemin de la fiche projet) | |
| Journal de build | `04-realisation/journal-de-build.md` | `LOT-` |
| Notes de revue de code | `04-realisation/revues/revue-<lot>.md` | `LOT-`, constats |
| Sorties de tests | `04-realisation/journaux/` | |
| Anomalies | registre des anomalies | `ANO-`, `CT-` |
| Procès-verbal de recette | `05-validation/pv-recette.md` | `CT-` |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/decoupage-lots.md` | avant de découper en lots ou d'écrire `lots.md` |
| `${CLAUDE_SKILL_DIR}/references/boucle-build-test.md` | avant de construire ou de relire un lot : boucle, définition de « terminé », trois tentatives |
| `${CLAUDE_SKILL_DIR}/references/sobriete-code.md` | avant tout codage : contexte minimal, `essais.py`, générateurs |
| `${CLAUDE_SKILL_DIR}/references/tests-par-niveau.md` | pour choisir outils, seuils et jeux de données de chaque niveau de test |
| `${CLAUDE_SKILL_DIR}/references/recette.md` | pour la campagne de recette, les anomalies, le procès-verbal |
| `${CLAUDE_SKILL_DIR}/references/checklist-realisation.md` | contrôles DEV, à traiter par jalon |
| `${CLAUDE_SKILL_DIR}/references/checklist-tests.md` | contrôles TST, à traiter par jalon |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

## Garde-fous

- Travail en local : aucun push vers un dépôt distant, aucun déploiement, aucune dépendance installée sans l'avoir listée au compte rendu. Ces actes demandent l'accord de l'utilisateur.
- Aucune donnée de production ni donnée personnelle réelle dans les tests ; données fictives ou anonymisées.
- Test d'intrusion : jamais sans périmètre et autorisation écrits du propriétaire de l'environnement, et jamais sur un système tiers.
- Une version d'outil ou de framework non vérifiée à la source s'écrit « à vérifier » ; aucun résultat de test n'est annoncé sans la sortie qui le prouve.
- Le pôle ne décide pas seul d'un changement d'architecture, de contrat ou de seuil de qualité : il le propose à l'architecte ou au chef d'orchestre.
