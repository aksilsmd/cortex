# Formation — Types de tests : niveaux, types, stratégie par les risques

Fiche de formation pour concepteur de tests, automaticien, exécutant, recetteur, testeurs web et mobile. Elle complète `tests-par-niveau.md` (outils et seuils du projet), `recette.md` et `checklist-tests.md`. Vocabulaire aligné sur l'ISTQB CTFL v4.0.1. Sources primaires en fin de fiche (consultées le 2026-11-03) ; collecte détaillée : `sources/types-de-tests.md`.

## Sommaire
1. Objectifs
2. Vocabulaire ISTQB indispensable
3. Formes de portefeuille : pyramide, trophée, quadrants
4. Stratégie par les risques
5. Critères d'entrée et de sortie
6. Catalogue des tests fonctionnels et structurels
7. Catalogue des tests non fonctionnels
8. Tests de sécurité : SAST, DAST, SCA et compagnie
9. Tests spécifiques au mobile
10. Techniques de conception des cas
11. Données de test
12. Check-list d'audit d'une stratégie de test
13. Anti-patterns et pièges
14. Sources

## 1. Objectifs

L'agent sait :
- nommer correctement un test (niveau, type, technique) et choisir où le placer pour un coût minimal ;
- construire une stratégie proportionnée aux risques produit, traçable aux exigences ;
- fixer des critères d'entrée et de sortie mesurables par niveau et pour la recette ;
- choisir, pour chaque caractéristique de qualité (ISO/IEC 25010:2023), le type de test, l'outil et le seuil ;
- distinguer ce qu'un agent peut prouver (sortie d'outil) de ce qui exige un humain (utilisabilité réelle, audit d'accessibilité complet, pentest autorisé).

## 2. Vocabulaire ISTQB indispensable

- **Erreur → défaut → défaillance** : l'humain se trompe, le code porte un défaut, l'exécution produit une défaillance observée. Un rapport d'anomalie décrit une défaillance (attendu, obtenu, étapes, environnement, gravité, priorité).
- **Niveaux de test** (5) : composant (unitaire), intégration de composants, système, intégration système (avec services externes), acceptation (utilisateur, opérationnelle, contractuelle/réglementaire, alpha/bêta).
- **Types de test** (4) : fonctionnel (quoi), non fonctionnel (comment bien : performance, sécurité, compatibilité…), boîte noire (fondé sur la spécification), boîte blanche (fondé sur la structure). Tout type peut s'exercer à tout niveau.
- **Test de confirmation** : rejouer le cas qui a révélé le défaut, après correction. **Test de régression** : vérifier qu'un changement n'a rien cassé ailleurs. Ne pas confondre : la confirmation ne remplace jamais la régression.
- **Test de maintenance** : déclenché par une évolution, un correctif, une migration ou mise à niveau d'environnement, un retrait (archivage, purge). Toujours analyse d'impact + régression ciblée.
- **Test statique** : revue et analyse sans exécution (spécifications, user stories, code, configuration). Le moins cher des tests ; compte dans la stratégie.
- **Les 7 principes** : le test montre la présence de défauts, pas leur absence ; l'exhaustivité est impossible ; tester tôt économise ; les défauts se regroupent ; les tests s'usent (paradoxe du pesticide) ; le test dépend du contexte ; l'absence de défauts ne garantit pas l'utilité.
- **Shift-left** : revue des spécifications côté test, cas écrits avant le code, CI/CD, analyse statique, non fonctionnel dès le composant — sans abandonner les tests tardifs. **Shift-right** : observabilité, canari, flags, tests en production maîtrisés.

## 3. Formes de portefeuille : pyramide, trophée, quadrants

### Pyramide (Cohn, reprise par Fowler/Vocke)
Beaucoup de tests petits, isolés, rapides en bas ; peu de tests larges, lents, coûteux en haut.
- Règle 1 : écrire des tests de granularités différentes.
- Règle 2 : plus on monte, moins on en a.
- Règle 3 : ne pas dupliquer une vérification entre couches ; si un E2E attrape un défaut qu'aucun test bas n'a vu, écrire le test bas manquant.
- Ordre de grandeur courant (indicatif, non normatif) : ≈ 70 % unitaires / 20 % intégration-API / 10 % E2E en nombre de tests.

### Trophée (K. C. Dodds, front-end JavaScript)
Statique (types, lint) → unitaire → **intégration (couche la plus large)** → E2E. Critère : confiance par minute investie ; plus un test ressemble à l'usage réel, plus il rassure. Adapté aux interfaces composant + réseau simulé (MSW).

### Quadrants agiles (repris par l'ISTQB)
| | Soutient l'équipe | Critique le produit |
|---|---|---|
| Orienté métier | Q2 : tests fonctionnels, exemples, user stories, API, prototypes UX | Q3 : exploratoire, utilisabilité, recette utilisateur (souvent manuel) |
| Orienté technologie | Q1 : composant, intégration de composants (automatisés, en CI) | Q4 : fumée, non fonctionnel (perf, sécurité…), souvent outillé |

Choix : back-end/API riches en règles → pyramide ; front riche en composants → trophée ; dans tous les cas, couvrir les 4 quadrants.

## 4. Stratégie par les risques

1. Lister les **risques produit** (caractéristiques de qualité, parcours critiques) et les **risques projet** (délais, compétences, environnements, fournisseurs).
2. Coter chaque risque produit : probabilité (1–3 ou 1–5 : complexité, nouveauté, historique de défauts, fréquence de changement) × impact (1–3 ou 1–5 : argent, données, sécurité, image, réglementaire, nombre d'utilisateurs touchés).
3. Niveau de risque = probabilité × impact. Exemple sur 1–3 : 7–9 élevé, 4–6 moyen, 1–3 faible.
4. Décliner par niveau de risque :

| Risque | Profondeur | Exemples d'exigences de test |
|---|---|---|
| Élevé | techniques multiples, revue indépendante, automatisation de non-régression, test en premier | paiement, authentification, calcul de prix/TVA, droits, données personnelles |
| Moyen | technique principale + exploratoire ciblé | recherche, filtres, notifications |
| Faible | fumée, exploratoire léger | pages statiques, préférences d'affichage |

5. Prioriser l'exécution par risque décroissant ; si le temps manque, c'est le bas du tableau qui saute, et cela se dit dans le rapport.
6. Réévaluer les risques à chaque incrément (nouveaux défauts = probabilité en hausse : les défauts se regroupent).
7. Traçabilité : exigence ↔ risque ↔ cas ↔ exécution ↔ anomalie. Une exigence sans cas est un trou visible.

Options de traitement d'un risque : tester, accepter, transférer, plan de contingence. Le test n'est qu'une option.

## 5. Critères d'entrée et de sortie

Critères d'entrée = prérequis pour démarrer (ressources, environnement, testware, qualité initiale). Critères de sortie = ce qui permet de déclarer terminé (couverture, défauts ouverts, taux d'échec). En agile : DoR (entrée d'une story) et DoD (sortie).

| Niveau | Entrée (exemples chiffrables) | Sortie (exemples chiffrables) |
|---|---|---|
| Composant | code compilé, lint et types sans erreur | 100 % des tests verts ; couverture de branches ≥ seuil projet (souvent 80 % sur le code métier) ; pas de test désactivé sans ticket |
| Intégration / API / contrat | composants livrés, contrats publiés, doublures disponibles | 100 % des contrats vérifiés ; codes d'erreur et cas limites couverts |
| Système / E2E | build déployé sur environnement stable, fumée verte, données chargées | 100 % des parcours critiques passés ; 0 anomalie bloquante/majeure ouverte sur ces parcours |
| Non fonctionnel | objectifs chiffrés écrits (SLO, budgets) | budgets tenus (ex. p95 API ≤ 500 ms à charge nominale, LCP ≤ 2,5 s, 0 violation axe critique) |
| Recette | DoD des lots atteinte, cahier de recette validé, utilisateurs disponibles | 100 % des cas prioritaires exécutés ; 0 bloquante, 0 majeure (ou dérogation signée) ; PV signé par le métier |

Règles : un critère non mesurable n'est pas un critère ; une dérogation est écrite, motivée, datée, avec un responsable ; « plus de temps » n'est pas un critère de sortie.

## 6. Catalogue des tests fonctionnels et structurels

| Test | But | Niveau | Outils typiques (2026) | Règles clés |
|---|---|---|---|---|
| Statique | défauts sans exécution | tous | ESLint, TypeScript strict, Ruff, mypy, SonarQube, revue | bloque la CI ; zéro avertissement nouveau |
| Unitaire | logique d'une unité isolée | composant | Vitest, Jest, pytest, JUnit 5, XCTest | < 100 ms par test ; déterministe ; un comportement par test ; pas de réseau ni d'horloge réelle |
| Mutation | qualité des assertions | composant | Stryker, PIT, mutmut | score de mutation sur le cœur métier ; révèle les tests sans assertion utile |
| Propriétés | invariants sur entrées générées | composant | fast-check, Hypothesis | pour parseurs, calculs, sérialisation |
| Intégration de composants | collaboration de modules, accès BDD réel | intégration | Testcontainers, Supertest, Testing Library + MSW | vraie base dans un conteneur jetable plutôt qu'un mock de l'ORM |
| Contrat | compatibilité fournisseur ↔ consommateur | intégration | Pact (consumer-driven), Schemathesis, validation OpenAPI | contrat publié et vérifié côté fournisseur en CI avant tout déploiement |
| API | fonctions, erreurs, sécurité d'une API | intégration/système | Postman/Newman, Bruno, REST Assured, Playwright request, pytest+httpx | statuts, schémas, en-têtes, idempotence, pagination, 4xx/5xx, authz par rôle |
| Bout en bout / parcours par persona | parcours métier complet, comme un utilisateur | système | Playwright, Cypress, Robot Framework, Maestro/Appium (mobile) | peu nombreux, sur les parcours critiques ; un scénario par persona et objectif (ex. « acheteur invité paie par carte ») ; données isolées par test |
| Fumée (smoke) | le build est-il testable ? | système | sous-ensemble E2E/API taggé | < 5 min ; échec = arrêt de la campagne |
| Santé (sanity) | la correction précise fonctionne-t-elle ? | système | ciblé | ne remplace pas la régression |
| Non-régression | rien de cassé ailleurs | tous | suites automatisées taggées par risque | sélection par analyse d'impact ; exécution à chaque fusion (rapide) et nightly (complète) |
| Exploratoire | apprendre et trouver l'inattendu | système | chartes, sessions de 60–90 min, notes | charte « Explorer [cible] avec [ressources] pour découvrir [info] » ; débriefing ; défauts reproductibles consignés |
| Acceptation (ATDD/BDD) | conformité aux critères d'acceptation | acceptation | Gherkin + Cucumber/Behave/Robot | exemples écrits avec le métier avant le code ; un scénario = une règle |
| Recette utilisateur (UAT) | adéquation au besoin réel | acceptation | cahier de recette, Xray/Squash | exécutée par des utilisateurs métier, pas par l'équipe de dev |
| Données / migration | intégrité, complétude, transformation | intégration/système | requêtes de rapprochement, Great Expectations, dbt tests | comptages source/cible, sommes de contrôle, clés orphelines, encodage, fuseaux horaires |
| Installation / mise à jour | déploiement et retour arrière | système | scripts, pipelines | tester la montée de version ET le rollback ; migrations rejouables |

Persona en E2E : chaque scénario porte un persona documenté (rôle, droits, appareil, langue, contraintes d'accessibilité) et un objectif ; les variantes (mobile lent, lecteur d'écran, arabe RTL) sont des personas de bord, pas des options.

## 7. Catalogue des tests non fonctionnels

Caractéristiques ISO/IEC 25010:2023 : adéquation fonctionnelle, efficacité de performance, compatibilité, capacité d'interaction (ex-utilisabilité), fiabilité, sécurité, maintenabilité, flexibilité (ex-portabilité), sûreté (safety).

| Test | But | Outils | Seuils / règles |
|---|---|---|---|
| Utilisabilité | les utilisateurs réussissent-ils ? | protocole de test, SUS, SEQ (voir `formation-ui-ux.md`) | ≈ 5 participants par itération qualitative ; réussite, temps, erreurs ; un agent ne remplace pas de vrais utilisateurs |
| Accessibilité | WCAG 2.2 AA | axe-core (@axe-core/playwright), Lighthouse, Pa11y, lecteurs d'écran NVDA/VoiceOver/TalkBack | automatique ≈ un tiers des critères seulement ; compléter par clavier seul, zoom 200 %/400 %, lecteur d'écran ; 0 violation critique/sérieuse |
| Compatibilité navigateurs/OS | rendu et fonctions identiques | Playwright (Chromium, Firefox, WebKit), BrowserStack/Sauce (payants) | matrice tirée de l'analytique ou des parts de marché de la cible ; couvrir ≥ 90–95 % du trafic |
| Visuel | régressions d'apparence | Playwright `toHaveScreenshot`, Storybook + Chromatic/Loki, BackstopJS | polices et animations figées, seuil de pixels explicite, captures par OS de CI |
| Responsive | mise en page par largeur | Playwright projets/viewports | 320, 375, 768, 1024, 1280, 1440 px au minimum ; pas de défilement horizontal à 320 px (WCAG 1.4.10) |
| Performance web | vitesse perçue | Lighthouse CI, WebPageTest, Web Vitals (RUM) | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 au 75e centile ; budgets JS par route |
| Charge — fumée | le script tient-il ? | k6, Gatling, JMeter, Locust | charge faible, secondes à minutes |
| Charge — nominale | comportement attendu | idem | charge de production moyenne, 5–60 min ; p95/p99, taux d'erreur < 1 % |
| Stress | au-delà du nominal | idem | 5–60 min au-dessus de la moyenne ; dégradation gracieuse attendue |
| Endurance (soak) | fuites, dérives | idem | charge moyenne pendant des heures ; mémoire, connexions, files |
| Pic (spike) | survie à un afflux soudain | idem | très haute charge, quelques minutes ; ex. campagne promotionnelle |
| Point de rupture | capacité maximale | idem | montée progressive jusqu'à rupture ; ne jamais viser la production |
| Résilience / chaos | tenue aux pannes | Toxiproxy, Chaos Mesh, LitmusChaos, AWS FIS | état stable mesurable + hypothèse + rayon d'impact minimal ; jamais sans accord écrit hors environnement du projet |
| Reprise (DR) | sauvegarde/restauration réelle | scripts de restauration | restauration testée, RPO/RTO mesurés, pas seulement « sauvegarde OK » |
| Localisation / i18n | langues, formats, RTL | pseudo-localisation, tests paramétrés par locale | textes +30–40 % plus longs, `dir="rtl"` pour l'arabe, formats date/nombre/devise (ex. DZD), pluriels ICU, aucune chaîne en dur |
| Maintenabilité | coût de modification | SonarQube, complexité, duplication | dette nouvelle nulle sur le code modifié |

## 8. Tests de sécurité : SAST, DAST, SCA et compagnie

| Acronyme | Ce que c'est | Quand | Outils libres |
|---|---|---|---|
| SAST | analyse statique du code source à la recherche de motifs vulnérables | chaque PR | Semgrep, CodeQL, Bandit, SonarQube |
| SCA | inventaire des dépendances et vulnérabilités connues (CVE), licences | chaque PR + quotidien | OSV-Scanner, Trivy, Dependabot/Renovate, npm audit, Syft (SBOM) |
| Secrets | clés et mots de passe dans le dépôt | pré-commit + CI | Gitleaks, TruffleHog |
| IaC / conteneurs | mauvaises configurations | CI | Trivy, Checkov, Hadolint |
| DAST | attaque d'une application en fonctionnement, boîte noire | environnement de test, nightly | ZAP (baseline puis full scan), Nuclei |
| IAST / RASP | instrumentation en exécution | optionnel | souvent commerciaux |
| Fuzzing | entrées aléatoires/mutées | parseurs, API | Schemathesis, RESTler, AFL++, libFuzzer |
| Test d'intrusion | expert humain, scénarios d'attaque | avant mise en production, annuel | voir `securite-protection/references/test-intrusion.md` ; autorisation écrite obligatoire |

Référentiels : OWASP ASVS 5.0.0 (mai 2025) pour les exigences vérifiables, WSTG 4.2 (5.0 en développement) pour la méthode de test web, MASVS + MASTG pour le mobile, OWASP Top 10 pour la sensibilisation (pas une méthode de test). Tests fonctionnels de sécurité à automatiser : contrôle d'accès par rôle (IDOR : l'utilisateur A lit-il l'objet de B ?), expiration de session, limitation de débit, en-têtes (CSP, HSTS), validation côté serveur.

## 9. Tests spécifiques au mobile

- **Appareils** : matrice réelle (parts de marché du pays cible : en Algérie, Android très majoritaire et nombreux appareils d'entrée de gamme), émulateurs pour le volume, appareils réels pour performance, capteurs, notifications, paiement.
- **Interruptions** : appel entrant, passage en arrière-plan, rotation, verrouillage, faible batterie, mode avion, permission refusée puis accordée.
- **Réseau** : 3G lente, perte et retour de connexion, hors-ligne, latence élevée ; synchronisation et conflits.
- **Cycle de vie** : installation propre, mise à jour depuis la version N-1 (migration des données locales), désinstallation.
- **Stores** : règles de revue Apple/Google, tailles d'écran, mode sombre, taille de police système maximale, TalkBack/VoiceOver.
- **Outils** : Espresso/UI Automator (Android), XCUITest (iOS), Maestro, Appium, Detox (React Native), integration_test (Flutter) ; sécurité : MASTG.

## 10. Techniques de conception des cas

- **Partitions d'équivalence** : un représentant par classe valide et invalide. Ex. âge 18–65 → {<18, 18–65, >65, non numérique, vide}.
- **Valeurs limites** : à 2 valeurs (limite + voisin de la partition adjacente : 17/18, 65/66) ou à 3 valeurs (limite et ses deux voisins : 17/18/19, 64/65/66). Le 3 valeurs détecte davantage d'erreurs d'opérateur.
- **Tables de décision** : conditions × actions, une colonne par règle ; réduire les colonnes impossibles. Pour remises, droits, tarification.
- **Transitions d'états** : couvrir tous les états, toutes les transitions valides, puis tester les transitions invalides (ex. rembourser une commande non payée).
- **Paires (pairwise)** : combinaisons de paramètres (navigateur × langue × rôle) réduites par outil (PICT, allpairs).
- **Boîte blanche** : couverture d'instructions < couverture de branches ; 100 % de branches implique 100 % d'instructions, pas l'inverse. La couverture mesure ce qui est exécuté, pas ce qui est vérifié.
- **Expérience** : estimation d'erreurs (attaques de fautes : vide, très long, Unicode, injection, double clic), check-lists, exploratoire.
- **Collaboratives** : user stories écrites ensemble, critères d'acceptation, ATDD (exemples avant le code), Example Mapping.

Exemple Gherkin (une règle, un exemple concret) :
```gherkin
Règle: la livraison est offerte dès 5 000 DZD
  Scénario: panier juste au seuil
    Étant donné un panier de 5 000 DZD
    Quand j'affiche le récapitulatif
    Alors les frais de livraison valent 0 DZD
```

## 11. Données de test

- Fictives ou anonymisées, jamais de données de production personnelles réelles (RGPD ; voir garde-fous du pôle).
- Chaque test crée et nettoie ses données (fabriques, seeds par test) ; aucune dépendance d'ordre entre tests.
- Jeux de bord : noms avec apostrophes et accents, arabe et tifinagh, emoji, chaînes de 255+ caractères, montants 0 et maximum, dates 29 février et changements d'heure, fuseaux (Africa/Algiers UTC+1 sans heure d'été).
- Données de performance représentatives en volume et distribution (pas 10 lignes).

## 12. Check-list d'audit d'une stratégie de test

- [ ] Risques produit listés, cotés probabilité × impact, et réévalués à chaque incrément.
- [ ] Chaque exigence et chaque risque élevé tracés vers au moins un cas.
- [ ] Les 4 quadrants couverts ; forme du portefeuille justifiée (pyramide ou trophée).
- [ ] Critères d'entrée et de sortie chiffrés par niveau et pour la recette.
- [ ] Analyse statique, SAST, SCA et secrets bloquants en CI.
- [ ] Contrats d'API vérifiés côté fournisseur avant déploiement.
- [ ] Parcours critiques en E2E par persona, y compris un persona de bord (mobile lent, lecteur d'écran, RTL).
- [ ] Fumée < 5 min, non-régression rapide à chaque fusion, complète nightly.
- [ ] Objectifs non fonctionnels écrits (Web Vitals, p95, taux d'erreur, WCAG 2.2 AA) et mesurés.
- [ ] Accessibilité : automatique + manuel (clavier, zoom, lecteur d'écran).
- [ ] Matrice navigateurs/appareils issue de données de la cible.
- [ ] Charge : au minimum fumée + nominale avant lancement ; pic si campagne prévue.
- [ ] Restauration de sauvegarde testée réellement.
- [ ] Exploratoire en sessions chartées, débriefées.
- [ ] Tests instables (flaky) suivis, mis en quarantaine avec ticket et délai, jamais ignorés en silence.
- [ ] Données de test fictives, isolées, nettoyées.
- [ ] Rapport de campagne : exécutés/passés/échoués/bloqués, anomalies par gravité, risques résiduels, recommandation go/no-go.

## 13. Anti-patterns et pièges

- **Cornet de glace** : beaucoup d'E2E/manuel, peu d'unitaires → lenteur, instabilité, coût. **Sablier** : unitaires + E2E sans intégration → défauts d'interface tardifs.
- Viser 100 % de couverture de code : on écrit des tests sans assertion utile ; préférer couverture de branches sur le métier + score de mutation.
- Mocker ce qu'on ne possède pas (SDK tiers) dans des tests censés prouver l'intégration ; préférer contrat ou bac à sable du fournisseur.
- `sleep()` fixes dans les tests UI ; sélecteurs CSS fragiles au lieu de rôles accessibles ou `data-testid`.
- Tests dépendants de l'ordre, de l'horloge, du fuseau ou de données partagées.
- Relancer un test rouge jusqu'au vert (« retry » qui masque un vrai défaut de concurrence).
- Confondre confirmation et régression ; corriger sans ajouter le test qui aurait détecté le défaut.
- Tests de charge contre la production ou un environnement tiers ; résultats sans conditions (données, matériel, réseau) indiquées.
- « Lighthouse = accessible » : l'outil automatique ne couvre qu'une partie des critères.
- DAST lancé sans authentification : il ne voit que la page de connexion.
- Recette faite par l'équipe de développement ; PV signé avec des bloquantes ouvertes sans dérogation écrite.
- Annoncer « tests OK » sans la sortie qui le prouve (règle du pôle).

## 14. Sources

Consultées le 2026-11-03.
- ISTQB, CTFL v4.0 (syllabus v4.0.1) : https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/
- ISTQB, CTFL Syllabus v4.0 (PDF) : https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Foundation%20Level/ISTQB_CTFL_Syllabus-v4.0%20.pdf
- ASTQB, 2.2 Test Levels and Test Types : https://astqb.org/2-2-test-levels-and-test-types/
- H. Vocke / martinfowler.com, The Practical Test Pyramid (2018) : https://martinfowler.com/articles/practical-test-pyramid.html
- K. C. Dodds, The Testing Trophy and Testing Classifications : https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications
- Grafana k6, Load test types : https://grafana.com/docs/k6/latest/testing-guides/test-types/
- Principles of Chaos Engineering : https://principlesofchaos.org/
- OWASP WSTG : https://owasp.org/www-project-web-security-testing-guide/
- OWASP ASVS 5.0.0 : https://asvs.owasp.org/
- OWASP MASVS : https://mas.owasp.org/MASVS/
- arc42 Quality, ISO 25010 update 2023 : https://quality.arc42.org/articles/iso-25010-update-2023
- W3C, WCAG 2.2 : https://www.w3.org/TR/WCAG22/
- web.dev, Web Vitals : https://web.dev/articles/vitals
