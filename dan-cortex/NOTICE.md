# NOTICE — contenus tiers intégrés à Dan-Cortex

Dan-Cortex intègre des textes tiers traduits et adaptés (forme B limitée de `skills/robustesse-agents/references/renfort-externe.md` §1), sans aucun script, hook ni appel réseau. Chaque dossier vendorisé porte son propre `NOTICE.md` avec le texte complet de la licence, le commit source, les fichiers repris et les modifications. Les apports de forme A (méthodes réécrites, aucun texte repris) sont listés dans `renfort-externe.md` §8 et dans les fiches `references/sources/` des skills.

| Dossier | Dépôt amont | Titulaire | Licence | Commit | Fichiers repris | NOTICE détaillée |
|---|---|---|---|---|---|---|
| `skills/maquettes-parcours/references/drawio/` | https://github.com/Agents365-ai/drawio-skill | © 2026 Agents365-ai | MIT | `1f59eae2ca4740ed72a195279469fb58fa39d9e0` | `references/shapes.md`, `diagram-types.md`, `xml-authoring.md` | `skills/maquettes-parcours/references/drawio/NOTICE.md` |
| `skills/architecture-normes/references/ddd-hexagonal/` | https://github.com/ccheney/robust-skills | © 2026 robust-skills contributors | MIT | `0eea7b060d12e3520556a73b15fbfa79480987d1` | `skills/clean-ddd-hexagonal/SKILL.md`, `references/DDD-TACTICAL.md`, `HEXAGONAL.md`, `CQRS-EVENTS.md` | `skills/architecture-normes/references/ddd-hexagonal/NOTICE.md` |
| `skills/conception-interface/` | https://github.com/anthropics/skills | © 2026 Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/frontend-design/SKILL.md`, `LICENSE.txt` | `skills/conception-interface/NOTICE.md` |
| `skills/communication-interne/` | https://github.com/anthropics/skills | © 2026 Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/internal-comms/SKILL.md`, `examples/` (4 fichiers), `LICENSE.txt` | `skills/communication-interne/NOTICE.md` |
| `skills/fabrique-themes/` | https://github.com/anthropics/skills | © 2026 Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/theme-factory/SKILL.md`, `themes/` (10 fichiers), `LICENSE.txt` (hors PDF) | `skills/fabrique-themes/NOTICE.md` |
| `skills/design-affiche/` | https://github.com/anthropics/skills | © 2026 Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/canvas-design/SKILL.md`, `LICENSE.txt` (hors `canvas-fonts`, OFL) | `skills/design-affiche/NOTICE.md` |
| `skills/vigilance-discernement/` | https://github.com/anthropics/skills | © 2026 Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/discernment-nudge/SKILL.md`, `LICENSE.txt` | `skills/vigilance-discernement/NOTICE.md` |

**Dossiers de l'exception du 12/11/2026 (copie telle quelle, scripts compris)** : `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`, `slack-gif-creator`, `algorithmic-art`, `claude-api`, `academy-guide`, `brand-guidelines`, même dépôt et même commit, avec `THIRD_PARTY_NOTICES.md` à la racine du plugin. **État : copie faite le 12/11/2026 (version 2.1.0).** Leurs scripts s'exécutent sur la machine de l'utilisateur. Seule modification : la description de `brand-guidelines` est préfixée (exemple d'Anthropic, à ne pas appliquer aux projets des clients).

| Dossier | Dépôt amont | Titulaire | Licence | Commit | Fichiers repris | Licence complète |
|---|---|---|---|---|---|---|
| `skills/docx/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/docx/` en entier, sans modification | `skills/docx/LICENSE.txt` |
| `skills/pdf/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/pdf/` en entier, sans modification | `skills/pdf/LICENSE.txt` |
| `skills/pptx/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/pptx/` en entier, sans modification | `skills/pptx/LICENSE.txt` |
| `skills/xlsx/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/xlsx/` en entier, sans modification | `skills/xlsx/LICENSE.txt` |
| `skills/skill-creator/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/skill-creator/` en entier, sans modification | `skills/skill-creator/LICENSE.txt` |
| `skills/mcp-builder/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/mcp-builder/` en entier, sans modification | `skills/mcp-builder/LICENSE.txt` |
| `skills/webapp-testing/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/webapp-testing/` en entier, sans modification | `skills/webapp-testing/LICENSE.txt` |
| `skills/web-artifacts-builder/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/web-artifacts-builder/` en entier, sans modification | `skills/web-artifacts-builder/LICENSE.txt` |
| `skills/slack-gif-creator/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/slack-gif-creator/` en entier, sans modification | `skills/slack-gif-creator/LICENSE.txt` |
| `skills/algorithmic-art/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/algorithmic-art/` en entier, sans modification | `skills/algorithmic-art/LICENSE.txt` |
| `skills/claude-api/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/claude-api/` en entier, sans modification | `skills/claude-api/LICENSE.txt` |
| `skills/academy-guide/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/academy-guide/` en entier, sans modification | `skills/academy-guide/LICENSE.txt` |
| `skills/brand-guidelines/` | https://github.com/anthropics/skills | © Anthropic, PBC | Apache-2.0 | `2c5958ecac7cee2b583967a2c4981d0f4a75c579` | `skills/brand-guidelines/` en entier, sans modification | `skills/brand-guidelines/LICENSE.txt` |

**Bibliothèque (2026-11-21, version 2.2.0)** — copies fidèles, non traduites, scripts compris, à la demande d'Aksil (« ajouter toutes les compétences de ces dépôts »), rangées hors de `skills/` (aucun chargement automatique) ; leurs scripts ne s'exécutent jamais sans lecture et accord explicite :

| Dossier | Dépôt amont | Titulaire | Licence | Commit | Fichiers repris | NOTICE détaillée |
|---|---|---|---|---|---|---|
| `bibliotheque/scenario-labs/` | https://github.com/scenario-labs/skills | © 2026 Scenario Inc. | MIT | `221ed89562795d4a7095c9530cf807062e7ad8d3` | `skills/` complet (172 skills, références, scripts), non traduit ; famille Roblox rangée dans `game-engines-roblox/` (contenu inchangé) | `bibliotheque/scenario-labs/NOTICE.md` |
| `bibliotheque/scroll-world/` | https://github.com/oso95/scroll-world | © 2026 cyw | MIT | `71cc36d3bb150248ae36a2c552f9cbf88802a79c` | `skills/scroll-world/` complet, non traduit | `bibliotheque/scroll-world/NOTICE.md` |
| `bibliotheque/cli-anything/` | https://github.com/HKUDS/CLI-Anything | © 2026 HKUDS — Yuhao Yang, Tianyu Fan, Chao Huang | Apache-2.0 | `34f519533bc175d2fe287ab8316b0dd99bb9cc43` | `skills/` seul (70 compétences, aucun script), non traduit | `bibliotheque/cli-anything/NOTICE.md` |
| `bibliotheque/understand-anything/` | https://github.com/Egonex-AI/Understand-Anything | © 2026 Yuxiang Lin ; © 2026 Infinite Universe, Inc. | MIT | `17550efd7f70c9af683ce2b4bf0bd71f42593500` | `understand-anything-plugin/skills/` seul (9 compétences, 20 scripts d'analyse locale), non traduit | `bibliotheque/understand-anything/NOTICE.md` |

Les dépôts GPL, AGPL ou sans licence du même renfort (Blender, BlenderGIS, Canvas LMS, 3d-portfolio) ne sont repris qu'en forme A, sans texte ni code : voir `references/sources.md` des skills `studio-3d-jeu`, `web-3d-immersif`, `plateforme-elearning`, `reconstruction-salle-blanche`, `creation-medias-ia`.

Apache-2.0 : le texte complet de la licence figure dans le `LICENSE.txt` de chaque dossier (copie du fichier amont) ; les fichiers modifiés (traduits) portent l'avis de modification de leur `NOTICE.md`, comme l'exige l'article 4 b.

Modifications communes : traduction en français ; adaptation au format Dan-Cortex (références chargées à la demande, au plus 1 500 mots, contrôles avant de rendre) ; suppression de tout script, appel réseau, URL d'encodage de diagramme, icône par CDN et consigne absolue. Détail par dossier dans sa NOTICE.

MIT (`drawio/`, `ddd-hexagonal/`) : le texte complet de la licence, avec la mention de copyright de chaque titulaire, figure dans la NOTICE de chaque dossier, comme l'exige la licence. Décision d'origine : PV « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042), lot 5. Retrait : `renfort-externe.md` §7 (supprimer le dossier, ses renvois et la ligne ci-dessus ; supprimer ce fichier si plus aucun lot B ne subsiste).
