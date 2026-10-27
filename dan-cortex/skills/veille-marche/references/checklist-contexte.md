# Contrôles — contexte politique, économique, social, culturel, environnemental

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| CTX-001 | J1 | bloquant | tous | - | La liste des marchés visés et du secteur est écrite, avec un tableau de facteurs distinct pour chaque marché | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-002 | J1 | majeur | tous | - | Chaque facteur retenu indique son effet décisionnel sur une exigence, un prix, un canal, un calendrier ou un choix de marché | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-003 | J1 | majeur | tous | - | Chaque fait porte sa source, sa date et sa nature primaire ou secondaire, et les sources secondaires sont signalées comme telles | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-004 | J1 | majeur | tous | - | Les échéances réglementaires et économiques des vingt-quatre prochains mois sont listées avec leur date et leur statut | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-005 | J1 | bloquant | tous | - | Les facteurs légaux sont repérés, marqués « à valider » et transmis au juriste dans le prédiagnostic juridique | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-006 | J1 | bloquant | tous | international | Les sanctions, embargos, restrictions d'export et règles de transfert de données applicables à chaque pays visé sont examinés | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-007 | J1 | majeur | tous | international | La stabilité politique, le risque de coupure d'accès ou de censure et les réformes annoncées sont évalués pour chaque pays hors Union européenne | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-008 | J1 | majeur | tous | secteur-public,grand-compte | Les exigences d'achat public ou de grand compte (préférence nationale, localisation des données, clauses sociales et environnementales) sont repérées | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-009 | J1 | majeur | ecommerce,saas,mobile,niche | international | La TVA, les droits de douane et les taxes sur les services numériques de chaque marché sont repérés, à valider par un expert-comptable | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-010 | J1 | majeur | ecommerce,saas,mobile,niche | paiement,abonnement | Le pouvoir d'achat, la monnaie, le risque de change et les moyens de paiement dominants sont documentés pour chaque marché | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-011 | J1 | majeur | ecommerce,saas,mobile,niche | dz,ma,tn | Le paiement à la livraison, les cartes locales, l'accès bancaire et les règles de transfert de devises sont vérifiés par une source locale | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-012 | J1 | majeur | site,ecommerce,mobile,saas,niche | b2c | L'équipement des cibles, la qualité de la connexion, le coût des données et l'illectronisme sont évalués par marché | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-013 | J1 | majeur | tous | multilingue,international | Les langues, variantes, formats de date, nombre et adresse, et sens de lecture de chaque marché sont listés pour le rédacteur de localisation | 01-decouverte/analyse-contexte.md | Unicode CLDR 47 |
| CTX-014 | J1 | majeur | tous | rtl | Les exigences propres à l'écriture de droite à gauche et la relecture par un locuteur natif sont signalées comme contraintes de conception | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-015 | J1 | mineur | tous | international,multilingue | Aucun stéréotype culturel n'est présenté comme un fait : les dimensions culturelles sont écrites comme hypothèses à valider localement | 01-decouverte/analyse-contexte.md | Hofstede, à vérifier |
| CTX-016 | J3 | majeur | tous | international,multilingue | Les hypothèses culturelles de chaque marché sont validées auprès d'au moins cinq utilisateurs locaux avant de figer la direction de contenu | 03-conception/design/contenu-localisation.md | bonne pratique |
| CTX-017 | J1 | majeur | tous | - | Les plateformes dont dépend l'offre (magasins, API, paiement, hébergeur) sont listées avec le risque de changement de leurs règles | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-018 | J1 | mineur | tous | - | Les facteurs environnementaux (écoconception, exigences d'acheteurs, hébergement) sont examinés au regard du RGESN 2024 | 01-decouverte/analyse-contexte.md | RGESN 2024 |
| CTX-019 | J1 | majeur | tous | mineurs | Les règles de protection des mineurs applicables à chaque marché sont repérées et transmises au juriste avec leur date | 01-decouverte/analyse-contexte.md | DSA art. 28 ; lignes directrices 2025 |
| CTX-020 | J1 | majeur | tous | ia,ugc | Les obligations existantes ou annoncées sur l'intelligence artificielle et les contenus publiés par les utilisateurs sont repérées et datées | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-021 | J1 | majeur | tous | ue | Les textes européens en préparation ou en transition qui touchent l'offre sont datés avec leur statut, par exemple le Digital Fairness Act | 01-decouverte/analyse-contexte.md | DSA art. 25 ; à vérifier |
| CTX-022 | J1 | majeur | ecommerce,saas,erp | fr | Les échéances françaises qui touchent l'offre (rétractation en ligne, facturation électronique) sont datées et transmises au juriste | 01-decouverte/analyse-contexte.md | à vérifier |
| CTX-023 | J1 | bloquant | tous | - | Les facteurs bloquants, structurants et à surveiller sont classés en fin de document avec leur conséquence sur le choix des marchés | 01-decouverte/analyse-contexte.md | bonne pratique |
| CTX-024 | J2 | majeur | tous | - | Les facteurs structurants sont repris dans la note de cadrage et transmis au contrôleur financier pour le budget | 02-cadrage/note-de-cadrage.md | bonne pratique |
