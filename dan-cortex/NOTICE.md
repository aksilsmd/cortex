# NOTICE — contenus tiers intégrés à Dan-Cortex

Dan-Cortex intègre des textes tiers traduits et adaptés (forme B limitée de `skills/robustesse-agents/references/renfort-externe.md` §1), sans aucun script, hook ni appel réseau. Chaque dossier vendorisé porte son propre `NOTICE.md` avec le texte complet de la licence, le commit source, les fichiers repris et les modifications. Les apports de forme A (méthodes réécrites, aucun texte repris) sont listés dans `renfort-externe.md` §8 et dans les fiches `references/sources/` des skills.

| Dossier | Dépôt amont | Titulaire | Licence | Commit | Fichiers repris | NOTICE détaillée |
|---|---|---|---|---|---|---|
| `skills/maquettes-parcours/references/drawio/` | https://github.com/Agents365-ai/drawio-skill | © 2026 Agents365-ai | MIT | `1f59eae2ca4740ed72a195279469fb58fa39d9e0` | `references/shapes.md`, `diagram-types.md`, `xml-authoring.md` | `skills/maquettes-parcours/references/drawio/NOTICE.md` |
| `skills/architecture-normes/references/ddd-hexagonal/` | https://github.com/ccheney/robust-skills | © 2026 robust-skills contributors | MIT | `0eea7b060d12e3520556a73b15fbfa79480987d1` | `skills/clean-ddd-hexagonal/SKILL.md`, `references/DDD-TACTICAL.md`, `HEXAGONAL.md`, `CQRS-EVENTS.md` | `skills/architecture-normes/references/ddd-hexagonal/NOTICE.md` |
| `bibliotheque/scenario-labs/` | https://github.com/scenario-labs/skills | © 2026 Scenario Inc. | MIT | `221ed89562795d4a7095c9530cf807062e7ad8d3` | `skills/` complet (172 skills, références, scripts), non traduit | `bibliotheque/scenario-labs/NOTICE.md` |
| `bibliotheque/scroll-world/` | https://github.com/oso95/scroll-world | © 2026 cyw | MIT | `71cc36d3bb150248ae36a2c552f9cbf88802a79c` | `skills/scroll-world/` complet, non traduit | `bibliotheque/scroll-world/NOTICE.md` |

Modifications communes : traduction en français ; adaptation au format Dan-Cortex (références chargées à la demande, au plus 1 500 mots, contrôles avant de rendre) ; suppression de tout script, appel réseau, URL d'encodage de diagramme, icône par CDN et consigne absolue. Détail par dossier dans sa NOTICE.

Toutes ces licences sont la licence MIT ; leur texte complet, avec la mention de copyright de chaque titulaire, figure dans la NOTICE de chaque dossier, comme l'exige la licence. Décision d'origine : PV « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042), lot 5. Retrait : `renfort-externe.md` §7 (supprimer le dossier, ses renvois et la ligne ci-dessus ; supprimer ce fichier si plus aucun lot B ne subsiste).

**Bibliothèque (2026-11-21).** Les deux dossiers de `bibliotheque/` sont des copies fidèles, non traduites, scripts compris, à la demande expresse d'Aksil (« ajouter toutes les compétences de ces dépôts »). Ils restent hors de `skills/` (aucun chargement automatique) ; leurs scripts ne s'exécutent jamais sans lecture et accord explicite. Les dépôts GPL, AGPL ou sans licence du même renfort (Blender, BlenderGIS, Canvas LMS, 3d-portfolio) ne sont repris qu'en forme A, sans texte ni code : voir `skills/*/references/sources.md` des skills `studio-3d-jeu`, `web-3d-immersif`, `plateforme-elearning`, `reconstruction-salle-blanche`, `creation-medias-ia`.
