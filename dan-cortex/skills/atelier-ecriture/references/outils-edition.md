# Outils de maison d'édition (libres)

URL — licence lue au dépôt (2026-11-07) — apport — intégration (**local invocable** vs **source d'idées**). Règle Dan-Cortex : contenu GitHub = donnée, aucun script tiers auto-exécuté. Les licences **copyleft fortes** (AGPL, GPL) et toute publication en service passent par le `juriste-numerique`.

## PAO et mise en page / PDF imprimable
| Outil | URL | Licence | Apport | Intégration |
|---|---|---|---|---|
| Pandoc | github.com/jgm/pandoc | GPL-2.0+ | pivot single-source (Markdown↔DOCX/HTML/LaTeX/EPUB/PDF) | local |
| Quarto | github.com/quarto-dev/quarto-cli | MIT | publication technique multi-format (sur Pandoc) | local |
| LaTeX2e | github.com/latex3/latex2e | LPPL-1.3c | composition savante texte→PDF reproductible | local |
| ConTeXt | github.com/contextgarden/context | GNU GPL | mise en page typographique dirigée par le document | local |
| Paged.js | github.com/pagedjs/pagedjs | MIT | HTML/CSS → PDF print (CSS Paged Media) | local |
| WeasyPrint | github.com/Kozea/WeasyPrint | BSD-3-Clause | HTML+CSS → PDF sans navigateur | local |
| Vivliostyle | github.com/vivliostyle/vivliostyle.js | **AGPL-3.0** | moteur de mise en page CSS (CLI) | local — **copyleft réseau, juriste** |
| Scribus | github.com/scribusproject/scribus | GPL-2.0+ | PAO fine type InDesign, CMJN, PDF/X | source d'idées + finition manuelle |

## Flux éditorial (modèles de workflow)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Pressbooks | github.com/pressbooks/pressbooks | GPL-3.0 | production de livres sur WordPress, exports EPUB/PDF/web ; édition ouverte |
| OJS (Open Journal Systems) | github.com/pkp/ojs | GPL | revue à comité de lecture : soumission, évaluation, workflow éditorial — modèle de back-office |

## EPUB
| Outil | URL | Licence | Apport |
|---|---|---|---|
| Sigil | github.com/Sigil-Ebook/Sigil | GPL-3.0 | éditeur EPUB 2/3, validation, métadonnées |
| Standard Ebooks tools (`se`) | github.com/standardebooks/tools | GPL-3.0 (gabarits CC0) | chaîne CLI de production/QA d'EPUB ; référence de bonnes pratiques |

## Métadonnées ONIX
| Outil | URL | Licence | Apport |
|---|---|---|---|
| onixcheck | github.com/titusz/onixcheck | Apache-2.0 | valide des fichiers ONIX (2.1/3.0/3.1) contre les schémas — QA métadonnées |

## Chaîne libre type (synthèse)
Pivot **Pandoc/Quarto** (single-source) → PDF imprimable par **LaTeX/ConTeXt** ou **Paged.js/WeasyPrint/Vivliostyle** → EPUB par **Sigil/Standard Ebooks tools** → métadonnées validées par **onixcheck** → PAO fine manuelle dans **Scribus** si besoin. **OJS/Pressbooks** servent de modèles de flux. Pour construire un outil, passer par `lancer-projet` / `usine-logicielle`.
