# Journal des versions

Toutes les évolutions notables de Dan-Cortex sont consignées ici. Le format suit
[Keep a Changelog 1.1.0](https://keepachangelog.com/fr/1.1.0/) et le projet applique le
[versionnage sémantique](https://semver.org/lang/fr/) : majeure pour un changement de parcours ou de format du
dossier projet, mineure pour un skill, un agent ou une capacité en plus, correctif sinon.

Catégories : **Ajouté**, **Modifié**, **Corrigé**, **Supprimé**, **Sécurité**, **Documentation**.

## [Non publié]

Corrections de cohérence relevées par l'audit du 22/11/2026 (`docs/audit-coherence-2026-11-22.md`). Le numéro
de version ne change pas : il se choisit à la publication (`CONTRIBUTING.md` §7), et ces correctifs donneront
une 2.3.1.

### Corrigé

- **Import dans l'application Claude refusé.** Trois limites de validation de l'éditeur, constatées le 23/11/2026 en important `dist/dan-cortex.plugin` par « Téléverser un plugin » : chemins de plus de 12 dossiers (famille Roblox de `scenario-labs` remontée), description du plugin de plus de 500 caractères (`plugin.json` ramené à moins de 500 ; la présentation complète reste dans le `README.md`), description de skill de plus de 1 024 caractères (`claude-api`, raccourcie, modification notée dans `NOTICE.md`). `tests/test_archive.py` les vérifie désormais.
- Le résumé « In English » annonçait encore la version 2.2.0 : la correction notée en 2.3.0 s'était arrêtée à
  mi-chemin. Il annonce 2.3.0 et cite la licence Apache-2.0 de CLI-Anything.
- La bibliothèque compte **252** compétences (MIT et Apache-2.0), pas 173 (MIT) : `AGENTS.md`,
  `docs/architecture.md`, `docs/bibliotheque.md`, `plugin.json`, `bibliotheque/README.md` et les schémas
  `carte-depot.svg` (qui comptait aussi 48 skills au lieu de 50) et `chargement-a-la-demande.svg`.
- `docs/architecture.md` §11 : les pivots `pilotage-outils-cli` et `comprendre-un-code` manquaient ;
  `plateforme-elearning` et `reconstruction-salle-blanche` y figuraient à tort comme pivots.
- `AGENTS.md` renvoyait à un `INDEX.md` absent de la racine de la bibliothèque, et omettait six skills maison
  de sa table d'orientation.
- `outils-par-agent.md` se disait généré mais ne l'était pas : 13 agents sur 59 manquaient et 18 lignes ne
  suivaient plus les skills préchargés des fiches. Le tableau est repris des fiches.
- `dan-cortex/README.md` : 251 fichiers de référence et gabarits (pas 231), 11 scripts maison dont 3 scripts
  Node (pas 10 et 2).
- `CONTRIBUTING.md` §7 oubliait `pyproject.toml` parmi les endroits où s'écrit la version ; le modèle de ticket
  proposait 2.1.0 comme exemple.
- L'entrée 2.3.0 de ce journal portait deux sections « Ajouté » : elles sont fusionnées.
- L'import de `dan-cortex.plugin` par « Téléverser un plugin » était refusé : « Zip file contains path more
  than 12 folders deep ». Le gabarit `arena` de `scenario-roblox-architecture` descendait à 13 segments. La
  famille Roblox de `bibliotheque/scenario-labs/` passe d'un bloc de `skills/game-engines/roblox/` à
  `game-engines-roblox/`, contenu inchangé : 11 segments au plus. Index, pivot `studio-3d-jeu` et notices
  suivent (audit, constat A29).

### Ajouté

- `tests/test_coherence.py` : douze contrôles qui auraient détecté ces écarts (version du résumé anglais,
  compteur de la bibliothèque partout, licence et notice de chaque source, pivots, inventaire du plugin,
  chemins `${CLAUDE_SKILL_DIR}` et `${CLAUDE_PLUGIN_ROOT}`, noms `dan-cortex:…`, fiches d'agents).
- `tests/test_archive.py` et un contrôle dans `scripts/construire_plugin.py` : l'archive est refusée si un
  chemin dépasse 11 segments, si le plugin dépasse 5 000 fichiers ou 200 Mo, s'il a un `bin/` à sa racine ou
  s'il perd `.claude-plugin/plugin.json`.

## [2.3.0] - 2026-11-22

### Ajouté

- **Deux skills-pivots** vers de nouvelles compétences vendorisées, chargées à la demande :
  - `pilotage-outils-cli` ouvre `bibliotheque/cli-anything/` — **70 compétences** pour piloter un logiciel
    depuis le terminal : 3D et CAO (Blender, FreeCAD, CloudCompare), image et son (GIMP, Krita, Inkscape,
    Audacity, MuseScore), vidéo (Kdenlive, Shotcut, OBS), notes et documents (Obsidian, Joplin, Zotero,
    Calibre, LibreOffice), données et cartes (QGIS, OpenRefine, ChromaDB), infrastructure et réseau (PM2, n8n,
    Ollama, AdGuard Home, WireMock), navigateur et terminal. Copie fidèle de
    [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything) (Apache-2.0, commit `34f5195`), dossier
    `skills/` seul : **aucun script embarqué**.
  - `comprendre-un-code` ouvre `bibliotheque/understand-anything/` — **9 compétences** pour comprendre un dépôt
    qu'on n'a pas écrit : carte de l'architecture, domaines métier, dépendances, graphe de connaissances, revue
    de différences, parcours d'arrivée, lecture d'une maquette Figma. Copie fidèle de
    [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) (MIT, commit `17550ef`),
    dossier `skills/` seul, avec ses 20 scripts d'analyse **locale** (aucun appel réseau, vérifié).
- La bibliothèque passe de 173 à **252 compétences** vendorisées. Elles ne se chargent toujours pas d'office :
  le coût en tokens d'une session ne bouge pas, seuls deux descriptifs de pivots s'ajoutent.
- Notices, registre des sources (`renfort-externe.md` §8) et exception du 22/11/2026 : contrôles du §3 passés
  fichier par fichier, et motif du **refus d'un troisième dépôt**, `Twigpine/openclaude`, dont le `LICENSE`
  indique qu'il redistribue du code propriétaire d'Anthropic sans autorisation.
- `Makefile` : point d'entrée unique, aligné sur la CI (`make verify`) et sur la chaîne de régénération de
  `CONTRIBUTING.md` (`make build`).
- `CLAUDE.md` : les règles de travail du dépôt pour Claude Code, qui ne lit pas `AGENTS.md` de lui-même.
- `SUPPORT.md`, `.github/CODEOWNERS`, `.github/dependabot.yml`, `.editorconfig`, `.gitattributes` — l'archive et
  les catalogues y sont marqués comme générés, la bibliothèque comme vendorisée.
- Deux contrôles automatiques : six images au plus dans le `README`, et aucun `mermaid`.

### Corrigé

- **Affichage du `README` sur mobile.** L'application mobile de GitHub en tronquait la fin et les images
  tardaient. Deux causes : le diagramme `mermaid` était dessiné par le navigateur *après* le chargement, ce qui
  change la hauteur de la page une fois celle-ci déjà mesurée ; et onze images devenaient onze requêtes séparées
  servies par le proxy d'images de GitHub. Le diagramme faisait double emploi avec `vague-agents.svg`, déjà dans
  `docs/architecture.md` ; la carte du dépôt précédait la même arborescence en texte. Il reste six images et
  aucun diagramme rendu par le navigateur.
- Les compteurs de skills, d'agents et de contrôles passent des badges au texte : quatre requêtes externes de
  moins, et les mêmes chiffres restent vérifiés contre le plugin par les tests.
- Le résumé « In English » annonçait encore la version 2.1.0.

### Modifié

- L'intégration continue annule les exécutions dépassées, nomme ses étapes, va au bout de la matrice et refuse
  un arbre de travail sale.
- Un contrôle de plus : les liens vers une section (`#une-ancre`) doivent viser un titre qui existe. Ils sont
  tous valides aujourd'hui ; le test empêche qu'un renommage de titre les casse en silence.
- `docs/audit-depot.md` dit l'état réel du plan d'action. La fusion des branches `audit-structure-depot`,
  `renfort-3d-jeu-elearning` et `v2.1-skills-anthropic` est vérifiée — leurs sommets sont exactement ceux des
  pull requests 4, 3 et 2 —, donc leur suppression ne perdra rien ; `dan-cortex` et `v2.0-universel` sont à
  garder, leur fusion n'étant pas démontrable.

## [2.2.0] - 2026-11-21

### Ajouté

- **Bibliothèque de compétences vendorisées** (`dan-cortex/bibliotheque/`) : copie fidèle, licence MIT, de
  [scenario-labs/skills](https://github.com/scenario-labs/skills) (172 skills : Blender, Maya, ZBrush, Godot,
  Unity, Unreal, Roblox, et 85 skills de la plateforme Scenario pour images, vidéo, audio, textures et 3D) et de
  [oso95/scroll-world](https://github.com/oso95/scroll-world). Rangée hors de `skills/` : rien ne se charge
  d'office ; un skill-pivot ouvre l'index de la famille puis un seul `SKILL.md`. Aucun script n'est exécuté sans
  lecture et accord explicite. Notices et textes de licence dans chaque dossier.
- Cinq skills-pivots : `studio-3d-jeu` (Blender en ligne de commande, bpy, MCP pour Blender, BlenderGIS, choix et
  routage des moteurs de jeu), `web-3d-immersif` (three.js, React Three Fiber, fluide WebGL, scroll-world,
  portfolio 3D, performance et accessibilité), `creation-medias-ia` (plateforme Scenario, devis avant
  génération, droits, données), `plateforme-elearning` (Canvas LMS, LTI 1.3, API, AGPL, données des apprenants),
  `reconstruction-salle-blanche` (étudier un produit et construire sa version sans rien copier, méthode inspirée
  de Craft Anything).

### Modifié

- Branchements dans `lancer-projet` (table de routage, section « Skills spécialisés ») et `accueil-recueil`
  (`outils-quand`) ; README, AGENTS.md, catalogues, paquet universel et archive mis à jour.

### Documentation

- Audit du dépôt (`docs/audit-depot.md`) : constats chiffrés, priorités, plan en deux lots.
- Index de la documentation (`docs/README.md`) avec parcours de lecture par profil, et page
  `docs/bibliotheque.md` (principe, garde-fous, ajout d'une source).
- Trois schémas : carte du dépôt (sources et fichiers générés), chaîne de génération et chargement à la demande,
  ces deux derniers animés et immobiles si le système demande moins d'animations.
- Architecture : §10 réécrit (tableau « modifier à la main ? », schémas), nouveau §11 sur la bibliothèque.
- `pyproject.toml` aligné sur la version du plugin (test ajouté) ; caches de tests ignorés.

### Sécurité

- Blender et BlenderGIS (GPL), Canvas LMS (AGPL), 3d-portfolio (sans licence) : forme A seulement, aucun texte ni
  code repris. Registre : `robustesse-agents/references/renfort-externe.md` §8.

## [2.1.0] - 2026-11-12

### Ajouté

- Cinq skills traduits en français et adaptés (forme B, Apache-2.0, © Anthropic, PBC, dépôt anthropics/skills,
  commit `2c5958e`) : `conception-interface`, `communication-interne`, `fabrique-themes` (dix thèmes, sans le PDF),
  `design-affiche` (sans les polices OFL), `vigilance-discernement` (activé par le chef d'orchestre, plus de
  déclenchement automatique). Chacun a son `LICENSE.txt` et son `NOTICE.md`.
- Treize skills copiés sans modification, avec leur `LICENSE.txt` : `docx`, `pdf`, `pptx`, `xlsx`,
  `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`, `slack-gif-creator`,
  `algorithmic-art`, `claude-api`, `academy-guide`, `brand-guidelines` (description préfixée : exemple
  d'Anthropic, à ne pas appliquer aux projets des clients). `THIRD_PARTY_NOTICES.md` amont à la racine du plugin.
- Référence de co-rédaction `specifications/references/coredaction-documents.md` (forme A, réécriture).
- Guide `lancer-projet/references/skills-officiels-anthropic.md` et ligne dans `routage-skills-outils.md`.
- `scripts/generer_catalogues.py` : catalogues des skills et des agents, carte des skills et carte des pôles
  générés à partir des fichiers du plugin ; `--verifier` en CI.
- Test `tests/test_documentation.py` : catalogues et cartes à jour, SVG valides, liens relatifs résolus,
  chiffres du README alignés sur le plugin.

### Modifié

- L'organigramme du réseau (`lancer-projet/references/organigramme.md`) liste les 59 agents : ajout de
  `vigie-oublis`, `intervieweur`, `organisateur`, des testeurs web, mobile et visuel, et des pôles Écriture et
  édition, Traduction et localisation.

### Sécurité

- Exception du 12/11/2026 (décision du mainteneur) : levée, pour ce seul renfort, de l'interdit des scripts et du
  réseau (`renfort-externe.md`) pour les treize dossiers copiés tels quels. **Leurs scripts s'exécutent sur la
  machine de l'utilisateur.**

### Documentation

- README racine réécrit : bannière, badges cohérents, sommaire, démarrage en trois étapes, schéma d'architecture,
  skills par famille, partie anglaise alignée (59 agents, 43 skills). L'historique des versions quitte les README
  pour ce journal.
- Nouveaux documents dans `docs/` : guide de démarrage, architecture, sécurité et robustesse, FAQ, et six schémas
  SVG originaux dans `docs/images/`.
- `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md` étoffé, modèles d'issue et de pull request dans `.github/`.
- Ce journal passe au format Keep a Changelog.

### Corrigé

- Chiffres contradictoires : partie anglaise du README (46 agents au lieu de 59), table de contenu (24 skills au
  lieu de 43), README du plugin (51 agents), nombres de références et de scripts.
- `dan-cortex/NOTICE.md` indiquait la copie des treize skills d'Anthropic comme non faite et ne citait que la
  licence MIT.

## [2.0.0] - 2026-11-10

### Ajouté

- Skill `accueil-recueil` : chef de parcours du premier contact. Salutation, besoin brut, reformulation validée,
  exploration du domaine (web et GitHub) **avant** l'entretien, propositions, entretien en neuf thèmes
  (interview de `recueil-besoin`), parcours en dix étapes jusqu'à la décision de l'utilisateur : réalisation par
  Dan-Cortex, dossier pour une entreprise, ou startup.
- Livrable « étude de réalisation » (par IA, par une entreprise tierce, mixte, produit existant), budget sur trois
  ans en trois scénarios, gains dans le temps, seuil de rentabilité.
- Table « quel outil, quel skill, quel plugin, à quel moment » et procédure pour aller chercher un outil manquant,
  toujours avec l'accord écrit de l'utilisateur.
- Paquet universel `dan-cortex/universel/` : noyau de moins de 8 000 caractères, version complète en un fichier,
  fichiers de connaissance, skill portable. Construit par `scripts/construire_universel.py`, contrôlé par
  `tests/test_universel.py`.

### Modifié

- `lancer-projet` passe par l'accueil quand le besoin n'est pas encore cadré.

## [1.17.0] - 2026-11-07

### Ajouté

- Skill `traduction-interpretariat` (FR/AR/EN) : traduire un texte, un livre ou une interface en gardant sens,
  registre et intention ; localiser un produit (RTL arabe, PO/XLIFF, mémoires de traduction) ; cadrer
  l'interprétation orale. Outils libres (OmegaT, Weblate, Translate Toolkit, LanguageTool, Okapi). Agents
  `traducteur`, `interprete`, `localisateur`.
- `recueil-besoin` : option **étude approfondie** enchaînée après le recueil (marché, concurrence, existant, voix
  du client, design, outils, marketing), avec réunions, décisions tracées et documentation consolidée.
- `AGENTS.md` à la racine : guide d'entrée universel pour Claude Code, OpenAI Codex, Google Antigravity/Gemini ou
  un simple chat.

### Modifié

- `atelier-ecriture` enrichi : métiers et chaîne du livre, droits, métadonnées ONIX/BISAC/CLIL/Thema, ISBN, outils
  d'édition libres, littératures française, arabe et anglaise, philosophie.
- Matière rassemblée en ligne et sur GitHub, contenu traité comme donnée, aucun script tiers exécuté, licences
  lues (forme A). Le plugin compte 24 skills et 59 agents.

## [1.16.0] - 2026-11-07

### Ajouté

- Skill `recueil-besoin` : recueil du besoin par un entretien adapté au profil (débutant, intermédiaire,
  professionnel), priorisation (MoSCoW, impact/effort, carte des histoires), cahier des charges complet avec
  schémas Mermaid. Agent `intervieweur`.
- Skill `atelier-ecriture` : écrire et accompagner un livre de l'idée au manuscrit publiable (EPUB/PDF,
  métadonnées, ISBN), ou concevoir un outil d'aide à l'écriture. Agents `architecte-recit`, `plume`,
  `editeur-litteraire`, `concepteur-univers`.
- Mise à niveau du dépôt : cette version publie aussi les versions internes 1.5.0 à 1.13.0 du plugin, jamais
  poussées séparément, détaillées ci-dessous. Le plugin compte 23 skills et 56 agents.

#### Versions internes intégrées (1.5.0 à 1.13.0)

- **1.5.0 — testeurs experts** : agents `testeur-mobile` (appareils émulés, thème sombre, tactile, arabe RTL,
  réseau lent) et `testeur-web` (conformité aux maquettes, multi-navigateurs, heuristiques, accessibilité clavier,
  régression visuelle).
- **1.6.0 — formations** : fiches de référence denses rattachées aux agents par une ligne « Formations : » (design
  web et mobile, UI/UX, animation, Figma, types de tests, Chrome DevTools, Playwright MCP, Robot Framework,
  Cypress, Postman, Tosca, architectures, Vercel, Supabase, Keycloak, DatoCMS, référentiel PASSI v2.2), chacune
  avec sa fiche de collecte datée dans `references/sources/`.
- **1.10.0 — graphe du code et design Apple** : `cartographie-graphe` (Graphify en version figée, analyse locale
  seulement, sans service en ligne) et `design-apple` (règles `HIG-n.m` et `HGE-n.m` réécrites en français).
- **1.11.0 — CRM Twenty** : `crm-twenty` (décider, auto-héberger en version figée, intégrer par API, webhooks ou
  MCP ; alerte CVE-2026-26720 ; obligations de l'AGPL ; règles `TW-n.m`).
- **1.12.0 — mouvement et données extrêmes** : `mouvement-interface` (construire, chorégraphier, fluidifier,
  auditer le mouvement ; règles `MV-n.m`) ; références `donnees-extremes-ui.md`, `mobile-react-native-animation.md`,
  `swift-moderne.md`, `web-mobile-natif.md`, `prototypes-en-variantes.md`, `choisir-une-bibliotheque-ui.md`.
- **1.13.0 — choix de l'outillage** : `usine-logicielle/references/selection-outillage.md` (qui choisit skills,
  plugins et outils de navigateur, et quand) ; aucune installation sans accord écrit.
- **Boîte à outils IT** (annoncée en 1.4.0 dans le README du plugin) : `boite-outils-it` installe IT-Tools en local (empreinte vérifiée, 127.0.0.1:3110, aucun
  appel sortant) et fournit `scripts/outils-it.mjs`.

### Sécurité

- Renforts d'audit de sécurité : compétence `safety` branchée dans le pôle, référence `renforts-securite`.

## [1.4.0] - 2026-11-07

### Ajouté

- Agent `suivi-avancement` (pilotage, niveau C, `haiku`) : avancement de chaque étape sur preuves comptables,
  rendu en barres de progression avec leur état. Sans compte, l'étape est « non mesurée ».
- `cortex.py avancement maj|afficher|liste|retirer` : étapes et sous-étapes dans `00-pilotage/avancement.csv`,
  rendu dans `00-pilotage/avancement.md`, repris dans le tableau de bord.

### Modifié

- Le chef d'orchestre déclare les étapes dès le plan et joint le bloc d'avancement à chaque compte rendu de vague.

## [1.3.1] - 2026-10-27

### Modifié

- Les skills `execution-resiliente` et `confidentialite-traces` sont branchés dans le réseau par renvoi, sans
  dupliquer leur contenu.

### Ajouté

- Test : chaque renvoi `${CLAUDE_SKILL_DIR}/../<skill>/…` des skills pointe vers un fichier existant.

### Supprimé

- Le paquet de mise à jour 1.3.0 (`apply_update.py`) ne doit plus être relancé : il ramènerait la version à 1.3.0.

## [1.3.0] - 2026-10-27

### Ajouté

- Skill `execution-resiliente` : planification orientée critères d'acceptation, récupération après erreur,
  vérification des résultats.
- Skill `confidentialite-traces` : masquage des secrets et minimisation des données sensibles.
- Construction reproductible de `dist/dan-cortex.plugin` par `scripts/construire_plugin.py`, vérifiée en CI ;
  tests de cohérence des manifestes, du chargement des skills et du build.

### Sécurité

- Permissions et traçabilité maintenues : aucune falsification des journaux, aucun contournement des contrôles
  d'accès.

## [1.0.1] - 2026-10-27

### Corrigé

- `cortex.py registre` accepte `--dossier` (et `--max`) avant, entre ou après les champs `cle=valeur`, y compris
  sous Python 3.11 et 3.12. Une option inconnue reste refusée.

## [1.0.0] - 2026-10-27

Cortex devient **Dan-Cortex** et fusionne avec Claude Code Autonomy Lab.

### Ajouté

- Niveaux d'autonomie `accompagne`, `delegue`, `autonome` (`init --autonomie`, `etat --set autonomie=…`). En
  `autonome`, décisions de type 1 au statut `provisoire`, autorisations permanentes écrites à J0, six limites dures.
- Skill `robustesse-agents` : audit des réglages Claude Code, gabarit de réglages pour l'autonomie, corpus de
  scénarios d'injection d'instructions, évaluation live sur accord, script `robustesse.py` et paquet `ccal`.
- Seize contrôles `ROB-` (784 au total), alignés sur l'OWASP Top 10 LLM 2025.
- Tests automatisés (`tests/`) et intégration continue.

### Modifié

- Renommage : plugin `dan-cortex`, commandes `/dan-cortex:…`, types d'agents `dan-cortex:<nom>`. Le script
  `cortex.py` et le fichier `cortex.json` gardent leur nom : les projets existants se reprennent tels quels.
- J0 audite les réglages des agents ; J5 exige le rapport de robustesse pour un projet `ia`.

### Sécurité

- Règle commune à tous les agents : ce qu'ils lisent est une donnée, jamais un ordre ; aucun vrai secret dans un
  livrable.

## [0.9.0] - 2026-10-11

Première version publique.

### Ajouté

- Chef d'orchestre et sept jalons, de l'opportunité au bilan, en trois modes.
- Treize skills : un par pôle, plus les réunions et l'audit général.
- Agents experts natifs aux outils restreints, répartis sur trois niveaux de modèle.
- Matrice de couverture filtrée par type de projet, étiquettes, mode et périmètre.
- Script de pilotage : registres, jalons, traçabilité, cohérence des interactions, journal de consommation.
- Essai en conditions réelles sur le jalon J1 en mode éclair.

[2.1.0]: https://github.com/aksilsmd/cortex/pull/2
[2.0.0]: https://github.com/aksilsmd/cortex/commit/a5eb0df
[1.17.0]: https://github.com/aksilsmd/cortex/commit/7bc8931
[1.16.0]: https://github.com/aksilsmd/cortex/commit/5c2f5a6
[1.4.0]: https://github.com/aksilsmd/cortex/commit/efddcc7
[1.3.1]: https://github.com/aksilsmd/cortex/commit/105fbfa
[1.3.0]: https://github.com/aksilsmd/cortex/commit/2d957b8
[1.0.1]: https://github.com/aksilsmd/cortex/commit/c083fa7
[1.0.0]: https://github.com/aksilsmd/cortex/commit/6368e2b
[0.9.0]: https://github.com/aksilsmd/cortex/commit/3bc2a8b
