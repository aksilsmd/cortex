# Formation — DatoCMS pour piloter bandeaux, annonces et promotions (et alternatives)

Fiche de formation pour architecte solution, développeur front-end, rédacteur contenu et localisation, responsable support et formation. Elle complète `formation-architectures-web-mobile.md` (rendu, cache), `formation-vercel.md` (localisation des données, cas algérien) et `contenu-localisation-culture.md` du pôle maquettes. Sources en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/datocms.md`. « dato csm » (terme du PO) = **DatoCMS**.

**Cas d'usage visé** : afficher sur un site SSR (ex. parapharmacie Parapro, Azazga) des **bandeaux et messages paramétrés depuis un back-office** : promotions, annonces, bandeau d'information, carrousel d'accueil, en FR/AR/EN, avec période de diffusion, pages ciblées, ordre et statut.

**Rappels obligatoires**
- **Publicité des produits de santé** : encadrée (médicaments en particulier ; produits de parapharmacie, allégations de santé, promotions sur des produits soumis à prescription). Tout contenu promotionnel est **à valider par un juriste selon le droit algérien** avant publication ; prévoir un circuit de validation.
- **Aucun traceur tiers** introduit par les bandeaux : pas de pixel, script ou iframe externe dans le contenu ; images servies sans cookie ; mesures de clic par l'analytics du site (consentement respecté).
- **Localisation des données** : DatoCMS est un SaaS hébergé hors d'Algérie (localisation exacte à vérifier dans son DPA). Le contenu des bandeaux n'est en principe pas une donnée personnelle, mais les comptes des éditeurs le sont, et l'hébergement du site marchand est soumis à la loi 18-05 : **à valider par le juriste** (voir `formation-vercel.md` §10).

## Sommaire
1. Objectifs
2. DatoCMS en bref
3. Modéliser bandeaux, annonces, promotions, carrousel
4. Localisation FR/AR/EN et RTL
5. Médias et images
6. Planification, statut, prévisualisation, validation
7. API et intégration à un site SSR
8. Cache, revalidation par webhook, repli si le CMS est indisponible
9. Environnements et migrations
10. Rôles et sécurité
11. Coûts réels pour ce volume
12. Comparaison : DatoCMS, module natif, CMS libres auto-hébergés
13. Recommandation pour le cas Parapro
14. Check-list d'audit
15. Anti-patterns et pièges
16. Sources

## 1. Objectifs

L'agent sait :
- modéliser des contenus de bandeau/annonce/promo complets et contrôlés ;
- gérer langues, RTL, médias, planification et prévisualisation ;
- intégrer le contenu à un site SSR avec cache, revalidation et repli ;
- chiffrer le coût réel et comparer avec un module natif et des CMS libres ;
- rappeler les contraintes juridiques (publicité santé, traceurs, localisation).

## 2. DatoCMS en bref

- CMS **headless SaaS** (éditeur italien) : modèles de contenu, éditeur pour non-techniciens, API **GraphQL Content Delivery (CDA)** en lecture via CDN, **Content Management API (CMA)** REST pour écrire et administrer, médias avec transformation d'images (imgix), localisation, **blocs modulaires**, **environnements sandbox** et migrations scriptées, webhooks, publication planifiée, prévisualisation, serveur MCP.
- SDK : `@datocms/cda-client`, `@datocms/cma-client-node`, `react-datocms` (images responsives, texte structuré), CLI `@datocms/cli` (migrations).

## 3. Modéliser bandeaux, annonces, promotions, carrousel

Modèle **`bandeau`** (collection) — champs :

| Champ | Type DatoCMS | Validation |
|---|---|---|
| `titre_interne` | texte court | requis, unique (identifiant éditorial, non affiché) |
| `type` | énumération (texte court + valeurs prédéfinies) | `info`, `promo`, `annonce`, `alerte` |
| `message` | texte court ou **texte structuré** (gras, lien) **localisé** | requis dans la langue par défaut ; longueur ≤ 120 caractères (bandeau) |
| `texte_bouton` | texte court localisé | ≤ 25 caractères |
| `lien` | lien vers enregistrement (page, produit) ou URL | URL interne de préférence ; externe : `rel="noopener"` |
| `image` | fichier unique (image) | formats JPEG/PNG/WebP/SVG, poids max, **texte alternatif requis** (localisé) |
| `image_mobile` | fichier unique | facultatif, ratio dédié |
| `debut_diffusion`, `fin_diffusion` | date et heure | fin > début ; fuseau Africa/Algiers documenté |
| `pages_ciblees` | liens multiples vers `page` ou énumération (`accueil`, `catalogue`, `fiche-produit`, `panier`, `toutes`) | au moins une |
| `ordre` | entier ou tri manuel de la collection | 1–99 |
| `priorite` | énumération | `normale`, `haute` (alerte) |
| `fermable` | booléen | si vrai, mémoriser la fermeture côté client (localStorage, sans traceur) |
| `couleur` | énumération de jetons du design (`marque`, `succes`, `avertissement`) | pas de couleur libre (contraste garanti) |
| `validation_juridique` | booléen + note | requis pour `promo` (case cochée par le validateur) |
- **Statut** : activer **brouillon/publié** sur le modèle ; seuls les enregistrements publiés **et** dans leur période sont affichés.
- **Carrousel d'accueil** : modèle singleton `accueil` avec un champ **blocs modulaires** `diapositives` (bloc `diapositive` : image desktop/mobile, titre, sous-titre, bouton, lien, alt) — ordre par glisser-déposer, 3 à 5 diapositives maximum (au-delà, personne ne les voit), défilement automatique **désactivé par défaut** ou avec bouton pause (WCAG 2.2.2).
- **Promotion** : soit un type de bandeau, soit un modèle `promotion` (code, remise, produits liés) — mais **le prix et la remise réels restent dans le système de commande** (source de vérité) ; le CMS n'affiche qu'un message, jamais un prix appliqué.

## 4. Localisation FR/AR/EN et RTL

- Déclarer les locales du projet (`fr`, `ar`, `en` ; 5 incluses) ; champs **localisés** pour message, bouton, alt, image si visuel avec texte.
- Règle de repli : afficher le bandeau seulement s'il a une traduction dans la langue de la page (ou repli explicite sur la langue par défaut, choisi et documenté).
- RTL : le site pose `dir="rtl"` pour `ar` ; le bandeau utilise des propriétés logiques (`padding-inline-start`), icônes de direction inversées ; éviter le texte incrusté dans les images (non traduisible, non accessible) ; prévoir images miroir si la composition est directionnelle.
- Arabe : longueur et typographie différentes (police arabe adaptée), chiffres (arabes occidentaux ou orientaux : choix éditorial), dates localisées.
- Rôles par locale (traducteur arabe ne modifiant que `ar`) : **Enterprise uniquement**.

## 5. Médias et images

- Médiathèque avec métadonnées (alt, titre, focal point) ; dossiers et tags.
- Transformation d'images à la volée via paramètres d'URL (imgix) : `?auto=format&w=1200&fit=crop&crop=focalpoint` ; `react-datocms` `<Image>` génère `srcset`, placeholder flou et dimensions (pas de CLS).
- LCP : l'image du carrousel d'accueil est souvent l'élément LCP → `priority`/`fetchpriority="high"`, taille adaptée, AVIF/WebP.
- Les images sont servies depuis le CDN de DatoCMS (hors Algérie) : vérifier l'absence de cookie et la conformité ; alternative : copier les images vers le stockage du site lors de la revalidation.
- Droits d'usage des visuels (photos de produits, marques) à vérifier.

## 6. Planification, statut, prévisualisation, validation

- **Publication/dépublication planifiées** natives (toutes offres) : programmer la mise en ligne et le retrait d'un enregistrement ; doubler par les champs `debut_diffusion`/`fin_diffusion` filtrés à la requête pour un retrait garanti même si le cache tarde.
- **Prévisualisation** : endpoint de brouillons de la CDA (en-tête d'inclusion des brouillons, jeton en lecture seule dédié) + mode brouillon du framework (Next.js Draft Mode) ; plugin **Web Previews** pour ouvrir l'aperçu depuis l'éditeur ; édition visuelle (Content Link) selon configuration.
- **Validation** : workflows éditoriaux natifs (étapes « à relire » → « validé ») **réservés à Enterprise** ; sur Free/Professional, organiser la validation par rôles (rédacteur sans droit de publier, validateur qui publie) + champ `validation_juridique` requis pour les promotions + historique des versions (3 j Free, 60 j Professional).
- Validations de champs (requis, longueur, format, unicité, plages de dates) pour empêcher un bandeau incomplet.

## 7. API et intégration à un site SSR

Requête GraphQL (CDA) :
```graphql
query Bandeaux($locale: SiteLocale!, $maintenant: DateTime!) {
  allBandeaux(
    locale: $locale
    filter: { debutDiffusion: { lte: $maintenant }, finDiffusion: { gt: $maintenant } }
    orderBy: ordre_ASC
    first: 10
  ) {
    id type message texteBouton lien couleur fermable pagesCiblees
    image { responsiveImage(imgixParams: { auto: format, w: 1200 }) { src srcSet width height alt } }
  }
}
```
- Appel **côté serveur uniquement** (jeton CDA en lecture seule, variable d'environnement, jamais exposé au navigateur) ; filtrage par page côté serveur ; sortie validée par un schéma (Zod) avant rendu.
- Rendu : texte échappé, texte structuré rendu par le composant officiel (pas de HTML brut injecté) ; liens externes contrôlés (liste d'autorisation de domaines).
- CMA (écriture) : uniquement pour scripts de migration ou d'import, jeton à droits limités, jamais dans le site.

## 8. Cache, revalidation par webhook, repli si le CMS est indisponible

- **Cache** : résultats mis en cache côté serveur (Next.js `use cache` / cache de données avec étiquette `bandeaux`), TTL de sécurité court (ex. 5–15 min) pour respecter les fins de diffusion même sans webhook.
- **Revalidation par webhook** : webhook DatoCMS (publication, dépublication, suppression sur le modèle `bandeau`, ou webhook de **cache tags**) → route du site `POST /api/revalidate` qui **vérifie un secret** (en-tête signé ou authentification basique), puis invalide l'étiquette. Webhooks : IP statiques seulement en Enterprise → authentifier par secret.
- **Repli si DatoCMS est indisponible ou lent** :
  - délai court sur l'appel (≤ 1–2 s) ; en cas d'échec, servir la **dernière version en cache** (stale-if-error) ;
  - sinon, **aucun bandeau** (la page s'affiche normalement) ou un bandeau de secours statique versionné dans le code ;
  - jamais d'erreur 500 ou de page bloquée à cause d'un bandeau ;
  - alerte (journal/monitoring) si échecs répétés.
- Les appels CDA restent très bas avec ce schéma (quelques milliers par mois), bien sous les quotas.

## 9. Environnements et migrations

- Environnement principal + **sandboxes** (3 incluses) : tester une évolution de modèle (nouveau champ) dans une sandbox, puis la promouvoir.
- **Migrations scriptées** (CLI `datocms migrations:new`, scripts TypeScript via CMA) versionnées dans le dépôt : le modèle est reproductible.
- Le site cible l'environnement via l'en-tête/URL d'environnement ; préproduction sur sandbox, production sur principal.

## 10. Rôles et sécurité

- Rôles : **rédacteur** (crée/modifie des brouillons de bandeaux), **validateur** (publie), **administrateur** (modèles, jetons) ; collaborateurs limités par l'offre (1 en Free, 10 en Professional).
- MFA pour tous les comptes éditeurs ; SSO et journaux d'audit en Enterprise seulement.
- Jetons d'API : un jeton CDA en lecture seule pour la production, un pour la prévisualisation (brouillons), un CMA pour les migrations ; rotation et stockage en coffre.
- Contenu = donnée non fiable : échappement, liste d'autorisation de liens, pas d'iframe ni de script.

## 11. Coûts réels pour ce volume

Volume type Parapro : 5 à 30 bandeaux/promotions actifs ou archivés par an, 1 carrousel, 3 langues, 2–3 éditeurs, trafic modéré.
| Poste | Free | Professional |
|---|---|---|
| Abonnement | 0 € | 149 €/mois en annuel (≈ 1 788 €/an) ou 199 €/mois |
| Enregistrements (300 max en Free) | suffisant si archivage/suppression régulière | largement suffisant |
| Collaborateurs | **1 seul** : bloquant pour séparer rédacteur et validateur | 10 |
| Appels CDA avec cache + webhook | quelques milliers/mois ≪ 100 000 | ≪ 1 M |
| Bande passante images (10 Go Free) | risque si images lourdes servies par DatoCMS à fort trafic ; **en Free, dépassement = service bloqué** | 1 To |
| Workflows de validation | non (Enterprise) | non (Enterprise) |
Lecture : en Free, un seul compte éditeur et un blocage au dépassement ; en Professional, ≈ 1 800 €/an pour quelques bandeaux — coût disproportionné face à un module natif (§12). Prix à revérifier au moment de la décision (changements tarifaires de février 2026).

## 12. Comparaison : DatoCMS, module natif, CMS libres auto-hébergés

| Critère | **DatoCMS** (SaaS) | **(a) Module natif « Bandeaux et messages »** dans le back-office | **(b) CMS libre auto-hébergé** (Strapi, Directus, Payload) |
|---|---|---|---|
| Coût | 0 € (limité) à ≈ 1 800 €/an + options | développement initial (≈ quelques jours : modèle, écran CRUD, prévisualisation, cache) puis maintenance faible | gratuit (licence) + hébergement + exploitation et mises à jour |
| Localisation des données | SaaS hors Algérie (à vérifier) | **même infrastructure que le site (en Algérie)** | sur l'infrastructure choisie (en Algérie possible) |
| Ergonomie éditeur | excellente, médiathèque, planification native | à concevoir (simple : liste, formulaire, dates, aperçu) | bonne, interface d'admin générée |
| Validation / workflow | Enterprise seulement | sur mesure (statut « à valider », rôle validateur, case juridique) | Strapi : relecture/workflows en édition payante (à vérifier) ; Directus : flux et permissions fines ; Payload : brouillons, versions, contrôle d'accès en code |
| Rôles, comptes | collaborateurs limités par offre | réutilise les comptes et rôles du back-office (un seul SSO) | gestion de comptes séparée |
| Intégration au site | API externe, webhook, cache, repli | **lecture directe en base**, pas de dépendance réseau externe, pas de webhook | API (REST/GraphQL) interne ; Payload s'intègre dans l'application Next.js elle-même |
| Disponibilité | dépend du SaaS (repli nécessaire) | dépend du site seulement | dépend d'un service de plus à exploiter |
| Sécurité / conformité | SaaS certifié, peu de contrôle | maîtrisée, aucun tiers | à durcir et mettre à jour (historique de CVE des CMS à surveiller) |
| Évolutivité éditoriale | idéale si le contenu s'étend (pages, blog, landing pages) | limitée au besoin bandeaux/messages | bonne pour un vrai site de contenu |
Points spécifiques des CMS libres :
- **Strapi** (Node, licence MIT pour l'édition communautaire ; fonctions avancées en édition payante) : modèles par interface, i18n, médias, API REST/GraphQL.
- **Directus** (licence BSL 1.1 : gratuit sous un seuil de revenus de l'organisation, à vérifier) : se pose sur une base SQL existante, permissions très fines, flux d'automatisation.
- **Payload** (MIT, TypeScript) : configuration en code, s'installe **dans** l'application Next.js (même base, même déploiement), brouillons, versions, publication planifiée, localisation, contrôle d'accès par fonction.

## 13. Recommandation pour le cas Parapro

1. **Par défaut : module natif « Bandeaux et messages »** dans le back-office existant (ERP/dashboard) — données et comptes en Algérie, aucune dépendance externe, validation juridique intégrée au statut, coût marginal faible, lecture directe en base avec cache applicatif.
   Spécification minimale : table `bandeau` (champs §3, traductions par locale), écran liste/formulaire avec aperçu dans les 3 langues, statuts `brouillon → à valider → publié → expiré`, rôle validateur, journal des modifications, cache invalidé à l'enregistrement.
2. **Si le contenu éditorial doit croître** (pages, blog, landing pages) : **Payload** intégré à l'application Next.js (même hébergement en Algérie), ou Directus/Strapi auto-hébergés.
3. **DatoCMS** seulement si le client accepte un SaaS étranger (validation juridique), veut une ergonomie haut de gamme sans développement, et accepte le coût Professional (Free trop limité : 1 éditeur, blocage au dépassement).
Décision tracée en ADR, avec estimation en trois scénarios (pôle finance).

## 14. Check-list d'audit

- [ ] Modèle de bandeau complet : textes localisés, alt requis, période, pages ciblées, ordre, statut, couleur par jeton, validation juridique pour les promotions.
- [ ] Affichage = publié **et** dans la période ; fin de diffusion garantie même si le cache tarde.
- [ ] Prévisualisation des brouillons protégée, jetons distincts lecture/brouillons/gestion, aucun jeton côté client.
- [ ] Revalidation par webhook authentifiée par secret ; TTL de sécurité ; repli sur cache ou absence de bandeau sans erreur.
- [ ] FR/AR/EN vérifiés, RTL correct, pas de texte incrusté dans les images.
- [ ] Carrousel : ≤ 5 diapositives, pas de défilement automatique sans pause, image LCP optimisée.
- [ ] Aucun traceur tiers ni script/iframe dans le contenu ; liens externes en liste d'autorisation.
- [ ] Publicité santé validée par un juriste (droit algérien) avant publication.
- [ ] Localisation des données et choix SaaS vs natif validés juridiquement ; ADR.
- [ ] Coût annuel calculé sur le volume réel ; limites de l'offre (collaborateurs, blocage Free) connues.

## 15. Anti-patterns et pièges

- Prendre DatoCMS Professional (≈ 1 800 €/an) pour cinq bandeaux, ou le Free avec un seul compte partagé entre plusieurs personnes.
- Stocker le prix ou la remise appliqués dans le CMS (divergence avec la caisse/commande).
- Appeler le CMS depuis le navigateur avec un jeton ; afficher du HTML brut venant du CMS.
- Page qui plante si le CMS ne répond pas ; aucun cache ; aucun TTL (promotion expirée encore affichée).
- Carrousel automatique de 8 diapositives sans pause ; bannières images avec texte incrusté non traduit.
- Bandeau qui insère un pixel publicitaire ou une vidéo externe avec cookies.
- Publier une promotion de produit de santé sans validation juridique.
- Croire que « pas de données personnelles dans les bandeaux » règle seul la question de l'hébergement.

## 16. Sources

Consultées le 2026-11-03.
- DatoCMS, Pricing : https://www.datocms.com/pricing.md
- DatoCMS, Introducing our 2026 pricing changes : https://www.datocms.com/blog/introducing-our-2026-pricing-changes
- DatoCMS Community, annonce 2026 : https://community.datocms.com/t/announcement-2026-professional-plan-pricing-api-limits-changes-for-existing-plans/8512
- DatoCMS, How to manage a live and a preview site : https://www.datocms.com/docs/general-concepts/how-to-manage-a-live-and-a-preview-site.md
- DatoCMS, Content Delivery API : https://www.datocms.com/docs/content-delivery-api/endpoint
- DatoCMS, Overcharges on API and bandwidth : https://www.datocms.com/docs/plans-pricing-and-billing/overcharges-on-api-and-bandwidth
- Openli, DatoCMS privacy (tiers) : https://explore.openli.com/privacy/datocms
- Gide, Algérie – loi 25-11 : https://www.gide.com/en/?p=93297
- W3C, WCAG 2.2 (2.2.2 Pause, arrêt, masquage) : https://www.w3.org/TR/WCAG22/
