# Mouvement fluide à la manière d'Apple, appliqué au web

Une interface cesse de paraître mécanique quand elle répond à l'instant, suit le doigt, se laisse rattraper en plein vol, prolonge l'élan et résiste doucement aux bords. Complète `design-apple`, qui reste la référence pour la mise en page, la typographie de base, les rayons, les matières et les ombres ; ici, seulement ce qui bouge. Lecture à la demande : geste, glisser, feuille, carrousel, ressort.

## 1. Fil conducteur

Chaque mouvement **part de la valeur affichée**, **hérite de la vitesse du geste**, **projette l'élan** et **peut être saisi et inversé à tout instant**. Le ressort, qui repart de l'état courant avec sa vitesse, sert ces quatre propriétés.

## 2. Réponse immédiate

- Le retour visuel part à l'appui (`pointerdown`, `:active`), pas au relâchement.
- Toute attente sur le chemin de l'entrée (anti-rebond, minuterie, fin de transition, délai de tapotement) est suspecte.
- Glisser, curseur, tiroir : suivi continu du pointeur, pas seulement une animation finale.

## 3. Manipulation directe

- L'objet reste collé au doigt **en conservant le décalage de prise** : le recentrer sur le pointeur à la saisie casse l'illusion.
- Pointer Events et `setPointerCapture` : le suivi continue hors des limites de l'élément.
- Garder un court historique des positions horodatées (quelques derniers mouvements) pour connaître la vitesse au relâchement.

## 4. Interruptibilité

C'est la propriété dont dépendent toutes les autres.
- Aucune entrée n'est verrouillée pendant une transition. Une feuille qui se ferme et qu'on rattrape suit le doigt, sans finir de se fermer d'abord.
- On repart toujours de la **valeur de présentation** (la transformation réellement affichée), lue au moment de l'interruption, et non de la valeur cible ; sinon, saut visible.
- Au changement de sens, la vitesse se raccorde au lieu d'être coupée net (sinon effet « mur ») : moteur de ressort qui reprend la vitesse courante.
- En deux dimensions : deux ressorts indépendants (X et Y).

## 5. Ressorts : amortissement et réponse

Apple raisonne avec deux paramètres lisibles plutôt que masse, raideur et amortissement :
- **Taux d'amortissement** : 1,0 = amorti critique, aucun dépassement ; en dessous, l'objet dépasse et oscille.
- **Réponse** (en secondes) : rapidité pour rejoindre la cible. Ce n'est pas une durée ; le temps d'arrêt découle des paramètres.

Le rebond se mérite : il n'apparaît que si l'utilisateur a fourni de l'énergie (lancer, relâchement en mouvement). Une surface qui s'ouvre d'elle-même se pose sans dépasser ; c'est l'élan donné par la main qui justifie l'oscillation.

| Ce qui bouge | Amortissement | Réponse (s) |
|---|---|---|
| Objet replacé à un nouvel endroit | 1,0 | 0,4 |
| Objet qu'on fait pivoter | 0,8 | 0,4 |
| Tiroir ou feuille qu'on ouvre ou ferme | 0,8 | 0,3 |

Valeurs relevées dans la source (`apple-design`, section 4). Sur le web, l'écriture « durée perçue + rebond » s'en approche (rebond 0 ≈ amorti critique) : sans rebond par défaut, 0,1 à 0,2 après un geste avec élan.

## 6. Passage de vitesse

À la fin du geste, l'animation repart **à la vitesse exacte du doigt** : aucune couture entre glisser et animer. Si le moteur attend une vitesse relative :

```
vitesse_relative = vitesse_geste / (valeur_cible − valeur_courante)
```

Exemple : 80 px/s pour 160 px restants donnent 0,5. D'autres moteurs prennent des px/s.

## 7. Projection d'inertie

Plutôt que de choisir le point d'arrêt le plus proche *du relâchement*, on projette où le geste mènerait, comme une décélération de défilement, puis on choisit le point d'arrêt le plus proche *de la projection*. Fonction utilisée par Apple (décroissance exponentielle, pas la formule de cinématique `v²/2a`) :

```
projection(v en px/s, d) = (v / 1000) × d / (1 − d)
d ≈ 0,998 (défilement normal) ; 0,99 (plus sec)
point_projeté = position_courante + projection(vitesse_relâchement)
```

Ensuite : cible = point d'arrêt le plus proche du point projeté, ressort lancé avec la vitesse du relâchement (section 6). Pour décider fermer ou revenir, on regarde le **signe** de la vitesse, pas seulement la position.

## 8. Cohérence spatiale et anticipation

Trois questions avant d'animer une apparition :
1. **D'où vient-elle ?** Du déclencheur : l'origine de transformation y est posée, pour qu'on voie quel bouton a ouvert quel panneau.
2. **Par où repartira-t-elle ?** Du même côté, pour que l'utilisateur prévoie la fermeture et le geste qui la provoque ; si l'aller et le retour sont réversibles, la courbe du retour est le symétrique de celle de l'aller.
3. **Où va-t-elle ?** Dès les premières images, la trajectoire montre l'état d'arrivée, au lieu d'un fondu neutre qui ne dit rien.

En RTL, « suivant », geste de retour et bords d'élastique horizontaux changent de côté ; le signe d'une vitesse horizontale s'interprète dans le sens de lecture du document.

## 9. Élastique aux bords

Au-delà d'une limite, la résistance croît avec la distance au lieu d'un arrêt sec ; l'arrêt sec paraît figé, la résistance dit « rien de plus ici ». Formule courante :

```
élastique(dépassement, dimension, c = 0,55)
  = (dépassement × dimension × c) / (dimension + c × |dépassement|)
```

## 10. Reconnaissance des gestes

| Phase | Ce que fait l'interface |
|---|---|
| Contact | état pressé immédiat ; rien n'est encore validé |
| Premiers pixels | sous ~10 px de déplacement, c'est encore un tapotement ; au-delà, la direction est choisie et le suivi devient 1:1 |
| Sortie de la cible | une tolérance de ~10 px autour d'elle ; au-delà, l'action s'annule, et revenir la réarme |
| Plusieurs gestes possibles | tous écoutés dès le départ, un seul retenu quand l'intention est nette ; pas de détecteur qui ne signale que la fin |
| Relâchement | validation |

Coût caché : prévoir un double tapotement oblige à attendre avant de valider un tapotement simple. On ne l'active que là où il sert.

## 11. Fluidité image par image

Un saut trop grand d'une image à l'autre fait stroboscope ; un mouvement très rapide gagne à un léger flou de vitesse. Horloge et propriétés : `performance-animation.md`.

## 12. Matières en mouvement

Valeurs de matière (flou, saturation, bordure, repli) : `design-apple`. Côté mouvement :
- Matière plus dense pour la structure et les grandes surfaces, plus légère pour l'interactif ; pas deux surfaces translucides claires l'une sur l'autre.
- Une tâche modale assombrit et fait reculer l'arrière-plan ; un panneau non bloquant se contente d'un décalage translucide, sans voile.
- Sous une barre flottante, un léger masque flou plutôt qu'un filet fixe.
- Une surface de verre apparaît en animant ensemble flou et échelle, plutôt qu'en simple fondu ; le flou coûte cher, donc surface petite et durée courte.

## 13. Retours multimodaux

Son et vibration s'ajoutent au visuel seulement pour un événement qui compte (validation, erreur, aimantation), déclenchés par cet événement même et sur la même image que lui ; un décalage entre les trois sens se perçoit comme une panne, et un excès de retours apprend à les ignorer. L'API Vibration manque sur iOS Safari : le visuel doit suffire seul. Ni son par défaut, ni vibration impossible à couper.

## 14. Mouvement réduit et préférences voisines

Réduire, c'est garder le retour sans effet vestibulaire.
- `prefers-reduced-motion: reduce` : glissements, ressorts et parallaxes remplacés par des fondus courts ou des changements statiques ; plus de dépassement ni d'élastique. Le suivi 1:1 d'un glisser voulu par l'utilisateur reste ; l'élan projeté après relâchement est raccourci.
- `prefers-reduced-transparency: reduce` : surfaces plus opaques, flou retiré.
- `prefers-contrast: more` : fonds presque pleins, bordure nette.
- À éviter : fond plein écran en mouvement, oscillation lente en boucle (vers 0,2 Hz), saut brusque de luminosité.

## 15. Typographie qui change avec la taille

Échelle, graisses et pile système : `design-apple`. En plus : interlettrage négatif sur les grands titres (vers −0,02 em), nul pour le corps ; interligne serré sur un titre (vers 1,05), 1,4 à 1,5 pour le corps, plus ample en arabe ; `font-optical-sizing: auto` si possible ; tailles en `rem`, mise en page tenue à 200 % ; sur verre, texte plus contrasté et un peu plus gras.

## 16. Contrôles avant de rendre

- [ ] Retour à l'appui, suivi continu, décalage de prise respecté.
- [ ] Interruption possible à tout instant, sans saut ni « mur ».
- [ ] Vitesse transmise au ressort ; projection pour choisir la cible.
- [ ] Élastique aux bords ; sens inversé en RTL.
- [ ] Mouvement réduit, transparence réduite et contraste élevé traités.
- [ ] Gestes essayés sur un vrai téléphone, enregistrement relu image par image.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`, synthèse de conférences WWDC ; aucune citation d'Apple reprise. Fichier lu : `skills/apple-design/SKILL.md`. Exclus : « Initial Response », citations, section des huit principes (déjà couverte par `design-apple`) et section processus. Fiche : `references/sources/renfort-github.md`.
