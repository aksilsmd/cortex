# Étude de marché : taille, segments, tendances

Ce fichier cadre `01-decouverte/etude-de-marche.md` : combien vaut le marché, où se trouve la demande atteignable, dans quel sens il bouge. Le but est un chiffre de décision défendable, pas un grand chiffre.

## Sommaire
1. Cadrer avant de chiffrer
2. Taille du marché de deux façons
3. Segments et client idéal
4. Tendances et timing
5. Cinq forces et substituts
6. Économie unitaire : l'ordre de grandeur
7. Gabarit
8. Pièges et contrôles
9. Sources

## 1. Cadrer avant de chiffrer

Écrire en trois phrases : le **job** à accomplir (situation, motivation, résultat attendu), le **segment** visé, l'**alternative actuelle** (y compris « ne rien faire », le tableur, l'agence). Sans elles, le périmètre du marché flotte et les chiffres ne se comparent pas.

Fixer ensuite l'unité : clients, comptes, utilisateurs actifs, commandes ou euros par an. Une seule unité par calcul.

## 2. Taille du marché de deux façons

| Étage | Définition | Méthode par le haut | Méthode par le bas |
|---|---|---|---|
| TAM | tout le marché du job, tous pays et segments | chiffre public daté (fédération, statistique officielle, étude) | nombre de clients possibles × prix annuel |
| SAM | la part que l'offre peut servir (pays, segment, canal, langue) | TAM × part du segment servable | clients du segment servable × prix × taux d'équipement visé |
| SOM | ce que l'on peut raisonnablement capter en 12 à 36 mois | part plausible du SAM, étayée par un comparable | prospects joignables par canal × conversion × prix |

Règles :
- **Le chiffre de décision est celui du bas.** Le haut sert de borne et de contrôle de plausibilité. « 1 % du marché » seul n'est pas une méthode.
- Si les deux méthodes divergent de plus d'un facteur 2, chercher l'hypothèse fautive avant de conclure ; ne jamais moyenner.
- Chaque facteur du calcul bas est une hypothèse `HYP-` avec source, date, fourchette basse, centrale, haute. Montrer la sensibilité : quelles deux hypothèses font bouger le SOM de plus de 30 %.
- Dater chaque série. Les séries publiques sont révisées : en octobre 2026, la Fevad donne 196,4 Md€ pour l'e-commerce français en 2025 (+7 %) et 2,9 Md de transactions pour 2024 dans le bilan 2026 contre 2,6 Md dans l'édition précédente. Écrire l'édition citée.
- Sans source primaire : « non trouvé » ou fourchette marquée hypothèse, jamais un chiffre de blog présenté comme un fait.

Exemple fictif de calcul par le bas : 12 000 cabinets cibles (annuaire officiel, date) × 35 % équipables × 480 € par an = 2,0 M€ de SAM ; SOM an 3 : 900 prospects joignables × 4 % × 480 € = 17 k€, à comparer au coût de construction.

## 3. Segments et client idéal

1. Segmenter par **situation et job**, pas par démographie seule : deux profils différents qui cherchent le même résultat forment un segment.
2. Retenir un **client idéal** défini par des critères observables : taille, secteur, outil actuel, déclencheur d'achat, canal où on le joint.
3. Noter pour chaque segment : volume, intensité de la douleur (renvoi vers `voix-du-client.md`), alternatives en place, consentement à payer observé, coût d'accès.
4. Choisir le segment de départ là où quatre conditions se combinent : douleur fréquente, alternatives faibles, canal accessible, paiement observé. Si l'une manque, c'est une hypothèse de plus.

## 4. Tendances et timing

Le timing est une cause d'échec fréquente (29 % des fermetures de startups financées analysées par CB Insights, mars 2026 ; cohorte capital-risque, à transposer avec prudence à un projet autofinancé, un e-commerce ou un ERP). Relever :
- demande : volumes de recherche sur plusieurs années, saisonnalité, requêtes montantes ;
- offre : arrivées et sorties d'acteurs, levées de fonds, rachats, changements de prix ou de modèle ;
- technologie : ce qui rend possible aujourd'hui ce qui ne l'était pas (coût, API, appareils) ;
- réglementation : échéances qui forcent l'achat ou interdisent l'offre (voir `analyse-contexte.md`).

Pour chaque tendance : sens, vitesse, source datée, effet sur le SOM, et « signal qui nous ferait changer d'avis ».

## 5. Cinq forces et substituts

Une page : rivalité, entrants, substituts (y compris l'internalisation et « ne rien faire »), pouvoir des clients, pouvoir des fournisseurs (plateformes, stores, API, hébergeurs, passerelles de paiement). Porter reproche aux dirigeants de définir la concurrence trop étroitement : élargir à tout ce qui sert le même job. Conclure chaque force par « ce que cela change pour l'offre ».

## 6. Économie unitaire : l'ordre de grandeur

Ne pas bâtir le modèle (c'est `controleur-financier`), mais vérifier que le marché le permet : prix observé, coût d'acquisition plausible par canal, revenu par client sur 12 mois, marge brute estimée. Si le coût d'acquisition probable dépasse le revenu annuel par client sans rétention démontrable, le dire en synthèse. L'économie unitaire est la troisième cause racine d'échec citée (19 %).

## 7. Gabarit

````markdown
# Étude de marché — <projet>

## Synthèse
<12 lignes au plus : recommandation (aller, pivoter, renoncer, tester d'abord) ; 3 chiffres (SAM, SOM bas et haut, prix de référence) ; segment de départ ; 2 risques ; hypothèses HYP- les plus sensibles ; accès manquants>

## Périmètre
Job, segment, alternative actuelle, unité, zone, horizon.

## Taille du marché
| Étage | Par le haut | Par le bas | Écart | Source et date |
|---|---|---|---|---|
Sensibilité : deux hypothèses dominantes.

## Hypothèses
| ID | Hypothèse | Valeur (basse, centrale, haute) | Source et date | Confiance |
|---|---|---|---|---|
| HYP-01 | | | | |

## Segments et client idéal
## Tendances et timing
## Cinq forces et substituts
## Économie unitaire (ordre de grandeur)
## Risques et tests de demande à lancer
## Limites et non trouvé
## Annexes : sources datées (fiches de sources/marche/)
````

## 8. Pièges et contrôles

- TAM seul ; marché défini par la solution et non par le job ; oubli des substituts.
- Série révisée mélangée à une ancienne ; chiffre en dollars et en euros sans date de change.
- Estimations d'outils (trafic, parts) présentées comme des mesures.
- Contrôles avant de rendre : deux méthodes présentes ; chaque `HYP-` sourcée ou marquée hypothèse ; sensibilité chiffrée ; segment de départ justifié ; « non trouvé » listé ; aucun chiffre sans URL et date.

## Sources

- Porter, « The Five Competitive Forces That Shape Strategy », HBR, janvier 2008 : https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy
- Christensen et al., « Know Your Customers' Jobs to Be Done », HBR, septembre 2016 : https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- Fevad, bilan du e-commerce en France 2025 : https://www.fevad.com/bilan-du-e-commerce-en-france-les-francais-ont-depense-pres-de-200-milliards-deuros-sur-internet-en-2025/
- Fevad, chiffres clés 2026 : https://www.fevad.com/ledition-2026-des-chiffres-cles-du-e-commerce/
- CB Insights, causes d'échec des startups (mise à jour du 6 mars 2026) : https://www.cbinsights.com/research/report/startup-failure-reasons-top/
- data.gouv.fr, données économiques du commerce 2026 : https://www.data.gouv.fr/datasets/donne-economique-sur-le-commerce-et-son-evolution-en-france-2026
- TAM, SAM, SOM : aucune source primaire retrouvée (état : octobre 2026) ; méthode de bonne pratique.
