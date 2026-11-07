# Sources — skill mouvement-interface

Dépôt consulté en lecture seule le 2026-11-07 (clone fourni, aucun script exécuté, aucune dépendance installée, aucune commande `npx`). Forme A de `robustesse-agents/references/renfort-externe.md` : méthodes reformulées en français, aucune phrase traduite mot à mot, aucun exemple ni tableau repris tel quel ; seules des valeurs techniques et formules sont conservées (durées, courbes de Bézier, paramètres de ressort, fonction de projection, formule d'élastique).

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/emilkowalski/skills | MIT, © 2026 Emil Kowalski (fichier LICENSE) | `c8a79627b59d72d764d6ab6f2c87c09a48169833` | `skills/animate/SKILL.md`, `skills/animate/RECIPES.md`, `skills/emil-design-eng/SKILL.md` | `construire-une-animation.md` |
| idem | idem | idem | `skills/choreograph/SKILL.md`, `skills/choreograph/RECIPES.md` | `choregraphie.md` |
| idem | idem | idem | `skills/apple-design/SKILL.md` | `mouvement-fluide-apple.md` |
| idem | idem | idem | `skills/animation-performance/SKILL.md`, `performance-cheatsheet.md` | `performance-animation.md` |
| idem | idem | idem | `skills/animation-vocabulary/SKILL.md` | `vocabulaire-du-mouvement.md` |
| idem | idem | idem | `skills/review-animations/SKILL.md`, `STANDARDS.md`, `skills/improve-animations/SKILL.md`, `AUDIT.md`, `PLAN-TEMPLATE.md`, `skills/find-animation-opportunities/SKILL.md`, `skills/remove-animations/SKILL.md` | `audit-du-mouvement.md` |

Filtres §3 : licence MIT lue dans LICENSE et confirmée par le README ; aucun hook, aucun script (seuls des fichiers Markdown, plus `.gitattributes`, `.gitignore` et un fichier vide `.pl`) ; appels réseau : liens et commande d'installation du README non suivis ; injection : sections « Initial Response » (réponse imposée), consignes de format obligatoire et de citation à l'identique écartées ; caractères invisibles : espaces sans largeur dans `PLAN-TEMPLATE.md` (balisage des blocs de code), jugés inoffensifs et non repris. Recherche de caractères invisibles sur les fichiers reformulés : aucun résultat.

Exclus : `README.md` (lu pour la licence et l'inventaire seulement), `ask-sonner/API.md`, toute commande d'installation. Les autres fichiers du dépôt sont repris dans `usine-logicielle` et `maquettes-parcours` (voir leurs fiches).

Propriétaire : `maquettiste` (références de design), `developpeur-frontend` (performance). Prochaine revue : 2027-02.

Correction du 2026-11-07, après relecture indépendante (verdict NON, `parapro/05-validation/securite/pentest-20261104/relecture-plugin-1.12.0.md`) : formats de sortie imposés retirés (constats au format Dan-Cortex, gravité C/H/M) ; passages réécrits de mémoire avec une structure propre (choix du correctif, cohérence spatiale, reconnaissance des gestes, ressorts, vocabulaire des ressorts, règles d'entrée et causes des données extrêmes) ; valeurs des ressorts confirmées à la source (`apple-design`, section 4) ; licences et poids marqués « à revérifier avant usage ». Relecture de non-copie par un agent distinct : à faire.
