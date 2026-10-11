# Orchestration du pôle Architecture et normes

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `architecte-solution` | A | J1 (faisabilité, acheter ou construire) ; J2 (relecture du cahier des charges) ; J3, vague 3A ; J4, vague 4A (lots) |
| `architecte-donnees` | B | J3, vague 3A ; repris en J4 pour les migrations et la revue du schéma |
| `gardien-des-normes` | B | J3, après le comité d'architecture ; J4, vagues 4A puis chaque incrément |
| `ingenieur-devops` | B | J3, après le comité d'architecture ; J4, vague 4A ; J5 et J6 |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J1, 1A | `architecte-solution` : acheter, configurer ou construire, risques techniques | fiche projet, note d'opportunité en cours | `01-decouverte/note-faisabilite-technique.md` |
| J2, 2A | `architecte-solution` en revue : faisabilité du cahier des charges | cahier des charges | constats au registre |
| J3, 3A-1 | `architecte-solution` : options, grille, tranche verticale, ADR « proposée », dossier ; `architecte-donnees` : modèle conceptuel et logique, options de moteur | cahier des charges, SFG en cours, cartographie des données, analyse de risques | `architecture/dossier-architecture.md`, `adr/`, `modele-donnees.md` |
| Réunion | comité d'architecture | ADR proposées | décisions `DEC-` validées |
| J3, 3A-2 | `gardien-des-normes` : normes et dépendances ; `ingenieur-devops` : infrastructure ; `architecte-donnees` repris : modèle physique | ADR validées | `normes-developpement.md`, `dependances.md`, `infrastructure.md` |
| J4, 4A | `architecte-solution` avec `planificateur` : lots et contrats d'interface ; `gardien-des-normes` : outils de contrôle ; `ingenieur-devops` : dépôt, intégration continue, environnements | architecture validée | `04-realisation/lots.md`, outillage |
| J4, 4B et suivantes | `gardien-des-normes` sur les différences ; `architecte-donnees` pour les migrations ; `architecte-solution` si une règle d'architecture échoue | code des lots | constats, ADR mises à jour |
| J5, 5A | `ingenieur-devops` : répétition de déploiement, restauration | produit en recette | preuves d'infrastructure |
| J6, 6A | `ingenieur-devops` : supervision, alertes, retour arrière | plan de lancement | contrôles d'infrastructure traités |

Le comité sépare 3A-1 de 3A-2 : normes et infrastructure dépendent du langage et de l'hébergement retenus.

## Essaimage

- **Évaluation d'options :** une instance d'`architecte-solution` par option candidate (deux à trois) pour la tranche verticale et la notation, le même gabarit d'ADR en entrée ; une instance finale compare.
- **Modèle de données :** une instance d'`architecte-donnees` par contexte borné au-delà de quatre modules ; le noyau commun (identité, locataires, audit) va à une seule instance, écrit avant.
- **Normes :** une instance de `gardien-des-normes` par langage.

## Dépendances à respecter

Les exigences non fonctionnelles chiffrées précèdent le choix du style. Le comité d'architecture précède normes, infrastructure et lots. `architecte-donnees` a besoin de la cartographie des données (`02-cadrage/cartographie-donnees.md`) et de la SFG.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Dossier d'architecture et ADR | `architecte-securite`, `ingenieur-devops`, `redacteur-specs-techniques`, `controleur-financier` (coût sur 3 à 5 ans), `contradicteur` en `integral` |
| Modèle de données | `delegue-protection-donnees`, `architecte-securite`, `redacteur-sfd`, `concepteur-tests` |
| Normes et dépendances | `relecteur-code`, `auditeur-securite`, `juriste-numerique` (licences) |
| Infrastructure | `architecte-securite`, `controleur-financier` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Acheter, configurer ou construire | 1 | comité d'opportunité (J1) puis comité d'architecture |
| Langage, frameworks structurants | 1 | comité d'architecture, collégiale, deux options au moins |
| Style d'architecture (monolithe modulaire, microservices) | 1 | comité d'architecture |
| Moteur de base, schéma, modèle de tenancy | 1 | comité d'architecture |
| Hébergement et fournisseur | 1 | comité d'architecture |
| Dépendance majeure, outil de test ou de build | 2 | arbitrage direct ou panel |

Ordre du jour : exigences, options notées, risques, recommandation. Chaque décision finit en ADR et au registre.

## Sortie du pôle par jalon

- **J1 :** note de faisabilité présente, contrôles `ARC-` de J1 traités.
- **J2 :** revue d'architecte du cahier des charges au registre.
- **J3 :** dossier, ADR validées, modèle de données, normes, dépendances, infrastructure présents ; contrôles `ARC-` et `DON-` de J3 traités ; décisions de type 1 validées par l'utilisateur.
- **J4 :** outillage branché, règles d'architecture en intégration continue, contrôles de J4 traités.
- **J5 :** restauration et déploiement répétés, dossier d'architecture à jour.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | `architecte-solution` seul absorbe données, normes et infrastructure ; deux options notées dans une ADR unique ; arbitrage direct |
| `standard` | comme décrit |
| `integral` | deux options instruites en parallèle, évaluation de scénarios avec parties prenantes, `contradicteur` sur le modèle de la session, relecteur indépendant du dossier, revue d'architecte avant chaque incrément |

## Outils extérieurs

Sans connecteur de diagrammes, écrire les schémas C4 en Mermaid dans le dossier d'architecture.
