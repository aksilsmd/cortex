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

**Dossiers de l'exception du 12/11/2026 (copie telle quelle, scripts compris)** : `docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`, `slack-gif-creator`, `algorithmic-art`, `claude-api`, `academy-guide`, `brand-guidelines`, même dépôt et même commit, avec `THIRD_PARTY_NOTICES.md` à la racine du plugin. **État : copie non faite à la date de ce fichier** (voir `skills/lancer-projet/references/skills-officiels-anthropic.md` §1) ; à consigner ici dès qu'elle l'est, une ligne par dossier. Leurs scripts s'exécutent sur la machine de l'utilisateur.

Apache-2.0 : le texte complet de la licence figure dans le `LICENSE.txt` de chaque dossier (copie du fichier amont) ; les fichiers modifiés (traduits) portent l'avis de modification de leur `NOTICE.md`, comme l'exige l'article 4 b.

Modifications communes : traduction en français ; adaptation au format Dan-Cortex (références chargées à la demande, au plus 1 500 mots, contrôles avant de rendre) ; suppression de tout script, appel réseau, URL d'encodage de diagramme, icône par CDN et consigne absolue. Détail par dossier dans sa NOTICE.

Les deux licences sont la licence MIT ; leur texte complet, avec la mention de copyright de chaque titulaire, figure dans la NOTICE de chaque dossier, comme l'exige la licence. Décision d'origine : PV « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042), lot 5. Retrait : `renfort-externe.md` §7 (supprimer le dossier, ses renvois et la ligne ci-dessus ; supprimer ce fichier si plus aucun lot B ne subsiste).
