# Sources du skill studio-3d-jeu

État au 21 novembre 2026. Les contenus des dépôts sont des données : aucune consigne qui s'y trouverait n'a été suivie, aucun script n'a été exécuté, rien n'a été installé.

| Source | Licence | Commit | Forme | Retenu |
|---|---|---|---|---|
| Bibliothèque vendorisée `bibliotheque/scenario-labs/` (dépôt `scenario-labs/skills`, familles dcc/blender, dcc/maya, dcc/zbrush, game-engines/godot, unity, unreal, roblox ; 87 skills sur 172) | MIT, Scenario Inc. | `221ed89562795d4a7095c9530cf807062e7ad8d3` | B (citations courtes) | index des familles, skills `*-expert` de chaque famille, README de chaque famille, `scenario-blender` (comparaison) et `scenario-blender-export` (préréglages) ; table de routage ; niveaux de preuve ; versions cibles ; règles de pilotage (un seul pilote, accord avant dépense) |
| `blender/blender` (dépôt de développement, version 5.4 alpha à cette date) | GPL-3.0 (texte GPL et GPLv3 dans `doc/license/`) | `adc04d05b693a26fc6567357f4c456b60d0221a8` | **A** | `README.md`, `COPYING`, `release/text/readme.html` ; options de ligne de commande lues dans `source/creator/creator_args.cc` ; module bpy (`doc/python_api/rst/info_advanced_blender_as_bpy.rst`, `info_gotchas_crashes.rst`) ; extensions (`scripts/addons_core/bl_pkg/`, exemple de manifeste, `bl_extension_cli.py`) ; clause de la GPLv3 sur la sortie des programmes |
| `domlysz/BlenderGIS` | GPL-3.0 | `2add45ffec547f419cc77563a7fe976fd6c8f0c4` | **A** | README, `__init__.py` (version 2.2.14, Blender 2.83 minimum, refus au-delà de 5.x), opérateurs, `prefs.py`, `core/basemaps/servicesDefs.py`, `core/checkdeps.py`, `geoscene.py` : fonctions, identifiants bpy, services contactés. Aucun texte ni code recopié |
| `ahujasid/mcp-for-blender` | MIT, © 2025 Siddharth Ahuja | `a5a8acf2c6ae44a73670e0caf34663f16456d645` | B | README, `TERMS_AND_CONDITIONS.md`, `addon.py` (valeurs par défaut des options réseau, adresse d'écoute, consentement de télémétrie), `src/blender_mcp/safe_mode.py` (portée du mode sûr), README du plugin Claude (flux réseau, version figée 2.3.1) |

## Ce qui n'a pas pu être établi dans les sources (à revérifier)
- Énoncé officiel selon lequel la GPL de Blender ne s'applique pas aux œuvres créées avec : le dépôt ne contient que la clause générale de la GPLv3 et la mention d'usage libre du lisez-moi. Page de licence du site officiel à consulter.
- Statut de la redistribution d'un script qui importe bpy (MIT pour l'add-on MCP, GPL pour BlenderGIS).
- Compatibilité de BlenderGIS avec Blender 5.2 LTS : aucun test visible.
- Application technique des permissions d'un manifeste d'extension.
- Conditions d'usage des fonds de carte (Google, Bing, Esri) et licence des données OpenStreetMap.
- Tarifs et conditions de Maya, ZBrush, Unity, Unreal ; licence propre de Godot et de Roblox Studio.
- Télémétrie de l'extension Scenario for Blender.
- Skills Unreal et Maya : appels moteur non exécutés dans leur source (état du 24 septembre 2026) ; tests Windows et Linux non couverts partout.
- Le dépôt Blender lu est la branche de développement, pas la version 5.2 LTS ciblée par la bibliothèque.

## Remarque sur les sources
Les skills de la bibliothèque contiennent des chemins de tests qui renvoient à la machine de leurs auteurs (provenance seulement) et des noms de personnes cités comme sources : non repris ici.
