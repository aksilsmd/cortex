# React Three Fiber (R3F)

Source : dépôt `pmndrs/react-three-fiber` (MIT), commit `d74622ea8ed717f7212d7e19d65ff3e325508389`, paquet `@react-three/fiber` version `9.8.1` (lue dans `packages/fiber/package.json`). À revérifier avant le projet.

## Compatibilité des versions

| Élément | Valeur lue |
|---|---|
| `@react-three/fiber` 8 | s'associe à React 18 |
| `@react-three/fiber` 9 | s'associe à React 19 |
| Pairs déclarés de la version 9.8.1 | `react` et `react-dom` `>=19 <19.4`, `three` `>=0.156`, `react-native` `>=0.78` (optionnel) |
| Version 10 | en alpha, annoncée avec WebGPU et un nouvel ordonnanceur de boucle ; ne pas la retenir pour une production sans décision tracée |

R3F est un moteur de rendu React : il doit être apparié à la version majeure de React, comme `react-dom`. Le projet de portfolio étudié (dépendances `react ^19`, `@react-three/fiber ^9`, `three ^0.174`) illustre une combinaison cohérente, mais les numéros se relèvent à nouveau à chaque démarrage.

Installation : `npm install three @react-three/fiber` (ajouter `@types/three` en TypeScript). Vite fonctionne directement ; avec Next.js, le dépôt indique d'ajouter `three` à `transpilePackages` dans `next.config.js` (versions 13.1 et suivantes). React Native passe par `@react-three/fiber/native` et `expo-gl`, à tester sur appareil réel.

## Principe

Chaque balise est une classe three.js : `<mesh />` crée un `THREE.Mesh`. Tout ce qui existe dans three.js est utilisable. Les composants vivent dans un `<Canvas>`, qui crée la scène, la caméra, le moteur de rendu et la boucle.

Valeurs par défaut du `Canvas` (documentation) : anticrénelage actif, fond transparent (`alpha`), `powerPreference` haute performance, espace colorimétrique sRGB, tonalité ACES Filmic (désactivable avec `flat`). Props utiles : `dpr` (défaut `[1, 2]`), `frameloop` (`always`, `demand`, `never`), `shadows`, `fallback`, `eventSource`, `performance`.

## Hooks

- **`useFrame((state, delta) => ...)`** : code exécuté à chaque image, à la fréquence de l'écran. Ne jamais appeler `setState` dedans : on **mute** les objets via des références. Utiliser `delta` (secondes) pour rester indépendant de la fréquence d'affichage. Une priorité numérique reprend la main sur le rendu automatique : à n'utiliser que si on gère soi-même le rendu.
- **`useThree(sélecteur)`** : accès au moteur (`gl`), à la scène, à la caméra, au pointeur, à la taille, au `viewport`, à `invalidate`, à `setDpr`. Utiliser un sélecteur pour limiter les rendus. Les hooks ne fonctionnent qu'**à l'intérieur** du `Canvas`.
- **`useLoader(Chargeur, url, extension)`** : charge et **met en cache** par URL, en suspendant le composant (à envelopper dans `Suspense`). Le troisième argument configure le chargeur, par exemple pour brancher `DRACOLoader`. `useLoader.preload` précharge. Pour un glTF, on obtient aussi `nodes` et `materials`. Ne pas muter ni libérer un actif partagé.
- **`useGraph`** : collection nommée d'objets et de matériaux d'un `Object3D`.

## Événements

Les objets qui implémentent `raycast` (maillages, lignes) acceptent `onClick`, `onPointerOver`, `onPointerOut`, `onPointerMove`, `onWheel`, `onDoubleClick`, `onContextMenu`, `onPointerMissed` sur le `Canvas`. L'événement transporte l'événement du navigateur et les données d'intersection. Particularité : l'événement atteint d'abord l'objet le plus proche puis remonte, puis passe à l'objet suivant derrière ; `event.stopPropagation()` arrête aussi la livraison aux objets plus lointains. La capture du pointeur passe par `event.target.setPointerCapture`. `eventSource` permet de rattacher les événements à un parent commun avec les surcouches HTML.

## Performance (pièges du dépôt)

- **Pas de `setState` dans une boucle ou un événement rapide** : muter par référence, avec `delta`.
- **Ne pas lier d'état rapide de façon réactive** (état animé à 60 Hz lu par un sélecteur) : lire l'état directement dans `useFrame`.
- **Ne pas monter et démonter sans raison** : matériaux et tampons se recompilent. Préférer la visibilité (`visible`) aux montages conditionnels. `startTransition` aide pour les opérations coûteuses.
- **Ne pas créer d'objets dans la boucle** (nouveau `Vector3` à chaque image) : réutiliser.
- **Réutiliser géométries et matériaux** (créés une fois, hors du rendu, ou via `useMemo`). Si on crée des couleurs hors du `Canvas`, activer `THREE.ColorManagement`.
- **Instanciation** (`instancedMesh`) pour les objets répétés : chaque maillage est un appel de dessin ; le guide donne comme repère « pas plus de 1000 au maximum absolu, idéalement quelques centaines ou moins ».
- **Rendu à la demande** : `<Canvas frameloop="demand">`, avec `invalidate()` quand un objet est muté hors de React (les contrôles de drei le font seuls). `invalidate` demande une image, il ne rend pas immédiatement.
- **Niveaux de détail** (`Detailed` de drei), **chargement imbriqué** (un `Suspense` dont le repli est la version basse définition), **`PerformanceMonitor`** de drei pour ajuster `dpr` selon les images par seconde, avec bornes pour éviter les va-et-vient.
- **Libération** : R3F appelle `dispose` des objets démontés. Pour des ressources partagées ou en cache, poser `dispose={null}` sur le groupe. Un `<primitive object=...>` ne libère pas l'objet qu'il porte.

## Écosystème utile

`@react-three/drei` (aides : contrôles, chargeurs, `useGLTF`), `@react-three/gltfjsx` (glTF vers composants), `@react-three/postprocessing`, `@react-three/rapier` (physique), `@react-three/a11y` (accessibilité de la scène), `@react-three/xr`. Chaque ajout est une dépendance à inscrire dans l'ADR, avec sa licence et son poids.

## Repli et robustesse

`<Canvas fallback={...}>` s'affiche si WebGL n'est pas pris en charge ; le dépôt recommande de plus d'entourer le `Canvas` d'une frontière d'erreur pour les pertes de contexte (pilotes défectueux, GPU désactivé), et que le repli remplace visuellement le rendu si possible.
