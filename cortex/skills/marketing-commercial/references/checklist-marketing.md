# Contrôles — marketing

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| MKT-001 | J2 | majeur | tous | - | La stratégie de marché s'appuie sur la note d'opportunité, le benchmark et la voix du client, cités avec leurs dates, sans refaire l'étude | 02-cadrage/strategie-marche.md | bonne pratique |
| MKT-002 | J2 | bloquant | tous | - | Un client idéal unique est décrit avec son déclencheur d'achat, son problème, son alternative actuelle et les segments écartés | 02-cadrage/strategie-marche.md | bonne pratique |
| MKT-003 | J2 | majeur | tous | - | Une phrase de positionnement relie la cible, le problème, la catégorie, le bénéfice et l'alternative, chaque promesse portant une preuve vérifiable | 02-cadrage/strategie-marche.md | bonne pratique |
| MKT-004 | J2 | majeur | saas,erp,site | b2b | Un message distinct par rôle d'achat du comité (décideur, utilisateur, financeur, technique, juridique) est rédigé | 02-cadrage/strategie-marche.md | Gartner, mai 2025 |
| MKT-005 | J2 | majeur | tous | - | Le modèle de croissance dominant (produit, vente, communauté ou hybride) est choisi et justifié par le type de projet | 02-cadrage/strategie-marche.md | bonne pratique |
| MKT-006 | J2 | majeur | tous | - | Une métrique de référence unique, ses leviers et sa cible à J+90 sont définis et rattachés au produit | 02-cadrage/strategie-marche.md | Amplitude, North Star |
| MKT-007 | J2 | bloquant | tous | - | Les paliers de lancement (discret, bêta ouverte, disponibilité générale) portent des seuils de passage chiffrés, dont le seuil d'ajustement produit-marché | 02-cadrage/strategie-marche.md | Sean Ellis ; First Round |
| MKT-008 | J3 | majeur | tous | - | Les objectifs à J+90 sont chiffrés : métrique de référence, activation, coût d'acquisition cible et délai de récupération | 03-conception/marketing/plan-marketing.md | bonne pratique |
| MKT-009 | J3 | bloquant | tous | - | Chaque allégation publicitaire figure dans un tableau avec sa preuve et sa source, et a été relue par le juriste | 03-conception/marketing/plan-marketing.md | Code de la consommation, à valider |
| MKT-010 | J3 | majeur | tous | - | Chaque canal prioritaire, trois au plus au lancement, a un budget test, un indicateur et un seuil de coupure chiffrés | 03-conception/marketing/plan-marketing.md | bonne pratique |
| MKT-011 | J3 | majeur | site,saas,ecommerce,niche | - | Les pages à promouvoir sont indexables avec extrait, et robots.txt et le CDN autorisent Googlebot et OAI-SearchBot | 03-conception/marketing/plan-marketing.md | Google Search Central ; OpenAI |
| MKT-012 | J4 | majeur | site,saas,ecommerce | - | Des pages de preuve textuelles (cas clients, comparatifs, FAQ) sont prêtes, sans élément qui bloque l'extrait | rapport de test | Google Search Central, 10/12/2025 |
| MKT-013 | J3 | majeur | ecommerce | - | Le flux produit et Merchant Center sont configurés, et le profil d'établissement est à jour pour une activité locale | 03-conception/marketing/plan-marketing.md | Google Search Central |
| MKT-014 | J4 | majeur | mobile | stores | La fiche de store par défaut, au moins trois fiches personnalisées par audience et un test de fiche sont préparés | 03-conception/marketing/plan-marketing.md | Apple ; Google Play Console |
| MKT-015 | J3 | majeur | mobile | stores | Le calendrier de soumission des fiches personnalisées tient compte de la revue de la plateforme et du suivi de rétention par fiche | 03-conception/marketing/plan-marketing.md | Apple ; Google Play Console |
| MKT-016 | J3 | bloquant | tous | donnees-perso | Un plan de marquage liste les événements par étape (acquisition à recommandation), leurs propriétés, leur dictionnaire et le consentement requis | 03-conception/marketing/plan-marketing.md | CNIL ; bonne pratique |
| MKT-017 | J3 | majeur | tous | donnees-perso+ue | L'outil de mesure est choisi et sa base juridique documentée : mesure consentie ou outil exempté selon les conditions de la CNIL | 03-conception/marketing/plan-marketing.md | CNIL, juillet 2025 |
| MKT-018 | J5 | bloquant | tous | donnees-perso+ue | Le dispositif de consentement et Consent Mode v2 sont testés en accepté et en refusé, et la mesure se comporte comme prévu | rapport de test | Google Consent Mode v2 ; CNIL |
| MKT-019 | J5 | majeur | tous | ue | Aucune mention « certifié CNIL » n'apparaît, et la durée de conservation des données de mesure respecte les conditions de l'exemption | 05-validation/dossier-conformite.md | CNIL, juillet 2025 |
| MKT-020 | J3 | majeur | tous | ue | Une pile de mesure consentie, distincte de la mesure exemptée, est prévue pour les audiences publicitaires | 03-conception/marketing/plan-marketing.md | CNIL, juillet 2025 |
| MKT-021 | J5 | majeur | tous | - | Les balises sont recettées de bout en bout, balisage serveur compris ou son absence justifiée | rapport de test | bonne pratique |
| MKT-022 | J5 | bloquant | tous | b2c,b2b | SPF, DKIM, DMARC et le désabonnement en un clic sont en place avant le premier envoi de masse | capture | Gmail ; Yahoo ; RFC 8058 |
| MKT-023 | J3 | bloquant | tous | fr | Une grille de prospection valide chaque envoi ou appel : canal, B2C ou B2B, base légale, preuve et désinscription | 03-conception/marketing/plan-marketing.md | CNIL ; DGCCRF, à valider |
| MKT-024 | J6 | majeur | tous | fr,b2c | Aucun appel de prospection aux consommateurs sans consentement préalable de moins d'un an, et les preuves sont conservées au moins trois ans | 06-lancement/plan-communication.md | DGCCRF, août 2026 |
| MKT-025 | J5 | majeur | tous | donnees-perso | Les listes de contacts proviennent de consentements propres datés, jamais de listes achetées, avec une liste d'opposition durable | 06-lancement/plan-communication.md | CNIL |
| MKT-026 | J5 | majeur | tous | fr | Les contrats d'influence ou d'agence sont écrits et signés, et la mention « publicité » ou « collaboration commerciale » figure dans les briefs | contrat signé | DAJ, cadre de l'influence commerciale ; guide 01/2026, à valider |
| MKT-027 | J3 | majeur | tous | - | Le nom de marque a fait l'objet d'une vérification des domaines, comptes, stores et antériorités par le juriste | 03-conception/marketing/plan-marketing.md | bonne pratique |
| MKT-028 | J3 | mineur | tous | - | Le ton éditorial est écrit avec exemples, et la ligne éditoriale précise piliers, formats, cadence et sourçage | 03-conception/marketing/plan-marketing.md | bonne pratique |
| MKT-029 | J6 | majeur | tous | - | Aucun faux avis, faux témoignage, urgence fictive ni chiffre d'usage inventé n'apparaît dans les supports de lancement | 06-lancement/plan-communication.md | bonne pratique ; à valider |
| MKT-030 | J6 | majeur | tous | - | Un plan de crise nomme un porte-parole, des seuils d'alerte, des messages types validés et les accès aux comptes | 06-lancement/plan-communication.md | bonne pratique |
| MKT-031 | J6 | majeur | tous | - | Une procédure d'avis fixe un délai de réponse de 24 heures au lancement et interdit l'achat ou la rédaction d'avis | 06-lancement/plan-communication.md | bonne pratique ; à valider |
| MKT-032 | J6 | majeur | tous | - | Le calendrier de lancement de J-90 à J+90 attribue chaque action à un responsable humain avec un texte prêt | 06-lancement/plan-communication.md | bonne pratique |
| MKT-033 | J6 | majeur | tous | - | Le tableau de bord de lancement est en production : volume et coût par canal, activation, erreurs, plaintes, satisfaction | capture | bonne pratique |
| MKT-034 | J7 | majeur | tous | - | Les indicateurs de J+7, J+30 et J+90 sont relus par canal, et les canaux sous le seuil sont coupés ou corrigés | 07-exploitation/suivi-indicateurs.md | bonne pratique |
| MKT-035 | J7 | mineur | tous | - | Un bilan de J+90 compare objectifs et résultats, et un post-mortem écrit alimente la décision d'échelle | 07-exploitation/suivi-indicateurs.md | bonne pratique |
