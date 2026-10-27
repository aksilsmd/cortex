# Voix du client : dépouiller avis, commentaires, réseaux, forums, stores

Ce fichier guide `analyste-voix-client` et les `collecteur-web` de l'essaim. Livrables : fiches dans `01-decouverte/sources/avis/<source>-<concurrent>.md`, puis `01-decouverte/voix-du-client.md`. Le but : dire ce qui fait souffrir, ce que les gens attendent et ce que personne ne couvre.

## Sommaire
1. Définir le corpus
2. Accès et conformité par source
3. Fiche de source (gabarit du collecteur)
4. Taxonomie
5. Coder
6. Quantifier
7. Biais
8. Gabarit de la synthèse
9. Pièges et contrôles
10. Sources

## 1. Définir le corpus

Écrire d'abord la question (« pourquoi les clients quittent-ils X ? »), puis le corpus : concurrent × source × période (12 à 24 mois) × langue. Viser au moins **200 avis par concurrent clé**, **échantillonnés par note et par trimestre** : prendre autant de 1 à 2 étoiles que de 4 à 5, sinon le corpus ne dit que ce que la plateforme met en avant. Si le volume disponible est plus faible, le dire en synthèse.

## 2. Accès et conformité par source

Consulter le statut avant d'envoyer un collecteur (`sources-et-requetes.md` §4). État : octobre 2026.

| Source | Statut | Conduite |
|---|---|---|
| G2, Capterra | conditions interdisant tout scraping, même de contenu public, et l'usage pour entraîner ou évaluer un modèle | lecture manuelle d'un échantillon par une personne, ou export ou données sous licence |
| Trustpilot | conditions de novembre 2025 interdisant fouille de textes et scraping « pour tout objectif, y compris l'IA » | idem ; ne pas confier à un agent d'exploration |
| Reddit | usage commercial soumis à approbation écrite | demander l'accord à l'utilisateur ; sinon lecture manuelle de quelques fils |
| X | API facturée à l'usage (0,005 $ par ressource lue, plafond mensuel) | budget fixé avant ; sinon lecture manuelle |
| Magasins d'applications | API d'avis limitée aux applications de l'éditeur (à vérifier) | données sous licence (Sensor Tower) ou lecture manuelle |
| Forums, blogs, Hacker News, YouTube, réseaux professionnels | conditions et API non vérifiées à la source | lire les conditions et `robots.txt` avant ; accès libre sans compte uniquement ; à défaut, lecture manuelle |
| Avis de l'utilisateur (support, enquêtes, tickets, e-mails) | données de l'utilisateur | meilleure source ; pseudonymiser avant transmission |

Quand la lecture est « manuelle », l'agent lit les pages que la recherche lui renvoie, copie moins de 25 mots par verbatim et ne parcourt pas en série. Une source fermée reste listée avec son statut.

## 3. Fiche de source (gabarit du collecteur)

Identique pour toutes les instances, 50 lignes au plus.

````markdown
# Fiche de source — <plateforme> / <concurrent ou sujet>
Collecté le : <date> par collecteur-web · Méthode : lecture manuelle | API | export | licence · Statut d'accès : <conditions lues le, résultat>

## Corpus
Période, langue, nombre d'avis lus, critère d'échantillon.
Distribution des notes lues : 1 étoile n, 2 étoiles n, 3 étoiles n, 4 étoiles n, 5 étoiles n. Note affichée, volume total affiché.

## Verbatims
| N° | Code provisoire (I irritant, A attente, M manque, S satisfaction) | Verbatim ou reformulation (R) | Note | Date | URL de la page |
|---|---|---|---|---|---|
| 1 | | « citation exacte de 25 mots au plus » | | | |

## Observations brutes
Volume par code provisoire. Rafales d'avis suspects, avis incités, langue.

## Non trouvé et limites
````

Règles : auteur jamais noté ; URL de la page d'avis, pas du profil ; une reformulation porte « (R) » ; 30 verbatims au plus par fiche, choisis pour leur diversité, pas pour leur éclat.

## 4. Taxonomie

| Code | Sens | Exemple de formulation |
|---|---|---|
| I irritant | douleur vécue avec l'offre existante | « impossible d'exporter sans passer au plan supérieur » |
| A attente | fonction ou qualité souhaitée, que l'offre soit censée la fournir ou non | « il faudrait pouvoir… » |
| M manque | besoin non couvert, contourné ou bricolé | « on le fait sous tableur à côté » |
| S satisfaction | ce qui est aimé : à préserver | |
| C contexte | job, persona, situation d'usage | |

Ajouter pour chaque occurrence : aspect (prix, prise en main, performance, support, fiabilité, intégration, contenu), segment si connu, concurrent. Le sentiment se note par aspect, pas pour l'avis entier.

## 5. Coder

1. Le modèle propose un **codebook** (liste de thèmes avec définition et exemples) sur 100 à 200 avis ; l'analyste l'ajuste.
2. Coder tout le corpus avec le codebook figé. Un thème = une définition d'une phrase.
3. **Double codage** d'au moins 10 % du corpus par une seconde passe indépendante ; reporter l'accord (kappa) ; sous 0,6, reprendre les définitions.
4. **Contrôle humain** d'au moins 50 codages produits par modèle ; consigner le taux d'erreur (ironie, négation, langue, hallucination). Si l'utilisateur n'a personne pour contrôler, écrire « codage non contrôlé » en synthèse.
5. Nettoyer avant : doublons, spam, rafales (beaucoup d'avis proches le même jour), avis sans texte.

## 6. Quantifier

| Mesure | Calcul | Seuil |
|---|---|---|
| Fréquence | avis citant le thème ÷ avis lus | aucun thème conclu sous 30 occurrences |
| Sévérité | 1 gêne, 2 abandon d'une tâche, 3 départ ou perte d'argent ; moyenne des cas lus | |
| Tendance | fréquence par trimestre | à signaler si le sens est constant sur 3 trimestres |
| Segment | fréquence par segment ou concurrent | |
| Confirmation | nombre de sources de natures différentes (avis publics, forum, support, entretien) | **3 au moins** pour déclarer un manque « confirmé » ; sinon « indice » |

Chaque thème reçoit un identifiant `THM-` et un statut : confirmé, indice, anecdote.

## 7. Biais

- **Distribution en J** : acquisition et sous-déclaration donnent beaucoup de 5 et de 1 et peu de milieu ; la moyenne est un mauvais estimateur de la qualité. Présenter la distribution.
- Minorité vocale et audience propre à chaque plateforme (G2 : acheteurs B2B ; forums techniques : profils experts ; Trustpilot : service et e-commerce).
- Avis incités, faux ou retirés ; survivance (ceux qui sont partis n'écrivent plus) ; récence ; langue.
- Dire pour chaque biais ce qu'il change à la conclusion.

## 8. Gabarit de la synthèse

````markdown
# Voix du client — <projet>

## Synthèse
<12 lignes : corpus (volumes, périodes, sources, exclusions), 5 thèmes majeurs avec fréquence, 3 manques, 3 satisfactions à protéger, biais dominants, confiance>

## Question et corpus
## Sources et statut d'accès
| Source | Statut | Avis lus | Fiche |
|---|---|---|---|
## Méthode (codebook, double codage, accord, taux d'erreur du modèle)
## Thèmes
| ID | Type (I, A, M, S) | Thème | Fréquence | Sévérité | Tendance | Sources | Statut | Verbatims (N° de fiche) |
|---|---|---|---|---|---|---|---|---|
| THM-01 | | | | | | | | |
## Par concurrent et par segment
## Biais et limites
## Opportunités (entrée du stratège) et hypothèses à tester
## Annexes : codebook, échantillon codé
````

## 9. Pièges et contrôles

Moyenne lue au lieu de la distribution ; Reddit ou X surpondérés ; thème conclu sur cinq cas ; auteurs identifiables dans les fiches.

Contrôles avant de rendre : chaque verbatim a URL de page, date, note ; aucun nom ni lien de profil ; chaque thème a fréquence, sévérité, statut ; 3 sources pour tout « confirmé » ; sources fermées listées.

## Sources

- G2, conditions d'utilisation : https://legal.g2.com/terms-of-use ; Capterra : https://www.capterra.com/legal/terms-of-use/
- Trustpilot, conditions pour entreprises (nov. 2025) : https://corporate.trustpilot.com/legal/for-businesses/terms-of-use-and-sale-for-businesses/nov-2025
- Reddit, Responsible Builder Policy : https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy
- X API, tarifs : https://docs.x.com/x-api/getting-started/pricing
- Hu, Pavlou, Zhang, distribution en J des avis : https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2380298
- CNIL, moissonnage et intérêt légitime (19 juin 2025) : https://www.cnil.fr/fr/focus-interet-legitime-collecte-par-moissonnage
- Sensor Tower, étiquettes d'avis d'applications : https://sensortower.com/blog/app-review-tags
