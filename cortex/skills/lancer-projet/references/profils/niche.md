# Profil — produit ou micro-SaaS de niche (type `niche`)

Lu par le chef d'orchestre à J0 pour qualifier le projet et composer une équipe minimale. État : octobre 2026.

## Ce qui distingue ce type de projet

- Le risque est commercial, pas technique : personne ne paie. Sur plus de 1 000 produits, environ 70 % restent sous 1 000 $ de revenu mensuel récurrent (MRR) ; médiane des rentables vers 4,2 k$ (Freemius, source secondaire ; le même article contient une affirmation contradictoire, biais de survie probable).
- Environ la moitié des SaaS indépendants sont portés par une seule personne.
- Mode Cortex recommandé : `eclair`, avec rôles fusionnés. Un grand arsenal documentaire est contre-productif ici.

## Étiquettes à poser

Peu : `b2b`, `abonnement`, `paiement`, `comptes`, `donnees-perso`, `code` ; `international` si vente à l'étranger ; `integrations` s'il dépend d'une plateforme tierce ; `ia` le cas échéant. Mieux vaut une étiquette de trop qu'un contrôle oublié, mais ne pas gonfler la matrice.

## Acheter, configurer ou construire

| Choix | Position |
|---|---|
| Valider avant de coder | pré-vente, lettre d'intention, démarrage « à la main » |
| Pile minimale (déduction) | framework full-stack, Postgres managé, prestataire de paiement ou MoR, e-mail transactionnel |
| No-code | pour valider, pas pour porter durablement l'authentification et la facturation |
| Paiement | prestataire de paiement ou MoR choisi avant le premier client étranger |

Critères : coûts fixes mensuels plafonnés, aucune dépendance critique à une plateforme sans plan B (Drift et Gainsight ont perdu l'accès à Salesforce AppExchange fin 2025, billet anecdotique). Délai au premier revenu, coûts types, panorama no-code, effet de l'IA sur la saturation : non établis, **à vérifier**.

## Prérequis propres à ce type

1. Cible B2B précise ; entretiens clients menés, seuil fixé d'avance (exemple : dix).
2. Au moins un pré-paiement ou une lettre d'intention avant la première ligne de code.
3. Concurrents recensés et lus comme preuve de marché : l'absence de concurrence est un signal d'alerte.
4. Un canal d'acquisition testé avec un objectif chiffré.
5. Seuil d'arrêt fixé d'avance (MRR, churn, activation suivis chaque semaine).

## Agents à renforcer et livrables spécifiques

- `analyste-concurrence` (fusionné avec marché et voix du client) et `stratege-produit` : cœur de J1.
- `expert-cahier-des-charges` : MVP limité à un flux de valeur ; `architecte-solution` (fusionné) ; `developpeur-backend` ou `developpeur-frontend`.
- `juriste-numerique` : conditions et données personnelles de base ; `controleur-financier` : coût fixe, seuil de rentabilité.
- Livrables : note d'opportunité avec preuves d'engagement, MVP décrit en une page, tableau des indicateurs hebdomadaires.

## Exigences des plateformes et des tiers

- Plateforme d'accueil (place de marché, API tierce) : conditions et risque de retrait à lire avant de bâtir dessus.
- Paiement : voir profil `saas` pour prestataire contre marchand d'enregistrement (taxes : **à valider**).
- Aucune autre exigence établie.

## Pièges et causes d'échec fréquentes

- Construire avant de vendre ; mesurer la validation par des inscriptions plutôt que par des engagements.
- Viser le grand public ou une niche « fun » qui paie peu.
- Dépendre d'une plateforme sans plan B.
- Croire aux chiffres de rentabilité optimistes.
- Surdimensionner : un MVP avec administration, multi-tenant et API publique.

## Planning type

Aucune durée type établie. Séquence : entretiens et pré-vente → MVP d'un flux de valeur avec paiement réel (livré en semaines : hypothèse) → premiers clients → test d'un canal → revue au seuil d'arrêt fixé. Le jalon de décision pivot ou arrêt est le principal du plan.

## Sources

- Freemius, « State of micro-SaaS 2025 » (secondaire) ; MicroConf, non lu.
- Indie Hackers, « The SaaS graveyard is paved with cool ideas » (anecdotique).
- Notes `specificites_par_type_de_projet.md`, §5, état au 11 octobre 2026.
