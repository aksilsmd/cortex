# Boucle de build et de test d'un lot

La boucle que suit chaque développeur pour un lot, de la mise en route à la livraison. Elle est identique pour les quatre développeurs ; seules leurs exigences propres changent.

## Sommaire
1. La boucle en sept temps
2. Contrôles automatiques
3. Revue des différences
4. Définition de « terminé »
5. Règle des trois tentatives et escalade
6. Gabarit du journal de build
7. Gabarit de la note de revue
8. Pièges fréquents
9. Contrôles avant de rendre
10. Sources

## 1. La boucle en sept temps

1. **Cadrer.** Lire l'ordre de mission, la fiche du lot dans `lots.md`, ses contrats, les `RG-` et `CT-` couverts, les normes. Rien d'autre.
2. **Écrire les tests unitaires** d'une règle ou d'un comportement, les voir échouer pour la bonne raison (rouge).
3. **Écrire le code** minimal qui les passe (vert), puis refactorer. Un fichier, un test, puis la suite.
4. **Contrôles automatiques** (section 2), en une commande unique via `essais.py`.
5. **Revue des différences** par `relecteur-code` (section 3).
6. **Tests du lot** : fonctionnels, d'API, de bout en bout par `automaticien-tests`, rejoués par `executant-tests`.
7. **Correction et non-régression** : le développeur est repris, corrige, rejoue toute la suite du lot et les suites voisines.

## 2. Contrôles automatiques

Une seule commande de vérification par lot, déclarée dans `lots.md`, enchaîne dans l'ordre : format, analyse statique, types, tests unitaires, tests d'architecture, couverture du code nouveau. Elle passe toujours par `essais.py`.

| Contrôle | Seuil de départ | Note |
|---|---|---|
| Nouvelles alertes d'analyse statique | 0 | code nouveau, pas l'ancien |
| Couverture du code nouveau | ≥ 80 % | seuil « Sonar way », à calibrer par pile |
| Duplication du code nouveau | ≤ 3 % | idem |
| Règles d'architecture (couches, cycles) | 0 violation | dependency-cruiser, import-linter, ArchUnit |
| Dépendance nouvelle | listée, licence autorisée | `dependances.md` |
| Secrets dans les différences | 0 | analyse de secrets |

Une règle désactivée porte un commentaire justifié. Abaisser un seuil ou retoucher un test existant pour obtenir le vert est interdit sans validation du chef d'orchestre, tracée.

## 3. Revue des différences

`relecteur-code` reçoit la liste des fichiers modifiés et la différence, les contrats, les `RG-` du lot et la sortie verte des contrôles, jamais le raisonnement de l'auteur ni le dépôt entier. Il cherche ce que les outils ne voient pas :

- l'écart entre une règle `RG-` et son code, un cas limite oublié, une transaction ou une idempotence manquante ;
- des tests qui épousent le code : assertion absente, tautologique, mock qui masque le comportement ;
- la lisibilité, la complexité cachée, le code mort, la dette créée sans le dire ;
- les failles évidentes (validation d'entrée, autorisation, secret, journalisation de donnée personnelle).

Verdict : accepté, accepté avec réserves, refusé. Il constate, il ne modifie rien.

## 4. Définition de « terminé »

Un lot est terminé quand toutes les cases sont vraies, preuves à l'appui :

- tests unitaires écrits avant le code, verts, couverture du code nouveau au seuil ;
- commande de vérification verte, journal rangé dans `04-realisation/journaux/` ;
- revue : accepté, constats bloquants et majeurs corrigés ;
- tests fonctionnels, d'API et de bout en bout du lot verts ;
- non-régression des lots voisins verte ;
- contrôles de sécurité automatisés sans vulnérabilité critique ni haute ;
- journal de build à jour, aucun fichier hors de la propriété du lot modifié.

## 5. Règle des trois tentatives et escalade

Par anomalie : trois tentatives de correction au plus. Chaque tentative commence par la **cause**, lue dans les lignes d'échec, pas par un essai au hasard. À la troisième sans succès, ne pas insister :

| Nature de l'échec | Escalade vers |
|---|---|
| Revue ou norme contestée | `relecteur-code`, puis `gardien-des-normes` |
| Contrat insuffisant ou contradictoire | `architecte-solution` |
| Règle de gestion ambiguë | `redacteur-sfd`, via le chef d'orchestre |
| Test lui-même douteux | `concepteur-tests` |
| Environnement ou intégration continue | `ingenieur-devops` |

Le compte rendu indique ce qui a été essayé et ce qui reste inconnu. Une anomalie non résolue est inscrite au registre, jamais masquée.

## 6. Gabarit du journal de build

```markdown
# Journal de build — <nom du projet>

## Synthèse
<Lots livrés sur lots prévus, incrément en cours, anomalies ouvertes, tentatives épuisées, écarts.>

| Date | Lot | Incrément | Agent | Tentatives | Commande de vérification | Résultat | Couverture | Revue | Anomalies ouvertes | Journal |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-12 | LOT-001 | 1 | developpeur-backend | 1 | `essais.py -- make verifier` | OK | 86 % | accepté | 0 | `journaux/lot-001.log` |
```

## 7. Gabarit de la note de revue

```markdown
# Revue de code — LOT-001

## Synthèse
Verdict : accepté / accepté avec réserves / refusé. Différence relue : <fichiers, lignes>. Constats : <n bloquants, n majeurs, n mineurs>.

| N° | Gravité | Fichier et ligne | Constat | Correction demandée |
|---|---|---|---|---|
| 1 | majeur | `code/server/core/auth.py:42` | `RG-012` non appliquée au cas d'un compte verrouillé | appliquer la règle et ajouter le test |
```

200 mots au plus ; bloquants et majeurs aussi au registre des constats.

## 8. Pièges fréquents

- S'arrêter « quand ça a l'air fini » : seul un signal exécutable ferme la boucle.
- Tests écrits après le code, qui valident le code tel qu'il est.
- Réparation automatique d'un test qui affaiblit son assertion.
- Correction hors du lot, qui crée un conflit avec un lot voisin.
- Dépendance ajoutée sans la déclarer.

## 9. Contrôles avant de rendre

- Chaque case de la section 4 a sa preuve dans le journal.
- Aucun test existant modifié sans justification écrite.
- Le compte rendu cite les fichiers touchés, les commandes lancées et les écarts.

## Sources

- Claude Code, bonnes pratiques (critère pass/fail exécutable, second avis par vérificateur) : https://code.claude.com/docs/en/best-practices
- SonarQube Server, quality gate « Sonar way » : https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates
- DORA 2025 : https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Playwright, Test Agents (healer qui peut affaiblir un test) : https://playwright.dev/docs/test-agents
- ISO/IEC 25010:2023 (maintainability, reliability), état : octobre 2026.
