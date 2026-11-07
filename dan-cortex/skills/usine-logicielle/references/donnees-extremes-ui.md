# Données extrêmes : casser une interface avant l'utilisateur

Une interface conçue avec « Jean Martin, 12 membres » casse au premier vrai client. Méthode : relever chaque valeur affichée, lui opposer le pire cas **réaliste**, basculer entre démonstration et extrême, consigner chaque casse avec cause et correctif. Lecture à la demande : testeurs, recetteur, et développeurs avant de livrer une liste, une fiche ou une carte.

## 1. Deux erreurs à éviter

1. **Des données absurdes** (suite de « a », nom de 5 000 caractères) : « ça n'arrive jamais », et l'on cesse d'écouter. Chaque valeur est plausible, ou c'est la limite réelle du schéma.
2. **S'arrêter au texte long** : les casses livrées sont souvent le nom de deux lettres, l'avatar absent, « 1 membres », la liste vide, le badge traduit.

## 2. Ce que les règles du pôle imposent déjà

Rien de neuf à inventer : l'exercice applique des règles Dan-Cortex existantes.
- **Données fictives** (garde-fous de `usine-logicielle`) : le jeu extrême est inventé, avec des domaines réservés (`example.com`, `.test`) ; aucune donnée de production ni personne réelle.
- **Jeu de données stable avant capture** (`controle-visuel.md`) : le jeu extrême est une seconde fixture, chargée par le même mécanisme que celle des captures. Le composant n'est pas retouché pour provoquer une casse : ce serait tester la retouche.
- **Contrat avant intuition** (`tests-par-niveau.md`, `architecture-normes`) : chaque limite vient du schéma de validation, de la migration ou du contrat d'API. Une limite absente, ou différente entre saisie et stockage, est remontée à l'architecte : le pôle ne fixe pas seul un contrat.
- **Le PO tranche les choix de design** (`recette.md`) : couper ou tronquer un champ, afficher ou masquer un rôle vide sont proposés, pas décidés par le testeur.
- **Rien de non livrable en production** : la bascule entre jeux reste dans l'environnement de développement ou une route de prototype.

## 3. Relever la surface

Pour chaque valeur affichée : d'où elle vient, sa limite, si elle peut manquer. Sans oublier compteur d'en-tête, date relative, texte de badge, libellé venu des données, infobulle, avatar, et la **longueur de la liste**. Noter les désaccords : une saisie limitée à 50 caractères vers une colonne de 255 recevra un jour plus long, par import ou API.

## 4. Composer le jeu extrême

Une fixture de même forme que la démonstration, rangée à côté. Familles à couvrir (exemples à adapter au marché du projet) :

- **Noms** : très long et composé (« Lalla Fatma-Zohra Aït Ouaguenoun-Benmansour ») ; deux lettres (« Lu ») ; une seule ; particules et suffixe (« Jean-Baptiste de La Tour du Pin, fils ») ; initiale accentuée (« Émeline Œhlschläger ») ; diacritiques empilés du vietnamien ; écriture arabe (« عبد القادر بن علي ») et tifinagh ; CJK sans espace ; tout en minuscules ; espaces en trop au début, au milieu, à la fin ; émoji en tête, et émoji composé (personne avec teinte et métier) saisi directement dans la fixture ; nom absent, seulement un courriel.
- **Identifiants insécables** : courriel très long sur sous-domaine (`marie-claire.vandenbroucke@direction-regionale.exemple-holding.example.com`), le plus court possible (`a@b.fr`), adresse avec `+`, URL longue à paramètres, UUID, nom de fichier où la fin compte (`Devis-client-v14-DEFINITIF-signe.pdf`), pseudonyme d'un caractère ou de quarante.
- **Libellés venus des données** : intitulé de poste sur trois lignes, statut long en badge, mot composé allemand, traduction plus longue d'un tiers, quinze étiquettes, étiquette plus large que son conteneur, titre vide, saut de ligne dans un champ d'une ligne, balise HTML à afficher telle quelle, description de 2 000 caractères.
- **Nombres et montants** : 0, 1, 1284 (séparateur de milliers), un million, montant à huit chiffres, négatif, flottant mal arrondi, pourcentage hors bornes (130 %, −5 %), `null`, `NaN`, format régional (`1 284,50 DZD` et `1,284.50`), valeur qui change en direct (99 → 100).
- **Collections** : vide ; un élément ; taille de page exacte, et un de plus ; plus de 1 000 sans pagination ; un élément dix fois plus grand ; homonymes.
- **Temps** : à l'instant ; il y a 12 jours, 11 mois, 3 ans (date absolue au-delà d'une semaine environ) ; date future ; horodatage zéro ; soirée qui change de jour selon le fuseau ; très longue durée. `Intl.RelativeTimeFormat` et `Intl.DateTimeFormat`.
- **Images** : URL d'avatar en erreur, pas d'avatar, panorama très large, image très haute, logo transparent ou sombre sur fond sombre, image lente.
- **États** : chargement, erreur d'API, données partielles dans une même liste, tous les statuts à la fois, absence de droit, l'utilisateur courant dans la liste.

Cas hors jeu unique, à ne pas sauter : **vide**, **un**, **énorme** (positions supplémentaires de la bascule ou fixtures dédiées).

## 5. Brancher la bascule

Commande segmentée « Démo / Extrême / Vide / Un / 1 000 lignes », sobre, sans animation du contenu ; choix porté par un paramètre d'URL (`?donnees=extreme`) ou une route de prototype, ou, pour un composant isolé, un fichier HTML autonome.

## 6. Regarder : largeurs et environnements

Avec le jeu extrême, vérifier :
- à la **largeur réelle du conteneur** (une liste de barre latérale n'est pas une liste pleine page), puis 320 px, puis les largeurs de `controle-visuel.md` (390, 768, 1440) et la plus large prise en charge ;
- zoom à **200 %** (le texte grandit, les boîtes non) ;
- **sombre** et **RTL** (`dir="rtl"` sur un conteneur, contenu arabe réel) ;
- **tactile** : une action qui n'apparaît qu'au survol est inaccessible.

Captures des deux jeux à chaque largeur si l'outillage le permet (`formation-playwright-mcp.md`) ; sinon, distinguer le vu du déduit.

## 7. Causes habituelles et correctifs

- **Boîtes flexibles** : une boîte de taille fixe (avatar, icône, badge, action en fin de ligne) prend `flex-shrink: 0` ; la colonne de texte prend `min-width: 0` (`minmax(0, 1fr)` en grille) pour pouvoir rétrécir ; un badge qui doit rester sur une ligne prend `white-space: nowrap`, et l'on décide qui cède. Texte sur plusieurs lignes : aligner en haut.
- **Chaînes sans point de coupure** (courriel, URL, mot composé) : `overflow-wrap: anywhere`, qui ne coupe qu'au besoin, plutôt que `word-break: break-all`.
- **Dimensions figées** : hauteur fixe → défilement visible ou fondu ; bouton à largeur fixe → largeur au contenu avec `min-width` ; interligne serré et `overflow: hidden` qui rognent les diacritiques → desserrer.
- **Texte fabriqué en dur** : pluriels par `Intl.PluralRules` (six formes en arabe) ; nombres par `Intl.NumberFormat`, avec garde contre `null` et `NaN` ; `tabular-nums` pour les chiffres qui changent ; initiales par graphèmes (`Intl.Segmenter`), premier et dernier mot, icône de repli.
- **Replis absents** : champ facultatif vide → ligne omise ou hauteur réservée exprès ; image en erreur → initiales et `object-fit: cover` ; texte tronqué → valeur complète accessible (infobulle, fiche).
- **Volume** : au-delà de quelques centaines de lignes, virtualiser ou paginer.
- **Échappement** : balises ou entités visibles → échapper une fois, au rendu ; aucune injection HTML de données utilisateur.

## 8. Tronquer, couper ou limiter

Choix par champ, jamais global :
- **Passer à la ligne** pour ce qui identifie (nom, titre en fiche) ; deux lignes conviennent, quatre signalent une colonne trop étroite.
- **Tronquer à la fin** pour les métadonnées dont le début porte le sens (rôle, aperçu de message), avec accès à la valeur complète.
- **Tronquer au milieu** quand les éléments diffèrent par la fin (fichiers, courriels d'un même domaine, chemins, empreintes).
- **Limiter à n lignes** (`line-clamp`) pour les aperçus de cartes.
- **Jamais tronquer** un nombre, un montant, une date, ce qu'on compare.
- En RTL, la troncature et l'ellipse se placent du côté logique de fin.

## 9. Constats et suite

Chaque casse devient un constat au format de `controle-visuel.md` : identifiant de règle (le contrôle `VIS-` concerné, ou la règle `HIG-` de `design-apple`), écran `EC-`, largeur et environnement (zoom, thème, langue), capture nommée selon la convention de capture, champ et valeur extrême en cause, correctif proposé avec `fichier:ligne`, et gravité **C/H/M** : C = bloquant (contenu illisible, action inaccessible, donnée fausse), H = majeur (lisible mais visiblement faux), M = mineur, y compris le fragile (pas de limite, pas de repli). Les constats C et H entrent au registre d'anomalies selon `recette.md` ; les choix de design vont au PO.

Après correction, repasser **tous** les états, démonstration comprise. La fixture extrême reste au dépôt comme test de non-régression.

## 10. Contrôles avant de rendre

- [ ] Chaque valeur affichée relevée, avec sa limite ou « non bornée ».
- [ ] Jeu extrême plausible, entré par la frontière des données, sans donnée réelle.
- [ ] Vide, un, énorme essayés.
- [ ] Largeurs, zoom 200 %, sombre, RTL et tactile vérifiés, ou mention « déduit ».
- [ ] Chaque casse : constat avec règle, écran, largeur, capture, gravité C/H/M.
- [ ] Animations éventuelles : `mouvement-interface/references/audit-du-mouvement.md`.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié ni exemple repris, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/break-ui/SKILL.md`, `skills/break-ui/CATALOG.md`. Exclus : « Initial Response », persona, sous-commandes, émoji composé du catalogue (aucun caractère invisible repris). Fiche : `references/sources/renfort-github.md`.
