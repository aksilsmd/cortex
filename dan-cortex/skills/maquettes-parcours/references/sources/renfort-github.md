# Sources — renfort externe (schemas-mermaid.md)

Dépôts consultés en lecture seule le 2026-11-03 (clone superficiel, aucun script exécuté). Méthodes reformulées en français ; aucun texte copié. Forme A de la décision « renfort GitHub » (projet Parapro, DEC-042). Procédure de mise à jour et propriétaire : `robustesse-agents/references/renfort-externe.md`.

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/ccheney/robust-skills | MIT, © 2026 robust-skills contributors | `0eea7b060d12` | `skills/mermaid-diagrams/references/STATE-JOURNEY.md`, `SEQUENCE.md`, `CLASS-ER.md`, `ARCHITECTURE.md` | conventions réécrites |
| https://github.com/softaworks/agent-toolkit | MIT, © 2026 Leonardo Flores | `3027f20f3181` | `skills/mermaid-diagrams`, `skills/c4-architecture` | conventions réécrites |
| https://github.com/Agents365-ai/drawio-skill | MIT, © 2026 Agents365-ai | `1f59eae2ca47` | `skills/drawio-skill/references/diagram-types.md`, `shapes.md` (BPMN) | idées seulement ; aucun script |
| https://github.com/Agents365-ai/drawio-skill (lot B) | MIT, © 2026 Agents365-ai | `1f59eae2ca4740ed72a195279469fb58fa39d9e0` | `skills/drawio-skill/references/shapes.md`, `diagram-types.md`, `xml-authoring.md` | texte traduit et adapté, sans script : `drawio/` (voir `drawio/NOTICE.md`) |

Exclus pour ce skill : tout hook, script, serveur ou appel réseau des dépôts ci-dessus (condition 1 de la décision).

## Ajout du 2026-11-07 — skill `design-apple` (forme A)

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/ehmo/platform-design-skills | MIT, © 2026 (fichier LICENSE) | `dc2be825d8b439caea78e9eaa8fb3ac23b0ff3e9` | `skills/web/SKILL.md`, `skills/ios/SKILL.md`, `skills/ipados/SKILL.md`, `skills/macos/SKILL.md` | règles réécrites en français : `design-apple/references/regles-web-mobile.md`, `regles-grand-ecran.md` |

Exclus : `Apple_HIG.pdf` (texte d'Apple protégé, non redistribué), skills Android/tvOS/watchOS/visionOS (hors besoin), tout fichier `AGENTS.md`/`CLAUDE.md` du dépôt. Filtres §3 : licence MIT présente ; aucun hook, script ni appel réseau ; caractères invisibles recherchés (aucun) ; aucune consigne absolue reprise.

## Ajout du 2026-11-07 — web mobile, prototypes, bibliothèques d'interface (forme A)

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/emilkowalski/skills | MIT, © 2026 Emil Kowalski (fichier LICENSE) | `c8a79627b59d72d764d6ab6f2c87c09a48169833` | `skills/mobile-native/SKILL.md`, `ui-cheatsheet.md` | méthode réécrite en français : `references/web-mobile-natif.md` |
| idem | idem | idem | `skills/prototype/SKILL.md`, `skills/prototype/PICKER.md` | `references/prototypes-en-variantes.md` (contrat du sélecteur décrit, ni balisage ni code repris) |
| idem | idem | idem | `skills/pick-ui-library/SKILL.md`, `skills/ask-sonner/SKILL.md` (installation, appels, style) | `references/choisir-une-bibliotheque-ui.md` (licences et poids ajoutés par Dan-Cortex, à revérifier) |

Exclus : sections « Initial Response », consigne de reprise à l'identique du sélecteur, consigne de s'en tenir à la liste, `ask-sonner/API.md`, deux bibliothèques à licence non vérifiée. Le skill `design-apple` renvoie désormais, pour le mouvement, vers `mouvement-interface/references/mouvement-fluide-apple.md` (fiche : `mouvement-interface/references/sources/renfort-github.md`). Filtres §3 : licence MIT lue ; aucun hook ni script ; caractères invisibles recherchés dans les fichiers reformulés (aucun).
