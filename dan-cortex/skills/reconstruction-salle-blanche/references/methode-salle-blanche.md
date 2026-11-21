# Méthode salle blanche, étape par étape

Cette fiche détaille les rôles, les livrables et les modèles. Elle complète le `SKILL.md` ; elle ne remplace pas l'avis d'un juriste.

## Principe

Une équipe **observe** et écrit. Une autre **construit** à partir de l'écrit seul. Entre les deux, un **relecteur** vérifie que la spécification ne contient rien de protégé. Le but : que le produit final ne dérive que de fonctions et de règles décrites en termes neutres, jamais d'une expression protégée de l'original.

Limite à dire franchement : la séparation d'équipes réduit le risque de copie, elle ne le supprime pas, et elle ne garantit rien devant un tribunal. Elle sert de preuve de bonne foi et de méthode de travail.

## Rôles

| rôle | qui | voit l'original | écrit | ne fait jamais |
|---|---|---|---|---|
| Observateur | `collecteur-web`, `analyste-concurrence` | oui | le relevé d'observation | coder |
| Rédacteur de spécification | pôle spécifications | le relevé, pas l'original brut si possible | la spécification neutre | copier un texte ou une valeur de marque |
| Relecteur neutralité | une personne ou un agent distinct | le relevé et la spécification | la liste des passages à réécrire | valider sa propre rédaction |
| Constructeur | `developpeur-frontend` ou équivalent | **non** | le code | demander une capture de l'original |
| Vérificateur | `testeur-visuel`, `testeur-web` | oui, pour comparer | le rapport d'écarts | corriger le code lui-même |
| Juriste | `juriste-numerique` | le résultat et la provenance | l'avis | décider à la place de l'utilisateur |

Si un seul agent doit tout faire (petit projet), le dire dans la fiche cible : la séparation est alors procédurale (documents distincts, relecture) et non réelle. Le niveau de garantie est plus faible.

## Livrables

### 1. Fiche cible et autorisation

Contenu : nom et adresse de la cible ; type (site, application, jeu) ; objectif de l'utilisateur (quelles fonctions l'intéressent) ; ce que l'utilisateur possède ou a le droit d'examiner ; pays concerné ; périmètre (pages, parcours, zones publiques seulement) ; accord écrit de l'utilisateur ; dates. Sans cette fiche, pas d'étude.

### 2. Relevé d'observation

Une entrée par observation, numérotée (`OBS-001`…), avec : source (page, écran), date, ce qui est observé, type (parcours, écran, état, comportement, performance, accessibilité), référence de la capture interne.

À relever : les parcours de bout en bout ; les écrans et leurs rôles ; les **états** (menu ouvert, fenêtre, onglet, erreur, vide, chargement) ; les comportements (ce qui se passe après chaque action, règles visibles, limites) ; les mesures de performance utiles (temps de chargement perçu, poids approximatif) ; l'accessibilité (navigation clavier, contrastes, libellés, langue). Les captures restent **internes**, rangées à part, jamais transmises au constructeur.

### 3. Spécification neutre

Réécriture en trois passes : (a) on liste la fonction en une phrase sans nom de marque ; (b) on décrit la règle ou le parcours avec nos mots ; (c) on remplace toute valeur d'identité (couleurs de marque, nom, slogan, textes) par une consigne neutre (« palette sobre à définir », « libellé court à rédiger »). Chaque article cite les `OBS-` dont il vient. S'appuyer sur `${CLAUDE_SKILL_DIR}/../specifications/SKILL.md` pour la forme (exigences, règles de gestion) et sur `${CLAUDE_SKILL_DIR}/../maquettes-parcours/SKILL.md` pour les parcours et la matrice d'interactions.

Test de neutralité : si une phrase de la spécification, lue seule, permet d'identifier la marque ou de reconstituer un texte de l'original, elle est à réécrire.

### 4. Construction par lots

Le constructeur reçoit : la spécification, les maquettes propres, la charte **de l'utilisateur** (la sienne, pas celle de la cible), ses propres contenus. Lots courts, chacun relié aux articles qu'il couvre. Voir `${CLAUDE_SKILL_DIR}/../usine-logicielle/SKILL.md`. Dépendances : licences vérifiées avant ajout.

### 5. Vérification par comparaison du comportement

On compare sur des critères de fonctionnement : le parcours aboutit-il, les états existent-ils, les règles sont-elles respectées, l'accessibilité est-elle au moins équivalente, les performances sont-elles du même ordre. On ne cherche pas à rapprocher les pixels de marque. Pour la mise en page, ne comparer que la structure (présence des zones, ordre, comportement aux trois grandes largeurs d'écran : bureau, tablette, téléphone).

Attention aux scores de ressemblance : une forte similitude de texte ou d'image est un **défaut** à corriger (copie probable), non un succès. Fixer un plafond de ressemblance sur les contenus et un plancher sur le comportement.

### 6. Affinage

Nombre de tours borné et annoncé à l'avance. Chaque écart de comportement devient une correction de la **spécification** d'abord, puis du code. Le constructeur ne reçoit jamais la capture de l'écart, seulement la règle corrigée.

### 7. Journal de provenance

Tableau : fonction construite | lot | article de spécification | `OBS-` d'origine | contenu propre ou neutre utilisé | auteur. Il sert d'audit et de preuve en cas de contestation.

### 8. Revue juridique avant publication

Recherche de ressemblances (textes, images, noms, structure de code, polices), contrôle des licences des dépendances et des polices, vérification du nom, du logo et de la charte. Chaque point douteux : retiré ou réécrit, puis consigné. Avis final de `juriste-numerique`, ou mention « à faire vérifier » avec le pays visé.

## Pièges fréquents

- Le constructeur « jette un œil » à l'original pour gagner du temps : la séparation est perdue ; recommencer le lot.
- La spécification garde des textes ou des couleurs de marque : repasser le test de neutralité.
- Le score de ressemblance devient l'objectif : le remplacer par des critères de comportement.
- Les captures circulent : les ranger en interne, avec accès limité.
