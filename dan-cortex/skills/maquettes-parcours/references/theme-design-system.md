# Thème, jetons de design et système de design

Ce fichier explique comment choisir un thème sur critères, le présenter à l'utilisateur, puis le fixer en jetons, composants et règles. Livrable : `03-conception/design/design-system.md` et `maquettes/jetons.css`.

## Sommaire
1. Choisir le thème
2. Présenter deux ou trois directions
3. Jetons de design
4. Composants
5. Mode sombre
6. Gabarit de `design-system.md`
7. Pièges et contrôles avant de rendre

## 1. Choisir le thème

Le thème découle de quatre entrées, dans cet ordre. Un thème choisi « parce qu'il est à la mode » vieillit avec la mode.

| Entrée | Question | Effet sur le choix |
|---|---|---|
| Marque | 3 à 5 attributs et leurs contraires (sobre, pas ostentatoire) | ton, forme, typographie, couleur d'accent |
| Cible | âge, compétences, appareils, contexte, handicaps | taille du texte, densité, tailles de cibles, contrastes |
| Secteur | conventions et confiance attendues | familiarité des composants |
| Culture et marché | langues, sens de lecture, symboles | police multi-écritures, miroir, couleurs |

Cadrage par type de projet (hypothèse de départ, à confirmer) :

| Projet | Orientation |
|---|---|
| Site d'administration ou de service public | système de design imposé ou recommandé : DSFR en France (obligatoire pour les sites de l'État, circulaire 6411-SG), GOV.UK au Royaume-Uni ; vérifier le périmètre d'application avec le juriste |
| SaaS, ERP | densité maîtrisée, sobriété, mode sombre, tableaux et filtres soignés |
| E-commerce | confiance, photographie, clarté du prix et du paiement |
| Mobile | conventions de la plateforme (Material 3 sur Android, Human Interface Guidelines sur iOS) plus jetons de marque |
| Site de grande entreprise | identité forte, performance, multilingue |

Repères d'état : octobre 2026. Material 3 Expressive (couleur, forme, taille, mouvement, contenant). Apple : Liquid Glass introduit en juin 2025 ; sa variante translucide peut gêner la lisibilité, la tester. GOV.UK Frontend 6.0.0 (9 février 2026). Les systèmes publics restent sobres et normatifs. Version courante du DSFR : à vérifier.

Si une marque existe : reprendre ses couleurs et sa typographie, vérifier leurs contrastes, proposer des correctifs plutôt que les imposer. Si elle n'existe pas : décision de type 1 (création d'identité).

## 2. Présenter deux ou trois directions

Méthode : benchmark de 8 à 12 références (directes, adjacentes, hors secteur) → planche → 2 ou 3 pistes appliquées à **trois écrans identiques** (accueil, liste, formulaire) → choix de l'utilisateur → verrouillage en jetons.

Chaque direction est présentée dans un même format, pour être comparable : nom, attributs de marque servis, palette (valeurs et contrastes), typographie, forme, densité, ton des textes, risque, coût d'implémentation, trois maquettes HTML. Recommander une direction avec ses motifs, ne pas laisser l'utilisateur sans avis. Consigner la décision : `registre decisions ajouter` (type 1 si une marque se crée, sinon type 2).

Idéalement, tester la préférence et la compréhension auprès de 5 utilisateurs de la cible ; sans test, écrire « hypothèse de conception ».

## 3. Jetons de design

Source de vérité : un JSON versionné dans le dépôt au format **Design Tokens Format Module 2025.10** (DTCG). Attention : c'est un rapport final de Community Group (28 octobre 2025), pas une Recommandation W3C. Pourquoi JSON : Figma, Penpot, Style Dictionary et le code s'y rattachent ; un jeton enfermé dans un outil se perd.

Trois couches :

| Couche | Rôle | Exemple de nom |
|---|---|---|
| Primitifs | valeurs brutes | `couleur.bleu.600` |
| Sémantiques | intention, alias des primitifs | `couleur.action.fond`, `couleur.texte.erreur` |
| Composants | usage précis, alias des sémantiques | `bouton.principal.fond` |

Propriétés DTCG : `$value`, `$type`, `$description`, `$extensions`, `$deprecated`. Types : color, dimension, fontFamily, fontWeight, duration, cubicBezier, number ; composites : border, shadow, transition, typography, gradient, strokeStyle. Alias : `{couleur.bleu.600}`. Fichiers `.tokens.json`.

```json
{
  "couleur": {
    "bleu": { "600": { "$type": "color", "$value": "#1f4e9c" } },
    "action": { "fond": { "$type": "color", "$value": "{couleur.bleu.600}", "$description": "Fond du bouton principal" } }
  }
}
```

Valeurs à fixer : échelle typographique, espacements (une base), rayons, ombres, durées de mouvement, points de rupture (360, 768, 1280 px comme point de départ), taille minimale des cibles tactiles (24×24 px CSS au minimum WCAG 2.2, viser 44 px). Chaque paire texte/fond est calculée : 4,5:1 pour le texte courant, 3:1 pour le texte large et les composants graphiques.

## 4. Composants

Pour chaque composant : usage et non-usage, variantes, **états** (défaut, survol, focus, actif, désactivé, erreur, chargement), comportement clavier, exigences d'accessibilité, contenu (longueur maximale, extrême traduction), jetons utilisés. Liste minimale : bouton, lien, champ et étiquette, case et bouton radio, liste déroulante, message d'erreur et résumé d'erreurs, modale, panneau, onglets, tableau, pagination, navigation, fil d'Ariane, notification, bandeau de consentement, état vide, indicateur de chargement. Chaque composant utilisé dans la matrice (`Type` des `EL-`) existe dans cette liste ; sinon le créer.

Le focus visible a un jeton propre. Le mouvement respecte `prefers-reduced-motion`.

## 5. Mode sombre

Thème sémantique, jamais une inversion : un second jeu d'alias vers d'autres primitifs. Contrastes recalculés dans chaque thème ; images, ombres et focus testés. Respecter `prefers-color-scheme` et offrir un choix manuel mémorisé.

## 6. Gabarit de `design-system.md`

````markdown
# Système de design — <projet>

## Synthèse
<direction retenue et décision (DEC-), source des jetons, nombre de jetons et de composants, contrastes vérifiés (oui/non, dans les deux thèmes), thèmes, hypothèses non testées>

## Direction artistique
Attributs de marque, directions écartées et motifs.

## Jetons
Chemin du JSON (`maquettes/jetons.tokens.json`), tableau des couleurs avec contrastes, typographie, espacements, rayons, mouvement.

## Thèmes
Clair, sombre, haut contraste éventuel, correspondances d'alias.

## Composants
| Composant | Variantes | États | Clavier | Jetons | Utilisé par (EL-) |
|---|---|---|---|---|---|

## Règles d'usage
Mise en page, grille, densité, images, icônes (avec texte), ton rédactionnel.

## Langues et sens de lecture
Polices par écriture, propriétés logiques, icônes à refléter.
````

## 7. Pièges et contrôles avant de rendre

- Palette de marque non vérifiée en contraste ; couleur seule porteuse de sens ; icône sans libellé.
- Tendance visuelle (verre, animations riches) qui dégrade lisibilité et sobriété.
- Jetons seulement dans l'outil de design ; mode sombre par inversion.
- Contrôles : deux ou trois directions comparées sur trois écrans identiques ; décision tracée ; tous les états de chaque composant ; contrastes chiffrés ; JSON conforme à DTCG.

## Sources
- Design Tokens Format Module 2025.10 : https://www.designtokens.org/tr/2025.10/format/
- DSFR : https://www.systeme-de-design.gouv.fr/ (périmètre : circulaire 6411-SG).
- GOV.UK Frontend v6.0.0 : https://github.com/alphagov/govuk-frontend/releases
- Material 3 Expressive : https://design.google/library/expressive-material-design-google-research
- Apple Human Interface Guidelines, Materials : https://developer.apple.com/design/human-interface-guidelines/materials
- WCAG 2.2, critères 1.4.3, 1.4.11, 2.5.8 (W3C).
