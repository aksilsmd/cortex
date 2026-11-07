# Formation — Tricentis Tosca (outil commercial d'automatisation par modèles)

Fiche de formation pour concepteur de tests, automaticien, exécutant, recetteur, testeurs web et mobile. Elle complète `formation-types-de-tests.md` et `tests-par-niveau.md`. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/tosca.md`. Versions : Tosca 2026.1 (documentation en ligne), 2025.1 LTS ; Tosca Cloud (SaaS).

**Outil commercial sous licence** : les agents Dan-Cortex ne disposent ni de licence ni d'accès Tosca ; ils n'en installent pas et n'ouvrent pas d'essai. Cette fiche sert à conseiller un client déjà équipé, à concevoir des cas transposables dans Tosca, à relire un référentiel exporté ou à comparer avec les outils libres.

## Sommaire
1. Objectifs
2. Positionnement
3. Concepts et sections
4. Automatisation par modèles : Modules, TestCases, XScan
5. Conception des cas : TestCase-Design
6. Exigences et couverture par les risques
7. Données de test
8. Exécution, agents, CI
9. Technologies couvertes et IA
10. Bonnes pratiques
11. Quand recommander Tosca (ou pas)
12. Check-list d'audit d'un référentiel Tosca
13. Anti-patterns et pièges
14. Sources

## 1. Objectifs

L'agent sait :
- expliquer le modèle Tosca (exigences pondérées, conception combinatoire, modules, cas, exécution) ;
- concevoir des cas de test structurés, transposables dans TestCase-Design ;
- relire un référentiel Tosca et repérer les défauts de structure ;
- recommander ou non Tosca face à Playwright, Robot Framework ou Cypress, selon le contexte, le coût et la compétence.

## 2. Positionnement

- Plateforme d'automatisation **sans code / à faible code** fondée sur des **modèles** (model-based test automation) : on décrit les écrans et interfaces une fois (Modules), puis on assemble des cas par paramétrage.
- Cible : grands comptes, progiciels (SAP, Salesforce, Oracle, Guidewire), applications hétérogènes (web, client lourd, mainframe, API, mobile), banques et assurances, contextes Cycle en V et forte traçabilité.
- Deux modes de déploiement : **Tosca** sur poste (Tosca Commander + référentiel partagé, serveur) et **Tosca Cloud** (SaaS, exécution élastique, Business Flow Designer).
- Coût : licences par utilisateur/agent négociées avec l'éditeur, non publiques — « à obtenir par devis ».

## 3. Concepts et sections

| Section | Rôle |
|---|---|
| **Requirements** | arbre d'exigences pondérées par le risque métier ; liens vers cas et exécutions ; couverture |
| **TestCase-Design** | conception structurée : classes, attributs, instances, combinaisons → TestSheets |
| **Modules** | modèles techniques des objets à piloter (écrans, contrôles, API), créés par scan |
| **TestCases** | cas composés de TestSteps qui réutilisent les Modules ; modèles (Templates) instanciés depuis TestCase-Design |
| **Execution** | ExecutionLists, journaux, résultats, exploratoire, exécution distribuée |
| **Issues** | anomalies liées aux journaux d'exécution (intégration Jira possible) |
| **Configurations** | paramètres de test centralisés (navigateur, environnement) |
| **Test Data Management** | gestion et réutilisation des données |
| **TestPlanning**, **Reporting** | planification et rapports d'état |

Vocabulaire clé : **Module**, **ModuleAttribute**, **TestStep**, **TestStepValue** (valeur + **ActionMode** : Input, Verify, Buffer, WaitOn, Select, Constraint…), **Buffer** (variable dynamique), **Reusable TestStepBlock** (bloc réutilisable), **Recovery Scenario** / **CleanUp Scenario**, **ExecutionList**.

## 4. Automatisation par modèles : Modules, TestCases, XScan

- **XScan** analyse l'application et crée des Modules (contrôles identifiés par propriétés techniques, ancres ou image) ; on garde les propriétés stables (id, nom accessible), on écarte les index et chemins absolus.
- Un Module par écran ou zone logique ; jamais de doublons (même écran scanné deux fois) : réutiliser et mettre à jour.
- TestCase = enchaînement de TestSteps sur des Modules ; ActionMode **Verify** pour les vérifications explicites ; **WaitOn** pour attendre un état (pas d'attente fixe).
- **Blocs réutilisables** (connexion, recherche produit) avec paramètres ; un bloc = une intention métier.
- **Recovery** (rétablir l'application après une erreur imprévue) et **CleanUp** (remettre l'état initial) au niveau des ExecutionLists.
- Tests API : Tosca API Scan, import OpenAPI ; combiner API pour préparer les données et UI pour le parcours.
- Réanalyse des Modules à grande échelle (Tosca Cloud) quand l'interface change : l'intérêt du modèle est de corriger une fois.

## 5. Conception des cas : TestCase-Design

- Décomposer le domaine en **attributs** (type de client, mode de paiement, montant) et **instances** (valeurs représentatives : partitions et limites).
- Marquer les instances **valides / invalides**, **straight-through** (chemin nominal) ; la combinatoire est générée selon une stratégie (toutes combinaisons, par paires, linéaire « une variation à la fois » depuis le chemin nominal).
- Le **TestSheet** liste les cas générés ; il est lié à un **Template** TestCase qui est instancié automatiquement (un cas par ligne).
- Règles : relier chaque attribut à une exigence ; éviter l'explosion combinatoire (≤ quelques dizaines de cas par TestSheet) ; préférer la variation linéaire puis compléter par paires pour les interactions à risque.
- Ces principes correspondent aux techniques ISTQB (partitions, valeurs limites, tables de décision, pairwise) : un cas conçu par Dan-Cortex selon `formation-types-de-tests.md` est transposable.

## 6. Exigences et couverture par les risques

- Arbre d'exigences (RequirementSets) pondéré par le **risque métier** (poids relatif : le processus le plus critique reçoit le poids le plus élevé ; méthode de calcul précise dans la doc « Weight your Requirements », à vérifier).
- Liens exigence ↔ TestCase ↔ ExecutionEntry ; tableau de bord de **couverture du risque** (conçu, automatisé, exécuté, réussi) et tendances.
- Usage : prioriser l'exécution par poids ; justifier un go/no-go par le pourcentage de risque couvert et réussi (ex. ≥ 95 % du risque pondéré exécuté et réussi, 0 échec sur les exigences de poids maximal — seuil à fixer dans la stratégie).
- Cohérent avec la stratégie par les risques ISTQB (probabilité × impact) : reporter la cotation du projet dans les poids.

## 7. Données de test

- Test Data Management : jeux de données réutilisables, réservation (un enregistrement consommé par une exécution), provisionnement.
- Données fictives ou anonymisées ; pas de données de production personnelles (RGPD).
- Buffers pour les valeurs dynamiques (numéro de commande) ; pas de valeurs codées en dur répétées dans les cas.

## 8. Exécution, agents, CI

- ExecutionLists par campagne (smoke, régression, recette) ; exécution locale, distribuée (agents) ou cloud (agents élastiques zero-footprint de Tosca Cloud).
- Intégration CI/CD : déclenchement d'ExecutionLists depuis Jenkins, Azure DevOps, GitLab… via les interfaces d'exécution Tricentis (API/CLI selon la version, à vérifier) ; résultats JUnit/rapports.
- Intégrations ALM : Jira, Azure DevOps, qTest (Tricentis), synchronisation d'exigences et d'anomalies.

## 9. Technologies couvertes et IA

- Web (navigateurs principaux), client lourd (Windows/.NET/Java), SAP GUI et Fiori, Salesforce, mainframe/terminal, API (REST/SOAP), mobile, PDF, bases de données.
- **Vision AI** (reconnaissance visuelle des contrôles, notamment pour applications difficiles à scanner ou environnements distants) et fonctions d'IA générative annoncées puis déployées progressivement : vérifier leur disponibilité dans la version et l'offre du client.
- Tricentis possède aussi qTest (gestion des tests), NeoLoad (performance), Testim (web à faible code).

## 10. Bonnes pratiques

- Structure de référentiel standardisée : dossiers par application → domaine → fonction, mêmes niveaux dans Requirements, TestCase-Design, Modules, TestCases, Execution.
- Nommage métier des cas et blocs ; conventions écrites et vérifiées.
- Modules uniques, propriétés d'identification stables ; demander aux développeurs des identifiants stables (`data-testid`, noms accessibles) dès la conception.
- Vérifications explicites (Verify) dans chaque cas ; pas de cas sans vérification.
- Blocs réutilisables plutôt que copies ; Templates + TestSheets plutôt que dizaines de cas clonés.
- Recovery et CleanUp définis ; cas indépendants.
- Revue par pair des Modules et des blocs ; gestion des versions du référentiel (check-in/check-out, branches selon l'offre).
- Mesures : taux d'automatisation par risque, taux de réussite, instabilité, temps de maintenance.

## 11. Quand recommander Tosca (ou pas)

| Contexte | Recommandation |
|---|---|
| Grand compte déjà équipé, SAP/progiciels, équipes QA fonctionnelles sans développeurs | Tosca pertinent : le valoriser plutôt que d'ajouter un autre outil |
| Paysage hétérogène (mainframe + web + client lourd) et forte traçabilité réglementaire | Tosca ou Robot Framework (libre) à comparer |
| Startup, PME, projet web/mobile moderne (cas Dan-Cortex courant), équipe technique | Playwright Test ou Cypress (libres, code versionné) ; Tosca surdimensionné et coûteux |
| Budget contraint, besoin de lisibilité métier | Robot Framework ou Cucumber |
Critères à chiffrer : coût de licences sur 3 ans, compétences disponibles (sur le marché algérien et français), dépendance à l'éditeur (référentiel propriétaire, export limité), intégration CI, maintenance.

## 12. Check-list d'audit d'un référentiel Tosca

- [ ] Exigences pondérées par le risque et liées aux cas ; couverture du risque suivie.
- [ ] Structure de dossiers homogène entre sections ; conventions de nommage respectées.
- [ ] Aucun Module en double ; propriétés d'identification stables (pas d'index).
- [ ] Cas construits à partir de blocs réutilisables et de Templates ; peu de cas clonés.
- [ ] Chaque cas contient des vérifications explicites ; pas d'attente fixe.
- [ ] Recovery et CleanUp définis ; cas indépendants et rejouables.
- [ ] Données de test fictives, gérées (TDM), sans valeur codée en dur répétée.
- [ ] ExecutionLists par campagne, déclenchées en CI ; résultats publiés et liés aux anomalies.
- [ ] Indicateurs : automatisation par risque, réussite, instabilité, maintenance.

## 13. Anti-patterns et pièges

- « Sans code » compris comme « sans conception » : référentiel enregistré-rejoué, cloné, impossible à maintenir.
- Modules rescannés à chaque changement au lieu d'être mis à jour.
- Explosion combinatoire dans TestCase-Design (des centaines de cas sans valeur).
- Poids d'exigences tous identiques : la couverture par le risque perd son sens.
- Données de production copiées dans les jeux de test.
- Recommander Tosca à un petit projet web par réflexe « outil de grand compte » ; ou promettre un prix sans devis.
- Prétendre qu'un agent a exécuté une campagne Tosca sans accès ni sortie à l'appui.

## 14. Sources

Consultées le 2026-11-03.
- Tricentis, Tosca 2026.1 – Plan, create and execute tests : https://docs.tricentis.com/tosca-2026.1/en-us/content/resources/webhelp/tosca_sections_overview.htm
- Tricentis, Tosca 2026.1 – Requirements : https://docs.tricentis.com/tosca-2026.1/en-us/content/requirements/rqm_introduction.htm
- Tricentis, Tosca 2026.1 – TestCase-Design : https://docs.tricentis.com/tosca-2026.1/en-us/content/testcase_design/testcase_design_intro.htm
- Tricentis, Tosca 2025.1 LTS – Key features : https://docs.tricentis.com/tosca-2025.1/en-us/content/release_notes/key_features.htm
- Tricentis, Tosca Cloud capabilities (avril 2025) : https://www.tricentis.com/news/tricentis-launches-cloud-capabilities-tosca-ai-powered-platform
- Tricentis, Test automation in 2026 : https://www.tricentis.com/resources/test-automation-in-2026-tosca
