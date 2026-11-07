# Formation — Robot Framework : tests d'acceptation par mots-clés

Fiche de formation pour concepteur de tests, automaticien, exécutant, recetteur, testeurs web et mobile. Elle complète `formation-types-de-tests.md` et `tests-par-niveau.md`. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/robot-framework.md`. Versions de référence : Robot Framework 7.4.x / 7.5 (septembre 2026, à vérifier), Browser library 19.x (Playwright 1.59, Python ≥ 3.10, Node LTS).

## Sommaire
1. Objectifs
2. Quand choisir Robot Framework
3. Écosystème de bibliothèques
4. Structure d'un projet
5. Syntaxe essentielle
6. Écrire de bons mots-clés
7. Données, variables, secrets
8. Web avec Browser library
9. API, base de données, mobile
10. Exécution, tags, rapports, CI
11. Lien avec Xray / Squash / Jira
12. Exemple complet
13. Check-list d'audit
14. Anti-patterns et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- décider si Robot Framework est adapté (équipe, système, lisibilité métier) ;
- structurer suites, ressources, bibliothèques et données ;
- écrire des mots-clés métier lisibles qui cachent la technique ;
- automatiser web (Browser), API (Requests), mobile (Appium) et base de données ;
- exécuter en CI avec tags, parallélisme (Pabot), relance des échecs et rapports exploitables.

## 2. Quand choisir Robot Framework

| Pour | Contre |
|---|---|
| Tests d'acceptation et de bout en bout lisibles par le métier (style mots-clés ou BDD) | Tests unitaires et de composant : utiliser le framework du langage (pytest, Vitest) |
| Équipe QA mixte (testeurs fonctionnels + automaticiens Python) | Équipe 100 % front TypeScript : Playwright Test est plus direct |
| Systèmes hétérogènes : web, API, SSH, bases, mainframe, desktop (RPA), mobile dans un même outil | Besoin de débogage pas à pas très fin dans le code |
| Contextes Cycle en V / bancaires avec traçabilité vers Xray ou Squash | Suites très volumineuses sans discipline : dérive en « scripts en français » illisibles |

Libre (Apache 2.0), soutenu par la Robot Framework Foundation, écrit en Python ; extensible par bibliothèques Python.

## 3. Écosystème de bibliothèques

| Besoin | Bibliothèque | Remarque |
|---|---|---|
| Web moderne | **Browser** (robotframework-browser, Playwright) | recommandé : auto-attente, contextes isolés, traces ; nécessite Node |
| Web historique | SeleniumLibrary | parc existant ; plus d'attentes explicites à gérer |
| API REST | RequestsLibrary (+ JSONLibrary) | sessions, statuts, JSON |
| Base de données | DatabaseLibrary | requêtes de vérification, jeux de données |
| Mobile natif | AppiumLibrary | Appium 2 + pilotes UiAutomator2 / XCUITest |
| SSH / systèmes | SSHLibrary, Process, OperatingSystem | intégration et exploitation |
| Fichiers, Excel, PDF | bibliothèques RPA (RPA Framework) | vérifier la maintenance |
| Parallélisme | **Pabot** | suites ou tests en parallèle |
| Qualité du code de test | **Robocop** (lint), **Robotidy** (formatage) | à brancher en CI |
| Intégré | BuiltIn, Collections, String, DateTime, XML, Dialogs (à proscrire en CI) | |

## 4. Structure d'un projet

```
tests/
  acceptance/
    panier.robot            # suites : cas de test, lisibles métier
    paiement.robot
resources/
  keywords/panier.resource  # mots-clés métier
  pages/panier_page.resource # mots-clés techniques (localisateurs)
  common.resource           # Setup/Teardown, imports
libraries/
  donnees.py                # bibliothèque Python maison (fabriques de données)
data/
  environnements/recette.yaml
results/                    # ignoré par Git
```
- Trois couches : **cas de test** (quoi, vocabulaire métier) → **mots-clés métier** (comment, en étapes) → **mots-clés techniques / bibliothèques** (localisateurs, appels).
- Un fichier `.resource` ne contient pas de cas de test ; une suite `.robot` n'importe que des ressources.

## 5. Syntaxe essentielle

- Sections : `*** Settings ***`, `*** Variables ***`, `*** Test Cases ***` (ou `*** Tasks ***` pour la RPA), `*** Keywords ***`, `*** Comments ***`.
- Séparateur : **au moins deux espaces** (quatre recommandés) entre mot-clé et arguments.
- Variables : scalaire `${nom}`, liste `@{items}`, dictionnaire `&{donnees}`, environnement `%{VAR}` ; portée avec `VAR` (RF ≥ 7 : `VAR    ${x}    valeur    scope=SUITE`).
- Contrôle : `IF / ELSE IF / ELSE / END`, `FOR ... IN ... END`, `WHILE`, `TRY / EXCEPT / FINALLY`, `BREAK`, `CONTINUE`, `RETURN` — à limiter dans les cas de test (la logique va dans les mots-clés ou en Python).
- Réglages : `[Documentation]`, `[Tags]`, `[Setup]`, `[Teardown]`, `[Template]` (tests pilotés par données), `[Timeout]`, `[Arguments]` ; au niveau suite : `Suite Setup`, `Test Setup`, `Test Tags`, `Test Timeout`.
- Arguments typés et nommés : `[Arguments]    ${montant: int}    ${devise}=DZD`.
- Mots-clés à arguments intégrés : `L'acheteur ajoute "${produit}" au panier`.
- Style BDD : préfixes `Given/When/Then/And/But` ignorés à l'exécution (et localisés en français : `Étant donné`, `Quand`, `Alors`… selon la langue déclarée `Language: French`, à vérifier).

## 6. Écrire de bons mots-clés

- Un cas de test se lit comme une procédure métier : 3 à 10 lignes, sans localisateur ni URL.
- Nom de mot-clé = action métier au présent, sans détail technique (« Payer Par Carte » et non « Cliquer Sur #btn-pay »).
- Un mot-clé fait une chose ; ≤ 10–15 lignes ; pas de dépendance à l'état laissé par un autre test.
- Les vérifications sont explicites (`Le Total Du Panier Doit Être    12 500 DZD`), jamais cachées dans une action.
- Logique complexe (calculs, fabriques, appels multiples) → bibliothèque Python testée.
- Documentation `[Documentation]` sur chaque mot-clé public ; Libdoc génère le catalogue (`libdoc resources/keywords/panier.resource panier.html`).

## 7. Données, variables, secrets

- Fichiers de variables par environnement (YAML ou Python) : `robot --variablefile data/environnements/recette.yaml`.
- Secrets par variables d'environnement `%{MDP_TEST}` injectées par la CI ; masquer dans les journaux (`Set Log Level    NONE` autour, ou mot-clé de saisie qui ne journalise pas — Browser : `Fill Secret`).
- Données fictives créées par le test (API ou fabriques), nettoyées en Teardown ; aucune donnée personnelle réelle.
- Tests pilotés par données : `[Template]` + tableau, ou DataDriver (CSV/Excel) pour les partitions et valeurs limites.

## 8. Web avec Browser library

- Hiérarchie : `New Browser` (chromium/firefox/webkit, headless) → `New Context` (isolation, viewport, locale, fuseau, storage state) → `New Page`.
- Sélecteurs : `role=button[name="Ajouter au panier"]`, `text=`, `id=`, `data-testid=` (via `Set Selector Prefix` ou stratégie), `css=` en dernier recours ; chaînage `>>`.
- Auto-attente : `Click`, `Fill Text`, `Get Text    sel    ==    attendu` (assertion intégrée avec opérateur) ; pas de `Sleep`.
- Authentification : `Save Storage State` puis `New Context    storageState=...`.
- Réseau : `Wait For Response`, `Route URL` pour simuler un tiers.
- Preuves : `Take Screenshot`, trace Playwright (`New Context    tracing=...`), vidéo.
- Mobile web : `Get Device    Pixel 7` puis `New Context    &{device}`.

## 9. API, base de données, mobile

- API (RequestsLibrary) : `Create Session`, `GET On Session    expected_status=200`, vérification du schéma (bibliothèque JSON Schema) ; tester 4xx, droits par rôle, pagination.
- Base : `Connect To Database`, `Query`, `Row Count Is Equal To X` ; lecture seule sur les environnements partagés.
- Mobile (AppiumLibrary) : serveur Appium 2, capacités (`platformName`, `appium:automationName=UiAutomator2`), localisateurs par `accessibility_id` (qui sert aussi l'accessibilité) ; interruptions et réseau à tester (voir fiche types de tests).

## 10. Exécution, tags, rapports, CI

- `robot -d results --include smoke --exclude wip tests/` ; tags : `smoke`, `regression`, `critique`, ID d'exigence (`EX-012`), persona.
- Relance des échecs : `robot --rerunfailed results/output.xml -o rerun.xml` puis `rebot --merge results/output.xml results/rerun.xml` ; un test vert au second passage est signalé instable.
- Parallélisme : `pabot --processes 4 ...` ; données et comptes isolés par processus.
- Rapports : `log.html` (détail), `report.html` (synthèse), `output.xml` (machine) ; `--xunit` pour la CI ; `rebot` pour fusionner.
- Statuts : PASS, FAIL, SKIP (`Skip If`) ; un test non applicable est SKIP motivé, pas supprimé.
- Listeners (API v3) pour publier vers un outil de gestion des tests ou un tableau de bord.
- CI : conteneur avec Python + Node (Browser : `rfbrowser init` pour les navigateurs), Robocop bloquant, artefacts `results/` conservés.

## 11. Lien avec Xray / Squash / Jira

- Tag par cas : ID du test Xray/Squash (`XRAY-123`) ou ID d'exigence ; import du résultat `output.xml` ou JUnit dans Xray (Robot Framework est un format d'import pris en charge) ou dans Squash TM (connecteur Squash AUTOM).
- Une exécution = une campagne/test execution, avec environnement et version testée.
- Ne pas dupliquer le pas-à-pas dans l'outil et dans le `.robot` : l'outil porte le cas et la traçabilité, le `.robot` porte l'automatisation.

## 12. Exemple complet

```robotframework
*** Settings ***
Documentation     Panier — acheteur connecté (EX-012, EX-014)
Resource          ../../resources/common.resource
Resource          ../../resources/keywords/panier.resource
Suite Setup       Ouvrir Le Navigateur De Test
Test Setup        Se Connecter En Tant Que    acheteur
Test Teardown     Vider Le Panier
Suite Teardown    Close Browser    ALL
Test Tags         panier    regression

*** Test Cases ***
Le total du panier est affiché en dinars
    [Tags]    smoke    EX-012
    Ajouter Au Panier    Tapis kabyle
    Le Total Du Panier Doit Être    12 500 DZD

Seuil de livraison gratuite
    [Template]    Frais De Livraison Pour Un Panier De
    4 999    500 DZD
    5 000    0 DZD
    5 001    0 DZD

*** Keywords ***
Frais De Livraison Pour Un Panier De
    [Arguments]    ${montant}    ${frais_attendus}
    Préparer Un Panier De    ${montant}
    Les Frais De Livraison Doivent Être    ${frais_attendus}
```
```robotframework
*** Settings ***
Library    Browser

*** Keywords ***
Ajouter Au Panier
    [Arguments]    ${produit}
    Go To    ${BASE_URL}/produits?q=${produit}
    Click    role=button[name="Ajouter au panier"]
    Get Text    role=status    *=    ajouté au panier

Le Total Du Panier Doit Être
    [Arguments]    ${attendu}
    Get Text    data-testid=total    ==    ${attendu}
```

## 13. Check-list d'audit

- [ ] Choix de Robot Framework justifié (lisibilité métier, hétérogénéité) ; versions RF, Browser, Python, Node épinglées.
- [ ] Trois couches respectées ; aucun localisateur dans les cas de test.
- [ ] Mots-clés documentés, catalogue Libdoc généré.
- [ ] Browser library pour le web neuf ; aucun `Sleep` ; sélecteurs par rôle ou `data-testid`.
- [ ] Secrets en variables d'environnement, masqués ; données fictives créées et nettoyées.
- [ ] Tags : smoke, régression, ID d'exigence ; sélection par tags en CI.
- [ ] Robocop et Robotidy en CI ; Pabot avec isolation des données.
- [ ] Relances tracées, tests instables suivis ; rapports archivés ; résultats importés dans l'outil de gestion des tests.

## 14. Anti-patterns et pièges

- Cas de test qui empilent des `Click    css=div:nth-child(3) > span` : illisibles et fragiles.
- `Sleep    5s` pour « stabiliser » ; logique `IF/FOR` lourde dans les cas de test.
- Mots-clés fourre-tout à 15 arguments ; noms techniques ; vérifications cachées.
- Dépendances entre tests (le test 2 utilise le panier du test 1) ; casse avec Pabot.
- Mots de passe en clair dans `*** Variables ***` ou dans `log.html`.
- SeleniumLibrary sur un projet neuf sans raison ; `Dialogs` (pause manuelle) dans une suite CI.
- Relancer jusqu'au vert sans signaler l'instabilité.
- Utiliser Robot Framework pour des tests unitaires.

## 15. Sources

Consultées le 2026-11-03.
- Robot Framework, User Guide : https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html
- Forum Robot Framework, 7.5 RC1 : https://forum.robotframework.org/t/robot-framework-7-5-release-candidate-1-has-been-released/9824
- Miroir v7.4.2 : https://sourceforge.net/projects/robot-framework.mirror/files/v7.4.2
- MarketSquare, robotframework-browser (releases) : https://github.com/MarketSquare/robotframework-browser/releases
- newreleases.io, Browser 19.14.1 : https://newreleases.io/project/github/MarketSquare/robotframework-browser/release/v19.14.1
