# Politique, réglementation sectorielle et international

Facteurs politiques et réglementaires qui peuvent interdire, retarder ou renchérir un projet : sanctions, exportations, souveraineté, commande publique, secteurs réglementés, Algérie, Maroc, Tunisie ; méthode de veille et de pré-diagnostic par pays. État : octobre 2026. Sanctions, export, souveraineté et commande publique ne sont pas sourcés : ces lignes sont des connaissances établies **à vérifier**. Ce livrable prépare le travail d'un avocat local et ne vaut pas conseil juridique.

## Sommaire
- Méthode de pré-diagnostic par pays
- Sanctions et exportations
- Souveraineté et commande publique
- Secteurs réglementés
- Algérie
- Maroc et Tunisie
- Veille réglementaire
- Gabarit
- Sources

## Méthode de pré-diagnostic par pays

1. Pour chaque pays visé, répondre à six questions : le projet y est-il licite (activité, produits) ? Faut-il un établissement local ? Quelle loi s'applique au contrat et au consommateur ? Où héberger ? Comment encaisser et rapatrier ? Quelles données peuvent sortir ?
2. Classer le pays : **ouvert** (règles UE applicables), **conditionné** (formalités locales), **strict** (hébergement, paiement ou établissement imposés), **fermé** (activité interdite ou sanctionnée).
3. Un pays « strict » ou « fermé » est une décision de type 1 : l'`utilisateur` tranche, `juriste-numerique` peut s'opposer.
4. Demander l'avis d'un avocat local pour tout pays hors France et UE, avant J3.

## Sanctions et exportations

| Sujet | Règle (connaissance établie, à vérifier) | Garde-fou |
|---|---|---|
| Sanctions UE | Règlements du Conseil publiés au JOUE ; gel d'avoirs, interdiction de mise à disposition de fonds et de services | Filtrer clients, fournisseurs et bénéficiaires effectifs contre les listes officielles à l'inscription et périodiquement |
| Sanctions américaines (OFAC) | Portée extraterritoriale possible dès qu'un lien américain existe (dollar, services, composants) | Évaluer le lien américain avec l'avocat ; clause de conformité dans les contrats |
| Biens à double usage | Règlement (UE) 2021/821 : certains logiciels et techniques, dont des fonctions cryptographiques, peuvent exiger une autorisation | Cartographier les fonctions cryptographiques exportées ; déclaration ou autorisation selon l'avis du conseil |
| Embargos et pays à risque | Variables selon les années | Liste des pays exclus écrite dans les CGV et les contrôles d'inscription |
| Sanction pénale | Code des douanes art. 459 (à vérifier) | Voir `penal-responsabilites.md` |

## Souveraineté et commande publique

- **Souveraineté du cloud :** qualification SecNumCloud de l'ANSSI, label « cloud de confiance », schéma européen de certification cloud (EUCS) : statuts et exigences à vérifier. Exigée par des clients publics et opérateurs sensibles ; décision d'hébergement de type 1.
- **Dépendances et lois extraterritoriales :** risque de dépendance à un fournisseur non européen (CLOUD Act américain : à vérifier). Parades : clause de changement de loi, veille datée, hébergeur substituable, réversibilité (Data Act).
- **Commande publique :** Code de la commande publique (articles à vérifier) ; accessibilité numérique (RGAA obligatoire pour le secteur public), sécurité (référentiel de l'État, qualifications), souveraineté, clauses de réversibilité, marchés publics de moins de 40 000 € (seuil à vérifier). Étiquette `secteur-public`.
- **Instabilité politique observée :** tensions commerciales UE/États-Unis (TSN et droits de douane), réformes qui changent de calendrier (attestation de caisse supprimée en 2025 puis rétablie en 2026 ; calendrier de PSD3 divergent), contrôle accru des colis (droit de 3 € depuis le 01/07/2026).
- **Plateformes :** règlement sur les marchés numériques (DMA), conditions des magasins d'applications, Digital Fairness Act en projet : à vérifier. Voir `ia-plateformes.md`.

## Secteurs réglementés

| Secteur | Autorité ou régime (à vérifier) | Conséquence |
|---|---|---|
| Services financiers, paiement, crypto-actifs | ACPR, AMF ; agrément ; règlement MiCA | Agrément ou partenariat agréé avant lancement |
| Santé, pharmacie en ligne, dispositifs médicaux | Ministère, ANS, ordres professionnels ; hébergeur de données de santé certifié ; règlement sur les dispositifs médicaux | Hébergement certifié, qualification du logiciel (voir `international-donnees.md`) |
| Jeux d'argent | ANJ en France ; agrément | Interdit sans agrément ; interdit en Algérie |
| Alcool, tabac | Restrictions de vente à distance | Contrôle d'âge, interdiction en Algérie |
| Formation, éducation | Certifications et déclaration d'activité | À vérifier |
| Communications électroniques, audiovisuel | Arcep, Arcom | À vérifier |

Un site relevant d'une activité autorisée indique l'autorité d'autorisation dans les mentions légales (Service-Public F31228).

## Algérie (`dz`)

Loi n° 18-05 du 10 mai 2018 sur le commerce électronique (JORADP, fascicule n° 28). **La version arabe fait foi** ; l'extraction française disponible est automatisée : recouper.

| Sujet | Règle | Garde-fou |
|---|---|---|
| Champ (art. 2) | Loi algérienne si une partie est algérienne, résidente légale ou personne morale algérienne, ou si le contrat est conclu ou exécuté en Algérie | Un site étranger ciblant l'Algérie reste exposé |
| Interdits (art. 3, 5) | Jeux de hasard, paris, loteries, alcool, tabac, produits pharmaceutiques, atteintes à la propriété intellectuelle, biens exigeant un acte authentique ; matériels sensibles et défense nationale | Catalogue filtré, contrôle à la mise en ligne |
| Établissement (art. 8-9) | Inscription au registre du commerce ou de l'artisanat ; site hébergé en Algérie sous « .com.dz » avec authentification ; fichier national des e-fournisseurs ; dépôt du nom de domaine au CNRC | Hébergement local ; ne pas confondre « .dz » et « .com.dz » |
| Offre et commande (art. 10-13) | NIF, RC, prix TTC, livraison, CGV, garanties ; confirmation explicite sans champ orientant le choix ; contrat électronique | Écrans de commande dédiés |
| Exécution (art. 19-26) | Copie du contrat, facture, retour sous 4 jours ouvrables en cas de retard ou non-conformité, remboursement sous 15 jours, pas de commande hors stock, registre des transactions transmis au CNRC, données minimales et consenties | Règles de gestion dédiées |
| Paiement (art. 27-29) | Plateformes exploitées exclusivement par banques agréées et Algérie Poste ; certification électronique ; contrôle de la Banque d'Algérie | PSP étranger incompatible a priori : à valider |
| Sanctions (art. 37-44, 49) | 200 000 à 1 000 000 DA et fermeture de 1 à 6 mois (art. 3) ; 500 000 à 2 000 000 DA et radiation (art. 5) ; 50 000 à 500 000 DA avec suspension de l'accès à la plateforme de paiement (art. 11-12) ; 20 000 à 200 000 DA (art. 25) ; suspension du nom de domaine ; mise en conformité sous 6 mois pour les acteurs existants (art. 49) | Décision de type 1 avant de cibler l'Algérie |

À vérifier : SATIM (cartes CIB, Edahabia), plafonds et règles de change (article présumé 7), statut d'auto-entrepreneur, label startup (décret n° 20-254 de 2020, de mémoire), loi 18-07 sur les données personnelles.

## Maroc (`ma`) et Tunisie (`tn`)

De mémoire, **non vérifié** : Maroc, lois 53-05 (échange électronique de données juridiques), 31-08 (protection du consommateur), 09-08 (données personnelles) ; Tunisie, loi n° 83-2000 (échanges et commerce électroniques) et loi sur les données personnelles de 2004 (numéro à vérifier). Aucune obligation chiffrée n'est reprise ici. Appliquer la méthode de pré-diagnostic et obtenir l'avis d'un avocat local avant d'ouvrir le marché.

## Veille réglementaire

1. Tenir la liste des textes suivis (source officielle, date, statut : en vigueur, voté, en discussion) dans `conformite-reglementaire.md`.
2. Dater chaque ligne ; une ligne sans contrôle depuis 30 jours est « à vérifier ».
3. Texte en discussion (TSN, PSD3/PSR, Digital Fairness Act) : l'écrire « en discussion », jamais comme règle.
4. Revoir la liste à J3, J5, J6 et à chaque changement de pays ou de produit.

## Gabarit (extrait du pré-diagnostic)

```markdown
## Pays visés
| Pays | Étiquette | Classement | Obstacles | Avis local requis |
|---|---|---|---|---|
| Algérie | dz | strict | .com.dz, hébergement local, paiement bancaire | oui |
```

## Sources

- JORADP, loi n° 18-05 du 10 mai 2018 (joradp.dz/FTP/jo-francais/2018/F2018028.pdf).
- Conseil de l'UE, petits colis ; Solutions Numériques (TSN) ; BOFiP (caisse) pour l'instabilité.
- Service-Public F31228 (activité réglementée).
- Règlement (UE) 2021/821 ; ANSSI, SecNumCloud : à relever à la date de l'étude.
