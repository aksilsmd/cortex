# Formation — Cypress + TypeScript + Cucumber (BDD)

Fiche de formation pour concepteur de tests, automaticien, exécutant, recetteur, testeurs web et mobile. Elle complète `formation-types-de-tests.md`, `formation-playwright-mcp.md` et `tests-par-niveau.md`. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/cypress-typescript-cucumber.md`. Versions de référence : Cypress 15.x (15.21.1 en août 2026), `@badeball/cypress-cucumber-preprocessor` 24.x : vérifier à l'installation.

## Sommaire
1. Objectifs
2. Cypress ou Playwright ?
3. Architecture d'un projet
4. Configuration TypeScript + Cucumber
5. Gherkin de qualité
6. Définitions d'étapes en TypeScript
7. Règles d'or Cypress
8. Réseau, sessions, données
9. Tests de composants, accessibilité, visuel
10. Exécution, rapports, CI
11. Exemple complet
12. Check-list d'audit
13. Anti-patterns et pièges
14. Sources

## 1. Objectifs

L'agent sait :
- choisir Cypress à bon escient et le combiner avec Cucumber quand le métier lit les scénarios ;
- configurer un projet TypeScript strict avec le préprocesseur Cucumber ;
- écrire des scénarios Gherkin déclaratifs (une règle, un exemple) et des étapes réutilisables typées ;
- appliquer les règles Cypress (chaînes de commandes, auto-attente, sélecteurs, `cy.session`, `cy.intercept`) ;
- exécuter en CI avec rapports Cucumber et traçabilité vers les exigences.

## 2. Cypress ou Playwright ?

| Critère | Cypress | Playwright |
|---|---|---|
| Modèle | s'exécute dans le navigateur, à côté de l'app ; runner interactif très lisible | pilote le navigateur depuis Node (CDP / protocoles) |
| Navigateurs | Chrome, Edge, Electron, Firefox ; WebKit expérimental | Chromium, Firefox, WebKit (Safari) stables |
| Onglets, multi-origines | limité (`cy.origin` pour plusieurs domaines ; pas de multi-onglets) | natif |
| Parallélisme | via Cypress Cloud (payant) ou découpage maison | natif et gratuit |
| Tests de composants | oui (React, Vue, Angular, Svelte) | expérimental |
| Débogage | voyage dans le temps du runner, très pédagogique | Trace Viewer, UI mode |
Règle : projet neuf exigeant Safari/WebKit, multi-onglets ou parallélisme gratuit → Playwright ; équipe déjà outillée en Cypress, ou forte valeur du runner interactif et des tests de composants → Cypress.

Cucumber n'est utile que si des non-développeurs lisent ou écrivent les scénarios (PO, recetteurs, métier). Sinon, il ajoute une couche de maintenance sans valeur : écrire directement en TypeScript.

## 3. Architecture d'un projet

```
cypress/
  e2e/
    panier/
      panier.feature            # scénarios métier
      panier.steps.ts           # étapes spécifiques (facultatif)
  support/
    step_definitions/           # étapes communes réutilisables
      navigation.steps.ts
      authentification.steps.ts
    pages/                      # objets d'écran légers ou « app actions »
      panier.page.ts
    commands.ts                 # commandes personnalisées typées
    e2e.ts
  fixtures/                     # données JSON fictives
cypress.config.ts
tsconfig.json
```
- Les `.feature` décrivent le quoi ; les étapes traduisent en actions ; les pages/commandes portent les sélecteurs.
- Une étape commune n'est écrite qu'une fois (recherche avant création ; les doublons ambigus font échouer).

## 4. Configuration TypeScript + Cucumber

Dépendances (dev) : `cypress`, `typescript`, `@badeball/cypress-cucumber-preprocessor`, `@bahmutov/cypress-esbuild-preprocessor`, `esbuild`.

```ts
// cypress.config.ts
import { defineConfig } from 'cypress';
import createBundler from '@bahmutov/cypress-esbuild-preprocessor';
import { addCucumberPreprocessorPlugin } from '@badeball/cypress-cucumber-preprocessor';
import { createEsbuildPlugin } from '@badeball/cypress-cucumber-preprocessor/esbuild';

export default defineConfig({
  e2e: {
    baseUrl: 'http://localhost:3000',
    specPattern: 'cypress/e2e/**/*.feature',
    async setupNodeEvents(on, config) {
      await addCucumberPreprocessorPlugin(on, config);
      on('file:preprocessor', createBundler({ plugins: [createEsbuildPlugin(config)] }));
      return config;
    },
    retries: { runMode: 2, openMode: 0 },
    video: false,
  },
});
```
```json
// package.json (extrait) : configuration du préprocesseur
"cypress-cucumber-preprocessor": {
  "stepDefinitions": ["cypress/support/step_definitions/**/*.ts", "cypress/e2e/[filepath].steps.ts"],
  "json": { "enabled": true, "output": "reports/cucumber.json" },
  "html": { "enabled": true, "output": "reports/cucumber.html" },
  "filterSpecs": true, "omitFiltered": true
}
```
`tsconfig.json` : `"strict": true`, `"types": ["cypress", "node"]`, `"moduleResolution": "bundler"` (ou `node16`) pour les exports du préprocesseur.

Vigilance : le préprocesseur a un seul mainteneur principal ; épingler la version, suivre les versions majeures (changements de configuration fréquents) et prévoir un plan de sortie.

## 5. Gherkin de qualité

- `# language: fr` en tête pour les mots-clés français : `Fonctionnalité`, `Règle`, `Contexte`, `Scénario`, `Plan du scénario` / `Exemples`, `Soit`/`Étant donné`, `Quand`, `Alors`, `Et`, `Mais`.
- **Déclaratif, pas impératif** : « Quand je paie ma commande par carte » et non « Quand je clique sur le bouton #pay ».
- Un scénario = une règle métier illustrée par un exemple concret ; 3 à 7 étapes ; un seul `Quand`.
- `Règle:` pour regrouper les exemples d'une même règle (Example Mapping) ; `Contexte:` court (≤ 3 étapes) pour le commun.
- `Plan du scénario` + `Exemples` pour les partitions et valeurs limites (4 999 / 5 000 / 5 001).
- Tags : `@smoke`, `@regression`, `@EX-012`, `@persona-invite`, `@wip` ; exécution filtrée par expressions de tags.
- Vocabulaire du glossaire métier, identique aux spécifications ; pas de données techniques (sélecteurs, URL) dans les scénarios.
- Écrits avec le PO/métier avant le code (ATDD) ; relus comme des spécifications vivantes.

## 6. Définitions d'étapes en TypeScript

```ts
// cypress/support/step_definitions/panier.steps.ts
import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Given('un panier de {int} DZD', (montant: number) => {
  cy.task('db:panier', { montant });            // préparation par API/tâche, pas par l'IHM
});

When('j\'affiche le récapitulatif', () => {
  cy.visit('/panier');
});

Then('les frais de livraison valent {string}', (frais: string) => {
  cy.findByTestId('frais-livraison').should('have.text', frais);
});
```
- **Expressions Cucumber** (`{int}`, `{string}`, `{float}`, `{word}`, types personnalisés) plutôt que des regex.
- Étapes génériques mais pas fourre-tout ; pas de logique conditionnelle selon le texte.
- Partage d'état entre étapes : alias Cypress (`cy.wrap(x).as('commande')`, `this.commande` avec `function () {}`) ou contexte du monde ; pas de variables globales.
- `Before`/`After` (hooks Cucumber) pour préparer/nettoyer ; `BeforeAll` pour l'initialisation lourde.
- Commandes personnalisées typées (`declare global { namespace Cypress { interface Chainable { connexion(role: Role): Chainable<void> } } }`).

## 7. Règles d'or Cypress

- Les commandes Cypress sont **asynchrones et mises en file** : pas de `const x = cy.get(...)`, pas d'`async/await` sur les chaînes ; utiliser `.then()`, alias, `.should()`.
- **Auto-attente et relance** : `cy.get(sel).should('be.visible')` réessaie jusqu'au délai ; jamais `cy.wait(3000)` ; attendre une requête par alias (`cy.wait('@commande')`).
- **Sélecteurs** : `data-cy`/`data-testid` ou Testing Library (`@testing-library/cypress` : `findByRole`, `findByLabelText`) ; jamais de classes CSS de mise en forme ni de texte qui sera traduit.
- **Tests indépendants** : état préparé par API (`cy.request`, `cy.task`) ; nettoyage **avant** le test plutôt qu'après (un test interrompu ne laisse pas l'état suivant sale).
- **`cy.session()`** pour mettre en cache la connexion par rôle (avec `validate`) ; connexion par API, l'IHM de connexion n'est testée qu'une fois.
- Ne pas visiter de sites tiers ; `cy.origin()` seulement pour un SSO du projet.
- Pas de conditions sur l'état du DOM (« si le bouton existe, cliquer ») : rendre l'état déterministe.
- `testIsolation: true` (défaut) : page et stockage réinitialisés entre tests.

## 8. Réseau, sessions, données

- `cy.intercept('POST', '/api/paiement', { statusCode: 500 }).as('paiement')` : simuler un tiers en panne ; `cy.intercept` en espion pour attendre une vraie requête.
- Ne pas simuler l'API du produit dans un test censé être de bout en bout ; réserver les bouchons aux tiers (paiement, transporteur, cartes).
- Fixtures JSON fictives ; secrets par `Cypress.env()` alimenté par la CI (`CYPRESS_MDP_TEST`), jamais dans `cypress.config.ts` ni dans les fixtures versionnées.
- Horloge : `cy.clock()` / `cy.tick()` pour promotions temporisées et expiration de session.
- Locale et fuseau : forcer `Africa/Algiers` côté navigateur (variable `TZ` du processus) et tester `ar` (RTL).

## 9. Tests de composants, accessibilité, visuel

- Component testing : `cy.mount(<Bouton variant="primary" />)` ; couvrir chaque état du système de design.
- Accessibilité : `cypress-axe` (`cy.injectAxe(); cy.checkA11y(null, { includedImpacts: ['critical', 'serious'] })`) ; compléter par des tests manuels (clavier, lecteur d'écran).
- Visuel : plugins (Percy, Applitools : payants ; `cypress-image-diff` libre) ; figer animations et polices.
- Viewports : `cy.viewport('iphone-x')`, tailles de la matrice.

## 10. Exécution, rapports, CI

- `npx cypress open` (local), `npx cypress run --browser chrome --env tags="@smoke and not @wip"`.
- Rapports : JSON/HTML Cucumber du préprocesseur ; JUnit (`mocha-junit-reporter`) pour la CI ; messages Cucumber importables dans Xray (format Cucumber JSON) pour la traçabilité.
- Parallélisme : Cypress Cloud (payant) ou découpage des specs par job (`--spec`) ; données isolées par job.
- Image Docker officielle `cypress/included` épinglée ; cache des binaires Cypress.
- Captures sur échec par défaut ; vidéo désactivée sauf besoin (taille).
- `retries.runMode: 2` : tout test passé au second essai est signalé instable et traité.

## 11. Exemple complet

```gherkin
# language: fr
@panier @regression
Fonctionnalité: Frais de livraison
  Règle: la livraison est offerte dès 5 000 DZD

    @EX-021
    Plan du scénario: frais selon le montant du panier
      Étant donné un panier de <montant> DZD
      Quand j'affiche le récapitulatif
      Alors les frais de livraison valent "<frais>"

      Exemples:
        | montant | frais   |
        | 4999    | 500 DZD |
        | 5000    | 0 DZD   |
        | 5001    | 0 DZD   |
```

## 12. Check-list d'audit

- [ ] Choix Cypress et Cucumber justifiés (lecteurs non développeurs réels) ; versions épinglées.
- [ ] TypeScript strict ; commandes personnalisées typées.
- [ ] Scénarios déclaratifs, une règle par scénario, vocabulaire du glossaire, tags d'exigence.
- [ ] Aucune étape dupliquée ou ambiguë ; étapes communes centralisées.
- [ ] Aucun `cy.wait(nombre)` ; sélecteurs `data-*` ou par rôle ; pas de conditions sur le DOM.
- [ ] Connexion par `cy.session` + API ; état préparé par API ; tests indépendants.
- [ ] Bouchons limités aux tiers ; secrets hors dépôt.
- [ ] Accessibilité axe intégrée ; viewports de la matrice.
- [ ] Rapports Cucumber et JUnit en CI ; résultats importés dans l'outil de gestion des tests ; instabilité suivie.

## 13. Anti-patterns et pièges

- Gherkin impératif (« je clique », « je saisis dans le champ #email ») : scénarios fragiles et illisibles pour le métier.
- Cucumber sans lecteur métier : coût double sans bénéfice.
- Scénarios-fleuves à plusieurs `Quand` ; `Contexte` de 10 étapes.
- Étapes qui contiennent de la logique conditionnelle ou appellent d'autres étapes.
- Variables globales entre étapes ; tests dépendants de l'ordre.
- Préparer les données par l'IHM à chaque test (lent, fragile).
- `async/await` mélangé aux commandes Cypress ; affectation du résultat de `cy.get`.
- Tester des sites tiers ou le SSO d'un fournisseur réel.
- Relancer en boucle un test instable sans enquête.

## 14. Sources

Consultées le 2026-11-03.
- Cypress, Changelog : https://docs.cypress.io/guides/references/changelog
- Cypress, release 15.21.1 : https://www-production.cypress.io/releases/15-21-1
- Cypress, Best Practices : https://docs.cypress.io/app/core-concepts/best-practices
- badeball, cypress-cucumber-preprocessor (quick start) : https://github-redirect.dependabot.com/badeball/cypress-cucumber-preprocessor/blob/master/docs/quick-start.md
- depscope, fiche du préprocesseur : https://depscope.dev/pkg/npm/@badeball/cypress-cucumber-preprocessor
- Cucumber, Gherkin reference : https://cucumber.io/docs/gherkin/reference/
