# Contrôles — spécifications

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| SPC-001 | J2 | bloquant | tous | - | La note de cadrage nomme un sponsor et une seule personne responsable du projet de bout en bout | 02-cadrage/note-de-cadrage.md | Cour des comptes 2020 ; HERMES 2022 |
| SPC-002 | J2 | majeur | tous | - | Chaque objectif de la note de cadrage porte un indicateur de mesure, une valeur cible et une échéance | 02-cadrage/note-de-cadrage.md | bonne pratique |
| SPC-003 | J2 | majeur | tous | - | Le périmètre de la première version distingue ce qui est inclus, exclu et reporté, avec la condition de reprise | 02-cadrage/note-de-cadrage.md | bonne pratique |
| SPC-004 | J2 | majeur | tous | - | Le cycle de vie du projet (séquentiel, agile ou hybride) est choisi et justifié par écrit | 02-cadrage/note-de-cadrage.md | HERMES 2022 ; PRINCE2 7 |
| SPC-005 | J2 | majeur | tous | - | Chaque instance de pilotage a un mandat de décision écrit, un rythme et un seuil d'escalade | 02-cadrage/note-de-cadrage.md | CREDAF 2019 ; bonne pratique |
| SPC-006 | J2 | majeur | tous | - | Les critères de succès et les critères d'arrêt du projet sont écrits et chiffrés | 02-cadrage/note-de-cadrage.md | HERMES 2022 |
| SPC-007 | J2 | majeur | tous | secteur-public+fr | Pour un projet de l'État supérieur à 9 M€, l'avis de la DINUM est demandé et un mois figure au planning | 02-cadrage/note-de-cadrage.md | Assemblée nationale, QE 6412 (16e législature), à vérifier |
| SPC-008 | J2 | majeur | tous | secteur-public+fr | La part d'externalisation est calculée, avec alerte à 60 % et lancement exclu au-delà de 80 % | 02-cadrage/note-de-cadrage.md | circulaire du 7 février 2023, à vérifier |
| SPC-009 | J2 | bloquant | tous | - | Chaque exigence du cahier des charges porte un identifiant unique, une source, une priorité et un critère d'acceptation | 02-cadrage/cahier-des-charges.md | ISO/IEC/IEEE 29148:2018 |
| SPC-010 | J2 | bloquant | tous | - | Aucune exigence n'emploie un terme qualitatif (rapide, ergonomique, sécurisé, intuitif) sans seuil chiffré ni méthode de mesure | 02-cadrage/cahier-des-charges.md | ISO/IEC/IEEE 29148:2018 |
| SPC-011 | J2 | majeur | tous | - | Chaque exigence traite un seul sujet et distingue l'obligatoire (doit) du souhaitable (devrait) | 02-cadrage/cahier-des-charges.md | ISO/IEC/IEEE 29148:2018 |
| SPC-012 | J2 | majeur | tous | - | Les priorités sont justifiées en une phrase et les exigences Must représentent au plus 60 % du périmètre de la première version | 02-cadrage/cahier-des-charges.md | MoSCoW, bonne pratique |
| SPC-013 | J2 | majeur | tous | - | Le cahier des charges exprime le besoin sans imposer de solution technique, sauf contrainte justifiée et tracée | 02-cadrage/cahier-des-charges.md | NF EN 16271 |
| SPC-014 | J2 | majeur | tous | - | Chaque exigence non fonctionnelle est rattachée à une caractéristique d'ISO/IEC 25010:2023 avec métrique, seuil, conditions et méthode de vérification | 02-cadrage/cahier-des-charges.md | ISO/IEC 25010:2023 |
| SPC-015 | J2 | majeur | tous | - | Les neuf caractéristiques de qualité sont traitées ou écartées avec un motif explicite | 02-cadrage/cahier-des-charges.md | ISO/IEC 25010:2023 |
| SPC-016 | J2 | majeur | tous | - | Les thèmes transverses sont couverts ou écartés avec motif : droits, audit, export, administration, notifications, fin de vie | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-017 | J2 | majeur | tous | - | Les exigences réglementaires sont identifiées et marquées à valider par le juriste avant d'être figées | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-018 | J2 | majeur | tous | - | Les conditions de recette en test (VABF) et en production (VSR) sont décrites : environnement, données, durée, critères d'admission | 02-cadrage/cahier-des-charges.md | CCAG-TIC 2021, art. 32 et 33 |
| SPC-019 | J2 | majeur | tous | - | Le cahier des charges est relu par l'architecte, le concepteur de tests, le juriste et le contrôleur financier, constats traités | 00-pilotage/audits/ | bonne pratique |
| SPC-020 | J2 | mineur | tous | - | Les hypothèses et questions ouvertes ont un responsable et une date de levée | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-021 | J2 | mineur | tous | - | Les versions des référentiels et normes appliqués sont indiquées avec leur date | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-022 | J2 | majeur | mobile | - | Les exigences précisent les systèmes et versions minimales pris en charge, les notifications et le comportement sans réseau | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-023 | J2 | majeur | tous | migration | Les exigences de reprise de données fixent sources, volumes, qualité attendue, rapprochement et conduite en cas de rejet | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-024 | J2 | majeur | tous | integrations | Chaque système externe à interfacer est listé avec son propriétaire, sa finalité, ses données et ses contraintes | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-025 | J2 | majeur | erp,saas | progiciel | Le cahier des charges distingue ce qui relève du standard, du paramétrage et du développement spécifique | 02-cadrage/cahier-des-charges.md | bonne pratique |
| SPC-026 | J3 | bloquant | tous | - | Chaque exigence est reprise par au moins une fonction, une règle ou un workflow, selon le script de traçabilité | 03-conception/specifications/sfg.md | ISO/IEC/IEEE 29148:2018 |
| SPC-027 | J3 | bloquant | tous | - | Chaque fonction est reprise par au moins une règle de gestion ou un workflow, et aucun identifiant cité n'est indéfini | 03-conception/specifications/sfd/ | ISO/IEC/IEEE 29148:2018 |
| SPC-028 | J3 | majeur | tous | - | La SFG décrit les acteurs, les fonctions, les processus, les objets métier avec leur cycle de vie et la matrice de droits | 03-conception/specifications/sfg.md | bonne pratique |
| SPC-029 | J3 | majeur | tous | - | Chaque module a une plage unique d'identifiants de règles, un propriétaire et au plus quinze fonctions | 03-conception/specifications/sfg.md | bonne pratique |
| SPC-030 | J3 | majeur | tous | - | Chaque fonction est nommée par un verbe et un objet, cite ses acteurs et les exigences qu'elle couvre | 03-conception/specifications/sfg.md | bonne pratique |
| SPC-031 | J3 | bloquant | tous | - | Chaque module de la SFD se lit seul : plage, fonctions, acteurs, objets, glossaire et dépendances y figurent | 03-conception/specifications/sfd/ | bonne pratique |
| SPC-032 | J3 | bloquant | tous | - | Chaque règle de gestion énonce une condition, un effet, ses valeurs et unités, et porte un exemple vérifiable | 03-conception/specifications/sfd/ | bonne pratique ; Gherkin |
| SPC-033 | J3 | majeur | tous | - | Chaque fonction détaillée décrit le cas nominal et les exceptions : donnée invalide, droit insuffisant, tiers indisponible, abandon, double action | 03-conception/specifications/sfd/ | bonne pratique |
| SPC-034 | J3 | majeur | tous | - | Chaque cause d'erreur a un message au texte exact, une action possible pour l'utilisateur et une règle de rattachement | 03-conception/specifications/sfd/ | bonne pratique |
| SPC-035 | J3 | majeur | tous | comptes | Chaque rôle a ses droits par fonction, avec les conditions de propriété de la ressource et d'état de l'objet | 03-conception/specifications/sfd/ | bonne pratique |
| SPC-036 | J3 | majeur | tous | donnees-perso | Les champs de données personnelles sont signalés dans la SFD et relus par le délégué à la protection des données | 03-conception/specifications/sfd/ | RGPD, à valider |
| SPC-037 | J3 | majeur | tous | - | Les règles et écrans ont été croisés avec le cartographe des interactions et aucune règle manquante n'est ouverte | 03-conception/specifications/sfd/ | bonne pratique |
| SPC-038 | J3 | majeur | tous | integrations | Chaque interface externe a un contrat : protocole, authentification, limites, versionnement, exemples valides et invalides | 03-conception/specifications/specs-techniques.md | bonne pratique |
| SPC-039 | J3 | majeur | tous | - | Chaque traitement non interactif précise son déclencheur, sa volumétrie et sa reprise après échec | 03-conception/specifications/specs-techniques.md | bonne pratique |
| SPC-040 | J3 | majeur | tous | - | Les règles techniques sont des règles numérotées citant leur fonction ou exigence, et les valeurs paramétrables ont un responsable | 03-conception/specifications/specs-techniques.md | bonne pratique |
| SPC-041 | J3 | majeur | tous | - | Chaque exigence non fonctionnelle est citée par au moins un cas de test du cahier de recette | 03-conception/tests/cahier-de-recette.md | ISO/IEC 25010:2023 |
| SPC-042 | J3 | majeur | tous | - | La SFD et les spécifications techniques ont été relues par le testeur, le délégué aux données, l'architecte et l'architecte sécurité | 00-pilotage/audits/ | bonne pratique |
| SPC-043 | J4 | majeur | tous | - | Toute modification d'exigence après le cadrage est tracée par une décision au registre et répercutée jusqu'aux tests | 00-pilotage/registres/ | bonne pratique |
| SPC-044 | J5 | majeur | tous | - | Le procès-verbal de recette donne, pour chaque exigence prioritaire, le résultat de ses cas de test | 05-validation/pv-recette.md | CCAG-TIC 2021, art. 32 et 33 |
