# Discipline de réalisation : TDD, débogage, vérification, plans, revue

Complète `boucle-build-test.md`. Ces règles s'appliquent au développeur pendant le lot et au relecteur quand il juge les preuves. Chacune a une preuve attendue : sans preuve, la règle n'est pas respectée. Lecture à la demande, section utile seulement.

## Sommaire
1. Cycle rouge-vert-remaniement
2. Excuses à refuser
3. Débogage en quatre phases
4. Vérifier avant de dire « fini »
5. Plan d'implémentation en tâches courtes
6. Demander une revue
7. Recevoir une revue
8. Origine

## 1. Cycle rouge-vert-remaniement

Le point de départ est toujours le test : on décrit le comportement visé par un test, on le regarde échouer en signalant précisément ce manque, et c'est seulement ce rouge constaté qui ouvre le droit de modifier le code livré.

1. **Rouge** : écrire un seul test, le plus petit qui exprime un comportement attendu (une règle `RG-`, un critère `CT-`). Le lancer. Il doit échouer, et le message d'échec doit correspondre au comportement absent (pas une erreur d'import ou de syntaxe).
2. **Vert** : écrire le code le plus simple qui fait passer ce test, rien de plus. Relancer : vert, et tous les autres tests restent verts.
3. **Remaniement** : améliorer noms, duplication, structure, sans changer le comportement ; les tests restent verts après chaque petit pas.
4. Recommencer avec le test suivant.

Du code écrit avant son test se jette et se réécrit à partir du test : le garder « comme modèle » revient à écrire le test pour épouser le code.

Preuve attendue au journal de build : pour chaque règle, la sortie rouge (une ligne via `essais.py`) puis la sortie verte.

Exceptions acceptées, écrites au journal : prototype jetable explicitement marqué, code généré, configuration pure. Toute autre exception se demande au relecteur.

## 2. Excuses à refuser

| Excuse | Réponse |
|---|---|
| « C'est trop simple pour être testé » | un test simple coûte une minute ; le défaut simple en production coûte plus |
| « J'ajouterai les tests après » | un test écrit après passe du premier coup : il ne prouve rien |
| « J'ai vérifié à la main » | une vérification manuelle ne se rejoue pas à la régression |
| « Le test passe déjà, donc c'est bon » | un test qui n'a jamais été rouge peut être tautologique |
| « Je garde ce code écrit avant, il marche » | il n'a pas été conçu par le test ; le réécrire à partir du test |
| « C'est urgent » | l'urgence augmente le coût d'un retour arrière ; le cycle reste court |
| « Modifier le test est plus rapide » | principe 6 du skill : un test ne s'affaiblit pas pour passer |

## 3. Débogage en quatre phases

Tant que l'origine du défaut n'est ni localisée ni expliquée par écrit, on reste en enquête et le code ne bouge pas : soigner le symptôme ne fait que déplacer le défaut.

**Phase 1, enquêter**
- Lire le message d'erreur et la pile en entier, jusqu'à la première ligne du projet.
- Reproduire de façon fiable, avec la plus petite entrée possible. Non reproductible : collecter des traces, ne pas deviner.
- Regarder ce qui a changé : différence, dépendance, configuration, données.
- Dans un système à plusieurs étages (interface, API, base), tracer la donnée à chaque frontière pour localiser l'étage où elle devient fausse ; remonter vers l'origine de la mauvaise valeur, pas vers l'endroit où elle explose.

**Phase 2, comparer**
- Trouver un cas voisin qui fonctionne (autre écran, autre test, version précédente) et lister toutes les différences, même celles qui paraissent sans rapport.

**Phase 3, une hypothèse à la fois**
- Écrire l'hypothèse : « la cause est X parce que Y ».
- La tester par le plus petit changement possible, une seule variable à la fois.
- Hypothèse infirmée : revenir à la phase 1 avec ce nouveau fait, sans empiler un second correctif.

**Phase 4, corriger**
- Écrire d'abord un test qui reproduit le défaut (rouge), puis le correctif unique (vert), puis la non-régression.
- **Trois correctifs échoués de suite** : arrêter. Le problème est probablement de conception ; le signaler à l'architecte ou au chef d'orchestre (règle des trois tentatives de `boucle-build-test.md`).

Signaux d'arrêt : « je tente juste ça », plusieurs changements dans un même essai, correctif proposé sans avoir lu la pile.

## 4. Vérifier avant de dire « fini »

Annoncer qu'un travail est terminé revient à citer ce que vient d'afficher la commande de contrôle, relancée pour l'occasion ; un souvenir d'exécution, une exécution plus ancienne ou une conviction ne valent pas preuve.

1. Nommer la commande qui prouve l'affirmation (tests, build, analyse, script de contrôle).
2. La lancer maintenant, en entier, via `essais.py`.
3. Lire la sortie : code de retour, nombre d'échecs, avertissements.
4. Si la sortie confirme : l'affirmer **avec** la preuve (commande, date, résumé de sortie). Sinon : dire l'état réel.

| Affirmation | Preuve exigée | Insuffisant |
|---|---|---|
| « Les tests passent » | sortie du lanceur, 0 échec | une exécution antérieure, « devrait passer » |
| « Le build est bon » | code de retour 0 du build | l'analyse statique seule |
| « Le défaut est corrigé » | test du symptôme d'origine vert | code modifié |
| « Exigence couverte » | contrôle ligne à ligne contre la `RG-` | tests verts seuls |
| « Le sous-agent a fini » | différence relue et vérifiée | son compte rendu |

Mots qui déclenchent une vérification avant d'écrire : « devrait », « probablement », « normalement », « terminé », « tout est vert ».

## 5. Plan d'implémentation en tâches courtes

Pour tout lot de plus d'une demi-journée de travail humain (ou plus de quelques fichiers), écrire d'abord un plan dans `04-realisation/plans/plan-<lot>.md` :

- En-tête : but en une phrase, architecture retenue en deux ou trois phrases, outils et versions.
- Tâches de 2 à 5 minutes, chacune avec : fichiers exacts à créer ou modifier (chemin, et lignes si connues) ; test à écrire et sortie rouge attendue ; changement minimal ; commande de vérification et sortie verte attendue ; point de sauvegarde (commit local).
- Ordre : un test, son code, sa vérification. Pas de tâche « tout implémenter ».
- Écrire pour un exécutant sans contexte : aucun « comme d'habitude », aucun renvoi implicite.
- Pas de fonctionnalité non demandée (principe « on n'en aura pas besoin ») ; pas de duplication.

Exécution : par lots de trois tâches, vérification à chaque tâche, compte rendu à la fin de chaque lot de trois. Un blocage ou une instruction ambiguë arrête l'exécution et remonte au planificateur du lot : on ne devine pas.

## 6. Demander une revue

- Quand : à la fin de chaque lot, avant toute fusion, et après un correctif délicat.
- Fournir à `relecteur-code` : ce qui a été fait, les exigences visées (`RG-`, `CT-`, plan), la plage de différence (commit de base et commit de tête), la sortie verte des contrôles.
- Ne pas fournir son raisonnement ni ses doutes orientés : le relecteur juge le résultat avec un contexte neuf.
- Traiter les constats bloquants avant de continuer ; les majeurs avant la fin du lot ; les mineurs se notent.

## 7. Recevoir une revue

1. Lire tous les constats avant de réagir.
2. Reformuler chaque constat dans ses propres mots ; un constat flou se clarifie **avant** de toucher au code, sinon les constats liés seront mal traités.
3. Vérifier chaque constat contre le code et les exigences : est-il exact ici ? casse-t-il autre chose ? contredit-il une décision tracée ?
4. Répondre par un fait : correction faite (avec preuve) ou désaccord argumenté (fichier, ligne, test, décision). Pas d'accord de façade, pas de remerciements de convenance.
5. Corriger un constat à la fois, tester chacun.
6. Désaccord persistant après deux allers-retours : escalade au chef d'orchestre.

Un constat qui propose une fonctionnalité « plus complète » se vérifie contre le besoin : si rien ne l'utilise, le refuser avec ce motif.

## 8. Origine

Méthodes reformulées en français pour Dan-Cortex ; aucun texte copié, aucun hook ni script repris. Inspirées des skills `test-driven-development`, `systematic-debugging`, `verification-before-completion`, `writing-plans`, `executing-plans`, `requesting-code-review` et `receiving-code-review` de `obra/superpowers` (MIT, © 2025 Jesse Vincent) — https://github.com/obra/superpowers, commit `2ce8aa1`. Le hook `SessionStart` et les scripts de ce dépôt sont exclus. Détail : `sources/renfort-github.md`. Décision d'origine : réunion « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042).
