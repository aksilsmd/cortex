# draw.io : écrire le XML d'un fichier .drawio

> Traduit et adapté de `Agents365-ai/drawio-skill`, `skills/drawio-skill/references/xml-authoring.md`, commit `1f59eae2ca47`. © 2026 Agents365-ai, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire avant d'écrire à la main un fichier `.drawio`. Formes : `formes.md` ; préréglages : `types-diagrammes.md`. Le fichier se produit et se rend **localement** : aucun lien de partage qui encode le diagramme dans une URL, aucun service en ligne.

## Sommaire
1. Squelette
2. Formes
3. Conteneurs
4. Connecteurs
5. Répartir les connexions
6. Couleurs et légende
7. Mise en page
8. Pièges vérifiés au rendu
9. Contrôles avant de rendre

## 1. Squelette

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="drawio" version="26.0.0">
  <diagram name="Page-1">
    <mxGraphModel>
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <!-- les formes commencent à id="2" -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

- Les cellules `id="0"` et `id="1"` sont obligatoires.
- Les formes commencent à `id="2"` et se suivent ; `parent="1"` sauf dans un conteneur (identifiant du conteneur).
- `html=1` dans le style de toute cellule avec du texte.
- Jamais `--` dans un commentaire XML : c'est interdit par la norme et casse la lecture.
- Échapper dans les attributs : `&amp;`, `&lt;`, `&gt;`, `&quot;`.
- Retour à la ligne dans un libellé : `&#xa;` (pas `\n`), par exemple `value="Ligne 1&#xa;Ligne 2"`.
- Export SVG destiné au web : ajouter `convertToSvg=1;` au style des cellules à texte (draw.io 28.0.3 ou plus) pour obtenir du texte SVG sélectionnable. Tableaux, listes, liens, images, fonds colorés et écriture verticale restent en HTML. Le texte SVG ne se replie pas (sauf 29.6.7 ou plus) : réexporter après tout redimensionnement.

## 2. Formes

```xml
<mxCell id="2" value="Catalogue" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="60" as="geometry" />
</mxCell>
<mxCell id="3" value="Base" style="shape=cylinder3;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#333333;" vertex="1" parent="1">
  <mxGeometry x="350" y="100" width="120" height="80" as="geometry" />
</mxCell>
<mxCell id="4" value="Stock suffisant ?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="1">
  <mxGeometry x="100" y="220" width="160" height="80" as="geometry" />
</mxCell>
```

## 3. Conteneurs

Pour imbriquer, utiliser la relation parent-enfant ; ne pas poser une forme sur une plus grande. Types : `formes.md` §4. Ajouter `pointerEvents=0;` au conteneur qui ne doit pas capter les connexions de ses enfants. Les enfants portent `parent="<id du conteneur>"` et des coordonnées relatives.

```xml
<mxCell id="svc1" value="Service Commande" style="swimlane;startSize=30;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
<mxCell id="api1" value="API REST" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="svc1">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

## 4. Connecteurs

Toute arête contient un enfant `<mxGeometry relative="1" as="geometry" />`. Une arête auto-fermante (`<mxCell ... edge="1" />`) est invalide et ne s'affiche pas.

```xml
<mxCell id="10" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="4">
  <mxGeometry relative="1" as="geometry">
    <Array as="points"><mxPoint x="500" y="50" /></Array>
  </mxGeometry>
</mxCell>
```

- Inclure `rounded=1;orthogonalLoop=1;jettySize=auto` : routage qui évite les chevauchements.
- Fixer `exitX/exitY/entryX/entryY` sur chaque arête dès qu'un nœud a deux connexions ou plus.
- Points de passage (`<Array as="points">`) quand l'arête doit contourner une forme.
- Dernier segment droit d'au moins 20 px avant la cible, sinon la pointe chevauche le coude.
- `flowAnimation=1;` anime le flux (export SVG et draw.io de bureau).
- Un diagramme dense garde des croisements : l'ouvrir une fois dans draw.io de bureau, mise à jour automatique coupée (voir `../schemas-mermaid.md` §9), et laisser son routeur de connecteurs retracer. Ne pas cumuler deux routeurs.

## 5. Répartir les connexions

| Position | exitX/entryX | exitY/entryY | Quand |
|---|---|---|---|
| Haut centre | 0.5 | 0 | nœud au-dessus |
| Haut gauche / droite | 0.25 / 0.75 | 0 | 2e et 3e connexions par le haut |
| Droite centre | 1 | 0.5 | nœud à droite |
| Bas centre | 0.5 | 1 | nœud en dessous |
| Gauche centre | 0 | 0.5 | nœud à gauche |

N connexions sur un côté : les espacer régulièrement (trois en bas : 0.25, 0.5, 0.75).

## 6. Couleurs et légende

Palette par défaut, quand le thème du projet n'en fixe pas (`../theme-design-system.md` prime) :

| Couleur | fillColor | strokeColor | Usage |
|---|---|---|---|
| Bleu | `#dae8fc` | `#6c8ebf` | services, clients |
| Vert | `#d5e8d4` | `#82b366` | succès, bases |
| Jaune | `#fff2cc` | `#d6b656` | files, décisions |
| Orange | `#ffe6cc` | `#d79b00` | passerelles, API |
| Rouge | `#f8cecc` | `#b85450` | erreurs, alertes |
| Gris | `#f5f5f5` | `#666666` | externe, neutre |
| Violet | `#e1d5e7` | `#9673a6` | sécurité, authentification |

Dès trois couleurs de sens, ajouter une légende : un conteneur dans un coin libre, une pastille de 30×16 et un libellé de rôle par couleur **réellement utilisée**, pas de 24 px, hauteur `30 + 24 × lignes`. Jamais d'entrée inventée ; pas de légende pour un schéma d'une seule couleur.

## 7. Mise en page

| Complexité | Nœuds | Écart horizontal | Écart vertical |
|---|---|---|---|
| Simple | 5 ou moins | 200 px | 150 px |
| Moyenne | 6 à 10 | 280 px | 200 px |
| Complexe | plus de 10 | 350 px | 250 px |

- Laisser un couloir vide d'environ 80 px entre rangées et colonnes pour les arêtes ; n'y poser aucune forme.
- Aligner `x`, `y`, `width`, `height` sur des multiples de 10.
- Placer la grille avant les coordonnées ; regrouper les nœuds liés sur une même bande.
- Nœuds très connectés au centre ; un enfant centré sous son parent pour éviter les obliques.
- Bus d'événements au milieu de la rangée des services, pas en dessous : liaisons horizontales courtes, sans croisement.
- Arbre : relier seulement des rangées voisines. Étoile : satellites autour du centre. Arête longue : par le couloir extérieur.
- Suivre chaque arête de tête avant de figer : si elle traverse une forme, déplacer la forme ou ajouter un point de passage.

## 8. Pièges vérifiés au rendu

| Piège | Règle |
|---|---|
| Sortie latérale d'un losange qui repart vers l'intérieur : le coude traverse le losange | une sortie de sommet part vers l'extérieur. Si les deux cibles sont en dessous, tracer deux droites (`edgeStyle=none`) depuis `exitX=0.25;exitY=0.75` et `exitX=0.75;exitY=0.75` vers le haut de chaque cible |
| `entryX` décalé de 1 ou 2 px par rapport à la sortie : double courbe avant la pointe | calculer `entryX = (centreX source − x cible) / largeur cible`, avec plus de deux décimales |
| Pointe `blockThin` collée au bord : lue comme « perce la boîte » | `endArrow=block;endSize=8` sur les flux principaux |
| Libellé long centré sur l'arête : il la coupe | garder sur la ligne les seuls « Oui » / « Non » ; décaler les autres (`<mxPoint as="offset" x="…" y="…"/>`) vers un espace vide, ou les raccourcir |
| Se fier à « ça a l'air bon » | exporter localement en SVG ou PNG et regarder l'export à 100 % ; une relecture visuelle seule peut manquer ou inventer des défauts |

## 9. Contrôles avant de rendre

- Le fichier s'ouvre sans erreur et s'exporte localement ; l'export est versionné avec le `.drawio`.
- Aucune arête auto-fermante, aucun `--` dans un commentaire, aucune URL.
- Pièges du §8 vérifiés sur l'export, pas de mémoire.
