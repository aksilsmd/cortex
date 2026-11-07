# Revue multi-angles : échecs silencieux et analyse des tests

Approfondit la section « Revue des différences » de `boucle-build-test.md`. `relecteur-code` passe la différence sous plusieurs angles, l'un après l'autre, plutôt qu'en une lecture globale. Les deux angles détaillés ici sont ceux que les outils ne voient presque jamais. La note de revue reste au gabarit et au plafond de `boucle-build-test.md`.

## Sommaire
1. Ordre des angles
2. Angle « échecs silencieux »
3. Angle « analyse des tests »
4. Gravité et formulation des constats
5. Contrôles avant de rendre
6. Origine

## 1. Ordre des angles

| Ordre | Angle | Question | Quand l'appliquer |
|---|---|---|---|
| 1 | Règle contre code | chaque `RG-` du lot est-elle appliquée, cas limites compris ? | toujours |
| 2 | Analyse des tests | les tests prouvent-ils le comportement ou épousent-ils le code ? | toujours |
| 3 | Échecs silencieux | une erreur peut-elle disparaître sans trace ni message ? | dès qu'il y a gestion d'erreur, valeur par défaut, appel externe |
| 4 | Failles évidentes | validation, autorisation, secret, donnée personnelle journalisée | toujours |
| 5 | Lisibilité et complexité | noms, code mort, dette non déclarée, commentaires faux | en dernier |

Un angle par passage : on relit la différence plusieurs fois avec une seule question en tête. C'est plus fiable qu'une lecture unique qui cherche tout.

## 2. Angle « échecs silencieux »

Principe : une erreur doit être soit traitée réellement, soit remontée avec assez de contexte pour être diagnostiquée. Toute erreur avalée est un défaut, même si les tests sont verts.

**Où chercher dans la différence**
- Blocs de capture d'exception vides, ou qui ne font que journaliser puis continuer.
- Captures trop larges (toute exception, toute erreur) qui masquent des erreurs sans rapport avec le cas prévu.
- Valeurs de repli qui transforment un échec en résultat plausible : liste vide, zéro, chaîne vide, objet par défaut, `null` renvoyé sans le dire.
- Chaînage optionnel ou opérateurs de valeur par défaut qui font disparaître une donnée obligatoire.
- Promesses ou tâches asynchrones non attendues, sans gestion de rejet.
- Nouvelles tentatives sans plafond ni journal ; délai d'attente qui renvoie « succès ».
- Journal au mauvais niveau (erreur en « debug »), message sans identifiant de corrélation ni contexte métier.
- Interface qui affiche « succès » alors que l'appel serveur a échoué ; message utilisateur générique sans action possible.
- Code de retour de commande ou de script ignoré.

**Questions à poser pour chaque gestion d'erreur**
1. Quelles erreurs cette capture attrape-t-elle vraiment ? Lesquelles n'étaient pas prévues ?
2. Si elle se déclenche en production, qui le saura, et comment ? (journal, alerte, message utilisateur)
3. Le repli est-il une règle métier écrite (`RG-`), ou un moyen de faire taire l'erreur ?
4. L'utilisateur peut-il agir à partir du message reçu ?
5. Une donnée incohérente peut-elle être enregistrée après l'erreur (paiement, stock, statut de commande) ?

**Attendu** : capture précise du type d'erreur prévu ; journal au niveau erreur avec contexte (identifiant de commande, étape, cause) et sans donnée personnelle ; message utilisateur clair ; transaction annulée ou compensée ; repli seulement s'il est une règle documentée.

## 3. Angle « analyse des tests »

Principe : on juge la couverture du **comportement**, pas le pourcentage de lignes.

**Lacunes à chercher**
- Chemin critique sans test : paiement, changement d'état, droits, calculs d'argent ou de stock.
- Cas négatifs absents : entrée invalide, droit refusé, ressource introuvable, double soumission, délai dépassé.
- Valeurs limites non testées : zéro, un, maximum, juste au-dessus du maximum, date de bascule.
- Branches d'erreur jamais exercées (celles de la section 2 en premier).
- Concurrence et idempotence : deux requêtes simultanées, rejeu d'un même appel.

**Faiblesses des tests présents**
- Assertion absente, ou seulement « ne lève pas d'erreur ».
- Assertion tautologique (on compare le résultat à lui-même ou à la même formule que le code).
- Simulacre (mock) qui remplace justement le comportement à tester.
- Test couplé à l'implémentation (appels internes, ordre privé) : il casse au remaniement sans détecter de régression.
- Test qui n'a jamais été vu rouge (voir `discipline-realisation.md`, section 1).
- Données de test réelles ou personnelles.

**Notation de chaque lacune** (de 1 à 10, critères explicites) :

| Note | Signification | Suite |
|---|---|---|
| 9-10 | perte d'argent, de données, faille, ou règle légale non vérifiée | bloquant |
| 6-8 | règle métier importante ou parcours principal non prouvé | majeur |
| 3-5 | cas limite ou message d'erreur non testé | mineur |
| 1-2 | complément souhaitable | note, sans constat |

Pour chaque lacune notée 6 ou plus, décrire le test manquant en une phrase : situation, action, résultat attendu, et la régression qu'il attraperait.

## 4. Gravité et formulation des constats

- Un constat : fichier et ligne, angle, gravité, fait observé, correction attendue. Pas de réécriture de code.
- Le relecteur distingue ce qu'il a constaté de ce qu'il suppose (« hypothèse : … »).
- Un même défaut vu sous deux angles fait un seul constat.
- Ce qu'un outil de format ou d'analyse statique détecte déjà ne fait pas l'objet d'un constat.

## 5. Contrôles avant de rendre

- Chaque angle applicable a été passé ; ceux non applicables sont dits (« pas de gestion d'erreur dans la différence »).
- Chaque gestion d'erreur nouvelle a reçu les cinq questions de la section 2.
- Chaque lacune de test bloquante ou majeure décrit le test manquant.
- La note respecte le gabarit et le plafond de `boucle-build-test.md`.

## 6. Origine

Angles reformulés en français pour Dan-Cortex ; aucun texte copié. Inspirés des agents `silent-failure-hunter` et `pr-test-analyzer` du plugin `pr-review-toolkit` de `anthropics/claude-plugins-official` (Apache-2.0) — https://github.com/anthropics/claude-plugins-official, commit `a7ba5b9`. Ordre de revue par angles inspiré du même plugin et de `requesting-code-review` de `obra/superpowers` (MIT, commit `2ce8aa1`). Détail : `sources/renfort-github.md`. Décision d'origine : réunion « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042).
