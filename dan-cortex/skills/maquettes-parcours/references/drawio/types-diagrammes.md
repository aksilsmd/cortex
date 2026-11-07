# draw.io : préréglages par type de diagramme

> Traduit et adapté de `Agents365-ai/drawio-skill`, `skills/drawio-skill/references/diagram-types.md`, commit `1f59eae2ca47`. © 2026 Agents365-ai, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire quand un type de diagramme est demandé en `.drawio` (BPMN 2.0 complet, couloirs, ER, classes, séquence, C4, réseau). Mermaid reste le format par défaut (`../schemas-mermaid.md`) ; draw.io sert quand Mermaid ne suffit pas (pools et flux de messages BPMN normés, échange avec un outil BPM, mise en page fine). Ces préréglages fixent la **structure** ; les couleurs suivent le thème du projet (`../theme-design-system.md`). Tout est écrit à la main : aucun générateur ni script.

## Sommaire
1. BPMN 2.0
2. Logigramme inter-fonctions (couloirs)
3. Logigramme
4. Entités-relations
5. Classes UML
6. Séquence
7. C4
8. Architecture par couches
9. Topologie réseau
10. Contrôles avant de rendre

## 1. BPMN 2.0

draw.io fournit environ 200 formes BPMN natives (`mxgraph.bpmn.*`). Les styles officiels portent une longue liste `points=[...]` de points d'accroche ; on l'omet ici, le rendu reste correct.

| Élément | Style | Notes |
|---|---|---|
| Pool | `swimlane;html=1;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;collapsible=0;` | conteneur ; libellé dans le bandeau gauche |
| Couloir | `swimlane;html=1;startSize=30;horizontal=0;collapsible=0;fillColor=none;` | enfant du pool, un par rôle |
| Tâche | `shape=mxgraph.bpmn.task2;whiteSpace=wrap;rectStyle=rounded;size=10;html=1;container=1;expand=0;collapsible=0;taskMarker=abstract;` | `taskMarker=user\|service\|script\|manual\|send\|receive\|businessRule` |
| Événement de début | `shape=mxgraph.bpmn.event;html=1;perimeter=ellipsePerimeter;aspect=fixed;outline=standard;symbol=general;verticalLabelPosition=bottom;verticalAlign=top;align=center;labelBackgroundColor=#ffffff;` 50×50 | `symbol=message\|timer` |
| Événement intermédiaire | idem, `outline=throwing` (émis) ou `outline=catching` (reçu) | double cercle |
| Événement de fin | idem, `outline=end;symbol=general` | `symbol=terminate` pour une fin terminale |
| Passerelle | `shape=mxgraph.bpmn.gateway2;html=1;perimeter=rhombusPerimeter;outline=none;symbol=none;gwType=exclusive;verticalLabelPosition=bottom;verticalAlign=top;align=center;labelBackgroundColor=#ffffff;` 50×50 | `gwType=exclusive\|parallel\|inclusive\|complex` |
| Flux de séquence | `edgeStyle=elbowEdgeStyle;html=1;endArrow=blockThin;endFill=1;` | plein |
| Flux conditionnel | idem + `startArrow=diamondThin;startFill=0;startSize=10;endSize=6;` | losange creux à la source |
| Flux par défaut | idem + `startArrow=dash;startFill=0;startSize=6;endSize=6;` | trait à la source |
| Flux de message | `dashed=1;dashPattern=8 4;endArrow=blockThin;endFill=1;startArrow=oval;startFill=0;startSize=4;endSize=6;html=1;` | seulement **entre** pools |
| Objet de données | `shape=mxgraph.bpmn.data2;size=15;html=1;verticalLabelPosition=bottom;verticalAlign=top;align=center;` 40×60 | association en pointillé |
| Annotation | `html=1;shape=mxgraph.flowchart.annotation_2;align=left;labelPosition=right;` | crochet ouvert |

Mise en page : de gauche à droite dans les couloirs, événements et passerelles centrés sur la ligne du flux. Un flux de séquence ne franchit jamais le bord d'un pool ; un flux de message ne reste jamais dans un seul pool. Chaque tâche porte l'identifiant de règle ou d'étape (`RG-`, `WF-`) de `../workflows-fonctionnels.md`.

## 2. Logigramme inter-fonctions (couloirs)

Qui fait quoi : un couloir par rôle, service ou système. Pool et couloirs : styles du §1. Les étapes reprennent le §3, avec `parent` = identifiant du couloir et coordonnées relatives. Les passages de main sont les connecteurs qui changent de couloir (`edgeStyle=orthogonalEdgeStyle;html=1;rounded=1;`) : c'est l'objet du schéma. Flux de gauche à droite, chaque étape dans le couloir de son acteur, 160 px au moins entre étapes.

## 3. Logigramme

| Élément | Style | Notes |
|---|---|---|
| Début / fin | `ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;` | ovale vert |
| Traitement | `rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;` | rectangle bleu |
| Décision | `rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;` | losange jaune |
| Entrée-sortie | `shape=parallelogram;perimeter=parallelogramPerimeter;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;` | orange |
| Sous-processus | `shape=process;whiteSpace=wrap;html=1;fillColor=#e1d5e7;strokeColor=#9673a6;` | violet, double bord |

Toujours libeller les branches d'une décision (« Oui », « Non »). De haut en bas, 200 px d'écart vertical ; les décisions s'ouvrent à gauche et à droite puis reviennent au centre.

## 4. Entités-relations

| Élément | Style | Notes |
|---|---|---|
| Table | `shape=table;startSize=30;container=1;collapsible=1;childLayout=tableLayout;fixedRows=1;rowLines=0;fontStyle=1;strokeColor=#6c8ebf;fillColor=#dae8fc;` | conteneur |
| Ligne (colonne) | `shape=tableRow;horizontal=0;startSize=0;swimlaneHead=0;swimlaneBody=0;fillColor=none;collapsible=0;dropTarget=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;fontSize=12;` | `parent` = table |
| Clé primaire | `fontStyle=1` sur la ligne, préfixe `PK` | |
| Clé étrangère | `dashed=1;endArrow=ERmandOne;startArrow=ERmandOne;` | notation patte d'oie |

Haut en bas, tables à 300 px, tables liées regroupées. Le schéma de référence reste celui de `architecture-normes/references/donnees-schema.md`.

## 5. Classes UML

| Élément | Style |
|---|---|
| Classe | `swimlane;fontStyle=1;align=center;startSize=26;html=1;` (titre, attributs, méthodes) |
| Séparateur | `line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=10;rotatable=0;labelPosition=left;points=[];portConstraint=eastwest;` |
| Héritage | `endArrow=block;endFill=0;` |
| Réalisation | `endArrow=block;endFill=0;dashed=1;` |
| Composition | `endArrow=diamondThin;endFill=1;` |
| Agrégation | `endArrow=diamondThin;endFill=0;` |

Haut en bas, 250 px entre classes, interfaces au-dessus des implémentations.

## 6. Séquence

| Élément | Style |
|---|---|
| Participant | `shape=umlLifeline;perimeter=lifelinePerimeter;whiteSpace=wrap;html=1;container=1;collapsible=0;recursiveResize=0;outlineConnect=0;portConstraint=eastwest;` |
| Message synchrone | `html=1;verticalAlign=bottom;endArrow=block;` |
| Message asynchrone | `html=1;verticalAlign=bottom;endArrow=open;dashed=1;` |
| Retour | `html=1;verticalAlign=bottom;endArrow=open;dashed=1;strokeColor=#999999;` |

Lignes de vie à 200 px, le temps descend. Placer la géométrie à la main est fastidieux : préférer `sequenceDiagram` en Mermaid (`../schemas-mermaid.md` §4) sauf besoin de mise en page fine.

## 7. C4

| Élément | Style |
|---|---|
| Personne | `shape=mxgraph.c4.person2;html=1;whiteSpace=wrap;fontColor=#ffffff;fillColor=#083F75;strokeColor=#06315C;` 200×180 |
| Système | `rounded=1;arcSize=10;html=1;whiteSpace=wrap;fontColor=#ffffff;fillColor=#1061B0;strokeColor=#0D5091;` 240×120 |
| Système externe | idem, `fillColor=#8C8496;strokeColor=#736782;` |
| Conteneur | idem, `fillColor=#23A2D9;strokeColor=#0E7DAD;` |
| Composant | idem, `fillColor=#63BEF2;strokeColor=#2086C9;` |
| Base | `shape=cylinder3;size=15;boundedLbl=1;` + couleurs du conteneur |
| Relation | `endArrow=blockThin;endFill=1;html=1;fontSize=11;fontColor=#404040;strokeColor=#828282;labelBackgroundColor=#ffffff;` |

Libellé sur trois lignes : nom, `[Type : techno]`, description. Une page (`<diagram>`) par niveau. Règles de contenu : `architecture-normes/references/c4-ddd-hexagonal.md`.

## 8. Architecture par couches

Couches (client, API, services, données) en `swimlane;startSize=30;`. Service : `rounded=1;whiteSpace=wrap;html=1;`. Base : `shape=cylinder3;`. File ou bus : jaune (`fillColor=#fff2cc;strokeColor=#d6b656;`), au centre. Système externe : `rounded=1;dashed=1;fillColor=#f5f5f5;strokeColor=#666666;`. Haut en bas à partir de quatre couches.

## 9. Topologie réseau

Bibliothèque `mxgraph.networks`. Préfixe commun : `fontColor=#0066CC;verticalAlign=top;verticalLabelPosition=bottom;labelPosition=center;align=center;html=1;outlineConnect=0;fillColor=#CCCCCC;strokeColor=#6881B3;gradientColor=none;strokeWidth=2;` puis `shape=mxgraph.networks.router|switch|firewall|load_balancer|server|storage|pc|laptop|cloud;`. Zone (sous-réseau, DMZ) : `rounded=1;dashed=1;fillColor=#f5f5f5;strokeColor=#666666;verticalAlign=top;fontStyle=1;container=1;`, libellé = CIDR. Lien physique `html=1;endArrow=none;strokeWidth=2;` ; lien logique ou VPN en pointillé. De haut en bas : Internet, bordure, distribution, serveurs.

## 10. Contrôles avant de rendre

- Le type choisi est justifié (Mermaid insuffisant) et le fichier `.drawio` est versionné à côté de son export.
- BPMN : aucun flux de séquence entre pools, aucun flux de message dans un pool, toute passerelle libellée.
- Chaque élément renvoie à un identifiant du projet ; légende présente dès trois couleurs (`redaction-xml.md` §6).
