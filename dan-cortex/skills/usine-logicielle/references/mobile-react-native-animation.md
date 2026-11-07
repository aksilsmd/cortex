# Animation mobile en React Native et Expo

Un mouvement qui tient sur un vrai téléphone, pas seulement au simulateur. Même ordre de décisions que sur le web (`mouvement-interface/references/construire-une-animation.md`), avec trois différences : **pas de survol**, **deux environnements d'exécution** (React et interface), **le doigt posé sur l'élément**. Lecture à la demande : agent `developpeur-mobile`, revue par `testeur-mobile`.

## 1. Filtre et raison d'être

- Centaines de fois par jour (changement d'onglet, clavier, défilement, interrupteurs de réglages) : comportement de la plateforme ou rien. **Les onglets ne glissent pas** : ce sont des pairs, pas une hiérarchie.
- Dizaines de fois (retour d'appui, sélection de ligne) : sous 150 ms, ou rien.
- Occasionnel (feuille, dialogue, notification, étape de découverte) : animation standard.
- Rare (réussite, illustration d'état vide) : place de l'agrément.

Raison nommée en un mot (retour, continuité spatiale, état, transition, démonstration, agrément) ; sinon on n'anime pas.

## 2. Outil le moins coûteux

- Changement d'état sans geste (appui, bascule, couleur) : transition de style de Reanimated 4.
- Boucle, plusieurs étapes ou lecture au montage : animation à images clés de Reanimated.
- Montage, démontage, réagencement de liste : animations d'entrée, de sortie et de mise en page.
- Tout ce que touche un doigt ou ce qui dérive du défilement : valeur partagée, geste, style animé.
- D'un écran à l'autre : options de la pile native d'Expo Router, jamais refaites à la main.
- Feuille-écran (`formSheet`), onglets natifs, menus contextuels, grand titre repliable : composants natifs d'Expo Router, pas du JS.
- Tirer pour rafraîchir : `RefreshControl`, sauf interaction signature.
- Interface qui suit le clavier : bibliothèque dédiée au clavier, position réelle image par image.
- Illustration ou célébration : Lottie, jamais pour un état d'interface. Scène très lourde ou dessin libre : Skia.

Une valeur partagée seulement pour une valeur continue ou interruptible : un retour d'appui est une transition, un glisser est une valeur partagée.

## 3. Dépendances : options et licences

Aucune n'est imposée ; chacune passe par l'ADR, en version exacte compatible avec le SDK Expo, verrou commité.

- `react-native-reanimated` et `react-native-worklets` (MIT, à revérifier avant usage) : animation sur le fil d'interface ; Reanimated 4 exige la nouvelle architecture.
- `react-native-gesture-handler` (MIT, à revérifier avant usage) : gestes.
- `expo-router` (MIT, à revérifier avant usage) : navigation, feuilles, onglets natifs, menus.
- `expo-haptics` (MIT, à revérifier avant usage) : retours haptiques.
- `react-native-keyboard-controller` (MIT, à revérifier avant usage) : interface synchronisée au clavier ; fournisseur à la racine.
- `lottie-react-native` (Apache-2.0, à revérifier avant usage) : illustrations.
- `@shopify/react-native-skia` (MIT, à revérifier avant usage) : canevas ; poids notable, à revérifier avant usage.

L'`Animated` du cœur de React Native ne convient pas à un geste (il traverse le pont).

## 4. Propriétés

- `transform` et `opacity` sont gratuits ; dimensions, marges, `flex`, positions, `gap` relancent la mise en page du nœud **et de ses voisins** à chaque image. Exception : un élément en position absolue sans enfant (pastille d'onglet, remplissage de barre), où animer la largeur garde le rayon que `scaleX` déformerait.
- Apparition depuis 0,9–0,97 avec opacité nulle, jamais depuis zéro.
- `transform` est un tableau ordonné : translation avant échelle, sauf effet voulu.
- Ombre Android (`elevation`) et intensité de flou : ne pas les animer (redessin à chaque image) ; fondre l'opacité d'une couche déjà ombrée ou floutée.
- Les pourcentages de translation se rapportent à l'élément : une feuille se cache de sa propre hauteur.

## 5. Minuterie ou ressort

**Un doigt était en jeu ? Ressort.** Il garde la vitesse à l'interruption. Reanimated accepte directement durée perçue et taux d'amortissement :
- arrêt sans dépassement : 400 ms, amortissement 1 ;
- retour en place après un glisser : 400 ms, amortissement 0,8, avec la vitesse du geste ;
- feuille, tiroir : 300 ms, amortissement 0,8, avec la vitesse ;
- bord à ne pas franchir : bridage du dépassement activé.

Rebond seulement si le geste portait de l'élan. Sans doigt : sortie douce forte pour entrer et sortir, entrée-sortie douce pour se déplacer, linéaire pour une progression ; courbes `Easing.bezier(0.23, 1, 0.32, 1)`, `(0.77, 0, 0.175, 1)` et, pour une feuille, `(0.32, 0.72, 0, 1)`. Pas de démarrage lent.

Durées : appui 100–150 ms ; petit état 150–200 ms ; feuille : ressort d'environ 300 ms ; écran : celle de la plateforme. Projection et élastique : `mouvement-interface/references/mouvement-fluide-apple.md`.

## 6. Rester hors du fil de React

- **Pas de mise à jour d'état depuis un geste ou un défilement** : un rendu par image est la première cause de saccade. Valeur partagée et style animé : React ne refait aucun rendu.
- **Pas de rappel vers le fil de React à chaque image** : `scheduleOnRN` (qui remplace l'ancien `runOnJS`) se place en fin de geste, ou dans une réaction qui se déclenche au franchissement d'un seuil.
- Ne jamais lire ni écrire une valeur partagée pendant le rendu ; seulement dans les worklets, gestionnaires et effets.
- Accès par `.get()` et `.set()` (compatibles avec le compilateur React), mise à jour fonctionnelle possible.
- Fonction appelée depuis un worklet : directive `'worklet'` en tête, sinon échec sur l'appareil seulement.
- Gestes mémorisés (`useMemo`) ; avec Gesture Handler 3, suivre son API par crochets.

## 7. Appui, cibles, retours haptiques

- Retour à l'appui, validation au relâchement ; échelle 0,97 en 100–150 ms sur tout élément pressable.
- Cible de 44 × 44 pt (48 dp sous Android) : agrandir la zone (`hitSlop`), pas le visuel ; marge de rétention pour qu'un doigt qui glisse de quelques pixels n'annule pas l'appui.
- Haptique, avec parcimonie : sélection pour un cran franchi ; impact léger pour une aimantation ou une validation de glisser ; impact moyen pour une action destructive ; notification de réussite ou d'échec. **Même image que le visuel**, **une par action**, **jamais seule** (désactivée chez beaucoup, muette sur nombre d'appareils Android). Depuis un worklet, elle passe par `scheduleOnRN`.

## 8. Mouvement réduit, accessibilité, RTL

- Préférence système lue (crochet de Reanimated, ou option par animation qui suit le système) : moins et plus doux, pas zéro ; translations, échelles, parallaxes et dépassements retirés, transitions d'écran en fondu.
- Le texte grandit (taille système jusqu'à 200 %) : jamais d'animation vers une hauteur codée en dur ; mesurer avec `onLayout` ou animer une transformation.
- Un geste a toujours une alternative accessible : balayer pour supprimer s'accompagne d'une action d'accessibilité (`accessibilityActions`) et d'un bouton ; une feuille se ferme aussi par un bouton.
- **RTL** (`I18nManager.isRTL`) : signe des translations horizontales, côté du balayage pour supprimer, sens de l'indicateur d'onglets et des transitions inversés.

## 9. Recettes condensées

- **Retour d'appui** : `Pressable` et transition d'échelle.
- **Feuille à glisser pour fermer** : au début du geste, partir de la valeur courante (sinon saut) ; décider par la projection de vitesse, pas par une distance de 40 % ; transmettre la vitesse au ressort ; brider le dépassement à la fermeture ; élastique vers le haut.
- **Balayer pour supprimer** : seuil par vitesse ou distance ; ressort de retour ; retour haptique au franchissement du seuil, une fois.
- **En-tête qui se replie** : conteneur de hauteur fixe, contenu translaté et découpé ; jamais la hauteur animée au défilement.
- **Entrée de liste** : jamais d'animation d'entrée sur une ligne de liste virtualisée (les lignes recyclées clignotent) ; animer le conteneur une fois, ou seulement le réagencement.
- **Indicateur d'onglets** : pastille absolue sans enfant, position et largeur en ressort.
- **Transitions d'écran** : pile native ; feuilles Android limitées à trois crans, sans poignée ni pile imbriquée.
- **Notification** : sous 300 ms, sortie par le chemin d'entrée et environ 20 % plus rapide, marges de zone sûre.

## 10. Réglages qui cassent le mouvement

- Plugin Babel des worklets : fourni par le préréglage Expo ; dans un projet React Native nu, déclaré en dernier. Absent : erreur à l'exécution.
- Racine de l'application enveloppée par le conteneur de Gesture Handler, sinon aucun geste, sans erreur.
- Expo Go et le mode développement ne mesurent pas la fluidité : version de production, sur l'appareil le plus lent pris en charge.
- 120 Hz sur iPhone : la clé `CADisableMinimumFrameDurationOnPhone` doit être présente dans l'`Info.plist` (souvent par défaut) ; le budget passe à 8 ms.

## 11. Contrôles avant de rendre

- [ ] Filtre et raison notés ; onglets sans glissement.
- [ ] Aucune dépendance ajoutée sans ADR ; licences relevées.
- [ ] Rien d'animé par l'état React ; aucun rappel par image.
- [ ] Ressort avec vitesse pour tout geste ; projection pour décider.
- [ ] Mouvement réduit, taille de texte, alternative accessible au geste, RTL.
- [ ] Haptique synchronisée, unique, jamais seule.
- [ ] Ressenti vérifié sur version de production et appareil lent : lancer, interrompre, inverser.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/animate-expo/SKILL.md`, `skills/animate-expo/RECIPES.md`. Exclus : « Initial Response », commandes d'installation, code. Licences ajoutées par Dan-Cortex, à revérifier. Fiche : `references/sources/renfort-github.md`.
