# Audit de cohérence du dépôt, 22 novembre 2026

Audit du 22 novembre 2026, version 2.3.0, commit `447cdb1` de `main`, branche de travail
`claude/audit-coherence-2.3.0`. Il vérifie que les documents racontent le même plugin que ses fichiers :
versions, compteurs, renvois, fiches d'agents, licences, paquet. Il complète [`audit-depot.md`](audit-depot.md),
qui porte sur l'organisation du dépôt et la publication : les deux ne se recouvrent pas.

## Sommaire

- [Synthèse](#synthèse)
- [Constats](#constats)
- [Verdict sur le correctif proposé](#verdict-sur-le-correctif-proposé)
- [Décisions laissées à l'auteur](#décisions-laissées-à-lauteur)
- [Résultat de make verify](#résultat-de-make-verify)
- [Méthode](#méthode)

## Synthèse

- `make verify` était **vert avant** l'audit : les 53 tests ne voyaient aucun des écarts ci-dessous.
- **27 constats** : 10 erreurs, 10 incohérences, 7 mineurs. 21 corrigés, 6 laissés à ta décision.
- Cause principale : la 2.3.0 a fait passer la bibliothèque de 173 à 252 compétences, avec une source sous
  Apache-2.0, sans reporter le chiffre ni la licence partout (six fichiers, deux schémas).
- `outils-par-agent.md` se disait généré mais ne l'était pas : 13 agents absents, 18 lignes périmées.
- Le résumé « In English » annonçait 2.2.0, alors que le CHANGELOG 2.3.0 disait l'avoir corrigé.
- Aucun lien mort, aucun chemin `${CLAUDE_SKILL_DIR}` ou `${CLAUDE_PLUGIN_ROOT}` cassé, aucun agent ni skill
  cité qui n'existe pas, toutes les commandes `cortex.py` citées existent avec leurs options.
- Frontmatter : 50 skills et 59 agents valides ; modèle et effort conformes à l'organigramme pour les 59.
- Licences : chaque source de la bibliothèque a sa `LICENSE` et sa `NOTICE.md` ; commits cités de façon
  cohérente partout.
- Paquet : `dist/dan-cortex.plugin` et `universel/` étaient à jour ; 2 579 fichiers, 35 Mo décompressés, pas de
  `bin/` à la racine du plugin.
- Douze tests ajoutés (`tests/test_coherence.py`) : sur le commit audité, ils relèvent 15 échecs ; corrigés, ils
  passent.
- Version inchangée (2.3.0) ; corrections consignées sous « Non publié » dans le `CHANGELOG.md`.

## Constats

Lignes du commit `447cdb1`. Gravité : **erreur** (fait faux), **incohérence** (deux sources se contredisent ou
une liste est incomplète), **mineur** (forme).

| Id | Gravité | Fichier:ligne | Constat | Preuve | Correction |
|---|---|---|---|---|---|
| A01 | erreur | `README.md:224` | Le résumé anglais annonce « current: 2.2.0 » | `plugin.json` : 2.3.0 | 2.3.0 (fait) |
| A02 | erreur | `CHANGELOG.md:43` | L'entrée 2.3.0 dit le résumé anglais corrigé ; il annonçait 2.2.0 | A01 | entrée « Non publié » qui le dit (fait) |
| A03 | erreur | `AGENTS.md:69` | « 173 skills tiers (MIT) » | 252 `SKILL.md` sous `bibliotheque/` ; `cli-anything/LICENSE` est Apache-2.0 | 252, MIT et Apache-2.0, quatre sources (fait) |
| A04 | erreur | `AGENTS.md:69` | « ouvre `INDEX.md` » : aucun `INDEX.md` à la racine de `bibliotheque/` | `ls dan-cortex/bibliotheque` : `README.md` et quatre dossiers | renvoi vers `bibliotheque/README.md` puis l'`INDEX.md` de la source (fait) |
| A05 | erreur | `docs/architecture.md:289` | « 173 compétences tierces (licence MIT) » | comme A03 | 252, tableau des sources et licences (fait) |
| A06 | incohérence | `docs/architecture.md:290-297` | « Cinq skills-pivots » mais `pilotage-outils-cli` et `comprendre-un-code` absents ; `plateforme-elearning` et `reconstruction-salle-blanche` présentés comme pivots | `bibliotheque/README.md`, colonne des pivots | cinq vrais pivots ; les deux autres sortis du tableau (fait) |
| A07 | erreur | `docs/bibliotheque.md:11` | « 173 compétences » | comme A03 | 252 (fait) |
| A08 | incohérence | `docs/bibliotheque.md:31` | Seuls les index de `scenario-labs` sont cités ; `cli-anything` et `understand-anything` ont aussi leur `INDEX.md`, écrit à la main | `ls` des deux dossiers ; leurs `NOTICE.md` | phrase complétée (fait) |
| A09 | erreur | `dan-cortex/bibliotheque/README.md:3` | « (licence MIT) » alors que la ligne `cli-anything/` du même tableau dit Apache-2.0 | `cli-anything/LICENSE` | « licences MIT et Apache-2.0 » (fait) |
| A10 | erreur | `dan-cortex/.claude-plugin/plugin.json:4` | « bibliothèque de 173 skills vendorisés » | comme A03 | 252 et les quatre sources (fait) |
| A11 | erreur | `docs/images/carte-depot.svg:3,19,32-34` | « 48 skills », « 173 compétences tierces MIT », deux sources seulement | 50 dossiers sous `skills/` ; quatre sources | 50 ; 252, quatre sources, deux licences ; rendu contrôlé (fait) |
| A12 | incohérence | `docs/images/chargement-a-la-demande.svg:3,15,96` | « 173 compétences », « 172 autres » | comme A03 | 252 et 251 (fait) |
| A13 | erreur | `dan-cortex/skills/lancer-projet/references/outils-par-agent.md:3-58` | « Généré à partir des fiches » : aucun script ne le génère ; 46 agents sur 59 ; skills préchargés périmés pour 18 agents (ex. `planificateur` : « aucun » au lieu de `cartographie-graphe`) | croisement des en-têtes `agents/*.md` | tableau repris des 59 fiches, en-tête rectifiée, test de concordance (fait) |
| A14 | incohérence | `dan-cortex/README.md:223` | 231 fichiers de référence et gabarits | 251 fichiers sous `skills/*/references/` et `skills/*/assets/` | 251 (fait) |
| A15 | incohérence | `dan-cortex/README.md:224` | 10 scripts maison, « 2 scripts Node » | 11 fichiers, dont 3 dans `boite-outils-it/scripts/` (`.cjs`, deux `.mjs`) | 11 et 3 (fait) |
| A16 | incohérence | `CONTRIBUTING.md:98` | §7 cite trois endroits de la version ; `CLAUDE.md` et les tests en exigent cinq (oubli de `pyproject.toml`) | `CLAUDE.md` règle 3 ; `test_versions_concordent` | `pyproject.toml` ajouté (fait) |
| A17 | incohérence | `AGENTS.md:22-45` | La table d'orientation omet six skills maison : `comprendre-un-code`, `pilotage-outils-cli`, `cartographie-graphe`, `boite-outils-it`, `crm-twenty`, `execution-resiliente` (`robustesse-agents` n'y est cité qu'en chemin) | `ls dan-cortex/skills` | quatre lignes ajoutées, agents tirés des fiches ; renvoi au catalogue pour les copies d'Anthropic (fait) |
| A18 | incohérence | `README.md:222-223` | « the rest is MIT » : ignore CLI-Anything, sous Apache-2.0 | `cli-anything/LICENSE` | phrase précisée (fait) |
| A19 | mineur | `.github/ISSUE_TEMPLATE/bogue.yml:17` | Exemple de version « 2.1.0 » | version courante 2.3.0 | 2.3.0 (fait) |
| A20 | mineur | `CHANGELOG.md:12,45` | L'entrée 2.3.0 porte deux sections « Ajouté » | `grep -n "### Ajouté"` | fusionnées (fait) |
| A21 | mineur | `README.md:82-83` | Ligne vide en double sous « Comment ça marche » | lecture | supprimée (fait) |
| A22 | incohérence | `SECURITY.md:7-8` | Versions prises en charge : 2.1.x et « 2.0.x jusqu'à la 2.2.0 » ; ni 2.2.x ni 2.3.x | version courante 2.3.0 | **à décider** (D1) |
| A23 | incohérence | `accueil-recueil/SKILL.md:3`, `recueil-besoin/SKILL.md:3` | Les deux descriptions se déclenchent sur « j'ai une idée » ; `accueil-recueil` délègue l'entretien à `recueil-besoin`, qui ne le mentionne pas | `grep` des déclencheurs | **à décider** (D2) |
| A24 | mineur | `dan-cortex/NOTICE.md:33` | Section « Bibliothèque (2026-11-21, version 2.2.0) » qui couvre aussi les ajouts du 22/11 (2.3.0) | lignes `cli-anything/`, `understand-anything/` | **à décider** (D3) : `CLAUDE.md` règle 6, notice conservée |
| A25 | mineur | `docs/images/carte-depot.svg:109` | La légende dit `scenario-labs/INDEX.md` et `index/` générés « par un script » : aucun script du dépôt ne le fait | `grep -n INDEX scripts/*.py` : rien | **à décider** (D4) |
| A26 | mineur | `dan-cortex/README.md:196` | « chacun avec le skill de son pôle, préchargé » : `orchestrateur-de-pole`, `verificateur` et `suivi-avancement` n'en préchargent aucun | `outils-par-agent.md` | **à décider** (D5) |
| A27 | mineur | `dan-cortex/agents/suivi-avancement.md:9` | `tools` écrit en liste en ligne, les 58 autres fiches en liste à tirets | lecture | **à décider** (D6) : YAML valide, forme seule |
| A28 | mineur | `accueil-recueil` ↔ `recueil-besoin` | Doublon apparent vérifié : pas un doublon. L'accueil est le parcours en dix étapes ; le recueil est l'entretien qu'il appelle à l'étape 4 | `accueil-recueil/SKILL.md:78` | aucun skill supprimé ; voir D2 pour les déclencheurs |

A28 n'est pas un constat mais une vérification demandée, sans écart : le décompte porte sur A01 à A27.

## Verdict sur le correctif proposé

Correctif `dan-cortex-v2.3.0-documentation-alignment.patch` fourni par l'utilisateur. Ses blocs n'ont pas de
numéros de ligne : `git apply --check` le refuse (« patch with only garbage »). Il a été appliqué à la main,
ligne par ligne, après contrôle.

| Ligne du correctif | Verdict | Contrôle |
|---|---|---|
| README : « current: 2.2.0 » → 2.3.0 | **exact**, appliqué | `plugin.json` |
| CHANGELOG : réécrire la ligne 2.3.0 en « aligné sur la version 2.3.0 » | **refusé dans cette forme** : il réécrit une entrée publiée pour lui faire dire vrai après coup | consigné sous « Non publié » |
| architecture : 173 → **252** compétences | **exact**, appliqué | 252 `SKILL.md` |
| « quatre sources, sous licences MIT et Apache-2.0 » | **exact** | quatre dossiers, quatre `LICENSE` lus |
| `scenario-labs/` 172, MIT | **exact** | `INDEX.md` : 87 + 85 ; `LICENSE` : MIT, © 2026 Scenario Inc. |
| `scroll-world/` MIT | **exact** (1 compétence, non chiffrée dans le correctif) | `LICENSE` : MIT, © 2026 cyw |
| `cli-anything/` 70, Apache-2.0 | **exact** | 70 `SKILL.md` ; `LICENSE` : Apache License 2.0 |
| `understand-anything/` 9, MIT | **exact** | 9 `SKILL.md` ; `LICENSE` : MIT, © 2026 Yuxiang Lin |
| « Cinq skills-pivots » | **exact** | `studio-3d-jeu`, `creation-medias-ia`, `web-3d-immersif`, `pilotage-outils-cli`, `comprendre-un-code` |
| pivots `pilotage-outils-cli` → « `cli-anything/` », `comprendre-un-code` → « `understand-anything/` » | **imprécis** : la porte d'entrée est l'`INDEX.md` de chaque source | écrit `cli-anything/INDEX.md`, `understand-anything/INDEX.md` |
| `plateforme-elearning` et `reconstruction-salle-blanche` sortis du tableau des pivots | **exact** | aucun renvoi vers `bibliotheque/` dans leurs fichiers |
| Ce que le correctif n'a pas vu | **incomplet** | A03, A04, A07 à A18 |

## Décisions laissées à l'auteur

| Id | Question | Proposition |
|---|---|---|
| D1 | Quelles versions reçoivent les correctifs de sécurité (`SECURITY.md`) ? | Suivre la règle déjà écrite : 2.3.x oui ; 2.2.x jusqu'à la 2.4.0 ; plus ancien, non |
| D2 | `accueil-recueil` et `recueil-besoin` partagent le déclencheur « j'ai une idée » | Le retirer de `recueil-besoin`, et y écrire que l'accueil l'appelle à l'étape 4 |
| D3 | Dater la section bibliothèque de `dan-cortex/NOTICE.md` (2.2.0 et 2.3.0) | Ajouter « et 2026-11-22, version 2.3.0 » au titre, si tu acceptes de toucher la notice |
| D4 | Les index de `scenario-labs` : générés par un script absent du dépôt | Ajouter le script, ou dire « générés une fois, à la main » dans la légende de `carte-depot.svg` |
| D5 | Trois agents de pilotage sans skill préchargé | Leur donner `lancer-projet`, ou écrire « la plupart » dans `dan-cortex/README.md` |
| D6 | Forme de l'en-tête `tools` de `suivi-avancement` | L'aligner sur les autres fiches |
| D7 | Publier ces correctifs | Une 2.3.1 (semver : correctif), aux cinq endroits de `CLAUDE.md` règle 3 |

## Résultat de make verify

| Moment | Résultat réel |
|---|---|
| Avant (commit `447cdb1`) | `784 contrôles`, format correct ; `Ran 53 tests`, `OK` ; `Catalogues à jour.` ; `dist/dan-cortex.plugin à jour (2579 fichiers).` ; audit des réglages : `NO_MATCHING_PATTERNS` (INFO) ; `Tout est vert.` |
| Après (`make build` puis `make verify`) | `784 contrôles`, format correct ; `Ran 65 tests`, `OK` ; `Catalogues à jour.` ; `dist/dan-cortex.plugin à jour (2579 fichiers).` ; audit des réglages : `NO_MATCHING_PATTERNS` (INFO) ; `Tout est vert.` |

## Méthode

- Versions : recherche de tout numéro `1.x` et `2.x` hors `CHANGELOG.md` historique et hors `bibliotheque/` ;
  les exemples de messages de commit (`Dan-Cortex 2.2.0 : …`) et les audits datés sont légitimes.
- Compteurs : comptage des dossiers `skills/`, des fiches `agents/`, des lignes de contrôle des
  `checklist-*.md`, des `SKILL.md` de chaque source, des fichiers `references/`, `assets/` et `scripts/`.
- Renvois : chaque lien Markdown relatif, chaque chemin entre accents graves, chaque `${CLAUDE_SKILL_DIR}/…` et
  `${CLAUDE_PLUGIN_ROOT}/…` des fichiers maison, chaque `dan-cortex:<nom>` ; `cortex.py aide` croisé avec toutes
  les commandes et options citées.
- Agents : en-têtes des 59 fiches croisés avec `organigramme.md` (niveau A, B, C ↔ modèle et effort) et
  `outils-par-agent.md` (outils, skills préchargés).
- Paquet : `make build` puis comparaison ; limites d'installation (5 000 fichiers, 200 Mo, pas de `bin/`) prises
  dans l'ordre de mission, non revérifiées en ligne : à vérifier dans la documentation de l'éditeur.
- Scripts de comptage hors dépôt ; les contrôles durables sont dans `tests/test_coherence.py`.
