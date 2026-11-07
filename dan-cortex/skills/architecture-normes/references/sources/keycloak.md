# Collecte — Keycloak

Pages consultées le 2026-11-03 (outils : WebSearch, WebFetch). Résumés et reformulations ; aucune copie de page.

| URL | Titre | Apport |
|---|---|---|
| https://www.keycloak.org/blog-archive | Keycloak – blog archive | Annonces officielles des versions (série 26.x en 2026). |
| https://blogs.apievangelist.com/blogs/keycloak-2026-08-31-keycloak-26-7-3-released/ | Keycloak 26.7.3 released (31 août 2026, relais) | Rythme de publication : 26.5.5 (mars), 26.6.2 (mai), 26.7.3 (août 2026). |
| https://buttondown.com/keycloak-advisory-watch/archive/keycloak-security-fixes-in-2681/ | Keycloak Advisory Watch – correctifs de 26.8.1 (13 oct. 2026, source secondaire) | 26.8.1 corrige 18 CVE Keycloak (14 moyennes, 3 faibles, 1 non notée : élévation d'un admin délégué en realm-admin via groupe) et des CVE de dépendances (jackson-databind) ; pas de correctif annoncé pour 26.7.x ; problème SAML signalé (#53354) sans CVE. À recouper avec les avis GHSA officiels. |
| https://skycloak.io/blog/keycloak-password-reset-cve-2026-18963/ | CVE-2026-18963 (source secondaire) | Prise de contrôle de compte par le flux de réinitialisation de mot de passe (CVSS 9,1) ; corrigé en 26.4.15, 26.6.6, 26.7.2 (août 2026) ; code d'exploitation public ; contournement : désactiver « Forgot password ». |
| https://vigilance.fr/vulnerability/Keycloak-multiple-vulnerabilities-dated-19-03-2026-50100 | Vigilance – vulnérabilités Keycloak du 19/03/2026 | Fréquence des avis de sécurité : suivi de veille indispensable. |
| https://www.keycloak.org/server/all-config | Keycloak – All configuration (référence) | Options serveur (`hostname`, `proxy-headers`, `http-enabled`, `db`, `cache`, `metrics-enabled`, `health-enabled`) — pratiques connues, à recouper sur la version installée. |
| https://www.keycloak.org/securing-apps/oidc-layers | Keycloak – Securing applications (OIDC) | Recommandation d'utiliser des bibliothèques OIDC standard côté application (les adaptateurs Keycloak historiques sont dépréciés). |
