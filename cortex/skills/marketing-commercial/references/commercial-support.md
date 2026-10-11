# Commercial et service client

Cette référence couvre la vente à des professionnels, la réponse aux appels d'offres, les partenaires, l'accompagnement du client et la rétention. Ce sujet est peu sourcé : la plupart des règles ci-dessous sont des inférences de méthode, marquées comme telles, à adapter au projet.

## Sommaire
1. Quand ce pôle intervient
2. Processus de vente
3. Qualification
4. Démonstration et preuve de concept
5. Appels d'offres
6. Partenaires et revendeurs
7. Accompagnement client et rétention
8. Gabarit de `plan-commercial.md`
9. Pièges et contrôles

## 1. Quand ce pôle intervient

| Type de projet | Vente | Service |
|---|---|---|
| SaaS B2B, ERP, grand compte | processus complet | support à niveaux, succès client |
| Site d'entreprise | prospects à qualifier | réponse aux demandes |
| E-commerce, mobile, niche | rarement de vente directe | support, avis, rétention |

Sans acheteur professionnel, limiter le plan commercial au service client et aux partenariats. Attention : 61 % des acheteurs B2B préfèrent un achat sans commercial (632 acheteurs, Gartner 2025 ; un autre document Gartner cite 75 %, millésime non vérifié). Prévoir donc un parcours en libre-service complet, avec contact humain à la demande.

## 2. Processus de vente

Étapes types (inférence) : prospect → qualifié → démonstration → proposition → négociation → signature → mise en service. Pour chaque étape : critère d'entrée, critère de sortie, propriétaire, durée cible, document produit. Un compte stratégique reçoit un plan de compte : rôles du comité d'achat, références sectorielles, valeur chiffrée, intégrateurs.

## 3. Qualification

| Cadre | Usage |
|---|---|
| BANT : budget, autorité, besoin, délai | contrôle initial léger en entrée |
| MEDDICC | qualification continue dès l'opportunité : métriques, acheteur économique, critères de décision, processus de décision, identification du besoin, champion, concurrence |

MEDDICC suit tout le cycle, contrairement à BANT (source de formation intéressée : MEDDICC.com). Règle : BANT en entrée, MEDDICC dès l'opportunité. Une opportunité sans champion identifié ni processus de décision connu reste en qualification. Revue des opportunités sur grille MEDDICC à J+60.

## 4. Démonstration et preuve de concept

- Démonstration construite sur le cas d'usage du champion, avec ses données fictives réalistes, jamais celles d'un autre client.
- Preuve de concept : critères de succès écrits avant le début, durée bornée, périmètre limité, responsable côté client, décision attendue à date fixe.
- Ne montrer que des fonctions existantes ; ce qui est prévu est étiqueté « feuille de route, sans engagement ».
- Aucun chiffre d'usage ni référence client non autorisée dans les supports.

## 5. Appels d'offres

1. Décider du **go ou no-go** par la grille MEDDICC : connaît-on le décideur ? Le cahier des charges est-il écrit pour un concurrent ? Le délai de réponse permet-il une réponse honnête ?
2. Découper les exigences, répondre point par point : conforme, partiel, non conforme, sur mesure.
3. Chiffrer avec le contrôleur financier ; engagement de niveau de service relu par le juriste (à valider).
4. Pièces administratives et références : vérifier validité et dates. Règles de la commande publique : à vérifier avec le juriste.
5. Jamais d'engagement contractuel envoyé par un agent : l'utilisateur envoie.

## 6. Partenaires et revendeurs

Surtout utiles pour les ERP : intégrateurs et revendeurs. Définir : critères de sélection, remise ou commission, formation et certification, zone, exclusivité éventuelle (décision de type 1), propriété de la relation client, partage des données, support de niveau 1 ou 2. Contrat de partenariat : à valider par le juriste.

## 7. Accompagnement client et rétention

| Élément | Règle (inférence) |
|---|---|
| Support | niveaux N1 à N3 ; délai de première réponse et de résolution par priorité (SLA) ; canaux et délais publiés avant J0 |
| Base de connaissances | alimentée par les tickets ; minimum viable prête à J-14 |
| Mesures | CSAT après chaque ticket et après l'intégration ; NPS après au moins 30 jours d'usage ; effort client (CES) pour les parcours difficiles |
| Rétention | cohortes par semaine d'acquisition ; alertes de baisse d'usage ; relance consentie |
| Références | demande d'avis et de référence vers J+45 ; jamais d'avis acheté ni rédigé |

CSAT mesure la satisfaction sur une interaction (amélioration à court terme) ; NPS mesure la loyauté durable et se compare aux concurrents. Les deux se complètent. Lien avec le pôle Lancement : le plan de support est écrit par `responsable-support-formation` ; ce fichier fixe seulement ce que la vente promet au client.

## 8. Gabarit de `plan-commercial.md`

```markdown
# Plan commercial — <projet>

## Synthèse
<12 lignes au plus : modèle de vente, segments, processus, partenaires, support promis, objectifs à J+90, décisions>

## Modèle de vente
<libre-service, vente assistée, vente directe, partenaires ; justification>

## Segments et comités d'achat
<rôles, messages, objections>

## Processus de vente
| Étape | Entrée | Sortie | Propriétaire | Durée cible |
|---|---|---|---|---|

## Qualification
<BANT en entrée, MEDDICC dès l'opportunité, critères d'abandon>

## Démonstration et preuve de concept
<trame, critères de succès, durée>

## Appels d'offres
<critères go ou no-go, trame de réponse, pièces>

## Partenaires
<types, conditions, contrats à valider>

## Service client et rétention
<niveaux, délais, base de connaissances, CSAT, NPS, rétention>

## Objectifs et indicateurs
<pipeline, cycle, taux de gain, rétention>

## Conformité
<prospection, contrats, engagements : relu par le juriste le …, à valider>

## Risques et hypothèses
```

## 9. Pièges et contrôles

- Un seul interlocuteur dans un compte ; conflit du comité ignoré (74 % des équipes B2B, Gartner 2025).
- Équipe commerciale recrutée trop tard (cas Twilio).
- Parcours sans commercial négligé.
- Support, base de connaissances et plan de crise absents à J0.
- Promesse de service plus large que ce que le support peut tenir.
- Avant de rendre : processus avec critères de sortie, grille MEDDICC, SLA cohérents avec le plan de support, contrats signalés « à valider ».

## Sources

- MEDDICC.com, MEDDICC contre BANT (source de formation, intéressée)
- Gartner, communiqué du 25/06/2025 : 61 % des acheteurs B2B préfèrent un achat sans commercial
- Gartner, communiqué du 7 mai 2025 : comités d'achat et conflit
- Qualtrics, HubSpot, Zendesk : CSAT, NPS, effort client
- First Round Review, leçons de Twilio
