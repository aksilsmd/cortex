# Formation — Postman et alternatives libres pour tester les API

Fiche de formation pour concepteur de tests, automaticien, exécutant, recetteur, testeurs web et mobile. Elle complète `formation-types-de-tests.md` (tests d'API et de contrat) et `tests-par-niveau.md`. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/postman.md`. Aucun compte n'est créé par un agent : Postman cloud suppose un compte de l'utilisateur ; les alternatives fichiers (Bruno, Newman, tests en code) fonctionnent hors ligne.

## Sommaire
1. Objectifs
2. Ce qu'il faut tester sur une API
3. Postman : concepts
4. Scripts et assertions
5. Variables, environnements, secrets
6. Données, enchaînements, flux
7. Exécution en ligne de commande et CI
8. Mocks, monitors, documentation, contrats
9. Offres Postman 2026 et confidentialité
10. Alternatives libres
11. Quel outil choisir
12. Exemple complet
13. Check-list d'audit
14. Anti-patterns et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- couvrir une API sur les axes fonctionnel, erreurs, sécurité, contrat et performance de base ;
- organiser collections, environnements et variables sans secret versionné ;
- écrire des assertions robustes (statut, schéma, en-têtes, temps) ;
- exécuter les collections en CI (Postman CLI, Newman, Bruno CLI) avec rapports ;
- choisir entre Postman et une alternative libre selon la confidentialité, l'équipe et le coût.

## 2. Ce qu'il faut tester sur une API

| Axe | Vérifications |
|---|---|
| Fonctionnel | réponse attendue pour chaque cas nominal ; CRUD complet ; règles métier (calculs, statuts) |
| Validation | champs obligatoires, types, longueurs, formats (email, téléphone +213), valeurs limites, champs inconnus |
| Erreurs | codes adaptés (400, 401, 403, 404, 409, 422, 429, 500) ; corps d'erreur normalisé (ex. RFC 9457 Problem Details) ; pas de trace interne exposée |
| Sécurité | authentification requise, **autorisation par rôle et par objet** (IDOR : A ne lit pas l'objet de B), jetons expirés/révoqués, limitation de débit, CORS, en-têtes de sécurité, injection |
| Contrat | conformité au schéma OpenAPI (requête et réponse), compatibilité ascendante |
| Protocole | méthodes et idempotence (PUT/DELETE répétés), pagination, tri, filtres, `ETag`/`If-None-Match`, compression, versionnement |
| Performance de base | temps de réponse sous seuil (ex. p95 ≤ 500 ms en recette, à fixer), taille de réponse |
| Données | encodage UTF-8 (arabe, tifinagh, emoji), fuseau horaire et format ISO 8601, montants en entiers/décimaux sans flottant |

## 3. Postman : concepts

- **Workspace** (personnel, équipe, partenaire, public) → **collections** (dossiers, requêtes) → **exemples** de réponses.
- **Environnements** (local, recette, préproduction) et **variables** à portées : globale, collection, environnement, données (itération), locale.
- **Scripts** pré-requête et post-réponse au niveau collection, dossier, requête (JavaScript, sandbox `pm.*`).
- **Collection Runner** (exécution manuelle, itérations, fichier de données CSV/JSON), **Postman CLI** (officiel) et **Newman** (CLI libre historique) pour la CI.
- **Flows**, **mock servers**, **monitors**, **API Builder / spécifications** (OpenAPI), **Postman Vault** pour les secrets locaux, assistant IA (selon l'offre).
- Import : OpenAPI, cURL, HAR ; export de collections au format JSON v2.1.

## 4. Scripts et assertions

```js
// Post-response
pm.test('statut 201', () => pm.response.to.have.status(201));
pm.test('temps < 500 ms', () => pm.expect(pm.response.responseTime).to.be.below(500));
pm.test('en-tête JSON', () => pm.response.to.have.header('Content-Type', /application\/json/));
const body = pm.response.json();
pm.test('schéma commande', () => pm.response.to.have.jsonSchema(pm.collectionVariables.get('schemaCommande')));
pm.test('total en DZD', () => pm.expect(body.total).to.eql({ montant: 12500, devise: 'DZD' }));
pm.collectionVariables.set('commandeId', body.id);   // chaînage
```
- Un test = une assertion lisible ; noms explicites (ils apparaissent dans le rapport).
- Valider le **schéma** (JSON Schema, Ajv intégré) plutôt que chaque champ un par un.
- Scripts communs au niveau collection (authentification, en-têtes) ; pas de copier-coller entre requêtes ; bibliothèques de scripts partagées (packages, selon l'offre).
- Pas de logique d'attente active (`setTimeout` en boucle) ; pour un traitement asynchrone, interroger avec un nombre d'essais borné.

## 5. Variables, environnements, secrets

- Variables d'environnement pour `baseUrl`, identifiants de test, jetons obtenus dynamiquement.
- Secrets : type de variable « secret » masqué, **valeur courante** (locale, non synchronisée) plutôt que valeur initiale (partagée) ; mieux : Postman Vault ou variables d'environnement de la CI (`--env-var`).
- Jamais de secret dans une collection exportée, une capture, un ticket ou un dépôt ; vérifier avant export.
- Jeton OAuth2 obtenu par le flux configuré dans l'onglet Authorization (client credentials pour machine à machine ; Authorization Code + PKCE pour un utilisateur), rafraîchi automatiquement.
- Un environnement par cible ; jamais d'environnement « production » avec écriture dans une collection de tests.

## 6. Données, enchaînements, flux

- Tests pilotés par données : fichier CSV/JSON d'itérations pour partitions et valeurs limites.
- Chaînage : créer → lire → modifier → supprimer, avec identifiants passés par variables ; chaque exécution crée ses propres données (préfixe unique) et nettoie.
- Ordre d'exécution : séquentiel dans une collection ; `pm.execution.setNextRequest()` pour un enchaînement conditionnel (avec parcimonie).
- Tests négatifs systématiques : chaque requête nominale a ses variantes 400/401/403/404.

## 7. Exécution en ligne de commande et CI

- **Postman CLI** (officiel) : `postman login --with-api-key $POSTMAN_API_KEY` puis `postman collection run <id ou fichier> -e <env> --reporters cli,junit` ; peut publier les résultats dans Postman.
- **Newman** (libre, npm) : `newman run collection.json -e recette.json --env-var "mdp=$MDP" -r cli,junit,htmlextra --reporter-junit-export reports/api.xml` ; fonctionne avec des fichiers exportés, sans compte (vérifier sa maintenance et la compatibilité avec les fonctions récentes de Postman).
- Bloquer la CI sur échec ; publier JUnit ; conserver les rapports HTML comme preuves.
- Exécuter contre un environnement éphémère ou de recette, jamais contre la production en écriture.

## 8. Mocks, monitors, documentation, contrats

- **Mock servers** : simuler une API pendant que le front avance ; illimités sur toutes les offres 2026. Les mocks n'attestent pas le comportement réel.
- **Monitors** : exécutions planifiées dans le cloud Postman (quota mensuel) ; ils envoient des requêtes depuis l'infrastructure Postman : ne pas viser une API interne non exposée ni mettre de vraies données.
- **Documentation** générée depuis la collection ; préférer la spécification OpenAPI comme source de vérité, la collection en étant dérivée.
- **Contrat** : valider réponses contre le schéma OpenAPI (Postman API Builder, ou outils dédiés : Schemathesis, Dredd, Pact pour le consumer-driven — voir fiche types de tests).
- Tests de charge : la fonction de performance de Postman est limitée (heures d'utilisateurs virtuels selon l'offre) ; utiliser k6 ou Gatling pour une vraie campagne.

## 9. Offres Postman 2026 et confidentialité

- Depuis mars 2026 : **Free** (1 utilisateur, pas d'équipe), **Solo**, **Team** (remplace Basic), **Enterprise** ; exécutions de collections et mocks illimités ; monitors et IA sous quotas. Prix : page tarifs, à vérifier ; anciennes offres conservées jusqu'au renouvellement.
- Conséquence : une équipe de plusieurs testeurs ne peut plus partager un espace sur l'offre gratuite ; partage par fichiers exportés (Git) ou offre payante.
- Données : les collections, environnements (valeurs initiales) et historiques sont synchronisés dans le cloud Postman (hébergement hors d'Algérie et hors UE par défaut, à vérifier selon l'offre : une option de région UE existe pour certaines offres Enterprise). Pour un client sensible : pas de données réelles, valeurs secrètes locales, ou outil hors ligne.
- Le Scratch Pad hors ligne a été retiré il y a plusieurs années ; un compte est requis pour l'application de bureau (vérifier l'état actuel du mode « lightweight client »).

## 10. Alternatives libres

| Outil | Licence / modèle | Atouts | Limites |
|---|---|---|---|
| **Bruno** | MIT, bureau, hors ligne | collections en fichiers texte (`.bru`) dans le dépôt Git, revues de code, CLI `bru run` pour la CI, scripts JS et assertions, import Postman/OpenAPI | certaines fonctions en édition payante ; écosystème plus jeune |
| **Hoppscotch** | MIT, web/PWA, auto-hébergeable | léger, REST/GraphQL/WebSocket/SSE, instance interne possible | moins d'automatisation de tests avancée |
| **Insomnia** (Kong) | cœur libre (Apache 2.0) | REST, GraphQL, gRPC ; stockage local ou Git | évolutions de modèle de compte à surveiller |
| **Tests en code** | libre | pytest + httpx, REST Assured (Java), Supertest/Vitest, Playwright `request` : versionnés, revus, dans la même CI que le reste | demande des compétences de développement |
| **HTTP en fichiers** | libre | fichiers `.http` (VS Code REST Client, JetBrains HTTP Client) pour l'exploration | peu d'assertions |
| **Schemathesis** | MIT | tests de propriété générés depuis OpenAPI (fuzzing de contrat) | complète, ne remplace pas les tests métier |

## 11. Quel outil choisir

1. API d'un projet Dan-Cortex, équipe technique, besoin de revue et de CI → **tests en code** (même langage que le back) + Schemathesis.
2. Testeurs fonctionnels qui veulent une interface graphique, données sensibles, pas de cloud → **Bruno** (collections dans le dépôt).
3. Client déjà équipé Postman Team/Enterprise, collaboration et monitors utiles → **Postman** + Postman CLI en CI, secrets en Vault/CI.
4. Instance web interne partagée → **Hoppscotch** auto-hébergé.
Toujours : spécification OpenAPI = source de vérité ; collections dérivées et versionnées.

## 12. Exemple complet

Scénario « acheteur ne peut pas lire la commande d'un autre » :
1. `POST /auth/token` (acheteur A) → enregistre `tokenA` ; idem `tokenB`.
2. `POST /commandes` avec `tokenA` → 201, enregistre `commandeA`.
3. `GET /commandes/{{commandeA}}` avec `tokenB` → **403 ou 404** attendu, corps Problem Details, aucune donnée de A.
4. `GET /commandes/{{commandeA}}` sans jeton → 401.
5. `DELETE /commandes/{{commandeA}}` avec `tokenA` (nettoyage) → 204 ; répété → 404 (idempotence documentée).

## 13. Check-list d'audit

- [ ] Spécification OpenAPI à jour ; chaque opération a des tests nominaux, négatifs et d'autorisation.
- [ ] Assertions de statut, schéma, en-têtes et temps ; noms de tests explicites.
- [ ] Contrôle d'accès par rôle et par objet testé (IDOR) ; limitation de débit vérifiée.
- [ ] Aucune donnée personnelle réelle ; données créées et nettoyées par l'exécution.
- [ ] Secrets hors collections exportées et hors dépôt ; variables secrètes masquées ; CI par `--env-var`.
- [ ] Collections (ou fichiers Bruno, ou tests en code) versionnées et revues.
- [ ] Exécution en CI bloquante avec rapport JUnit ; preuves HTML archivées.
- [ ] Offre et hébergement des données Postman vérifiés si cloud utilisé ; pas de monitor vers une API interne.

## 14. Anti-patterns et pièges

- Tester uniquement le chemin heureux avec un compte administrateur.
- Jetons et mots de passe dans la valeur initiale d'une variable partagée ou dans une collection publique.
- Workspace public par erreur (des fuites de clés via des workspaces publics ont été largement documentées).
- Collections divergentes de la spécification ; copier-coller de scripts dans chaque requête.
- Assertions sur des valeurs volatiles (dates, identifiants) au lieu du schéma et des invariants.
- Tests dépendants de l'ordre et de données préexistantes partagées.
- Monitors ou tests de charge contre la production ou une API tierce.
- Croire que l'offre gratuite permet toujours de collaborer à trois (fin en mars 2026).

## 15. Sources

Consultées le 2026-11-03.
- Postman Docs, About plans : https://learning.postman.com/latest-v-12/docs/billing/about-plans.md
- Postman Docs, About resource usage : https://learning.postman.com/docs/billing/resource-usage
- Postman, Pricing : https://www.postman.com/pricing/
- Bruno, Bruno vs Hoppscotch : https://www.usebruno.com/compare/bruno-vs-hoppscotch
- OpenAlternative, Bruno : https://openalternative.co/alternatives/bruno
- IETF, RFC 9457 Problem Details for HTTP APIs : https://www.rfc-editor.org/rfc/rfc9457
- OWASP, API Security Top 10 : https://owasp.org/API-Security/
