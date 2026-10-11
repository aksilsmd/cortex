# Normes de développement et politique de dépendances

Écrire le référentiel de normes, le faire appliquer par des outils, surveiller les écarts résiduels, tenir les dépendances. État : octobre 2026. Versions d'outils non vérifiées : les relever à la source avant de les figer.

## Sommaire
1. La règle : l'outil d'abord
2. Contenu du référentiel
3. Norme → outil, par écosystème
4. Seuils de qualité
5. Surveillance par échantillonnage
6. Dépendances et licences
7. Gabarits
8. Pièges et contrôles avant de rendre

## 1. La règle : l'outil d'abord

Une norme vérifiée par un outil coûte zéro token à chaque diff ; vérifiée par un modèle, elle coûte à chaque lecture et varie. Choisir le mode le moins cher qui la tient.

| Nature de la norme | Mode de contrôle | Coût |
|---|---|---|
| Mécanique (format, imports, nommage de fichiers, types, commits, couches, cycles) | outil en pré-commit et en intégration continue bloquante | nul |
| Mesurable (couverture, duplication, complexité, vulnérabilités, licences) | seuil dans la chaîne, qui fait échouer la fusion | nul |
| Partiellement outillable (journalisation sans donnée personnelle, messages d'erreur) | règle d'outil pour le cas simple, échantillon de diffs pour le reste | faible |
| Jugement (clarté du nommage métier, pertinence d'un test, découpage) | relecture humaine ou `relecteur-code`, sur les seuls diffs que les outils ne tranchent pas | élevé |

Le contrôle local (pré-commit, lefthook) donne un retour rapide ; **la chaîne d'intégration fait foi**, car il se contourne. Toute règle désactivée porte un commentaire.

## 2. Contenu du référentiel

| Rubrique | Ce qu'on fixe | Contrôlé par |
|---|---|---|
| Style | formateur unique, largeur, ordre des imports | formateur en mode vérification |
| Structure du dépôt | arborescence, un module par contexte, fichiers obligatoires (README, CODEOWNERS, licence) | test d'architecture, script |
| Nommage | casse, préfixes, vocabulaire métier (glossaire de la SFG) | lint ; glossaire en échantillon |
| Erreurs | types d'erreur, aucune erreur avalée, messages exacts de la SFD | lint ; échantillon |
| Journalisation | format structuré, niveaux, identifiant de corrélation, aucune donnée personnelle ni secret | lint ; échantillon |
| Tests | pyramide ou trophée, nommage, aucun test sans assertion, instable mis en quarantaine sous 48 h avec ticket | lint, seuils |
| Commits | Conventional Commits 1.0, versions SemVer 2.0, changelog généré | commitlint |
| Branches | trunk-based, branches courtes, feature flags ; GitFlow seulement pour des versions maintenues en parallèle | protection de branche |
| Revue | revue obligatoire, CODEOWNERS, taille de demande de fusion plafonnée | plateforme de dépôt |
| Sécurité | pas de secret dans le dépôt, entrées validées, dépendances scannées | scan de secrets, analyse statique, scan de dépendances |
| Accessibilité | cible WCAG 2.2 AA (ISO/IEC 40500:2025) sauf exigence contractuelle contraire (EN 301 549 v3.2.1 reste à WCAG 2.1 AA) | axe dans les tests de bout en bout, audit manuel |
| Documentation | README, commandes, décisions à jour ; `CLAUDE.md` ou `AGENTS.md` court | revue d'échantillon |

Décliner ISO/IEC 25010:2023 (neuf caractéristiques, Safety ajoutée) en tableau « caractéristique → contrôle ou revue » ; écarter une caractéristique par décision écrite. ISO/IEC 5055 n'en mesure que quatre : indicateur, pas preuve.

## 3. Norme → outil, par écosystème

Synthèse d'expert, non sourcée sauf mention : vérifier les outils et versions avant de les imposer.

| Écosystème | Format et lint | Types | Architecture | Tests unitaires | Dépendances |
|---|---|---|---|---|---|
| JavaScript, TypeScript | Biome ou ESLint avec Prettier | `tsc` strict | dependency-cruiser | Vitest ou Jest | npm audit ou OSV-Scanner, Renovate |
| Python | Ruff | mypy | import-linter | pytest, Hypothesis | pip-audit ou OSV-Scanner, Renovate |
| Java, Kotlin | Checkstyle, SpotBugs ; ktlint, detekt | compilateur | ArchUnit (Kotlin : Konsist) | JUnit 5 | OWASP Dependency-Check, Renovate |
| PHP | PHP-CS-Fixer ou Pint | PHPStan ou Psalm | Deptrac | PHPUnit ou Pest | Composer audit, Renovate |
| Go | gofmt, golangci-lint | compilateur | règles d'import de golangci-lint (à vérifier) | `go test` | govulncheck, Renovate |
| C# | `dotnet format`, analyseurs Roslyn, `.editorconfig` | compilateur, nullable activé | NetArchTest ou ArchUnitNET | xUnit | `dotnet list package --vulnerable`, Renovate |
| Dart, Flutter | `dart format`, `dart analyze` | analyseur en mode strict | tests de dépendances maison (à vérifier) | `flutter test` | `dart pub outdated`, Renovate |
| Swift | SwiftFormat ou swift-format, SwiftLint | compilateur | règles SwiftLint sur les imports (à vérifier) | XCTest ou Swift Testing | Swift Package Manager, Dependabot |

Transverses : SonarQube pour les seuils, commitlint, un scan de secrets, un générateur de SBOM CycloneDX ou SPDX. Mutation : Stryker, mutmut, PIT.

## 4. Seuils de qualité

| Seuil | Valeur de départ | Portée |
|---|---|---|
| Nouvelles issues | 0 | code nouveau (« Sonar way ») |
| Couverture | ≥ 80 % | code nouveau ; à calibrer par pile |
| Duplication | ≤ 3 % | code nouveau |
| Plancher de couverture | ne baisse jamais | code global : du code généré par IA peut loger dans l'ancien code |
| Score de mutation | seuil à fixer | modules critiques, en incrémental sur le diff |
| Vulnérabilités | aucune critique ni haute ouverte | passage J4 |
| Accessibilité | 0 violation sérieuse ou critique | tests de bout en bout |
| Taille d'une demande de fusion | plafond à fixer | DORA 2025 : petits lots, surtout avec des agents |

Tenir le niveau sur le code nouveau plutôt que bloquer sur l'héritage. Les « Security Hotspots » de Sonar sont en cours de suppression : bâtir le gate sur les « security issues » (mode MQR).

## 5. Surveillance par échantillonnage

Après les outils, le gardien lit un échantillon du diff d'un lot : nommage métier, messages d'erreur, journaux, découpage. Priorité aux plus gros diffs, aux configurations d'outils, aux tests modifiés, aux règles désactivées. Consigner dans `04-realisation/revues/normes-<lot>.md`. Une remarque qui revient trois fois devient une règle d'outil. Un agent ne modifie ni seuils, ni configuration d'outils, ni tests existants sans validation (CODEOWNERS) ; toute assertion retouchée par un outil de réparation de tests est revue comme un changement de comportement.

## 6. Dépendances et licences

| Sujet | Règle |
|---|---|
| Entrée d'une dépendance directe | licence compatible, plusieurs mainteneurs, publication récente, fenêtre de support, score OpenSSF Scorecard (seuil à calibrer), version épinglée avec empreinte |
| Licences | trois listes : autorisées (permissives courantes), à décision écrite (copyleft, y compris réseau), interdites (sources disponibles non libres, comme BUSL ou SSPL). Listes « à valider » par le juriste |
| Mise à jour | Renovate ou Dependabot actif, regroupement hebdomadaire, correctifs de sécurité hors cycle |
| Traçabilité | SBOM à chaque build, scan de vulnérabilités et de licences bloquant sur critique et haute |
| Risque de rupture | pour chaque dépendance structurante, un plan de remplacement : changement de licence de Terraform (10/08/2023, fork OpenTofu) ou de Redis (fork Valkey) |

## 7. Gabarits

```markdown
# Normes de développement — <projet>
## Synthèse
Langages couverts, nombre de normes, part vérifiée par outil, seuils, décisions ISO 25010 écartées.
## Référentiel
| ID | Rubrique | Norme | Contrôle (outil ou revue) | Bloquant |
|---|---|---|---|---|
## Outils et configuration
| Écosystème | Outil | Version (à vérifier) | Fichier de configuration | Pré-commit | CI |
|---|---|---|---|---|---|
## Seuils de qualité
## Branches, commits, revue
## Dérogations
| Règle | Portée | Motif | Décideur | Échéance |
|---|---|---|---|---|
```

```markdown
# Dépendances — <projet>
## Synthèse
Nombre de dépendances directes, licences, risques, outils de mise à jour et de scan.
## Politique de licences
| Liste | Licences | Validée par |
|---|---|---|
## Inventaire des dépendances directes
| Dépendance | Version épinglée | Licence | Mainteneurs | Support jusqu'au | Scorecard | Rôle | Plan de remplacement |
|---|---|---|---|---|---|---|---|
## Mise à jour et scan
```

## 8. Pièges et contrôles avant de rendre

- Formateur et linter qui se contredisent : un seul formateur, le linter sans règle de style.
- Couverture confondue avec qualité : un agent écrit des tests qui épousent son code ; ajouter mutation et revue des assertions.
- Noms ISO 25010 de 2011 et de 2023 mélangés.
- Avant de rendre : chaque norme a un mode de contrôle, chaque outil échoue sur une violation d'essai, les versions sont marquées « à vérifier ».

## Sources

- ISO/IEC 25010:2023 ; ISO/IEC 5055:2021 (https://www.it-cisq.org/standards/code-quality-standards/)
- SonarQube, quality gates : https://docs.sonarsource.com/sonarqube-server/quality-standards-administration/managing-quality-gates/introduction-to-quality-gates
- Sonar way for AI code : https://docs.sonarsource.com/sonarqube-server/2025.1/instance-administration/analysis-functions/quality-gates
- WCAG 2.2, ISO/IEC 40500:2025 : https://www.w3.org/WAI/news/2025-10-21/wcag22-iso/
- DORA 2025 : https://dora.dev/ai/
- Conventional Commits 1.0 ; SemVer 2.0 ; OpenSSF Scorecard : https://github.com/ossf/scorecard
