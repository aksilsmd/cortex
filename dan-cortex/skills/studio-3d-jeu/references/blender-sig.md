# BlenderGIS : données géographiques dans Blender

Add-on communautaire (dépôt `domlysz/BlenderGIS`, commit `2add45ff` du 20 décembre 2025, licence **GPL-3.0**). Méthode réécrite : aucun texte ni code recopié, seuls des faits (noms de fonctions, formats, services). Usage typique : terrain, bâtiments et routes réels pour un décor, une vue d'architecte, une carte ou une maquette 3D.

## Compatibilité
- Version de l'add-on lue dans le code : 2.2.14. Blender minimum : 2.83 (README et `bl_info`).
- Le code **refuse de s'activer** sous Blender 6 ou plus et le signale par une erreur de version : domaine annoncé de 2.83 à 5.x.
- Format ancien (`bl_info`) : pas de fichier `blender_manifest.toml` dans l'arborescence, donc pas une extension au sens de Blender 4.2+. Installation comme add-on classique.
- Aucun test sous Blender 5.2 LTS (cible de la bibliothèque) n'apparaît dans le dépôt : **à revérifier** par un essai sur la machine, scène vide, avant tout travail réel.

## Fonctions réelles (opérateurs lus dans `operators/`)
| Besoin | Fonction | Identifiant bpy |
|---|---|---|
| Vecteurs Shapefile | import avec choix des champs ; export SHP | `importgis.shapefile`, `exportgis.shapefile` |
| Rasters géoréférencés, MNT | modes : plan texturé, fond d'image, texture sur maillage existant, déplacement par MNT, nuage de points (lent, petits jeux de données) | `importgis.georaster` |
| Grille ASCII | import `.asc` | `importgis.asc_file` |
| OpenStreetMap | import d'un fichier XML, ou requête directe sur un serveur Overpass ; étiquettes par défaut : bâtiments, routes, occupation du sol, loisirs, nature, rail, cours d'eau ; bâtiments extrudés (hauteur par défaut 20, étage 3, d'après `building:levels`) | `importgis.osm_file`, `importgis.osm_query` |
| Altitudes | téléchargement SRTM 30 m ou 90 m (OpenTopography, clé API obligatoire) ou GMRT | `importgis.dem_query` |
| Fonds de carte | visionneuse de tuiles dans la vue 3D, recherche de lieu, cache disque | `view3d.map_start`, `view3d.map_viewer`, `view3d.map_search` |
| Maillage | triangulation de Delaunay, diagramme de Voronoï, poser un objet au sol | `tesselation.delaunay`, `tesselation.voronoi`, `object.drop` |
| Analyse de terrain | nœuds de matériau Cycles : altitude, pente, orientation ; reclassement des couleurs | `analysis.nodes` |
| Globe | longitude-latitude vers sphère, correction de courbure | `earth.sphere`, `earth.curvature` |
| Caméras | depuis des photos géolocalisées (EXIF) ; caméra de rendu géoréférencé | `camera.geophotos`, `camera.georender` |

Les commentaires du code indiquent que ces opérateurs s'appellent depuis la console ou un script ; beaucoup ouvrent des dialogues avec propriétés : l'appel scripté de chacun est **à vérifier**. Le mode `-b` n'est pas documenté pour l'add-on.

## Systèmes de coordonnées
- La scène stocke son système de référence (CRS) et son origine géographique ou projetée ; les conversions entre vue 3D et coordonnées projetées passent par cette origine et une échelle.
- Définitions préréglées de base : EPSG:3857 (Web Mercator, déformations fortes, déconseillé pour modéliser avec précision) et EPSG:4326 (degrés, **à ne pas utiliser comme CRS de scène**). Les définitions de fonds de carte comprennent Lambert 93 (EPSG:2154).
- Règle de méthode : choisir un CRS projeté en mètres adapté au lieu, l'inscrire dans la fiche de scène, ne jamais mélanger deux CRS sans reprojection.
- Moteurs de reprojection au choix : automatique, GDAL, pyproj, service en ligne epsg.io, ou fonctions internes. Moteurs d'image : GDAL, ImageIO, PIL. Les bibliothèques optionnelles absentes sont repérées au chargement ; le greffon FreeImage d'ImageIO tente de se télécharger.

## Flux réseau et conditions
À l'usage, l'add-on contacte : serveurs de tuiles (Google, Bing, Esri, OpenStreetMap, Géoportail, CRAIG), serveurs Overpass (trois préréglés), OpenTopography, GMRT, epsg.io si choisi. L'agent de requête annoncé par défaut imite un navigateur. Conséquences :
1. **Accord de l'utilisateur** avant la première requête ; couper le réseau avec `--offline-mode` ou la préférence Blender quand on travaille sur fichiers locaux.
2. **Clé OpenTopography** : donnée personnelle de l'utilisateur, stockée dans les préférences de l'add-on, jamais dans un échange ni un dépôt. Le service est gratuit mais exige l'inscription (README).
3. **Conditions d'usage des tuiles** (Google, Bing, Esri) et licence des données OpenStreetMap, avec attribution : non présentes dans le dépôt, **à revérifier** avant tout usage commercial ou toute redistribution (`juridique-conformite`). Un rendu ou un export contenant des tuiles est une œuvre qui embarque des données tierces.
4. Respecter les limites des serveurs publics : petites emprises, cache activé, pas de téléchargement massif.

## Chaîne de production
SIG vers Blender (CRS en mètres, origine fixée) ; nettoyage et allègement du maillage (`dcc/blender/scenario-blender-retopology`, `dcc/blender/scenario-blender-geometry-nodes`) ; matériaux et éclairage (`dcc/blender/scenario-blender-texturing-shading`) ; export `dcc/blender/scenario-blender-export` : glTF vers le web (`${CLAUDE_SKILL_DIR}/../web-3d-immersif/SKILL.md`) ou vers un moteur (`${CLAUDE_SKILL_DIR}/references/moteurs-de-jeu.md`). Terrain étendu : budget de triangles et découpage en tuiles à fixer avant import. Preuve : rendu relu, nombre de triangles, échelle mesurée contre une distance connue.
