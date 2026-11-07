# Formation — Design web et mobile

Fiche de formation de haut niveau pour maquettiste, concepteur UX, développeurs front et mobile, testeurs et expert accessibilité. Elle complète `theme-design-system.md` (méthode et livrables) par les règles de métier chiffrées. Les valeurs datées viennent des sources primaires listées en fin de fiche (consultées le 2026-11-03) ; revérifie toute valeur avant de l'inscrire dans un livrable engageant.

## Sommaire
1. Objectifs
2. Grilles et mise en page
3. Typographie
4. Espacement et densité
5. Couleur, thèmes clair et sombre, contraste
6. Composants et états
7. Responsive : points de rupture et requêtes de conteneur
8. Mobile : navigation, tiroirs, feuilles, gestes, cibles
9. Material Design 3 et Apple HIG : ce qu'il faut savoir
10. Droite à gauche (RTL)
11. Back-office et tableaux de bord
12. E-commerce : listes, fiche produit, panier, tunnel (Baymard)
13. Check-list d'audit
14. Anti-modèles et pièges
15. Sources

## 1. Objectifs

À l'issue de la fiche, l'agent sait :
- poser une grille, une échelle typographique et une échelle d'espacement cohérentes, exprimées en jetons ;
- produire un thème clair et un thème sombre dont chaque paire de couleurs passe WCAG 2.2 AA ;
- choisir points de rupture et requêtes de conteneur, et la navigation adaptée à chaque classe de largeur ;
- appliquer les conventions Material 3 (Android) et HIG (iOS) sans les mélanger ;
- concevoir un écran dense de back-office et un tunnel d'achat conforme aux constats de Baymard.

## 2. Grilles et mise en page

Principes :
- Une grille sert l'alignement et le rythme, pas la décoration. Colonnes fluides, gouttières et marges fixes par classe de largeur.
- Mesure de lecture : 45 à 75 caractères par ligne pour le texte courant (`max-inline-size: 65ch` est un bon défaut).
- Aligner sur une trame de 4 px (petits écarts) et 8 px (structure). Material 3 et la plupart des systèmes de design utilisent cette base.

Repères de grille (Material 3, classes de largeur de fenêtre, en dp ≈ px CSS) :

| Classe | Largeur | Volets recommandés | Navigation recommandée |
|---|---|---|---|
| Compacte | < 600 | 1 | barre de navigation basse ; rail étendu modal |
| Moyenne | 600–839 | 1 (ou 2) | barre de navigation ou rail |
| Étendue | 840–1199 | 2 recommandés | rail (modal ou standard) |
| Large | 1200–1599 | 2 recommandés | rail standard étendu |
| Très large | ≥ 1600 | 1 à 3 | rail standard étendu |

Code — grille fluide sans media query :
```css
.grille {
  display: grid;
  gap: var(--esp-4);
  grid-template-columns: repeat(auto-fill, minmax(min(16rem, 100%), 1fr));
}
.page { max-inline-size: 75rem; margin-inline: auto; padding-inline: clamp(1rem, 4vw, 2rem); }
```

Règles :
- Utiliser les propriétés logiques (`margin-inline`, `padding-block`, `inset-inline-start`) partout : le passage en RTL devient gratuit.
- `subgrid` (Baseline) pour aligner les contenus de cartes voisines (titres, prix, boutons au même niveau).
- Pas de largeur fixe en px sur un conteneur de texte ; pas de hauteur fixe sur un bloc qui contient du texte traduisible.

## 3. Typographie

Principes :
- Une famille (deux au maximum). Les polices système (`system-ui`) coûtent 0 octet et respectent la plateforme.
- Échelle modulaire : ratio 1,2 (dense, back-office) à 1,25–1,333 (éditorial, marketing). 5 à 7 tailles suffisent.
- Taille de base 16 px sur le web (jamais moins pour le corps de texte) ; 17 pt est la taille « Body » d'iOS ; 14–16 sp pour le corps sur Android selon le rôle M3.
- Interlignage : 1,4 à 1,6 pour le corps ; 1,1 à 1,3 pour les titres.
- Unités : `rem` pour les tailles (respect du réglage utilisateur), `clamp()` pour la typographie fluide avec une borne en `rem`.

Code — échelle fluide :
```css
:root {
  --txt-0: 1rem;                                   /* corps */
  --txt-1: clamp(1.125rem, 1.05rem + .4vw, 1.25rem);
  --txt-2: clamp(1.25rem, 1.1rem + .8vw, 1.563rem);
  --txt-3: clamp(1.5rem, 1.2rem + 1.5vw, 1.953rem);
  --txt-4: clamp(1.875rem, 1.4rem + 2.4vw, 2.441rem);
}
body { font: 400 var(--txt-0)/1.5 system-ui, sans-serif; }
```

Règles opérationnelles :
- WCAG 1.4.4 : le texte doit rester lisible à 200 % de zoom ; 1.4.12 : supporter interlignage 1,5, espacement de paragraphe 2×, lettres 0,12 em, mots 0,16 em sans perte de contenu.
- WCAG 1.4.10 (redistribution) : aucun défilement horizontal à 320 px CSS de large (sauf tableaux, cartes, éditeurs).
- iOS : supporter Dynamic Type ; Apple recommande de permettre au moins 200 % d'agrandissement du texte (140 % sur watchOS).
- Chiffres tabulaires (`font-variant-numeric: tabular-nums`) dans les tableaux, prix et compteurs.
- Polices web : `font-display: swap`, sous-ensembles (`unicode-range`), 2 fichiers WOFF2 au plus au premier rendu, préchargement de la police du texte courant seulement.
- Multi-écritures (arabe, tifinagh, latin) : vérifier la couverture des glyphes et prévoir une police par écriture ; l'arabe demande un interlignage plus grand (≈ 1,6–1,8).

## 4. Espacement et densité

Échelle d'espacement (base 4 px) : 0, 2, 4, 8, 12, 16, 24, 32, 48, 64, 96. Nommer par rang, pas par valeur (`--esp-1` … `--esp-10`), pour pouvoir changer la densité.

Règles :
- Proximité (Gestalt) : l'écart interne d'un groupe est plus petit que l'écart entre groupes (ratio ≈ 1:2).
- Densité : définir 2 ou 3 niveaux (confortable, standard, compact) par jeton, pas par composant. Material prévoit des crans de densité négatifs (−4 dp de hauteur par cran) pour certains composants ; vérifier la liste des composants concernés dans la bibliothèque utilisée.
- Le mode compact ne réduit jamais la cible tactile sous 24 × 24 px CSS (WCAG 2.5.8) ni, sur mobile, sous 44 pt (iOS) / 48 dp (Android) recommandés.

## 5. Couleur, thèmes clair et sombre, contraste

### Jetons à trois niveaux
1. Primitives : palette brute (`--bleu-600: #1d4ed8`).
2. Sémantiques : rôle (`--couleur-fond`, `--couleur-texte`, `--couleur-accent`, `--couleur-danger`, `--couleur-bordure`, `--couleur-focus`).
3. Composant (facultatif) : `--bouton-primaire-fond`.

Seuls les jetons sémantiques changent entre clair et sombre. Material 3 nomme les rôles par paire : `primary`/`on-primary`, `surface`/`on-surface`, `surface-container-*`, `outline`, `error`/`on-error` ; reprendre cette logique de paires « fond / contenu sur fond ».

Code — thèmes par jetons, avec choix utilisateur :
```css
:root { color-scheme: light dark;
  --fond: light-dark(#ffffff, #121316);
  --texte: light-dark(#1b1c1f, #e4e2e6);
  --accent: light-dark(#0b57d0, #a8c7fa);
  --focus: light-dark(#0b57d0, #a8c7fa);
}
:root[data-theme="light"] { color-scheme: light; }
:root[data-theme="dark"]  { color-scheme: dark; }
body { background: var(--fond); color: var(--texte); }
```
`light-dark()` est Baseline depuis 2024 ; prévoir un repli `@media (prefers-color-scheme: dark)` si le parc cible inclut des navigateurs plus anciens.

### Contraste : la règle applicable est WCAG 2.2
| Élément | Seuil AA | Critère |
|---|---|---|
| Texte courant | 4,5:1 | 1.4.3 |
| Grand texte (≥ 24 px, ou ≥ 18,66 px gras) | 3:1 | 1.4.3 |
| Composants d'interface, icônes porteuses de sens, indicateur de focus, bordures de champs | 3:1 contre les couleurs adjacentes | 1.4.11 |
| AAA (si visé) | 7:1 / 4,5:1 | 1.4.6 |

APCA : ce n'est pas une norme. En avril 2026 le brouillon de WCAG 3 indique que l'algorithme de contraste « reste à déterminer » ; APCA a été retiré du brouillon en 2023. Usage admis : outil complémentaire de lisibilité (par exemple pour les textes fins ou le mode sombre), à condition que chaque paire passe aussi WCAG 2. Ne jamais justifier une non-conformité WCAG 2 par un score APCA.

Règles mode sombre :
- Fond gris très foncé (#121212 à #1e1e1e), pas de noir pur sous du texte blanc pur (halo) ; texte à ≈ 87 % de luminance.
- Élévation par éclaircissement des surfaces (M3 : `surface-container-low` → `highest`), pas par ombres.
- Désaturer les couleurs d'accent (les tons saturés vibrent sur fond sombre) ; recalculer chaque contraste, ils ne se transposent pas.
- Images et illustrations : prévoir des variantes ou un léger assombrissement ; logos sur pastille si nécessaire.
- Ne jamais transmettre une information par la couleur seule (1.4.1) : icône, texte ou motif en plus.

## 6. Composants et états

Chaque composant interactif documente ses états : repos, survol, focus visible, actif/pressé, sélectionné, désactivé, chargement, erreur, succès, vide. Material 3 matérialise les états par une « couche d'état » d'opacité fixe sur la couleur du contenu : survol 8 %, focus 10 %, pressé 10 %, glissé 16 % (valeurs M3 ; à vérifier sur la page « States » avant reprise).

Règles :
- Focus : `:focus-visible` avec contour ≥ 2 px et contraste 3:1 ; jamais `outline: none` sans remplacement. WCAG 2.4.11 (AA) : l'élément focalisé ne doit pas être entièrement masqué (bandeaux collants, bannière cookies).
- Bouton désactivé : préférer un bouton actif qui explique l'erreur au clic ; un désactivé n'est pas focalisable et n'explique rien.
- Un seul bouton primaire par zone de décision.
- Libellés de boutons : verbe + objet (« Valider la commande »), pas « OK ».
- Icône seule : nom accessible obligatoire et info-bulle ; les icônes ambiguës (hamburger excepté) demandent un libellé visible.
- Glisser-déposer : une alternative à un seul pointeur est obligatoire (WCAG 2.5.7, AA).

## 7. Responsive : points de rupture et requêtes de conteneur

Principes :
- Mobile d'abord dans le CSS (`min-width`), contenu d'abord dans la conception : le point de rupture se place là où le contenu casse, pas sur une liste d'appareils.
- Points de départ raisonnables, alignés sur M3 : 600, 840, 1200, 1600 px.
- Requêtes de conteneur (`@container`, Baseline depuis 2023) pour tout composant réutilisé dans des emplacements de largeurs différentes (carte produit en grille, en barre latérale, en carrousel). Les media queries restent pour la mise en page globale.

Code — composant piloté par son conteneur :
```css
.carte-hote { container-type: inline-size; }
.carte { display: grid; gap: var(--esp-3); }
@container (min-width: 28rem) {
  .carte { grid-template-columns: 10rem 1fr; }
}
```

Autres règles :
- Images : `srcset`/`sizes` ou `<picture>` ; `width` et `height` explicites (ou `aspect-ratio`) pour éviter les décalages (CLS < 0,1) ; `loading="lazy"` sauf l'image principale au-dessus de la ligne de flottaison, qui reçoit `fetchpriority="high"`.
- Unités de viewport mobiles : `100dvh` plutôt que `100vh` (barres d'adresse dynamiques).
- Zones sûres (encoches) : `env(safe-area-inset-*)` avec `viewport-fit=cover`.
- Ne jamais bloquer le zoom (`user-scalable=no`, `maximum-scale=1`).
- Préférences : `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast`, `forced-colors` (mode contraste élevé de Windows : tester que bordures et focus restent visibles).

## 8. Mobile : navigation, tiroirs, feuilles, gestes, cibles

Navigation :
- 3 à 5 destinations de premier niveau : barre basse (M3 « navigation bar », iOS « tab bar »). Libellés toujours visibles ; icône + texte.
- Plus de 5 destinations ou destinations rares : tiroir/rail modal en complément, jamais comme seule navigation d'une appli fréquente (découvrabilité faible).
- iOS : la barre d'onglets ne se cache pas pendant la navigation dans une branche ; le retour se fait en haut à gauche et par geste de bord. Android : le retour système (geste ou bouton) doit toujours fonctionner, y compris dans les feuilles et dialogues ; prévoir le « retour prédictif » d'Android.
- Bouton d'action flottant (FAB, M3) : une seule action principale par écran.

Feuilles (bottom sheets) et dialogues :
- Feuille modale : actions contextuelles, choix courts ; poignée visible, fermeture par glissement, par toucher hors feuille et par le retour système ; focus piégé tant qu'elle est ouverte, restitué à la fermeture.
- Feuille non modale/persistante : contenu complémentaire (lecteur, carte).
- Dialogue : décision bloquante uniquement, 2 actions au plus, verbe explicite.
- Web : `<dialog>` natif avec `showModal()` (gestion du focus et de la touche Échap incluse) ; `popover` (Baseline) pour menus et info-bulles non modaux.

Gestes :
- Tout geste a un équivalent visible (bouton, menu). Les gestes sont des raccourcis, pas l'unique chemin (WCAG 2.5.1 : gestes multipoints ou à tracé → alternative à un pointeur simple).
- Ne pas détourner les gestes système : bords gauche/droit (retour), bas (accueil), haut (notifications).
- Balayage destructeur (supprimer) : annulation possible (toast « Annuler » 5 à 10 s) plutôt que confirmation modale.

Cibles tactiles :
| Référence | Valeur |
|---|---|
| WCAG 2.5.8 (AA) | ≥ 24 × 24 px CSS, ou espacement équivalent |
| WCAG 2.5.5 (AAA) | ≥ 44 × 44 px CSS |
| Apple HIG iOS/iPadOS | taille par défaut 44 × 44 pt ; minimum 28 × 28 pt ; ≈ 12 pt de marge autour d'un élément avec cadre, ≈ 24 pt sans cadre |
| Material 3 | ≥ 48 × 48 dp (≈ 9 mm), 8 dp entre cibles ; pointeur ≥ 44 × 44 dp |

Règle Dan-Cortex : 44 × 44 (iOS/web tactile) et 48 × 48 (Android) comme cible par défaut ; 24 × 24 est un plancher légal, pas un objectif.

Zone du pouce : placer les actions fréquentes dans le tiers inférieur ; les actions destructrices loin des actions fréquentes.

Clavier virtuel : `inputmode` et `type` adaptés (`email`, `tel`, `numeric`), `autocomplete` normalisé (`postal-code`, `cc-number`, `one-time-code`), `enterkeyhint`.

## 9. Material Design 3 et Apple HIG : ce qu'il faut savoir

Material 3 (Android, web possible) :
- Couleur dynamique : schéma généré à partir d'une couleur source (espace HCT), rôles par paires, palettes tonales. Outil : Material Theme Builder.
- « M3 Expressive » (2025) : formes plus variées, nouveaux composants et système de mouvement à ressorts ; le système durée + courbe n'est plus maintenu (voir `formation-animation-motion.md`).
- Composants de navigation selon la classe de largeur (tableau §2) ; mises en page canoniques : liste-détail, flux, volet secondaire.
- Jetons de typographie par rôle : display, headline, title, body, label × large/medium/small.

Apple HIG (iOS, iPadOS) :
- Hiérarchie : barre de navigation (titre large qui se réduit au défilement), barre d'onglets, feuilles (détentes moyenne et grande), menus contextuels.
- Matériau « Liquid Glass » introduit avec iOS 26 (2025) : barres et contrôles translucides qui flottent au-dessus du contenu ; vérifier la lisibilité du contenu passant dessous et respecter les réglages « Réduire la transparence » et « Augmenter le contraste ».
- Typographie système (SF Pro) et Dynamic Type ; icônes SF Symbols.
- Respect de « Réduire les animations » (voir fiche animation).

Règle : une appli native suit la plateforme (Material sur Android, HIG sur iOS). Une appli multiplateforme (Flutter, React Native) adapte au minimum : navigation et retour, sélecteurs de date, feuilles, typographie système, retours haptiques. Un site web ne copie ni l'un ni l'autre à l'identique : il emprunte les patterns, pas les chromes.

## 10. Droite à gauche (RTL)

- `<html dir="rtl" lang="ar">` ; `dir="auto"` sur les champs saisis par l'utilisateur et les contenus générés.
- Propriétés logiques partout (§2) ; `text-align: start`.
- Miroir : navigation, flèches directionnelles, barres de progression, carrousels, icône « retour ». Pas de miroir : logos, chiffres, horloges, icônes de lecture média, coches, graphiques de données temporelles (selon convention locale à valider).
- Nombres : chiffres arabes occidentaux ou orientaux selon le marché — décision produit, pas choix du développeur. `Intl.NumberFormat` et `Intl.DateTimeFormat` pour le formatage.
- Texte bidirectionnel : isoler les fragments (`<bdi>`, `unicode-bidi: isolate`) pour les noms, références, numéros de commande.
- Tester une variante miroir réelle de chaque gabarit clé, pas seulement une capture.

## 11. Back-office et tableaux de bord

Principes : la tâche prime sur l'esthétique ; densité élevée mais lisible ; constance absolue des composants.

Tableaux de données :
- Alignement : texte à gauche (à droite en RTL), nombres à droite avec chiffres tabulaires, en-têtes alignés comme leur colonne.
- En-tête et première colonne collants pour les grands tableaux ; tri visible (`aria-sort`) ; filtres au-dessus, avec puces de filtres actifs effaçables.
- Hauteur de ligne : 40–48 px standard, 32–36 px compact (souris uniquement).
- Pagination ou défilement virtuel au-delà de ~100 lignes ; afficher le total.
- Actions de masse : case à cocher par ligne, barre d'actions contextuelle, confirmation pour l'irréversible, annulation si possible.
- Sur mobile : transformer en liste de cartes ou permettre le défilement horizontal du seul tableau (exception admise par 1.4.10).

Tableaux de bord :
- 5 à 9 indicateurs clés au-dessus de la ligne de flottaison ; chaque indicateur porte sa période, sa comparaison (vs période précédente ou objectif) et son unité.
- Type de graphique selon la question : évolution → courbe ; comparaison → barres horizontales triées ; part d'un tout → barre empilée ou anneau (≤ 5 parts) ; distribution → histogramme. Éviter camemberts 3D, doubles axes ambigus, jauges décoratives.
- Couleurs de séries distinguables par daltoniens et doublées d'un repère (étiquette directe, motif) ; contraste 3:1 des tracés (1.4.11).
- Chaque graphique a une alternative textuelle ou un tableau de données accessible.
- États : chargement (squelette), vide (« Aucune donnée sur la période » + action), erreur (message + réessayer), données partielles.

## 12. E-commerce : listes, fiche produit, panier, tunnel (Baymard)

Chiffres de cadrage (Baymard, consultés le 2026-11-03) :
- Taux moyen d'abandon de panier documenté : ≈ 70 % (70,19 % ou 70,22 % selon la page et la date de mise à jour).
- Gain moyen de conversion attendu par la seule refonte du tunnel : ≈ 35 % pour les grands sites.
- Motifs d'abandon (acheteurs américains) : 40 % frais supplémentaires inattendus (livraison, taxes) ; 18 % obligation de créer un compte ; 17 % tunnel trop long ou compliqué ; 12 % coût total non visible tôt ; 9 % moyen de paiement préféré absent.
- Nombre d'éléments de formulaire : un tunnel américain moyen en affiche ≈ 20 à 23 par défaut ; un tunnel optimisé peut descendre à ≈ 12 éléments (7 champs, 2 cases, 2 listes, 1 bouton radio).

Liste de produits (catégorie, recherche) :
- Carte produit : image cohérente (même ratio), nom, prix (et prix barré explicite), note avec nombre d'avis, variantes (pastilles couleurs), disponibilité ; zone cliquable entière ; ajout au panier rapide optionnel.
- Filtres : affichés en panneau sur desktop, en feuille plein écran sur mobile avec bouton « Voir N résultats » ; filtres pertinents par catégorie ; filtres appliqués visibles et effaçables ; ne jamais vider les résultats sans proposer d'élargir.
- Tri explicite (pertinence, prix, nouveauté, note).
- Recherche : tolérance aux fautes, synonymes, suggestions, page « aucun résultat » utile (corrections, catégories proches).

Fiche produit :
- Galerie : plusieurs vues, zoom, image en contexte/à l'échelle, vidéo si utile ; vignettes visibles.
- Prix total et frais de livraison estimés visibles avant le panier ; délai de livraison concret (date plutôt que « 3 à 5 jours »).
- Sélection de variante : état indisponible visible sans masquer l'option ; l'image change avec la variante.
- Caractéristiques en liste scannable ; guide des tailles ; avis avec filtres et avis négatifs accessibles (ils renforcent la confiance).
- Bouton d'ajout au panier : visible sans défilement sur mobile (barre collante acceptable) ; retour clair après ajout (mini-panier ou confirmation) sans forcer la redirection.

Panier :
- Récapitulatif : image, variante, quantité modifiable, suppression avec annulation, sous-total, livraison, taxes, total.
- Code promo : champ repliable (un champ visible pousse à quitter le site pour chercher un code).
- Réassurance près du bouton : retours, paiement sécurisé, délais.

Tunnel de commande (règles Baymard) :
- Commande sans compte proposée en premier et en évidence ; création de compte proposée après le paiement (mot de passe seul). 62 % des sites ne mettent pas l'option invité en avant.
- Tunnel linéaire, indicateur d'étapes fidèle, jamais deux fois la même page ; pas de vente croisée, d'inscription newsletter ni de fenêtre surgissante au milieu.
- Facturation = livraison par défaut ; « Complément d'adresse » derrière un lien ; un seul champ « Nom complet » si le marché le permet ; saisie assistée d'adresse et compatibilité avec le remplissage automatique du navigateur (`autocomplete`).
- Libellés persistants au-dessus des champs ; champs obligatoires et facultatifs tous deux marqués.
- Validation en ligne à la sortie du champ (pas pendant la frappe) ; messages précis en langage clair ; ne jamais effacer les données saisies après une erreur (surtout la carte) ; une erreur → défilement jusqu'à elle, plusieurs → résumé + marqueurs.
- Carte : validation Luhn, formatage par groupes de 4, type de carte détecté ; au moins un portefeuille tiers ; moyen le plus utilisé présélectionné ; libellé du bouton adapté (« Continuer vers PayPal ») en cas de redirection.
- Page de revue : modifier chaque bloc sur place ; aucun frais nouveau à ce stade.
- Mobile : clavier adapté par champ, autocorrection désactivée sur noms, adresses, e-mails.
- Spécificités locales à arbitrer avec le juriste et le métier : paiement à la livraison, délais de rétractation, mentions obligatoires, bouton « Commande avec obligation de paiement » (droit français/UE).

## 13. Check-list d'audit

Mise en page et typographie
- [ ] Grille et espacements sur trame 4/8, exprimés en jetons ; aucune valeur magique.
- [ ] Texte courant ≥ 16 px, 45–75 caractères par ligne, interlignage ≥ 1,4.
- [ ] Zoom 200 % et redistribution à 320 px sans perte ni défilement horizontal.
- [ ] Propriétés logiques ; variante RTL testée si le marché l'exige.

Couleur
- [ ] Chaque paire texte/fond ≥ 4,5:1 (3:1 grand texte) dans chaque thème ; composants, focus et bordures de champs ≥ 3:1.
- [ ] Aucune information portée par la couleur seule.
- [ ] Mode sombre conçu (surfaces, accents désaturés), pas inversé ; `forced-colors` vérifié.

Composants et interaction
- [ ] Tous les états documentés et maquettés ; focus visible et jamais masqué.
- [ ] Cibles ≥ 44 × 44 pt (iOS/web tactile), ≥ 48 × 48 dp (Android) ; jamais < 24 × 24 px.
- [ ] Chaque geste a une alternative visible ; retour système fonctionnel partout.
- [ ] Un seul bouton primaire par zone ; libellés verbe + objet.

Responsive et performance perçue
- [ ] Points de rupture fondés sur le contenu ; requêtes de conteneur pour les composants réutilisés.
- [ ] Images dimensionnées (CLS < 0,1), image principale prioritaire, autres en chargement différé.
- [ ] `100dvh`, zones sûres, zoom non bloqué.

Back-office / e-commerce
- [ ] Tableaux : alignements, en-têtes collants, tri annoncé, états vide/erreur/chargement.
- [ ] Coût total visible avant le tunnel ; commande sans compte en premier ; ≤ 12–15 éléments de formulaire ; validation en ligne ; données conservées après erreur.

## 14. Anti-modèles et pièges

- Contraste calculé seulement en thème clair ; gris clair sur blanc pour les textes secondaires (souvent < 4,5:1).
- Remplacer les libellés de champs par des placeholders (disparition à la saisie, contraste faible).
- Menu hamburger comme unique navigation d'une appli mobile fréquente.
- Carrousels automatiques en page d'accueil (faible engagement, problèmes d'accessibilité : contrôle de pause obligatoire, WCAG 2.2.2).
- Copier l'interface iOS sur Android (ou l'inverse) : chevrons de retour, sélecteurs, feuilles incohérents avec la plateforme.
- Breakpoints par appareil (« iPhone 15 ») au lieu de points fondés sur le contenu.
- Modales en cascade, fenêtres surgissantes à l'arrivée, bannière cookies qui masque le focus.
- Boutons désactivés sans explication dans les formulaires.
- Frais révélés à la dernière étape ; création de compte imposée ; champs redondants (WCAG 3.3.7 : ne pas redemander une information déjà fournie dans le même processus).
- Squelettes de chargement qui ne correspondent pas à la mise en page finale (saut visuel).
- APCA présenté comme « la norme WCAG 3 ».

## 15. Sources

Consultées le 2026-11-03.
- W3C, WCAG 2.2 (version du 12 décembre 2024) : https://www.w3.org/TR/WCAG22/
- A. Roselli, « WCAG3 Contrast as of April 2026 » (statut d'APCA) : https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html
- Material Design 3, classes de largeur / points de rupture : https://m3.material.io/foundations/layout/breakpoints/window-size-classes
- Material Design 3, accessibilité et structure (cibles 48 dp, espacement 8 dp) : https://m3.material.io/foundations/designing/structure
- Material Design 3, mouvement (système physique) : https://m3.material.io/styles/motion/overview/how-it-works
- Apple HIG, Accessibilité (tailles de contrôles, Dynamic Type, Réduire les animations) : https://developer.apple.com/design/human-interface-guidelines/accessibility
- Apple HIG (index) : https://developer.apple.com/design/human-interface-guidelines/
- Baymard, Checkout Usability Report & Benchmark : https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark
- Baymard, Checkout flow UX optimization : https://baymard.com/blog/checkout-flow-ux-optimization
- Baymard, sujet « Checkout usability » : https://baymard.com/checkout-usability
- MDN, requêtes de conteneur : https://developer.mozilla.org/fr/docs/Web/CSS/CSS_containment/Container_queries
- MDN, `light-dark()` : https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/light-dark
