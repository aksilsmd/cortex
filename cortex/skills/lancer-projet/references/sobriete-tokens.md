# Sobriété en tokens

Un système multi-agents consomme plusieurs fois plus de tokens qu'une conversation simple : chaque agent ouvre
son propre contexte et envoie ses propres requêtes. Cortex accepte ce coût là où le parallélisme et l'expertise
le justifient, et le supprime partout ailleurs. Les règles ci-dessous sont classées par gain décroissant.

## Ordres de grandeur mesurés

Ordres de grandeur observés en octobre 2026 pendant la construction du plugin, sur Claude Code 2.1, dans une
session comptant environ 500 skills et 60 outils. Méthode : lancer un agent qui répond sans appeler d'outil et
lire sa consommation. Les valeurs varient avec l'équipement de la session ; le rapport entre elles compte plus
que les chiffres :

| Lancement | Contexte de départ |
|---|---|
| agent généraliste, tous outils | environ 90 000 tokens |
| agent Cortex avec l'outil de skills | environ 16 000 tokens |
| agent Cortex, 8 outils de métier | environ 6 000 tokens |
| agent Cortex, lecture seule | environ 4 000 tokens |

Ce contexte de départ est repayé à chaque appel d'outil de l'agent. D'où la première règle.

## Les règles

1. **Lancer des agents Cortex, pas des agents généralistes.** Un agent généraliste ne se justifie que s'il doit
   utiliser un skill ou un connecteur extérieur au plugin.
2. **Choisir le niveau le plus bas qui suffit.** Collecte, exécution de tests, vérification d'une liste : niveau C.
   Analyse, rédaction, code : niveau B. Arbitrage, architecture, audit, droit : niveau A.
3. **Dimensionner la vague.** `eclair` : 3 à 4 agents ; `standard` : 6 à 8 ; `integral` : 10 à 16. Avant chaque
   lancement, se demander : cette mission occupe-t-elle un expert au moins un quart d'heure ? Sinon, la fusionner
   avec une voisine ou la faire soi-même.
4. **Donner les chemins exacts.** « Lis `02-cadrage/cahier-des-charges.md`, section Exigences » coûte dix fois
   moins que « prends connaissance du projet ».
5. **Écrire pour être lu à moindre coût.** Synthèse de 12 lignes en tête de chaque livrable ; tableaux à
   identifiants ; un fichier par module plutôt qu'un document géant. Le lecteur suivant ne charge que ce qu'il
   lui faut.
6. **Laisser les scripts compter et vérifier.** `cortex.py` pour la couverture, les registres, les jalons, la
   traçabilité, les interactions et l'index ; `essais.py` pour toute commande de test ou de build. Ne jamais
   lire `couverture.csv` ou un journal de tests en entier.
7. **Borner les échanges.** Compte rendu de 150 mots ; positions de réunion de 200 mots ; deux tours de débat ;
   trois tentatives de correction avant d'escalader.
8. **Reprendre plutôt que relancer.** Un agent repris garde son contexte en cache ; un agent neuf relit tout.
   Valable pour les corrections après revue, les compléments, la consolidation d'un pôle.
9. **Ne chercher qu'une fois.** Toute collecte web est rangée dans `01-decouverte/sources/` avec URL et date. Un
   agent consulte ce dossier avant de chercher.
10. **Regrouper tes propres actions.** Plusieurs commandes de script dans un seul appel Bash ; tous les lancements
    d'une vague dans un seul message ; une seule série de questions à l'utilisateur par jalon.
11. **Ne pas faire tourner le réseau à vide.** Une question simple de l'utilisateur appelle une réponse directe,
    pas une vague.

12. **Vague pilote avant vague large.** Avant une vague de recherche ou de collecte de plus de quatre agents,
    en lancer deux ou trois, lire leur consommation au journal, puis élargir. Une douzaine d'agents de recherche
    lancés d'un coup peut épuiser une fenêtre d'utilisation avant d'avoir rendu quoi que ce soit.
13. **Fixer un plafond.** `cortex.py etat --set plafond_tokens=<n>` : le journal alerte à 80 % et à 100 %. À
    100 %, s'arrêter, rendre compte à l'utilisateur et lui laisser le choix : continuer, changer de mode, ou
    reprendre plus tard.
14. **Savoir continuer seul.** Si la limite de débit tombe ou si le budget est épuisé, ne rien relancer : jouer
    toi-même les rôles restants du jalon, un par un, avec les mêmes fiches et les mêmes gabarits. L'état du
    dossier projet permet de reprendre le réseau à la session suivante.

## Sobriété pendant la réalisation du code

Le code est la phase la plus coûteuse. Le détail est dans le skill `usine-logicielle`
(`references/sobriete-code.md`) ; l'essentiel :

- découper en lots aux contrats d'interface écrits, pour qu'aucun développeur n'ait à lire le code d'un autre ;
- un lot = un agent = un jeu de fichiers dont il est seul propriétaire ;
- générer le squelette avec l'outil officiel du framework plutôt que de l'écrire ;
- faire respecter les normes par les outils (formatage, analyse statique, typage), pas par relecture ;
- lancer toute commande par `essais.py` : seules les lignes d'échec entrent dans le contexte ;
- relire des différences, pas des fichiers entiers ;
- trois tentatives de correction par anomalie, puis escalade au relecteur ou à l'architecte.

## Budgets indicatifs par jalon

Ordres de grandeur en mode `standard`, pour calibrer et repérer une dérive, à remplacer par les mesures du
journal (`cortex.py journal bilan`) dès le premier jalon franchi.

| Jalon | Agents lancés | Remarque |
|---|---|---|
| J1 Opportunité | 8 à 14 | l'essaimage de collecte tourne au niveau C |
| J2 Cadrage | 6 à 9 | |
| J3 Conception | 14 à 22 | deux vagues ; la plus lourde hors code |
| J4 Réalisation | selon le nombre de lots | 3 à 4 lancements par lot : développement, revue, tests, correction |
| J5 Validation | 8 à 12 | audit général compris |
| J6 et J7 | 4 à 6 | |

Le mode `eclair` divise ces nombres par deux à trois ; le mode `integral` les multiplie par deux environ.

## Signes de dérive et remèdes

| Signe | Remède |
|---|---|
| un agent rend un compte rendu de plusieurs pages | lui rappeler le format ; ne lire que les rubriques |
| une vague dépasse la taille du mode | fusionner des missions, reporter ce qui n'est pas sur le chemin du jalon |
| deux agents ont écrit sur le même sujet | corriger les hors-périmètre des ordres de mission |
| une réunion entame un troisième tour | trancher : le décideur désigné arbitre avec ce qu'il a |
| tu relis des documents entiers | lire les synthèses ; demander un `verificateur` pour un contrôle détaillé |
| la même recherche revient | vérifier `01-decouverte/sources/` et l'indiquer dans l'ordre de mission |

## Rendre compte de la consommation

À chaque jalon, donner à l'utilisateur une ligne tirée de `cortex.py journal bilan` : nombre d'agents lancés et
tokens journalisés. Il doit pouvoir décider de changer de mode en connaissance de cause.
