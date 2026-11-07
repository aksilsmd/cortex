# Sources — renfort externe (discipline-realisation.md, revue-multi-angles.md)

Dépôts consultés en lecture seule le 2026-11-03 (clone superficiel, aucun script exécuté). Méthodes reformulées en français ; aucun texte copié. Forme A de la décision « renfort GitHub » (projet Parapro, DEC-042). Procédure de mise à jour et propriétaire : `robustesse-agents/references/renfort-externe.md`.

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/obra/superpowers | MIT, © 2025 Jesse Vincent | `2ce8aa15d05b` | `skills/test-driven-development`, `systematic-debugging`, `verification-before-completion`, `writing-plans`, `executing-plans`, `requesting-code-review`, `receiving-code-review` (SKILL.md) | méthode réécrite ; hook `SessionStart` et scripts exclus |
| https://github.com/anthropics/claude-plugins-official | Apache-2.0 | `a7ba5b93db0c` | `plugins/pr-review-toolkit/agents/silent-failure-hunter.md`, `pr-test-analyzer.md` | angles de revue réécrits |

Exclus pour ce skill : tout hook, script, serveur ou appel réseau des dépôts ci-dessus (condition 1 de la décision).

## Ajout du 2026-11-07 — skill `cartographie-graphe` (outil séparé)

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/Graphify-Labs/graphify | Apache-2.0 (LICENSE, NOTICE © 2026 Safi Shamsi et contributeurs) ; paquet PyPI `graphifyy` 0.9.103 | `16218bfc80d4ca2799734d045039f7ed1a5fa9fb` | `README.md`, `graphify/skill.md`, `pyproject.toml` | consignes d'usage réécrites en français : `cartographie-graphe/SKILL.md` ; aucun code ni texte embarqué |

Graphify reste un **outil séparé**, comme IT-Tools : il s'installe dans un environnement isolé, version figée, et ne s'exécute qu'en analyse de code locale (`GRAPHIFY_BACKEND=none`, `--code-only`, journal des requêtes désactivé). Exclus : `graphify install` (skill amont à côté de Dan-Cortex), crochets git, `--watch`, mode strict, passe sémantique sans accord, Graphify Cloud. Non essayé dans l'environnement de construction du 2026-11-07 (PyPI inaccessible) : premier usage réel à consigner.

## Ajout du 2026-11-07 — données extrêmes et développement mobile (forme A)

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/emilkowalski/skills | MIT, © 2026 Emil Kowalski (fichier LICENSE) | `c8a79627b59d72d764d6ab6f2c87c09a48169833` | `skills/break-ui/SKILL.md`, `skills/break-ui/CATALOG.md` | méthode réécrite en français : `references/donnees-extremes-ui.md` (exemples de données refaits) |
| idem | idem | idem | `skills/animate-expo/SKILL.md`, `skills/animate-expo/RECIPES.md` | `references/mobile-react-native-animation.md` |
| idem | idem | idem | `skills/write-swift/SKILL.md` | `references/swift-moderne.md` |

Forme A : aucune phrase traduite mot à mot, aucun exemple ni tableau repris tel quel ; valeurs techniques seulement (durées, paramètres de ressort, courbes). Exclus : sections « Initial Response », commandes d'installation (`npx expo install`), extraits de code, émoji composé de `CATALOG.md` (donnée de test contenant un caractère de liaison sans largeur, jugée inoffensive, non reprise). Filtres §3 : licence MIT lue ; aucun hook ni script ; aucun appel réseau repris ; caractères invisibles recherchés dans les fichiers reformulés (aucun). Licences des paquets React Native citées : ajoutées par Dan-Cortex, à revérifier au moment du choix.


## Ajout du 2026-11-07 — `selection-outillage.md`

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/affaan-m/everything-claude-code (ECC) | MIT, © 2026 Affaan Mustafa | `d2ef2680594f9a17526a6e1a2e18b3d242c5d17b` | inventaire des dossiers `agents/`, `skills/`, `hooks/hooks.json` (54 commandes de crochets) | aucune reprise de texte ; décision : ne pas installer (crochets, exécution automatique), source de méthodes en forme A au cas par cas |
