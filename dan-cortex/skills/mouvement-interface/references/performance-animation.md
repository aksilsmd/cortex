# Performance des animations : tenir le budget de chaque image

Méthode de diagnostic quand un mouvement saccade, et règles pour qu'il ne saccade pas. La question n'est jamais « est-ce joli ? » mais « chaque image est-elle prête à temps ? ». Une bonne courbe à 30 images par seconde ne se remarque plus. Lecture à la demande : animation hachée, choix d'une propriété, arbitrage CSS ou JS, tentation de `will-change`. Mobile natif : `usine-logicielle/references/mobile-react-native-animation.md`.

## 1. Deux pièges de posture

1. **« Chez moi c'est fluide. »** Un portable rapide masque presque tout. La référence est un téléphone de milieu de gamme ; sur un écran à 120 Hz, le budget est moitié moindre.
2. **Saupoudrer `will-change` et s'arrêter là.** C'est la dernière étape : la plupart des saccades viennent d'une mauvaise propriété ou d'un fil principal occupé, ce que `will-change` ne règle pas.

Toute correction proposée nomme la cause qu'elle traite ; on distingue ce qui est vérifié dans le code de ce qui demande un enregistrement sur appareil réel.

## 2. Symptôme → piste

| On observe | Première piste |
|---|---|
| Saccades générales | propriété de mise en page animée → `transform` / `opacity` |
| Ombre animée hachée | `box-shadow` → `filter: drop-shadow()` |
| Saccades seulement pendant une navigation ou un chargement | animation sur le fil principal → CSS ou Web Animations API |
| Raccourcis `x`/`y` d'une bibliothèque qui perdent des images | version ancienne → mise à jour ou chaîne `transform` complète |
| Animation faite main lente sous React | état modifié à chaque image → écrire dans le style via une référence |
| Glisser de plus en plus lent quand la liste grandit | variable CSS héritée → `transform` posé sur l'élément |
| Transition floue lente (Safari surtout) | flou animé trop fort → rester sous 20 px |
| Propriétés inattendues animées | `transition: all` → propriétés nommées |
| Décalage d'un pixel au début ou à la fin | changement de couche → `will-change: transform`, une fois constaté |
| Longue liste lente au défilement | trop de nœuds → virtualiser (n'afficher que le visible) |

## 3. Budget d'image

60 images/s donnent 16,7 ms par image ; 120 Hz, à peine plus de 8 ms. On conçoit pour le plus petit. Un recalcul de mise en page sur une page complexe peut dépasser 100 ms : ce n'est pas une image perdue, c'est une dizaine. Deux leviers : **le coût de chaque image** (ce qu'on anime) et **le risque d'être bloqué** (où cela s'exécute).

## 4. Ce que l'on anime : les trois étapes du rendu

Le navigateur peut avoir à recalculer la géométrie (*layout*), redessiner (*paint*), puis assembler les couches (*composite*). Plus on entre tôt, plus c'est cher.

| Niveau | Propriétés | Coût |
|---|---|---|
| Assemblage seul | `transform`, `opacity` ; selon navigateur `filter`, `clip-path`, `background-color` | le moins cher |
| Dessin + assemblage | `box-shadow`, `border-radius`, `color` | redessin à chaque image |
| Géométrie + dessin + assemblage | `width`, `height`, `padding`, `margin`, `top`, `left`, `border-width` | le plus cher ; peut déplacer tout le voisinage |

Descendre d'un niveau : grandir avec `scale()` plutôt que dimensions ou marges ; déplacer avec `translate()` plutôt que positions ou marges ; masquer avec `opacity` plutôt qu'en basculant `display`/`visibility` ; ombre avec `drop-shadow()` plutôt que `box-shadow`.

Une animation de `padding` sur un petit élément positionné peut passer sans dommage visible ; mais à rendu égal, la version en `scale()` ne peut pas régresser sur un appareil lent. Une marge latérale animée pousse aussi tout le contenu voisin à chaque image ; une translation ne pousse rien.

## 5. Où cela s'exécute : fil principal ou non

| Moteur | Fil |
|---|---|
| Boucle JS sur `requestAnimationFrame`, animations de mise en page des bibliothèques | toujours le fil principal |
| Web Animations API (et bibliothèques qui s'appuient dessus) | peut être accéléré hors fil principal |
| Transitions et animations CSS | peuvent être accélérées |

« JS » n'équivaut pas à « fil principal » : une bibliothèque qui délègue à la Web Animations API peut être accélérée, une boucle `requestAnimationFrame` non. Accélération fiable : `transform`, `opacity` ; en progression : `filter`, `clip-path`, `background-color`.

Cas à surveiller : **un mouvement qui joue pendant un travail lourd** (changement de page, indicateur d'onglet pendant la navigation, hydratation, chargement de données). Le basculer en CSS suffit souvent.

Avec Motion (option, licence MIT à revérifier avant usage) : opacité, transformation, découpe et filtre passent par la Web Animations API ; les raccourcis `x`, `y`, `scale`, `rotate` sont accélérés à partir de la 14.2. Restent sur le fil principal dans toutes les versions : animations de mise en page partagée, rappels à chaque image, inertie, valeurs pilotées par un glisser.

L'accélération est une amélioration progressive que le navigateur peut refuser (certains moteurs ont longtemps écarté les translations en pourcentage). Ce n'est pas une raison d'abandonner `translateY(100%)` pour un élément de taille inconnue : la justesse passe avant une optimisation incertaine.

## 6. React : ne pas animer par l'état

Les bibliothèques animent hors du cycle de rendu. Le piège est l'animation faite main qui met à jour un état à chaque image : un rendu toutes les 16 ms épuise le budget. On écrit directement `element.style.transform` via une référence (ou une valeur de mouvement). À chercher : mises à jour d'état dans `requestAnimationFrame`, `pointermove`, `scroll` ou un gestionnaire de glisser.

## 7. Deux pièges qui ont l'air corrects

Tous deux animent bien `transform`, et perdent pourtant des images.
- **Variable CSS héritée.** Écrire la distance de glisser dans une variable du parent lue par `translateY()` force le recalcul des styles de tous les descendants à chaque image : plus il y a de contenu, plus c'est lent. Poser `transform` sur l'élément lui-même. À soupçonner dès qu'une animation se dégrade quand le contenu grandit.
- **Flou.** `filter: blur()` devient vite coûteux, surtout sur Safari. Sous 20 px ; 2 à 5 px suffisent pour adoucir un fondu enchaîné.

## 8. `will-change`, en dernier

Le passage d'un élément du processeur à la carte graphique en cours d'animation peut le décaler d'un pixel au début ou à la fin ; `will-change: transform` le promeut à l'avance. On l'ajoute **seulement après avoir constaté** le décalage ou mesuré des pertes d'images : les navigateurs promeuvent déjà ce qui anime `transform` ou `opacity`, et chaque couche coûte de la mémoire graphique. Sur l'élément qui bouge, jamais sur `*` ni sur un grand conteneur. Utile pour un dessin coûteux (grand élément flouté) : couche petite de préférence.

## 9. CSS ou bibliothèque ?

Le JS n'est pas à proscrire : il ne souffre que si la page est occupée pendant l'animation. Une bibliothèque apporte de vrais ressorts, des animations de mise en page partagée, des sorties d'éléments démontés, des gestes avec élan. Partage de travail : **CSS** pour le simple et pour tout ce qui joue pendant un chargement ; **bibliothèque**, si l'ADR l'accepte, pour le complexe, l'interruptible, le gestuel. Aucune dépendance n'est ajoutée pour des raisons de performance sans mesure avant/après.

## 10. Démarche en trois temps

**1. Inventaire** : élément, moteur, propriétés réellement animées (développer `transition: all` et les raccourcis), moment où il joue (survol, glisser, navigation).

**2. Diagnostic**, dans l'ordre de fréquence des causes :
1. propriétés hors `transform`/`opacity` (mise en page d'abord, puis `box-shadow`, `border-radius`, faciles à manquer) ;
2. coïncidence avec une page occupée ;
3. rendu React à chaque image ;
4. dégradation avec la quantité de contenu (variable héritée, trop de nœuds animés) ;
5. variable CSS animée, raccourcis d'une version ancienne ;
6. flou animé au-delà de 20 px ;
7. reste un décalage : `will-change` sur l'élément animé.

Confirmer par un enregistrement, pas au ressenti : panneau Performance des DevTools (images perdues, tâches longues), panneau Animations pour ralentir. Profiler sur un téléphone moyen par débogage à distance : le bridage du processeur sur un ordinateur simule un processeur lent, pas une carte graphique faible ni une mémoire réduite (voir `usine-logicielle/references/formation-chrome-devtools.md`).

**3. Rapport** : pour chaque constat, élément et `fichier:ligne`, cause, avant, après, et « vérifié dans le code » ou « à enregistrer sur appareil ». Classer par coût : géométrie avant dessin, fil occupé avant fil libre. On applique les corrections sur demande ou selon l'ordre de mission.

## 11. Contrôles avant de rendre

- [ ] Aucune `transition: all` ; propriétés listées.
- [ ] Propriétés animées au niveau « assemblage » ou justifiées.
- [ ] Rien d'animé par l'état React à chaque image ; aucune variable héritée pilotée à chaque image.
- [ ] Mouvements joués pendant un chargement passés en CSS ou Web Animations API.
- [ ] `will-change` seulement là où un problème a été constaté.
- [ ] Variante `prefers-reduced-motion` conservée après optimisation.
- [ ] Mesure sur appareil réel ou mention « à vérifier ».

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/animation-performance/SKILL.md`, `performance-cheatsheet.md`. Exclus : « Initial Response », anecdotes de produits tiers, gabarit de rapport tel quel. Fiche : `references/sources/renfort-github.md`.
