# Localisation et outils libres

## Traduction vs localisation
La **traduction** transfère le texte ; la **localisation (l10n)** adapte un produit (logiciel, site, appli, jeu) à une **locale** : langue + formats date/heure/nombre/monnaie, unités, sens de lecture, images et couleurs, conformité légale, claviers. L'**internationalisation (i18n)** est la préparation technique en amont (externaliser les chaînes, Unicode, pluriels, bidi) qui rend la l10n possible.

## RTL (arabe/hébreu)
Interface « mise en miroir » : alignement à droite, inversion de l'ordre des éléments, icônes directionnelles retournées, algorithme bidi Unicode, marqueurs LRM/RLM pour les segments mixtes.

## Formats de fichiers
- **PO / gettext** (`.po`/`.pot`) : paires `msgid`/`msgstr`, pluriels, statut *fuzzy* ; très répandu dans le logiciel libre ; `.pot` = gabarit neutre.
- **XLIFF** (OASIS, 1.2 et 2.x) : format d'échange professionnel, source et cible distinctes, machine à états (`new`, `translated`…), interopérable entre outils TAO.
- Autres : `.properties`/ARB (Java/Flutter), `.strings`/`.xcstrings` (Apple), `.resx` (.NET), JSON/YAML (web), `.ts` (Qt), CSV/XLSX (échange simple).

## Mémoires de traduction et glossaires
- **Mémoire de traduction (TM)** : segments source/cible réutilisés par correspondance exacte (100 %) ou approximative (*fuzzy*) ; format d'échange **TMX**.
- **Glossaires / bases terminologiques** : terminologie imposée ; format d'échange **TBX**. Cohérence surtout en équipe et sur la durée.

## Outils libres (URL — licence lue — apport ; tous locaux/auto-hébergeables)
| Outil | URL | Licence | Apport |
|---|---|---|---|
| OmegaT | github.com/omegat-org/omegat | GPLv3+ | TAO de bureau (Java) : TM (TMX), glossaires (TBX), 20+ formats, RTL, LanguageTool intégré, MT optionnelle |
| Weblate | github.com/WeblateOrg/weblate | GPLv3+ | plateforme web de localisation continue, intégration Git, QA, glossaires |
| Translate Toolkit | github.com/translate/translate | GPL-3.0 | conversion PO/XLIFF/TMX/TBX et **QA** (`pofilter`, 40+ contrôles) ; socle de Weblate |
| GNU gettext | gnu.org/software/gettext | GPL (lib LGPL) | standard PO/POT (`xgettext`, `msgfmt`, `msgmerge`) |
| Poedit | github.com/vslavik/poedit | base MIT (Pro propriétaire) | éditeur de catalogues PO/MO, ouvre XLIFF |
| hunalign | github.com/danielvarga/hunalign | LGPL-3.0 | alignement de phrases bilingues → corpus parallèles et TM |
| LanguageTool | github.com/languagetool-org/languagetool | LGPL-2.1+ (cœur) | grammaire/style FR et EN, serveur local (arabe limité) |
| Okapi Framework | okapiframework.org | Apache-2.0 | filtres et conversion (PO, XLIFF, TMX, DOCX, HTML…), complément d'OmegaT |

## Chaîne libre type (FR/AR/EN)
**Translate Toolkit** (conversion + QA) → **OmegaT** ou **Weblate** (poste/plateforme, TM en TMX, glossaires TBX) → **Poedit** (édition PO ponctuelle) → **hunalign** (bâtir une TM depuis un corpus) → **LanguageTool** (QA FR/EN). Vigilance : **RTL/bidi** et **diglossie** côté arabe, **typographie française**, **variantes US/UK**, sens de traduction vers la langue maternelle, et skopos défini dès l'analyse.

*Sources : dépôts GitHub cités (licences lues) ; Wikipédia (localisation, i18n, XLIFF, gettext, TM, TMX) ; gnu.org/software/gettext ; docs.oasis-open.org (XLIFF).*
