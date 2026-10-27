# Tests par niveau : objectif, propriétaire, outils, seuils

Choisir pour chaque niveau de test un objectif, un propriétaire, un outil, un temps cible et un seuil, puis dériver les cas des règles de gestion et de la matrice d'interactions. Vocabulaire : ISTQB CTFL v4.0.1. État : octobre 2026. Les versions d'outils n'ont pas été vérifiées : les relever dans `package.json`, `pyproject.toml` ou `pom.xml` du projet, jamais de mémoire.

## Sommaire
1. Forme de la stratégie
2. Tableau des niveaux
3. Seuils transverses
4. Dériver les cas de test
5. Données de test
6. Pièges
7. Contrôles avant de rendre

## 1. Forme de la stratégie

- **Domaine métier** : pyramide, beaucoup de tests unitaires rapides.
- **API et front** : plutôt un diamant, avec des tests d'intégration et de contrat riches.
- **Bout en bout** : rares, réservés aux parcours critiques (liste versionnée).
- BDD (Gherkin) seulement si le métier lit les scénarios ; sinon des tests lisibles suffisent. TDD pour la logique métier.
- Pourquoi : un test coûte d'autant plus cher qu'il est haut dans la pile (lenteur, instabilité). Ne monter que si un niveau inférieur ne peut pas prouver la règle.

## 2. Tableau des niveaux

Colonne « Qui » : D = développeur du lot, A = `automaticien-tests`, R = `recetteur`, C = `concepteur-tests` (conçoit les cas).

| Niveau | Objectif | Qui | Outils (JS/TS · Python · Java · Go) | Seuil |
|---|---|---|---|---|
| Unitaire | logique isolée, rapide, déterministe, sans réseau ni horloge réelle | D | Vitest ou Jest · pytest + Hypothesis · JUnit 5 · `go test` | couverture du code nouveau ≥ 80 % (valeur « Sonar way », à calibrer par pile) ; mutation mesurée sur le cœur métier, seuil à fixer dans la stratégie |
| Intégration et composant | code contre vraies dépendances éphémères (base, file, cache) | D puis A | Testing Library + msw · pytest + Testcontainers · JUnit + Testcontainers · testcontainers-go | aucun mock de base de données ; chaque requête et migration exécutée au moins une fois |
| Fonctionnel | une règle de gestion RG- ou une fonction FN- de bout en bout du module | A | les outils d'API ou de E2E ci-dessous | chaque RG- a au moins un cas nominal et un cas limite |
| API et contrat | statuts, schémas, authentification, autorisation ; compatibilité consommateur-fournisseur | A | supertest · pytest + httpx · REST Assured · httptest ; Bruno ou Newman ; Pact ; Schemathesis ; Spring Cloud Contract | par endpoint : nominal, 4xx, autorisation, schéma ; contrat Pact dès qu'un consommateur dépend d'une autre équipe |
| Bout en bout web | parcours critiques en vrai navigateur | A | Playwright (agents de test depuis la 1.56) ou Cypress | 100 % des parcours critiques ; traces conservées ; ordre aléatoire (`--shuffle`) ; zéro attente fixe |
| Bout en bout mobile | parcours critiques sur émulateur puis appareil | A | Maestro · Detox (React Native) · Appium (natif multi-plateforme) | parcours critiques sur émulateur en CI ; appareils réels avant chaque version publiée |
| Performance | charge, endurance, pic ; tenue des objectifs de niveau de service | A | k6 · Locust · Gatling ou JMeter | EXNF chiffrées (p95, taux d'erreur) ; scénarios versionnés ; comparaison à la référence du jalon précédent |
| Accessibilité | violations WCAG automatisables, puis audit manuel | A puis expert-accessibilite | axe-core via `@axe-core/playwright` · pa11y · Lighthouse | WCAG 2.2 AA (ISO/IEC 40500:2025) ; 0 violation sérieuse ou critique ; audit clavier et lecteur d'écran à chaque jalon |
| Non-régression | rejouer les tests stables après chaque correction ou candidat de version | `executant-tests` | sélection par étiquette `@regression` dans les suites | 100 % au vert avant tout passage de jalon |
| Statique et architecture | normes, types, couches, cycles | D, `gardien-des-normes` | voir `normes-developpement.md` ; dependency-cruiser · import-linter · ArchUnit | bloquant en CI |

Mobile et web partagent les parcours : un cas CT- par parcours, deux implémentations.

Cadre d'exigence d'accessibilité : l'EN 301 549 v3.2.1 reste à WCAG 2.1 AA alors que la 2.2 est de plus en plus attendue ; le RGAA : non vérifié à la source. Vérifier l'exigence contractuelle ou légale avant de fixer le niveau.

## 3. Seuils transverses

- Un test instable est mis en quarantaine avec une anomalie sous 48 h. Il n'est jamais relancé « jusqu'au vert ».
- Les tests unitaires ne touchent ni réseau ni horloge réelle ; aucun test sans assertion (règle de lint).
- Une assertion modifiée par un agent (dont le « healer » de Playwright, qui peut affaiblir un test pour le faire passer) est revue comme un changement de comportement.
- Temps cibles à écrire dans la stratégie : unitaires en minutes, bout en bout en dizaines de minutes ; à défaut, la CI devient contournée.

## 4. Dériver les cas de test

Techniques ISTQB : partition d'équivalence, valeurs limites, table de décision, transitions d'états, cas d'utilisation.

| Source | Technique | Cas à produire |
|---|---|---|
| Règle de gestion RG- à seuil ou à plage | valeurs limites, partitions | valeur minimale, minimale moins un, maximale, maximale plus un, vide, type invalide |
| RG- à plusieurs conditions | table de décision | une colonne par combinaison utile ; combinaisons impossibles écartées par écrit |
| Objet à cycle de vie (commande, dossier, paiement) | transitions d'états | chaque transition autorisée, puis chaque transition interdite attendue en refus |
| Ligne de la matrice d'interactions (EL-) | une action, une réaction | cas nominal, puis chaque message d'erreur exact de la colonne « Erreurs et états » |
| Destination avec plusieurs cas `EC-a (succès) / EC-b (échec)` | un cas par branche | l'écran atteint est vérifié dans chaque branche |
| Condition de rôle ou de masquage | partition par rôle | rôle autorisé, rôle refusé, visiteur anonyme |
| Workflow WF- | cas d'utilisation | chemin nominal, chaque exception, retour arrière |
| Élément de type `automatique` | contrôle du délai | expiration de session, minuterie, perte de connexion |

Règle : un cas par ligne EL- à effet métier. Les éléments purement décoratifs ou de navigation simple sont couverts par le CT- de leur workflow (le script de traçabilité accepte l'un ou l'autre). Une EXNF est couverte par un CT- de performance, d'accessibilité ou de sécurité.

Cas oubliés à ajouter à chaque écran : double clic, retour du navigateur, rafraîchissement, hors-ligne, session expirée, droits insuffisants, donnée à la limite de longueur.

## 5. Données de test

- Factories ou graines déterministes ; une donnée par test, non partagée (le partage crée des tests dépendants de l'ordre).
- Aucune donnée de production non anonymisée, ni dans les tests ni en recette (RGPD, minimisation). Anonymisation à valider avec le délégué à la protection des données.
- Environnement éphémère par demande de fusion ou par campagne ; jeux de données versionnés avec le harnais.
- Comptes de test par rôle, listés dans le plan de recette, sans mot de passe réel dans le dépôt.
- Dates, devises, langues et fuseaux limites inclus si le projet est multilingue ou international.

## 6. Pièges

- Couverture confondue avec qualité : un agent écrit des tests qui épousent son code. Ajouter mutation et relecture des assertions.
- Bout en bout instables : ordre dépendant, données partagées, attentes fixes.
- Seuil Sonar appliqué au code ancien (blocage) ou code généré logé dans l'ancien code (oublié) : mesurer le code nouveau et poser un plancher non régressif sur le global.
- Gate bâti sur les « Security Hotspots », en cours de suppression chez Sonar : passer aux issues de sécurité.
- Automatisation d'un test non conçu : un cas se conçoit et se trace d'abord (CT-), s'automatise ensuite.

## 7. Contrôles avant de rendre

- Chaque niveau a un outil, un propriétaire, un temps cible et un job de CI nommés.
- Chaque RG- et chaque transition d'état ont un cas ; chaque transition interdite a un cas de refus.
- Les seuils sont chiffrés ; les valeurs non confirmées sont marquées « à vérifier ».
- Les jeux de données ne contiennent aucune donnée personnelle réelle.

## Sources

- ISTQB, syllabus Certified Tester Foundation Level v4.0.1 (niveaux, types, techniques de conception).
- ISO/IEC/IEEE 29119-1:2022, concepts et vocabulaire des tests logiciels.
- ISO/IEC 25010:2023, modèle de qualité du produit (neuf caractéristiques).
- W3C, WCAG 2.2, approuvée ISO/IEC 40500:2025 (annonce du 21 octobre 2025).
- Sonar, documentation des « quality gates » de SonarQube Server (gate « Sonar way »).
- Playwright, documentation « Test Agents » (planner, generator, healer) : https://playwright.dev/docs/test-agents
- DORA 2025, rapport sur l'IA dans le développement logiciel (Google Cloud, 2025).
