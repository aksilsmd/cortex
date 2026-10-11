# Orchestration du pôle Réalisation et qualité

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `developpeur-backend` | B | J4, un par lot serveur ; repris pour chaque correction |
| `developpeur-frontend` | B | J4, un par lot d'interface web |
| `developpeur-mobile` | B | J4, un par lot d'application mobile |
| `integrateur` | B | J4, lots d'intégration, de paramétrage de progiciel, de reprise de données |
| `relecteur-code` | B | J4, après chaque lot livré, sur les différences seulement |
| `concepteur-tests` | B | J3 (stratégie, recette) ; J4, vague 4A (harnais, jeux de données) |
| `automaticien-tests` | B | J4 après chaque incrément (fonctionnel, API, bout en bout) ; J5 (performance) |
| `recetteur` | B | J5, vague 5A |
| `executant-tests` | C | partout où une suite se rejoue : non-régression, contre-tests |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J4, 4A | `concepteur-tests` : harnais et jeux de données ; hors pôle : lots et contrats (`planificateur`, `architecte-solution`), dépôt et intégration continue (`ingenieur-devops`), outils de normes (`gardien-des-normes`) | architecture validée, cahier de recette | `lots.md`, outillage, harnais |
| J4, 4B-1 (incrément n) | un développeur par lot indépendant : tests unitaires puis code | `lots.md`, contrats, SFD du lot, normes | lots livrés, journal de build |
| J4, 4B-2 | `relecteur-code` et `gardien-des-normes` sur les différences ; `automaticien-tests` : tests du lot ; `auditeur-securite` : contrôles automatisés | lots livrés | notes de revue, suites de tests, constats |
| J4, 4B-3 | développeurs repris pour corriger ; `executant-tests` : non-régression | anomalies, constats | lots corrigés, journal à jour |
| J5, 5A | `recetteur` : campagne ; `automaticien-tests` : performance ; `auditeur-securite`, `testeur-intrusion`, `expert-accessibilite` (autres pôles) | produit déployé en recette | `pv-recette.md`, rapports |
| J5, corrections | développeurs repris ; `executant-tests` : contre-tests et non-régression | anomalies | PV levé de ses réserves |

Les vagues 4B se répètent par incrément ; le suivant peut démarrer pendant le 4B-2 du précédent si ses lots n'en dépendent pas.

## Essaimage

- **Lots :** une instance de développeur par lot indépendant du même incrément, chacune avec son seul dossier de lot, les contrats qu'elle consomme ou fournit et la liste de ses fichiers.
- **Relecture :** une instance de `relecteur-code` par lot, jamais l'auteur ; deux relecteurs en mode `integral`.
- **Tests :** une instance d'`automaticien-tests` par niveau (API, bout en bout) au-delà de dix cas par lot ; `executant-tests` par suite.
- **Recette :** une instance de `recetteur` par module au-delà de cinquante cas, le noyau commun à une seule.

## Dépendances à respecter

Les contrats d'interface sont figés avant le premier développeur. L'intégrateur de reprise de données attend le schéma validé. Pas de bout en bout avant la livraison des lots traversés. Les tests de sécurité complets et d'intrusion attendent un environnement de recette stable et l'autorisation écrite.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Lot de code | `relecteur-code`, `gardien-des-normes`, `auditeur-securite` |
| `lots.md` et contrats | `architecte-solution`, `developpeur-backend` ou `developpeur-frontend` concerné |
| Tests automatisés d'un lot | `concepteur-tests` (assertions réelles), `relecteur-code` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Écart à un contrat d'interface ou à une ADR | 1 si le contrat est publié ou partagé, sinon 2 | comité d'architecture |
| Abaissement d'un seuil de qualité | 2 | arbitrage direct du chef d'orchestre, tracé |
| Anomalie bloquante sans correction possible | 1 | comité de go/no-go |
| Livraison avec réserves | 1 | comité de go/no-go |

## Sortie du pôle par jalon

- **J4 :** tous les lots livrés ; tests unitaires, fonctionnels, d'API et de bout en bout au vert ; normes respectées ; aucune anomalie bloquante ; contrôles `DEV-` et `TST-` de jalon J4 traités.
- **J5 :** `pv-recette.md` signé par l'utilisateur ; contrôles de jalon J5 traités.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | lots plus gros ; contrôles automatiques à la place de `relecteur-code` ; un `concepteur-tests` fait aussi automatisation et recette |
| `standard` | comme décrit |
| `integral` | deux relecteurs par lot ; tests de mutation sur le cœur métier ; un worktree git par lot ; essai de bascule en recette |

## Outils extérieurs

Si un connecteur de gestion de tests (Xray, Squash TM, TestRail) ou de suivi de tickets est présent, y verser anomalies et cas ; sinon le registre des anomalies de `cortex.py` fait foi. Aucune action sur un dépôt distant sans accord explicite.
