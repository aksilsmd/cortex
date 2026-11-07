# Règles Apple appliquées au web et au mobile

Chaque règle a un identifiant `HIG-n.m` à citer dans les constats. Les priorités vont de **C** (critique, bloque la fusion) à **H** (haute), puis **M** (moyenne).

## 1. Accessibilité (C)

- **HIG-1.1** : sémantique HTML d'abord (`main`, `nav`, `button`, `dialog`) ; un `div` cliquable est un défaut.
- **HIG-1.2** : chaque contrôle a un nom accessible qui contient le texte visible (WCAG 2.5.3). Une icône seule a un `aria-label`.
- **HIG-1.3** : tout se fait au clavier, dans un ordre logique, sans piège. Les dialogues retiennent le focus, Échap les ferme et le focus revient sur l'élément qui les a ouverts.
- **HIG-1.4** : le focus est visible (anneau de 2 px au moins, contraste 3:1) et n'est jamais masqué par une barre collante (WCAG 2.4.11).
- **HIG-1.5** : contraste AA de 4,5:1 pour le texte et de 3:1 pour le grand texte, les icônes et les bordures de champ, vérifié en clair, en sombre et sur les surfaces translucides.
- **HIG-1.6** : jamais la couleur seule : un statut porte aussi une icône ou un mot.
- **HIG-1.7** : les messages dynamiques (ajout au panier, erreur, compteur de résultats) passent par une région `aria-live="polite"`, et l'erreur bloquante par `role="alert"`.
- **HIG-1.8** : texte agrandi à 200 % sans perte de contenu (WCAG 1.4.4) ; à 320 px de large (zoom 400 %), aucun défilement horizontal (WCAG 1.4.10).
- **HIG-1.9** : on respecte les préférences du système : `prefers-reduced-motion`, `prefers-contrast: more`, `prefers-reduced-transparency`, `forced-colors`.

## 2. Mise en page et responsive (C)

- **HIG-2.1** : on part du mobile (390 px), puis on élargit. Les points de rupture suivent le contenu, et les requêtes de conteneur servent aux composants réutilisés.
- **HIG-2.2** : une cible tactile fait 44 × 44 px au minimum, avec 8 px entre deux cibles voisines.
- **HIG-2.3** : zones sûres (`env(safe-area-inset-*)`) respectées pour les barres fixes.
- **HIG-2.4** : l'action principale d'un écran mobile se trouve dans la zone du pouce (moitié basse), sous forme d'un bouton pleine largeur ou d'une barre collante.
- **HIG-2.5** : la grille et les espacements sont des multiples de 4 px (rythme principal de 8). Les alignements se font sur une même colonne, sans décalage d'un pixel.
- **HIG-2.6** : aucun défilement horizontal de la page. Seul un carrousel s'aligne avec `scroll-snap`.
- **HIG-2.7** : la largeur de lecture est de 60 à 75 caractères, et les tableaux larges défilent dans leur propre cadre ou deviennent des cartes libellées en mobile.

## 3. Formulaires (H)

- **HIG-3.1** : chaque champ a un libellé visible, jamais un simple texte indicatif.
- **HIG-3.2** : on utilise les bons types et attributs (`type="email"`, `tel`, `inputmode="numeric"`, `autocomplete="one-time-code"`, `name`, `street-address`) pour avoir le bon clavier et le remplissage automatique.
- **HIG-3.3** : la validation se fait en ligne à la sortie du champ, avec un message près du champ qui dit comment corriger. Le focus va sur le premier champ en erreur à l'envoi.
- **HIG-3.4** : les champs liés sont groupés (`fieldset` et `legend`), et l'obligatoire ou le facultatif est indiqué de façon constante.
- **HIG-3.5** : le bouton d'envoi passe en état « en cours » et empêche le double envoi. On ne le désactive pas avant la saisie sans expliquer pourquoi.
- **HIG-3.6** : un champ occupe la largeur de son conteneur dans un formulaire en une colonne, et tous les champs d'un même formulaire ont la même largeur.

## 4. Typographie (H)

- **HIG-4.1** : pile de polices système ; une police de marque reste hébergée sur place avec repli système.
- **HIG-4.2** : les tailles sont en `rem` pour suivre le réglage de l'utilisateur. Le corps fait au moins 16 px en mobile (pas de zoom automatique sur les champs), et aucun texte ne descend sous 12 px.
- **HIG-4.3** : on garde trois ou quatre tailles par écran. La hiérarchie vient de la taille et de la graisse ; les titres se suivent sans sauter de niveau (`h1` unique).
- **HIG-4.4** : l'interligne est de 1,4 à 1,5 pour le corps et de 1,1 à 1,2 pour les grands titres. Les grands titres prennent un léger interlettrage négatif.
- **HIG-4.5** : montants, quantités et dates sont en chiffres tabulaires et alignés à droite (à gauche en RTL selon le contexte). On utilise les vraies apostrophes, les guillemets typographiques et l'espace insécable avant l'unité.

## 5. Couleur et thème (M)

- **HIG-5.1** : il y a une seule couleur d'accent pour tout ce qui est interactif. Les couleurs sémantiques (succès, alerte, erreur, info) gardent leur sens partout.
- **HIG-5.2** : les fonds sont hiérarchisés (fond, surface groupée, surface élevée). En sombre, on évite le noir pur, et plus une surface est élevée, plus elle est claire.
- **HIG-5.3** : le thème système est le réglage par défaut et un choix manuel est mémorisé (clair, sombre, système). On ajoute `color-scheme` et `<meta name="color-scheme">`, et le bon thème s'applique avant l'affichage pour éviter le flash.
- **HIG-5.4** : jetons CSS ; aucune couleur en dur dans un composant.
- **HIG-5.5** : le verre (flou d'arrière-plan) est réservé aux surfaces flottantes, avec un repli opaque. Les ombres sont douces et en deux couches, et aucun dégradé ne doit gêner la lecture.

## 6. Navigation (C)

- **HIG-6.1** : en mobile, une barre d'onglets en bas regroupe les sections principales (5 au plus : accueil, rayons, recherche, panier, compte). Un menu « hamburger » ne cache jamais l'essentiel.
- **HIG-6.2** : la page porte un grand titre, qui se réduit au défilement. La section active est toujours signalée (`aria-current`).
- **HIG-6.3** : le retour du navigateur et le geste de retour marchent toujours. Un état utile (filtre, onglet, page) se retrouve dans l'adresse, et la position de défilement revient après un retour.
- **HIG-6.4** : les tâches courtes s'ouvrent dans une feuille ou un panneau latéral (détail de commande, panier, filtre), sans changer de contexte. Une tâche longue a sa page.
- **HIG-6.5** : reconnaître plutôt que retenir (suggestions, récemment consultés).

## 7. Composants (H)

- **HIG-7.1** : il y a trois niveaux de boutons, chacun au même rôle partout : principal (plein, un seul par zone), secondaire (teinté ou contour) et tertiaire (texte). Le destructif est rouge et demande une confirmation s'il est irréversible.
- **HIG-7.2** : l'alerte modale est réservée à l'information critique ou irréversible. Le reste passe par un message en ligne ou un bandeau temporaire (« toast ») non bloquant.
- **HIG-7.3** : les listes sont groupées en cartes à coins arrondis, avec séparateurs en retrait, ligne entière cliquable et chevron si elle mène ailleurs.
- **HIG-7.4** : la recherche est visible en permanence sur les écrans de catalogue. Les suggestions arrivent dès 2 caractères, et la saisie peut être effacée en un geste.
- **HIG-7.5** : pendant les chargements, on affiche des squelettes à la forme du contenu, pas un indicateur tournant qui bloque. Un indicateur apparaît après 300 ms, pas avant.
- **HIG-7.6** : vignettes au format constant, espace d'image réservé (`aspect-ratio`).

## 8. Mouvement (M)

- **HIG-8.1** : le mouvement explique (provenance, destination, relation). Il ne décore pas.
- **HIG-8.2** : on anime seulement `transform` et `opacity` : retours en 150–250 ms, surfaces en 300–400 ms, sortie plus rapide que l'entrée.
- **HIG-8.3** : avec `prefers-reduced-motion: reduce`, on passe à des fondus brefs ou à rien. Aucun contenu ne clignote plus de 3 fois par seconde.
- **HIG-8.4** : un effet de survol n'existe que sous `(hover: hover) and (pointer: fine)` et a son équivalent au focus clavier. Aucune information n'est accessible seulement au survol.

## 9. Performance perçue (H)

- **HIG-9.1** : le premier écran s'affiche sans attendre le JavaScript. Les images sous la ligne de flottaison se chargent en différé (`loading="lazy"`), et l'image principale arrive en priorité.
- **HIG-9.2** : une action a toujours un retour en moins de 100 ms (état pressé). Au-delà d'une seconde, on montre une progression.
- **HIG-9.3** : longues listes paginées ou virtualisées ; CLS < 0,1.

## 10. International et RTL (M)

- **HIG-10.1** : `lang` et `dir` sont posés sur `html`. On utilise les propriétés logiques CSS (`margin-inline-start`, `inset-inline-end`) plutôt que gauche et droite.
- **HIG-10.2** : les icônes directionnelles (flèches, chevrons, progression) s'inversent en RTL ; les icônes de sens fixe (lecture, logo, horloge) restent comme elles sont.
- **HIG-10.3** : dates, nombres et montants passent par `Intl`, et un nombre est isolé (`bdi` ou `dir="ltr"`) dans un texte RTL.
- **HIG-10.4** : pas de texte dans les images ; libellés prévus 30 à 40 % plus longs.

## Contrôles avant de rendre

1. Captures 390/768/1280/1440 px, FR et AR, clair et sombre, 200 % : rien de coupé ni hors écran.
2. Parcours au clavier seul, avec le focus toujours visible.
3. Contraste mesuré, verre compris.
4. Préférences du système simulées : mouvement réduit, contraste élevé, couleurs forcées.
5. Chaque constat cite `HIG-n.m`, l'écran, la largeur et la capture.

## Origine

Méthode reformulée en français (forme A), sans texte copié, d'après `ehmo/platform-design-skills` (MIT), fichiers `skills/web/SKILL.md` et `skills/ios/SKILL.md`, commit noté dans `../../maquettes-parcours/references/sources/renfort-github.md`. Référence officielle : Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines) et WCAG 2.2.
