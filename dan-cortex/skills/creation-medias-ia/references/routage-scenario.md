# Routage : besoin vers SKILL.md de la bibliothèque Scenario

Tous les chemins se lisent `${CLAUDE_PLUGIN_ROOT}/bibliotheque/scenario-labs/skills/<dossier>/SKILL.md`. Seul le nom du dossier est donné ci-dessous. Règle de lecture : le skill racine `scenario` d'abord (boucle de génération, portée, erreurs), puis **un seul** skill du besoin, puis ses `references/` à la demande. Quand un skill dit « load sibling skill X », X se trouve dans cette liste, à lire en local ; ne rien installer. Les descriptions d'origine sont en anglais ; les familles de modèles sont détaillées par fournisseur.

## Socle et exploration

| Besoin | Dossier |
|---|---|
| Connexion MCP, portée, boucle découvrir-schéma-exécuter-attendre, erreurs et quotas | `scenario` |
| Aucune direction visuelle : pistes, planche d'inspiration | `scenario-inspiration` |

## Images

| Besoin | Dossier |
|---|---|
| Texte vers image, image vers image, retouche par instruction, masque, formats | `scenario-image` |
| Édition par modèle-outil : agrandissement, étalonnage, détourage, extension, découpe | `scenario-image-editing` |
| Une image composée de plusieurs références | `scenario-multi-reference` |
| Texte exact superposé (slogans, prix, mentions) | `scenario-text-overlay` |
| Décliner un visuel validé en formats et placements | `scenario-formats` |
| Familles de modèles image | `scenario-gpt-image`, `scenario-mai-image`, `scenario-seedream`, `scenario-gemini-image`, `scenario-reve`, `scenario-ideogram`, `scenario-grok-imagine-image`, `scenario-luma-image` |

## Vidéo

| Besoin | Dossier |
|---|---|
| Texte ou image vers vidéo, synchronisation labiale, doublage, extension, mise à l'échelle | `scenario-video` |
| Montage déterministe : coupe, découpe, redimensionnement, effets, étalonnage par modèle-outil | `scenario-video-editing` |
| Assembler des plans en film : chronologie, transitions, logo, musique, sous-titres | `scenario-video-assembly` |
| Étalonnage par code d'une vidéo existante | `scenario-video-color-grade` |
| Boucles graphiques sans couture aux couleurs d'une marque | `scenario-motion-loops` |
| Films en typographie animée | `scenario-kinetic-film`, `scenario-kinetic-music-video` |
| Clip musical depuis une chanson | `scenario-seedance-music-video` |
| Mouvement continu entre plans (danse, combat) | `scenario-seedance-storyboard` |
| Prises d'essai bon marché avant la version finale | `scenario-seedance-drafts` |
| Familles de modèles vidéo | `scenario-kling`, `scenario-veo`, `scenario-seedance`, `scenario-gemini-omni`, `scenario-luma-video`, `scenario-runway`, `scenario-grok-imagine-video`, `scenario-wan`, `scenario-minimax-video`, `scenario-vidu` |

## Audio, musique, voix

| Besoin | Dossier |
|---|---|
| Musique, bruitages, voix off, dialogue, chansons, sonorisation d'une vidéo | `scenario-audio` |
| Sous-titres incrustés ou fichier de sous-titres, traduction | `scenario-caption-studio` |
| Familles audio | `scenario-elevenlabs`, `scenario-ace-step`, `scenario-minimax-music`, `scenario-sonilo` |

## 3D

| Besoin | Dossier |
|---|---|
| Maillage depuis un texte ou une image, retexture, remaillage, dépliage UV, rigging | `scenario-3d` |
| Mondes 3D navigables, splats gaussiens | `scenario-3d-worlds` |
| Animation 3D depuis une vidéo de référence | `scenario-video-to-motion` |
| Nouveaux angles de caméra d'une même image | `scenario-orbit-views` |
| Pièce explorable dans un navigateur depuis une photo | `scenario-walkable-room` |
| Retexture PBR d'un maillage fini | `scenario-patina-retexture` |
| Familles 3D | `scenario-meshy`, `scenario-rodin`, `scenario-sparc3d` |

## Textures et skyboxes

| Besoin | Dossier |
|---|---|
| Textures sans couture, matériaux PBR | `scenario-textures` |
| Panoramas 360, skyboxes, cartes d'environnement | `scenario-skyboxes` |

## Jeu

| Besoin | Dossier |
|---|---|
| Sprites, icônes, accessoires, tuiles, pixel art | `scenario-game-assets` |
| Cycles d'animation 2D, feuilles de sprites, GIF | `scenario-sprite-animation` |
| Art de jeu de plateforme en vue de côté | `scenario-side-view-game-kit` |
| Pubs jouables HTML5 | `scenario-playable-ads` |
| Vidéos publicitaires d'acquisition pour jeu mobile | `scenario-game-ua-ads` |
| Plan 2D animé dans Blender depuis des images | `scenario-blender-2d-animation` |

Les skills `scenario-blender`, `scenario-zbrush-*`, `scenario-maya-*`, Unity, Unreal, Godot et Roblox pilotent des logiciels installés : relèvent de `studio-3d-jeu`, pas de ce skill.

## Marketing

| Besoin | Dossier |
|---|---|
| Déclinaisons de campagne depuis des rushs existants | `scenario-ad-variants` |
| Photos produit depuis une vraie photo | `scenario-product-shots` |
| Miniatures et couvertures vidéo | `scenario-thumbnails` |
| Vidéo style créateur (témoignage, démonstration) | `scenario-ugc` |
| Spot publicitaire depuis un visuel produit | `scenario-video-ads` |
| Identité visuelle : logo SVG, palette, typographie | `scenario-brand-kit` |
| Légendes et sous-titres par destination | `scenario-caption-studio` |

Sensibles : `scenario-fan-cam`, `scenario-reel-recast` et les pets (`scenario-chatgpt-pet-create`, `scenario-chatgpt-pet-update`) manipulent des visages ou des personnages : règle d'or 5 de `SKILL.md`, consentement écrit, jamais de personnalité publique. Les pets exécutent des scripts locaux : jamais sans accord après lecture.

## Narration

| Besoin | Dossier |
|---|---|
| Storyboards, planches, livre illustré | `scenario-storyboards` |
| Bande dessinée, manga, roman graphique | `scenario-comic-creator` |

## Entraînement et cohérence

| Besoin | Dossier |
|---|---|
| Tenir un même style, personnage ou produit sur un ensemble (essayer d'abord) | `scenario-consistency` |
| Personnage ou accessoire réutilisable, nommé | `scenario-identity-library` |
| Entraîner un modèle personnalisé (image, vidéo, voix) | `scenario-model-training` |

L'entraînement est coûteux et irréversible une fois lancé : devis `configure` avec `dry_run`, accord explicite, jamais de visage réel sans consentement.

## Pilotage

| Besoin | Dossier |
|---|---|
| Verdict réussite-alerte-échec sur une image, conformité à un guide de marque | `scenario-quality-gate` |
| Lecture d'assets : légendes, style, vérification contre un brief | `scenario-asset-analysis` |
| Itérer jusqu'à conformité avec critères écrits et plafond de tours | `scenario-refine-loop` |
| Comparer des modèles sur un même brief | `scenario-model-comparison` |
| Génération refusée ou bloquée | `scenario-moderation` |
| Exécuter une application ou un pipeline enregistré | `scenario-workflows` |
| Créer ou modifier un graphe de workflow | `scenario-workflow-authoring` |
| Signaler une anomalie (secrets et données personnelles retirés avant envoi) | `scenario-report` |
| Imputer les coûts à des tâches d'un suivi de tâches | `scenario-task-tracking` |
| Administrer équipe, accès aux modèles, plafonds par membre, clés | `scenario-team-admin` |
| Statistiques de consommation | `scenario-admin-analytics` |

Les actions d'administration (membres, plafonds, clés, accès aux modèles) modifient la configuration d'un compte : accord explicite de l'utilisateur, jamais en autonomie.
