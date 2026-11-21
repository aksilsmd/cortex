# Choisir un moteur de jeu : Godot, Unity, Unreal ou Roblox

Le choix se fait sur le cadrage, pas sur la préférence de l'agent. Il se consigne dans un ADR (`${CLAUDE_SKILL_DIR}/../architecture-normes/SKILL.md`) avec les alternatives écartées. Les faits ci-dessous viennent des SKILL.md experts de la bibliothèque (`${CLAUDE_PLUGIN_ROOT}/bibliotheque/scenario-labs/skills/game-engines/`) ; les orientations sont des recommandations de méthode à confronter au projet.

## Questions de cadrage
1. Plateforme de sortie : PC, mobile, navigateur, console, plateforme Roblox.
2. 2D ou 3D, taille du monde, besoin de rendu haut de gamme ou de cinématiques.
3. Multijoueur : local, en ligne, géré par la plateforme ou par nous.
4. Compétences : GDScript, C#, C++ et Blueprints, Luau.
5. Budget : licences, services, équipe. Chiffrer sur trois ans avec `${CLAUDE_SKILL_DIR}/../budget-finance/SKILL.md`.
6. Machine réelle de l'équipe : les procédures de la bibliothèque sont testées surtout sous macOS.

## Fiche par moteur (cibles de la bibliothèque)
| | Godot 4.7 | Unity 6.3 LTS | Unreal 5.8 | Roblox Studio |
|---|---|---|---|---|
| Langage | GDScript (version standard sans C#) | C# | C++ et Blueprints | Luau |
| Licence d'usage | aucune connexion ni licence demandée | licence personnelle : connexion au Hub, retour en ligne tous les 30 jours | à revérifier | compte Roblox connecté |
| Sorties vues dans la bibliothèque | macOS, Windows, Linux, Android, iOS (projet Xcode), web | PC, Android, iOS, WebGL | cuisson et paquet par UAT (`BuildCookRun`) ; cible Mac Apple Silicon | plateforme Roblox seule |
| Pilotage sans souris | scripts `--headless`, tests GUT | mode batch `-executeMethod`, Unity CLI | Python d'éditeur, serveur MCP d'Epic expérimental | serveur MCP intégré à Studio |
| Preuve dans la source | 14 skills joués en réel (macOS) | 14 joués en réel (macOS) | 10 skills, appels moteur **non exécutés** | 14 joués en réel (macOS) |

## Orientations par projet
| Projet | Piste | Pourquoi, et réserve |
|---|---|---|
| Jeu 2D, prototype, petite équipe, coût nul | Godot | skill 2D, export web et mobile documentés ; les installations sur téléphone et les dépôts sur stores n'ont pas été rejoués dans la source |
| Jeu mobile ou WebGL à écosystème large | Unity | skills mobile (budget d'image, chauffe, textures ASTC ou ETC2) et web (compression, en-têtes serveur) ; licence et conditions à revérifier |
| 3D réaliste, grands mondes, cinématiques | Unreal | skills monde (World Partition), éclairage (Lumen), effets (Niagara), cinématiques (Sequencer) ; aucun skill dédié mobile, web ni interface ; source non exécutée : prévoir un essai |
| Jeu pour la plateforme Roblox, monétisation et données joueurs | Roblox | skills données, anti-triche réseau, monétisation ; le jeu ne sort que sur Roblox |
| Expérience 3D de site, défilement, configurateur | aucun moteur | `${CLAUDE_SKILL_DIR}/../web-3d-immersif/SKILL.md` (three.js, WebGL) |
| Images, textures ou modèles à générer par IA | hors moteur | `${CLAUDE_SKILL_DIR}/../creation-medias-ia/SKILL.md`, puis finition dans Blender |

Aucun moteur ne se déduit d'un seul critère : si deux pistes restent ouvertes, convoquer `${CLAUDE_SKILL_DIR}/../reunion-decision/SKILL.md`.

## Du DCC au moteur : formats de la bibliothèque
Préréglages du skill `dcc/blender/scenario-blender-export` : Unity en FBX (squelettique : option propre) ; Unreal en FBX, échelle en centimètres, un seul os racine ; Godot en GLB ; Roblox en FBX, 20 000 triangles par maillage au plus (vérifié par la source le 18 octobre 2026) ; web en GLB compressé ; USD, USDZ pour AR, STL pour l'impression. Les préréglages Unity et Godot ont été réimportés et mesurés dans ces moteurs ; **Unreal et Roblox n'ont passé que le contrôle de réimport dans Blender**. Règle : un export n'est fini qu'une fois réimporté et mesuré (échelle, orientation, textures, animation).

## Licences et coûts
- Maya et ZBrush : logiciels commerciaux ; Unity : niveaux de licence ; Unreal : conditions propres. Aucune grille tarifaire n'est dans les sources : **à revérifier sur les sites officiels à la date de la décision**, puis à inscrire au budget (`controleur-financier`).
- Sans licence à acheter : Blender (GPL, usage libre selon son lisez-moi) et Godot. Cela ne dispense pas de contrôler les licences des assets tiers (`${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md`).
- Maya : un siège de licence est occupé par une instance graphique ; Arnold en batch sans licence dédiée ajoute un filigrane (source : skill expert Maya). Ne pas lancer d'instance sans accord.
- Publication (stores, Roblox, dépense de Robux, achats d'assets) : jamais sans accord explicite de l'utilisateur.

## Après le choix
1. Ouvrir `index/game-engines-<moteur>.md`, puis le skill `*-expert` du moteur, puis **un seul** spécialiste (table de routage de `${CLAUDE_SKILL_DIR}/../studio-3d-jeu/SKILL.md`).
2. Fixer les budgets mesurables avant de produire : triangles, taille de textures, millisecondes par image sur l'appareil visé (16,67 ms à 60 images par seconde ; le skill expert Unity ne vise qu'environ 65 % du budget d'image sur mobile, pour la chauffe).
3. Un éditeur graphique ouvert sur un projet interdit d'y travailler en parallèle en ligne de commande : passer par lui.
4. Mise en production et stores : `${CLAUDE_SKILL_DIR}/../lancement-exploitation/SKILL.md` ; code et tests hors moteur : `${CLAUDE_SKILL_DIR}/../usine-logicielle/SKILL.md`.
