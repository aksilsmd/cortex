# Contrôles — gouvernance et pilotage

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| GOV-001 | J1 | bloquant | tous | - | Un porteur du projet qui décide est nommé par écrit, avec son périmètre de décision et sa disponibilité estimée | 00-pilotage/fiche-projet.md | PRINCE2 7 ; HERMES 2022 |
| GOV-002 | J1 | majeur | tous | - | Une seule personne porte la responsabilité du projet de bout en bout, distincte des prestataires | 00-pilotage/fiche-projet.md | Cour des comptes 2020 |
| GOV-003 | J1 | majeur | tous | - | Le problème à résoudre, la population concernée et le résultat attendu sont écrits en une phrase chacun | 00-pilotage/fiche-projet.md | bonne pratique |
| GOV-004 | J1 | majeur | tous | - | La liste des parties prenantes, avec leur rôle et leur influence, est établie dès l'initiation | 00-pilotage/fiche-projet.md | HERMES 2022 ; PMBOK 8 |
| GOV-005 | J1 | majeur | tous | - | L'ordre de grandeur du budget et du délai souhaités par le porteur est consigné, avec le niveau d'autonomie accordé | 00-pilotage/fiche-projet.md | bonne pratique |
| GOV-006 | J1 | mineur | tous | - | L'existant (marque, site, données, équipes, outils, contrats en cours) est inventorié avec ses contraintes de reprise | 00-pilotage/fiche-projet.md | bonne pratique |
| GOV-007 | J1 | majeur | tous | - | Les instances de décision ont un mandat écrit, un président et des seuils d'escalade | 00-pilotage/organigramme.md | PRINCE2 7 ; bonne pratique |
| GOV-008 | J1 | majeur | tous | - | Les décisions de type 1 sont distinguées de celles de type 2 et réservées à l'utilisateur au registre des décisions | 00-pilotage/registres/decisions.csv | bonne pratique |
| GOV-009 | J2 | bloquant | tous | - | Le périmètre de la première version est validé par le porteur, avec la liste explicite de ce qui en est exclu | 02-cadrage/note-de-cadrage.md | NF EN 16271 |
| GOV-010 | J2 | majeur | tous | - | Chaque exigence du cahier des charges porte un identifiant, une priorité et un critère d'acceptation vérifiable | 02-cadrage/cahier-des-charges.md | ISO/IEC/IEEE 29148 |
| GOV-011 | J2 | majeur | tous | - | Toute demande de changement de périmètre après validation passe par un registre des changements avec son effet chiffré | 00-pilotage/registres/decisions.csv | PRINCE2 7 ; HERMES 2022 |
| GOV-012 | J2 | bloquant | tous | - | Le planning donne les lots, les charges à trois points, le chemin critique nommé et une marge explicite | 00-pilotage/planning.md | planification.md |
| GOV-013 | J2 | majeur | tous | - | Chaque estimation de charge indique sa base : analogie, décompte ou avis d'expert, et les hypothèses retenues | 00-pilotage/planning.md | planification.md |
| GOV-014 | J2 | majeur | tous | - | Les activités non techniques figurent au planning : juridique, contenus, marketing, formation, recette et validations du porteur | 00-pilotage/planning.md | planification.md |
| GOV-015 | J2 | majeur | tous | - | Les délais subis par des tiers (avis, revues, observation, fournisseurs) sont inscrits au planning avec leur source | 00-pilotage/planning.md | bonne pratique |
| GOV-016 | J2 | majeur | tous | - | Un RACI nomme un seul approbateur pour chaque décision et chaque livrable majeur | 00-pilotage/planning.md | PRINCE2 7 |
| GOV-017 | J2 | majeur | tous | - | Le registre des risques contient, pour chaque risque sérieux, un propriétaire, une parade et un déclencheur observable | 00-pilotage/registres/risques.csv | ISO 31000:2018 |
| GOV-018 | J2 | majeur | tous | - | L'écart entre le planning estimé et le délai ou le budget souhaité est présenté au porteur avec au moins deux scénarios | 00-pilotage/planning.md | bonne pratique |
| GOV-019 | J2 | majeur | tous | - | Le cycle de vie retenu (séquentiel, itératif ou hybride) est choisi et justifié par écrit | 00-pilotage/planning.md | HERMES 2022 |
| GOV-020 | J2 | majeur | erp,saas,ecommerce | grand-compte,integrations,migration | Un dossier de faisabilité chiffre au moins deux scénarios et a été étudié par le comité de pilotage | 02-cadrage/note-de-cadrage.md | Cour des comptes 2020 |
| GOV-021 | J2 | majeur | tous | secteur-public | Le taux d'externalisation est calculé et comparé aux seuils d'alerte de 60 % et d'exclusion de 80 % | 00-pilotage/planning.md | circulaire du 7 février 2023 |
| GOV-022 | J2 | majeur | tous | secteur-public | L'avis amont de la DINUM est demandé pour un projet dépassant 9 M€, avec un mois prévu au planning | 00-pilotage/planning.md | DINUM ; Cour des comptes 2020 |
| GOV-023 | J3 | majeur | tous | - | Les dépendances externes (fournisseurs, tiers, plateformes, autres projets) sont listées avec un propriétaire et une date limite | 00-pilotage/planning.md | bonne pratique |
| GOV-024 | J3 | majeur | tous | integrations,progiciel,migration | Chaque fournisseur ou intégrateur dispose d'un contrat ou d'une lettre de mission avec livrables, dates et conditions de sortie | contrat signé | bonne pratique |
| GOV-025 | J3 | majeur | tous | - | Un plan de communication du projet précise destinataires, fréquence et contenu des points de situation et des comptes rendus | 00-pilotage/planning.md | PRINCE2 7 ; PMBOK 8 |
| GOV-026 | J3 | mineur | tous | - | Chaque décision structurante est consignée au registre avec ses options écartées, son décideur et sa date | 00-pilotage/registres/decisions.csv | MADR |
| GOV-027 | J3 | majeur | erp,saas,ecommerce,site | grand-compte,migration | Un plan de conduite du changement rattache formation, communication et mesure d'adoption aux jalons de déploiement | 00-pilotage/planning.md | PRINCE2 7 ; bonne pratique |
| GOV-028 | J4 | majeur | tous | - | L'écart de délai et de coût par rapport à la référence validée est mesuré et reporté à chaque point d'étape | 00-pilotage/tableau-de-bord.md | bonne pratique |
| GOV-029 | J4 | mineur | tous | - | Les risques sont réévalués à chaque jalon et les risques réalisés passent au registre des anomalies ou des actions | 00-pilotage/registres/risques.csv | ISO 31000:2018 |
| GOV-030 | J5 | bloquant | tous | - | Le procès-verbal de recette est signé par le porteur et liste les réserves restantes avec leur échéance | 05-validation/pv-recette.md | CCAG-TIC 2021 |
| GOV-031 | J5 | bloquant | tous | - | La décision de lancement est prise par le porteur sur la base de la liste de go/no-go, avec un critère d'arrêt écrit | 06-lancement/checklist-go-no-go.md | HERMES 2022 |
| GOV-032 | J7 | mineur | tous | - | Une rétrospective consigne ce qui a marché, ce qui a coûté et ce qu'on change, avec le bilan de consommation | 07-exploitation/bilan-de-projet.md | bonne pratique |
