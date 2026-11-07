---
name: traduction-interpretariat
description: "Traduction et interprétariat, avec le français, l'arabe et l'anglais : traduire un texte, un livre ou une interface en gardant le sens, le registre et l'intention ; localiser un produit (logiciel, site, appli) ; organiser l'interprétation orale (consécutif, simultané, liaison). Théories et méthode (sourcier/cibliste, skopos, équivalence), spécificités FR/AR/EN (droite-à-gauche et diglossie de l'arabe, typographie française, variantes US/UK), localisation (RTL, PO/XLIFF, mémoires de traduction), et outils libres (OmegaT, Weblate, Translate Toolkit, LanguageTool). À utiliser pour « traduire », « traduction », « localiser », « interprète/interprétariat », « sous-titres », « version arabe/anglaise », « RTL »."
---

# Traduction et interprétariat (FR / AR / EN)

Faire passer un sens d'une langue à une autre sans le trahir. Règle d'or : **on traduit le sens, l'intention et le registre, pas les mots ; on traduit de préférence vers sa langue maternelle ; et on décide dès le départ la fonction du texte cible (son skopos), qui commande tous les choix.** On montre, on fait réviser, on itère.

## 1. Décider le cadre (avant de traduire)
- **Fonction du texte cible (skopos)** : notice, contrat, publicité, roman ? Elle commande les choix.
- **Posture** : plutôt **sourcier** (fidèle à la lettre et à l'étranger du texte) ou **cibliste** (fluide dans la langue d'arrivée) ? À régler selon le genre et le public.
- **Sens et paire** : vers quelle langue, pour qui ? Traduire vers sa langue maternelle est la règle. En triangle FR/AR/EN, choisir si l'on passe par une langue **pivot** (et surveiller les pertes en cascade).

## 2. Méthode (cycle qualité, proche d'ISO 17100)
1. **Analyse** : genre, public, fonction ; repérer terminologie et difficultés ; constituer glossaire et documentation.
2. **Premier jet** : transfert du sens, registre et intention tenus.
3. **Révision bilingue** (idéalement par un second regard) : exactitude, omissions, contresens, faux-sens.
4. **Relecture monolingue** de la cible : fluidité, naturel idiomatique, cohérence — « le texte doit se lire comme un original ».
5. **Harmonisation / QA** : cohérence terminologique, typographie, respect du glossaire et du guide de style.

Procédés utiles (Vinay & Darbelnet) : emprunt, calque, traduction littérale, transposition, modulation, équivalence (idiomes), adaptation (culturèmes). Théorie interprétative (ESIT) : **comprendre → déverbaliser → réexprimer**.

Pièges : **faux amis** (*library* = bibliothèque), décalages de **registre** (tu/vous absent en anglais), **culturèmes** (à expliciter ou adapter), **intraduisibles** (paraphrase, emprunt, compensation), sur/sous-traduction, calques syntaxiques.

Détail : `references/methode-et-langues.md`.

## 3. Spécificités FR / AR / EN
- **Arabe** : **droite-à-gauche (RTL)** et textes **bidirectionnels** (chiffres et latin en gauche-à-droite) → algorithme bidi, mise en page « en miroir ». **Diglossie** : *fushâ* (standard, écrit) vs **dialectes** (darija, égyptien, levantin) — choix décisif selon le public. Translittération : fixer un système (ALA-LC, DIN 31635). Ponctuation propre (، ؛ ؟), pas de majuscules, lettres liées selon la position.
- **Français** : tu/vous, politesse codifiée ; **typographie** : espace fine insécable avant `; : ! ?`, guillemets « … » avec insécables, tiret cadratin des dialogues, majuscules accentuées.
- **Anglais** : variantes **US/UK** (orthographe, lexique, dates), guillemets droits, pas d'espace avant la ponctuation haute.

Détail : `references/methode-et-langues.md`.

## 4. Interprétariat (oral, temps réel)
Distinct de la traduction écrite (pas de révision, mémoire et simultanéité, voix, stress). Modes : **consécutif** (après l'orateur, avec prise de notes type Rozan), **simultané** (cabine, relais 20-30 min), **chuchotage**, **de liaison** (va-et-vient bilatéral) ; variantes à distance, judiciaire, médicale. Déontologie (type AIIC) : fidélité, **neutralité**, **confidentialité**, transparence sur ses limites, ne pas se substituer aux parties. Détail : `references/interpretariat.md`.

## 5. Localisation (produit)
**i18n** (préparer : externaliser les chaînes, Unicode, pluriels, bidi) puis **l10n** (adapter à une locale : langue + formats date/heure/nombre/monnaie, unités, images, légal, RTL « mirroring »). Formats : **PO/gettext**, **XLIFF**, `.strings`/`.resx`/ARB/JSON. **Mémoire de traduction (TM)** au format **TMX** (correspondances exactes et *fuzzy*), **glossaires** au format **TBX**. Détail et outils : `references/localisation-et-outils.md`.

## 6. Outils libres (détail et licences dans `references/localisation-et-outils.md`)
TAO poste : **OmegaT** (GPLv3+, gère le RTL et LanguageTool). Plateforme collaborative : **Weblate** (GPLv3+, liée à Git). Moteur de formats et QA : **Translate Toolkit** (GPL-3.0, `pofilter`), **GNU gettext**. Édition PO : **Poedit** (base MIT). Alignement de corpus → TM : **hunalign** (LGPL-3.0). Contrôle qualité FR/EN : **LanguageTool** (LGPL-2.1+, serveur local ; arabe limité). Filtres : **Okapi** (Apache-2.0). Tous auto-hébergeables ; invoqués comme binaires/bibliothèques sur entrées contrôlées, sans auto-exécution de code tiers.

## Rôles (agents, si disponibles)
| Rôle | Agent |
|---|---|
| Traduction écrite + révision | `traducteur` |
| Interprétation orale | `interprete` |
| Localisation, formats, TM, outils CAT | `localisateur` |
| Terminologie, microcopie, adaptation culturelle | `redacteur-contenu-localisation` |
| Mise en page RTL et bilingue | `maquettiste` (+ `design-apple`) |

## Garde-fous
- Fidélité au sens et au registre ; ne pas lisser l'altérité d'un texte littéraire sans raison (choix à assumer).
- **Confidentialité** des documents confiés (skill `confidentialite-traces`).
- Respect des droits : traduire une œuvre protégée pour publication relève du contrat (droits de traduction) — renvoyer au `juriste-numerique`.
- Pas de reproduction d'extraits longs protégés ; sobriété.

## Références
| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/methode-et-langues.md` | théories, cycle qualité, procédés, pièges, et spécificités FR/AR/EN en détail |
| `${CLAUDE_SKILL_DIR}/references/interpretariat.md` | modes d'interprétation, prise de notes, compétences, déontologie |
| `${CLAUDE_SKILL_DIR}/references/localisation-et-outils.md` | i18n/l10n, RTL, formats (PO/XLIFF), TM/TBX, et outils libres avec licences |
