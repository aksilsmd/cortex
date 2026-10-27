# Contrôles — normes de développement et dépendances

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| NOR-001 | J3 | bloquant | tous | code | Le référentiel de normes versionné couvre style, structure du dépôt, nommage, erreurs, journalisation, tests, commits, branches, revue, sécurité, accessibilité et documentation | 03-conception/architecture/normes-developpement.md | bonne pratique |
| NOR-002 | J3 | majeur | tous | code | Chaque norme du référentiel est rattachée à un outil de contrôle ou, à défaut, à une revue d'échantillon nommée | 03-conception/architecture/normes-developpement.md | bonne pratique |
| NOR-003 | J3 | mineur | tous | code | Le modèle ISO/IEC 25010:2023 est décliné en tableau caractéristique-contrôle ; Safety et Interaction capability sont retenues ou écartées par décision écrite | 03-conception/architecture/normes-developpement.md | ISO/IEC 25010:2023 |
| NOR-004 | J3 | majeur | tous | code | Les seuils de qualité chiffrés (code nouveau, duplication, couverture globale, mutation, taille de demande de fusion) sont fixés et calibrés sur la pile retenue | 03-conception/architecture/normes-developpement.md | SonarQube, Sonar way |
| NOR-005 | J3 | majeur | tous | code | La stratégie de branches, de revue et de fusion est écrite : branches courtes, feature flags, CODEOWNERS, taille de demande de fusion plafonnée | 03-conception/architecture/normes-developpement.md | bonne pratique ; DORA 2025 |
| NOR-006 | J3 | majeur | tous | code | La politique de licences distingue licences autorisées, à décision écrite et interdites, et elle est soumise au juriste pour validation | 03-conception/architecture/dependances.md | bonne pratique |
| NOR-007 | J3 | majeur | tous | code | Chaque dépendance directe figure à l'inventaire avec sa version épinglée, sa licence, ses mainteneurs, sa fenêtre de support et son plan de remplacement | 03-conception/architecture/dependances.md | OpenSSF Scorecard |
| NOR-008 | J4 | bloquant | tous | code | Le format, le lint et les types s'exécutent avant commit et dans un job d'intégration continue bloquant qui fait foi | 04-realisation/journal-de-build.md | bonne pratique |
| NOR-009 | J4 | majeur | tous | code | Chaque outil a une configuration versionnée et toute règle désactivée porte un commentaire justifié | 04-realisation/revues/ | bonne pratique |
| NOR-010 | J4 | bloquant | tous | code | La fusion est bloquée sur le code nouveau en cas de nouvelle issue, de couverture sous le seuil ou de duplication au-dessus du seuil | rapport de test | SonarQube, Sonar way |
| NOR-011 | J4 | majeur | tous | code | Un plancher de couverture non régressif s'applique au code global, pour y inclure le code généré par IA logé dans l'ancien code | rapport de test | Sonar way for AI code |
| NOR-012 | J4 | majeur | tous | code | Des tests d'architecture bloquants en intégration continue vérifient les couches, les cycles et les dépendances interdites | rapport de test | bonne pratique |
| NOR-013 | J4 | majeur | tous | code | Les messages de commit sont contrôlés par commitlint ; versions SemVer et changelog sont générés et aucun tag n'est posé à la main | 04-realisation/journal-de-build.md | Conventional Commits 1.0 ; SemVer 2.0 |
| NOR-014 | J4 | majeur | tous | code | Les branches principales sont protégées : revue obligatoire, propriétaires de code, intégration continue verte, aucun push direct | capture | bonne pratique |
| NOR-015 | J4 | bloquant | tous | code | Un scan de secrets s'exécute avant commit et en intégration continue, et aucun secret ne figure dans l'historique du dépôt | rapport de test | bonne pratique |
| NOR-016 | J4 | bloquant | tous | code | Le scan des dépendances (vulnérabilités, licences) est bloquant en intégration continue pour toute alerte critique ou haute | rapport de test | bonne pratique |
| NOR-017 | J4 | majeur | tous | code | Un SBOM au format CycloneDX ou SPDX est produit à chaque build et archivé avec l'artefact | 04-realisation/journal-de-build.md | CycloneDX ; SPDX |
| NOR-018 | J4 | majeur | tous | code | Un outil de mise à jour (Renovate ou Dependabot) est actif, avec regroupement des mises à jour et correctifs de sécurité traités hors cycle | capture | bonne pratique |
| NOR-019 | J4 | majeur | site,ecommerce,saas,erp | code | Les violations d'accessibilité automatisables bloquent la fusion : zéro violation sérieuse ou critique, cible WCAG 2.2 AA sauf exigence contractuelle contraire | rapport de test | WCAG 2.2 ; ISO/IEC 40500:2025 |
| NOR-020 | J4 | majeur | tous | code | La norme de journalisation (format structuré, niveaux, corrélation, aucune donnée personnelle ni secret) est vérifiée par règle d'outil ou par échantillon de diffs | 04-realisation/revues/ | bonne pratique |
| NOR-021 | J4 | majeur | tous | code | Aucun agent ne modifie seuils de qualité, configuration d'outils ou tests existants sans validation, et la taille des diffs d'agent est plafonnée | capture | DORA 2025 |
| NOR-022 | J4 | mineur | tous | code | La documentation du dépôt (README, commandes, conventions) est contrôlée à chaque lot et le fichier d'instructions des agents reste court | 04-realisation/revues/ | bonne pratique |
| NOR-023 | J4 | majeur | tous | code | Les écarts relevés par échantillonnage des diffs sont consignés, et toute remarque récurrente trois fois devient une règle d'outil | 04-realisation/revues/ | bonne pratique |
