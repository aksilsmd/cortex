# Découpage en lots

Comment transformer l'architecture et les spécifications en lots que des agents développent en parallèle sans se gêner. Résultat : `04-realisation/lots.md`, écrit avec `architecte-solution` et `planificateur`.

## Sommaire
1. Méthode
2. Règles de découpe
3. Contrat d'interface
4. Propriété des fichiers
5. Graphe et incréments
6. Gabarit de `lots.md`
7. Pièges fréquents
8. Contrôles avant de rendre
9. Sources

## 1. Méthode

1. Lister les modules de la SFD et les contextes bornés du modèle de données.
2. Découper chaque module en lots de **une à trois journées d'agent** : un lot dépasse rarement 400 lignes de différences utiles. Plus gros, la revue devient inefficace.
3. Écrire d'abord les **lots de fondation** : squelette généré, configuration, authentification, journalisation, schéma de base, composants partagés du système de design.
4. Écrire les **contrats d'interface** entre lots (section 3) et les figer.
5. Attribuer à chaque lot ses fichiers (section 4) et son développeur.
6. Dessiner le graphe de dépendances, en déduire les incréments (section 5).
7. Rattacher chaque lot à ses `FN-`, `RG-`, `WF-`, `EC-` et `CT-`.

## 2. Règles de découpe

| Critère | Choix |
|---|---|
| Le lot touche serveur et interface | le séparer : un lot par agent, relié par un contrat |
| Deux lots modifient la même table | un seul propriétaire du schéma ; l'autre demande une migration |
| Un composant est partagé | lot de fondation, livré dans l'incrément 1 |
| Le lot attend un service tiers | développer contre une simulation du contrat, intégrer ensuite |
| La reprise de données est requise | lot d'intégrateur dédié, après validation du schéma |
| Le lot est purement répétitif (écrans de saisie, CRUD) | générateur officiel, modèle léger (`references/sobriete-code.md`) |

## 3. Contrat d'interface

Le contrat est un fichier exécutable versionné dans le dépôt, le document y renvoie. Il couvre : description formelle (OpenAPI, AsyncAPI, JSON Schema, types partagés), erreurs, idempotence, pagination, versionnement. Le détail des rubriques est dans `specifications/references/specs-techniques.md`, section 2.

- Le contrat se **fige** avant le premier développeur. Toute modification passe par `architecte-solution` et prévient les lots consommateurs.
- Le fournisseur publie un exemple de réponse par cas (succès, chaque erreur) : le consommateur développe contre cet exemple.
- Un test de contrat vérifie les deux côtés (Pact, ou Schemathesis depuis OpenAPI) : il protège de la dérive silencieuse.

## 4. Propriété des fichiers

Chaque lot déclare des chemins ou des motifs de fichiers dont il est seul propriétaire. Un agent n'écrit **que** dans ses chemins ; pour toute autre modification, il l'écrit dans son compte rendu, rubrique « Renforts demandés ». Les fichiers communs (configuration, routes, dépendances, schéma de base) appartiennent à un lot de fondation ou à l'`integrateur`, et se modifient par demande. En mode `integral`, un worktree git par lot rend l'isolement mécanique.

## 5. Graphe et incréments

Une arête « A → B » signifie « B consomme un contrat ou des fichiers de A ». Un **incrément** regroupe les lots sans arête entre eux. Règles :

- l'incrément 1 contient les fondations et un parcours de bout en bout minimal (tranche verticale) : il prouve la pile ;
- un incrément livre de la valeur testable de bout en bout, pas seulement des couches techniques ;
- les lots à risque (paiement, migration, intégration tierce) passent tôt ;
- un cycle dans le graphe signale un mauvais découpage : fusionner les deux lots ou extraire le contrat commun.

## 6. Gabarit de `lots.md`

```markdown
# Lots de réalisation — <nom du projet>

## Synthèse
<Nombre de lots, d'incréments, lots à risque, contrats figés, écarts à l'architecture, points « à vérifier ».>

## 1. Lots
| ID | Lot | Agent | Incrément | Dépend de | Couvre | Fichiers propres |
|---|---|---|---|---|---|---|
| LOT-001 | Fondation serveur | developpeur-backend | 1 | - | EXNF-003, ADR-001 | `code/server/core/**` |

## 2. Contrats d'interface
| ID | Contrat | Fournisseur | Consommateurs | Fichier exécutable | Statut |
|---|---|---|---|---|---|
| IF-01 | API commandes | LOT-004 | LOT-007, LOT-009 | `code/contracts/commandes.yaml` | figé |

## 3. Graphe de dépendances
<Schéma Mermaid ou liste des arêtes.>

## 4. Incréments
| Incrément | Lots | Valeur testable | Cas de test visés |
|---|---|---|---|
| 1 | LOT-001, LOT-002 | connexion de bout en bout | CT-001 à CT-006 |

## 5. Outillage de contrôle
<Commandes uniques de vérification par lot, seuils de qualité, via `essais.py`.>

## 6. Risques et questions ouvertes
```

## 7. Pièges fréquents

- Contrat décrit en prose seulement : deux agents l'interprètent différemment.
- Lot « divers » ou « utilitaires » qui devient le dépotoir partagé.
- Découpe par couche technique seule : rien n'est testable avant la fin.
- Fichiers de configuration modifiés par tous : conflits permanents.
- Incrément 1 trop ambitieux : l'échec de la pile se découvre tard.

## 8. Contrôles avant de rendre

- Chaque `FN-` est couvert par au moins un lot.
- Chaque contrat a un fichier exécutable, un fournisseur et un exemple par cas.
- Aucun chemin n'appartient à deux lots.
- Le graphe n'a pas de cycle.
- Chaque incrément a une valeur testable et des `CT-` visés.

## Sources

- ISO/IEC 25010:2023, modèle de qualité (compatibility : tests de contrat), état : octobre 2026.
- DORA 2025 : petits lots et retours rapides, https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Pact, tests de contrat : https://docs.pact.io ; Schemathesis : https://schemathesis.readthedocs.io
- Claude Code, sous-agents et contexte isolé : https://code.claude.com/docs/en/sub-agents
- Pratique d'expert (non sourcée) : contrats figés avant parallélisation, un worktree git par agent.
