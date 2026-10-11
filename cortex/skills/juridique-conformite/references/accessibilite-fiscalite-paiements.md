# Accessibilité légale, fiscalité et paiements

Obligations d'accessibilité, TVA du commerce en ligne, facturation électronique, déclarations des plateformes, services de paiement, encaissement pour compte de tiers, paiement fractionné. État : octobre 2026. Ce livrable prépare le travail d'un expert-comptable, d'un avocat et d'un auditeur d'accessibilité ; il ne vaut pas conseil juridique ou fiscal. Montants et taux non sourcés : « à vérifier ».

## Sommaire
- Accessibilité
- TVA et douane
- Facturation électronique
- DAC7 et caisse
- Paiements
- Gabarit
- Pièges
- Sources

## Accessibilité

| Point | Contenu | Source |
|---|---|---|
| Directive (UE) 2019/882 (EAA) | Applicable depuis le **28 juin 2025** au commerce en ligne, aux services bancaires, de communication, audiovisuels et de transport ; micro-entreprises de services exemptées | DGCCRF |
| Transposition française | Code de la consommation (D412-50, D412-51, L412-13) ; ordonnance n° 2023-859 du 6 septembre 2023 | Légifrance (articles à confirmer) |
| Seuil | La page DGCCRF évoque « 10 salariés et plus et plus de 2 M€ de CA » : formulation différente de l'exemption légale des micro-entreprises, **à valider** | notes |
| Sanctions rapportées | Contravention 7 500 € (15 000 € en récidive), astreinte jusqu'à 3 000 € par jour, amende jusqu'à 75 000 € | source secondaire (Access42), à vérifier |
| Référentiel | RGAA 4.1.2 contre 5, WCAG 2.2, EN 301 549 : versions non vérifiées. Viser WCAG 2.2 AA et le RGAA en vigueur | à vérifier |

Régime public (RGAA obligatoire) et régime privé (EAA, Code de la consommation) diffèrent : ne pas les confondre. Une micro-entreprise de services est exemptée, mais grands comptes et commande publique l'exigent par contrat. Pour un e-commerce ou une application B2C, prévoir audit, déclaration d'accessibilité et canal de retour. Contenu technique : `maquettes-parcours/references/accessibilite.md`. Aux États-Unis (`us`), ADA et Section 508 : à vérifier.

## TVA et douane

| Sujet | Règle | Action |
|---|---|---|
| Guichet unique OSS/IOSS | Depuis le 1er juillet 2021 : services B2C, ventes à distance intra-UE, biens importés ≤ 150 € ; seuil unique de **10 000 €** | S'immatriculer selon les flux, suivre le seuil |
| TVA par pays de destination | Taux du pays du consommateur au-delà du seuil | Paramétrer boutique et ERP par pays |
| Droit forfaitaire douanier | **3 €** par ligne tarifaire sur les colis < 150 € depuis le **1er juillet 2026**, sans plafond, jusqu'à la plateforme de données douanières ; fin de la franchise prévue en 2028 | Intégrer au prix rendu et à la marge |
| Taxe sur les services numériques | LF 2026 = loi n° 2026-103 du 19 février 2026 ; doublement de 3 % à 6 % voté en première lecture ; **taux définitif non confirmé** | Ne rien chiffrer sans vérification ; grands acteurs seulement (seuils à vérifier) |

## Facturation électronique

- **Calendrier :** depuis le **1er septembre 2026**, toutes les entreprises assujetties peuvent recevoir ; grandes entreprises et ETI émettent et font l'e-reporting ; PME et micro-entreprises le **1er septembre 2027**.
- **Tailles :** grande entreprise ≥ 5 000 salariés, ou CA > 1 500 M€ et/ou bilan > 2 000 M€ (« ou » chez Service-Public, « et » chez la DGFiP : à valider) ; ETI 250 à 4 999 salariés ; PME < 250 salariés et CA < 50 M€ ou bilan < 43 M€ ; micro < 10 personnes et CA ou bilan ≤ 2 M€ ; seuil franchi après deux exercices consécutifs.
- **Mécanique :** émission, transmission, réception et conservation par une plateforme agréée (ou solution compatible raccordée) ; un PDF ordinaire n'est plus une facture électronique ; quatre mentions nouvelles aux mêmes dates (liste à relever dans la fiche DGFiP).
- **Base légale :** CGI art. 289 bis, 289 E, 290, 290 A ; annexe II art. 242 nonies A ; amende par facture (art. 1737) avec mise en demeure de trois mois pour défaut de plateforme de réception (1737 IV bis) ; e-reporting (art. 1788 D). Montants des amendes : de mémoire, à confirmer. Formats (Factur-X, UBL, CII), e-reporting B2C : à vérifier.
- **Produit :** un SaaS de facturation ou un ERP vendu en France s'interconnecte à une plateforme agréée ou laisse le client la choisir.

## DAC7 et caisse

- **DAC7 :** les opérateurs de plateforme déclarent chaque année ; campagne 2026 sur les opérations 2025 (cahier des charges v1.6 du 05/11/2025) ; information fiscale des utilisateurs, CGI art. 242 bis. Collecter les données vendeurs dès l'inscription. Seuils : à vérifier.
- **Logiciel de caisse (CGI art. 286, I, 3° bis) :** obligatoire pour l'assujetti vendant à des particuliers et enregistrant les règlements par logiciel ; preuve par certificat d'organisme accrédité ou attestation individuelle de l'éditeur. Attestation supprimée au 16/02/2025 (LF 2025, art. 43) puis rétablie (LF 2026, loi n° 2026-103, art. 125). Dans un ERP, seule la fonction de caisse est visée ; l'intégrateur qui altère le dispositif devient « éditeur » ; logiciel développé pour soi : certificat seul (BOFiP 25/03/2026).

## Paiements

| Sujet | Règle | Décision |
|---|---|---|
| DSP2 | En vigueur ; SCA et 3-D Secure 2 : détail non vérifié | PSP agréé qui gère la SCA |
| PSD3 et PSR | Accord provisoire 27/11/2025 ; textes agréés publiés le 23/04/2026 ; publication au JOUE non confirmée ; application cible 2028 (18 ou 21 mois après entrée en vigueur selon les sources) | Veille datée |
| Crédit à la consommation | Directive (UE) 2023/2225 ; ordonnances n° 2025-880 (3 septembre 2025) et du 2 décembre 2025 ; **20 novembre 2026** ; plafond 100 000 € ; plancher de 200 € supprimé ; paiements fractionnés et mini-crédits inclus | Avant cette date, établir si le PSP est prêteur ou si le marchand devient intermédiaire de crédit |
| Marketplace | Ne pas encaisser pour compte de tiers sans statut ou PSP agréé (agent ou établissement de paiement) ; exclusion d'agent commercial : à vérifier | PSP de marketplace avec KYC intégré ; décision de type 1 |
| Algérie (`dz`) | Paiement via plateformes de banques agréées et Algérie Poste (loi 18-05, art. 27-29) | Voir `politique-reglementaire-international.md` |

## Gabarit (section de conformite-reglementaire.md)

```markdown
## Fiscalité et paiements
| ID | Obligation | Texte et date | Concerné ? | Action | Échéance | Statut |
|---|---|---|---|---|---|---|
| FIS-0nn | Réception des factures électroniques | calendrier du 01/09/2026 | oui | choisir une plateforme agréée | 01/09/2026 | à valider |
```

## Pièges fréquents

- Croire que l'e-facture ne concerne que l'émission : la réception est obligatoire pour tous depuis le 01/09/2026.
- Oublier OSS et le droit de 3 € dans les prix rendus.
- Intégrateur ERP qui modifie la caisse sans réattester.
- Proposer 3x/4x sans qualifier le statut avant le 20/11/2026.
- Se fier à un blog pour un montant d'amende ou un taux de TSN.

## Sources

- Directive (UE) 2019/882 ; DGCCRF (économie.gouv.fr/node/3238381) ; Légifrance, Code de la consommation.
- economie.gouv.fr, facturation électronique ; Service-Public F23208 et A15683 ; Guide DGFiP de la facturation électronique.
- impots.gouv.fr, guichet unique OSS/IOSS ; Conseil de l'UE, petits colis.
- BOFiP BOI-TVA-DECLA-30-10-30 (25/03/2026) ; cahier des charges DAC7 v1.6.
- Directive (UE) 2023/2225 ; EP Legislative Train sur PSD3/PSR.
