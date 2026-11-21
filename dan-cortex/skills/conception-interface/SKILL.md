---
name: conception-interface
description: "Direction visuelle d'une interface web ou mobile qui ne ressemble pas à un gabarit par défaut : sujet, palette, typographie, composition, mouvement, rédaction de l'interface, plan de design puis critique avant de coder. À utiliser pour « donne une identité visuelle », « ça fait générique », « choisis les polices et les couleurs », « refais le design de cette page », « conçois la page d'accueil »."
license: Apache-2.0 (texte complet dans LICENSE.txt)
---

# Conception d'interface — direction visuelle

Traduit et adapté de `frontend-design` (dépôt anthropics/skills, Apache-2.0, © Anthropic, PBC). Voir « Origine ». Complète `maquettes-parcours` (parcours, matrice, système de design) : ici, on choisit un parti pris visuel propre au sujet.

## Sommaire
1. Principes
2. Ancrer le design dans le sujet
3. Typographie et structure
4. Mouvement
5. Défauts à éviter
6. Processus : plan, revue, construction, critique
7. Rédiger dans l'interface
8. Contrôles avant de rendre
9. Origine

## 1. Principes

| Principe | Application |
|---|---|
| Une direction par brief | Le palette, la typographie et la composition répondent à ce brief, pas à tout brief similaire. |
| Le brief prime | Si le brief impose un style, le suivre à la lettre, même s'il ressemble à un défaut de la section 5. |
| Une seule audace | Une chose mémorable, le reste sobre ; retirer toute décoration qui ne sert pas le brief. |
| Socle de qualité sans l'annoncer | Adaptatif jusqu'au mobile, focus clavier visible, mouvement réduit respecté, contrastes, palette harmonieuse. |

## 2. Ancrer le design dans le sujet

- Si le brief ne dit pas quel est le produit, proposer un sujet concret, un public et la tâche principale de la page, puis les faire confirmer.
- Le secteur, les matières et le vocabulaire du sujet fournissent les choix distinctifs : un jouet pour enfants de 8 à 11 ans et un tableau de bord pour analystes financiers ne se ressemblent pas.
- Construire avec le vrai contenu du brief, pas avec du texte de remplissage générique.
- Pour une page web, l'accroche est ce qu'on voit d'abord : titre, image, animation, démonstration ou moment interactif, selon ce qui est le plus caractéristique du sujet. Le gros chiffre avec petit libellé, statistiques et dégradé est le traitement par défaut : ne le garder que s'il est le meilleur choix.

## 3. Typographie et structure

- La typographie porte la personnalité : une famille ou deux, clairement distinctes si deux ; pas les familles par défaut de tout projet.
- Échelle typographique explicite (graisses, largeurs, espacements) selon les usages classiques de la typographie ; titre utilisé comme élément actif du design.
- Lignes de moins de 80 caractères ; empattements : un peu plus de longueur de ligne et d'interligne admis.
- Éviter : un seul mot accentué dans un titre, libellés tout en capitales, étiquettes inutiles au-dessus du contenu.
- La structure (filets, bordures, numérotation, surtitres) porte de l'information : ne numéroter (01 / 02 / 03) que si le contenu est réellement une suite d'étapes.

## 4. Mouvement

| Type | Règle |
|---|---|
| Non déclenché par l'utilisateur | Rare et voulu : une séquence d'ouverture ou une révélation, pas des effets dispersés. Entrées « glisser et fondre » sur chaque section et survols sur chaque carte sont le défaut générique. |
| Répond à une action | Bienvenu s'il montre ce qui a changé (ouverture, déploiement, confirmation). |

Pour le détail des courbes, durées et règles : skill `mouvement-interface`.

## 5. Défauts à éviter (les signes d'une page générée)

1. Fond crème (proche #F4F1EA), titre serif à fort contraste, accent terre cuite (proche #D97757, accent de Claude lui-même, donc un signe sur un brief tiers).
2. Fond quasi noir et un seul accent vert acide ou vermillon.
3. Mise en page de journal : filets fins, angles nuls, colonnes denses.
4. Kit de cartes SaaS : cartes identiques, un seul rayon partout, même ombre grise douce, dégradés décoratifs.
5. Décor de gabarit : surtitre en capitales espacées au-dessus de chaque titre, chaînes de métadonnées séparées par des points médians, étiquettes « MOT — fragment », noir teinté, police à chasse fixe pour les petites données, « → » ajouté aux liens.

Ces choix sont légitimes pour certains briefs ; ils deviennent des défauts quand ils apparaissent quel que soit le sujet.

## 6. Processus : plan, revue, construction, critique

1. **Plan court** (jetons) : couleur (4 à 6 valeurs hexadécimales nommées), typographie et rôles, composition (une phrase par idée, schémas ASCII, alignement), principes propres à la page.
2. **Revue du plan contre le brief** : si une partie ressemble à ce qu'on produirait pour n'importe quelle page voisine, la réviser et dire ce qui a changé et pourquoi.
3. **Construction** : attention à la spécificité des sélecteurs CSS (un sélecteur de type et un sélecteur d'élément peuvent s'annuler, notamment pour les marges entre sections).
4. **Critique** : captures d'écran si l'environnement le permet ; retirer un « accessoire » avant de rendre ; noter ce qui a été essayé.

Décision de design à inscrire dans `03-conception/design/design-system.md` (jetons), pas dans le code seul.

## 7. Rédiger dans l'interface

Les mots servent à comprendre et à agir, pas à décorer. Détail du métier : `maquettes-parcours/references/contenu-localisation-culture.md`.

| Règle | Exemple |
|---|---|
| Point de vue de l'utilisateur, mots simples | « gérer les notifications », pas « configuration des webhooks » |
| Voix active, l'action garde son nom dans tout le parcours | bouton « Publier » → confirmation « Publié » |
| Libellé d'action précis | « Enregistrer les modifications », pas « Valider » |
| Erreur : cause et action, sans s'excuser ni rester vague | |
| État vide : une invitation à agir | |
| Ton conversationnel, majuscule de phrase, pas de remplissage | un élément écrit, un rôle |

## 8. Contrôles avant de rendre

- [ ] Le sujet, le public et la tâche principale sont énoncés et confirmés.
- [ ] Le plan a été comparé à la production « par défaut » et révisé au moins une fois.
- [ ] Aucun défaut de la section 5 gardé par habitude (seulement sur demande du brief).
- [ ] Une seule audace ; tout le reste est sobre.
- [ ] Mobile, focus clavier, mouvement réduit, contrastes vérifiés (`accessibilite.md`).
- [ ] Aucun compte à rebours ni stock fictif ; contenus fictifs signalés comme tels.
- [ ] Textes : verbes d'action précis, erreurs avec cause et action.

## 9. Origine

Texte traduit et adapté (forme B de `robustesse-agents/references/renfort-externe.md`, exception du 12/11/2026 pour les scripts ailleurs, sans objet ici : aucun script repris). Dépôt https://github.com/anthropics/skills, skill `frontend-design`, licence Apache-2.0 (`LICENSE.txt`), commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579`. Détail : `NOTICE.md`.
