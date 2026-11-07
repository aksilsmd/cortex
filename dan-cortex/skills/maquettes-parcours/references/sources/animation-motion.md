# Collecte — animation et motion

Pages consultées le 2026-11-03 (outils : Firecrawl scrape/query, WebSearch). Résumés et reformulations ; aucune copie de page.

| URL | Titre | Apport |
|---|---|---|
| https://motion.dev/docs/react-installation | How to install Motion for React | Paquet `motion`, import `motion/react`, React ≥ 18.2 ; App Router Next.js : directive `"use client"` ou import `motion/react-client` pour réduire le JS client ; Vite sans configuration. |
| https://motion.dev/docs/react-reduce-bundle-size | Reduce bundle size | Composant `motion` ≈ 43 ko non réductible ; `m` + `LazyMotion` ≈ 5 ko au rendu initial ; `domAnimation` +24 ko, `domMax` +38 ko ; `useAnimate` mini ≈ 3,3 ko (WAAPI seul) ; features chargeables par `import()` dynamique. |
| https://motion.dev/docs/react-accessibility | Create accessible animations in React | `MotionConfig reducedMotion="user"` coupe transform et layout animations, garde opacity/couleurs ; `useReducedMotion()` pour remplacer par un fondu, couper vidéo auto et parallaxe. |
| https://www.npmjs.com/package/motion | motion – npm | Version 14.9.0 publiée fin octobre 2026, licence MIT, JS/React/Vue. |
| https://www.npmjs.com/package/react-motion | react-motion – npm | Dernière version 0.5.2, publiée il y a environ 9 ans : bibliothèque abandonnée de fait. |
| https://github.com/chenglou/react-motion/issues/604 et /567 | Issues GitHub react-motion | Questions de la communauté sur la maintenance restées sans relève (signal d'abandon). |
| https://security.snyk.io/package/npm/react-motion | Snyk – react-motion | Fiche de suivi du paquet (aucune activité de maintenance récente). |
| https://www.npmjs.com/package/@react-spring/web | @react-spring/web – npm | Version 10.1.2 publiée il y a ~4 mois : alternative ressort maintenue. |
| https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion | prefers-reduced-motion – MDN | Valeurs `no-preference`/`reduce` ; Baseline largement disponible depuis janvier 2020 ; réglages OS (Windows 10/11, macOS, iOS, Android 9+) ; exemple : remplacer une mise à l'échelle par un fondu. |
| https://developer.chrome.com/docs/web-platform/view-transitions | Smooth transitions with the View Transition API | Same-document : Chrome/Edge 111, Safari 18, Firefox 144 ; cross-document (`@view-transition { navigation: auto }`) : Chrome/Edge 126, Safari 18.2, pas Firefox à la date de la page. |
| https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html | Understanding SC 2.3.3 | Critère AAA, intention (troubles vestibulaires, parallaxe), exception « essentiel », techniques C39 et SCR40 ; lien avec 2.2.2 pour les animations automatiques. |
| https://web.dev/articles/animations-guide | How to create high-performance CSS animations | Animer `transform` et `opacity`, éviter les propriétés qui déclenchent layout ou paint. |
| https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API | Using the Web Animations API | `element.animate()`, objet Animation (play, pause, reverse, `finished`, `playbackRate`), `fill`, `document.getAnimations()` ; moteur natif du navigateur sans rAF manuel. |
| https://www.nngroup.com/articles/animation-duration/ | Executing UX Animations: Duration | ≈ 100 ms pour un retour simple ; 200–300 ms pour un changement d'écran ; ≤ 400 ms pour grands déplacements ; à 500 ms l'animation devient pénible. |
| https://m3.material.io/styles/motion/easing-and-duration/tokens-specs | Material 3 – Easing and duration | Page consultée : contenu non extrait (rendu JS) ; la fiche ne reprend donc pas de valeur Material non vérifiée. |
| https://www.buildmvpfast.com/blog/css-scroll-driven-animations-replace-js-2026 | CSS Scroll-Driven Animations Go Cross-Browser (5 juil. 2026, source secondaire) | Chrome/Edge 115 (2023), Safari 26 (sept. 2025) ; Firefox stable 152 encore derrière un drapeau (juin 2026), priorité Interop 2026 ; pas Baseline : amélioration progressive obligatoire. |
