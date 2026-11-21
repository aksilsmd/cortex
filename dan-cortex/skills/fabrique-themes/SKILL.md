---
name: fabrique-themes
description: "Habillage cohérent d'un livrable (présentation, document, rapport, page HTML) avec un thème de couleurs et de polices : dix thèmes prêts à l'emploi et création d'un thème sur mesure. À utiliser pour « applique un thème à ce diaporama », « propose des palettes et des polices », « habille ce rapport », « crée un thème pour ce document »."
license: Apache-2.0 (texte complet dans LICENSE.txt)
---

# Fabrique de thèmes

Traduit et adapté de `theme-factory` (anthropics/skills, Apache-2.0, © Anthropic, PBC). Le PDF de présentation des thèmes n'est pas repris. Pour un thème de produit logiciel lié à une marque, passer plutôt par `maquettes-parcours/references/theme-design-system.md` : ici, on habille un livrable.

## Sommaire
1. Contenu d'un thème
2. Les dix thèmes
3. Méthode
4. Créer un thème sur mesure
5. Contrôles avant de rendre
6. Origine

## 1. Contenu d'un thème

Une palette cohérente avec codes hexadécimaux, un couple de polices (titres, texte) et une identité visuelle adaptée à des contextes et publics. Les polices sont celles **installées sur la machine ou fournies par l'utilisateur, sous licence lue** ; si une police nommée manque, choisir une police de repli de la même famille et le dire.

## 2. Les dix thèmes

| Thème | Caractère | Fichier |
|---|---|---|
| Profondeurs océaniques | maritime, professionnel et calme | `${CLAUDE_SKILL_DIR}/themes/ocean-depths.md` |
| Boulevard au couchant | couleurs de coucher de soleil, chaudes et vives | `${CLAUDE_SKILL_DIR}/themes/sunset-boulevard.md` |
| Canopée | tons de terre, naturel et ancré | `${CLAUDE_SKILL_DIR}/themes/forest-canopy.md` |
| Minimalisme moderne | gris contemporains, épuré | `${CLAUDE_SKILL_DIR}/themes/modern-minimalist.md` |
| Heure dorée | palette automnale riche et chaude | `${CLAUDE_SKILL_DIR}/themes/golden-hour.md` |
| Givre arctique | froid, net, hivernal | `${CLAUDE_SKILL_DIR}/themes/arctic-frost.md` |
| Rose du désert | tons poudrés, doux et raffinés | `${CLAUDE_SKILL_DIR}/themes/desert-rose.md` |
| Innovation technologique | audacieux, contrasté, moderne | `${CLAUDE_SKILL_DIR}/themes/tech-innovation.md` |
| Jardin botanique | couleurs fraîches et organiques | `${CLAUDE_SKILL_DIR}/themes/botanical-garden.md` |
| Galaxie de minuit | dramatique, tons profonds cosmiques | `${CLAUDE_SKILL_DIR}/themes/midnight-galaxy.md` |

## 3. Méthode

1. Présenter les thèmes à l'utilisateur sous forme de tableau (nom, caractère, échantillons de couleurs en valeurs hexadécimales) et le public du livrable.
2. Lui demander son choix et attendre une confirmation explicite.
3. Lire le fichier du thème retenu et appliquer partout ses couleurs et polices.
4. Vérifier contraste et lisibilité (`maquettes-parcours/references/accessibilite.md`), puis garder l'identité du thème sur toutes les pages ou diapositives.

## 4. Créer un thème sur mesure

Quand aucun thème ne convient : à partir des indications données (marque, public, ton), produire un thème sur le modèle des dix autres, avec un nom qui décrit ce que les couleurs et polices évoquent. Le montrer, le faire valider, puis l'appliquer. Un thème de marque d'un tiers n'est jamais imité sans autorisation de l'utilisateur.

## 5. Contrôles avant de rendre

- [ ] Choix du thème confirmé par l'utilisateur.
- [ ] Contrastes texte/fond suffisants, y compris texte clair sur fond foncé.
- [ ] Polices disponibles sur la machine ou fournies, licence lue ; repli signalé.
- [ ] Même thème sur tout le livrable.
- [ ] Le thème relève d'un goût ou d'un public, pas d'une marque : à valider avec le client.

## 6. Origine

Dépôt https://github.com/anthropics/skills, skill `theme-factory` (hors PDF), Apache-2.0 (`LICENSE.txt`), commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579`. Détail : `NOTICE.md`.
