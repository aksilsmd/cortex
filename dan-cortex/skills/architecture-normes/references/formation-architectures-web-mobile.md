# Formation — Architectures web et mobile

Fiche de formation pour architecte solution, architecte données, ingénieur DevOps, développeurs back, front et mobile. Elle complète `styles-architecture.md` (styles, API, messagerie, évaluation), `choix-techniques.md` (versions et piles d'octobre 2026), `infrastructure-hebergement.md` et `donnees-schema.md`. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/architectures-web-mobile.md`.

## Sommaire
1. Objectifs
2. Vue d'ensemble : les couches d'un produit web et mobile
3. Modes de rendu web
4. Front-end : structure, état, données
5. Back-end : monolithe modulaire, BFF, API
6. Authentification et sessions
7. Cache à tous les étages
8. Mobile : natif, multiplateforme, PWA
9. Architecture d'une application mobile
10. Hors ligne et réseaux contraints
11. Fichiers, médias, notifications, temps réel
12. Multilingue, RTL, fuseaux
13. Observabilité et livraison
14. Architectures de référence
15. Règles chiffrées
16. Check-list d'audit
17. Anti-patterns et pièges
18. Sources

## 1. Objectifs

L'agent sait :
- choisir un mode de rendu par type de page selon SEO, fraîcheur des données et Web Vitals ;
- structurer front, back et mobile en couches testables, avec une source de vérité par donnée ;
- choisir entre natif, multiplateforme et PWA, et concevoir le hors-ligne ;
- placer l'authentification, le cache et les médias au bon endroit ;
- justifier ces choix en ADR, avec des cibles mesurables adaptées au public visé (y compris réseaux mobiles lents, appareils d'entrée de gamme).

## 2. Vue d'ensemble : les couches d'un produit web et mobile

```
[Navigateur / App mobile]
   │  HTTPS (HTTP/2-3), CDN + WAF
[Front web SSR/SSG]  [BFF optionnel]
   │                     │
[API (REST/GraphQL) — monolithe modulaire]
   │         │            │
[PostgreSQL] [Cache Redis/Valkey] [Stockage objet + CDN images]
   │
[Tâches asynchrones / file]  →  [E-mail, SMS, push, paiement, transporteur]
```
- Une seule API métier pour web et mobile ; un **BFF** seulement si les besoins des clients divergent fortement.
- Les tiers (paiement, SMS, cartes) derrière des adaptateurs (ports et adaptateurs) pour les simuler en test et en changer.

## 3. Modes de rendu web

| Mode | Principe | Pour | Attention |
|---|---|---|---|
| **SSG** (statique) | HTML généré au build | pages de contenu stables, documentation, vitrine | rebuild ou revalidation pour mettre à jour |
| **ISR / revalidation** | statique régénéré à intervalle ou à la demande (webhook) | catalogue, articles, bandeaux pilotés par CMS | gérer l'invalidation ; contenu légèrement en retard |
| **SSR** | HTML à chaque requête | pages personnalisées, SEO + données fraîches (fiche produit avec stock) | coût serveur, TTFB ; mettre en cache ce qui peut l'être |
| **Streaming SSR + composants serveur** | HTML envoyé par morceaux, JS client réduit (React Server Components) | applications Next.js 16 / React 19 | frontière serveur/client à concevoir (`"use client"` au plus bas) |
| **CSR / SPA** | rendu dans le navigateur | back-office authentifié, outils internes | SEO faible, LCP dépendant du JS ; pas pour les pages publiques |
| **Îlots / MPA** (Astro, rendu serveur classique) | HTML serveur + interactivité ciblée | sites de contenu, e-commerce léger | interactions riches plus coûteuses |
Règle : choisir **par route**, pas pour tout le site. Pages publiques indexables → SSG/ISR/SSR ; espace client → SSR ou CSR ; back-office → CSR acceptable.

Next.js 16 (LTS active) : Turbopack par défaut, modèle de cache explicite (Cache Components, directive `use cache`), React 19.2 ; vérifier la documentation de la version installée, les API de cache ayant changé entre 14, 15 et 16.

## 4. Front-end : structure, état, données

- Découpage par **fonctionnalité** (`features/panier`, `features/catalogue`) plutôt que par type technique ; composants d'interface partagés dans un système de design.
- Distinguer l'**état serveur** (données de l'API : TanStack Query, SWR, ou chargement côté serveur) de l'**état d'interface** (ouvert/fermé, saisie : état local, Zustand) ; pas de store global pour tout.
- URL = état partageable (filtres, pagination, onglet) ; le bouton retour fonctionne.
- Formulaires : validation partagée client/serveur (schéma Zod/Valibot), la validation serveur fait foi.
- Budgets : JS initial par route (ex. ≤ 170 ko compressés sur mobile), images optimisées (AVIF/WebP, `srcset`, dimensions réservées), polices auto-hébergées avec `font-display: swap`.
- Accessibilité et internationalisation dès la structure (voir fiches du pôle maquettes).

## 5. Back-end : monolithe modulaire, BFF, API

- **Monolithe modulaire** par défaut (un déploiement, modules métier isolés : catalogue, commande, paiement, client) ; extraire un service seulement sur un besoin mesuré (charge, équipe, cycle de vie).
- Couches par module : interface (HTTP), application (cas d'usage), domaine (règles), infrastructure (base, tiers). Les règles métier ne dépendent ni du framework ni de la base.
- API : REST + OpenAPI par défaut (GraphQL si clients multiples aux besoins très variés) ; versionnement, pagination par curseur, idempotence des POST sensibles (clé d'idempotence pour paiement/commande), erreurs RFC 9457.
- Tâches longues (e-mails, PDF, imports, synchronisations) en **asynchrone** (file : BullMQ, pg-boss, RabbitMQ) avec reprises et idempotence ; motif **outbox** pour publier un événement de façon fiable après écriture en base.
- Processus sans état (12-factor) : sessions et fichiers hors du serveur d'application ; configuration par variables d'environnement ; mise à l'échelle horizontale possible.
- Multi-locataire (SaaS) : isolation par `tenant_id` + Row Level Security, schéma par locataire ou base par locataire selon l'exigence (voir `donnees-schema.md`).

## 6. Authentification et sessions

| Client | Recommandation |
|---|---|
| Web SSR même domaine | session serveur (cookie `HttpOnly; Secure; SameSite=Lax`), protection CSRF |
| SPA sur un autre domaine | motif BFF : le BFF détient les jetons, le navigateur n'a qu'un cookie de session ; éviter les jetons en `localStorage` |
| Mobile | OAuth 2.0 / OIDC **Authorization Code + PKCE** via navigateur système (AppAuth), jetons dans le Keychain / Keystore, jeton d'accès court (5–15 min) + jeton de rafraîchissement rotatif |
| Machine à machine | client credentials, secrets en coffre |
- Fournisseur d'identité : bibliothèque éprouvée (Auth.js/Better Auth, Spring Security), IDaaS, ou Keycloak auto-hébergé (`formation-keycloak.md`) ; jamais de cryptographie maison.
- MFA (TOTP, passkeys/WebAuthn) pour administrateurs au minimum ; autorisation vérifiée côté serveur sur chaque objet (anti-IDOR).

## 7. Cache à tous les étages

| Étage | Exemples | Règle |
|---|---|---|
| Navigateur | `Cache-Control: public, max-age=31536000, immutable` pour les fichiers fingerprintés | HTML : `no-cache` ou court + revalidation |
| CDN / edge | pages SSG/ISR, images, `stale-while-revalidate` | jamais de page personnalisée en cache partagé sans clé (`Vary`, cookie) |
| Application | cache de rendu, données (`use cache`, Redis/Valkey) | invalidation explicite (webhook, événement), TTL de sécurité |
| Base | index, vues matérialisées | mesurer avant de cacher |
Toujours documenter : ce qui est caché, la clé, la durée, qui invalide. Un cache sans stratégie d'invalidation est une anomalie en attente.

## 8. Mobile : natif, multiplateforme, PWA

| Option | Pour | Contre |
|---|---|---|
| **PWA** | une base de code, pas de store, mises à jour instantanées, très léger ; idéal pour un premier lancement ou un usage ponctuel | iOS : fonctions limitées (installation manuelle, push seulement si installée, stockage purgeable) ; découverte via stores absente |
| **React Native (Expo)** | équipe TypeScript/React, partage de logique avec le web, nouvelle architecture par défaut, mises à jour OTA (EAS Update) | modules natifs parfois nécessaires ; dépendance à l'écosystème Expo |
| **Flutter** | rendu homogène, performances, une équipe pour iOS/Android | Dart, taille de l'application, partage limité avec le web |
| **Natif** (SwiftUI, Jetpack Compose) | expérience et accès matériels pointus, performances maximales | deux bases de code |
| **Kotlin Multiplatform** | logique partagée, interfaces natives | maturité de l'interface partagée à évaluer |
Critères : public (Android très majoritaire en Algérie, appareils d'entrée de gamme, data mobile coûteuse : taille d'APK/AAB et consommation comptent), fonctions natives (caméra, paiement NFC, notifications), compétences, budget, besoin de présence en store.

## 9. Architecture d'une application mobile

- Couches (guide Android, transposable à iOS, React Native, Flutter) : **UI** (écrans + état d'écran) → **domaine** (cas d'usage, facultatif) → **données** (dépôts qui arbitrent entre réseau et stockage local).
- **Flux unidirectionnel** : événements montent, état descend ; **source de vérité unique** par donnée (souvent la base locale en hors-ligne d'abord).
- Navigation déclarée et liens profonds (App Links / Universal Links) vérifiés.
- Configuration à distance et **feature flags** ; versions minimales imposées (forcer la mise à jour si l'API casse).
- Compatibilité d'API : l'app N-1, N-2 reste en circulation des mois ; l'API évolue sans casser (champs ajoutés, jamais retirés sans dépréciation).
- Sécurité : MASVS (stockage, réseau TLS, pas de secret dans le binaire, obfuscation si besoin).

## 10. Hors ligne et réseaux contraints

- Concevoir pour 3G/4G instable : requêtes groupées, pagination, compression (Brotli), images adaptées, délais et reprises avec backoff exponentiel et gigue.
- Hors ligne d'abord quand l'usage le justifie (terrain, chantiers, commandes répétées) : base locale (SQLite, Room, Core Data, WatermelonDB, IndexedDB), file d'actions en attente, synchronisation à la reconnexion, résolution de conflits définie (dernier écrit gagne, fusion, ou intervention utilisateur).
- PWA : service worker (stratégies cache-first pour l'interface, network-first pour les données, stale-while-revalidate pour le catalogue), Background Sync où disponible.
- Toujours afficher l'état (hors ligne, synchronisation en cours, échec) et ne jamais perdre une saisie.

## 11. Fichiers, médias, notifications, temps réel

- Fichiers : téléversement direct vers le stockage objet par **URL présignée**, analyse antivirus et validation de type côté serveur, servis par CDN ; images transformées à la volée (redimensionnement, AVIF/WebP).
- Notifications : FCM (Android, web) et APNs (iOS) ; préférences et consentement ; jamais de donnée sensible dans le contenu de la notification.
- Temps réel : SSE pour le flux serveur → client simple, WebSocket pour le bidirectionnel ; sinon interrogation périodique raisonnable.
- E-mail/SMS transactionnels via fournisseur, en asynchrone, avec modèles localisés.

## 12. Multilingue, RTL, fuseaux

- Langues FR/AR/EN (et tamazight si requis) : routes localisées (`/fr`, `/ar`), `lang` et `dir="rtl"` sur `<html>`, propriétés CSS logiques (`margin-inline-start`), messages ICU (pluriels), contenus traduits stockés par locale.
- Dates en UTC en base, affichage dans le fuseau de l'utilisateur (Africa/Algiers = UTC+1, sans heure d'été) ; montants en entiers (centimes) avec devise (DZD).
- Recherche plein texte adaptée à l'arabe (normalisation des formes, diacritiques).

## 13. Observabilité et livraison

- Journaux structurés (JSON) avec identifiant de corrélation propagé (W3C Trace Context), métriques (RED : débit, erreurs, durée), traces distribuées (OpenTelemetry) ; RUM pour les Web Vitals réels ; crash reporting mobile.
- Environnements : local, recette/préproduction (parité avec la production), production ; données fictives hors production.
- Livraison : CI (lint, types, tests, SAST/SCA), déploiements immuables, migrations de base rétrocompatibles (expand/contract), feature flags, retour arrière testé ; mobile : pistes internes/bêta des stores, déploiement progressif (pourcentage).

## 14. Architectures de référence

**A. Site e-commerce B2C/B2B (ex. parapharmacie)** : Next.js 16 (pages catalogue en ISR, fiche produit SSR avec stock en cache court, compte client SSR, back-office CSR) ; API monolithe modulaire (Node/NestJS ou Django) ; PostgreSQL ; Redis/Valkey ; stockage objet + CDN images ; file pour e-mails/factures ; paiement et transporteur derrière adaptateurs ; contenus marketing (bandeaux) en module natif ou CMS headless (voir `formation-datocms.md`).

**B. Application mobile de terrain (hors ligne)** : Expo/React Native ou Flutter ; base locale SQLite, file de synchronisation ; API REST idempotente ; authentification OIDC + PKCE ; photos téléversées par URL présignée en différé ; notifications FCM/APNs.

**C. SaaS multi-locataire** : front SSR + back-office ; API avec isolation RLS ; IdP (Keycloak ou IDaaS) avec organisations ; facturation par adaptateur ; observabilité par locataire.

## 15. Règles chiffrées

- Web Vitals au 75e centile mobile : LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.
- TTFB cible ≤ 800 ms ; API p95 ≤ 300–500 ms (à fixer par exigence).
- JS initial par route ≤ 170 ko compressés (indicatif, mobile d'entrée de gamme).
- Jeton d'accès 5–15 min ; session inactive web 15–30 min pour un espace sensible.
- Application mobile : taille de téléchargement maîtrisée (objectif indicatif < 30 Mo), démarrage à froid < 2 s sur appareil médian.
- Disponibilité et RPO/RTO : fixés par exigence et vérifiés (voir `infrastructure-hebergement.md`).

## 16. Check-list d'audit

- [ ] Mode de rendu choisi par route et justifié (SEO, fraîcheur, Web Vitals).
- [ ] Une API métier documentée (OpenAPI), versionnée, idempotente sur les opérations sensibles ; BFF justifié s'il existe.
- [ ] Monolithe modulaire avec frontières claires ; tiers derrière adaptateurs.
- [ ] Authentification par client conforme (cookies HttpOnly, PKCE mobile) ; aucun jeton en localStorage ; MFA admin.
- [ ] Stratégie de cache documentée (clé, durée, invalidation) ; aucune page personnalisée en cache partagé.
- [ ] Choix mobile justifié par public, fonctions, compétences ; compatibilité N-1/N-2 de l'API.
- [ ] Hors-ligne et réseaux lents traités (reprises, états visibles, pas de perte de saisie).
- [ ] Médias par stockage objet + CDN, téléversement présigné et contrôlé.
- [ ] i18n/RTL, UTC en base, montants en entiers.
- [ ] Observabilité (journaux corrélés, métriques, traces, RUM, crashs) et livraison progressive avec retour arrière.
- [ ] Décisions en ADR avec alternatives et conséquences.

## 17. Anti-patterns et pièges

- SPA pure pour un site public qui vit du référencement.
- Microservices dès le MVP ; base partagée entre « microservices ».
- Deux API divergentes pour web et mobile sans raison ; BFF qui duplique la logique métier.
- Jetons dans localStorage ; sessions en mémoire du serveur empêchant la mise à l'échelle.
- Cache sans invalidation ; contenu personnalisé servi depuis le CDN à un autre utilisateur.
- Application mobile qui casse dès que l'API change ; pas de version minimale forcée.
- Oublier les réseaux lents et les appareils modestes du public réel.
- Fichiers stockés sur le disque du serveur d'application.
- Dates en heure locale en base ; montants en flottants.

## 18. Sources

Consultées le 2026-11-03.
- Next.js, Next.js 16 : https://nextjs.org/blog/next-16
- web.dev, Rendering on the Web : https://web.dev/articles/rendering-on-the-web
- web.dev, Web Vitals : https://web.dev/articles/vitals
- web.dev, Progressive Web Apps : https://web.dev/explore/progressive-web-apps
- Android Developers, Guide to app architecture : https://developer.android.com/topic/architecture
- The Twelve-Factor App : https://12factor.net/
- IETF, RFC 9457 : https://www.rfc-editor.org/rfc/rfc9457
- IETF, RFC 9700 OAuth 2.0 Security Best Current Practice : https://www.rfc-editor.org/rfc/rfc9700
- OWASP, MASVS : https://mas.owasp.org/MASVS/
