# Audit du dépôt Dan-Cortex

Audit du 21 novembre 2026, version 2.2.0, commit `e619aa8` de `main`. Il porte sur l'organisation du dépôt, la
documentation, la chaîne de construction, le coût en tokens et la publication, pas sur le fond des skills.

## Sommaire

- [1. Synthèse](#1-synthèse)
- [2. Ce qui est solide](#2-ce-qui-est-solide)
- [3. Constats](#3-constats)
- [4. Plan d'action](#4-plan-daction)
- [5. Méthode et mesures](#5-méthode-et-mesures)

## 1. Synthèse

| Axe | Note | En une phrase |
|---|---|---|
| Structure du plugin | ★★★★☆ | séparation nette `skills/`, `agents/`, `bibliotheque/`, `universel/` ; deux familles de skills tiers rangées à deux endroits différents |
| Documentation | ★★★★☆ | guides, architecture, catalogues générés, schémas ; il manquait un index des documents, la bibliothèque et la chaîne de construction en image |
| Qualité et CI | ★★★★★ | 53 tests, 3 générateurs vérifiés en CI sur Python 3.11 à 3.13, fichiers générés contrôlés |
| Licences | ★★★★★ | notices par dossier, registre des sources avec commits, formes A/B tracées |
| Sobriété en tokens | ★★★☆☆ | environ 5 400 tokens de descriptions chargés à chaque session, dont près de la moitié pour des copies de skills que Claude possède déjà |
| Publication | ★★☆☆☆ | archive binaire de 12 Mo versionnée dans git, aucune *release*, aucune étiquette de version, description GitHub au nom de l'ancien « Cortex » |

Les constats de priorité 1 qui ne changent pas le comportement du plugin sont corrigés dans ce lot. Les trois
décisions structurantes (§4, lot 2) attendent l'accord d'Aksil.

## 2. Ce qui est solide

- **Fichiers générés sous contrôle** : catalogues, cartes SVG, paquet universel et archive sont produits par
  script et la CI échoue s'ils ne sont pas à jour.
- **Traçabilité des sources** : chaque reprise tierce a sa licence, son commit et sa forme dans
  `dan-cortex/skills/robustesse-agents/references/renfort-externe.md` §8 et dans `dan-cortex/NOTICE.md`.
- **Gouvernance GitHub** : modèles d'issue (bogue, amélioration, correction de droit ou de norme), modèle de
  pull request, code de conduite, politique de sécurité, guide de contribution.
- **Entrée universelle** : `AGENTS.md` pour Codex, Claude Code et Gemini ; paquet `universel/` pour les IA de
  conversation.
- **Bibliothèque à la demande** : 173 compétences tierces sans coût permanent, ouvertes une à une par un
  skill-pivot.

## 3. Constats

Priorité : **P1** à corriger maintenant, **P2** à décider, **P3** amélioration.

| N° | Priorité | Constat | Preuve | Correction |
|---|---|---|---|---|
| C1 | P1 | Aucun index de la documentation : 10 documents dans `docs/`, sans parcours de lecture par profil | `ls docs/` | `docs/README.md` créé (fait) |
| C2 | P1 | La bibliothèque n'est expliquée ni dans l'architecture ni en image | `grep bibliotheque docs/*.md` : aucun résultat | `docs/bibliotheque.md`, architecture §11, schéma animé (fait) |
| C3 | P1 | La chaîne « source → générateur → fichier généré → CI → publication » n'existe qu'en Mermaid, sans distinguer les fichiers à ne jamais modifier à la main | `docs/architecture.md` §10 | carte du dépôt et schéma animé de la chaîne (fait) |
| C4 | P1 | `pyproject.toml` annonce la version 1.0.0, le plugin la 2.2.0 | `grep version pyproject.toml` | version alignée et test ajouté (fait) |
| C5 | P1 | Caches Python et `.pytest_cache` non ignorés | `.gitignore` | ajoutés (fait) |
| C6 | P2 | **Archive binaire versionnée** : `dist/dan-cortex.plugin` pèse 12 Mo ; chaque version en ajoute autant à l'historique, que tout clone télécharge | `du -sh dist` | la publier en *release* GitHub et la retirer de git (décision D1) |
| C7 | P2 | **Doublons avec Claude** : 13 skills d'Anthropic copiés tels quels (`docx`, `pdf`, `pptx`, `xlsx`, `skill-creator`…) existent déjà dans Claude ; ils doublent les déclenchements et coûtent environ 2 500 tokens par session | mesure des descriptions (§5) | les ranger dans `bibliotheque/anthropic/` comme Scenario, ouverts par un pivot (décision D2) |
| C8 | P2 | Aucune étiquette ni *release* : impossible d'installer ou de comparer une version précise | API GitHub : 0 tag, 0 release | étiqueter `v2.2.0` et publier les notes du CHANGELOG (décision D1) |
| C9 | P2 | Branches obsolètes | `git ls-remote --heads` | `audit-structure-depot`, `renfort-3d-jeu-elearning` et `v2.1-skills-anthropic` supprimées (fait) : leurs sommets étaient exactement ceux des pull requests 4, 3 et 2, fusionnées. `dan-cortex` et `v2.0-universel` conservées : la première n'a pas de pull request, la seconde porte des commits postérieurs à la fusion de la pull request 1 — leur fusion n'est pas démontrable |
| C10 | P3 | Description GitHub au nom de « Cortex », sans site | API GitHub | « Dan-Cortex : … » et lien vers la documentation (à faire dans les réglages du dépôt) |
| C11 | P3 | Actions GitHub épinglées par étiquette (`@v4`), pas par empreinte | `.github/workflows/tests.yml` | épingler par SHA, mise à jour par Dependabot |
| C12 | P3 | 7 `SKILL.md` dépassent 1 500 mots, dont 3 copies d'Anthropic | mesure (§5) | découper vers `references/` pour les skills maison (`lancer-projet`, `usine-logicielle`, `recueil-besoin`) |
| C13 | P3 | Noms mêlés : skills maison en français, copies d'Anthropic en anglais | `ls dan-cortex/skills` | réglé par D2 (les copies quittent `skills/`) |

## 4. Plan d'action

**Lot 1 (ce lot, sans effet sur le comportement du plugin)** : C1 à C5. Nouveaux documents : `docs/README.md`,
`docs/bibliotheque.md`, ce rapport ; nouveaux schémas : `carte-depot.svg`, `chaine-generation.svg`,
`chargement-a-la-demande.svg` (animés, immobiles si le système demande moins d'animations) ; architecture §10 et
§11, README et arborescence mis à jour ; test de concordance de version.

**État au 22 novembre 2026** : D3 est faite pour les trois branches dont la fusion est démontrable. D1 est
commencée — l'étiquette `v2.2.0` existe —, mais la *release* GitHub et le retrait de `dist/` de git restent liés :
tant qu'aucune *release* ne porte l'archive, le `README` doit continuer de pointer vers `dist/dan-cortex.plugin`.
D2 attend toujours : elle retire des commandes publiques (`/dan-cortex:docx`…) et relève donc d'un changement de
version majeur.

**Lot 2 (décisions d'Aksil)**

| Décision | Gain | Ce que ça change | Réversible |
|---|---|---|---|
| D1. Archive en *release* GitHub, étiquette `v2.2.0`, `dist/` retiré de git (construit et vérifié en CI) | dépôt allégé de 12 Mo par version ; versions téléchargeables | le lien d'installation pointe vers la page *Releases* | oui |
| D2. Les 13 copies d'Anthropic rejoignent `bibliotheque/anthropic/`, ouvertes par un pivot `documents-et-outils-claude` | environ 2 500 tokens de moins par session ; plus de double déclenchement avec les skills intégrés de Claude | les commandes `/dan-cortex:docx` etc. disparaissent au profit du pivot | oui |
| D3. Suppression des branches obsolètes | dépôt lisible | aucun : leur contenu est dans `main` | oui (commits conservés) |

## 5. Méthode et mesures

- Clone de `main`, contrôles par script (bibliothèque standard), lecture des documents, API GitHub en lecture.
- Descriptions des 48 skills : 21 716 caractères, soit environ 5 400 tokens chargés à chaque session (estimation à
  4 caractères par token). Les 13 copies d'Anthropic en représentent environ 10 000 caractères.
- `SKILL.md` de plus de 1 500 mots : `algorithmic-art`, `claude-api`, `lancer-projet`, `pptx`, `recueil-besoin`,
  `skill-creator`, `usine-logicielle`.
- Poids : `dist/` 12 Mo ; paquet git 12 Mo (clone superficiel) ; dépôt GitHub annoncé à 8 Mo avant la 2.2.0.
- Tests : 51 réussis avant et après ce lot.
