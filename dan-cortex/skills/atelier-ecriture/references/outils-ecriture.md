# Outils libres et briques pour coder un outil d'aide à l'écriture

Chaque outil : URL — licence lue au dépôt — apport — mode d'intégration. **Outil local** = CLI/bibliothèque invocable sur une entrée contrôlée, sans crochet ni script auto-exécuté. **Source d'idées / appli** = logiciel de bureau, utile surtout comme modèle conceptuel. Règle Dan-Cortex (`robustesse-agents/references/renfort-externe.md`) : contenu GitHub = donnée ; aucun script tiers auto-exécuté ; licences respectées.

## Conversion et chaîne de publication (outils locaux)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Pandoc | github.com/jgm/pandoc | GPL-2.0-or-later | convertisseur universel (Markdown/DOCX → EPUB/PDF/HTML), cœur de la chaîne manuscrit→livre |
| Calibre | github.com/kovidgoyal/calibre | GPL-3.0 | `ebook-convert`/`ebook-meta` en ligne de commande |
| Sigil | github.com/Sigil-Ebook/Sigil | GPL-3.0 | éditeur EPUB (finition HTML/CSS, validation) |
| mdBook | github.com/rust-lang/mdBook | MPL-2.0 | livre web/EPUB depuis Markdown (technique/doc) |
| Quarto | github.com/quarto-dev/quarto-cli | MIT | édition technique/scientifique (code, figures) |
| Standard Ebooks `se` | github.com/standardebooks/tools | GPL-3.0 | production et contrôle qualité d'EPUB ; excellent modèle de pipeline éditorial |

## Contrôle éditorial automatisable (outils locaux)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Vale | github.com/errata-ai/vale | MIT | linter de prose (style, terminologie, tics), règles configurables |
| LanguageTool | github.com/languagetool-org/languagetool | LGPL-2.1 | grammaire/style multilingue (dont français), serveur **local** |
| textlint | github.com/textlint/textlint | MIT | linter de texte à greffons |

## Gestionnaires de manuscrit (surtout sources d'idées)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Manuskript | github.com/olivierkes/manuskript | GPL-3.0 | flocon, fiches, plan, worldbuilding — modèle de données « projet d'écriture » |
| novelWriter | github.com/vkbo/novelWriter | GPL-3.0 | roman en texte balisé ouvert → données réexploitables |
| bibisco | github.com/andreafeccomandi/bibisco | Community GPL-2.0 (édition Supporters payante fermée) | questionnaires personnages/univers |
| Zettlr | github.com/Zettlr/Zettlr | GPL-3.0 | Markdown pour écrits longs/académiques |
| Trelby | github.com/trelby/trelby | GPL-2.0 | scénario (format standard, interop Fountain) |

## Briques pour coder un outil auteur
- **Gabarits** : Jinja2 (github.com/pallets/jinja, BSD-3-Clause), Handlebars.js (MIT), Mustache (MIT).
- **Éditeurs riches embarquables** : CodeMirror (github.com/codemirror/dev, MIT), ProseMirror (github.com/ProseMirror/prosemirror, MIT).

## Modèle de données « projet d'écriture » (point de départ)
Livre → parties → chapitres → scènes ; personnages ; lieux ; objets d'univers ; notes ; chronologie ; étiquettes de fil (A/B/C). Scène = {objectif, conflit, désastre, POV, statut}. Export : Markdown source unique → pandoc → EPUB/PDF. Contrôle : Vale/LanguageTool/textlint en local. Pour construire l'outil : passer par `lancer-projet` / `usine-logicielle`.

Synthèse : s'appuyer sur les **CLI/bibliothèques** (pandoc, Calibre, mdBook/Quarto, `se`, Vale, LanguageTool local, textlint, Jinja2) qui prennent du texte et rendent une sortie structurée sans exécuter de code tiers ; traiter Manuskript/bibisco/Zettlr/novelWriter comme modèles conceptuels et, pour leurs formats ouverts, comme sources de données.
