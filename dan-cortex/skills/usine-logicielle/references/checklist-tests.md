# Contrôles — tests et recette

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| TST-001 | J3 | majeur | tous | - | Une stratégie de test fixe les niveaux, les outils, les propriétaires, les environnements, les seuils et les risques produit classés | 03-conception/tests/strategie-de-test.md | ISTQB CTFL v4.0.1 ; ISO/IEC/IEEE 29119-1:2022 |
| TST-002 | J3 | majeur | tous | - | Chaque niveau de test retenu a un outil, un propriétaire, un temps cible et un job d'intégration continue nommés | 03-conception/tests/strategie-de-test.md | bonne pratique |
| TST-003 | J3 | bloquant | tous | - | Le cahier de recette contient au moins un cas CT- pour chaque règle de gestion RG- et chaque workflow WF- | 03-conception/tests/cahier-de-recette.md | ISTQB CTFL v4.0.1 |
| TST-004 | J3 | bloquant | tous | - | La commande de vérification de traçabilité s'exécute sans erreur : aucune exigence, fonction, règle ou workflow sans cas de test | rapport de test | bonne pratique |
| TST-005 | J3 | majeur | tous | - | Chaque exigence non fonctionnelle chiffrée est couverte par un cas de test de performance, d'accessibilité, de sécurité ou de compatibilité | 03-conception/tests/cahier-de-recette.md | ISO/IEC 25010:2023 |
| TST-006 | J3 | majeur | tous | - | Chaque élément interactif de la matrice est couvert par un cas de test, directement ou par le cas de son workflow | 03-conception/tests/cahier-de-recette.md | bonne pratique |
| TST-007 | J3 | majeur | tous | - | Chaque cas de test précise ses préconditions, ses étapes, un résultat attendu observable et exact, sa priorité et son mode | 03-conception/tests/cahier-de-recette.md | ISO/IEC/IEEE 29119-1:2022 |
| TST-008 | J3 | majeur | tous | - | Chaque objet à cycle de vie a sa table d'états, des cas pour les transitions autorisées et des cas de refus pour les interdites | 03-conception/tests/cahier-de-recette.md | ISTQB CTFL v4.0.1 |
| TST-009 | J3 | majeur | tous | - | Les règles à seuil ont des cas aux valeurs limites et les règles à plusieurs conditions une table de décision | 03-conception/tests/cahier-de-recette.md | ISTQB CTFL v4.0.1 |
| TST-010 | J3 | mineur | tous | - | Les cas de test sont relus par l'auteur de la spécification et par un développeur pour leur testabilité | 00-pilotage/audits | bonne pratique |
| TST-011 | J3 | majeur | tous | - | Les critères d'entrée et de sortie de la recette sont chiffrés et acceptés par l'utilisateur avant la première campagne | 03-conception/tests/strategie-de-test.md | bonne pratique |
| TST-012 | J3 | majeur | tous | - | La grille de sévérité et de priorité des anomalies est publiée et le cycle de vie des anomalies est défini | 03-conception/tests/strategie-de-test.md | ISTQB CTFL v4.0.1 |
| TST-013 | J3 | majeur | tous | donnees-perso | La stratégie interdit les données de production non anonymisées dans tous les environnements de test et de recette | 03-conception/tests/strategie-de-test.md | RGPD art. 5 ; bonne pratique |
| TST-014 | J4 | majeur | tous | - | Un harnais de tests exécutable par une commande unique à sortie courte est livré avec ses jeux de données déterministes | 04-realisation/journal-de-build.md | bonne pratique |
| TST-015 | J4 | bloquant | tous | code | Les tests unitaires de chaque lot passent en intégration continue, sans réseau ni horloge réelle | rapport de test | ISTQB CTFL v4.0.1 |
| TST-016 | J4 | majeur | tous | code | La couverture du code nouveau atteint le seuil fixé dans la stratégie, 80 % par défaut, et la couverture globale ne régresse pas | rapport de test | Sonar way, quality gate |
| TST-017 | J4 | mineur | tous | code | Un score de mutation est mesuré sur les modules du cœur métier et comparé au seuil fixé | rapport de test | bonne pratique |
| TST-018 | J4 | majeur | tous | code | Les tests d'intégration utilisent des dépendances réelles éphémères et aucun simulacre de base de données | rapport de test | bonne pratique |
| TST-019 | J4 | majeur | saas,ecommerce,erp,mobile | integrations | Chaque endpoint a un cas nominal, des cas 4xx, un cas d'autorisation et une validation de schéma, au vert | rapport de test | OpenAPI ; bonne pratique |
| TST-020 | J4 | majeur | saas,ecommerce,erp,mobile | integrations | Un test de contrat protège chaque interface dont le consommateur relève d'une autre équipe ou d'un autre fournisseur | rapport de test | bonne pratique |
| TST-021 | J4 | bloquant | tous | - | Les parcours critiques passent en test de bout en bout, avec traces conservées et ordre d'exécution aléatoire | rapport de test | bonne pratique |
| TST-022 | J4 | majeur | mobile | stores | Les parcours critiques passent sur émulateur en intégration continue puis sur appareils réels avant chaque version publiée | rapport de test | bonne pratique |
| TST-023 | J4 | majeur | tous | - | Aucun test instable n'est relancé jusqu'au vert : chacun est en quarantaine avec une anomalie ouverte sous 48 heures | 00-pilotage/registres | bonne pratique |
| TST-024 | J4 | majeur | tous | - | Toute modification d'un test existant, d'un seuil de qualité ou d'une assertion par un agent est relue par un tiers | 04-realisation/revues | bonne pratique |
| TST-025 | J4 | majeur | tous | - | Les anomalies détectées pendant la réalisation sont enregistrées avec leur cas de test, leur lot, leur sévérité et un responsable | 00-pilotage/registres/anomalies.csv | ISTQB CTFL v4.0.1 |
| TST-026 | J4 | bloquant | tous | - | La non-régression automatisée est rejouée après chaque correction et reste au vert avant la clôture du lot | rapport de test | ISTQB CTFL v4.0.1 |
| TST-027 | J4 | majeur | tous | migration | Les reprises de données sont testées sur un jeu représentatif avec rapprochement des volumes et des totaux de contrôle | rapport de test | bonne pratique |
| TST-028 | J5 | bloquant | tous | - | Le recetteur, indépendant des développeurs du lot, exécute le cahier de recette complet sur une version identifiée et figée | 05-validation/pv-recette.md | ISO/IEC/IEEE 29119-1:2022 |
| TST-029 | J5 | bloquant | tous | - | Les critères d'entrée de la campagne sont vérifiés avant son lancement : version déployée, fumée au vert, données chargées | 05-validation/pv-recette.md | bonne pratique |
| TST-030 | J5 | bloquant | tous | - | Aucune anomalie bloquante n'est ouverte et chaque anomalie majeure est corrigée ou porte un contournement validé par écrit | 00-pilotage/registres/anomalies.csv | ISTQB CTFL v4.0.1 |
| TST-031 | J5 | bloquant | tous | - | Tous les cas critiques sont exécutés et passés sur la version finale, et la non-régression est au vert | 05-validation/pv-recette.md | bonne pratique |
| TST-032 | J5 | majeur | tous | - | Chaque anomalie fermée a été contre-testée par le recetteur, et la fermeture est justifiée dans le registre | 00-pilotage/registres/anomalies.csv | ISTQB CTFL v4.0.1 |
| TST-033 | J5 | majeur | tous | - | Le rapport de performance compare les mesures p95 et le taux d'erreur aux objectifs chiffrés et à la référence précédente | 05-validation/rapport-performance.md | ISO/IEC 25010:2023 |
| TST-034 | J5 | majeur | site,ecommerce,saas,mobile | - | Les tests automatiques d'accessibilité ne relèvent aucune violation sérieuse ou critique et un audit manuel clavier et lecteur d'écran est fait | 05-validation/rapport-accessibilite.md | WCAG 2.2 AA ; ISO/IEC 40500:2025 |
| TST-035 | J5 | majeur | tous | - | Les tests de compatibilité couvrent les navigateurs, systèmes et tailles d'écran de la liste de support du cahier des charges | rapport de test | ISO/IEC 25010:2023 |
| TST-036 | J5 | majeur | tous | - | La recette utilisateur est menée par un panel défini, avec scénarios métier, canal de retour unique et critère de clôture écrit | 05-validation/pv-recette.md | bonne pratique |
| TST-037 | J5 | majeur | tous | - | Le procès-verbal de recette cite la version testée, les résultats, les réserves et l'écart aux critères de sortie | 05-validation/pv-recette.md | ISO/IEC/IEEE 29119-1:2022 |
| TST-038 | J5 | bloquant | tous | - | Le procès-verbal de recette est signé par l'utilisateur ou son représentant, avec ou sans réserves nominatives | 05-validation/pv-recette.md | bonne pratique |
| TST-039 | J6 | majeur | tous | - | Une campagne de fumée au vert est rejouée sur l'environnement de production après le déploiement, avant l'ouverture au public | rapport de test | bonne pratique |
| TST-040 | J7 | mineur | tous | - | Les anomalies reportées ont une version cible, un responsable et une date au registre, et le bilan de test est repris au bilan de projet | 07-exploitation/bilan-de-projet.md | bonne pratique |
