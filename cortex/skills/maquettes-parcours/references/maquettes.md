# Maquettes : du filaire à la haute fidélité

Ce fichier explique comment produire des maquettes fidèles à la matrice d'interactions, sans outil de dessin : fichiers HTML ou SVG autonomes, plus un cahier de maquettes qui permet de les reporter dans un outil de design. Dossier : `03-conception/design/maquettes/`.

## Sommaire
1. Niveaux de fidélité
2. Fichiers autonomes
3. Nommage et organisation
4. Annotations
5. Cahier de maquettes
6. Passation aux développeurs
7. Gabarit de `cahier-maquettes.md`
8. Pièges et contrôles avant de rendre

## 1. Niveaux de fidélité

| Niveau | Quand | Contenu | Ce qu'on teste |
|---|---|---|---|
| Filaire | J3, vague 3A, tous les écrans | blocs, hiérarchie, libellés réels des éléments, aucune couleur de marque | parcours, navigation, complétude |
| Haute fidélité | J3, vague 3B, écrans clés ; tous en mode `integral` | thème appliqué, textes réels, états, adaptations de largeur | lisibilité, contrastes, cohérence |
| Prototype navigable | sur demande | liens entre fichiers selon la matrice | tâches de bout en bout |

Écrans clés : accueil, tâche principale, formulaire le plus long, paiement ou action irréversible, tableau de données, erreur. Filaire d'abord pour tous : une erreur de structure coûte dix fois moins avant la couleur.

Largeurs à produire : mobile (360 px de large), tablette, bureau ; vérifier la lecture sans défilement horizontal à 320 px (reflow, WCAG 2.2 critère 1.4.10). Pour le RTL, une variante miroir des écrans clés.

## 2. Fichiers autonomes

Le `maquettiste` n'a pas d'outil de dessin. Il écrit du HTML ou du SVG que n'importe quel navigateur ouvre.

1. **Un fichier par écran** (HTML de préférence : texte sélectionnable, focus testable). SVG pour un schéma ou une illustration.
2. **Autonome** : une seule feuille de style dans le fichier, aucune ressource externe, aucune police ni script distant, aucun appel réseau. Pourquoi : lisible hors ligne, léger, sans fuite de données.
3. **Sobre** : HTML sémantique (`header`, `nav`, `main`, `footer`, `button`, `label`), CSS à base de variables reprises des jetons de `design-system.md`, pas de bibliothèque.
4. **Contenus fictifs évidents** (« Boutique Exemple », « Prénom Nom ») ; jamais la marque d'un tiers. Images : rectangles étiquetés, avec le texte alternatif prévu.
5. **Chaque élément interactif** porte `data-el="EL-001-04"` : le lien avec la matrice est vérifiable par recherche de texte.
6. **États** : un fichier ou une section par état (`EC-012-vide`, `EC-012-erreur`, `EC-012-chargement`), au minimum ceux déclarés dans l'inventaire.
7. Tester l'ouverture avec le seul clavier : l'ordre de tabulation visible et le focus doivent suivre l'ordre de lecture.

Pour les liens de navigation, pointer vers le fichier de l'écran de destination défini par la colonne « Destination » de la matrice, pas vers une page inventée.

## 3. Nommage et organisation

```
maquettes/
  cahier-maquettes.md
  EC-001-connexion.html
  EC-001-connexion--erreur.html
  EC-001-connexion--mobile.html
  EC-001-connexion--rtl.html
  jetons.css
```

Règle : `EC-<numéro>-<nom-court>[--<état ou variante>].<html ou svg>`, nom en minuscules sans accent. L'identifiant `EC-` est celui de `ecrans.md` : un écran absent de l'inventaire n'est pas maquetté ; un écran maquetté mais absent de l'inventaire est une erreur de l'un des deux. Le fichier `jetons.css` est autorisé comme seule ressource partagée, généré depuis les jetons (voir `theme-design-system.md`).

## 4. Annotations

Placer les annotations dans un bloc `<aside class="notes">` du fichier, masquable, ou en commentaires. Trois familles :

| Famille | Contenu |
|---|---|
| Comportement | renvoi aux `EL-` : réaction, destination, erreurs ; règles `RG-` appliquées |
| Accessibilité | nom accessible, rôle, ordre de focus, repère (landmark), annonce vocale, alternative au glissement |
| Contenu | clé de chaîne, longueur maximale, variantes de langue, données dynamiques |

Une annotation de comportement qui contredit la matrice est une anomalie de conception : la matrice fait foi, corriger l'un ou l'autre et le dire.

## 5. Cahier de maquettes

Document d'entrée du chef d'orchestre et des développeurs : il liste chaque écran, ses fichiers, son état de fidélité et ses annotations. Si le chef d'orchestre dispose d'un outil de design (Figma, Penpot ou autre, avec leur serveur MCP), il y reporte les écrans à partir du cahier ; sinon les fichiers HTML font office de maquettes. Ne pas supposer l'outil.

## 6. Passation aux développeurs

1. Statut par écran : `brouillon`, `relu`, `prêt pour dev`. Seul un écran dont la ligne de matrice est vérifiée par script passe à `prêt pour dev`.
2. Livrer les jetons en JSON versionné (voir `theme-design-system.md`), pas seulement en feuille de style.
3. Joindre carte de navigation (`navigation.md`), matrice, annotations d'accessibilité, chaînes de texte avec contexte.
4. Une maquette produite par IA ou un prototype généré n'est pas la spécification : les états rares et les règles implicites en sont absents.
5. Après réalisation : **recette design**. Comparer le produit à la maquette écran par écran, états compris, et consigner les écarts au registre des anomalies.

## 7. Gabarit de `cahier-maquettes.md`

````markdown
# Cahier de maquettes — <projet>

## Synthèse
<nombre d'écrans maquettés sur le total de l'inventaire, niveau de fidélité, écrans clés, états couverts, écarts avec la matrice, statut global, hypothèses non testées>

## Écrans
| ID | Fichier | Fidélité | États maquettés | Largeurs | Statut | Notes |
|---|---|---|---|---|---|---|
| EC-001 | EC-001-connexion.html | haute | défaut, erreur, chargement | 360, 1280 | relu | |

## Écarts et décisions
| Écran | Écart avec la matrice ou le thème | Décision |
|---|---|---|

## Pour reporter dans un outil de design
Hiérarchie de cadres, composants à créer, variables à définir (renvoi à `design-system.md`).
````

## 8. Pièges et contrôles avant de rendre

- Maquette du chemin heureux seul ; boutons sans `data-el` ; destinations factices.
- Texte de remplissage latin : le remplacer par un texte réel, sinon les longueurs sont fausses.
- Image contenant du texte ; contraste calculé sur la maquette claire seulement.
- Contrôles : chaque écran de l'inventaire a au moins un fichier filaire ; chaque `data-el` existe dans la matrice ; navigation fidèle à `navigation.md` ; fichiers ouverts au clavier ; aucune ressource externe.

## Sources
- WCAG 2.2, critère 1.4.10 Reflow (W3C).
- Design Tokens Format Module 2025.10, rapport final du Community Group : https://www.designtokens.org/tr/2025.10/format/
- Serveur MCP de Figma : https://www.figma.com/blog/introducing-figma-mcp-server/ ; Penpot (MPL 2.0, serveur MCP), sources secondaires.
