# Formation — Vercel : déploiement front, fonctions, coûts et localisation des données

Fiche de formation pour architecte solution, ingénieur DevOps et architecte données. Elle complète `infrastructure-hebergement.md`, `formation-architectures-web-mobile.md` et le pôle juridique. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/vercel.md`. Aucun compte n'est créé et aucun déploiement n'est fait par un agent (garde-fous).

**Alerte client en Algérie (à lire d'abord)** : pour un site de vente en ligne destiné à des résidents algériens, la loi 18-05 sur le commerce électronique et ses textes d'application imposent, selon les sources consultées, un hébergement sur des serveurs situés en Algérie et un nom de domaine .dz ; la loi 18-07 (modifiée par la loi 25-11 du 24 juillet 2025) soumet en principe le transfert de données personnelles à l'étranger à l'autorisation préalable de l'ANPDP. Vercel n'a pas de région en Algérie. Un hébergement Vercel de la boutique ou de données personnelles de clients algériens est donc **probablement non conforme** sans montage spécifique : décision **à valider par un juriste** en droit algérien, tracée en ADR.

## Sommaire
1. Objectifs
2. Ce qu'est Vercel
3. Concepts : projets, déploiements, environnements
4. Exécution : CDN, fonctions, middleware, rendu
5. Régions et latence
6. Données et stockage
7. Sécurité
8. Observabilité
9. Offres et coûts
10. Localisation des données : UE, Algérie
11. Montages possibles pour un client algérien
12. Alternatives
13. Check-list d'audit
14. Anti-patterns et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- décrire ce que Vercel héberge (front, fonctions, cache) et ce qu'il n'héberge pas (base principale, sauf intégrations tierces) ;
- configurer environnements, régions et sécurité de façon raisonnée ;
- estimer les coûts et repérer les risques de facture ;
- analyser la localisation des données et la conformité, en particulier pour un client algérien, et proposer des montages ou des alternatives.

## 2. Ce qu'est Vercel

- Plateforme cloud (infrastructure principalement AWS, réseau Anycast, 19 régions de calcul) spécialisée dans le déploiement de front-ends et de fonctions serveur, éditrice de Next.js.
- Déploiement à partir de Git (chaque branche/PR → URL de prévisualisation), CDN mondial, fonctions (Node.js, Python, Go, Ruby…), middleware, optimisation d'images, analytics, WAF, flags, AI Gateway, Workflows, marketplace d'intégrations (bases de données, stockage, CMS).
- Fonctionne avec de nombreux frameworks (Next.js, Nuxt, SvelteKit, Astro, Remix/React Router, Vite) ; Next.js y est le plus intégré.

## 3. Concepts : projets, déploiements, environnements

- **Projet** lié à un dépôt ; **déploiements immuables** ; **Production** (branche principale), **Preview** (chaque branche/PR), **Development** (local, `vercel dev`) ; environnements personnalisés sur les offres payantes.
- **Variables d'environnement** par environnement, marquées sensibles ; ne jamais exposer un secret côté client (préfixe `NEXT_PUBLIC_` = public).
- **Domaines** : production sur domaine personnalisé ; prévisualisations protégées (Deployment Protection : authentification Vercel, mot de passe, contournement pour l'automatisation).
- **Rollback instantané** vers un déploiement précédent ; **Rolling Releases** (déploiement progressif) selon l'offre.
- Configuration : réglages du projet et `vercel.json` / `vercel.ts` (régions, en-têtes, redirections, crons, durée max des fonctions).

## 4. Exécution : CDN, fonctions, middleware, rendu

- **CDN** : fichiers statiques et pages SSG/ISR en cache ; `Cache-Control` et revalidation (temps ou à la demande via webhook).
- **Fonctions** (Vercel Functions, modèle « Fluid compute » : instances réutilisées, concurrence par instance, facturation au **CPU actif** et à la mémoire provisionnée) ; durée max configurable (jusqu'à 300 s par défaut selon l'offre, davantage en Pro/Enterprise : à vérifier).
- **Middleware / routing middleware** : exécuté avant le cache pour réécritures, redirections, A/B, géolocalisation ; garder léger (pas d'appel base lourd).
- **Crons** (tâches planifiées), **Queues/Workflows** pour l'asynchrone (vérifier disponibilité et quotas).
- **Images** : optimisation à la demande (quota de transformations : poste de coût à surveiller).
- Pas de processus long, pas de WebSocket serveur persistant natif : prévoir un service tiers ou un autre hébergement pour le temps réel bidirectionnel.

## 5. Régions et latence

- Les **fonctions s'exécutent par défaut aux États-Unis** (région de Washington, `iad1`) ; choisir la région au plus près de la **base de données** (pas de l'utilisateur) pour limiter les allers-retours.
- Régions européennes disponibles (Francfort, Paris, Londres, Dublin, Stockholm : codes à vérifier dans la documentation des régions). Pour un public algérien et une base en Europe, Paris ou Francfort minimisent la latence (≈ 30–50 ms depuis Alger, indicatif).
- Plusieurs régions et bascule (failover) : offres Pro/Enterprise.
- Le CDN sert le contenu statique depuis le point de présence le plus proche de l'utilisateur, où qu'il soit : des copies du contenu en cache existent hors de la région choisie.

## 6. Données et stockage

- Vercel ne fournit pas de base relationnelle propre : intégrations marketplace (Neon, Supabase, PlanetScale, Upstash Redis, etc.) avec leurs propres régions et contrats.
- Stockage : **Vercel Blob** (fichiers), **Edge Config** (configuration à lecture très rapide), cache de données ; vérifier la région de chaque service.
- Journaux d'exécution conservés peu de temps selon l'offre (1 h en Hobby) ; **drains** de journaux vers un outil externe pour l'audit.
- Les données personnelles transitent par les fonctions et peuvent apparaître dans les journaux : masquer (voir skill `confidentialite-traces`).

## 7. Sécurité

- Certifications : SOC 2 Type 2, ISO 27001:2022, PCI DSS (AOC prestataire), HIPAA (BAA en Pro avec option ou Enterprise) ; certification EU-US Data Privacy Framework.
- **WAF** et règles personnalisées, protection DDoS, limitation de débit, **Attack Challenge Mode**, BotID ; nombre de règles limité selon l'offre.
- Deployment Protection sur les prévisualisations (elles exposent souvent des données de test et des fonctionnalités non publiées).
- En-têtes de sécurité (CSP, HSTS…) via `next.config` ou `vercel.json` ; secrets en variables sensibles ; jetons d'API à portée minimale ; SSO/SAML et journaux d'audit en Enterprise.
- **Secure Compute** (Enterprise) : réseau privé isolé, IP sortantes dédiées, VPC peering/VPN vers une base privée ; ce n'est pas, à lui seul, une garantie de résidence des données.

## 8. Observabilité

- Logs d'exécution, Observability (requêtes, fonctions, cache), **Speed Insights** (Web Vitals réels), **Web Analytics** (sans cookie, quotas), traces OpenTelemetry ; drains vers Datadog, Grafana, etc.
- Alertes d'usage et **plafond de dépenses** (Spend Management) à configurer dès le départ.

## 9. Offres et coûts (à vérifier sur la page tarifs au moment de la décision)

| Offre | Prix | Points clés |
|---|---|---|
| **Hobby** | gratuit | **usage personnel non commercial uniquement** ; quotas mensuels (100 Go de transfert, 1 M requêtes CDN, 4 h CPU actif, 1 M invocations, 5 000 transformations d'images…) ; au dépassement, fonction bloquée jusqu'à 30 jours |
| **Pro** | 20 USD par siège déployeur et par mois, crédit d'usage de 20 USD inclus | 1 To de transfert, 10 M requêtes ; facturation à l'usage au-delà (ex. ≈ 0,15 USD/Go de transfert, selon région) ; rôles en lecture gratuits |
| **Enterprise** | sur devis | SLA, SSO, Secure Compute, multi-régions, support, contrats sur mesure |
- Un site commercial (boutique, site d'entreprise) **ne peut pas** être en Hobby.
- Postes de coût à surveiller : CPU actif des fonctions (SSR non caché), transferts (images lourdes, vidéos), transformations d'images, requêtes CDN (robots), journaux et analytics au-delà des quotas, sièges.
- Bonnes pratiques coût : maximiser SSG/ISR et le cache, limiter le middleware, optimiser les images à la source, bloquer les robots abusifs (WAF), plafond de dépenses et alertes.

## 10. Localisation des données : UE, Algérie

**Pour un client européen (RGPD)** : Vercel Inc. est une société américaine ; transferts encadrés par le DPA (clauses contractuelles types) et la certification DPF ; choisir une région européenne pour les fonctions et les services de données ; documenter le risque d'accès extraterritorial (CLOUD Act) dans l'analyse d'impact si les données sont sensibles.

**Pour un client en Algérie** :
- **Loi 18-05 (commerce électronique)** : selon le guide officiel et les synthèses consultées, un site marchand vendant à des résidents algériens doit être hébergé sur des serveurs en Algérie et utiliser un domaine .dz / .com.dz ; inscription au CNRC (code d'activité e-commerce). Articles exacts à vérifier dans le texte et le guide de l'e-commerce (janvier 2024).
- **Loi 18-07 modifiée par la loi 25-11 (24 juillet 2025)** : protection des données personnelles ; DPO déclaré à l'ANPDP, registre des traitements et journal automatisé, notion de violation de données ; **transfert vers l'étranger soumis en principe à l'autorisation préalable de l'ANPDP**.
- **Conséquence** : Vercel (aucune région en Algérie, transferts vers les États-Unis possibles) n'est pas adapté pour héberger la boutique ou des données personnelles de clients algériens sans validation juridique. Tout usage doit être limité, justifié et autorisé.
- Statut : « à valider par un juriste » (pôle juridique-conformite), décision tracée en ADR avec alternatives.

## 11. Montages possibles pour un client algérien

1. **Hébergement en Algérie de bout en bout** (recommandé par défaut pour un site marchand) : hébergeur ou cloud situé en Algérie (offres d'hébergeurs et datacenters locaux, à identifier et comparer : disponibilité, SLA, sauvegardes, support) ; application Next.js en mode `standalone` dans un conteneur, derrière un reverse proxy ; base et fichiers en Algérie ; CDN éventuel uniquement pour des ressources statiques sans donnée personnelle, si validé.
2. **Vitrine sans donnée personnelle** (pas de vente, pas de formulaire collectant des données, ou formulaire relayé vers un service en Algérie) : Vercel possible si le juriste confirme ; analytics sans cookie ni donnée personnelle.
3. **Préproduction et prévisualisations** sur Vercel avec **données fictives uniquement**, production en Algérie : bénéficie du flux de travail Vercel sans exporter de données réelles.
4. **Client aussi visant la France/UE** : séparer les instances (Algérie / UE) si les deux régimes l'exigent.
Dans tous les cas : pas de traceurs tiers sans consentement, journaux sans données personnelles, portabilité (éviter les fonctions propriétaires non transposables : préférer les fonctionnalités standard de Next.js qui tournent aussi en `next start`).

## 12. Alternatives

| Besoin | Options |
|---|---|
| Hébergement en Algérie | hébergeurs et datacenters algériens (à comparer), VPS + Docker + Caddy/Nginx, Coolify ou Dokploy pour un « Vercel-like » auto-hébergé |
| UE, souveraineté | Scaleway, OVHcloud, Clever Cloud, Hetzner (Next.js en conteneur ou via OpenNext) |
| Plateformes équivalentes | Netlify, Cloudflare Workers/Pages (OpenNext), Render, Railway, Fly.io |
Next.js s'auto-héberge (`output: 'standalone'`, `next start`) ; certaines fonctions (ISR distribué, optimisation d'images, middleware) demandent configuration (cache partagé, `sharp`) : vérifier la documentation d'auto-hébergement de la version.

## 13. Check-list d'audit

- [ ] Nature du projet (commercial ou non) compatible avec l'offre ; jamais de Hobby pour un site commercial.
- [ ] Analyse de localisation des données faite (pays du client, lois 18-05 et 18-07/25-11 pour l'Algérie, RGPD pour l'UE), validée par le juriste, tracée en ADR.
- [ ] Région des fonctions alignée sur la base de données ; services de données et leurs régions inventoriés.
- [ ] Prévisualisations protégées ; données fictives hors production.
- [ ] Secrets en variables sensibles, aucun secret côté client.
- [ ] WAF, limitation de débit, en-têtes de sécurité configurés.
- [ ] Journaux sans données personnelles ; drains pour la conservation requise.
- [ ] Plafond de dépenses et alertes actifs ; estimation de coût sur 3 scénarios (pôle finance).
- [ ] Plan de sortie : application exécutable hors Vercel (conteneur `standalone`).

## 14. Anti-patterns et pièges

- Héberger une boutique algérienne sur Vercel sans analyse juridique ; croire qu'une région « Europe » règle la question algérienne.
- Laisser les fonctions en région par défaut (États-Unis) avec une base en Europe : latence doublée à chaque requête.
- Site d'entreprise en Hobby (contraire aux conditions, blocage au dépassement).
- SSR non caché sur toutes les pages : facture de CPU actif.
- Prévisualisations publiques avec données réelles.
- `NEXT_PUBLIC_` sur une clé secrète.
- Dépendre de fonctions propriétaires sans plan de sortie.
- Annoncer un prix sans vérifier la page tarifs du jour.

## 15. Sources

Consultées le 2026-11-03.
- Vercel, Hobby plan (miroir officiel) : https://examples.vercel.com/docs/plans/hobby
- Vercel, Compliance (miroir officiel) : https://examples.vercel.com/docs/security/compliance
- Vercel, Configuring regions : https://vercel.com/docs/functions/configuring-functions/region
- Vercel, Data Processing Addendum : https://vercel.com/legal/dpa
- Fencode, Vercel Free vs Pro 2026 (source secondaire) : https://www.fencode.dev/en/blog/vercel-free-vs-pro-2026-official-limits-pricing
- Gide, Algérie – loi 25-11 modifiant la loi 18-07 : https://www.gide.com/en/?p=93297
- Ministère du Commerce (Algérie), loi relative au commerce électronique : https://commerce.gov.dz/fr/actualites/la-loi-relative-au-commerce-electronique-fixant-les-regles-generales-du-commerce-electronique-des-biens-et-des-services
- AlgeriaTech, exigences de la loi 18-05 (source secondaire) : https://algeriatech.news/?p=24880
