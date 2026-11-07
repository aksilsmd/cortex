# NOTICE — contenus tiers intégrés à Dan-Cortex

Dan-Cortex intègre des textes tiers traduits et adaptés (forme B limitée de `skills/robustesse-agents/references/renfort-externe.md` §1), sans aucun script, hook ni appel réseau. Chaque dossier vendorisé porte son propre `NOTICE.md` avec le texte complet de la licence, le commit source, les fichiers repris et les modifications. Les apports de forme A (méthodes réécrites, aucun texte repris) sont listés dans `renfort-externe.md` §8 et dans les fiches `references/sources/` des skills.

| Dossier | Dépôt amont | Titulaire | Licence | Commit | Fichiers repris | NOTICE détaillée |
|---|---|---|---|---|---|---|
| `skills/maquettes-parcours/references/drawio/` | https://github.com/Agents365-ai/drawio-skill | © 2026 Agents365-ai | MIT | `1f59eae2ca4740ed72a195279469fb58fa39d9e0` | `references/shapes.md`, `diagram-types.md`, `xml-authoring.md` | `skills/maquettes-parcours/references/drawio/NOTICE.md` |
| `skills/architecture-normes/references/ddd-hexagonal/` | https://github.com/ccheney/robust-skills | © 2026 robust-skills contributors | MIT | `0eea7b060d12e3520556a73b15fbfa79480987d1` | `skills/clean-ddd-hexagonal/SKILL.md`, `references/DDD-TACTICAL.md`, `HEXAGONAL.md`, `CQRS-EVENTS.md` | `skills/architecture-normes/references/ddd-hexagonal/NOTICE.md` |

Modifications communes : traduction en français ; adaptation au format Dan-Cortex (références chargées à la demande, au plus 1 500 mots, contrôles avant de rendre) ; suppression de tout script, appel réseau, URL d'encodage de diagramme, icône par CDN et consigne absolue. Détail par dossier dans sa NOTICE.

Les deux licences sont la licence MIT ; leur texte complet, avec la mention de copyright de chaque titulaire, figure dans la NOTICE de chaque dossier, comme l'exige la licence. Décision d'origine : PV « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042), lot 5. Retrait : `renfort-externe.md` §7 (supprimer le dossier, ses renvois et la ligne ci-dessus ; supprimer ce fichier si plus aucun lot B ne subsiste).
