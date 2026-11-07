# Formation — Keycloak : gestion des identités et des accès auto-hébergée

Fiche de formation pour architecte solution, architecte sécurité, développeur back-end et ingénieur DevOps. Elle complète `formation-architectures-web-mobile.md` (§6 authentification), `formation-supabase.md` (Auth intégrée) et le pôle sécurité. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/keycloak.md`. Version de référence : **Keycloak 26.8.1** (octobre 2026) ; vérifier la dernière version et les avis de sécurité avant toute décision.

## Sommaire
1. Objectifs
2. Quand choisir Keycloak
3. Modèle : realms, clients, utilisateurs, rôles, groupes
4. Protocoles et flux
5. Authentification forte : MFA, WebAuthn, passkeys
6. Fédération d'identité
7. Thèmes, i18n, e-mails
8. Sessions, jetons, révocation
9. Administration et automatisation
10. Déploiement
11. Mises à jour et sécurité
12. Observabilité
13. Intégration avec une application Node SSR
14. Check-list d'audit
15. Anti-patterns et pièges
16. Sources

## 1. Objectifs

L'agent sait :
- décider entre Keycloak, une authentification intégrée au framework et un IDaaS ;
- modéliser realms, clients, rôles et groupes au plus juste ;
- choisir le bon flux OAuth 2.0 / OIDC (ou SAML) par type de client ;
- configurer MFA, fédération, thèmes et i18n (FR/AR RTL/EN) ;
- déployer Keycloak en production (conteneur, base, haute disponibilité), le tenir à jour et le surveiller ;
- intégrer une application Node SSR de façon sûre.

## 2. Quand choisir Keycloak

| Option | Pour | Contre |
|---|---|---|
| **Auth intégrée** (Auth.js/Better Auth, Django auth, Spring Security, Supabase Auth) | une seule application, besoins simples, peu d'exploitation | SSO multi-applications limité, fédération d'entreprise à construire |
| **Keycloak** (libre, Apache 2.0, projet CNCF) | plusieurs applications à fédérer (SSO), rôles fins, fédération LDAP/AD, SAML et OIDC, **données d'identité hébergées où l'on veut** (ex. en Algérie), pas de coût par utilisateur | exploitation réelle (mises à jour fréquentes, base, haute dispo, sécurité), courbe d'apprentissage, thèmes à maintenir |
| **IDaaS** (Auth0/Okta, Microsoft Entra ID / External ID, AWS Cognito, Google Identity Platform, Zitadel Cloud…) | exploitation déléguée, fonctions avancées (détection d'attaques), conformité fournie | coût par MAU, données hors du pays, dépendance |
| **Alternatives libres** | Zitadel, Authentik, Ory, Authelia (portail) | maturité et fonctionnalités à comparer |
Règle : ne jamais écrire sa propre gestion de mots de passe et de jetons. Keycloak se justifie dès qu'il y a ≥ 2 applications à fédérer, un annuaire d'entreprise, ou une contrainte de localisation des données d'identité.

## 3. Modèle : realms, clients, utilisateurs, rôles, groupes

- **Realm** : espace d'isolation (utilisateurs, clients, réglages). Le realm `master` sert **uniquement** à administrer Keycloak ; créer un realm par produit/organisation (`parapro`). Multi-locataire : un realm par locataire si isolement fort exigé (coût d'administration), sinon **Organizations** (fonction native des versions 26 pour le B2B) ou groupes.
- **Client** : application ou API. Types : **confidentiel** (serveur qui garde un secret : SSR, BFF, back-end), **public** (SPA, mobile : pas de secret, PKCE obligatoire), **bearer-only** historique remplacé par la simple validation de jeton côté API.
- **Rôles** : de realm (transverses : `admin`, `client`) et de client (propres à une application : `catalogue:editer`) ; **rôles composites** avec parcimonie.
- **Groupes** : hiérarchiques, portent des rôles et attributs ; affecter les rôles aux groupes, les utilisateurs aux groupes.
- **Client scopes** et **mappers** : contrôlent ce qui entre dans les jetons (minimiser : pas de données personnelles inutiles dans un JWT lisible par le client).
- **Authorization Services** (UMA, politiques fines) : puissants mais complexes ; souvent, l'autorisation métier reste dans l'application (rôles dans le jeton + règles par objet côté API).
- **User Profile** déclaratif : attributs, validation, permissions de modification par l'utilisateur ou l'admin.

## 4. Protocoles et flux

| Client | Flux | Réglages |
|---|---|---|
| Application web SSR / BFF | **Authorization Code** (client confidentiel) + **PKCE** | secret ou, mieux, `private_key_jwt` ; redirections exactes |
| SPA | Authorization Code + PKCE (client public) — de préférence via un BFF qui garde les jetons | pas d'implicit flow ; pas de jetons en localStorage |
| Mobile | Authorization Code + PKCE via navigateur système (AppAuth), liens d'app vérifiés | pas de WebView intégrée pour la connexion |
| Machine à machine | **Client Credentials** | compte de service du client, rôles minimaux |
| Appareils sans clavier | Device Authorization Grant | |
| Délégation entre services | Token Exchange (standard, RFC 8693) | à n'activer que si nécessaire |
- Désactiver sur chaque client ce qui n'est pas utilisé : Implicit, Direct Access Grants (mot de passe), Service accounts.
- **Redirect URIs** et **Web origins** exacts (pas de `*`), **post-logout redirect URIs** déclarées.
- Options de sécurité : PAR (Pushed Authorization Requests), DPoP ou mTLS pour lier les jetons (profils FAPI pour la finance), refresh token rotation (« revoke refresh token »).
- **SAML 2.0** : pour les applications d'entreprise qui l'exigent ; signer les assertions, valider les signatures, métadonnées à jour.

## 5. Authentification forte : MFA, WebAuthn, passkeys

- **TOTP** (application d'authentification), **WebAuthn** (clés de sécurité) et **passkeys** (WebAuthn sans mot de passe, prise en charge renforcée dans la série 26), codes de récupération, OTP par e-mail selon version.
- Flux d'authentification configurables (Browser flow) : MFA obligatoire pour les rôles administrateurs ; **authentification conditionnelle** (par rôle, par client, par niveau requis : **step-up** via `acr_values` / Level of Authentication).
- Politique de mots de passe (longueur ≥ 12, liste noire, historique, hachage : algorithme par défaut moderne — vérifier pbkdf2/argon2 selon version) ; **brute force detection** activée (verrouillage progressif).
- Actions requises : vérification d'e-mail, configuration OTP, mise à jour du mot de passe, acceptation des conditions.

## 6. Fédération d'identité

- **User Federation** : LDAP / Active Directory (lecture seule ou synchronisation, mappers de groupes et rôles, LDAPS obligatoire), Kerberos.
- **Identity Brokering** : connexion via Google, Apple, Microsoft, GitHub, Facebook, ou tout fournisseur OIDC/SAML d'entreprise ; « first broker login » (liaison de comptes existants : vérifier l'e-mail avant de lier pour éviter la prise de contrôle) ; mappers d'attributs.
- Connexion sociale pour le grand public algérien : Google très répandu ; Apple obligatoire sur iOS si d'autres connexions sociales sont proposées (règles App Store).
- Organisations B2B : rattachement par domaine d'e-mail, fournisseur d'identité par organisation.

## 7. Thèmes, i18n, e-mails

- Thèmes : login, account, e-mail, admin ; **Keycloakify** (React) ou thèmes FreeMarker ; nouvelle console de compte et thème de connexion par défaut modernes ; maintenir le thème à chaque montée de version.
- **Internationalisation** : activer les langues (fr, ar, en…), langue par défaut, fichiers de messages personnalisés ; vérifier le rendu **RTL** de l'arabe (direction, alignement, icônes) ; traductions des e-mails.
- Accessibilité du thème (WCAG 2.2 AA : libellés, erreurs, contraste, clavier).
- E-mails : SMTP du realm avec TLS strict (attention au repli en clair avec `starttls` signalé dans les avis d'octobre 2026), SPF/DKIM/DMARC du domaine expéditeur.

## 8. Sessions, jetons, révocation

- Jeton d'accès court (**5 min** par défaut, 5–15 min selon le besoin) ; jeton de rafraîchissement lié à la session ; **SSO Session Idle** (ex. 30 min) et **Max** (ex. 10 h) ; sessions hors ligne (offline tokens) seulement si indispensables (mobile), avec durée bornée.
- Les API valident les jetons localement (signature via JWKS, `iss`, `aud`, `exp`, `azp`) ; l'introspection sert aux jetons opaques ou aux révocations immédiates.
- **Révocation** : déconnexion de l'utilisateur (console ou API), révocation des sessions, « not-before » sur le realm ou le client ; rotation des jetons de rafraîchissement.
- Déconnexion : RP-initiated logout (`end_session_endpoint` avec `id_token_hint`), **back-channel logout** pour prévenir les applications (signature vérifiée obligatoire), front-channel en complément.
- Rotation des **clés de signature** (fournisseurs de clés RS256/ES256, clés actives/passives) sans casser les jetons en cours.

## 9. Administration et automatisation

- Console d'administration : accès restreint (réseau d'administration, pas exposée sur Internet), MFA obligatoire, comptes nominatifs, pas d'admin partagé.
- **Permissions d'administration fines** (admin délégués par realm/groupe) : les tester, des failles d'élévation ont été corrigées en 2026.
- Automatisation : **Admin REST API**, `kcadm.sh`, **keycloak-config-cli** ou **Terraform provider** pour versionner realms, clients, rôles (configuration as code) ; import/export de realm (`kc.sh export/import`) sans secrets dans le dépôt.
- Événements : **événements utilisateur** (connexion, échec, mise à jour) et **événements admin** activés, conservation bornée, export vers le SIEM.

## 10. Déploiement

- Distribution **Quarkus** (WildFly abandonné) : image officielle `quay.io/keycloak/keycloak:26.x` ; phase **build** (`kc.sh build` : base, fonctionnalités, providers) puis **start** optimisé (`--optimized`) ; jamais `start-dev` en production.
- Base : **PostgreSQL** (ou autre supportée) dédiée, sauvegardée ; l'embarquée (dev-file) est réservée au développement.
- Options clés : `hostname` (URL publique), `proxy-headers=xforwarded` (ou `forwarded`) derrière reverse proxy, TLS de bout en bout ou terminaison au proxy avec réseau privé, `http-enabled=false` en direct, `health-enabled`, `metrics-enabled`.
- Exposer uniquement les chemins nécessaires (`/realms/`, `/resources/`) ; **`/admin` et port de gestion (9000) non exposés publiquement**.
- **Haute disponibilité** : ≥ 2 instances, cache distribué Infinispan (sessions), sessions persistantes en base (par défaut dans la série 26), répartiteur avec affinité facultative ; multi-sites possible (architecture actif/actif documentée).
- Kubernetes : **opérateur Keycloak** (CRD `Keycloak`, `KeycloakRealmImport`) ; ressources : ≥ 1–2 vCPU et 1–2 Go RAM par instance comme point de départ, à mesurer (le hachage de mot de passe est coûteux en CPU).
- Localisation : Keycloak auto-hébergé permet de garder les identités sur une infrastructure en Algérie (loi 18-07/25-11) — choix à valider avec le juriste.

## 11. Mises à jour et sécurité

- Rythme : mineures 26.x fréquentes, correctifs de sécurité réguliers ; la branche corrigée n'est pas toujours rétroportée (ex. 26.7 → passer en 26.8.1). Prévoir une **fenêtre de mise à jour mensuelle** et une procédure (lecture du guide de migration, préproduction, sauvegarde de la base, tests de connexion automatisés, retour arrière).
- Exemples 2026 à retenir : **CVE-2026-18963** (prise de contrôle par réinitialisation de mot de passe, CVSS 9,1, corrigée en 26.4.15 / 26.6.6 / 26.7.2, code d'exploitation public) ; **26.8.1** (octobre 2026) corrige 18 CVE (dont élévation d'un admin délégué, contournement de 2FA, logout back-channel non signé, repli SMTP en clair) — sources secondaires à recouper avec les avis GHSA officiels.
- Veille : avis GitHub Security Advisories du dépôt keycloak, liste keycloak-announce, CERT-FR.
- Durcissement : realm `master` réservé à l'admin, console non exposée, MFA admin, brute force activée, clients minimaux, redirections exactes, PKCE partout, jetons courts, événements activés, en-têtes de sécurité (CSP, X-Frame-Options du realm), providers tiers audités, secrets (base, clients, SMTP) en coffre, image épinglée et scannée (Trivy).
- Tests de sécurité : flux de réinitialisation, liaison de comptes fédérés, élévation de privilèges admin, redirections ouvertes, CSRF sur la connexion.

## 12. Observabilité

- Métriques Prometheus (`/metrics` sur le port de gestion) : connexions, échecs, durées, sessions, cache ; tableaux de bord Grafana fournis par le projet.
- Santé : `/health/ready`, `/health/live` pour l'orchestrateur.
- Journaux structurés JSON, niveau INFO, sans jetons ni mots de passe ; événements vers le SIEM ; alertes sur pics d'échecs (attaque par force brute, bourrage d'identifiants).
- Traces OpenTelemetry (selon version).

## 13. Intégration avec une application Node SSR

Principe : l'application SSR est un **client confidentiel** ; elle réalise le flux Authorization Code + PKCE côté serveur, garde les jetons côté serveur et ne donne au navigateur qu'un cookie de session.

- Bibliothèques OIDC standard, pas d'adaptateur Keycloak (les adaptateurs historiques sont dépréciés) : `openid-client` (Node), Auth.js (fournisseur Keycloak) pour Next.js, `express-openid-connect`, Passport + `openid-client`.
- Découverte : `https://auth.exemple.dz/realms/parapro/.well-known/openid-configuration`.
- Cookie de session `HttpOnly; Secure; SameSite=Lax`, chiffré ; stockage des jetons côté serveur (session store Redis) pour éviter de gros cookies.
- Rafraîchir le jeton d'accès côté serveur avant expiration ; gérer l'échec (session terminée → reconnexion).
- Côté API (Node) : valider le JWT avec `jose` (`createRemoteJWKSet` sur `/protocol/openid-connect/certs`), vérifier `iss`, `aud` (mapper d'audience à configurer), `exp`, puis rôles dans `realm_access` / `resource_access`.
- Déconnexion : détruire la session locale puis rediriger vers `end_session_endpoint` avec `id_token_hint` et `post_logout_redirect_uri` ; implémenter le back-channel logout si plusieurs applications.

```ts
// API Node : vérification d'un jeton Keycloak
import { createRemoteJWKSet, jwtVerify } from 'jose';
const ISS = 'https://auth.exemple.dz/realms/parapro';
const JWKS = createRemoteJWKSet(new URL(`${ISS}/protocol/openid-connect/certs`));
export async function verifier(token: string) {
  const { payload } = await jwtVerify(token, JWKS, { issuer: ISS, audience: 'api-catalogue' });
  const roles = (payload as any).resource_access?.['api-catalogue']?.roles ?? [];
  return { sub: payload.sub, roles };
}
```

## 14. Check-list d'audit

- [ ] Choix Keycloak justifié (SSO, fédération, localisation) en ADR ; version courante corrigée de tous les avis connus.
- [ ] Realm `master` réservé à l'administration ; console et port de gestion non exposés ; MFA admin ; admins nominatifs.
- [ ] Clients minimaux : flux inutiles désactivés, PKCE, redirections et origines exactes, secrets en coffre ou `private_key_jwt`.
- [ ] Jetons courts, rotation des refresh tokens, durées de session définies ; mappers limités (pas de données personnelles superflues).
- [ ] MFA/passkeys pour les rôles sensibles ; brute force activée ; politique de mots de passe.
- [ ] Fédération : LDAPS, liaison de comptes vérifiée par e-mail ; brokering SAML/OIDC à jour des correctifs.
- [ ] Thème FR/AR (RTL)/EN, accessible ; e-mails en TLS strict, SPF/DKIM/DMARC.
- [ ] Production : `start --optimized`, PostgreSQL sauvegardé, ≥ 2 instances, proxy configuré, `hostname` fixé.
- [ ] Configuration as code (Terraform/keycloak-config-cli) ; événements utilisateur et admin vers le SIEM.
- [ ] Métriques, santé, alertes sur échecs ; procédure de mise à jour mensuelle testée.
- [ ] Côté application : bibliothèque OIDC standard, jetons côté serveur, validation complète des JWT côté API, déconnexion complète.

## 15. Anti-patterns et pièges

- Utiliser le realm `master` pour les utilisateurs de l'application.
- `start-dev` ou base embarquée en production ; console d'administration exposée sur Internet.
- Redirect URI `*` ; Direct Access Grants (mot de passe) activé pour une application web ; implicit flow.
- Jetons dans localStorage ; SPA qui détient un secret client.
- Rester sur une branche non corrigée (26.7 après octobre 2026, ou avant 26.4.15/26.6.6 pour CVE-2026-18963).
- Tout mettre dans Authorization Services sans besoin ; rôles composites en cascade incompréhensibles.
- Liaison automatique de comptes fédérés sans vérification d'e-mail.
- Valider un JWT sans vérifier `aud` ni `iss` ; se fier au contenu d'un jeton non vérifié.
- Thème personnalisé jamais mis à jour, qui casse à la montée de version.
- Choisir Keycloak pour une seule petite application sans capacité d'exploitation.

## 16. Sources

Consultées le 2026-11-03.
- Keycloak, blog archive (annonces de versions) : https://www.keycloak.org/blog-archive
- Keycloak, All configuration : https://www.keycloak.org/server/all-config
- Keycloak, Securing applications with OIDC : https://www.keycloak.org/securing-apps/oidc-layers
- API Evangelist, Keycloak 26.7.3 released (relais) : https://blogs.apievangelist.com/blogs/keycloak-2026-08-31-keycloak-26-7-3-released/
- Keycloak Advisory Watch, correctifs de 26.8.1 (source secondaire) : https://buttondown.com/keycloak-advisory-watch/archive/keycloak-security-fixes-in-2681/
- Skycloak, CVE-2026-18963 (source secondaire) : https://skycloak.io/blog/keycloak-password-reset-cve-2026-18963/
- Vigilance, vulnérabilités Keycloak du 19/03/2026 : https://vigilance.fr/vulnerability/Keycloak-multiple-vulnerabilities-dated-19-03-2026-50100
- IETF, RFC 9700 OAuth 2.0 Security BCP : https://www.rfc-editor.org/rfc/rfc9700
