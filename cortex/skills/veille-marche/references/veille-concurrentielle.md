# Veille concurrentielle : repérer, démonter, comparer

Ce fichier guide `analyste-concurrence` et les `collecteur-web` de l'essaim. Livrables : une fiche par concurrent dans `01-decouverte/sources/concurrents/<slug>.md`, puis `01-decouverte/benchmark-concurrentiel.md`.

## Sommaire
1. Repérer les concurrents
2. Démonter une offre en huit couches
3. Fiche concurrent (gabarit du collecteur)
4. Matrice fonctionnelle
5. Prix
6. Positionnement et fiche de bataille
7. Gabarit du benchmark
8. Rythme de veille, pièges, contrôles
9. Sources

## 1. Repérer les concurrents

Lister au moins dix noms avant de choisir, classés :

| Classe | Définition | Où les trouver |
|---|---|---|
| Direct | même job, même segment | requêtes `"alternative to X"`, `"X vs"`, catégories d'un annuaire lues à la main, magasins d'applications, annonceurs des bibliothèques de publicités |
| Indirect | même job, autre segment ou autre forme | requêtes sur le problème sans nommer de produit, forums, offres d'emploi qui citent l'outil à maîtriser |
| Substitut | autre moyen d'atteindre le résultat (tableur, agence, service public, internalisation) | entretiens, forums, avis qui disent « on le fait sur Excel » |
| Ne rien faire | le statu quo | voix du client : ce que les gens supportent |

Retenir cinq à huit concurrents pour la collecte détaillée : trois directs, deux indirects ou plus petits mais en croissance, un substitut. Les autres restent en veille légère (nom, prix d'appel, positionnement). Garder la **raison de chaque exclusion**.

## 2. Démonter une offre en huit couches

| Couche | Ce qu'on relève | Source type | Fiabilité |
|---|---|---|---|
| Fonctions | liste, niveau, limites par plan | pages produit, documentation, essai | haute si essai ou doc |
| Parcours et onboarding | inscription, premier succès, états vides | inscription gratuite ou démo publique, avec compte au nom de l'utilisateur | haute |
| Prix et packaging | plans, unités, limites, remises | page tarifs, archive datée | haute |
| Pile technique | frameworks, hébergeur, outils de mesure | BuiltWith, Wappalyzer | moyenne : détection partielle |
| Trafic et acquisition | visites, sources, mots-clés | Similarweb, Semrush, Ahrefs | faible : modèles, croiser deux outils, « estimation » |
| Publicité | annonces actives, messages, pays | Meta Ad Library, TikTok Commercial Content Library | haute sur ce qui est listé |
| Emploi et financement | postes ouverts, levées, rachats | pages carrières, communiqués | moyenne |
| Changelog | nouveautés des 12 derniers mois | blog, notes de version, magasins | haute |

Règles de collecte : pages publiques seulement ; un compte d'essai ouvert honnêtement au nom du projet est admis si les conditions le permettent ; aucun faux profil, aucune extraction massive ; une capture ou archive datée par donnée sensible au changement (prix, promesse). Voir `sources-et-requetes.md`.

## 3. Fiche concurrent (gabarit du collecteur)

Identique pour toutes les instances, 60 lignes au plus. Une ligne sans source vaut « non trouvé ».

````markdown
# Fiche concurrent — <slug>
Collecté le : <date> par collecteur-web · Classe : direct | indirect | substitut · Pages lues : <n>

## Identité
Nom, URL, pays, année de création, taille déclarée — URL, date de consultation

## Positionnement
Promesse (citation exacte courte entre « »), cible déclarée, catégorie — URL, date

## Fonctions
| Fonction | Niveau (absent, partiel, complet) | Preuve (URL) | Consulté le |
|---|---|---|---|

## Prix
| Plan | Prix, unité, périodicité | Limites | URL | Consulté le |
|---|---|---|---|---|

## Pile, trafic, publicité
| Donnée | Valeur | Outil | Nature (mesure ou estimation) | Date |
|---|---|---|---|---|

## Emploi, financement, changelog
Trois à cinq faits datés, avec URL.

## Avis (chiffres seulement)
Plateforme, note, volume, date — le détail va dans sources/avis/.

## Non trouvé et limites d'accès
Liste.
````

## 4. Matrice fonctionnelle

1. Construire la liste des fonctions depuis les fiches (au moins 20), regroupées par job ; ajouter les fonctions qui manquent partout mais que les avis réclament.
2. Trois niveaux seulement : **absent**, **partiel** (précisé en une demi-phrase : limite, plan payant, bêta), **complet**.
3. Une **preuve par cellule** : URL de la fiche et date. Une cellule sans preuve est « non vérifié », jamais « absent ».
4. Ajouter deux colonnes : « fréquence de citation dans les avis » (renvoi `THM-`) et « chez nous » (prévu, option, non).
5. Lire la matrice en colonnes : une fonction présente chez tous est un **attendu** (à ajouter) ; présente chez un seul et peu citée est suspecte (à ne pas copier).

## 5. Prix

- Comparer sur **un cas d'usage type** décrit au début (par exemple dix utilisateurs, 500 commandes par mois, un an) : coût total, pas prix d'appel.
- Relever l'unité (siège, usage, commande, module), les paliers, les frais cachés (mise en service, support, intégrations, commissions de paiement), l'essai et la reconduction.
- Noter les changements de prix datés : un concurrent qui monte ses prix ouvre un segment.
- Prix indisponible (« nous contacter ») : le noter et chercher une fourchette dans des sources secondaires étiquetées comme telles.

## 6. Positionnement et fiche de bataille

Pour chaque concurrent clé : positionnement adverse (sa phrase), forces et faiblesses issues de la voix du client (avec `THM-`), objections probables, pièges à poser en démonstration, prix du cas type, signaux récents. Pas de dénigrement : tout énoncé comparatif doit rester exact et prouvé (le `juriste-numerique` relit).

## 7. Gabarit du benchmark

````markdown
# Benchmark concurrentiel — <projet>

## Synthèse
<12 lignes : concurrents retenus et exclus ; 3 constats ; fonctions attendues partout ; irritants non résolus ; écart de prix ; angles libres ; accès manquants>

## Périmètre et critères de sélection
## Concurrents
| ID | Concurrent | Classe | Positionnement | Prix cas type | Fiche |
|---|---|---|---|---|---|
| CON-01 | | | | | sources/concurrents/<slug>.md |
## Matrice fonctionnelle
## Parcours et onboarding comparés
## Prix et packaging
## Courbe de valeur
## Forces et faiblesses vues par les clients
## Écarts (ajouter, supprimer, différencier) — entrée du stratège
## Fiches de bataille
## Plan de veille
## Non trouvé et limites
````

## 8. Rythme, pièges, contrôles

Rafraîchir prix et changelog chaque mois, le reste chaque trimestre ; consigner la date du prochain passage.

Pièges : copier les fonctions des concurrents (parité) au lieu de viser leurs irritants ; confondre estimation et mesure ; oublier substituts et « ne rien faire » ; prix d'appel au lieu du coût total ; captures sans date.

Contrôles avant de rendre : chaque cellule a URL et date ; fiches toutes au même gabarit ; au moins un indirect et un substitut ; exclusions motivées ; écarts reliés aux `THM-`.

## Sources

- Meta Ad Library et API : https://www.facebook.com/ads/library/api/ (compte requis, pays obligatoire ; interface : annonces diffusées dans l'UE sur un an)
- TikTok Commercial Content Library : https://library.tiktok.com/ads
- BuiltWith : https://builtwith.com/ ; Wappalyzer : https://www.wappalyzer.com/ ; Similarweb : https://www.similarweb.com/
- Sensor Tower (applications), rachat de data.ai : https://sensortower.com/blog/data-ai-joins-sensor-tower
- Google Merchant API, rapports de compétitivité sur son propre compte : https://developers.google.com/merchant/api/guides/reports/understand-the-market
- Porter, HBR, 2008 : https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy
- Courbe de valeur (Kim et Mauborgne) : référence de mémoire, non vérifiée à la source (état : octobre 2026).
