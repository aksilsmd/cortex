# Formation — Animation et motion design (web et mobile)

Fiche de formation pour maquettiste, concepteur UX, cartographe des interactions, développeurs front et mobile, testeurs et expert accessibilité. Elle complète `formation-ui-ux.md`, `formation-design-web-mobile.md`, `accessibilite.md` et `theme-design-system.md`. Sources primaires en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/animation-motion.md`.

## Sommaire
1. Objectifs
2. À quoi sert une animation
3. Principes de motion design
4. Durées et courbes : règles chiffrées
5. Accessibilité : prefers-reduced-motion et WCAG
6. Performance
7. Outils natifs : CSS, View Transitions, scroll-driven, WAAPI
8. Motion (ex-Framer Motion)
9. React Motion : état de maintenance et alternatives
10. Arbre de décision : quelle technique
11. Mobile natif
12. Spécifier une animation (handoff)
13. Check-list d'audit
14. Anti-patterns et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- justifier chaque animation par une fonction (retour, orientation, continuité, attention) ou la supprimer ;
- choisir durées et courbes cohérentes, en jetons du système de design ;
- garantir l'accessibilité (réduction de mouvement, pas de clignotement, pause des animations automatiques) ;
- n'animer que des propriétés peu coûteuses et vérifier la fluidité ;
- choisir entre CSS pur, View Transitions, WAAPI et une bibliothèque (Motion, React Spring), en pesant le poids ajouté ;
- spécifier une animation de façon testable.

## 2. À quoi sert une animation

| Fonction | Exemple | Sinon |
|---|---|---|
| Retour d'action | bouton qui s'enfonce, coche de validation | l'utilisateur doute que l'action ait eu lieu |
| Orientation spatiale | panneau qui glisse depuis le bord d'où il vient | perte de repère dans la navigation |
| Continuité | une vignette s'agrandit en page de détail | changement d'écran brutal, recherche visuelle |
| Changement d'état | élément ajouté à la liste, suppression qui se replie | le changement passe inaperçu |
| Attention (rare) | badge de nouvelle notification | surcharge si répété |
| Attente | indicateur de progression, squelette | sentiment de blocage au-delà de ≈ 1 s |

Une animation sans fonction est décorative : elle est facultative, courte, désactivable, et ne retarde jamais une tâche.

## 3. Principes de motion design

- **Rapide et discret** : l'interface répond, elle ne fait pas un spectacle.
- **Cohérent** : un même type de mouvement (entrée de modale, toast, tiroir) a toujours la même durée et la même courbe ; ce sont des jetons (`--motion-duration-fast`, `--motion-ease-out`).
- **Physique crédible** : accélération et décélération (pas de linéaire pour un déplacement), entrées en décélération (ease-out), sorties en accélération (ease-in), déplacements internes en ease-in-out.
- **Origine logique** : un menu s'ouvre depuis son déclencheur (`transform-origin`), une modale émerge du centre ou du bouton.
- **Hiérarchie** : décalage (stagger) de 20–50 ms entre éléments d'une liste, plafonné (au-delà de 6–8 éléments, animer le groupe).
- **Interruptible** : un geste ou un clic pendant l'animation la reprend depuis l'état courant, sans saut (ressorts, WAAPI, Motion le gèrent).
- **Les 12 principes Disney** utiles en UI : anticipation légère, ralentis d'entrée/sortie, arcs, chevauchement ; à doser — l'exagération ne sert qu'à la marque ou au jeu.

## 4. Durées et courbes : règles chiffrées

| Mouvement | Durée indicative |
|---|---|
| Retour simple (survol, pression, case, interrupteur) | ≈ 100 ms (100–150) |
| Petits composants (info-bulle, menu, toast) | 150–200 ms |
| Changement d'écran, modale, tiroir | 200–300 ms |
| Grands déplacements plein écran | ≤ 400 ms |
| Seuil de gêne | ≈ 500 ms : trop long pour une UI courante |

- Sortie ≈ 20–30 % plus courte que l'entrée (l'utilisateur a déjà décidé).
- Mobile : plutôt bas de fourchette ; tablette/desktop grand écran : un peu plus long pour de grandes distances.
- Courbes CSS de base : `ease-out` pour entrer, `ease-in` pour sortir, `ease-in-out` pour déplacer ; jamais `linear` pour un déplacement (réservé aux rotations continues et barres de progression).
- Courbes personnalisées : `cubic-bezier(0.2, 0, 0, 1)` (décélération marquée) est une base courante ; la fonction CSS `linear()` permet d'approximer un ressort sans JavaScript.
- Ressort (Motion, React Spring, SwiftUI, Compose) : préférer pour les gestes ; régler par rigidité/amortissement ou par durée + rebond (`bounce` 0–0,25 en UI ; 0 = pas de dépassement).
- Respect des limites de réponse (NN/g) : 0,1 s = instantané ; 1 s = flux de pensée préservé ; au-delà, indicateur de progression.

## 5. Accessibilité : prefers-reduced-motion et WCAG

Pourquoi : les mouvements amples (parallaxe, zoom, défilement automatique) déclenchent nausées et vertiges chez les personnes avec troubles vestibulaires ; les animations perpétuelles gênent l'attention (TDAH, troubles cognitifs).

Règles :
- **`prefers-reduced-motion: reduce`** (Baseline depuis 2020 ; réglage OS : Windows, macOS, iOS, Android 9+) : remplacer les déplacements, zooms et parallaxes par un fondu court ou rien ; conserver les retours d'état (couleur, opacité).
- **WCAG 2.2.2 (A) Pause, arrêt, masquage** : tout contenu qui bouge automatiquement plus de 5 s et en parallèle d'autres contenus doit pouvoir être mis en pause, arrêté ou masqué (carrousels, bandeaux défilants, vidéos décoratives).
- **WCAG 2.3.1 (A)** : rien ne clignote plus de 3 fois par seconde (sauf sous les seuils de flash).
- **WCAG 2.3.3 (AAA) Animation déclenchée par interaction** : les animations de mouvement déclenchées par l'interaction doivent pouvoir être désactivées, sauf si essentielles. AAA, mais à appliquer par défaut via `prefers-reduced-motion`.
- L'information ne doit jamais dépendre uniquement d'une animation (un champ en erreur qui « tremble » doit aussi afficher un message).
- Le focus clavier ne doit pas être perdu pendant une transition ; après une transition de page, le focus va au titre ou au contenu principal.

Modèle sûr (« mouvement en option ») :
```css
.carte { opacity: 1; }
@media (prefers-reduced-motion: no-preference) {
  .carte { transition: transform 200ms cubic-bezier(.2,0,0,1), opacity 200ms; }
  .carte:hover { transform: translateY(-2px); }
}
```
Lecture JS : `matchMedia('(prefers-reduced-motion: reduce)').matches`, écouter `change`. Offrir aussi un réglage dans l'application quand l'animation est importante pour la marque.

## 6. Performance

- N'animer que **`transform`** et **`opacity`** (et `filter` avec prudence) : ils sont composités par le GPU sans recalcul de mise en page. Éviter `width`, `height`, `top`, `left`, `margin`, `box-shadow` animés : ils déclenchent layout ou paint.
- Simuler une ombre animée : animer l'opacité d'un pseudo-élément portant l'ombre.
- `will-change` : seulement juste avant une animation lourde et retiré après ; jamais en masse (mémoire GPU).
- Budget de trame : 16,7 ms à 60 Hz, 8,3 ms à 120 Hz ; vérifier dans le panneau Performance des DevTools (images longues, layout shift).
- Une animation ne doit pas dégrader l'INP (≤ 200 ms) ni provoquer de CLS (≤ 0,1) : réserver l'espace, animer `transform` plutôt que la hauteur.
- Animations de hauteur « auto » : préférer `grid-template-rows: 0fr → 1fr`, ou `interpolate-size: allow-keywords` (Chromium seulement, amélioration progressive), ou les layout animations de Motion (FLIP).
- Appareils d'entrée de gamme (cible mobile algérienne) : tester avec ralentissement CPU ×4 à ×6 dans les DevTools.

## 7. Outils natifs : CSS, View Transitions, scroll-driven, WAAPI

**Transitions et `@keyframes` CSS** : suffisent pour survols, ouvertures, toasts, squelettes. Zéro dépendance. Entrée d'un élément nouvellement affiché : `@starting-style` (+ `transition-behavior: allow-discrete` pour `display`/`overlay`, utile avec `<dialog>` et `popover`).

**View Transitions API** :
- Same-document (SPA) : `document.startViewTransition(() => majDuDOM())` ; disponible Chrome/Edge 111, Safari 18, Firefox 144 ⇒ largement utilisable, avec repli si la fonction est absente.
- Cross-document (MPA) : `@view-transition { navigation: auto; }` sur les deux pages ; Chrome/Edge 126, Safari 18.2 ; Firefox non à la date de la page ⇒ amélioration progressive.
- Nommer les éléments partagés avec `view-transition-name` (unique par page) ; personnaliser via `::view-transition-old()` / `::view-transition-new()`.
- Toujours entourer l'animation par `prefers-reduced-motion` (fondu simple ou aucune animation).
- Frameworks : Next.js, Astro, SvelteKit, React (`<ViewTransition>` expérimental/canari à vérifier) offrent des intégrations ; vérifier l'état à la source avant usage en production.

**Animations pilotées par le défilement** (`animation-timeline: scroll()` / `view()`) : Chrome/Edge 115+, Safari 26+ ; Firefox stable encore derrière un drapeau mi-2026 ⇒ pas Baseline. À réserver aux effets décoratifs avec repli statique, protégés par `@supports (animation-timeline: view())`.

**Web Animations API (WAAPI)** : `el.animate(keyframes, { duration, easing, fill })` renvoie un objet Animation (`play`, `pause`, `reverse`, `finished`, `playbackRate`) ; moteur natif, pas de `requestAnimationFrame` manuel. Idéal pour séquencer en JS sans dépendance ; `document.getAnimations()` pour tout mettre en pause (bouton « pause » de 2.2.2, ou tests).

```js
const reduit = matchMedia('(prefers-reduced-motion: reduce)').matches;
el.animate(
  reduit ? [{ opacity: 0 }, { opacity: 1 }]
         : [{ opacity: 0, transform: 'translateY(8px)' }, { opacity: 1, transform: 'none' }],
  { duration: reduit ? 120 : 200, easing: 'cubic-bezier(.2,0,0,1)', fill: 'both' }
);
```

## 8. Motion (ex-Framer Motion)

- Paquet **`motion`** (licence MIT ; version 14.x fin octobre 2026 selon npm), pour JavaScript, React et Vue. Ancien nom `framer-motion` : migrer l'import vers `motion/react`.
- React ≥ 18.2. Next.js App Router : composant client (`"use client"`) ou import `motion/react-client`.
- Atouts : `animate`/`initial`/`exit` déclaratifs, `AnimatePresence` (animations de sortie), **layout animations** (FLIP automatique, `layoutId` pour éléments partagés), gestes (`whileHover`, `whileTap`, `drag`), ressorts interruptibles, `useScroll`, moteur hybride WAAPI + JS.
- **Poids** (à intégrer au budget JS) : composant `motion` ≈ 43 ko ; `m` + `LazyMotion` ≈ 5 ko au rendu initial, puis `domAnimation` (+≈ 24 ko : animations, variantes, exit, gestes tap/hover/focus) ou `domMax` (+≈ 38 ko : en plus drag et layout) chargés de préférence par `import()` dynamique ; `useAnimate` mini ≈ 3,3 ko (WAAPI seul).
- **Accessibilité** : `<MotionConfig reducedMotion="user">` à la racine coupe transformations et layout animations quand l'OS demande moins de mouvement (opacité et couleurs conservées) ; `useReducedMotion()` pour remplacer un effet par un fondu, couper la vidéo auto ou la parallaxe.

```tsx
import { LazyMotion, domAnimation, MotionConfig, AnimatePresence } from "motion/react";
import * as m from "motion/react-m";

<MotionConfig reducedMotion="user">
  <LazyMotion features={domAnimation} strict>
    <AnimatePresence>
      {ouvert && (
        <m.div key="panneau" initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}
               exit={{ opacity: 0, y: 8 }} transition={{ duration: 0.2, ease: [0.2, 0, 0, 1] }} />
      )}
    </AnimatePresence>
  </LazyMotion>
</MotionConfig>
```
Remarque : vérifier à la source le chemin exact d'import de `m` pour la version installée (documentation « Reduce bundle size »).

## 9. React Motion : état de maintenance et alternatives

- **`react-motion`** (C. Lou) : dernière version 0.5.2, publiée il y a environ 9 ans ; questions de maintenance restées sans relève sur GitHub. À considérer **abandonné** : ne pas l'introduire dans un nouveau projet ; planifier sa sortie dans un projet existant (compatibilité React 18/19 non garantie).
- Alternatives maintenues :

| Besoin | Choix |
|---|---|
| Animations UI générales, sorties, layout, gestes en React | Motion (`motion/react`) |
| Physique par ressorts, style proche de react-motion | `@react-spring/web` (v10.x, maintenue en 2026) |
| Listes simples sans dépendance lourde | CSS + `@starting-style`, ou AutoAnimate (vérifier la maintenance) |
| Animations vectorielles de marque (illustrations) | Lottie / dotLottie (fichiers exportés) ou Rive |
| Séquences complexes, timeline, SVG | GSAP (gratuit, y compris plugins, depuis le rachat par Webflow en 2024 : vérifier la licence à la source) |

## 10. Arbre de décision : quelle technique

1. L'animation est-elle utile (section 2) ? Non → ne pas animer.
2. Simple changement d'état au survol/focus/ouverture ? → transition CSS.
3. Entrée/sortie d'un élément ou d'un `<dialog>`/`popover` ? → CSS `@starting-style` + `allow-discrete`.
4. Changement de vue ou élément partagé entre pages ? → View Transitions (repli sans animation).
5. Effet lié au défilement, décoratif ? → scroll-driven CSS sous `@supports`, sinon rien ; jamais de parallaxe sans réduction de mouvement.
6. Séquencement, contrôle (pause, inversion) en JS sans framework ? → WAAPI.
7. React avec sorties, réordonnancement de listes, layout partagé, gestes de glisser ? → Motion avec `LazyMotion`.
8. Physique de ressorts fine ? → Motion (spring) ou React Spring.
Rester sans dépendance tant que les points 2 à 6 suffisent : chaque bibliothèque ajoutée se justifie par un besoin non couvert et son poids mesuré.

## 11. Mobile natif

- **iOS (SwiftUI)** : `withAnimation(.spring(duration:bounce:))`, `matchedGeometryEffect` ; lire `@Environment(\.accessibilityReduceMotion)`.
- **Android (Compose)** : `animate*AsState`, `AnimatedVisibility`, `AnimatedContent`, transitions d'éléments partagés ; respecter l'échelle d'animation système (`ANIMATOR_DURATION_SCALE`, 0 = animations désactivées).
- **React Native** : Reanimated (thread UI), `AccessibilityInfo.isReduceMotionEnabled()` ; **Flutter** : `AnimatedContainer`, `Hero`, `MediaQuery.disableAnimations`.
- Respecter les conventions de plateforme (retour arrière, feuilles modales, rebond iOS) plutôt qu'un mouvement « maison ».
- Retour haptique : bref, lié à une action confirmée, désactivable.

## 12. Spécifier une animation (handoff)

Pour chaque animation, une ligne dans la matrice d'interactions :
`déclencheur | élément | propriétés (de → à) | durée (jeton) | courbe (jeton) | délai/décalage | comportement si interrompue | variante reduced-motion | critère de test`.

Exemple : `clic « Ajouter au panier » | badge panier | scale 1 → 1.15 → 1, opacity | motion-fast (150 ms) | ease-out | 0 | reprend depuis l'état courant | changement de couleur seul | le compteur s'incrémente, aucune animation > 200 ms`.

Jetons : `--motion-duration-instant: 100ms; --motion-duration-fast: 150ms; --motion-duration-base: 250ms; --motion-duration-slow: 350ms; --motion-ease-out; --motion-ease-in; --motion-ease-in-out` (valeurs à fixer dans `theme-design-system.md`). Figma : prototypage avec Smart Animate et courbes ressort pour l'intention ; la valeur de référence reste le jeton.

## 13. Check-list d'audit

- [ ] Chaque animation a une fonction écrite ; les décoratives sont facultatives.
- [ ] Durées et courbes issues des jetons ; aucune animation d'UI courante > 400 ms.
- [ ] Aucune propriété animée hors `transform`/`opacity` sans justification ; pas de CLS induit.
- [ ] `prefers-reduced-motion` testé (émulation DevTools : Rendering > Emulate CSS media feature) : plus de déplacement ample, de zoom ni de parallaxe.
- [ ] Contenus animés automatiquement > 5 s : bouton pause/arrêt (WCAG 2.2.2).
- [ ] Aucun clignotement > 3 par seconde (WCAG 2.3.1).
- [ ] Information jamais portée par la seule animation ; focus préservé après transition.
- [ ] Animations interruptibles sans saut ; double clic et navigation rapide testés.
- [ ] Fluidité vérifiée en ralentissement CPU ×4 sur mobile ; pas d'images longues.
- [ ] Bibliothèque d'animation justifiée, poids mesuré, chargement différé (`LazyMotion`) ; aucune dépendance abandonnée (`react-motion`).
- [ ] Fonctions non Baseline (cross-document View Transitions, scroll-driven) protégées par `@supports` ou détection et dotées d'un repli.
- [ ] Tests visuels stabilisés (animations désactivées ou figées pendant les captures).

## 14. Anti-patterns et pièges

- Animer pour « faire moderne » ; animations d'entrée de page qui retardent la lecture ; texte qui apparaît au défilement (le contenu reste invisible si le JS échoue).
- Parallaxe, zoom plein écran, défilement automatique sans réduction de mouvement ; carrousel automatique sans pause.
- `transition: all` : anime des propriétés imprévues et coûteuses.
- Durées différentes pour un même composant selon les écrans ; `linear` sur un déplacement.
- Squelettes ou indicateurs pour des réponses de 100 ms (clignotement) ; indicateur absent au-delà de 1 s.
- Importer tout `motion` (≈ 43 ko) pour un fondu ; garder `framer-motion` et `motion` en double dans le bundle.
- Nouvelles dépendances sur `react-motion` ; copier un extrait ancien de Framer Motion sans vérifier l'API actuelle.
- `view-transition-name` dupliqué sur une page (la transition est annulée).
- Tests E2E qui cliquent pendant une animation (cibles en mouvement) : attendre l'état stable via assertions, désactiver les animations en test (`reducedMotion: 'reduce'` dans le contexte Playwright, ou `animations: 'disabled'` pour les captures).

## 15. Sources

Consultées le 2026-11-03.
- Motion, Installation pour React : https://motion.dev/docs/react-installation
- Motion, Reduce bundle size : https://motion.dev/docs/react-reduce-bundle-size
- Motion, Accessibility : https://motion.dev/docs/react-accessibility
- npm, motion : https://www.npmjs.com/package/motion
- npm, react-motion : https://www.npmjs.com/package/react-motion
- npm, @react-spring/web : https://www.npmjs.com/package/@react-spring/web
- MDN, prefers-reduced-motion : https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- MDN, Using the Web Animations API : https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API
- Chrome for Developers, View Transition API : https://developer.chrome.com/docs/web-platform/view-transitions
- W3C, Understanding SC 2.3.3 Animation from Interactions : https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- W3C, WCAG 2.2 : https://www.w3.org/TR/WCAG22/
- web.dev, High-performance CSS animations : https://web.dev/articles/animations-guide
- NN/g, Executing UX Animations: Duration : https://www.nngroup.com/articles/animation-duration/
- NN/g, Response Times: The 3 Important Limits : https://www.nngroup.com/articles/response-times-3-important-limits/
- État des scroll-driven animations (source secondaire, juillet 2026) : https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026
