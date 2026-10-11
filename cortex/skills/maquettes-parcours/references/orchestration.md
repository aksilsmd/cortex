# Orchestration du pôle Design

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `concepteur-ux` | B | J2, dès que la cible est connue |
| `cartographe-interactions` | B | J3, vague 3A pour les workflows et l'inventaire, vague 3B en essaim par module pour la matrice |
| `maquettiste` | B | J3, vague 3A en filaire, vague 3B en haute fidélité |
| `expert-accessibilite` | B | J3 pour les exigences, J5 pour l'audit |
| `redacteur-contenu-localisation` | B | J3, vague 3B ; plus tôt si plusieurs langues ou marchés |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J2, 2A | `concepteur-ux` : personas et parcours cibles | fiche projet, voix du client, note d'opportunité | `02-cadrage/personas-parcours.md` |
| J3, 3A | `cartographe-interactions` : workflows de toutes les fonctions et inventaire des écrans ; `maquettiste` : maquettes filaires des parcours principaux, proposition de thème ; `expert-accessibilite` : exigences | cahier des charges, personas, SFG en cours | `design/workflows/`, `design/interactions/ecrans.md`, `design/maquettes/`, `design/design-system.md`, `design/accessibilite.md` |
| J3, 3B | `cartographe-interactions` en essaim, une instance par module : matrice d'interactions ; `maquettiste` : haute fidélité des écrans clés ; `redacteur-contenu-localisation` | SFD du module, workflows, inventaire des écrans | `design/interactions/<module>.md`, maquettes, `design/contenu-localisation.md` |
| J5, 5A | `expert-accessibilite` : audit sur le produit construit | produit en recette, exigences | `05-validation/rapport-accessibilite.md` |

Après la vague 3B, lancer toi-même, sans agent :
`cortex.py interactions verifier`, `cortex.py interactions graphe`, `cortex.py tracabilite verifier`. Renvoyer
chaque erreur à l'instance qui a écrit le module, en la reprenant.

## Essaimage

- **Matrice d'interactions :** une instance de `cartographe-interactions` par module de la SFD. Donner à chacune
  l'inventaire des écrans complet (pour les destinations hors de son module), la plage d'écrans dont elle est
  propriétaire, et la SFD de son seul module. Le module `commun` (en-tête, menu, pied de page, consentement) va à
  une seule instance.
- **Maquettes :** une instance de `maquettiste` par parcours si plus de quinze écrans, toutes avec le même
  `design-system.md` en entrée, écrit avant.
- **Localisation :** une instance par langue ou par marché au-delà de deux.

## Dépendances à respecter

L'inventaire des écrans précède la matrice. Le système de design précède la haute fidélité. La SFD d'un module
précède sa matrice ; si elle n'existe pas encore, lancer `redacteur-sfd` et `cartographe-interactions` en binôme
sur le même module, chacun recevant le chemin du livrable de l'autre.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Workflows et matrice | `redacteur-sfd`, `expert-accessibilite`, `concepteur-tests` |
| Maquettes et système de design | `concepteur-ux`, `expert-accessibilite`, `developpeur-frontend`, `stratege-marketing` |
| Contenus et localisation | `juriste-numerique` pour les mentions et promesses, `stratege-marketing` pour le ton |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Thème et direction artistique | 1 si une marque se crée, sinon 2 | présenter deux ou trois directions à l'utilisateur |
| Navigation principale et architecture de l'information | 2 | panel |
| Niveau d'accessibilité visé | 1 quand une obligation légale s'applique | comité de cadrage |
| Langues et marchés de la première version | 1 | comité de cadrage |

## Sortie du pôle par jalon

- **J2 :** `personas-parcours.md` présent.
- **J3 :** workflows, inventaire, matrice et maquettes présents ; `interactions verifier` sans erreur ;
  contrôles `UXD-`, `ACC-`, `LOC-` de jalon J3 traités.
- **J5 :** rapport d'accessibilité présent, contrôles `ACC-` de jalon J5 traités.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | un seul `cartographe-interactions` fait workflows, inventaire, matrice et maquettes filaires du parcours principal ; accessibilité contrôlée par un `verificateur` avec la liste `ACC-` |
| `standard` | comme décrit |
| `integral` | maquettes haute fidélité de tous les écrans ; prototype cliquable ; test d'utilisabilité proposé à l'utilisateur ; audit d'accessibilité complet sur échantillon représentatif |

## Outils extérieurs

Si un connecteur de maquettage ou le type Design de l'application est disponible, tu peux y porter les maquettes
à partir du cahier produit par le `maquettiste` (écrans, composants, jetons). Sinon le `maquettiste` écrit des
maquettes HTML ou SVG autonomes dans `design/maquettes/`.
