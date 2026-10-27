# Infrastructure, hébergement et chaîne de livraison

Concevoir hébergement, environnements, infrastructure as code, chaîne de livraison, observabilité et continuité. État : octobre 2026. Plan de bascule, go/no-go et surveillance renforcée relèvent du pôle Lancement : ici on conçoit, on ne met pas en production.

## Sommaire
1. Méthode
2. Hébergement : critères et options
3. Modèles d'exécution
4. Réseau, certificats, dimensionnement
5. Environnements et infrastructure as code
6. Intégration et déploiement continus
7. Observabilité
8. Continuité
9. Coût et sobriété
10. Gabarit de `infrastructure.md`
11. Pièges et contrôles avant de rendre

## 1. Méthode

1. Reprendre les exigences non fonctionnelles chiffrées et la classification des données. Sans SLO, RTO et RPO par parcours métier, ne rien dimensionner : les demander.
2. Instruire au moins deux options d'hébergement sur les quatre critères du §2 ; la décision est de type 1, elle passe au comité d'architecture.
3. Choisir le modèle d'exécution (§3), puis écrire environnements, infrastructure as code et chaîne de livraison.
4. Fixer SLO, alertes et stratégie de reprise, chiffrer l'exploitation sur trois à cinq ans pour le contrôleur financier.

## 2. Hébergement : critères et options

| Critère | Question | Piège |
|---|---|---|
| Souveraineté | quelle garantie juridique et technique, pour quelles données ? | confondre « données en UE », « cloud souverain », SecNumCloud et SEAL |
| Coût | total sur 3 à 5 ans, sortie comprise | offres qualifiées environ 15 à 20 % plus chères (presse, S3NS) |
| Compétences | qui exploite, avec quelle formation ? | premier obstacle Kubernetes : le changement culturel (47 %, CNCF) |
| Réversibilité | données, IaC et secrets repartent-ils ? | le Data Act réduit le coût de sortie, pas la réécriture des services propriétaires |

| Notion de souveraineté | Ce qu'elle garantit | Point d'attention |
|---|---|---|
| SecNumCloud (ANSSI, référentiel v3.2) | qualification de 3 ans, audits annuels, immunité aux lois extra-européennes | vérifier le périmètre exact sur la liste ANSSI ; héberger sur une offre qualifiée ne qualifie pas le service |
| SEAL (Cloud Sovereignty Framework, Commission) | niveaux SEAL-0 à SEAL-4, seuil SEAL-2 du marché européen | autre échelle que SecNumCloud : non équivalents |
| Offres « souveraines » d'hyperscaler | par exemple entités de droit européen, exploitation par résidents UE | label commercial : lire le contrat ; qualification SecNumCloud non acquise d'office |

Qualifications en cours (S3NS : PREMI3NS qualifié 3.2 ; Bleu : non qualifié au 09/10/2026, cible décembre 2026) : **jamais sur le chemin critique**. Autres hébergeurs, PaaS, sur site et hybride : « à vérifier ».

Data Act, art. 29 : plus aucun frais de changement de fournisseur à compter du 12/01/2027 (frais réduits au coût direct jusque-là) ; frais standard, pénalités proportionnées et sortie d'usage en multi-cloud restent facturables. Le contrat chiffre ces trois postes. Lecture contractuelle « à valider » par le juriste.

## 3. Modèles d'exécution

Synthèse d'expert, non sourcée ; à confirmer par la tranche verticale.

| Situation | Modèle | Pourquoi |
|---|---|---|
| Petite équipe, produit simple, trafic modéré | PaaS ou conteneurs managés | exploitation minimale |
| Nombreux services, équipe plateforme, exigence de portabilité | Kubernetes managé (82 % des utilisateurs de conteneurs en production, CNCF) | socle dominant, mais coût humain réel |
| Charges par à-coups | serverless | paiement à l'usage ; verrouillage plus fort |
| Contrainte réglementaire ou d'existant | machines virtuelles, sur site ou hybride | maîtrise ; exploitation lourde |

Kubernetes : dernière version 1.37 (26/08/2026) ; planifier les montées. Ingress NGINX : retrait annoncé pour mars 2026, ni version ni correctif ensuite : migrer vers Gateway API ou un contrôleur maintenu ; confirmer l'exécution effective du retrait.

## 4. Réseau, certificats, dimensionnement

- Certificats : validité maximale 200 jours depuis le 15/03/2026, 100 jours le 15/03/2027, 47 jours le 15/03/2029. ACME obligatoire en pratique, chaîne servie surveillée de l'extérieur.
- Dimensionnement : trafic de lancement et projection à six mois, test de charge de bout en bout, redondance N+2, marge de croissance 10×. Les pics de lancement montent jusqu'à 15× les estimations et la surcharge n'est pas linéaire.
- Clients et SDK : backoff exponentiel avec jitter, aucun retry sur les erreurs 4xx.
- Aucun point unique de défaillance ; dépendances tierces en dégradation gracieuse.

## 5. Environnements et infrastructure as code

| Environnement | Rôle | Règle |
|---|---|---|
| dev | développement | éphémère, données fictives |
| test | tests automatisés | éphémère par demande de fusion si possible |
| recette | campagne du cahier de recette | version figée, données représentatives anonymisées |
| préproduction | rejoue charge, déploiement et restauration | topologie identique à la production |
| production | service réel | accès nominatifs, rien n'y est manuel |

Aucune donnée de production non anonymisée hors production. Toute l'infrastructure est en code versionné et relu. Terraform ou OpenTofu : décision de licence et de gouvernance (HashiCorp est passé à la BUSL le 10/08/2023) ; motiver le choix. GitOps avec détection de dérive (Argo CD majoritaire chez les utilisateurs déclarés de la CNCF : biais de sélection, pas une part de marché). La promotion entre environnements est le point faible : l'outiller, jamais de script manuel. Secrets hors dépôt, coffre, rotation automatisée, moindre privilège (pratique usuelle, non étayée ici).

## 6. Intégration et déploiement continus

- Un artefact unique, versionné et lié à un commit, promu d'un environnement à l'autre sans reconstruction.
- Étapes bloquantes : format, lint, types, tests, scans (`references/normes-developpement.md`). Identifiants de la chaîne éphémères, à moindre privilège.
- Déploiement progressif : canary, puis région, puis global, retour arrière automatique sur alarme ; feature flags sur 1 à 10 % des utilisateurs pour dissocier déploiement et mise en service.
- Migrations de schéma rétrocompatibles et découplées du déploiement (expand puis contract), retour arrière exercé.
- Métriques DORA : débit (délai de livraison, fréquence de déploiement, temps de restauration) et instabilité (taux d'échec, taux de reprise). Mesurer par service, en tendance, sans cible imposée (loi de Goodhart). Ne pas confondre avec le règlement (UE) 2022/2554, aussi appelé DORA.

## 7. Observabilité

OpenTelemetry pour traces, métriques et journaux ; le signal Profiles est en alpha depuis le 26/03/2026 : aucune dépendance critique. Alertes sur les symptômes utilisateur, fondées sur les SLO. Point de départ pour un SLO de 99,9 % :

| Action | Fenêtres longue et courte | Burn rate | Budget consommé |
|---|---|---|---|
| Page | 1 h et 5 min | 14,4 | 2 % |
| Page | 6 h et 30 min | 6 | 5 % |
| Ticket | 3 j et 6 h | 1 | 10 % |

Recalibrer sur le SLO réel ; un seuil fixe est source de bruit. Superviser la supervision. Incident : Incident Commander, responsable des communications, responsable des opérations ; playbooks et un exercice avant lancement ; post-mortems sans blâme, actions avec échéance au backlog. Page de statut hébergée hors de l'infrastructure surveillée.

## 8. Continuité

| Stratégie | RPO | RTO | Coût |
|---|---|---|---|
| Sauvegarde-restauration | heures | jusqu'à 24 h | le plus bas |
| Pilot light | minutes | dizaines de minutes | moyen |
| Warm standby | secondes | minutes | élevé |
| Actif-actif multi-région | proche de 0 | proche de 0 | le plus élevé, le plus complexe |

Le RPO et le RTO cibles dictent le choix ; l'actif-actif seulement si le métier l'exige. La réplication ne protège pas de la corruption sans restauration à un instant donné. ANSSI-BP-100 v1.1 (27/11/2025) : trois copies dont une hors ligne, serveurs de sauvegarde hors domaine AD de production, procédure de restauration écrite et testée, ordre de remise en service tenant compte de DNS, NTP et annuaire, sauvegarde de l'infrastructure de sauvegarde et des clés. Tests : restauration mensuelle ou trimestrielle, reprise après sinistre semestrielle ou annuelle, game days hors production d'abord, une région à la fois ensuite.

## 9. Coût et sobriété

Allouer les coûts par produit et par environnement, avec budgets et alertes d'anomalie avant lancement (FinOps Framework 2025). RGESN 2024 (78 critères, Arcep et Arcom avec l'ADEME) : évaluer hébergement et architecture ; caractère obligatoire « à vérifier ».

## 10. Gabarit de `infrastructure.md`

```markdown
# Infrastructure — <projet>
## Synthèse
Hébergeur retenu et ADR, modèle d'exécution, environnements, SLO/RTO/RPO, stratégie de reprise, coût annuel, points « à vérifier ».
## Hébergement
Charges classées, options notées, plan de sortie.
## Exécution et réseau
## Environnements
| Environnement | Rôle | Données | Topologie | Accès |
|---|---|---|---|---|
## Infrastructure as code et secrets
## Chaîne d'intégration et de déploiement
## Observabilité
| Parcours | SLI | SLO | Alertes | Propriétaire |
|---|---|---|---|---|
## Continuité
| Application | RPO | RTO | Stratégie | Dernier test |
|---|---|---|---|---|
## Coûts et sobriété
```

## 11. Pièges et contrôles avant de rendre

- Planning bâti sur une qualification attendue ; Ingress NGINX laissé en production ; certificats gérés à la main.
- Sauvegardes dans le domaine d'administration de production, jamais restaurées ; réplication prise pour sauvegarde.
- Avant de rendre : SLO, RTO, RPO issus du cahier des charges ; deux options d'hébergement ; plan de sortie ; « à vérifier » sur tout point non étayé.

## Sources

- ANSSI, SecNumCloud : https://cyber.gouv.fr/enjeux-technologiques/cloud/faq-qualification-secnumcloud/
- Commission, Cloud Sovereignty Framework : https://commission.europa.eu/news-and-media/news/commission-advances-cloud-sovereignty-through-strategic-procurement-2026-04-17_en
- Data Act, art. 29 : https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854
- Kubernetes, Ingress NGINX : https://kubernetes.io/blog/2026/01/29/ingress-nginx-statement/
- Google SRE, lancement et alertes : https://sre.google/sre-book/launch-checklist/ ; https://sre.google/workbook/alerting-on-slos/
- DORA métriques : https://dora.dev/guides/dora-metrics/
- ANSSI-BP-100 v1.1 : https://messervices.cyber.gouv.fr/documents-guides/anssi_fondamentaux_sauvegarde_systemes_dinformation_v1.1.pdf
