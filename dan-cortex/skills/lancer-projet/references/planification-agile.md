# Planification agile : sprints, capacité, vélocité, découpage, feuille de route

Complète `planification.md` (découpage, trois points, chemin critique, jalons) quand le projet avance par itérations. Le planning à jalons reste la vue d'engagement ; les sprints en sont l'exécution. Référence du `planificateur`, lue à la demande.

## Sommaire
1. Quand passer aux sprints
2. Estimation relative
3. Capacité d'un sprint
4. Vélocité et prévision
5. Découper une épopée
6. Préparer et clore un sprint
7. Feuille de route
8. Gabarit de `plan-sprints.md`
9. Contrôles avant de rendre
10. Origine

## 1. Quand passer aux sprints

| Situation | Forme de planning |
|---|---|
| Périmètre figé, contrat au forfait, dépendances externes datées | jalons et chemin critique seuls |
| Périmètre qui évolue, retours utilisateurs attendus, équipe stable | jalons + sprints de 1 ou 2 semaines |
| Réseau d'agents autonome (lots exécutés en heures) | « sprint » = vague de lots ; la capacité se compte en lots et en budget de tokens, pas en jours |

Ne jamais mélanger deux unités dans un même plan : soit des jours-personne, soit des points, soit des lots.

## 2. Estimation relative

- Unité : le point, mesure de taille relative (effort, complexité, incertitude), jamais convertie en heures dans un engagement.
- Échelle bornée : 1, 2, 3, 5, 8, 13. Au-delà de 13, l'élément est trop gros : le découper (section 5) avant de l'estimer.
- Étalon : choisir deux éléments déjà livrés comme référence (un « 2 » et un « 5 ») et comparer chaque nouvel élément à eux.
- Estimation à plusieurs voix (planning poker ou équivalent entre agents) : chacun estime seul, puis on discute les écarts extrêmes. Un écart de plus de deux crans révèle une incompréhension du besoin, pas un désaccord de chiffre.
- Pour un réseau d'agents, l'estimation se fait par analogie à des lots passés du `journal-de-build.md` ; toute estimation sans historique est marquée « hypothèse ».

## 3. Capacité d'un sprint

Capacité = (personnes × jours disponibles × taux de focalisation) − réserve.

| Paramètre | Valeur de départ | Commentaire |
|---|---|---|
| Taux de focalisation | 0,6 à 0,7 | réunions, revues, support, imprévus |
| Réserve pour anomalies | 10 à 20 % | plus si une recette est en cours |
| Absences, jours fériés | calendrier réel | fêtes nationales et religieuses du pays du projet |

Pour un réseau d'agents, la capacité se lit en lots exécutables en parallèle sans conflit de fichiers (`usine-logicielle/references/decoupage-lots.md`) et en budget de tokens de la vague.

## 4. Vélocité et prévision

- Vélocité = points des éléments **terminés** (définition de « terminé » satisfaite) dans le sprint. Un élément à 90 % compte zéro.
- Retenir la moyenne glissante des trois derniers sprints, avec la plus basse et la plus haute : elles donnent une fourchette, pas un chiffre.
- Prévision de fin : reste à faire ÷ vélocité basse = date prudente ; ÷ vélocité haute = date optimiste. Montrer les deux.
- Les trois premiers sprints n'ont pas de vélocité fiable : utiliser l'estimation à trois points de `planification.md` jusque-là.
- Signaux d'alerte : vélocité qui varie de plus de 30 % d'un sprint à l'autre ; éléments reportés deux fois ; travail ajouté en cours de sprint supérieur à 20 % de l'engagement.
- La vélocité ne se compare jamais entre équipes et ne sert jamais d'objectif : elle se gonfle dès qu'on la pilote.

## 5. Découper une épopée

Un bon élément de carnet est indépendant, négociable, porteur de valeur, estimable, petit et testable. Pour couper une épopée en tranches verticales (chaque tranche traverse interface, logique et données), essayer ces angles dans l'ordre :

| Angle | Question à poser | Exemple Parapro |
|---|---|---|
| Étapes d'un parcours | quelles étapes peut-on livrer l'une après l'autre ? | panier, puis livraison, puis paiement |
| Variantes de règle métier | quelle règle simple d'abord, les cas rares ensuite ? | paiement en ligne d'abord, paiement à la livraison ensuite |
| Effort majeur unique | qu'est-ce qui coûte une fois, puis peu ensuite ? | premier mode de paiement, puis les suivants |
| Simple ou complexe | quelle version minimale reste utile ? | adresse saisie librement, puis contrôle de zone |
| Variantes de données | quel type de donnée d'abord ? | produits sans variante, puis avec variantes |
| Saisie des données | interface rudimentaire d'abord ? | import CSV avant le formulaire riche |
| Exigences non fonctionnelles | fonctionner d'abord, performer ensuite ? | liste paginée, puis cache |
| Opérations | créer, lire, modifier, supprimer séparément ? | création de commande, puis annulation |
| Exploration | faut-il un essai borné avant d'estimer ? | essai de passerelle SMS, durée fixe |

Règle : après découpage, chaque tranche doit pouvoir être démontrée seule. Une tranche « couche technique » (« faire la base de données ») n'est pas une tranche.

## 6. Préparer et clore un sprint

**Préparation** (avant le sprint) : objectif du sprint en une phrase ; éléments prêts (critères d'acceptation, maquette si écran, dépendances levées) ; engagement ≤ vélocité basse ; risques du sprint nommés.

**Suivi** : courbe du reste à faire ; tout ajout en cours de sprint se paie par un retrait de même taille, décidé par le responsable produit.

**Clôture** : démonstration de ce qui est terminé (preuves exécutables, pas de déclaration) ; rétrospective courte : un point à garder, un point à changer, une action avec responsable ; mise à jour de la vélocité et de la prévision.

## 7. Feuille de route

Trois horizons, avec une incertitude croissante assumée :

| Horizon | Contenu | Précision |
|---|---|---|
| Maintenant | sprints en cours et suivant | éléments estimés |
| Ensuite | 1 à 3 mois | épopées et objectifs, taille en fourchette |
| Plus tard | au-delà | thèmes et résultats visés, sans date |

- Chaque ligne exprime un résultat attendu (« un particulier d'Azazga peut payer à la livraison »), pas une fonctionnalité nue.
- Les dates n'apparaissent que sur l'horizon « Maintenant » et sur les jalons contractuels.
- Une version courte pour le décideur (objectifs, risques, décisions à prendre) et une version détaillée pour l'équipe : jamais deux contenus contradictoires.
- La feuille de route se revoit à chaque clôture de sprint ; ses changements se tracent au registre des décisions.

## 8. Gabarit de `plan-sprints.md`

```markdown
# Plan de sprints — <projet ou évolution>
## Synthèse
## Hypothèses (durée du sprint, équipe, focalisation, réserve)
## Carnet découpé (ID, élément, points, dépendance, sprint)
## Capacité et engagement par sprint
## Prévision (vélocité basse, haute ; dates prudente et optimiste)
## Risques et décisions à prendre
```

## 9. Contrôles avant de rendre

- Aucun élément engagé au-dessus de 13 points.
- Engagement ≤ capacité calculée ; calcul montré.
- Prévision donnée en fourchette, hypothèses écrites.
- Chaque tranche se démontre seule et cite ses règles `RG-` ou ses décisions `DEC-`.
- Le lien avec les jalons de `planning.md` est explicite.

## 10. Origine

Méthode reformulée en français pour Dan-Cortex ; aucun texte copié. Idées inspirées de :
- `alirezarezvani/claude-skills` (MIT) : skills `project-management/skills/scrum-master`, `.gemini/skills/sprint-plan`, `product-team/skills/roadmap-communicator`, `business-operations/skills/capacity-planner` — https://github.com/alirezarezvani/claude-skills, commit `7f92eda`.
- Angles de découpage d'épopées : motifs publiés par Richard Lawrence (Humanizing Work) ; repris ici **en idées seulement**, réécrits, à partir de `deanpeters/Product-Manager-Skills` (CC BY-NC-SA 4.0, aucun texte repris) — https://github.com/deanpeters/Product-Manager-Skills, commit `cfcb697`.
- Détail des sources et commits : `sources/renfort-github.md`. Décision d'origine : réunion « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042).
