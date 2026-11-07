# Chorégraphie : coordonner plusieurs éléments qui bougent ensemble

Faire qu'un groupe en mouvement (liste qui entre, échange de vues, étapes, élément qui sort pendant que ses voisins se resserrent) se lise comme **un seul geste**, pas comme une file d'attente. Animation isolée : `construire-une-animation.md`. Lecture à la demande dès que plusieurs éléments bougent sur un même événement.

## 1. Le travers à éviter

Le réflexe est d'ajouter : délai croissant sur chaque enfant, panneau puis lignes qui ruissellent, vue qui attend la suivante. Chaque morceau est fluide ; l'ensemble fait patienter. Une bonne chorégraphie consiste surtout à **retirer des pièces mobiles et à faire jouer les autres en parallèle**. On ne séquence que si l'ordre a un sens : lecture, cause puis effet, arrivée physique d'un objet avant un autre.

Repères par défaut :
- **Une seule entrée par conteneur.** Si le panneau entre, son contenu est déjà là ; on n'anime pas le parent *et* ses enfants.
- **Pas de cascade sur une surface fréquente ou ouverte au clavier** (lignes de menu, palette, contenu d'onglet).
- **Pas de cascade uniforme** : des délais, distances et durées tous identiques font un métronome, l'équivalent d'une courbe linéaire pour un groupe.
- **Rien ne bloque l'action** : ce qui est visible est cliquable.
- **Une séquence supporte l'interruption** ; sinon elle n'est pas finie.

## 2. Distribuer les rôles

Avant tout réglage de temps, lister chaque élément qui bouge et lui donner un rôle.

- **Meneur** (le titre, la vue nouvelle, l'objet manipulé) : part en premier, parcourt le plus de distance.
- **Soutien** (sous-titre, boutons d'action, reste de la liste) : suit, avec un trajet plus court.
- **Ornement** (pastille, badge, filet, fond) : fondu sur place, ou rien.
- **Immobile** (tout le reste, y compris le conteneur dont le contenu s'anime) : ne bouge pas.

Deux meneurs possibles signalent un problème de hiérarchie, à remonter au maquettiste. Souvent le groupe rétrécit : un volet à huit entrées devient un seul mouvement, celui du volet.

## 3. Relier chaque paire

Pour deux éléments mobiles, quatre relations possibles :

- **Ensemble** (même objet, même instant, ou ordre sans signification) : même départ, même famille de courbes.
- **Chevauchement** ou cascade (ordre signifiant, les deux restent lisibles ensemble) : le second part pendant que le premier bouge.
- **Séquence** (ensemble, ce serait cassé : superposition, traversée, deux vues riches) : le second part à la fin du premier, ou juste avant.
- **Porter** (trajet de l'enfant non maîtrisable, par exemple mise en page partagée) : on anime le parent, l'enfant suit.

**Ensemble, par défaut.**
- Un élément qui sort quitte le flux tout de suite (sans bibliothèque : `position: absolute` à sa place courante), pour que ses voisins comblent le vide *pendant* son fondu, sans pause.
- Échanger deux vues dans un même conteneur est un fondu enchaîné : l'ancienne sort pendant que la nouvelle entre.
- Les sous-animations d'un composant partagent durée et famille de courbes (sinon un tiroir à 500 ms redimensionné en 200 ms ressemble à deux objets) ; le contenu peut avoir une courbe plus légère, de la même famille, fixée par une variable commune.

**Chevauchement.**
- Interface produit : 30 à 80 ms entre éléments, total ≤ ~300 ms. Pour une longue liste, ne décaler que les six premiers environ ; les suivants arrivent avec le dernier.
- Accueil marketing ou premier lancement : pas de 100 à 150 ms sur des entrées de 0,5 à 0,6 s, car vu une fois et porteur du message.
- L'ordre suit l'importance, pas l'ordre du DOM. Un titre et son premier paragraphe peuvent partager le même temps.
- On fait varier le traitement, pas seulement le délai : le meneur glisse plus loin, le soutien moins, l'ornement se contente d'un fondu. Des délais qui raccourcissent au fil du groupe donnent une vague.

**Séquence.**
- Conteneur qui change de largeur *et* de hauteur entre deux vues denses : l'ancienne part avant l'arrivée de la nouvelle (pour garder un fondu, dédoubler la vue sortante en position absolue, avec sa propre échelle).
- Objet qui traverserait visiblement un autre : retarder l'apparition de l'avant-plan jusqu'à l'atterrissage, sans séquence complète.
- Tracé de cause à effet (cadre puis coche) : délai du second ≈ durée du premier, état final conservé (`forwards`) ; démarrer le second un peu avant pour souder le geste.

## 4. Caler le secondaire sur le bon instant

Chaque animation de soutien s'accroche à un moment précis du meneur (départ, impact, arrêt), pas à un délai « qui a l'air bien ».
- Accrocher à la cause : dans un survol puis un clic, l'impulsion du fond part au clic.
- Les accents (traits, étincelles) se terminent avec le meneur, dans les derniers 20 % environ de la ligne de temps, le plus important en premier, les autres environ 40 ms après.
- Une action répétée saute la mise en place : mêmes proportions internes, déplacées plus tôt.

## 5. Adapter le temps à l'ampleur du changement

- **Durée selon la distance.** Pour un conteneur qui change de hauteur : durée = clamp(0,15 s ; |Δhauteur| / 500 ; 0,27 s). Un petit saut avec un long fondu ressemble à un clignotement.
- **Rebond selon la taille.** Un petit élément a besoin de plus de rebond pour paraître vivant ; un grand, de moins.
- **Peu d'états ? Valeurs écrites à la main** pour chaque transition. Une formule seulement quand les états sont trop nombreux pour être réglés un par un.

## 6. Sens de lecture, sorties, RTL

- « Suivant » pousse le contenu vers la fin de ligne inverse (en LTR, le nouveau arrive par la droite) ; « Précédent » fait l'inverse. **En RTL, tout s'inverse** : on exprime le sens avec un signe tiré de la direction du document, jamais avec « gauche » codé en dur. Entre menus voisins, le contenu arrive du côté du déclencheur d'origine.
- Une sortie lit son état à son démarrage : la direction doit lui être transmise explicitement (avec Motion, la propriété `custom` posée sur le conteneur de présence **et** sur l'enfant), sinon elle sort dans l'ancien sens.
- Les sorties sont simultanées, plus courtes, plus simples : pas de cascade inversée à la fermeture.
- Une sortie reprend le chemin de l'entrée.

## 7. Interruption et boucles d'attention

À tester systématiquement :
- relancer au milieu (quitter un survol à mi-course, double clic sur « Suivant », changer de menu pendant l'ouverture) : chaque relance arrête les animations en cours avant d'en lancer d'autres, sans empilement ;
- n'enchaîner qu'après la fin de *toutes* les animations de remise à zéro (attendre la promesse groupée) ;
- un drapeau « prêt » qui ne s'affiche pas se garde dans une référence, pas dans un état qui provoque un rendu ;
- bascule rapide de vues : vérifier qu'il ne reste pas deux enfants montés, clés stables et uniques.

Boucle d'attention (icône qui invite au geste) : première occurrence après environ 2,5 s, répétition rare (environ 6 s d'intervalle), arrêt pendant l'interaction, reprise après la remise à zéro. Elle respecte le mouvement réduit et ne tourne pas indéfiniment sur une page de travail.

## 8. Mouvement réduit

On **replie** la chorégraphie au lieu de la raccourcir : délais et déplacements supprimés, fondus conservés, groupe affiché d'un coup. Si la séquence *est* l'explication (illustration pas à pas), on passe d'une image à l'autre sans interpolation.

## 9. Mise en œuvre

- CSS (variable d'index × pas de délai, `fill-mode: both`) : entrées ponctuelles ; `both` évite que les éléments retardés montrent leur état final avant de partir.
- Bibliothèque déclarative (variantes et décalage avec courbe ou point de départ) : groupes qui entrent et sortent avec l'état de l'application ; **option**, licence et poids à l'ADR.
- Orchestration impérative (animations attendues, arrêtées, enchaînées) : seulement si plusieurs éléments se coordonnent sur plusieurs événements ; plus puissante, plus dure à maintenir.

Variable CSS héritée : bien pour une entrée ponctuelle, pas pour une valeur recalculée à chaque image (`performance-animation.md`).

## 10. Ligne de temps et contrôles

Avant de coder, écrire la ligne de temps (rôle, départ, durée, mouvement et relation de chaque élément mobile) dans la fiche du lot ou la matrice d'interactions ; y noter aussi ce qu'on a volontairement laissé immobile, et le moment à revoir image par image. Les écarts relevés en revue suivent le format de constat de `audit-du-mouvement.md`.

- [ ] Inventaire avec `fichier:ligne`, rôles attribués, mouvement retiré de tout ce qui n'est ni meneur ni soutien.
- [ ] Relation choisie et motivée pour chaque paire.
- [ ] Groupe d'interface produit terminé en ≤ ~300 ms ; aucune cascade sur surface fréquente.
- [ ] Contrôles d'interruption joués.
- [ ] Sens inversé en RTL ; variante réduite repliée.
- [ ] Test du « cinquantième usage de la journée » : si on le sauterait, on le coupe.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/choreograph/SKILL.md`, `skills/choreograph/RECIPES.md`. Exclus : « Initial Response », code des recettes. Fiche : `references/sources/renfort-github.md`.
