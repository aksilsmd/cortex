# NOTICE — références draw.io (lot B, forme B limitée)

Dossier vendorisé dans Dan-Cortex le 2026-11-03, décision « renfort GitHub » (projet Parapro, DEC-042, PV du 2026-11-03, lot 5), après banc favorable (`banc-resultats.md`). Propriétaire : cartographe-interactions. Mise à jour : `robustesse-agents/references/renfort-externe.md` §6.

| Champ | Valeur |
|---|---|
| Dépôt amont | https://github.com/Agents365-ai/drawio-skill |
| Titulaire | © 2026 Agents365-ai |
| Licence | MIT (fichier `LICENSE` du dépôt, reproduit ci-dessous) |
| Commit source | `1f59eae2ca4740ed72a195279469fb58fa39d9e0` (2026-11-01) |

## Fichiers repris

| Fichier amont | Fichier Dan-Cortex |
|---|---|
| `skills/drawio-skill/references/shapes.md` | `formes.md` |
| `skills/drawio-skill/references/diagram-types.md` | `types-diagrammes.md` |
| `skills/drawio-skill/references/xml-authoring.md` | `redaction-xml.md` |

## Modifications

- Traduction en français et adaptation au format Dan-Cortex : sommaire, contrôles avant de rendre, renvois vers les références du skill (`schemas-mermaid.md`, `theme-design-system.md`, `workflows-fonctionnels.md`, `accessibilite.md`), identifiants `RG-` et `WF-`, exemples Parapro.
- **Supprimés** : tout appel à un script (`shapesearch.py`, `aiicons.py`, `sqlerd.py`, `seqlayout.py`, `c4.py`, `edgeports.py`, `validate.py`) et l'index de formes qui les accompagne ; logos de marques par CDN (lobe-icons, simple-icons) et toute URL d'image distante ; vérification par URL de visionneuse encodant le diagramme et `--dump-dom` ; routeur via serveur MCP ; renvois aux fichiers amont non repris (`style-presets.md`, `troubleshooting.md`, `mermaid-authoring.md`, `autolayout.md`) ; formulations impératives absolues (« always », « never », « CRITICAL ») ramenées à des règles ordinaires.
- **Retirés par choix de périmètre** : sections ML/apprentissage profond et SysML de `diagram-types.md` ; paragraphe sur l'origine de l'index de formes de `shapes.md`.
- **Ajoutés** : principe « rendu local, aucun lien de partage », recherche d'une forme rare dans draw.io de bureau, vérification sur export local, contrôles avant de rendre.

## Texte de la licence

```text
MIT License

Copyright (c) 2026 Agents365-ai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
