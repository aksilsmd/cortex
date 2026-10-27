---
name: audit-general
description: >
  Audit général Dan-Cortex : un super-auditeur indépendant passe le projet en revue à 360°, son rapport est débattu
  en plénière, puis les corrections sont décidées et recontrôlées. À utiliser avant un lancement, à un jalon, ou
  pour « audite mon projet », « vérifie que rien n'est oublié », « revue complète », même hors Dan-Cortex.
---

# Audit général

L'audit répond à une seule question : **peut-on se fier à ce qui a été produit ?** Il est fait par un agent qui
n'a rien produit, parce qu'un auteur ne voit pas ses propres angles morts. Son rapport n'est pas un verdict : il
est soumis à ceux qu'il vise, débattu, puis tranché.

## Les trois niveaux

| Niveau | Quand | Profondeur |
|---|---|---|
| Audit de jalon | fin de J3, et à tout jalon en mode `integral` | contrôles mécaniques, synthèses, 3 à 5 documents lus en entier |
| Audit général | J5, avant le go/no-go | tout ce qui suit |
| Audit de clôture | J7 | écarts entre prévu et réel, constats restés ouverts, enseignements |

En mode `eclair`, l'audit général garde les étapes 1, 2 et 5 et lit en entier les trois documents les plus
risqués.

## Déroulé

1. **Lancer un `auditeur-general` au contexte neuf.** Ne jamais reprendre un agent qui a produit un livrable.
   Ordre de mission : dossier du projet, jalon, niveau d'audit, chemin du rapport
   (`00-pilotage/audits/audit-general.md` ou `audit-<Jn>.md`).
2. **L'auditeur instruit** selon la méthode ci-dessous et enregistre chaque constat au registre.
3. **Diffuser.** Regrouper les constats par pôle responsable (`cortex.py registre constats liste --ouverts`).
4. **Plénière d'audit.** Suivre le skill `reunion-decision`, réunion type « plénière d'audit » :
   - tour 1, en parallèle : chaque pôle visé répond à chacun de ses constats, par écrit : *accepté* avec plan de
     correction et délai, ou *contesté* avec preuve ;
   - l'auditeur, repris, réplique aux contestations : il maintient, requalifie ou retire ;
   - le `contradicteur` signale ce que l'audit lui-même aurait manqué ;
   - arbitrage, constat par constat : **corriger avant lancement**, **corriger après** à date fixée, ou
     **accepter le risque** en nommant qui l'accepte. Les constats bloquants sont tranchés par l'utilisateur.
5. **Corriger et recontrôler.** Chaque correction retourne à son auteur, repris avec le constat. L'auditeur,
   repris lui aussi, recontrôle chaque constat corrigé et le passe à `verifie`. Un constat corrigé mais non
   recontrôlé reste ouvert.
6. **Avis final** ajouté en tête du rapport : *favorable*, *favorable avec réserves* (listées) ou *défavorable*.
   Cet avis alimente le go/no-go ; il ne le remplace pas.

En mode `integral`, un second `auditeur-general` mène un contre-audit sur un échantillon différent ; les écarts
entre les deux rapports sont eux-mêmes des constats.

## Méthode de l'auditeur

Aller du mécanique au jugement, pour dépenser l'attention là où elle compte.

1. **Contrôles mécaniques d'abord**, dans le dossier du projet :
   `cortex.py etat` ; `couverture stats` ; `couverture liste --statut a-faire --criticite bloquant` ;
   `tracabilite verifier` ; `interactions verifier` ; `docs verifier` ; `registre constats liste --ouverts` ;
   `registre anomalies liste --ouverts` ; `registre risques liste --ouverts`.
2. **Vue d'ensemble** : `00-pilotage/index-documents.md` (le régénérer : `cortex.py docs index`), fiche projet,
   registre des décisions.
3. **Cinq axes**, avec la grille de `references/grille-audit.md` :
   - *complétude* : tout ce qui devait exister existe ; chaque contrôle de couverture a une issue justifiée ;
   - *cohérence* : les documents ne se contredisent pas (périmètre, budget, planning, architecture, juridique,
     marketing racontent le même projet) ;
   - *conformité* : normes de développement, sécurité, accessibilité, droit applicable ;
   - *preuves* : un contrôle « fait » pointe vers une preuve qui existe et dit bien ce qu'on lui fait dire ; un
     chiffre a une source ; un test « vert » a une trace ;
   - *risques résiduels* : ce qui reste dangereux même si tout est conforme.
4. **Échantillonnage par le risque** : lire en entier les documents dont dépend le plus le reste (cahier des
   charges, dossier d'architecture, modèle de menaces, budget, conformité, PV de recette), et vérifier par
   sondage au moins dix contrôles « fait » et trois contrôles « non-applicable ».
5. **Vérifications actives** : refaire un calcul du budget, rejouer une suite de tests avec `essais.py`, ouvrir
   une source citée, suivre un parcours dans la matrice d'interactions de bout en bout.
6. **Rédiger** le rapport au gabarit de `references/rapport-audit.md`, et enregistrer chaque constat :
   `cortex.py registre constats ajouter source=audit-general gravite=… domaine=… constat="…" preuve="…" responsable=… recommandation="…"`.

## Gravité d'un constat

| Gravité | Définition | Effet |
|---|---|---|
| `bloquant` | met en cause le lancement : risque légal ou pénal, faille exploitable, perte de données, fonction vitale non testée, incohérence majeure | interdit le passage du jalon tant qu'il est ouvert |
| `majeur` | dégrade sérieusement la qualité, le coût ou le délai | à corriger avant lancement sauf décision contraire tracée |
| `mineur` | défaut limité | à planifier |
| `observation` | piste d'amélioration ou bonne pratique à généraliser | pour information |

## Exigences de l'audit

- Un constat cite sa preuve : fichier et section, sortie de script, source. Pas de constat d'impression.
- Un constat désigne un pôle responsable et propose une correction réaliste.
- L'auditeur dit aussi ce qu'il **n'a pas pu vérifier** et pourquoi : c'est une information, pas un aveu.
- L'auditeur relève les points forts : savoir ce qui est solide évite de le casser en corrigeant le reste.
- Tout ce qui engage juridiquement, fiscalement ou en sécurité certifiante est marqué « à valider par un
  professionnel », même quand l'audit n'a rien trouvé.

## Auditer un projet qui n'a pas été mené avec Dan-Cortex

Créer un dossier d'audit (`cortex.py init` avec les types et étiquettes du projet, `--perimetre J5`), y référencer
les documents et le code existants dans la fiche projet, puis dérouler l'audit général : la matrice de couverture
sert de liste de questions, et chaque contrôle sans preuve devient un constat.

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/grille-audit.md` | par l'auditeur, avant d'instruire les cinq axes |
| `${CLAUDE_SKILL_DIR}/references/rapport-audit.md` | par l'auditeur, avant de rédiger |
