# Analyse du contexte : politique, économique, social, culturel, technologique, environnemental, légal

Ce fichier guide `analyste-contexte`. Livrable : `01-decouverte/analyse-contexte.md`. Le but n'est pas un tableau de généralités mais, pour chaque marché visé, la liste des facteurs qui changent une décision de produit, de prix, de calendrier ou de marché.

## Sommaire
1. Méthode
2. Questions par facteur
3. Adaptation culturelle
4. Où chercher
5. Gabarit
6. Pièges et contrôles
7. Sources

## 1. Méthode

1. Lister les **marchés visés** (pays, et région si pertinent) et le secteur. Un tableau de facteurs par marché, jamais un tableau unique pour « l'international ».
2. Pour chaque facteur, ne retenir que ce qui a un **effet décisionnel** : il modifie une exigence, un prix, un canal, un calendrier, un choix de marché ou un risque. Les autres sont écartés.
3. Dater chaque fait et noter son **échéance** : une règle qui entre en vigueur dans l'année est plus décisive qu'un contexte stable.
4. Donner à chaque facteur : sens (menace, opportunité, neutre), certitude (fait daté, probable, spéculatif), effet, action proposée, destinataire (`juriste-numerique`, `controleur-financier`, `redacteur-contenu-localisation`, `stratege-produit`).
5. Le légal est un **repérage** : renvoyer au `juriste-numerique` (`01-decouverte/prediagnostic-juridique.md`) sans trancher, avec « à valider ».
6. Classer en fin de document les facteurs en trois : bloquants (peuvent faire renoncer ou changer de marché), structurants (changent le périmètre ou le prix), à surveiller.

## 2. Questions par facteur

| Facteur | Questions à se poser pour chaque marché visé |
|---|---|
| Politique et géopolitique | Stabilité du pays et de l'administration ? Sanctions, embargos, restrictions d'export ou de transfert de données ? Souveraineté numérique, localisation obligatoire des données, préférence nationale dans les marchés publics ? Élections ou réformes prévues dans l'horizon ? Rapports du pays avec la plateforme ou le fournisseur dont le produit dépend ? Censure ou coupures d'internet ? |
| Économique | Pouvoir d'achat et inflation ? Monnaie, change, convertibilité, transferts de fonds ? Taxation (TVA, droits de douane, taxe sur les services numériques) ? Moyens de paiement dominants et accès bancaire ? Coûts de main-d'œuvre, d'hébergement, d'acquisition ? Cycle économique du secteur, taux, accès au financement ? |
| Social | Démographie et part de la cible ? Équipement (appareil d'entrée de gamme, forfait de données), connectivité, illectronisme ? Habitudes d'achat et de confiance (paiement à la livraison, achat sur facture) ? Évolution des attentes (vie privée, durabilité, inclusion) ? |
| Culturel | Langues et variantes, sens de lecture, formats de dates, nombres, adresses, noms ? Normes de communication (formel ou direct), symboles, couleurs, humour ? Jours fériés, saisonnalité, rythmes d'achat ? Références culturelles qui ne voyagent pas ? |
| Technologique | Infrastructures disponibles, réseaux, cloud local ? Dépendance à des plateformes (stores, API, passerelles) et à leurs changements de règles ? Maturité de l'IA, de l'identité numérique, des paiements instantanés ? Normes d'interopérabilité imposées ? |
| Environnemental | Obligations d'écoconception ou de déclaration ? Exigences d'acheteurs sur l'empreinte numérique ? Intensité carbone de l'hébergement visé ? Attentes de durabilité de la clientèle ? |
| Légal | Activité réglementée, agrément, licence ? Protection des données et transferts ? Consommation (rétractation, affichage du prix, abonnements) ? Propriété intellectuelle, fiscalité de la vente à distance, facturation électronique ? Obligations d'accessibilité ? Calendrier d'entrée en vigueur des textes à venir ? |

## 3. Adaptation culturelle

Les dimensions culturelles de type Hofstede sont des **hypothèses à valider** par recherche locale, jamais des stéréotypes ; couleurs et symboles n'ont pas de sens universel. Avant de figer une direction pour un marché, prévoir la validation auprès d'au moins 5 utilisateurs locaux (`maquettes-parcours/references/contenu-localisation-culture.md`). Noter pour le `redacteur-contenu-localisation` : langues et variantes, RTL (`lang`, `dir`, propriétés CSS logiques), formats via CLDR et `Intl` plutôt que codés en dur, champ « nom complet » plutôt que prénom et nom.

Paiements, à vérifier au moment du projet (sources secondaires, mars 2026) : cartes 71 % et PayPal 57 % en France, iDEAL 66 % aux Pays-Bas, PayPal 67 % et achat sur facture 40 % en Allemagne, Bancontact 73 % en Belgique ; en Algérie, paiement à la livraison encore dominant, carte CIB et Edahabia cités par des sources commerciales ou faibles ; Maroc et Tunisie : non trouvés.

## 4. Où chercher

Textes officiels du pays (journal officiel, régulateurs), autorités statistiques, banques centrales, organismes de commerce, publications des plateformes dont le produit dépend, cabinets d'avocats pour les synthèses (étiquetées secondaires), rapports d'éco-conception. Préférer la source primaire ; quand seule une source secondaire est lue, l'écrire. Pour les données statistiques précises (INSEE, Eurostat, Banque de France), aucune source n'est vérifiée : à rechercher et à dater.

Exemples de faits datés à instruire (secondaires, à vérifier) : fonction de rétractation obligatoire en vente à distance française depuis le 19 juin 2026 ; fin de l'exonération de droits des envois de 150 € ou moins dans l'UE avec 3 € par article dès le 1er juillet 2026 ; facturation électronique en France dès le 1er septembre 2026 (réception pour toutes, émission selon la taille) ; Digital Fairness Act attendu au quatrième trimestre 2026 ; article 25 du DSA sur les interfaces trompeuses.

## 5. Gabarit

````markdown
# Analyse du contexte — <projet>

## Synthèse
<12 lignes : marchés analysés ; 3 facteurs bloquants ; 3 structurants ; échéances datées dans les 24 mois ; conséquence sur le choix des marchés ; points renvoyés au juriste et au contrôleur financier>

## Marchés et secteur analysés
## Facteurs
| ID | Marché | Facteur (P, E, S, C, T, En, L) | Fait daté et source | Échéance | Sens | Certitude | Effet décisionnel | Action et destinataire |
|---|---|---|---|---|---|---|---|---|
| FAC-01 | | | | | | | | |
## Adaptation culturelle par marché
## Comparaison des marchés
## Facteurs bloquants, structurants, à surveiller
## Non trouvé et à valider
````

## 6. Pièges et contrôles

- PESTEL générique recopié sans effet décisionnel ; marchés mélangés ; facteurs sans échéance.
- Stéréotype culturel présenté comme fait ; traduction prise pour adaptation.
- Synthèse d'un cabinet citée comme texte de loi ; réglementation de la France appliquée aux autres pays.
- Contrôles avant de rendre : un tableau par marché ; chaque `FAC-` a source et date ; chaque facteur légal est marqué « à valider » ; échéances des 24 mois listées ; facteurs bloquants distingués.

## Sources

- Commission européenne, lignes directrices sur la protection des mineurs (DSA art. 28), 14 juillet 2025 : https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors
- DSA, article 25 : https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html
- Parlement européen, Digital Fairness Act (suivi législatif) : https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act
- Unicode CLDR 47 (mars 2025) : http://blog.unicode.org/2025/03/unicode-cldr-47-release-messageformat-2.html
- RGESN 2024 : https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/
- Paiements en Europe (secondaire) : https://scandiweb.com/blog/ecommerce-review-popular-payment-methods-2022/
- PESTEL et Hofstede : aucune source primaire retrouvée (état : octobre 2026) ; compléments juridique et financier : à vérifier.
