# Estimation : méthodes, trois points, réserves, dérives

Référence du `controleur-financier` pour chiffrer un projet sans fausse précision. Règle d'or : **une estimation est une fourchette avec sa base, jamais un chiffre nu.** État : octobre 2026. Ce qui n'est pas établi est marqué « à vérifier ».

## Sommaire
1. Choisir la méthode
2. Estimer à trois points
3. Réserves
4. Dérives typiques
5. Pièges
6. Contrôles avant de rendre
7. Sources

## 1. Choisir la méthode

| Situation | Méthode | Pourquoi |
|---|---|---|
| J1, périmètre flou | analogique : projets comparables de l'utilisateur, puis fourchettes publiques de `structure-budget.md` | rapide ; l'ordre de grandeur suffit pour décider d'y aller |
| J2, cahier des charges écrit | ascendante : jours-personnes par lot et par profil, à partir des charges du `planificateur` (`planning.md`) | le périmètre est connu, chaque EX- se rattache à un lot |
| Besoin de contrôle indépendant | taille fonctionnelle COSMIC (ISO/IEC 19761:2011), mesurée sur les fonctions FN-, du système entier à la user story | indépendante de la technologie ; sert à estimer effort de développement et de test, coût de remplacement, maintenance (source : éditeur d'outil, biais possible). Cinq normes ISO de mesure fonctionnelle existent (CAST) |
| Progiciel ou ERP | ascendante + ratio licences/intégration traité comme un plancher | le ratio 1:1 des éditeurs est jugé « dérisoirement bas » (Panorama) |
| Mode `integral` | deux méthodes croisées + contre-estimation indépendante | l'écart entre méthodes mesure l'incertitude |

Ne jamais retenir une seule méthode pour un budget soumis à un comité. Si les méthodes divergent de plus de 30 % (seuil de travail, hypothèse), chercher le périmètre implicite qui les sépare avant de moyenner.

Paramètres COCOMO II, tailles « t-shirt », Monte-Carlo, taux de réserve normatifs (Boehm 2000, PMBOK, AACE) et recommandation de « reference class forecasting » de Flyvbjerg (absente de l'abstract lu) : connaissance générale, non sourcée, à vérifier avant publication.

## 2. Estimer à trois points

Les charges viennent du planning. Ne pas les ré-estimer : les relire.

1. Reprendre par lot les valeurs O, M, P (jours-personnes) du `planificateur`.
2. Charge attendue E = (O + 4M + P) / 6 ; écart-type σ = (P − O) / 6 ; pour un ensemble de lots, σ² = somme des σ². La formule est celle de `lancer-projet/references/planification.md`.
3. Convertir en euros par profil avec les TJM de `structure-budget.md`, trois jeux de taux (bas, central, haut) : cela produit les trois scénarios.
4. Chiffrer à partir de E et de P, pas de M seul : M est l'estimation d'un jour sans accident.
5. Lot avec intégration, migration ou tiers : P au moins égal à 2 fois O.
6. Écrire pour chaque ligne sa base : analogie, décompte (écrans, API, règles RG-) ou avis d'expert ; sans base, « hypothèse ».

Calculer par script (Python, tableur), jamais de tête : somme des E, des σ², intervalle E ± 1,28 σ pour un intervalle à environ 80 % (approximation normale, hypothèse). Joindre le script ou la formule au dossier.

## 3. Réserves

| Réserve | Qui la détient | Taille de départ | Usage |
|---|---|---|---|
| Aléas | chef de projet | 20 % du budget de construction au minimum (heuristique d'agence pour un MVP, non vérifiée) | risques identifiés au registre |
| Gestion | sponsor (l'utilisateur) | calibrée sur la queue : voir ci-dessous | scénarios extrêmes, libérée par décision écrite |
| Change | porteur | selon le périmètre ajouté | demandes de changement acceptées |

- Poser la réserve d'aléas **une fois**, au niveau du projet et du chemin critique, pas dans chaque lot : chaque lot consommerait la sienne.
- Dérive moyenne observée : 27 % (Flyvbjerg et Budzier, 1 471 projets IT). Une réserve de 20 % (heuristique d'agence pour un MVP, RailsCarma, non vérifiée) ne la couvre pas. Pour le scénario prudent, retenir au moins 27 %.
- Environ 1 projet sur 6 (17 %, « cygne noir ») dérape de 200 % en moyenne, avec près de +70 % de délai. Aucune réserve raisonnable ne couvre ce cas : le traiter par des **jalons go/no-go** à enveloppes limitées, et nommer le seuil d'arrêt.
- Ne jamais additionner 27 % (Flyvbjerg), 17 % (cas extrêmes) et « plus d'un quart » (Panorama, ERP) : ils mesurent des choses différentes. Ce sont des ancrages de scénarios prudent, central et extrême.
- Une réserve consommée se justifie par une ligne au registre des risques (`RSQ-`) ou des décisions.

## 4. Dérives typiques

| Dérive | Signal | Parade |
|---|---|---|
| Périmètre qui grossit | EX- ajoutées sans lot ni budget | demande de changement chiffrée, décision de l'utilisateur |
| Besoins technologiques supplémentaires | première cause de dépassement ERP : plus d'un quart des organisations dépassent leur budget (Panorama, 2026 ERP Report, 4 mars 2026) | inventaire des intégrations dès J2 |
| Reprise de données | migration tardive | lot dédié, P ≥ 2 O, répétitions planifiées |
| Coûts d'exploitation oubliés | budget limité à la construction | TCO sur trois ans, voir `structure-budget.md` |
| Commissions variables | stores ou paiement qui changent de barème | hypothèse de variation en sensibilité |
| Facturation à l'usage de l'IA | crédits ou tokens consommés au-delà du plan | plafond d'usage par développeur |
| Biais d'optimisme | estimations du porteur toujours basses | classe de référence plutôt que cas particulier |

Contexte (planification.md, Flyvbjerg et Gardner) : 8,5 % des projets seulement tiennent coût et délai. Partir de la classe de référence, ajuster ensuite.

## 5. Pièges

- Mélanger HT et TTC, euros et dollars, jours facturés et jours de présence. Annoncer devise, taxe et date de la source sur chaque ligne.
- Appliquer à un MVP les fourchettes de blogs d'agences (15–180 k$) sans voir qu'elles supposent souvent des équipes réduites ou hors de France : une équipe freelance française donne ≈ 100–200 k€ (calcul de `structure-budget.md`).
- Traiter un gain IA comme acquis : mesures contrôlées proches de zéro (+19 % de temps en 2025), gains auto-déclarés 1,4 à 3x, biais de perception documenté. Voir `structure-budget.md`.
- Écraser un écart entre budget souhaité et budget estimé. L'écart se montre et se renégocie en périmètre, en délai ou en moyens.
- Donner un montant à trois chiffres significatifs : 187 342 € n'est pas plus exact que « 170 à 210 k€ ».
- Oublier le temps de l'utilisateur et de ses équipes (recette, validations, formation) : c'est un coût, même interne.

## 6. Contrôles avant de rendre

- Chaque ligne chiffrée a une base, une devise, une date de source.
- Les trois scénarios existent et leurs hypothèses séparatrices sont écrites.
- Le calcul est fait par script ou tableur, et reproductible.
- Les réserves sont séparées par détenteur ; le seuil d'arrêt est nommé.
- Le livrable rappelle qu'il ne vaut pas avis d'expert-comptable.

## Sources

- Flyvbjerg et Budzier, arXiv 1304.0265 (1 471 projets IT : +27 % en moyenne, 1 sur 6 à +200 %).
- ISO/IEC 19761:2011 (COSMIC) ; ScopeMaster (éditeur) ; CAST, glossaire des points de fonction.
- Panorama Consulting, 2026 ERP Report (4 mars 2026) et « How much does it cost to implement an ERP system ».
- RailsCarma, coût d'un MVP (réserve de 20 %, heuristique non vérifiée).
- `lancer-projet/references/planification.md` : formule à trois points, Flyvbjerg et Gardner (2023).
