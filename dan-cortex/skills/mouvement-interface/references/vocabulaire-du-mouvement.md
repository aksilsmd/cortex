# Vocabulaire du mouvement : de « ce truc qui… » au mot juste

Glossaire inversé : de ce que l'on voit ou ressent au terme français, l'anglais entre parenthèses pour chercher ou demander à un outil. Sert à rédiger sans ambiguïté une exigence, une interaction (`EL-`), une anomalie ou une consigne de maquette. Lecture à la demande.

## 1. Mode d'emploi

- Lire l'intention : « ça rebondit », « ça résiste » décrivent une sensation.
- Donner le meilleur terme d'abord, puis une ou deux variantes avec ce qui les distingue (section 14).
- Sans correspondance exacte, le dire et décrire l'effet avec ces termes (« cascade d'entrées par agrandissement ») ; on n'invente pas de terme.
- Une question de nom appelle un nom, pas un exposé.

## 2. Apparaître et disparaître

- devient visible ou invisible par la transparence : fondu entrant / sortant (*fade in / fade out*)
- arrive depuis un bord de l'écran : entrée glissée (*slide in*)
- grandit jusqu'à sa taille, souvent avec un fondu : entrée par agrandissement (*scale in*)
- grandit et dépasse un peu avant de se poser : apparition rebondie (*pop in*)
- le contenu se découvre progressivement derrière une découpe : dévoilement (*reveal*)

## 3. Enchaîner dans le temps

- des jalons (0 %, 50 %, 100 %) reliés par le navigateur : images clés (*keyframes*)
- le calcul de toutes les positions intermédiaires : interpolation (*interpolation, tween*)
- les éléments partent l'un après l'autre, en cascade : décalage en cascade (*stagger*)
- plusieurs animations réglées pour n'en faire qu'une : orchestration, chorégraphie (*orchestration*)
- l'élément garde son premier ou son dernier état hors animation : mode de remplissage (*fill mode*)
- le mouvement avance par crans, comme un compte à rebours : animation par paliers (*stepped animation*)

## 4. Déplacer, tourner, déformer

- se déplace sur un axe : translation (*translate*)
- grossit ou rapetisse : mise à l'échelle (*scale*)
- pivote autour d'un point : rotation (*rotate*)
- penche comme un parallélogramme : inclinaison (*skew*)
- bascule en profondeur, comme une carte qu'on retourne : bascule 3D, retournement (*3D tilt, flip*)
- le point d'où part l'agrandissement ou la rotation : origine de transformation (*transform origin*)
- le menu semble sortir du bouton cliqué, pas de son propre centre : animation ancrée au déclencheur (*origin-aware animation*)

## 5. Passer d'un état à un autre

- l'un s'efface pendant que l'autre apparaît, au même endroit : fondu enchaîné (*crossfade*)
- on garde ses repères parce que l'avant et l'après sont visuellement reliés : transition de continuité (*continuity transition*)
- une forme se transforme en une autre : métamorphose (*morph*)
- une vignette voyage et devient la fiche détaillée : transition d'élément partagé (*shared element transition*)
- un élément qui change de taille ou de place glisse au lieu de sauter : animation de mise en page (*layout animation*)
- une section s'ouvre et se referme en hauteur : accordéon, repli (*accordion, collapse*)
- le contenu part d'un côté en avançant, de l'autre en revenant : transition orientée (*direction-aware transition*) ; s'inverse en RTL

## 6. Défilement et navigation

- les blocs apparaissent quand ils entrent dans la fenêtre : apparition au défilement (*scroll reveal*)
- l'avancement de l'animation suit la position du défilement : animation pilotée par le défilement (*scroll-driven animation*)
- fond et premier plan défilent à des vitesses différentes : parallaxe (*parallax*)
- une animation au changement de page ou de route : transition de page (*page transition*)
- le navigateur relie lui-même deux états ou deux pages : transition de vue (*view transition*)

## 7. Répondre à un geste

- changement quand le pointeur passe dessus : effet de survol (*hover effect*)
- le bouton s'enfonce légèrement au clic : retour d'appui (*press / tap feedback*)
- une jauge se remplit tant qu'on garde le doigt appuyé : maintien pour confirmer (*hold to confirm*)
- on attrape et on déplace, avec de l'élan au relâchement : glisser (*drag*)
- on réordonne une liste, les autres s'écartent : glisser pour réordonner (*drag to reorder*)
- on balaie un élément hors de l'écran pour le fermer : balayer pour fermer (*swipe to dismiss*)
- résiste puis revient quand on tire trop loin : effet élastique (*rubber-banding*)
- tremble de gauche à droite pour dire « non » : secousse (*shake, wiggle*)
- un cercle s'étend depuis le point touché : onde (*ripple*)

## 8. Courbes de vitesse

- la façon dont ça accélère ou ralentit : courbe d'accélération (*easing*)
- démarre vite, finit en douceur ; défaut de l'interface : sortie douce (*ease-out*)
- démarre lentement, finit vite ; paraît mou : entrée douce (*ease-in*)
- lent, rapide, lent ; pour aller d'un point à un autre à l'écran : entrée-sortie douce (*ease-in-out*)
- vitesse constante ; pour une roue de chargement ou un bandeau : linéaire (*linear*)
- une courbe sur mesure définie par quatre nombres : courbe de Bézier (*cubic-bezier*)
- accélère et freine à des rythmes différents : courbe asymétrique (*asymmetric easing*)

## 9. Ressorts et élan

- un mouvement réglé par une physique plutôt que par un chronomètre : ressort (*spring*)
- on peut l'attraper en route et lui faire changer de cap : animation interruptible (*interruptible animation*)
- combien et dans quel sens ça file, à un instant donné : vitesse (*velocity*)
- une carte lancée file encore un peu après le doigt : élan, inertie (*momentum*)
- petite exagération au-delà de la place finale, puis retour : rebond (*bounce*)
- ça oscille longtemps, ou au contraire se pose sans frémir : amortissement (*damping*) ; plus il est faible, plus ça oscille
- on voudrait que ça « claque » plus vite vers sa place : raideur (*stiffness, tension*)
- l'objet paraît lourd, lent à se mettre en route : masse (*mass*)
- l'œil juge l'animation finie alors que le calcul continue en micro-oscillations : durée perçue (*perceptual duration*)

## 10. Mouvements en boucle

- un texte qui défile sans fin : bandeau défilant (*marquee*)
- la boucle repart en sens inverse au lieu de sauter au début : aller-retour (*alternate, yoyo*)
- un élément tourne autour d'un autre : orbite (*orbit*)
- léger battement de taille ou d'opacité pour attirer l'œil : pulsation (*pulse*)
- lente dérive verticale, comme en apesanteur : flottement (*float*)
- petit mouvement quand rien ne se passe, pour inviter au geste : animation d'attente (*idle animation*)

## 11. Finitions

- un léger flou qui adoucit ou masque un défaut : flou (*blur*)
- découper un élément selon une forme nette : découpe (*clip-path*)
- même chose avec des bords fondus : masque (*mask*)
- une poignée qu'on glisse pour comparer deux images : comparateur avant/après (*before/after slider*)
- un tracé SVG qui se dessine : tracé progressif (*line drawing*)
- un texte qui change caractère par caractère : métamorphose de texte (*text morph*)
- un gabarit gris avec un reflet qui passe pendant le chargement : squelette, reflet (*skeleton, shimmer*)
- des chiffres qui roulent jusqu'à leur valeur : compteur animé (*number ticker*)
- des chiffres à largeur fixe qui ne dansent pas : chiffres tabulaires (*tabular numbers*)
- le texte s'écrit lettre après lettre : machine à écrire (*typewriter*)

## 12. Performance

- nombre d'images affichées par seconde : fréquence d'images (*frame rate, FPS*)
- saccade : saccade (*jank*)
- une image ratée, un petit accroc : image perdue (*dropped frame*)
- la carte graphique bouge une couche sans tout recalculer : assemblage de couches (*compositing*)
- prévenir le navigateur qu'un élément va bouger : indice `will-change` (*will-change*)
- recalcul de la géométrie à chaque image : emballement de mise en page (*layout thrashing*)

## 13. Notions de conduite

- le mouvement sert à quelque chose : mouvement utile (*purposeful animation*)
- un petit recul avant l'élan : anticipation (*anticipation*)
- des parties continuent un peu après l'arrêt : prolongement (*follow-through*)
- s'écrase et s'étire pour exprimer poids et vitesse : écrasement-étirement (*squash and stretch*)
- l'interface paraît plus rapide grâce au mouvement : performance perçue (*perceived performance*)
- plus c'est vu souvent, plus c'est court et discret : fréquence d'usage (*frequency of use*)
- l'élément garde son identité et sa place d'un état à l'autre : cohérence spatiale (*spatial consistency*)
- respecter le réglage « réduire les animations » : mouvement réduit (*reduced motion*)

## 14. Termes voisins à départager

- **Découpe ou masque** : bord net, ou bord fondu.
- **Apparition rebondie ou rebond** : une entrée, ou un comportement de ressort.
- **Élément partagé ou mise en page** : deux vues reliées, ou un même élément qui change de taille ou de place.
- **Fondu enchaîné ou métamorphose** : superposition sur place, ou transformation continue d'une forme.
- **Transition de vue ou de page** : un mécanisme du navigateur, ou le besoin qu'il sert.

## Origine

Glossaire reformulé en français (forme A, `robustesse-agents/references/renfort-externe.md`) : entrées réorganisées, définitions réécrites, terme anglais gardé comme clé de recherche. D'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichier lu : `skills/animation-vocabulary/SKILL.md`. Exclus : « Initial Response », consigne de citation à l'identique, exemples de dialogue. Fiche : `references/sources/renfort-github.md`.
