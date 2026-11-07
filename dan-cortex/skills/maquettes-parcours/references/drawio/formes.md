# draw.io : vocabulaire de formes écrites à la main

> Traduit et adapté de `Agents365-ai/drawio-skill`, `skills/drawio-skill/references/shapes.md`, commit `1f59eae2ca47`. © 2026 Agents365-ai, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire quand un fichier `.drawio` demande une forme précise (UML, BPMN, conteneur, connecteur) et qu'on serait tenté de **deviner** une chaîne `style=`. Lecture à la demande, depuis `schemas-mermaid.md` §6 ou la table de routage du skill.

## Sommaire
1. Principe
2. Formes courantes
3. Primitives UML
4. Conteneurs
5. Connecteurs
6. Réglages utiles
7. Contrôles avant de rendre

## 1. Principe

- Les styles ci-dessous sont courts et stables : ils s'écrivent à la main. Les compléter par `whiteSpace=wrap;html=1;`.
- Un nom de pochoir `shape=mxgraph.*` deviné et faux s'affiche comme une boîte vide, sans erreur. Pour une icône de fournisseur (nuage, réseau, Kubernetes) ou une forme rare, ouvrir la bibliothèque de formes de draw.io de bureau, poser la forme, puis copier son style (menu Modifier le style). Ne jamais inventer le nom.
- Aucune icône chargée depuis un CDN ni par URL d'image distante : un rendu hors ligne afficherait une boîte vide, et l'ouverture du fichier déclencherait un appel réseau. Pour une marque absente des bibliothèques, utiliser une forme générique (cylindre pour une base) avec le nom en libellé.

## 2. Formes courantes

| Besoin | Style |
|---|---|
| Rectangle / coins arrondis | `rounded=0;` / `rounded=1;` |
| Cercle / ellipse | `ellipse;` (`aspect=fixed;` pour un vrai cercle) |
| Losange (décision) | `rhombus;` |
| Cylindre (base de données) | `shape=cylinder3;` |
| Nuage | `cloud;` |
| Cube | `shape=cube;` |
| Note | `shape=note;` |
| Document (bas ondulé) | `shape=document;` |
| Dossier | `shape=folder;` |
| Carte (coin coupé) | `shape=card;` |
| Processus (double bord) | `shape=process;` |
| Étape / chevron | `shape=step;` |
| Parallélogramme (entrée-sortie) | `shape=parallelogram;perimeter=parallelogramPerimeter;` |
| Trapèze | `shape=trapezoid;perimeter=trapezoidPerimeter;` |
| Hexagone | `shape=hexagon;perimeter=hexagonPerimeter2;` |
| Saisie manuelle | `shape=manualInput;` |
| Stockage de données | `shape=dataStorage;` |
| Renvoi hors page | `shape=offPageConnector;` |
| Délai | `shape=delay;` |
| Porte OU / OU exclusif | `shape=or;` / `shape=xor;` |
| Flèche pleine | `shape=singleArrow;` / `shape=doubleArrow;` |
| Bulle | `shape=callout;` |

## 3. Primitives UML

| Élément | Style |
|---|---|
| Acteur | `shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;` |
| Frontière | `shape=umlBoundary;` |
| Contrôle | `shape=umlControl;` |
| Entité | `shape=umlEntity;` |
| Ligne de vie | `shape=umlLifeline;perimeter=lifelinePerimeter;container=1;` |
| Cadre | `shape=umlFrame;` |
| Interface fournie (sucette) | `shape=lollipop;direction=south;` |
| Interface requise | `shape=requires;direction=north;` |
| Composant | `shape=component;` |

## 4. Conteneurs

Les enfants d'un conteneur ont des coordonnées relatives à lui.

| Type | Style | Quand |
|---|---|---|
| Groupe invisible | `group;pointerEvents=0;` | pas de bord, pas de connexion propre |
| Couloir titré | `swimlane;startSize=30;` | titre visible, ou le conteneur porte des connexions |
| Toute forme en conteneur | ajouter `container=1;pointerEvents=0;` | boîte sans connexion propre |

## 5. Connecteurs

| Besoin | À ajouter au style |
|---|---|
| Tracé orthogonal | `edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;` |
| Courbe | `curved=1;` |
| Sans pointe | `endArrow=none;` |
| Pointe ouverte / fine | `endArrow=open;` / `endArrow=classicThin;` |
| Pointillé | `dashed=1;` (motif : `dashPattern=8 8;`) |
| Animation de flux | `flowAnimation=1;` |
| Fond du libellé | `labelBackgroundColor=#ffffff;` |

## 6. Réglages utiles

- `fontStyle` est un masque : `1` gras, `2` italique, `4` souligné ; additionner pour combiner (`3` = gras et italique).
- `direction=north|south|east|west` tourne une forme par quarts de tour ; `rotation=<degrés>` pour un angle libre.
- Dégradé : `gradientColor=#RRGGBB;` et `gradientDirection=north;`.
- `sketch=1;` donne un aspect dessiné à la main ; à réserver aux ateliers, jamais à un livrable de conception.

## 7. Contrôles avant de rendre

- Aucun `shape=mxgraph.*` qui n'ait été vérifié dans draw.io de bureau.
- Aucune URL dans un style (`image=http…`) ni dans un libellé.
- Couleurs conformes au thème (`theme-design-system.md`), contraste lisible (`accessibilite.md`).
