# Performance et accessibilité de la 3D web

Cette fiche mêle des faits lus dans les sources (three.js, R3F, scroll-world, exemple de fluide) et des **recommandations de méthode** de Dan-Cortex, signalées comme telles. Les seuils chiffrés sont des points de départ à mesurer sur l'appareil cible, pas des normes.

## 1. Budget

Fixer le budget **avant** de modéliser, et le consigner dans le dossier du projet (ADR ou spécifications techniques).

| Poste | Repère | Origine |
|---|---|---|
| Appels de dessin | chaque maillage est un appel ; pas plus de 1000 au maximum absolu, idéalement quelques centaines ou moins | documentation R3F |
| Polygones, poids des modèles | à fixer par projet, plus bas sur mobile | recommandation |
| Mémoire de textures | une texture de 1024 x 1024 occupe environ 4 à 6 Mo décompressée en mémoire, même si le fichier JPEG est léger | manuel three.js |
| Ratio de pixels | plafonner (par exemple 2), à mesurer ; R3F : `dpr` par défaut `[1, 2]` | manuel et documentation |
| Images par seconde | cible à fixer (par exemple 60 sur ordinateur, 30 acceptable sur téléphone d'entrée de gamme) | recommandation |
| Poids transféré | budget de page à fixer, modèles et textures compris | recommandation |

Leviers, dans l'ordre : réduire les appels de dessin (fusion de géométries, `InstancedMesh`), réutiliser géométries et matériaux, baisser la résolution de rendu, simplifier les ombres et le post-traitement, niveaux de détail (`LOD` de three.js, `Detailed` de drei).

## 2. Compression glTF (documentée dans three.js)

La documentation de `GLTFLoader` liste les extensions prises en charge, dont `KHR_draco_mesh_compression`, `KHR_meshopt_compression` et `EXT_meshopt_compression`, `KHR_texture_basisu` (textures KTX2), `EXT_texture_webp`, `EXT_texture_avif`, `EXT_mesh_gpu_instancing`, `KHR_mesh_quantization`.

- **Draco** (géométrie) : fichiers nettement plus petits au prix d'un temps de décodage sur l'appareil. Brancher un `DRACOLoader` unique et réutilisé, via `setDRACOLoader`, avec `setDecoderPath`. Le décodeur WASM ou JS est choisi selon le navigateur.
- **KTX2 / Basis** (textures) : le `KTX2Loader` transcode vers le format compressé que le GPU sait lire ; appeler `detectSupport(renderer)` avant le chargement et `setTranscoderPath` vers les fichiers `basis`. Nécessite WebAssembly.
- **Meshopt** : alternative pour la géométrie via `setMeshoptDecoder` avec le module fourni dans les addons.
- Les décodeurs sont des fichiers à servir depuis le site (chemins à configurer), pas une simple importation.
- Outils de compression à utiliser en amont : relèvent de `${CLAUDE_SKILL_DIR}/../studio-3d-jeu/SKILL.md` ; ne rien installer sans accord de l'utilisateur.
- R3F : brancher le chargeur compressé dans l'argument d'extension de `useLoader`.
- Choix pratique (recommandation) : Draco ou Meshopt, pas les deux ; KTX2 pour les textures volumineuses ; comparer le poids total ET le temps de décodage sur téléphone.

## 3. Libération de la mémoire

`dispose()` sur géométries, matériaux, textures, cibles de rendu ; `close()` pour les bitmaps ; contrôles et moteur inutilisables après disposition. En R3F, les objets démontés sont libérés automatiquement, sauf `dispose={null}` ou `primitive`. Diagnostic : `renderer.info`. Détail dans `threejs-essentiel.md`. À tester : monter et démonter la scène vingt fois, la mémoire ne doit pas croître.

## 4. Chargement progressif

- Afficher d'abord le texte et une image fixe (affiche), puis charger la 3D en différé, après le premier affichage.
- Indicateur de progression : `LoadingManager` (three.js) ou, en R3F, `Suspense` avec repli.
- Chargement imbriqué : version basse définition d'abord, haute définition ensuite (modèle documenté dans le guide de performance de R3F).
- Précharger ce qui sera vu bientôt (`useLoader.preload`), pas tout.
- scroll-world charge les clips voisins à l'avance et garde l'image fixe en affiche tant que la vidéo n'a pas peint sa première image.

## 5. Repli sans WebGL

- three.js : le module de détection `WebGL.isWebGL2Available()` (addon `capabilities/WebGL.js`) avant d'initialiser.
- R3F : `<Canvas fallback={...}>` plus une frontière d'erreur pour les pertes de contexte.
- Repli recommandé : image fixe de la scène, ou version statique du contenu, avec le même texte. Le contenu essentiel ne dépend jamais du rendu 3D.
- WebGPU : le moteur sait retomber sur WebGL 2 ; `forceWebGL` pour tester ce chemin.
- Tester avec le GPU désactivé et dans un navigateur sans WebGL, via `testeur-visuel`.

## 6. Mouvement réduit

- Détecter `prefers-reduced-motion: reduce` (CSS ou `matchMedia`) et réagir : pas de rotation automatique, pas de défilement piloté, pas de fluide continu, pas de particules.
- Ce que fait scroll-world : il ne charge pas les clips et laisse les images fixes ; il coupe aussi l'animation de l'indicateur et les particules.
- « Moins » ne veut pas dire « rien » : transitions courtes et douces possibles ; voir `${CLAUDE_SKILL_DIR}/../mouvement-interface/SKILL.md`.
- Proposer aussi un réglage visible dans la page pour couper l'animation, même sans réglage système.

## 7. Accessibilité clavier et texte alternatif

Un canevas est opaque pour les technologies d'assistance. Recommandations :
- Le contenu informatif est dans le HTML, pas dans la scène : titres, paragraphes, liens, boutons natifs.
- Le canevas porte un rôle et un libellé (`role="img"` et `aria-label` pour une scène décorative ou illustrative) ou est masqué (`aria-hidden`) s'il est purement décoratif ; une description plus longue peut suivre dans le texte.
- Toute interaction avec la scène (clic sur un objet, rotation) a un **équivalent clavier** : éléments HTML focalisables doublant les objets cliquables, ordre de tabulation logique, focus visible, jamais piégé dans la scène. Pour R3F, `@react-three/a11y` existe (à évaluer, licence et maintenance à vérifier).
- Contrôles de caméra : alternatives aux gestes à deux doigts ; ne pas bloquer le défilement de la page quand le pointeur est sur le canevas.
- Contraste du texte posé sur la scène vérifié dans les pires cas ; pas de clignotement rapide.
- Voir `expert-accessibilite` pour l'audit.

## 8. Mesurer sur mobile

1. Appareil réel, bas de gamme visé, pas seulement l'émulation ; iOS Safari séparément.
2. Relever : images par seconde, temps jusqu'au premier affichage, poids transféré, mémoire, température et batterie sur dix minutes d'usage.
3. Émulation navigateur avec processeur ralenti (quatre à six fois), comme le recommande scroll-world pour son essai mobile.
4. Défilement rapide, rotation d'écran, barre d'adresse qui se replie : la page ne doit pas sauter.
5. Surveiller `renderer.info` pendant les essais ; ajuster le ratio de pixels dynamiquement (`PerformanceMonitor` de drei en R3F) avec des bornes pour éviter les oscillations.
6. Rendre le résultat dans un tableau daté dans le dossier de tests.
