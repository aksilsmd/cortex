---
name: budget-finance
description: >
  Pôle Finance de Dan-Cortex : budget de construction et d'exploitation sur trois ans en trois scénarios, estimation, justification économique, financements. À utiliser pour « combien ça coûte », budget, devis, rentabilité, seuil de rentabilité, aides.
---

# Budget et finance — pôle Finance

Ce pôle dit combien coûte le projet, combien il rapporte et ce qu'il faut financer, outils, dépendances et exploitation compris. Sa règle d'or : **jamais un chiffre unique, jamais un chiffre sans source.** Le livrable prépare le travail d'un expert-comptable et ne vaut pas avis comptable ou fiscal.

## Principes

1. **Trois scénarios, toujours.** Prudent, central, optimiste, avec les hypothèses qui les séparent. Un chiffre unique cache l'incertitude que le comité doit voir.
2. **Une fourchette porte sa source et sa date.** Quand les sources divergent fortement (de 1 à 10 entre agences), on le dit et on explique le périmètre qui sépare. Aucune fourchette inventée : un poste sans source reste « non sourcé, devis à obtenir ».
3. **Le coût total, pas le coût de construction.** Exploitation, maintenance, abonnements, commissions, support, sécurité récurrente pèsent souvent plus que la construction. Le budget couvre trois ans.
4. **Les postes oubliés sont les premiers à lister.** Juridique, sécurité, contenus, marketing de lancement, frais de paiement, commissions des stores, outils, agents IA : `structure-budget.md` sert de liste de ratissage.
5. **La dérive est la norme.** 27 % en moyenne sur 1 471 projets informatiques, environ un projet sur six à +200 % (Flyvbjerg et Budzier). La réserve d'aléas se pose une fois ; l'arrêt est une option chiffrée.
6. **L'IA ne réduit pas le budget d'office.** Les gains mesurés sont incertains ; le scénario prudent n'en déduit aucun, et la sensibilité teste 0, 15 et 30 %.
7. **On calcule par script, pas de tête.** Estimations, indicateurs, trésorerie, sensibilité : un script ou tableur reproductible, joint au dossier.
8. **L'écart se montre.** Entre le budget souhaité et le budget estimé, on propose périmètre, délai ou moyens ; on ne l'absorbe pas.

## Méthode

1. **Reprendre les entrées** : charges O, M, P du `planificateur` (`planning.md`), architecture et hébergement de l'`architecte-solution` et de l'`ingenieur-devops`, prix du pôle commercial, exigences du cahier des charges.
2. **Choisir et croiser les méthodes d'estimation**, poser les réserves (`references/estimation.md`).
3. **Lister et chiffrer tous les postes** de construction et d'exploitation sur trois ans, avec la source de chaque fourchette (`references/structure-budget.md`).
4. **Bâtir les trois scénarios** et nommer les hypothèses qui les séparent.
5. **Justifier économiquement** : modèle, indicateurs unitaires, seuil de rentabilité, trésorerie sur 36 mois, rentabilité, sensibilité (`references/justification-economique.md`).
6. **Instruire les financements** possibles, sans les compter avant octroi (`references/financements-aides.md`).
7. **Rédiger `budget.md`** avec le gabarit, synthèse en tête, puis traiter les contrôles `FIN-` du jalon (`references/checklist-finance.md`).
8. **Faire relire** le chiffrage par les pôles concernés ; consigner leurs réserves.

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Ordres de grandeur et modèle économique | versés dans `01-decouverte/note-opportunite.md` | |
| Budget de construction et d'exploitation, justification économique, financements | `02-cadrage/budget.md` | `FIN-` |
| Budget révisé après conception | `02-cadrage/budget.md` (section datée) | `FIN-` |
| Réel contre budget | `07-exploitation/bilan-de-projet.md` (partie financière) | `FIN-` |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/estimation.md` | avant d'estimer : méthodes, trois points, réserves, dérives |
| `${CLAUDE_SKILL_DIR}/references/structure-budget.md` | pour lister et chiffrer les postes, et écrire `budget.md` |
| `${CLAUDE_SKILL_DIR}/references/justification-economique.md` | pour le modèle, les indicateurs, le seuil, la trésorerie, la sensibilité |
| `${CLAUDE_SKILL_DIR}/references/financements-aides.md` | pour les aides et financements, France, Union, Algérie |
| `${CLAUDE_SKILL_DIR}/references/checklist-finance.md` | pour traiter les contrôles `FIN-` du jalon |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, revues |

## Garde-fous

- Ne jamais inventer un chiffre, un barème ou un taux : écrire « non sourcé » ou « à vérifier ». Les fourchettes datent d'octobre 2026 et viennent surtout d'agences.
- Le livrable ne vaut pas avis d'expert-comptable : fiscalité, crédits d'impôt, actualisation, aides d'État et statut juridique sont marqués « à valider ».
- Le pôle ne décide seul ni du budget, ni du seuil d'arrêt, ni du plan de financement : ce sont des décisions de type 1 pour l'utilisateur.
- Une aide non octroyée n'entre jamais dans la trésorerie ; aucune démarche, demande ou paiement n'est déclenché sans accord de l'utilisateur.
