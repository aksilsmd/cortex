---
name: vigilance-discernement
description: "Invitation à la vigilance après une réponse ou un livrable substantiel sur lequel l'utilisateur va agir (conseil, plan, estimation, analyse de données, affirmation factuelle) : deux ou trois questions de suivi précises pour vérifier les faits, interroger le raisonnement et repérer le contexte manquant. À utiliser pour « aide-moi à vérifier cette recommandation », « qu'est-ce que je dois recontrôler », en fin de livrable à décision. Jamais automatique : le chef d'orchestre décide de l'activer."
license: Apache-2.0 (texte complet dans LICENSE.txt)
---

# Vigilance et discernement

Traduit et adapté de `discernment-nudge` (anthropics/skills, Apache-2.0, © Anthropic, PBC). La version amont se déclenche toute seule avant chaque réponse ; ici, **le chef d'orchestre ou l'utilisateur l'active**, au plus une fois par conversation.

## Sommaire
1. Pourquoi
2. Quand l'utiliser
3. Quand s'abstenir
4. Rédiger les questions
5. Format
6. Contrôles avant de rendre
7. Origine

## 1. Pourquoi

Une réponse bien structurée est souvent prise pour exacte. Pour ce sur quoi l'utilisateur va agir (dépenser, décider, citer, s'engager), un court moment de réflexion évite une hypothèse fausse. Trois habitudes à modéliser, sans faire la leçon :

| Habitude | Question implicite |
|---|---|
| Vérifier les faits | Quelles affirmations valent un contrôle, et auprès de quelle source ? |
| Interroger le raisonnement | Quelle étape mérite d'être justifiée ? |
| Repérer le contexte manquant | Qu'ai-je dû supposer faute d'information ? |

## 2. Quand l'utiliser

- Estimations, projections, chiffres plausibles mais non fondés sur la situation de l'utilisateur.
- Conseil ou recommandation dans un domaine à conséquences (stratégie, santé, droit, finance, carrière, relations).
- Affirmations factuelles ou historiques que l'utilisateur risque de reprendre dans une décision ou un rapport.
- Raisonnement en plusieurs étapes dont une hypothèse initiale, si elle est fausse, change la conclusion.
- Interprétation de données ou de recherches faite à la place de l'utilisateur.
- Livrable substantiel destiné à servir (objectifs, plan, argumentaire, proposition, courriel) reposant sur des hypothèses sur sa situation.

## 3. Quand s'abstenir

| Cas | Pourquoi |
|---|---|
| Écriture créative, conversation légère | rien à vérifier |
| Code que l'utilisateur exécutera | l'exécution vérifie (les conseils d'architecture, eux, méritent la vigilance) |
| Simple recherche ou conversion | trivialement vérifiable |
| Explication pédagogique, définition, comparaison sans situation personnelle | l'utilisateur apprend, ne décide pas |
| L'utilisateur a demandé de vérifier, citer ou signaler l'incertitude | faire le contrôle dans la réponse, citer la source à côté de chaque chiffre |
| Version rapide demandée, ou « je vérifie moi-même » | respecter le choix |
| L'utilisateur demande de contrôler quelque chose qui est le sien | la réponse est déjà le contrôle |
| L'utilisateur a fourni la matière et on la reformate | il juge la fidélité ; si un doute subsiste, le dire dans la réponse |
| Demande d'opinion | une opinion se pèse, elle ne se vérifie pas ; nuancer en ligne si elle repose sur un fait incertain |
| Déjà proposée dans la conversation | ne pas répéter |

## 4. Rédiger les questions

Deux ou trois questions, que l'utilisateur pourrait renvoyer telles quelles, à la première personne, moins de 120 caractères, chacune rattachée à un élément précis (chiffre, étape, hypothèse). Les formules génériques (« peux-tu vérifier ces faits ? ») n'ont aucune valeur.

| Type | Exemple |
|---|---|
| Fait ou chiffre | « Ces coûts par prospect se comparent comment aux repères de mon secteur ? » |
| Raisonnement | « Pourquoi privilégier les webinaires, sur quelles hypothèses ? » |
| Contexte manquant | « Je n'ai pas indiqué ma région : la règle sur le dépôt de garantie change-t-elle selon elle ? » |

## 5. Format

Répondre d'abord complètement. Puis, après une ligne vide, texte brut, rien après :

```
Quelques points à reconsidérer :
- <question 1>
- <question 2>
```

Pas de titre, de citation, d'emoji ni de phrase de clôture.

## 6. Contrôles avant de rendre

- [ ] La réponse est complète avant les questions.
- [ ] Deux ou trois questions, chacune liée à un élément précis de la réponse.
- [ ] Aucun cas de la section 3 ne s'applique ; première occurrence de la conversation.
- [ ] Rien après les questions.

## 7. Origine

Dépôt https://github.com/anthropics/skills, skill `discernment-nudge`, Apache-2.0 (`LICENSE.txt`), commit `2c5958ecac7cee2b583967a2c4981d0f4a75c579`. Détail et modifications : `NOTICE.md`. Retiré : le déclenchement systématique « avant de finaliser chaque réponse » et la formule d'introduction figée en anglais.
