# Règles Apple pour les grands écrans et les outils de gestion

À appliquer aux interfaces de travail sur ordinateur et tablette (ERP, back-office, caisse, planning, tableaux de bord), en complément de `regles-web-mobile.md`. Identifiants `HGE-n.m`. Priorités : **C** critique, **H** haute, **M** moyenne.

## 1. Structure de fenêtre (C)

- **HGE-1.1** : trois zones stables : une barre latérale de navigation (repliable), une barre d'outils propre à l'écran, et le contenu. Aucune ne bouge quand on change d'élément.
- **HGE-1.2** : modèle maître-détail. La liste reste visible et le détail s'ouvre à côté (panneau ou colonne) sur grand écran ; il ne s'affiche jamais sous une longue liste. En dessous de 1024 px, le détail devient une page ou une feuille.
- **HGE-1.3** : l'élément sélectionné est marqué dans la liste, et son identifiant figure dans l'adresse (lien partageable, retour du navigateur).
- **HGE-1.4** : l'espace s'adapte : les colonnes optionnelles se masquent avant que le texte ne se coupe, et la largeur choisie d'un panneau est mémorisée.

## 2. Barre latérale (H)

- **HGE-2.1** : on groupe par domaine (Ventes, Catalogue, Stock, Équipe, Réglages) avec des intitulés courts, une icône cohérente et un compteur discret pour ce qui attend une action.
- **HGE-2.2** : la section active se voit (fond teinté, `aria-current`). La barre latérale reste visible sauf si l'utilisateur la replie, et son état est mémorisé.
- **HGE-2.3** : jamais plus de deux niveaux. Au-delà, on utilise des onglets ou des filtres dans le contenu.

## 3. Barre d'outils et actions (H)

- **HGE-3.1** : l'action principale de l'écran (« Nouvelle commande », « Valider ») est à droite de la barre d'outils, en bouton principal unique. Les actions secondaires sont regroupées, et les actions rares vont dans un menu « Plus ».
- **HGE-3.2** : la barre d'actions d'un détail reste visible au défilement (collante en haut ou en bas). Les actions sans objet sont masquées ou désactivées avec une explication au survol et au focus.
- **HGE-3.3** : les filtres sont des puces avec compteurs (« À valider 12 ») appliqués aussitôt. La recherche est en haut de liste, tri et densité sont choisis par l'utilisateur et mémorisés.
- **HGE-3.4** : les actions en masse apparaissent quand on sélectionne plusieurs lignes, avec le nombre sélectionné et une annulation possible.

## 4. Clavier (C)

- **HGE-4.1** : tout parcours fréquent se fait sans souris : flèches dans les listes et les grilles, Entrée pour ouvrir, Échap pour fermer ou annuler, Tab dans un ordre logique.
- **HGE-4.2** : raccourcis standards : `/` ou `Ctrl+K` pour chercher, `N` pour nouveau dans une liste, `Ctrl+S` pour enregistrer un formulaire, `?` pour la liste des raccourcis. Ils ne s'appliquent jamais pendant une saisie dans un champ et ne masquent pas les raccourcis du navigateur ni du lecteur d'écran.
- **HGE-4.3** : dans une grille (planning, tableau éditable), on applique le modèle ARIA `grid` : une seule tabulation pour entrer, puis les flèches pour se déplacer.
- **HGE-4.4** : un glisser-déposer a toujours une alternative au clavier et sans glisser (WCAG 2.5.7) : menu « Déplacer vers… », champs de date ou d'heure.

## 5. Pointeur (H)

- **HGE-5.1** : un élément cliquable montre un état de survol discret, et le curseur change seulement pour les liens, le glisser et le redimensionnement.
- **HGE-5.2** : une infobulle complète une information, ne la remplace jamais. Elle s'ouvre aussi au focus, se ferme avec Échap, et son contenu reste lisible au survol (WCAG 1.4.13).
- **HGE-5.3** : le menu contextuel (clic droit) ne contient que des actions présentes ailleurs. Les zones de glisser sont signalées au survol et pendant le glisser (zone de dépôt surlignée, aperçu).

## 6. Données denses (H)

- **HGE-6.1** : les tableaux ont un en-tête collant, des chiffres tabulaires alignés, des unités dans l'en-tête et non dans chaque cellule, et des statuts en pastille texte et couleur.
- **HGE-6.2** : on propose deux densités (confort et compacte). Une ligne fait au moins 32 px en mode compact et 44 px en tactile.
- **HGE-6.3** : vide, chargement et erreur ont chacun un état dédié avec l'action suivante (« Aucune commande à valider, voir toutes les commandes »).
- **HGE-6.4** : le calendrier et le planning ont des lignes par ressource et des colonnes par temps, aujourd'hui et l'heure actuelle marqués, des blocs à coins arrondis colorés par catégorie avec libellé, les conflits signalés par une icône et un texte, et la navigation précédent, aujourd'hui, suivant.

## 7. Retours et notifications (M)

- **HGE-7.1** : une action réussie donne un retour en place (ligne mise à jour, toast « Commande validée » avec « Annuler » si c'est réversible) sans recharger toute la page ni perdre la sélection.
- **HGE-7.2** : une confirmation modale n'existe que pour l'irréversible ou le coûteux. Elle nomme l'objet et la conséquence, et le bouton reprend le verbe (« Supprimer la commande »), pas « OK ».
- **HGE-7.3** : une erreur dit ce qui s'est passé et quoi faire, garde la saisie, et le focus va dessus.

## 8. Fenêtres secondaires (M)

- **HGE-8.1** : un popover sert à un réglage court ancré à son bouton. Une feuille ou un panneau sert à une tâche ; une page sert à un travail long.
- **HGE-8.2** : on n'ouvre jamais de dialogue par-dessus un dialogue. Fermer revient à l'état précédent, focus compris.

## Contrôles avant de rendre

1. À 1366 × 768, l'action principale de chaque écran de travail est visible sans défilement, et à 390 px elle est atteignable en un geste.
2. Le parcours fréquent (par exemple valider une commande) tient en trois clics au plus, et se fait aussi au clavier seul.
3. Le maître-détail conserve la sélection après une action, et l'adresse permet de rouvrir le même détail.
4. Chaque constat cite `HGE-n.m`, la largeur et la capture.

## Origine

Méthode reformulée en français (forme A), sans texte copié, d'après `ehmo/platform-design-skills` (MIT), fichiers `skills/macos/SKILL.md` et `skills/ipados/SKILL.md`, commit noté dans `../../maquettes-parcours/references/sources/renfort-github.md`. Référence officielle : Apple Human Interface Guidelines (developer.apple.com/design/human-interface-guidelines), WCAG 2.2 et ARIA Authoring Practices Guide.
