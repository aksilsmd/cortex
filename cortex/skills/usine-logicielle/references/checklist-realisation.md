# Contrôles — réalisation

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| DEV-001 | J3 | majeur | tous | code | Le découpage en lots indique pour chaque lot son agent, ses dépendances, les exigences couvertes et son incrément | 04-realisation/lots.md | bonne pratique ; DORA 2025 |
| DEV-002 | J4 | bloquant | tous | code | Chaque contrat d'interface entre lots existe sous forme exécutable et versionnée, et est figé avant le premier développement | 04-realisation/lots.md | bonne pratique |
| DEV-003 | J4 | majeur | tous | code | Chaque fichier du dépôt appartient à un seul lot, et aucun agent n'écrit hors de ses fichiers propres | 04-realisation/lots.md | bonne pratique |
| DEV-004 | J4 | majeur | tous | code | Le graphe de dépendances entre lots ne comporte aucun cycle et l'incrément 1 livre un parcours de bout en bout | 04-realisation/lots.md | bonne pratique |
| DEV-005 | J4 | majeur | tous | code | Chaque lot a une commande unique de vérification (format, analyse statique, types, tests) lancée par essais.py | 04-realisation/lots.md | bonne pratique ; code.claude.com/docs/en/costs |
| DEV-006 | J4 | bloquant | tous | code | Les tests unitaires de chaque lot sont écrits avant le code et passent sans réseau ni horloge réelle | rapport de test | ISTQB CTFL v4.0.1 |
| DEV-007 | J4 | majeur | tous | code | Le code nouveau de chaque lot atteint le seuil de couverture et de duplication fixé dans les normes de développement | 04-realisation/journal-de-build.md | SonarQube « Sonar way » |
| DEV-008 | J4 | majeur | tous | code | Aucune nouvelle alerte d'analyse statique ni violation des règles d'architecture n'est ouverte sur le code livré | 04-realisation/journal-de-build.md | ISO/IEC 25010:2023 maintainability |
| DEV-009 | J4 | mineur | tous | code | Tout test existant, seuil de qualité ou règle d'analyse modifié pour obtenir le vert porte une justification écrite validée | 04-realisation/journal-de-build.md | bonne pratique |
| DEV-010 | J4 | bloquant | tous | code | Chaque lot est relu sur ses différences par un relecteur distinct de son auteur, avec un verdict écrit | 04-realisation/revues/ | bonne pratique ; code.claude.com/docs/en/best-practices |
| DEV-011 | J4 | majeur | tous | code | Les constats bloquants et majeurs de revue sont corrigés et recontrôlés avant la livraison du lot | 00-pilotage/registres/constats.csv | bonne pratique |
| DEV-012 | J4 | majeur | tous | code | Chaque anomalie a reçu au plus trois tentatives de correction avant escalade, avec ce qui a été essayé | 04-realisation/journal-de-build.md | bonne pratique |
| DEV-013 | J4 | majeur | tous | code | La non-régression des lots voisins est rejouée après chaque correction et son résultat est consigné | 04-realisation/journaux/ | ISTQB CTFL v4.0.1 |
| DEV-014 | J4 | majeur | tous | code | Les dépendances ajoutées sont déclarées, leurs licences autorisées, et un inventaire des composants est produit à chaque build | 03-conception/architecture/dependances.md | SBOM CycloneDX ou SPDX |
| DEV-015 | J4 | majeur | tous | code | Aucun secret ni donnée réelle de production n'apparaît dans le code, les tests ou les journaux de build | rapport de test | OWASP ASVS (version à vérifier) |
| DEV-016 | J4 | mineur | tous | code | Les messages de commit suivent Conventional Commits et les versions suivent SemVer sans étiquette posée à la main | 04-realisation/journal-de-build.md | Conventional Commits 1.0 ; SemVer 2.0 |
| DEV-017 | J4 | majeur | site,ecommerce,saas,niche,erp | code | Les entrées de chaque point d'entrée serveur sont validées et la journalisation ne contient aucune donnée personnelle | 04-realisation/revues/ | RGPD art. 5 (minimisation) ; à valider |
| DEV-018 | J4 | majeur | ecommerce,saas,erp | code | Les écritures multiples d'une règle de gestion sont transactionnelles et les opérations rejouables sont idempotentes | rapport de test | bonne pratique |
| DEV-019 | J4 | majeur | site,ecommerce,saas,niche,erp | code | Chaque migration de schéma est versionnée, rejouable et testée en avant et, si possible, en arrière | rapport de test | bonne pratique |
| DEV-020 | J4 | majeur | site,ecommerce,saas,niche | code | Chaque écran réalise tous les états de la matrice d'interactions : vide, chargement, erreur, succès et non autorisé | rapport de test | bonne pratique |
| DEV-021 | J4 | majeur | site,ecommerce,saas | code | Les composants d'interface passent un contrôle d'accessibilité automatisé sans violation sérieuse ni critique, et se pilotent au clavier | rapport de test | WCAG 2.2 AA ; ISO/IEC 40500:2025 |
| DEV-022 | J4 | majeur | site,ecommerce,saas,mobile | code+multilingue | Aucun texte visible n'est écrit en dur : tout libellé passe par les fichiers de traduction, y compris le sens de lecture | rapport de test | bonne pratique |
| DEV-023 | J4 | majeur | mobile | code+stores | L'application respecte les exigences de publication des magasins et ne demande une permission qu'au moment de son usage | rapport de test | règles des stores, version à vérifier |
| DEV-024 | J4 | majeur | mobile | code+hors-ligne | Les parcours hors ligne sont testés : mise en file, reprise de connexion, résolution des conflits et message à l'utilisateur | rapport de test | bonne pratique |
| DEV-025 | J4 | majeur | erp,ecommerce | progiciel,integrations | Le paramétrage du progiciel et les correspondances de données sont documentés, versionnés et rejouables sur un environnement vierge | 04-realisation/journal-de-build.md | bonne pratique |
| DEV-026 | J4 | bloquant | erp,ecommerce,saas | migration | La reprise de données est réconciliée : volumes, totaux et échantillons concordent, les rejets sont listés et la reprise est rejouable | rapport de test | bonne pratique |
| DEV-027 | J4 | majeur | erp,ecommerce,saas | integrations | Chaque échange avec un tiers est idempotent, a une gestion des relances et un test de contrat contre une simulation | rapport de test | Pact ; bonne pratique |
| DEV-028 | J4 | bloquant | tous | code | Aucun lot n'est livré avec une vulnérabilité critique ou haute ouverte, ni avec un test unitaire, fonctionnel ou d'API en échec | 04-realisation/journal-de-build.md | bonne pratique |
