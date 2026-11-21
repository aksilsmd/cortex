# three.js : l'essentiel

Source : dépôt three.js (MIT), version `0.187.0` lue dans `package.json` au commit `6246c818834fd19d0c216d3dbc074b6cc9c27896`. À revérifier au démarrage du projet : la bibliothèque change souvent, et le guide de migration officiel (lié depuis le README) fait foi.

## Installer

- **Recommandé** : paquet npm plus un outil de build. Le manuel cite `npm install --save three` et `npm install --save-dev vite`, puis `npx vite` pour le serveur local et `npx vite build` pour la production. Les textures, sons et modèles vont dans un dossier `public/`.
- **Sans outil de build** : une table d'import (`importmap`) pointe `three` et `three/addons/` vers un CDN, avec une **version explicite**. Le manuel insiste : toutes les dépendances doivent venir de la même version et du même CDN, sinon du code est dupliqué ou l'application casse. Il faut aussi un serveur local, pas un double-clic sur le fichier.
- **Addons** (contrôles, chargeurs, post-traitement) : import explicite, par exemple `three/addons/loaders/GLTFLoader.js`.
- Les types TypeScript sont maintenus par la communauté (`three-types/three-ts-types`).

## Une scène minimale

Trois éléments : une scène, une caméra, un moteur de rendu. Le README et le manuel donnent le schéma : `new THREE.Scene()`, `new THREE.PerspectiveCamera(fov, aspect, near, far)`, `new THREE.WebGLRenderer({ antialias: true })`, un maillage (`Mesh`) composé d'une géométrie et d'un matériau, puis `renderer.setAnimationLoop(animate)`. Le canevas est `renderer.domElement`, à insérer dans la page.

Points à retenir :
- La caméra et l'objet sont tous deux à l'origine au départ : reculer la caméra (`camera.position.z`).
- Tout ce qui bouge passe par la boucle d'animation. Le paramètre de temps de la fonction est en millisecondes.
- Rapport `aspect` = largeur divisée par hauteur du conteneur, sinon l'image est écrasée.

## Responsive

Règle du manuel : laisser le CSS fixer la taille du canevas (`width: 100%; height: 100%; display: block`), et adapter le moteur à cette taille affichée. Un canevas a deux tailles : celle d'affichage (CSS) et celle de son tampon de dessin (en pixels). Schéma :
1. lire `clientWidth` et `clientHeight` du canevas ;
2. si le tampon diffère, appeler `renderer.setSize(largeur, hauteur, false)`, le `false` final évitant que three.js écrase le CSS ;
3. si la taille a changé, mettre à jour `camera.aspect` puis appeler `camera.updateProjectionMatrix()`.

**Écrans haute densité** : `renderer.setPixelRatio(window.devicePixelRatio)` multiplie le coût de rendu. Le manuel rappelle que les GPU mobiles sont moins puissants alors que les téléphones ont des écrans très denses : plafonner le ratio (par exemple à 2) est une décision de performance à mesurer.

## Rendu à la demande

Le manuel (« rendering on demand ») : si la scène n'anime rien en continu, rendre une fois au départ puis seulement quand quelque chose change (chargement terminé, réglage, mouvement de caméra). Boucle continue inutile = batterie et chaleur gaspillées.

## Charger un modèle glTF

Le manuel présente glTF comme format de transmission : binaire compact, prêt à rendre, matériaux définis. À préférer à OBJ ou aux formats d'éditeur.

```js
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
const gltf = await new GLTFLoader().loadAsync('models/objet.glb');
scene.add(gltf.scene);
```

Compression, selon la documentation du chargeur : `DRACOLoader` (géométrie, `setDecoderPath` vers `examples/jsm/libs/draco/`), `KTX2Loader` (textures, `setTranscoderPath` vers `examples/jsm/libs/basis/`, et `detectSupport(renderer)` avant usage), `MeshoptDecoder` (`examples/jsm/libs/meshopt_decoder.module.js`). On les branche avec `setDRACOLoader`, `setKTX2Loader`, `setMeshoptDecoder`. L'exemple `webgl_loader_gltf_compressed` montre l'assemblage. Le détail du choix est dans `performance-accessibilite-3d.md`. Un `LoadingManager` (`onStart`, `onProgress`, `onLoad`) permet d'afficher une progression.

## Libérer la mémoire

Règles du manuel (« How to dispose of objects ») :
- Géométries, matériaux, textures, cibles de rendu et squelettes ne sont **pas** libérés automatiquement : appeler `dispose()`.
- Retirer un maillage de la scène ne libère ni sa géométrie ni son matériau.
- Disposer un matériau ne libère pas ses textures.
- Les contrôles et le moteur de rendu ne sont plus utilisables après `dispose()` ; les autres objets peuvent être recréés, au prix d'un coût à l'image suivante.
- Les textures bitmap d'image demandent un `close()` côté application.
- `renderer.info` donne le nombre de géométries, textures et programmes en mémoire : outil de diagnostic des fuites. Certaines ressources internes (environnement, fond) peuvent rester listées sans fuite.
- Le manuel propose un petit suivi de ressources (une collection d'objets à `dispose()`), et conseille de nettoyer au changement de niveau ou de scène.

## WebGPU

Le manuel décrit `WebGPURenderer` comme le moteur de nouvelle génération, avec repli automatique sur WebGL 2.
- Import : `three/webgpu` (et `three/tsl` pour le langage de shaders TSL).
- L'initialisation est asynchrone : `setAnimationLoop` s'en charge ; sinon `await renderer.init()`.
- `forceWebGL: true` force le repli, utile pour tester.
- **Non pris en charge** : `ShaderMaterial`, `RawShaderMaterial`, `onBeforeCompile`, `EffectComposer`. Ils doivent être portés vers les matériaux à nœuds et TSL.
- Décision : WebGL reste le choix prudent pour un projet qui utilise des shaders maison ou l'écosystème R3F actuel ; WebGPU se justifie par un besoin précis et se trace dans un ADR.

## Parcours d'apprentissage et exemples

- **Exemples officiels** : le dossier `examples/` contient des centaines de fichiers préfixés `webgl_`, `webgpu_`, `webxr_`, `misc_`, `physics_`, `webaudio_`, `svg_`, `games_`. S'en servir comme catalogue d'effets (instanciation, ombres, post-traitement, chargeurs).
- **Manuel** : pages sur les fondamentaux, caméras, lumières, ombres, textures, matériaux, gestion des couleurs, instanciation, picking, post-traitement.
- **Livre d'initiation** (dépôt `ThreeExample.js`, en chinois) : exemples par chapitres : 1 vue d'ensemble, 2 caméras, 3 géométries, 4 matériaux, 5 maillages, 6 animation, 7 modèles externes, 8 lumières et ombres, 9 shaders. **Attention : ils utilisent three.js r79 (2016). L'API a changé depuis** : `CubeGeometry` est devenu `BoxGeometry` ; `THREE.Geometry` avec `vertices` et `faces` a laissé place à `BufferGeometry` ; `renderer.shadowMapEnabled` est devenu `renderer.shadowMap.enabled` ; les anciennes propriétés d'ombre de lumière (`shadowCameraNear`, `shadowDarkness`...) ont changé ; les chargeurs OBJ et Collada se chargent aujourd'hui comme addons. Utiliser ces exemples pour comprendre l'ordre des notions, jamais comme code à copier, et transposer avec le manuel actuel.
