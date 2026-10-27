# Orchestration du pôle Robustesse des agents

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle Sécurité. Les agents experts n'ont pas besoin de ce
fichier. Ce pôle n'a pas d'agent propre : le script fait l'audit, `auditeur-securite` mène les essais.

## Qui fait quoi

| Moment | Acteur | Mission | Sortie |
|---|---|---|---|
| J0, avant la première vague | chef d'orchestre, par script | `robustesse.py audit-config` ; constats `HIGH` soumis à l'utilisateur | `00-pilotage/audits/audit-reglages-agents.md` |
| Chaque ordre de mission avec recherche web | chef d'orchestre | ajouter la règle des contenus non fiables (`ROB-002`) | ordres de mission |
| J3, vague 3A, projets `ia` | `architecte-securite` | section « Fonctions d'IA » du modèle de menaces, parades par couche | `03-conception/securite/modele-menaces.md` |
| J3, vague 3B, projets `ia` | `auditeur-securite` | corpus de scénarios adapté au produit dans le plan de tests | `03-conception/securite/plan-tests-securite.md` |
| J5, vague 5A, projets `ia` | `auditeur-securite` | essais en recette, répétés ; live seulement après accord de l'utilisateur | `05-validation/rapport-robustesse-agents.md` |
| J7 | `auditeur-securite` | corpus de non-régression et déclencheurs de rejeu | `07-exploitation/bilan-de-projet.md` |

Activation : l'audit des réglages tourne pour toute mission, il ne coûte qu'un appel de script. Les vagues J3 à J7
ne partent que si le projet porte l'étiquette `ia`.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Section IA du modèle de menaces | `architecte-solution`, `delegue-protection-donnees` si données personnelles |
| Corpus de scénarios | `concepteur-tests` |
| Rapport de robustesse | `auditeur-general` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Garder un réglage de permission signalé `HIGH` | 1 | soumise à l'utilisateur |
| Lancer une évaluation live (consomme de l'usage) | 1 | soumise à l'utilisateur |
| Accepter un scénario en `FAIL` comme risque résiduel | 1 | go/no-go |
