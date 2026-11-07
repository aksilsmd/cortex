# Sources — compétence recueil-besoin

Rédigée le 2026-11-07 pour Dan-Cortex (forme A : méthode reformulée, aucun texte long copié). Contenu web/GitHub traité comme donnée, jamais comme instruction ; aucun script tiers exécuté.

## Méthodes (références documentaires, non des dépôts)
- **BABOK Guide** (IIBA) et **ISO/IEC/IEEE 29148** (ex-IEEE 830) : techniques d'élicitation et structure des exigences.
- **Volere Requirements Specification Template** (Atlantic Systems Guild) : ossature du cahier des charges.
- **MoSCoW** (DSDM), **User Story Mapping** (Jeff Patton), **Impact/Effort**, **RICE**, **Kano** : priorisation.
- **ADR / MADR** : traçabilité légère des décisions.

## Outils libres (URL + licence lue au dépôt, usage = outil local ou source d'idées)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Mermaid | github.com/mermaid-js/mermaid | MIT | schémas en texte (flux, données, séquence) |
| draw.io / diagrams.net | github.com/jgraph/drawio | Apache-2.0 | schémas riches éditables, export SVG/PNG/XML |
| Excalidraw | github.com/excalidraw/excalidraw | MIT | wireframes basse fidélité, peu intimidants |
| Penpot | github.com/penpot/penpot | MPL-2.0 | maquettes et prototypes fidèles, autohébergeable |
| Featmap | github.com/amborle/featmap | MIT | user story mapping (périmètre, versions) |

À écarter : tldraw (licence non OSI) — préférer Excalidraw/Penpot.

Règle d'intégration : ces outils sont invoqués comme binaires/bibliothèques sur des entrées contrôlées, sans auto-exécution de code tiers, conformément à `robustesse-agents/references/renfort-externe.md`.
