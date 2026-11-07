# Web mobile au toucher natif : une application web qui se comporte comme une application installée

Sur un téléphone, une application web se trahit par une dizaine de détails de plateforme, presque tous réglés par une déclaration CSS ou une balise. Lecture à la demande : application web ou PWA destinée au mobile, feuille, carrousel, mise en page plein écran, revue « ça va dans Chrome mais pas sur mon téléphone ». Mouvement : `mouvement-interface`.

## 1. Posture

- **Le téléphone fait foi.** L'émulation du navigateur de bureau ne reproduit ni le survol collé, ni le délai de tapotement, ni l'élastique, ni les zones sûres, ni le clavier logiciel. Sans appareil, dire ce qui est vérifié dans le code et ce qui reste à confirmer.
- **CSS ou balise avant JavaScript.** Un crochet « est-ce un écran tactile ? » pour masquer des survols est le mauvais outil ; une requête média est le bon.
- **Chaque correctif a sa raison** et ne s'applique que là où elle vaut : rendre un texte non sélectionnable est juste sur un bouton, fautif sur un paragraphe.
- **Capacités, pas appareils** : `(hover)`, `(pointer)`, `env()`, `dvh`. Jamais de détection par agent utilisateur ou largeur d'écran pour deviner le tactile. Tablette avec pavé, portable tactile, téléphone avec souris : on écrit pour les deux à la fois.
- **Le zoom reste permis** : `user-scalable=no` et `maximum-scale=1` sont des fautes d'accessibilité (WCAG 1.4.4).

## 2. Symptôme → correctif

| Symptôme | Correctif |
|---|---|
| Survol qui reste après un tapotement | styles de survol sous `(hover: hover) and (pointer: fine)` |
| Éclair gris ou bleu au tapotement | `-webkit-tap-highlight-color: transparent` |
| Hauteur fausse, bouton du bas masqué | `100dvh` (coquille d'application) ou `100svh` (accueil) |
| La page zoome sur un champ | police des champs ≥ 16 px |
| Tapotement mou | retour sur `:active` ou `pointerdown`, `touch-action: manipulation` |
| Le défilement déclenche le rafraîchissement | `overscroll-behavior` |
| Contenu arrêté par l'encoche | `viewport-fit=cover` et `env(safe-area-inset-*)` |
| Appui long qui sélectionne le libellé | `user-select: none` sur les commandes |
| Carrousel qui fait bouger la page | `touch-action: pan-y` ou défilement à aimantation |
| Barre d'état mal colorée | `theme-color` par schéma de couleurs |

## 3. Les correctifs expliqués

**Survol collé.** Sans survol réel, le navigateur en simule un au premier tapotement et le garde jusqu'au tapotement suivant. Les deux conditions comptent : la première dit que l'entrée principale sait survoler, la seconde qu'elle est précise. Tailwind 4 génère déjà son variant de survol sous `(hover: hover)` ; en version 3, une option de configuration l'active. Le retour tactile passe par `:active`.

**Éclair au tapotement.** iOS et Android voilent tout élément cliquable, signe le plus visible d'un site. On le neutralise sur `html`, et chaque élément tapable reçoit son propre `:active`.

**Hauteur.** Sur mobile, `100vh` correspond à la fenêtre la plus grande (barre d'adresse repliée) : au chargement, l'élément déborde et un bouton fixé en bas passe dessous. `dvh` suit l'apparition et la disparition des barres : juste pour une coquille d'application ou un tiroir, mais il provoque des décalages en plein défilement sur une page éditoriale. `svh`, la plus petite hauteur, est stable : juste pour un écran d'accueil. `lvh` reproduit l'ancien comportement. Ligne de repli en `vh` seulement si la matrice de compatibilité l'exige.

**Zoom à la saisie.** Safari iOS zoome sur un champ dont la police fait moins de 16 px et ne dézoome pas ensuite. Le correctif est la taille de police (au besoin seulement sous `(pointer: coarse)`), pas le blocage du zoom. Au passage, choisir le bon clavier : `inputmode="numeric"` pour un code, `"decimal"` pour un montant, `type="email"` ou `"tel"`, `autocapitalize="none"` et `autocorrect="off"` pour un identifiant, `enterkeyhint` (« envoyer », « rechercher », « terminé ») pour annoncer l'action de la touche Entrée. `autocomplete` renseigné (`one-time-code`, `postal-code`…).

**Tapotement mou.** Deux causes cumulées. Le délai historique d'environ 300 ms, gardé pour détecter un double tapotement, disparaît avec `touch-action: manipulation` sur les éléments interactifs. Et un retour posé sur `click` arrive au relâchement : on le place sur `:active` (ou `pointerdown` en JS), 100 à 160 ms en sortie douce, avec les jetons de mouvement du projet.

**Défilement qui s'échappe.** En haut de page, Android déclenche le rafraîchissement et iOS fait rebondir toute la page : normal pour un document, gênant dans une application à zones de défilement propres, une feuille qu'on tire ou un canevas. `overscroll-behavior: none` sur la racine ; `contain` sur chaque zone intérieure (contenu de feuille, fil de discussion), qui garde son propre rebond sans entraîner la page. Pas d'écouteur `touchmove` qui annule l'événement : il bloque le défilement et coûte des images.

**Encoche et zones sûres.** Par défaut, la page reste dans la zone sûre et le fond remplit le reste. Une application native peint bord à bord et écarte seulement son contenu. Balise viewport avec `viewport-fit=cover`, puis marges `env(safe-area-inset-top | bottom | left | right)` sur en-tête fixe, barre d'onglets, notifications et feuilles, avec une valeur de repli dans les calculs (`env(…, 0px)`). Sans la balise, ces valeurs valent zéro. **RTL et paysage** : on utilise les marges logiques (`padding-inline-start`) et l'on vérifie que les insets gauche et droite s'appliquent du bon côté.

**Appui long.** Un appui prolongé sélectionne le libellé d'un bouton ou ouvre le menu contextuel d'un lien. Sur les commandes (bouton, onglet, puce, poignée) : `user-select: none` avec son préfixe Safari, et `-webkit-touch-callout: none` si un lien ou une image sert de commande. Jamais sur `body` : adresses, messages d'erreur et numéros de commande se copient.

**Carrousel.** Un balayage horizontal est ambigu pour le navigateur. `touch-action` dit ce que le navigateur garde : `pan-y` sur un carrousel horizontal (il garde le vertical), `pan-x` sur une poignée de feuille verticale, `none` seulement sur une surface qui gère vraiment tous les axes, sinon on ne peut plus défiler par-dessus. Si le carrousel est un défilement natif, préférer `scroll-snap-type: x mandatory` et `scroll-snap-align` : la physique du navigateur bat un ressort fait main, et elle respecte le sens RTL.

**Barre d'état.** Sa couleur vient de `theme-color` : une seule valeur donne une barre sombre en mode clair ou l'inverse. Une balise par `prefers-color-scheme`, avec la couleur du haut de page (fond d'en-tête, pas couleur de marque), plus `color-scheme: light dark`. Thème basculé par classe : mettre la balise à jour au changement. PWA installée : `theme_color` et `background_color` du manifeste, et le style de barre d'état iOS, relèvent de la même décision.

## 4. Socle à poser dès le départ

Avant le premier composant :
- viewport : `width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content` (le clavier Android réduit alors la fenêtre comme sur iOS, et les champs fixés en bas suivent) ;
- deux balises `theme-color` (clair, sombre) ;
- sur `html` : voile de tapotement neutralisé, `-webkit-text-size-adjust: 100%` (pas de grossissement en paysage), `overscroll-behavior: none` sauf document où le rafraîchissement par traction est bienvenu ;
- champs de saisie à 16 px ;
- boutons et liens : `touch-action: manipulation`, non sélectionnables ;
- toutes les règles de survol regroupées sous `(hover: hover) and (pointer: fine)`.

## 5. Petits détails d'affichage

- Au-delà d'une semaine, une date relative (« il y a 340 jours ») devient une date absolue.
- Nombres qui changent : `font-variant-numeric: tabular-nums`.
- Grands titres : interlettrage resserré (vers −0,02 em).
- Corps de texte : lignes de 60 à 75 caractères (`max-width: 65ch`).
- Dégradé de fondu dont on voit le bord : ajouter des arrêts de couleur répartis sur une courbe douce.
- Avatar écrasé : `flex-shrink: 0`. Pluriels : `Intl.PluralRules`. Données extrêmes : `usine-logicielle/references/donnees-extremes-ui.md`.

## 6. À ne pas livrer

- Zoom bloqué au lieu de champs à 16 px.
- Survol hors requête de capacité.
- `100vh` sur une coquille d'application ; `100dvh` sur un accueil éditorial.
- Retour d'appui seulement au `click`.
- `touchmove` annulé pour bloquer le rebond.
- Texte de contenu non sélectionnable.
- `touch-action: none` sur une zone qu'il faut pouvoir défiler.
- `env(safe-area-inset-*)` sans `viewport-fit=cover`.
- Une seule `theme-color` pour deux schémas.
- Détection du tactile par agent utilisateur.
- « Corrigé » prononcé sur la foi de l'émulation.

## 7. Contrôles avant de rendre

- [ ] Socle de la section 4 présent, ou écart motivé.
- [ ] Chaque correctif appliqué avec sa raison, à l'endroit où elle vaut.
- [ ] Zoom autorisé ; cibles de 44 px (règles `HIG-` de `design-apple`).
- [ ] RTL et paysage vérifiés (insets, carrousel, marges logiques).
- [ ] Essai sur appareil réel : téléphone branché, serveur de développement écoutant sur le réseau local, inspecteur Safari ou `chrome://inspect` ; un modèle de quelques années, clavier ouvert, une fois en paysage, et en mode installé si la PWA est visée. Sinon, liste « à confirmer sur appareil » remise au `testeur-mobile`.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/mobile-native/SKILL.md`, `ui-cheatsheet.md`. Exclus : « Initial Response », blocs de code, mentions propres à un cadriciel au-delà de Tailwind. Fiche : `references/sources/renfort-github.md`.
