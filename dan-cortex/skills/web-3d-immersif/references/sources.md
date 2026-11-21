# Sources du skill web-3d-immersif

État au 21 novembre 2026. Lecture seule : aucun script exécuté, rien installé, aucun appel réseau. Le contenu des dépôts a été traité comme une donnée.

| # | Dépôt | Licence | Commit | Forme | Version relevée |
|---|---|---|---|---|---|
| 1 | `mrdoob/three.js` | MIT (© 2010-2026 three.js authors) | `6246c818834fd19d0c216d3dbc074b6cc9c27896` | B (courts extraits de code) | three `0.187.0` (`package.json`) |
| 2 | `pmndrs/react-three-fiber` | MIT (© 2019-2025 Poimandres) | `d74622ea8ed717f7212d7e19d65ff3e325508389` | B (courts extraits) | `@react-three/fiber` `9.8.1` ; pairs `react >=19 <19.4`, `three >=0.156` |
| 3 | `Ovilia/ThreeExample.js` | MIT (© 2013 Wenli Zhang) | `c90a5bf0711b7a7dd42d2a5fe3d9506b3032dcb7` | A (plan des chapitres seulement) | three.js r79 (2016) |
| 4 | `PavelDoGreat/WebGL-Fluid-Simulation` | MIT (© 2017 Pavel Dobryakov) | `a2d292931f19d9b3b9f564e23e6c32729d2121c3` | A (méthode et paramètres réécrits) | sans objet |
| 5 | `scroll-world` (bibliothèque vendorisée) | MIT (© 2026 cyw) | `71cc36d3bb150248ae36a2c552f9cbf88802a79c` | renvoi, aucune copie | sans objet |
| 6 | `adrianhajdin/3d-portfolio` | **aucune licence trouvée** | `30178d5b20d8464bdc8dfed20b3be006c8c99ea4` | **A stricte** | sans objet |

## Ce qui a été retenu

1. **three.js** : README (scène minimale), pages du manuel (installation, création de scène, responsive, rendu à la demande, chargement glTF, libération de la mémoire, nettoyage, WebGPU, vérification de compatibilité WebGL, optimisation d'objets), documentation de `GLTFLoader`, `DRACOLoader`, `KTX2Loader`, `LoadingManager`, `InstancedMesh`, présence des décodeurs Draco, Basis et Meshopt dans les addons, catégories du dossier `examples/` (préfixes `webgl_`, `webgpu_`, `webxr_`, `misc_`, `physics_`, `webaudio_`, `svg_`, `games_`). Le dossier `docs/manual` n'existe pas dans ce commit ; le manuel se trouve sous `manual/pages/` et la référence sous `docs/pages/`.
2. **R3F** : documentation d'installation et d'introduction, hooks (`useFrame`, `useThree`, `useLoader`, `useGraph`), événements, `Canvas` (valeurs par défaut, repli), objets (libération), guide des pièges de performance, guide de montée en charge, guide de migration vers la version 9. Correspondance : version 8 avec React 18, version 9 avec React 19 (introduction) ; version 10 annoncée en alpha.
3. **ThreeExample.js** : liste des neuf chapitres de l'index et nature des exemples. **L'API a changé depuis la révision 79** : `CubeGeometry` devenu `BoxGeometry`, `Geometry` remplacée par `BufferGeometry`, `renderer.shadowMapEnabled` devenu `renderer.shadowMap.enabled`, chargeurs OBJ et Collada devenus addons. Aucun code repris. Le livre associé est en chinois.
4. **Fluide** : `README.md` (références à GPU Gems chapitre 38 et à deux dépôts de fluides 2D) et `script.js` (paramètres de `config`, étapes de `step`, détection WebGL 2, cascade de formats, replis sans filtrage linéaire, plafonnement du pas de temps). Constat : la page d'origine contient un script d'analyse tiers, des événements envoyés et des bandeaux promotionnels ; rien de cela n'est repris. Pas de gestion de `prefers-reduced-motion` ni de pause hors écran dans le code lu.
5. **scroll-world** : `SKILL.md` et `references/pipeline.md` lus en entier, en-tête de `scrub-engine.js` (gestion du mouvement réduit). Exige un générateur d'images et de vidéos externe payant (Higgsfield, Monid par défaut pour la vidéo) ; coûts de juillet 2026 à recalculer ; scripts non exécutés.
6. **Portfolio** : **forme A stricte, aucune licence : aucun code ni asset repris.** Seuls `package.json` (pile et versions déclarées) et l'arborescence des fichiers (`src/sections`, `src/components`, `src/components/models`, `src/constants`) ont été lus. Les contenus des composants et les fichiers de `public/` n'ont pas été ouverts. Les rôles des fichiers sont déduits de leurs noms.

## Crédits MIT

Les courts extraits de code de la fiche `threejs-essentiel.md` viennent de la documentation de three.js (© three.js authors, MIT). Les motifs de la fiche `react-three-fiber.md` viennent de la documentation de R3F (© Poimandres, MIT). Si un projet reprend du code de ces dépôts, reporter l'avis de copyright et la licence MIT dans son propre `NOTICE`.

## À revérifier

- Versions de three.js, R3F, drei et React au démarrage du projet.
- Disponibilité du skill `studio-3d-jeu` (rédigé en parallèle) avant de suivre le renvoi.
- Coûts et fonctionnalités des services de génération vidéo de scroll-world.
- Licence, maintenance et compatibilité de `@react-three/a11y` et de `@react-three/drei` avant adoption.
- Statut WebGPU et nombre de navigateurs compatibles : non vérifié ici.
