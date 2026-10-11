# Acquisition par type de projet

Cette référence aide à choisir les canaux selon le type de projet, à les configurer correctement et à mesurer leurs résultats sans enfreindre le consentement. État des règles : octobre 2026, France et UE d'abord.

## Sommaire
1. Canaux prioritaires par type
2. Référencement classique et réponses IA
3. Stores d'applications
4. Publicité
5. E-mail et prospection
6. Partenariats
7. Plan de marquage et mesure
8. Pièges et contrôles

## 1. Canaux prioritaires par type

Synthèse de travail (inférence, à ajuster au marché et aux données du benchmark).

| Type de projet | Canaux prioritaires | Indicateurs clés |
|---|---|---|
| Site d'entreprise | référencement et contenus d'expertise, LinkedIn et ciblage de comptes léger, e-mail B2B encadré, partenariats | prospects qualifiés et coût par prospect qualifié ; conversion formulaire ou démo ; trafic organique ; impressions et clics du rapport « Web » de Search Console |
| Application mobile | optimisation de fiche (ASO), Apple Ads, campagnes d'applications Google, influence, relance après valeur démontrée | conversion de la fiche ; coût par installation et CAC ; rétention J1, J7, J30 ; LTV et revenu moyen par utilisateur |
| SaaS | produit (essai ou gratuité), référencement et comparatifs, places de marché d'intégrations, prospection B2B ciblée, communauté | activation ; essai vers payant ; rétention nette et churn ; payback CAC sous 12 mois ; LTV:CAC supérieur à 3 |
| Produit de niche | communauté propre, construction en public, prescripteurs, référencement longue traîne, places de marché spécialisées | croissance et engagement de la communauté ; « très déçus » au moins 40 % ; coût par client |
| E-commerce | référencement produit et Merchant Center, Search et Shopping, publicité sociale, e-mail et relance de paniers, places de marché, affiliation | conversion ; abandon de panier (~70 % en moyenne) ; panier moyen ; CAC, ROAS et marge après publicité ; réachat |
| ERP, grand compte | marketing de comptes et vente directe, intégrateurs et revendeurs, références, événements, appels d'offres | couverture du comité d'achat ; pipeline par étape ; durée du cycle ; taux de gain ; références actives |

Règle : au plus trois canaux prioritaires au lancement, chacun avec budget test, indicateur et seuil de coupure.

## 2. Référencement classique et réponses IA

Google indique (Search Central, mise à jour du 10 décembre 2025) qu'aucune exigence technique supplémentaire ne conditionne l'apparition dans les aperçus IA et le mode IA : la page doit être indexée et éligible à un extrait. Il n'existe donc pas d'« astuce » spécifique.

| Action | Pourquoi |
|---|---|
| Autoriser Googlebot dans robots.txt et au niveau du CDN ; autoriser OAI-SearchBot | bloquer OAI-SearchBot retire le site des réponses de ChatGPT search (OpenAI) |
| Vérifier qu'aucun `nosnippet`, `max-snippet` restrictif ou `noindex` ne frappe les pages à promouvoir | ces contrôles limitent l'extrait et la citation |
| Contenu textuel, maillage interne, données structurées cohérentes avec le texte visible | fondamentaux du référencement |
| Pages de preuve : cas clients, comparatifs, FAQ en texte | répondent aux questions décomposées par le moteur (« query fan-out ») |
| Merchant Center et Business Profile à jour | e-commerce et activité locale |

Piloter autrement qu'au clic : aux États-Unis, en mars 2025, un clic sur un lien classique survient dans 8 % des visites avec résumé IA contre 15 % sans (Pew). Suivre impressions, citations, conversions. Le trafic IA de Google est compté dans le rapport « Web » de Search Console. La valeur de `llms.txt` n'est pas établie : à vérifier avant de le recommander.

## 3. Stores d'applications

| Plateforme | Leviers | Limite à connaître |
|---|---|---|
| Apple | jusqu'à 70 pages produit personnalisées ; tests d'optimisation avec jusqu'à 3 variantes ; rétention mesurable par page | les pages passent la revue : les soumettre à temps |
| Google Play | jusqu'à 50 fiches personnalisées (pays, mot-clé, campagne) ; expériences A/B | idem, délai de publication |

Apple annonce environ 2,5 points de conversion en plus pour les pages personnalisées (page par défaut : 1,6 %), chiffre de l'éditeur. Prévoir une fiche par défaut, au moins trois fiches personnalisées par audience et un test planifié. Mesurer la rétention par fiche, pas seulement l'installation.

## 4. Publicité

- Budget test d'abord, par canal, avec suivi de conversion validé avant la première dépense.
- Calculer le CAC admissible : (marge brute annuelle × durée de vie) / 3, avec payback sous 12 mois. En e-commerce, piloter la marge après remise et publicité, pas le seul ROAS.
- Publicité dans les réponses IA : ChatGPT Ads est en test hors de France (États-Unis, puis Royaume-Uni, Mexique, Brésil, Japon, Corée du Sud) ; Google déploie des formats dans le mode IA. Disponibilité France : à vérifier.
- L'utilisateur déclenche la dépense.

## 5. E-mail et prospection

| Canal | Règle (France, octobre 2026) |
|---|---|
| E-mail, SMS, MMS, automate d'appel, particuliers | consentement préalable |
| E-mail, SMS professionnels | information et droit d'opposition (CNIL) |
| Téléphone, consommateurs | consentement préalable depuis le 11 août 2026 ; consentement de moins d'un an, preuves conservées au moins trois ans ; plages horaires encadrées (DGCCRF, résumé à confirmer) |
| Cession de contacts par un partenaire | consentement recueilli par l'organisme lui-même, liste des partenaires à jour |

Authentification : SPF ou DKIM pour tous, SPF, DKIM et DMARC pour les gros volumes, désabonnement en un clic (RFC 8058), demandes traitées sous 48 h (Gmail). Spam déclaré au-dessus de 0,1 % pénalisant, au-dessus de 0,3 % sans remédiation possible. Lisser les pics d'envoi (Yahoo). Chaque envoi passe une grille : canal, B2C ou B2B, base légale, preuve, désinscription. Aucune liste achetée. Application B2B de la règle téléphonique : à vérifier.

## 6. Partenariats

Types : intégrateurs et revendeurs (ERP), places de marché d'intégrations (SaaS), affiliation (e-commerce), prescripteurs (niche), influence. Fixer par partenaire objectif, rémunération, exclusivité, données échangées. Influence : mention claire « publicité » ou « collaboration commerciale », contrat écrit (nullité à défaut au-delà des seuils du guide de janvier 2026), responsabilité commune annonceur et influenceur, représentant légal dans l'UE pour un influenceur hors UE. Contrats à valider par le juriste.

## 7. Plan de marquage et mesure

1. Un événement par étape (acquisition, activation, rétention, revenu, recommandation) plus la métrique de référence ; dictionnaire de données (nom, propriétés, déclencheur) ; recette avant J-30.
2. Choisir l'outil et documenter la décision : Google Analytics 4 avec consentement, ou outil de mesure d'audience exempté. L'exemption CNIL suppose une finalité limitée à l'audience de l'éditeur, des statistiques anonymes, aucun recoupement ni suivi inter-sites ; interdit de se dire « certifié CNIL ».
3. Consent Mode v2 pour les produits Google dans l'EEE : paramètres `ad_user_data` et `ad_personalization`, testés en accepté et en refusé.
4. L'exemption n'autorise pas les audiences publicitaires : prévoir une pile consentie séparée pour la publicité.
5. Balisage serveur possible via Tag Manager : déployer ou justifier son absence.
6. Tableau de bord hebdomadaire : volume et coût par canal, activation, rétention, CAC et payback, métrique de référence, satisfaction.

Digital Omnibus : non adopté (état au 9 octobre 2026). Ne pas planifier sur des règles assouplies.

## 8. Pièges et contrôles

- Consent Mode jamais testé en refusé : mesure et reciblage perdus dans l'EEE.
- Avant de rendre : tableau type-canal-indicateur complet, seuils de coupure chiffrés, grille de prospection relue, recette des balises planifiée.

## Sources

- Google Search Central, fonctionnalités IA dans la recherche (mise à jour du 10/12/2025)
- Pew Research, 22/07/2025, clics et résumés IA
- OpenAI, documentation des robots (OAI-SearchBot)
- Gmail et Yahoo, exigences des expéditeurs ; RFC 8058
- Apple, pages produit personnalisées ; Google Play Console, fiches personnalisées
- CNIL, outils de mesure d'audience exemptés (juillet 2025) ; prospection par voie électronique
- DGCCRF, démarchage téléphonique (fiche à confirmer)
- Guide de l'influence commerciale, janvier 2026
