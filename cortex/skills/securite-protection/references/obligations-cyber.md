# Obligations de cybersécurité : qui est concerné par quoi

Qualifier par écrit, pour chaque régime, « applicable ou non » avec le motif. État : 11 octobre 2026. Ce fichier prépare le travail du juriste et de l'auditeur : toute qualification est « à valider ».

## Sommaire
- Calendrier
- Qualification par régime
- Qui est concerné : cas types
- Exigences des acheteurs
- Méthode de qualification
- Pièges et contrôles
- Sources

## Calendrier

| Date | Fait |
|---|---|
| 31 mars 2025 | exigences nouvelles de PCI DSS 4.0.1 obligatoires |
| 17 janvier 2025 | DORA applicable |
| 10 décembre 2024 | CRA en vigueur |
| 11 juin 2026 | CRA : organismes notifiés |
| 16 mai 2026 | HDS v2.0 exigible (fin des 18 mois de transition) |
| 11 septembre 2026 | CRA : obligation de notification (article 14) |
| 11 décembre 2027 | CRA : obligations principales |
| 17 octobre 2024 | date limite de transposition de NIS2 ; en France, le projet de loi « résilience » n'est pas adopté au 11 octobre 2026 (examen à l'Assemblée retiré de l'ordre du jour le 6 octobre) |

Revoir ce calendrier chaque trimestre.

## Qualification par régime

| Régime | Qui est concerné | Obligations principales | Vérifier |
|---|---|---|---|
| NIS2 | entités de 18 secteurs : essentielles (au moins 250 personnes, ou chiffre d'affaires supérieur à 50 M€ et bilan supérieur à 43 M€) ; importantes (au moins 50 personnes, ou chiffre d'affaires et bilan supérieurs à 10 M€) | enregistrement, gestion des risques, déclaration d'incidents ; sanctions jusqu'à 2 % (essentielles) ou 1,4 % (importantes) du chiffre d'affaires mondial | fournisseurs d'infrastructures numériques et de services TIC : règlement d'exécution (UE) 2024/2690, pas le socle national ; seuils à valider |
| DORA | entités financières (21 types) | gestion des risques TIC, incidents, tests de résilience, tiers ; les prestataires TIC de la finance restent sous NIS2 et reçoivent des clauses contractuelles de leurs clients | tests avancés (TLPT) et fréquences : à vérifier |
| Cyber Resilience Act | produits avec éléments numériques mis sur le marché de l'UE (application mobile, agent installé, SDK, produit sur site) | sécurité dès la conception, gestion des vulnérabilités, notification 24 h et 72 h, support défini | le SaaS pur est a priori hors champ, mais le service peut intégrer des composants distribués ; produits mis sur le marché avant le 11 décembre 2027 : sources divergentes sur l'article 69, à trancher ; guidance de la Commission du 27 juillet 2026 |
| PCI DSS 4.0.1 | toute entité qui stocke, traite ou transmet des données de cartes | selon le mode d'encaissement (questionnaire d'auto-évaluation ou audit) ; scripts de la page de paiement ; tests de segmentation | numérotation des exigences (6.4.2, 6.4.3, 11.6.1, 12.10) : non relue, à vérifier |
| HDS v2.0 | hébergeur de données de santé pour des tiers | certification alignée sur ISO 27001:2022 | seuls les hébergeurs certifiés v2.0 peuvent héberger ces données |
| RGPD | traitement de données personnelles | sécurité du traitement, notification des violations (article 33) | traité par le pôle Juridique, textes à relire |

Si l'une des conditions du tableau est incertaine, écrire « à qualifier » et saisir le juriste : une exclusion jugée « hors sujet » sans qualification écrite est un défaut fréquent.

## Qui est concerné : cas types

| Projet | Régimes probables |
|---|---|
| Site vitrine | RGPD (formulaires, mesure d'audience), hygiène de base |
| E-commerce | RGPD, PCI DSS 4.0.1 selon le mode d'encaissement ; NIS2 s'il exploite une place de marché (fournisseur numérique) ou relève d'un autre secteur couvert |
| Application mobile | RGPD, magasins d'applications ; CRA à qualifier pour l'application |
| SaaS B2B | NIS2 probable (cloud, services TIC), clauses DORA répercutées par les clients financiers, HDS si données de santé, ISO 27001 ou SOC 2 comme preuves |
| ERP | selon les clients et les secteurs ; CRA si la solution est installée chez le client |
| Niche, micro-SaaS | RGPD ; exigences des acheteurs plus qu'obligations propres |

Appliquer ReCyF (v2.5 du 17 mars 2026, document de travail de l'ANSSI) dès maintenant : il n'est pas obligatoire par défaut, mais il est invocable en cas de contrôle et attendu par les clients. Il relie ses objectifs de sécurité à l'article 21.2 de NIS2.

## Exigences des acheteurs

| Preuve demandée | Contenu | Quand l'envisager |
|---|---|---|
| ISO/IEC 27001:2022 (modifiée 2024) | système de management de la sécurité certifié ; catalogue de contrôles ISO 27002:2022 | grands comptes, appels d'offres, HDS |
| SOC 2 | rapport d'un auditeur sur les contrôles de service (critères de confiance) | clients nord-américains ; détails à vérifier |
| Questionnaires de sécurité | réponses déclaratives | tout acheteur B2B |
| Rapport de test d'intrusion récent | par prestataire qualifié | souvent exigé |
| Liste des sous-traitants, politique de vulnérabilités | contrat | grand compte |

Préparer ce dossier de preuves tôt : le délai de certification se compte en mois. SecNumCloud n'a pas été relu : à vérifier si un client public l'exige.

## Méthode de qualification

1. Reprendre taille, secteur, pays, clients et nature des données (fiche projet, cartographie des données).
2. Remplir le tableau « Régimes applicables » de `analyse-risques-securite.md` : régime, applicable ou non ou à qualifier, motif, source, date.
3. Pour chaque régime applicable, déduire les contrôles `SEC-` conditionnés (étiquettes `paiement`, `sante`, `finance`, `grand-compte`, `stores`, `ue`).
4. Faire valider par le juriste ou par l'auditeur qualifié.

## Pièges

- Attendre la transposition de NIS2 pour agir.
- Oublier le CRA pour une application mobile ou un agent installé chez le client.
- Croire que le prestataire de paiement décharge de toute obligation PCI DSS.
- Héberger des données de santé chez un hébergeur non certifié.
- Citer une date du CRA sans préciser laquelle (notification ou obligations principales).

## Contrôles avant de rendre

- Chaque régime du tableau a une conclusion écrite et datée.
- Chaque conclusion est marquée « à valider » avec le professionnel désigné.
- Les dates sont accompagnées de leur état au jour de la rédaction.

## Sources

- ANSSI, NIS2 : https://messervices.cyber.gouv.fr/nis2
- ANSSI, directive NIS 2 : https://cyber.gouv.fr/reglementation/cybersecurite-systemes-dinformation/directives-nis-nis2-et-dispositif-saiv/directive-nis-2/
- Règlement d'exécution (UE) 2024/2690 : https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=OJ:L_202402690
- Commission européenne, résumé du CRA : https://digital-strategy.ec.europa.eu/en/policies/cra-summary
- ANS, certification HDS : https://esante.gouv.fr/actualites/certification-hds-six-mois-pour-etre-pret
- PCI SSC, PCI DSS 4.0.1 : https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1
- ISO/IEC 27001:2022 : https://www.iso.org/standard/88435.html
