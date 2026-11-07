# Formation — Supabase : Postgres managé, Auth, Storage, RLS

Fiche de formation pour architecte solution, ingénieur DevOps et architecte données. Elle complète `donnees-schema.md`, `infrastructure-hebergement.md`, `formation-architectures-web-mobile.md` et `formation-vercel.md` (localisation des données, cas algérien). Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/supabase.md`. Aucun compte n'est créé par un agent.

**Alerte client en Algérie** : Supabase Cloud ne propose pas de région en Algérie. Pour des données personnelles de clients algériens ou un site marchand visant des résidents algériens, les lois 18-05 (hébergement en Algérie selon les sources consultées) et 18-07 modifiée par la loi 25-11 (transfert à l'étranger soumis en principe à autorisation de l'ANPDP) rendent Supabase Cloud **probablement non conforme** sans validation juridique. Alternative : **Supabase auto-hébergé** sur une infrastructure en Algérie, ou PostgreSQL seul. Décision « à valider par un juriste », tracée en ADR (voir `formation-vercel.md` §10–11).

## Sommaire
1. Objectifs
2. Ce qu'est Supabase
3. Clés, rôles et Row Level Security
4. Modélisation et migrations
5. Auth
6. Storage
7. Edge Functions, Realtime, autres briques
8. Intégration côté application (SSR, mobile)
9. Performance et exploitation
10. Offres et coûts
11. Localisation, conformité, auto-hébergement
12. Quand choisir Supabase (ou pas)
13. Check-list d'audit
14. Anti-patterns et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- concevoir un schéma Postgres sécurisé par RLS, exposé par l'API auto-générée sans fuite ;
- utiliser correctement les clés (publishable / secret) et les rôles Postgres ;
- intégrer Auth, Storage et Edge Functions dans une application SSR et mobile ;
- gérer migrations, environnements, sauvegardes et coûts ;
- trancher cloud vs auto-hébergé selon la localisation des données.

## 2. Ce qu'est Supabase

- Plateforme libre (licence Apache 2.0 pour l'essentiel) bâtie sur **PostgreSQL** : base, API REST auto-générée (**PostgREST**), GraphQL (pg_graphql), **Auth** (GoTrue), **Storage** (S3-compatible), **Realtime**, **Edge Functions** (Deno), files (pgmq/Queues), crons (pg_cron), vecteurs (pgvector), Studio (console), CLI.
- Offre cloud managée (régions AWS sur plusieurs continents, dont l'Europe) ou auto-hébergement (Docker Compose officiel).
- Force : c'est du Postgres standard ; on peut en sortir (`pg_dump`) — à condition de ne pas dépendre exclusivement des briques propriétaires du cloud.

## 3. Clés, rôles et Row Level Security

| Clé | Où | Rôle Postgres | Effet |
|---|---|---|---|
| **Publishable** (`sb_publishable_…`) | navigateur, mobile | `anon` (non connecté) ou `authenticated` (connecté) | soumise aux grants et à la **RLS** |
| **Secret** (`sb_secret_…`) | serveur, Edge Functions, crons | `service_role` (`BYPASSRLS`) | **contourne la RLS** ; jamais côté client ni dans un dépôt |
| `anon` / `service_role` (JWT, héritées) | — | idem | **dépréciées d'ici fin 2026** : migrer puis désactiver manuellement |

Règles RLS :
- **Activer la RLS sur toute table du schéma exposé** (`public` ou schéma API) ; une table sans RLS est lisible et modifiable par quiconque a la clé publishable.
- Politiques par opération (`select`, `insert`, `update`, `delete`) et par rôle (`to authenticated`) ; `using` (lignes visibles) et `with check` (lignes écrites).
- Écrire `(select auth.uid())` plutôt que `auth.uid()` dans les politiques (évaluation une fois par requête) et **indexer** les colonnes filtrées (`user_id`, `tenant_id`).
- Ne jamais baser une autorisation sur `user_metadata` (modifiable par l'utilisateur) ; utiliser `app_metadata` ou une table de rôles.
- Fonctions `security definer` : schéma non exposé, `search_path` fixé, droits révoqués à `public` ; sinon elles contournent la RLS.
- Vues : `security_invoker = true` pour qu'elles respectent la RLS.
- Déboguer : vérifier les **grants** d'abord (erreur de permission) puis la politique (résultat vide).
- Tester les politiques : tests SQL (pgTAP) pour chaque rôle — l'utilisateur A ne voit pas les lignes de B.

```sql
alter table commandes enable row level security;
create policy "client lit ses commandes" on commandes
  for select to authenticated using ((select auth.uid()) = client_id);
create policy "client crée ses commandes" on commandes
  for insert to authenticated with check ((select auth.uid()) = client_id);
create index on commandes (client_id);
```

## 4. Modélisation et migrations

- Schéma conçu comme pour tout Postgres (`donnees-schema.md`) : clés primaires (UUID v7 ou identity), contraintes, `timestamptz` en UTC, montants en `numeric`/entiers.
- Ne pas exposer les tables internes : schéma `private` non exposé ; exposer des vues ou fonctions dédiées si besoin.
- **Migrations versionnées** avec la CLI (`supabase migration new`, `supabase db diff`, `supabase db push`) dans le dépôt ; jamais de modification manuelle en production via Studio.
- Environnements : local (`supabase start`, Docker), préproduction, production ; **branches** de prévisualisation (option payante) ; données de seed fictives.
- Types TypeScript générés (`supabase gen types`) pour un client typé.

## 5. Auth

- Méthodes : e-mail + mot de passe, lien magique / OTP, téléphone (SMS via fournisseur), OAuth (Google, Apple, etc.), SSO SAML (offres supérieures), anonyme ; **MFA** TOTP (et téléphone) ; passkeys selon la version (à vérifier).
- Jetons JWT courts + jetons de rafraîchissement ; clés de signature asymétriques (JWKS) recommandées pour vérifier les JWT côté serveur.
- Réglages à durcir : confirmation d'e-mail, politique de mot de passe et détection des mots de passe compromis, limites de débit, CAPTCHA, durée de session, URL de redirection autorisées strictes.
- **SMTP personnalisé** obligatoire en production (le service intégré est limité et réservé aux tests).
- Hooks d'Auth (ajout de rôles dans le jeton, contrôle à l'inscription).
- Alternative : Keycloak ou IDaaS si SSO d'entreprise complexe (voir `formation-keycloak.md`).

## 6. Storage

- Buckets publics (images de catalogue) ou privés (factures, ordonnances) ; politiques RLS sur `storage.objects`.
- URL signées à durée courte pour les fichiers privés ; téléversement direct depuis le client avec politique, ou téléversement résumable (TUS) pour gros fichiers.
- Transformation d'images à la volée (offres payantes) et CDN ; limiter types MIME et tailles par bucket ; analyse antivirus à prévoir hors Supabase si fichiers d'utilisateurs.
- Données de santé (ordonnances) : bucket privé, accès minimal, journalisation, durée de conservation — avis juridique (données sensibles).

## 7. Edge Functions, Realtime, autres briques

- **Edge Functions** (Deno, TypeScript) : webhooks (paiement), logique avec la clé secrète, intégrations tierces ; secrets par `supabase secrets set` ; vérification du JWT de l'appelant ; région d'exécution à vérifier.
- **Realtime** : diffusion des changements de tables (soumis à la RLS), Broadcast et Presence ; limiter aux tables utiles.
- **Database Webhooks / triggers**, **pg_cron** (tâches planifiées), **Queues** (pgmq), **pgvector** (recherche sémantique).
- La logique métier critique peut vivre dans l'API applicative (Node, Django) qui utilise Supabase comme base : choix d'architecture à trancher (tout dans Supabase vs back-end dédié).

## 8. Intégration côté application (SSR, mobile)

- Next.js / SSR : paquet `@supabase/ssr` ; client serveur créé par requête avec les cookies (jamais partagé entre utilisateurs) ; client navigateur avec la clé publishable ; middleware de rafraîchissement de session ; côté serveur, valider l'utilisateur avec `getUser()`/`getClaims()` (vérification du jeton), pas seulement `getSession()` (lu dans le cookie, non vérifié).
- Opérations privilégiées (administration, webhooks) : uniquement côté serveur avec la clé secrète, après contrôle d'autorisation applicatif.
- Mobile : SDK (JS pour React Native/Expo, Flutter, Swift, Kotlin), stockage sécurisé de la session (Keychain/Keystore), OAuth via navigateur système avec PKCE, liens profonds pour les redirections.
- Hors ligne : Supabase n'est pas une base locale ; prévoir SQLite/WatermelonDB/PowerSync et une synchronisation.

## 9. Performance et exploitation

- Connexions : pooler **Supavisor** (mode transaction pour le serverless, port dédié ; pas d'instructions préparées en mode transaction) ; dimensionner la taille de calcul (paliers) selon les connexions et la RAM.
- Index (Index Advisor, `pg_stat_statements`), `explain analyze`, politiques RLS indexées ; Performance et Security Advisors de Studio à traiter.
- Sauvegardes quotidiennes (7 j en Pro, 14 j en Team) ; **PITR** en option ; tester une restauration ; export `pg_dump` régulier hors fournisseur pour la réversibilité.
- Réplicas de lecture, montée de version Postgres planifiée ; journaux (durée selon l'offre), Log Drains (payants).
- Surveillance des quotas (egress, stockage, MAU) et alertes de facturation.

## 10. Offres et coûts (relevés fin septembre 2026, à vérifier)

| Offre | Prix | Points clés |
|---|---|---|
| **Free** | 0 USD | 2 projets actifs, 500 Mo de base, 1 Go de fichiers, 5 Go d'egress, 50 000 MAU ; **projets mis en pause après une semaine d'inactivité** ; pas de sauvegarde exploitable : inadapté à la production |
| **Pro** | dès 25 USD/mois (1er projet, 10 USD de crédit compute = instance Micro) | 8 Go base, 100 Go fichiers, 250 Go egress, 100 000 MAU ; dépassements facturés (ex. 0,09 USD/Go egress, 0,125 USD/Go base) ; projet supplémentaire dès 10 USD/mois ; plafond de dépenses qui exclut compute, réplicas, PITR |
| **Team** | dès 599 USD/mois | conformité (SOC 2, ISO 27001), SSO de la console, rôles fins, sauvegardes 14 j ; HIPAA en option |
| **Enterprise** | sur devis | SLA, support 24/7, PrivateLink |
- Postes de coût : palier de calcul (le plus significatif), egress (images non mises en cache), PITR, réplicas, Log Drains (60 USD/drain/projet), branches.
- Estimation en trois scénarios avec le pôle finance.

## 11. Localisation, conformité, auto-hébergement

- Cloud : région choisie à la création (non modifiable ensuite sans migration) ; régions européennes disponibles (Francfort, Paris, Londres, etc. : vérifier) ; Supabase Inc. est une société américaine (DPA, clauses types).
- **Client algérien** : pas de région en Algérie → voir alerte en tête ; option **auto-hébergée** sur serveurs en Algérie.
- **Auto-hébergement** (Docker Compose officiel : Postgres, Auth, PostgREST, Realtime, Storage, Kong, Studio, Edge Runtime) :
  - régénérer **tous** les secrets et clés (JWT secret, clés, mot de passe Postgres, accès Studio) ; Studio derrière authentification et réseau privé ;
  - TLS par reverse proxy, sauvegardes et PITR à construire (pgBackRest/WAL-G), mises à jour à suivre (images épinglées), supervision ;
  - certaines fonctions du cloud absentes ou à reconstruire (branches, advisors, transformations d'images selon version, pooler managé) ;
  - charge d'exploitation réelle : à chiffrer (compétence Postgres requise). Alternative plus simple : PostgreSQL seul + API applicative + Auth (Keycloak) + stockage objet (MinIO/Garage) en Algérie.

## 12. Quand choisir Supabase (ou pas)

| Situation | Recommandation |
|---|---|
| MVP, SaaS, application mobile, équipe front forte, données hors Algérie autorisées | Supabase Cloud Pro, région au plus près des utilisateurs, RLS stricte |
| Données personnelles de clients algériens / site marchand algérien | auto-hébergé en Algérie, ou Postgres + back-end classique en Algérie (après avis juridique) |
| Logique métier complexe, ERP, intégrations lourdes | back-end dédié (NestJS, Django, Spring) avec Postgres ; Supabase éventuellement comme base managée seulement |
| Exigences de conformité élevées (santé, finance) | offre Team/Enterprise ou auto-hébergé maîtrisé ; analyse d'impact |

## 13. Check-list d'audit

- [ ] RLS activée sur 100 % des tables exposées ; politiques par opération et rôle, testées (pgTAP) avec deux utilisateurs.
- [ ] Clés publishable/secret utilisées ; clés héritées migrées et désactivées avant fin 2026 ; clé secrète absente du client et du dépôt.
- [ ] Fonctions `security definer` hors schéma exposé, `search_path` fixé ; vues en `security_invoker`.
- [ ] Autorisation jamais fondée sur `user_metadata`.
- [ ] Migrations versionnées via CLI ; aucune modification manuelle en production.
- [ ] Auth durcie : SMTP personnalisé, confirmation e-mail, limites, CAPTCHA, redirections strictes, MFA admin.
- [ ] Buckets privés pour documents sensibles, URL signées courtes, types/tailles limités.
- [ ] SSR : client par requête, utilisateur vérifié côté serveur (`getUser`/`getClaims`).
- [ ] Pooler adapté (transaction pour serverless), index sur colonnes de RLS, advisors traités.
- [ ] Sauvegardes testées, export hors fournisseur, PITR si exigé.
- [ ] Offre ≠ Free en production ; alertes de coût ; estimation en trois scénarios.
- [ ] Localisation des données validée juridiquement (Algérie : auto-hébergement en Algérie par défaut).

## 14. Anti-patterns et pièges

- Table créée sans RLS « pour tester » puis oubliée (fuites massives documentées sur des applications générées rapidement).
- Clé `service_role`/secrète dans le code du front, une app mobile ou un dépôt public.
- Politique `using (true)` sur une table sensible ; autorisation sur `user_metadata`.
- `getSession()` côté serveur pour décider d'un accès.
- Production sur l'offre Free (pause après une semaine d'inactivité, pas de sauvegarde).
- Logique métier dispersée entre triggers, Edge Functions et front sans architecture.
- Auto-hébergement avec les secrets d'exemple du dépôt.
- Région choisie au hasard (non modifiable) ; données algériennes hébergées à l'étranger sans autorisation.

## 15. Sources

Consultées le 2026-11-03.
- Supabase, API keys : https://supabase.com/docs/guides/api/api-keys.md
- Supabase, Row Level Security : https://supabase.com/docs/guides/database/postgres/row-level-security
- Supabase KB, coût d'un projet base seule : https://supabase.com/kb/faqs/platform/database-only-cost
- Jetadmin, Supabase Review 2026 (prix relevés le 26/09/2026, source secondaire) : https://www.jetadmin.io/blog/supabase-review/
- ComputingForGeeks, Self-host Supabase with Docker Compose (source secondaire) : https://computingforgeeks.com/self-host-supabase-docker-compose/
- Gide, Algérie – loi 25-11 : https://www.gide.com/en/?p=93297
