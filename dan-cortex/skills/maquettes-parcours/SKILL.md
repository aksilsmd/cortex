---
name: maquettes-parcours
description: >
  Pôle Design de Dan-Cortex : workflow schématisé de chaque fonctionnalité, matrice d'interactions (chaque écran,
  bouton, clic, réaction, destination), maquettes, thème, accessibilité, localisation. À utiliser pour des
  maquettes, wireframes, parcours utilisateur, « où mène chaque bouton », carte de navigation, design system,
  choix d'un thème.
---

# Maquettes et parcours — pôle Design

Ce pôle transforme des exigences en une interface que l'on peut construire et tester sans rien deviner. Sa règle
d'or : **un développeur ou un testeur ne doit jamais avoir à inventer ce qui se passe après un clic.**

## Principes

1. **Le parcours avant l'écran.** On dessine d'abord ce que la personne cherche à accomplir, étape par étape,
   puis les écrans qui le permettent. Une maquette sans workflow est une image.
2. **Tout élément interactif a quatre réponses :** qui peut l'actionner et quand ; ce que fait le système ; où
   l'on arrive ; ce qui se passe quand ça échoue.
3. **Tout écran de données a ses états :** vide, chargement, erreur, succès, et selon le cas partiel, hors-ligne,
   non autorisé. Un état non dessiné sera improvisé en production.
4. **L'exhaustivité se vérifie par script.** La matrice d'interactions suit un format que `cortex.py` contrôle :
   aucun cul-de-sac, aucun écran orphelin, aucune destination indéfinie.
5. **L'accessibilité et la langue se conçoivent, elles ne se rattrapent pas.** Contrastes, navigation au
   clavier, textes de remplacement, longueur des libellés traduits, sens de lecture sont des contraintes de
   départ.
6. **Le thème découle de la marque et de la cible,** pas du goût du jour : on le choisit sur critères, on le
   documente en jetons de design.

## Méthode

1. **Comprendre** : personas et parcours cibles à partir du cahier des charges et de la voix du client
   (`references/recherche-utilisateur.md`).
2. **Modéliser les workflows** : un workflow `WF-` par fonctionnalité, avec déclencheur, étapes, règles,
   exceptions et schéma (`references/workflows-fonctionnels.md`).
3. **Inventorier les écrans** : chaque écran `EC-`, son type, ses rôles, ses états
   (`references/matrice-interactions.md`).
4. **Décrire chaque interaction** : chaque élément `EL-` avec action, conditions, réaction, destination,
   erreurs, workflow de rattachement (même référence).
5. **Vérifier** : `cortex.py interactions verifier`, puis `cortex.py interactions graphe` pour la carte de
   navigation. Corriger jusqu'à zéro erreur.
6. **Maquetter** : filaire pour tous les écrans, haute fidélité pour les écrans clés
   (`references/maquettes.md`).
7. **Fixer le thème et le système de design** (`references/theme-design-system.md`).
8. **Contrôler l'accessibilité** (`references/accessibilite.md`) et **adapter contenus, langues et cultures**
   (`references/contenu-localisation-culture.md`).

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Personas et parcours | `02-cadrage/personas-parcours.md` | |
| Workflows par fonctionnalité | `03-conception/design/workflows/<module>.md` | `WF-` |
| Inventaire des écrans | `03-conception/design/interactions/ecrans.md` | `EC-` |
| Matrice d'interactions | `03-conception/design/interactions/<module>.md` | `EL-` |
| Carte de navigation | `03-conception/design/interactions/navigation.md` (générée) | |
| Maquettes | `03-conception/design/maquettes/` | nommées par `EC-` |
| Système de design et thème | `03-conception/design/design-system.md` | |
| Exigences et audit d'accessibilité | `03-conception/design/accessibilite.md`, `05-validation/rapport-accessibilite.md` | |
| Contenus et localisation | `03-conception/design/contenu-localisation.md` | |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/workflows-fonctionnels.md` | avant de modéliser un workflow |
| `${CLAUDE_SKILL_DIR}/references/matrice-interactions.md` | avant d'inventorier les écrans ou de décrire des interactions : le format est imposé |
| `${CLAUDE_SKILL_DIR}/references/recherche-utilisateur.md` | pour les personas, les parcours, l'architecture de l'information |
| `${CLAUDE_SKILL_DIR}/references/maquettes.md` | avant de produire des maquettes |
| `${CLAUDE_SKILL_DIR}/references/theme-design-system.md` | pour choisir un thème et écrire le système de design |
| `${CLAUDE_SKILL_DIR}/references/accessibilite.md` | pour les exigences et l'audit d'accessibilité |
| `${CLAUDE_SKILL_DIR}/references/contenu-localisation-culture.md` | pour la microcopie, la traduction, l'adaptation culturelle |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

## Garde-fous

- Ne jamais présenter une maquette comme validée par des utilisateurs si elle ne l'a pas été : écrire
  « hypothèse de conception ».
- Pas d'interface trompeuse : refuser aussi simple qu'accepter, se désabonner aussi simple que s'abonner, aucun
  compte à rebours ou stock fictif.
- Les maquettes n'utilisent que des contenus fictifs clairement identifiables ou des contenus fournis par
  l'utilisateur ; jamais la marque ou l'identité visuelle d'un tiers.
