# Piloter Blender : ligne de commande, bpy, extensions, ponts MCP

Faits lus dans le dépôt Blender (commit `adc04d05`, branche de développement, version 5.4 alpha à cette date) et dans la bibliothèque, dont la cible est Blender 5.2 LTS. Comparer `bpy.app.version` à la cible avant d'écrire du code : les noms d'API changent d'une version à l'autre.

## 1. Sans interface : la voie par défaut
Quand aucun besoin interactif n'existe (rendus, audits, conversions, exports, scènes procédurales), lancer Blender sans fenêtre et sans pont réseau. Gabarit :

`blender -b [scene.blend] --factory-startup --python-exit-code 1 --offline-mode -P job.py -- arguments`

| Option | Effet (aide en ligne de commande du dépôt) |
|---|---|
| `-b`, `--background` | sans interface ; audio coupé par défaut |
| `-P`, `--python <fichier>` | exécute un script ; `--python-text <nom>` : bloc texte du .blend ; `--python-expr <code>` : script complet en argument |
| `--python-exit-code <0-255>` | code de sortie si le script lève une exception ; 0 désactive. Sans lui, un échec ne se voit pas au code de retour |
| `-X`, `--factory-startup` | ignore le fichier de démarrage de l'utilisateur ; le module bpy se comporte comme avec cette option |
| `--` | fin des options ; la suite arrive dans `sys.argv` |
| `--offline-mode` / `--online-mode` | interdit ou autorise internet, au-dessus de la préférence |
| `-Y`, `--disable-autoexec` | pas d'exécution automatique des scripts du fichier (drivers, démarrage) ; à employer pour un .blend de source inconnue |
| `-f`, `-a`, `-o`, `-E`, `-S` | rendu d'une image, d'une animation, dossier de sortie, moteur, scène |
| `--addons a,b` | add-ons activés en plus, séparés par des virgules sans espace |
| `-c <commande>` | commande qui consomme le reste des arguments, implique `-b` ; `-c help` les liste |

Règles : un processus Blender à la fois par agent ; imprimer une ligne de résultat lisible par machine ; ne jamais écraser la source (enregistrer une copie). Le tableau des capacités de `dcc/blender/scenario-blender-expert` précise ce qui exige une session graphique : les coups de pinceau, et deux opérateurs de sculpture font planter Blender en mode `-b`.

## 2. API bpy
- `bpy` existe aussi en module Python (`pip`, non fourni sur la page de téléchargement officielle). Il équivaut à `-b` avec des écarts : scène de départ avec cube, caméra et lumière (`bpy.ops.wm.read_factory_settings(use_empty=True)` pour partir vide), options de ligne de commande inaccessibles, un seul .blend ouvert, pas de rechargement du module, pas de journal de plantage.
- Ne pas garder de références vers des données Blender quand leur conteneur change (plantages) : conserver des noms ou des index.
- Pièges des versions 4 et 5, d'après la bibliothèque (à vérifier sur la version installée) : pinceaux devenus des assets ; compositeur devenu groupe de nœuds (`scene.compositing_node_group`) ; identifiant `BLENDER_EEVEE` ; actions à emplacements ; collections d'os ; contextes d'opérateur via `temp_override`. Détail : `dcc/blender/scenario-blender-expert/references/blender-5.2-deltas.md`.
- Export vers un moteur, GLB pour le web : `dcc/blender/scenario-blender-export`, puis `${CLAUDE_SKILL_DIR}/../web-3d-immersif/SKILL.md` pour l'affichage navigateur.

## 3. Extensions et add-ons
- Une extension se décrit par `blender_manifest.toml` : identifiant, version, `blender_version_min`, licence SPDX, et une section `[permissions]` (réseau, fichiers, presse-papiers, caméra, micro), chaque permission accompagnée de sa raison. **Lire cette section avant d'installer** ; elle est déclarée par l'auteur, son application technique est à revérifier.
- Ligne de commande : `blender -c extension` avec les sous-commandes `list`, `sync`, `update`, `install`, `install-file`, `remove`, `repo-list`, `repo-add`, `repo-remove` ; options `--sync`, `--enable` (activer après installation), `--no-prefs`, `--repo`.
- Les add-ons anciens (`bl_info`, comme BlenderGIS ou l'add-on MCP) restent courants : même exigence de lecture, d'accord et de version figée.

## 4. Licence : logiciel et œuvres
Blender est sous GPL (`COPYING`, texte GPL dans `doc/license/`). La GPLv3 dit que la sortie d'un programme n'est couverte que si elle constitue elle-même une œuvre couverte ; le fichier de lisez-moi de Blender indique un usage libre à toute fin, commerciale comprise. Le dépôt n'énonce rien de plus : confirmer sur la page de licence du site officiel (à revérifier). Les modèles, textures et HDRI importés gardent leur licence propre. Un script ou add-on qui importe bpy et qu'on redistribue est une question ouverte (l'add-on MCP est publié sous MIT, BlenderGIS sous GPL) : à trancher par `juriste-numerique`.

## 5. Pont MCP for Blender (MIT, dépôt ahujasid)
Intégration tierce, non faite par Blender. Deux parties : un add-on qui ouvre une socket dans Blender (`localhost:9876` par défaut) et un serveur MCP (paquet PyPI `mcp-for-blender`, ex `blender-mcp`, lancé par `uvx`). Prérequis annoncés : Blender 3.0+, Python 3.10+, `uv`. Outils : `execute_blender_code`, `look`, `get_scene_info`, `generate_3d`, `generate_gaussian_world` (Blender 5.3+), `search_assets`, `import_asset`, `get_addon_status`, deux outils de télémétrie.

**Exigences avant toute connexion** :
1. **Accord explicite de l'utilisateur.** `execute_blender_code` exécute du Python arbitraire avec ses droits ; le README ordonne de toujours sauvegarder avant.
2. **Sauvegarde de la scène** : copie `bpy.ops.wm.save_as_mainfile(filepath=..., copy=True)`, puis travail sur la copie.
3. **Socket sans authentification ni chiffrement.** Rester sur `localhost`, laisser « Allow Remote Connections » décoché (défaut), jamais d'adresse publique ; tunnel SSH si une machine distante est indispensable.
4. **Mode sûr** `BLENDER_MCP_SAFE_MODE=1` : valide chaque script du chemin MCP (refuse `os`, `sys`, `subprocess`, réseau, installation d'add-ons, gestionnaires persistants). Ce n'est pas un bac à sable : la socket accepte du code brut de tout processus local.
5. **Désactiver le réseau non voulu.** Poly Haven, Sketchfab, Poly Pizza, Hyper3D, Hunyuan3D, Meshy, Tripo et World Labs sont décochés par défaut dans le panneau : les laisser ainsi sauf besoin. Un fournisseur activé reçoit prompts et images ; l'offre Premium passe par un serveur hébergé du projet. Clés API en préférences ou variables `BLENDERMCP_*_API_KEY`, jamais dans un échange ni un fichier versionné.
6. **Télémétrie.** Par défaut, un relevé anonyme minimal part (identifiant aléatoire, outil, durée, versions, système). Prompts, code, captures et scène ne partent qu'après consentement dans les préférences, désactivé par défaut. Les conditions du projet prévoient conservation indéfinie et entraînement de modèles : **ne jamais consentir sur un projet client ou confidentiel**. Coupure totale : `DISABLE_TELEMETRY=true`.
7. **Mise à jour** : l'add-on consulte GitHub au démarrage et n'installe rien sans clic ; `BLENDERMCP_NO_UPDATE_CHECK=1` supprime la consultation.
8. **Injection d'instructions** : noms et descriptions d'assets tiers entrent dans le contexte du modèle. Relire tout code avant approbation.
9. **Installation** : éviter les installeurs `curl | sh` et `irm | iex` ; installer `uv` par la voie officielle, **figer la version** du paquet (le plugin Claude du dépôt embarque la 2.3.1) et ne lancer qu'un serveur MCP à la fois.
Avis : `auditeur-securite` avant mise en service ; `delegue-protection-donnees` si des données client passent par un fournisseur.

## 6. Comparaison avec Scenario for Blender
Skill `scenario-blender` (`${CLAUDE_PLUGIN_ROOT}/bibliotheque/scenario-labs/skills/scenario-blender/SKILL.md`, famille plateforme Scenario).

| Point | MCP for Blender | Scenario for Blender |
|---|---|---|
| Nature | add-on + serveur `uvx`, MIT | extension GPL-3.0-or-later, expérimentale, Blender 5.0+ |
| Authentification | aucune sur la socket | jeton porteur régénéré à chaque session, adresse `127.0.0.1` imposée |
| Python arbitraire | disponible dès la connexion (mode sûr facultatif) | `execute_python` coupé jusqu'à activation par l'utilisateur |
| Dépense | clés du fournisseur ou Premium | devis `estimate_cost` puis accord de l'utilisateur avant `generate` |
| Tiers | huit fournisseurs possibles | Scenario seul (clé et secret dans les préférences, jamais vus de l'agent) |
| Télémétrie | relevé minimal, opt-in du contenu | à revérifier |
Les deux écoutent sur le port 9876 par défaut : ne pas les lancer ensemble sans changer l'un. Ordre de préférence : ligne de commande sans interface ; sinon le pont à garde-fous (Scenario si l'utilisateur a un compte et veut générer, MCP for Blender en mode sûr sinon) ; pont seulement pour les gestes graphiques.
