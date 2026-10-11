# Commerce en ligne et consommation

Obligations d'information et de loyauté qui s'imposent à un site, une application, un SaaS ou une boutique, par type de projet et de clientèle. État : octobre 2026. Ce livrable prépare le travail d'un avocat et ne vaut pas conseil juridique.

## Sommaire
- Qui est concerné
- Obligations et textes
- Méthode
- Gabarit de matrice
- Pièges
- Sources

## Qui est concerné

| Projet et clientèle | Mentions légales | CGV et précontractuel | Rétractation | Garanties, médiation | Prix, avis, influence |
|---|---|---|---|---|---|
| Site vitrine B2B | oui | non | non | non | avis et influence si utilisés |
| Site vitrine B2C sans vente | oui | non | non | non | oui si promotions ou avis |
| E-commerce B2C | oui | oui | oui | oui | oui |
| SaaS ou application B2C payante | oui | oui | oui, avec exceptions à arbitrer | oui | oui |
| SaaS B2B | oui | CGV B2B et contrat | non (professionnels) | non, sauf petit professionnel à vérifier | rarement |
| ERP, progiciel B2B | oui | contrat | non | non | non |
| Marketplace | oui, pour la plateforme | oui, et information sur la qualité du vendeur (à vérifier) | oui | oui | avis : oui |

## Obligations et textes

| Obligation | Contenu exigé | Texte et sanction (notes, état : octobre 2026) |
|---|---|---|
| Mentions légales | Identité (nom ou dénomination, forme, capital, siège), RCS ou RNE, TVA intracommunautaire, courriel et téléphone, hébergeur (nom, adresse, téléphone), autorité d'autorisation si activité réglementée, directeur de la publication pour un site d'information, droits sur images et textes tiers | Service-Public F23455 ; economie.gouv.fr. Absence : 1 an et 75 000 € (EI), 375 000 € (société) |
| CGV et information précontractuelle B2C à distance | Coordonnées, garanties légales (conformité, vices cachés) et commerciales, médiation, rétractation 14 jours avec formulaire type, frais de renvoi à la charge du consommateur, compatibilité, interopérabilité et fonctionnalités des contenus et services numériques, restrictions d'installation | Service-Public F33527. Amende administrative jusqu'à 3 000 € (personne physique), 15 000 € (personne morale), DGCCRF |
| Fonction de rétractation en ligne | Fonction gratuite « renoncer au contrat ici » ou formule analogue, lisible, avant la fin du délai de 14 jours ; accusé de réception ; remboursement sous 14 jours | Directive (UE) 2023/2673 ; ordonnance n° 2026-2 et décret n° 2026-3 du 5 janvier 2026 ; art. L221-21 (ordonnance art. 3), L221-18, L221-24, D221-5 du Code de la consommation. **Applicable le 19 juin 2026.** Accusé et amende jusqu'à 75 000 € (personne morale) : source secondaire, à confirmer au JORF |
| Résiliation en ligne | Fonction de résiliation des abonnements accessible en ligne | Absence : 15 000 € (EI), 75 000 € (société) (economie.gouv.fr). Article exact : à vérifier |
| Prix de référence | Afficher le prix le plus bas pratiqué sur les 30 jours précédents, en ligne et en magasin | DGCCRF, fiche et actualité du 31/05/2022 ; en vigueur depuis mai 2022. Pratique commerciale trompeuse : 2 ans et 300 000 € |
| Médiation | Médiateur de la consommation désigné et cité dans les CGV ; retirer le lien vers la plateforme européenne de règlement en ligne, fermée le 20/07/2025 | INC / Conseil UE. Article de désignation : à vérifier |
| Influence commerciale | Contrat écrit et mentions « publicité » (articles à vérifier) ; influenceur établi hors UE ciblant la France : représentant dans l'UE et assurance de responsabilité civile européenne | Loi n° 2023-451 du 9 juin 2023 ; ordonnance n° 2024-978 du 6 novembre 2024 (art. 9) |
| Avis en ligne | Informer sur la modération, la source, la date, l'existence d'une contrepartie ; interdiction des faux avis | Textes et normes : à vérifier (voir `penal-responsabilites.md`) |

## Méthode

1. Qualifier : vendeur, plateforme, éditeur ; consommateur ou professionnel ; pays de livraison. Une vente à un consommateur d'un autre État membre peut faire jouer son droit impératif : à vérifier avec l'avocat.
2. Dresser la liste des pages et écrans concernés : fiche produit, panier, bouton final de commande, confirmation, espace client, résiliation, pied de page.
3. Pour chaque obligation du tableau, rédiger une règle de gestion proposée (« le bouton final porte la mention commande avec obligation de paiement ») et la donner au rédacteur de la SFD.
4. Rédiger mentions, CGV et pages selon `documents-juridiques.md`.
5. Faire relire par le marketing (promesses, promotions) et par l'UX (parcours), puis clore les contrôles `JUR-`.

## Gabarit de matrice d'obligations (dans conformite-reglementaire.md)

```markdown
## Obligations commerce et consommation
| ID | Obligation | Texte et date | Écran ou document concerné | Règle proposée | Statut |
|---|---|---|---|---|---|
| JUR-008 | Fonction de rétractation | art. L221-21, applicable 19/06/2026 | confirmation, espace client, application | bouton gratuit avec accusé | à valider |
```

## Points de décision

| Critère | Choix |
|---|---|
| Contenu numérique fourni tout de suite, ou service pleinement exécuté | Exceptions à la rétractation possibles : conditions (consentement exprès, renoncement) à vérifier par l'avocat ; afficher la fonction par défaut |
| Abonnement | Résiliation en ligne aussi simple que la souscription ; rappel avant reconduction (texte à vérifier) |
| Promotion | Historique des prix tenu sur 30 jours par produit, source de l'affichage unique |
| Vente hors France | Mentions et CGV par pays ; Algérie : voir `politique-reglementaire-international.md` |
| Application mobile | Mentions, CGV et fonction de rétractation accessibles dans l'application, pas seulement sur le site |

## Pièges fréquents

- Garder dans les CGV le lien vers la plateforme européenne fermée, ou un ancien formulaire de rétractation.
- Oublier la fonction de rétractation dans l'application mobile et pour les abonnements B2C.
- Compte à rebours, stock fictif, « plus que 2 en stock » faux : pratique trompeuse (2 ans et 300 000 €).
- Case précochée ou refus plus difficile que l'acceptation : voir `cookies-prospection.md`.
- Mentions légales sans hébergeur, ou sans autorité d'autorisation pour une activité réglementée.
- Copier les CGV d'un concurrent : droit d'auteur et clauses inadaptées.
- Se fier à une source secondaire pour un montant d'amende sans le contrôler au JORF.

## Contrôles avant de rendre

- Chaque obligation du tableau est reprise ou écartée avec motif.
- Chaque texte porte sa date d'application ; chaque point non confirmé est « à vérifier ».
- Les écrans concernés sont identifiés par leur EC- quand l'inventaire existe.
- Le rappel « projet à valider par un avocat » figure en tête de chaque document.

## Sources

- economie.gouv.fr, « Mentions sur votre site internet » (11/12/2025) ; Service-Public F23455 et F33527.
- DGCCRF, « Commerce en ligne : le consommateur doit… » et fiche « Annonces de réduction de prix ».
- Directive (UE) 2023/2673 ; ordonnance n° 2026-2 et décret n° 2026-3 du 5 janvier 2026 (JORF n° 4 du 6/1/2026).
- Loi n° 2023-451 du 9 juin 2023 ; ordonnance n° 2024-978 du 6 novembre 2024.
- INC / Conseil de l'UE, fermeture de la plateforme de règlement en ligne des litiges (20/07/2025).
