# Construire une animation : de la demande au code

Transformer « ajoute du mouvement ici » en une animation qui passe la revue (`audit-du-mouvement.md`) du premier coup. Lecture à la demande : avant d'écrire ou de modifier une transition, une entrée, une sortie ou un geste.

## 1. Les sept décisions, dans l'ordre

1. Fréquence d'usage : trop fréquent, on n'anime pas.
2. Raison d'être, en un mot : introuvable, on n'anime pas.
3. Outil le moins coûteux : CSS par défaut.
4. Propriétés : `transform` et `opacity`.
5. Courbe et durée, ou ressort.
6. Interruption et sortie : transition plutôt qu'images clés.
7. Variante réduite, survol réservé au pointeur fin, sens RTL : livrés avec l'animation.

Les deux premières filtrent le reste : « zéro ligne de code » est alors une réussite. Le second piège est d'animer le bon élément avec de mauvais ingrédients.

On tranche et on justifie en une ligne, sans proposer un éventail de variantes (sauf prototype : `maquettes-parcours/references/prototypes-en-variantes.md`).

## 2. Fréquence et raison d'être

**Budget selon la fréquence**

- Centaines de fois par jour (raccourci, palette de commandes) : changement instantané ; une action clavier ne s'anime pas.
- Dizaines de fois (survol, liste) : à peine perceptible, ou rien.
- Occasionnel (dialogue, tiroir, notification) : animation standard.
- Rare (premier usage, réussite) : seule place de l'agrément.

**Raison d'être** — la nommer avant de continuer : *retour* (l'interface a entendu), *continuité spatiale* (d'où vient et où va l'élément), *changement d'état* lisible, *transition* qui évite une téléportation brutale, *démonstration* (page marketing ou découverte), *agrément* (moments rares seulement). « C'est joli » sur un élément fréquent est une raison de s'arrêter.

Les données qu'on lit ou sur lesquelles on agit (graphique bancaire, tableau, montant) ne bougent pas pour le style.

## 3. Outil : le moins coûteux qui convient

| Besoin | Outil |
- **État piloté par une classe ou un attribut (survol, appui, bascule, couleur)** : transition CSS.
- **Entrée à l'insertion, sans état JS** : `@starting-style` (repli : attribut posé après le premier rendu).
- **Mouvement prédéfini qui doit rester fluide pendant un chargement** : animation CSS (hors fil principal).
- **Contrôle par programme, sans bibliothèque** : Web Animations API (`element.animate()`).
- **Ressort, animation de mise en page, sortie différée, valeur pilotée par un geste** : bibliothèque de mouvement, **en option**.

Option bibliothèque : Motion (`motion.dev`, licence MIT à revérifier avant usage, gratuite), courante en React, non imposée ; poids mesuré au build et inscrit à l'ADR. Toute nouvelle dépendance suit la règle Dan-Cortex (version exacte, verrou commité, avis du pôle Architecture). Si le besoin est un *composant* (notification, tiroir, menu, palette), voir d'abord `maquettes-parcours/references/choisir-une-bibliotheque-ui.md` : un composant fait main oublie souvent le focus et le clavier.

## 4. Propriétés animées

- `transform` et `opacity` en priorité : ni calcul de mise en page ni repeinte. `clip-path` est une troisième voie acceptable. `height` se tolère pour un accordéon, en durée courte, la hauteur étant mesurée (pas d'animation vers `auto` sans support natif).
- Une apparition part d'une échelle de 0,9 à 0,97 avec opacité nulle, pas d'une échelle nulle.
- Point d'origine : un menu, une infobulle ou un sélecteur grandit depuis son déclencheur (`transform-origin` calculé, ou la variable fournie par la primitive). Un dialogue centré reste centré.
- Les pourcentages dans `translate()` se rapportent à l'élément lui-même : `translateY(100%)` le décale de sa propre hauteur, quel que soit son contenu.
- Le `transform` d'un élément se pose sur l'élément lui-même, pas via une variable CSS du parent (sinon tous les enfants sont recalculés).
- Avec Motion, les raccourcis `x`, `y`, `scale` sont accélérés à partir de la version 14.2 ; avant, préférer une chaîne `transform` complète.

## 5. Courbe, durée ou ressort

**Courbe selon la situation**

| Situation | Courbe |
- **Entrée ou sortie d'un élément** : sortie douce (`ease-out`).
- **Déplacement ou métamorphose à l'écran** : entrée-sortie douce (`ease-in-out`).
- **Survol, couleur** : `ease`.
- **Mouvement continu (défilement, progression)** : `linear`.

Une courbe qui démarre lentement (`ease-in`) retarde l'instant que l'œil guette : à éviter pour l'interface. Les courbes natives sont molles ; jetons proposés si le projet n'en a pas déjà :

```css
:root {
  --courbe-sortie: cubic-bezier(0.23, 1, 0.32, 1);
  --courbe-deplacement: cubic-bezier(0.77, 0, 0.175, 1);
  --courbe-tiroir: cubic-bezier(0.32, 0.72, 0, 1);
}
```

Des jetons de mouvement existent déjà ? On les étend, sans second jeu ni courbe bricolée « qui ressemble ».

**Durées indicatives** : appui 100–160 ms ; infobulle 125–200 ms ; menu, sélecteur 150–250 ms ; dialogue, tiroir 200–500 ms ; démonstration marketing, plus long. Sous 300 ms pour l'interface courante, sauf raison écrite.

**Ressort** quand le mouvement suit un geste, peut s'inverser en route, ou doit paraître vivant. Deux écritures : par durée perçue et rebond (`duration: 0.5, bounce: 0.2`), plus simple à raisonner ; ou par masse, raideur, amortissement (`1 / 100 / 10`), plus fine. Rebond entre 0,1 et 0,3, réservé aux gestes et aux composants ludiques. Détails physiques : `mouvement-fluide-apple.md`.

## 6. Interruption, sortie, asymétrie

- Tout ce qu'on peut déclencher deux fois par seconde (notification, bascule) utilise une transition : elle repart de la valeur courante, alors qu'une animation à images clés recommence à zéro.
- Un geste se termine par un ressort, qui conserve la vitesse.
- Sortir par où l'on est entré : la symétrie rend le balayage pour fermer évident.
- Asymétrie volontaire : lent quand l'utilisateur décide (maintien pour confirmer une suppression, environ 2 s linéaire), rapide quand le système répond (relâchement, environ 200 ms).

## 7. Mouvement réduit, survol, RTL

- `prefers-reduced-motion: reduce` : moins de mouvement et plus doux, pas zéro. On garde les fondus et changements de couleur utiles à la compréhension, on retire translations, échelles et parallaxes. Côté React, lire la préférence et neutraliser le décalage.
- Survol animé seulement sous `@media (hover: hover) and (pointer: fine)` ; l'état `:active` reste valable au toucher.
- RTL : tout décalage horizontal s'inverse avec la direction (`:dir(rtl)` ou variable de signe), de même que les côtés d'un `clip-path: inset()` et l'origine d'un panneau latéral (côté début de ligne). Un tiroir « de gauche » devient « du côté début ».
- Accessibilité : une animation ne bloque jamais la saisie ni le focus ; le focus va dans un dialogue ouvert et revient au déclencheur à la fermeture.

## 8. Fiches de construction

- **Bouton pressé** : `scale(0.97)` sur `:active`, transition `transform` 160 ms courbe de sortie ; les enfants suivent, ce qui donne l'effet physique.
- **Menu, sélecteur, popover** : opacité 0 et `scale(0.95)` à l'état de départ et de fin, 200 ms, origine au déclencheur.
- **Infobulle** : même forme, 125 ms et `scale(0.97)` ; délai à la première ouverture, puis ouverture instantanée des voisines tant qu'une est ouverte.
- **Dialogue** : `scale(0.96)`, 250 ms, origine centrée ; le voile s'anime en opacité avec la même durée.
- **Tiroir, feuille** : `translateY(100%)` fermé, 500 ms courbe de tiroir ; avec glisser, voir geste ci-dessous.
- **Notification** : translation de sa propre hauteur avec `@starting-style`, `ease`, environ 400 ms : le ton du composant prime sur le budget générique ; l'équilibre opacité/hauteur dans une pile se règle à l'œil.
- **Accordéon** : hauteur mesurée et opacité, 200 ms, `overflow: hidden`.
- **Entrée en cascade** : décalage de 30 à 80 ms entre éléments, liste vue rarement ; jamais bloquant.
- **Maintien pour confirmer** : voile en `clip-path` qui se remplit en 2 s linéaire à l'appui, se rétracte en 200 ms au relâchement.
- **Onglet actif bicolore** : dupliquer la liste stylée « active », la découper au `clip-path` sur l'onglet courant et animer la découpe (250 ms) : texte et fond changent ensemble.
- **Apparition au défilement** : marketing seulement ; `clip-path` révélé une seule fois via `IntersectionObserver`.
- **Glisser pour fermer** : fermer si distance dépassée **ou** vitesse > environ 0,11 px/ms ; capture du pointeur ; ignorer un second doigt ; résistance croissante au-delà du bord ; retour en ressort.
- **Fondu enchaîné qui « double »** : flou léger (2 px, jamais plus de 20) et opacité 0,7 pendant la bascule ; coûteux sur Safari.
- **Contrôle par programme** : `element.animate()` avec une courbe des jetons et `fill: 'forwards'`.


## 9. Contrôles avant de rendre

- [ ] Fréquence et raison d'être notées en une ligne ; refus motivé si l'animation ne passe pas le filtre.
- [ ] Pas de `transition: all` ; propriétés nommées.
- [ ] Pas d'échelle nulle, pas de courbe à démarrage lent, durée ≤ 300 ms ou justifiée.
- [ ] Origine au déclencheur (dialogues exceptés).
- [ ] Variante réduite, survol réservé au pointeur fin, sens RTL vérifiés.
- [ ] Aucune dépendance ajoutée sans ADR.
- [ ] Ressenti signalé : lecture ralentie (×2 à ×5) ou image par image (panneau Animations), geste essayé sur un vrai téléphone, second regard le lendemain.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/animate/SKILL.md`, `skills/animate/RECIPES.md`, `skills/emil-design-eng/SKILL.md` (parties animation, gestes, performance, accessibilité). Exclus : sections « Initial Response », format de revue imposé, principes de promotion de bibliothèque. Fiche : `references/sources/renfort-github.md`.
