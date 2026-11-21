# Effets et pages immersives : scroll-world, fluide, portfolio

## 1. Page « vol à travers un monde » (scroll-world)

Source : bibliothèque vendorisée `${CLAUDE_PLUGIN_ROOT}/bibliotheque/scroll-world/` (MIT, commit `71cc36d3bb150248ae36a2c552f9cbf88802a79c`). Lire `SKILL.md` puis `references/pipeline.md` avant de proposer quoi que ce soit.

**Principe.** Le visiteur défile ; une caméra pré-rendue plonge dans une scène, en ressort, puis enchaîne la scène suivante sans coupure. Les images et vidéos sont générées ; la page se contente de faire avancer la vidéo selon la position de défilement, avec un moteur autonome en JavaScript sans dépendance (`references/scrub-engine.js`), utilisable dans une page simple comme dans un framework.

**Quand le choisir.** Page d'atterrissage de marque, récit en séquence, effet de démonstration. **Quand l'éviter.** Contenu qui doit être indexé et lu comme du texte, public majoritairement sur réseau lent, budget nul, besoin d'interaction 3D libre (dans ce cas, three.js ou R3F).

**Prérequis et coût (à annoncer avant de commencer).**
- Le skill demande un **générateur externe payant** : images avec Higgsfield (ou Codex si disponible), vidéos par défaut via Monid, avec crédits Higgsfield en repli. Il compte N images et 2N moins 1 vidéos, ces dernières doublant pour une version mobile native en 9:16, plus environ 15 % de marge de reprises.
- Ordre de grandeur donné par le skill (juillet 2026) : environ 27 dollars pour six scènes en 1080p, environ 11 en 720p, coût de l'aperçu en 480p nettement plus bas. À recalculer, car les tarifs et le catalogue changent.
- Outils locaux : CLI du générateur (connexion interactive à faire par l'utilisateur), ffmpeg et ffprobe, outil d'image optionnel.
- Le skill pose ses questions d'entrée (sujet, charte, style, type de caméra, version mobile, budget) : les reprendre, ne pas répondre à la place de l'utilisateur.
- Règle centrale du skill : les raccords entre clips doivent partir des images réellement rendues des clips voisins, pas des images fixes d'origine, sinon un saut apparaît.
- Contrôle qualité : captures avant et après chaque raccord, console sans erreur, lecture suivant bien le défilement, essai mobile.
- Aucun script de la bibliothèque ne tourne sans lecture et accord explicite.

**Accessibilité de cette voie.** Le moteur n'utilise que les images fixes quand `prefers-reduced-motion` est demandé. À ajouter côté projet : texte réel dans le HTML (titres, paragraphes, liens, bouton d'appel à l'action), navigation clavier, descriptions des scènes, et un chemin d'accès au contenu sans défilement piloté.

## 2. Fond de fluide interactif

Source : `PavelDoGreat/WebGL-Fluid-Simulation` (MIT, commit `a2d292931f19d9b3b9f564e23e6c32729d2121c3`), fichier `script.js`. Le README renvoie à la méthode de fluide stable décrite dans le chapitre « Fast Fluid Dynamics Simulation on the GPU » de GPU Gems (NVIDIA).

**Méthode (lue dans `step`).** À chaque image, des passes de shaders sur des textures : calcul de la rotation du champ de vitesse (curl), application de la vorticité, calcul de la divergence, remise à zéro puis plusieurs itérations de la pression, soustraction du gradient de pression, puis advection de la vitesse et du colorant. Le pointeur injecte de la vitesse et de la couleur (`splat`). Le pas de temps est plafonné à 1/60 seconde.

**Paramètres de `config` (valeurs par défaut lues).**

| Paramètre | Défaut | Rôle |
|---|---|---|
| `SIM_RESOLUTION` | 128 | résolution de la grille de vitesse |
| `DYE_RESOLUTION` | 1024 | résolution du colorant (coût principal) |
| `DENSITY_DISSIPATION` | 1 | disparition de la couleur |
| `VELOCITY_DISSIPATION` | 0,2 | amortissement du mouvement |
| `PRESSURE` / `PRESSURE_ITERATIONS` | 0,8 / 20 | résolution de la pression |
| `CURL` | 30 | vorticité, tourbillons |
| `SPLAT_RADIUS` / `SPLAT_FORCE` | 0,25 / 6000 | taille et force de l'injection |
| `SHADING`, `BLOOM`, `SUNRAYS` | actifs | effets coûteux, facultatifs |
| `COLORFUL`, `TRANSPARENT`, `BACK_COLOR` | actif, non, noir | rendu et fond |

**Replis déjà présents dans le code.** Contexte WebGL 2 puis WebGL 1 ; extensions de texture à demi-précision ; choix d'un format de texture pris en charge, avec cascade R, RG puis RGBA ; si le filtrage linéaire manque, résolution du colorant ramenée à 512 et ombrage, flou lumineux et rayons désactivés ; sur mobile (détection par chaîne d'agent `Mobi|Android`), colorant à 512.

**Ce que le code d'origine ne fait pas, et que le projet doit ajouter (garde-fous).**
- **`prefers-reduced-motion`** : ne pas lancer la simulation (fond statique), ou la limiter à une réponse au clic.
- **Mobile et batterie** : résolutions réduites, effets coûteux coupés, détection par capacités plutôt que par agent utilisateur, cadence limitée si besoin.
- **Pause** : la boucle d'origine tourne sans fin ; arrêter hors écran (`IntersectionObserver`) et onglet masqué (`visibilitychange`).
- **Repli sans WebGL ou sans format de texture** : fond en dégradé CSS.
- **Contraste** : texte posé sur un fond animé, contraste vérifié dans le pire cas ; fond ne portant jamais d'information.
- **Pas de traceur** : la page d'origine charge un script d'analyse tiers, envoie des événements et affiche des bandeaux promotionnels vers des boutiques d'applications. Ne rien en reprendre : respecter la confidentialité et le consentement (`${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md`).
- **Crédit MIT** dans `references/sources.md` du projet si du code est repris ; sinon réécrire la méthode.

## 3. Portfolio 3D : architecture seulement

Source : dépôt `adrianhajdin/3d-portfolio`, **aucune licence trouvée** : **forme A stricte**, aucun code ni asset repris. Seuls `package.json` et l'arborescence `src/` ont été lus ; les contenus des composants n'ont pas été lus, les rôles ci-dessous sont déduits des noms de fichiers.

**Pile observée.** Vite, React 19, `@react-three/fiber` 9, `@react-three/drei`, `@react-three/postprocessing`, three, GSAP avec `@gsap/react`, Tailwind CSS 4, `react-responsive`, un service d'envoi de courriel côté client (`@emailjs/browser`). Ce dernier est un traitement de données personnelles par un tiers : à examiner avant tout usage.

**Découpage à retenir (à réécrire avec nos mots).**
- Un dossier de **sections de page**, une par bloc : accueil, présentation, logos, cartes de fonctionnalités, expérience, pile technique, témoignages, contact, pied de page.
- Un dossier de **composants d'interface** (barre de navigation, bouton, carte, titre de section, compteur animé).
- Un dossier de **scènes 3D**, une par zone concernée (accueil avec décor, lumières et particules ; contact avec un objet ; icônes technologiques), séparées du reste : la 3D est isolée dans des `Canvas` distincts, pas répartie partout.
- Un fichier de **constantes** pour les contenus (textes, listes), séparé de la présentation.
- Des **actifs** rangés en images et modèles 3D.

**Leçons de méthode.** Limiter les `Canvas` aux sections qui les justifient ; contenu textuel séparé du code ; animations de défilement distinctes des scènes ; versions de bibliothèques fixées par le fichier de verrouillage du projet (le dépôt étudié utilise des plages avec accent circonflexe) ; chargement différé des modèles lourds. Le portfolio doit rester lisible et navigable sans la 3D (fiche `performance-accessibilite-3d.md`).
