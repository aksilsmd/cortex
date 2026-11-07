---
name: mouvement-interface
description: "Mouvement des interfaces web et mobiles : décider s'il faut animer, construire une animation (outil, propriétés, courbe, durée, ressort), chorégraphier plusieurs éléments, rendre un geste fluide (interruption, vitesse, inertie, élastique), corriger les saccades, nommer un effet, puis réviser, compléter ou alléger le mouvement existant (règles MV-n.m). À utiliser pour « animation », « transition », « micro-interaction », « ça saccade », « trop d'animations », « effet de ressort », revue du mouvement."
---

# Mouvement d'interface

Le mouvement sert l'utilisateur ou disparaît. Il confirme une action, montre d'où vient et où va un élément, rend un changement d'état lisible, évite une téléportation. Il ne retarde jamais une action fréquente et ne bouge pas les données qu'on lit. Règle d'or : **dans le doute, ne pas animer ; si l'on anime, court, interruptible, respectueux du mouvement réduit et du sens de lecture.**

## Principes

1. **La fréquence décide.** Action clavier ou répétée des centaines de fois : rien. Dizaines de fois : à peine perceptible. Occasionnel : animation standard. Rare : place de l'agrément.
2. **Une raison nommée** pour chaque animation, ou pas d'animation.
3. **Le moins coûteux d'abord** : transition CSS, `@starting-style`, animation CSS, Web Animations API ; une bibliothèque seulement si le besoin l'exige (ressort, mise en page, geste), en option inscrite à l'ADR avec sa licence et son poids.
4. **`transform` et `opacity`**, sortie douce forte, moins de 300 ms pour l'interface courante ; ressort dès qu'un doigt est en jeu.
5. **Accessibilité et RTL livrés avec l'animation** : `prefers-reduced-motion` (moins et plus doux, pas zéro), survol réservé au pointeur fin, focus jamais retardé, sens horizontaux inversés en RTL.

## Ordre des décisions

1. Faut-il animer ? (fréquence, raison, fonction)
2. Un seul élément ou plusieurs ? (construction ou chorégraphie)
3. Un geste est-il en jeu ? (manipulation directe, ressort, vitesse)
4. Le rendu tient-il le budget d'image ? (performance)
5. Revue avant fusion (grille `MV-`).

## Références (à charger à la demande)

| Fichier | Quand |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/construire-une-animation.md` | écrire ou modifier une animation : filtre, outil, propriétés, courbes, durées, ressorts, fiches par composant |
| `${CLAUDE_SKILL_DIR}/references/choregraphie.md` | plusieurs éléments bougent sur un même événement : rôles, relations, cascade, séquence, sens, interruption |
| `${CLAUDE_SKILL_DIR}/references/mouvement-fluide-apple.md` | gestes, feuilles, carrousels : réponse immédiate, interruptibilité, ressorts, passage de vitesse, projection d'inertie, élastique, matières, retours multimodaux |
| `${CLAUDE_SKILL_DIR}/references/performance-animation.md` | animation qui saccade, choix d'une propriété, arbitrage CSS ou JS, `will-change` |
| `${CLAUDE_SKILL_DIR}/references/vocabulaire-du-mouvement.md` | nommer un effet décrit vaguement, rédiger une exigence ou une anomalie |
| `${CLAUDE_SKILL_DIR}/references/audit-du-mouvement.md` | revue d'une différence, audit d'un code entier, mouvements manquants, mouvements à retirer (règles `MV-n.m`) |

Mobile natif : `usine-logicielle/references/mobile-react-native-animation.md`. Bases du design : `design-apple` ; formation : `maquettes-parcours/references/formation-animation-motion.md`.

## Usage par agent

- `maquettiste`, `concepteur-ux` : fixent les jetons de mouvement (courbes, durées) et annotent dans la matrice d'interactions le mouvement attendu de chaque `EL-`, avec le terme du vocabulaire.
- `developpeur-frontend`, `developpeur-mobile` : construisent selon les références ; aucune dépendance de mouvement sans ADR.
- `testeur-visuel`, `testeur-web`, `testeur-mobile`, `expert-accessibilite` : vérifient avec la grille `MV-` et citent l'identifiant dans chaque constat ; un constat de gravité C bloque la fusion, comme pour les règles `HIG-`. Le ressenti se juge sur appareil réel, enregistrement relu image par image.

## Origine

Méthodes reformulées en français (forme A de `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski). Commit et fichiers lus : `references/sources/renfort-github.md`.
