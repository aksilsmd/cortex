# Prototypes en variantes : explorer plusieurs directions et choisir sur pièce

Pour une pièce d'interface précise (une notification, une carte tarifaire, un bouton de suppression par maintien), on construit plusieurs versions **réellement différentes**, toutes fonctionnelles, que l'on fait défiler une à une dans un sélecteur. L'utilisateur choisit en regardant et en manipulant, pas sur description. Lecture à la demande, quand une décision de design se joue sur le ressenti ou quand `theme-design-system.md` demande de comparer des directions. Déclenchement seulement sur demande explicite ou par l'ordre de mission.

## Sommaire
1. Principe : diverger sans baisser la barre
2. Règles
3. Cadrer et reconnaître le terrain
4. Choisir les directions
5. Construire le banc d'essai
6. Le sélecteur
7. Vérifier et présenter
8. Retenir une variante
9. Contrôles avant de rendre

## 1. Principe : diverger sans baisser la barre

Toute la valeur est dans l'écart. Trois nuances de la même idée n'apprennent rien. Chaque variante est une direction qu'on pourrait défendre seule.

L'écart n'excuse pas la négligence : chaque variante respecte les règles de mouvement (`mouvement-interface`), d'accessibilité (`accessibilite.md`) et de design (`design-apple`). Une variante bâclée perd sur l'exécution et ne dit rien de sa direction.

## 2. Règles

- **Aucun code de production touché pendant l'exploration** : tout vit dans un espace isolé. L'intégration ne vient qu'après le choix, pour la seule variante retenue.
- **Chaque variante a un axe nommé** : disposition, densité, caractère, mouvement, modèle d'interaction. Partager les jetons du projet n'est pas converger : les variantes doivent paraître natives du produit.
- **Chaque variante fonctionne vraiment** : interactions réelles, mouvement réel, contenu vraisemblable (textes du produit, noms et montants plausibles, au besoin le jeu extrême de `usine-logicielle/references/donnees-extremes-ui.md`). Pas de faux texte, pas de bouton mort.
- **Le sélecteur est un outil, pas un concurrent** : son aspect est fixe d'un projet à l'autre et ne prend pas le thème du produit.
- **Nettoyer après le choix** : l'espace de prototype est supprimé, sauf demande contraire.

## 3. Cadrer et reconnaître le terrain

**Une seule pièce par tour.** Une demande trop large (« le tableau de bord ») se réduit à la pièce au plus fort effet ; le reste est proposé pour les tours suivants. Reformuler en une phrase : ce qu'est la pièce, où elle vit, ce qu'elle doit faire.

**Reconnaissance** : cadriciel et système de style ; jetons (couleurs, rayons, espacements, polices, courbes et durées) ; caractère du produit (grand public ludique ou outil de gestion sobre), qui borne l'audace de la variante la plus osée ; contexte de rendu (fond, voisins, tailles, langues dont l'arabe en RTL). Sans projet : apparence neutre (gris, un accent, pile de polices système).

## 4. Choisir les directions

Trois variantes par défaut, cinq au plus : au-delà, la comparaison se dilue.

Avant toute ligne de code, lister l'ensemble : un **nom qui décrit la direction** (« Sobre », « Éditorial », « Dense », « Ludique »), jamais « Option A, B, C », et un **axe**. Deux directions qui ne diffèrent que par la couleur d'accent ou le texte n'en font qu'une : en remplacer une par une vraie alternative (autre disposition, autre interaction, autre histoire de mouvement).

Terminé quand chaque variante a un nom, un axe, et que deux variantes ne partagent pas la même position sur un axe.

## 5. Construire le banc d'essai

- **Projet avec serveur de développement** : une route isolée (par exemple `/prototypes/<sujet>`), un fichier par variante et un petit fichier de banc. Rien de la production n'importe depuis cet espace.
- **Sans projet, ou maquette Dan-Cortex** : un fichier HTML autonome, CSS et JS en ligne, sans dépendance ni ressource distante, conforme à `maquettes.md` (nommé d'après l'écran, éléments interactifs balisés `data-el="EL-…"`).

Le banc affiche **une variante à la fois, en taille réelle, dans son contexte** : une notification a besoin d'une page derrière elle, une carte de ses voisines, un bouton de son formulaire. Les vignettes côte à côte faussent espacements et échelle. Le passage d'une variante à l'autre est **instantané** : c'est une action répétée des dizaines de fois par séance, donc sans animation.

## 6. Le sélecteur

Une pastille flottante sombre et translucide, en bas au centre, lisible sur fond clair comme sombre : un bouton par variante portant son nom, un séparateur fin, puis un bouton « Rejouer » présent seulement si au moins une variante a une entrée ou une animation d'état à relancer.

Contrat de comportement :
- touches `1` à `N` et flèches gauche/droite pour changer, `R` pour rejouer ; touches ignorées si le focus est dans un champ, une zone de texte, une liste ou un contenu éditable, ou si une touche de modification est enfoncée ;
- en RTL, les flèches suivent l'ordre visuel des boutons ;
- un seul bouton actif à la fois, marqué `aria-current="true"` ; le sélecteur est un `nav` avec un libellé accessible (« Variantes du prototype ») ; focus visible ;
- le choix survit au rechargement par un paramètre d'URL (`?v=2`), variante 1 par défaut ;
- changer de variante la remonte entièrement, pour rejouer ses entrées ; « Rejouer » la remonte sans changer ;
- l'indicateur du bouton actif peut glisser (environ 250 ms, sortie douce forte), activé seulement après le premier affichage pour que le chargement ne s'anime pas, et coupé sous `prefers-reduced-motion` ;
- si la variante occupe le bas de l'écran (pile de notifications, feuille, barre d'onglets), le sélecteur passe en haut ; aucune autre adaptation.

Le sélecteur reste hors du périmètre jugé : il ne figure ni dans les captures de recette ni dans le code intégré.

## 7. Vérifier et présenter

Lancer le banc, parcourir soi-même chaque variante : rendu, interactions, console propre ; captures de chaque variante si l'outillage le permet (390 et 1440 px, clair et sombre, FR et AR).

Présenter puis **s'arrêter : le choix appartient à l'utilisateur** (ou au chef d'orchestre selon l'ordre de mission). Pour chaque variante, dire honnêtement dans quel cas elle gagne et ce qu'elle coûte, sans glisser de favori ; si l'on demande une préférence, la justifier par le caractère du produit et la fréquence d'usage, pas par le goût. Si deux variantes ont convergé pendant la construction, en retirer une et le dire.

Indiquer où tourne le banc (URL ou chemin) et les touches.

## 8. Retenir une variante

- **Choix fait** : intégrer la variante selon les conventions du projet (arborescence, nommage, jetons), passer la revue (`mouvement-interface/references/audit-du-mouvement.md`, `controle-visuel.md`), puis supprimer l'espace de prototype. Consigner la décision et les variantes écartées au registre des décisions.
- **Nouveau tour** : garder le banc et refaire la section 4 en divergeant autour de la direction préférée.

## 9. Contrôles avant de rendre

- [ ] Une seule pièce, reformulée en une phrase.
- [ ] Trois à cinq variantes, chacune nommée avec un axe distinct.
- [ ] Toutes fonctionnelles, contenu vraisemblable, règles de mouvement et d'accessibilité tenues, RTL vérifié.
- [ ] Banc isolé de la production ; une variante à la fois, en contexte, bascule instantanée.
- [ ] Sélecteur conforme au contrat ; console propre.
- [ ] Forces et limites de chaque variante exposées à égalité au décideur (PO), choix tracé au registre des décisions, banc nettoyé après le choix.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/prototype/SKILL.md`, `skills/prototype/PICKER.md`. Exclus : « Initial Response », balisage, styles et code du sélecteur (seul son contrat de comportement est décrit), consigne de reprise à l'identique, sous-commandes. Fiche : `references/sources/renfort-github.md`.
