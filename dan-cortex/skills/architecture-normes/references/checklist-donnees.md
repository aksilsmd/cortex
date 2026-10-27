# Contrôles — données et schéma

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| DON-001 | J3 | bloquant | tous | - | Le modèle de données couvre toutes les entités des fonctions et des règles de gestion, chaque entité étant rattachée à au moins une fonction FN | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-002 | J3 | majeur | tous | - | Chaque entité déclare en base sa clé primaire, ses clés étrangères et ses contraintes de non-nullité et d'unicité, pas seulement dans le code | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-003 | J3 | majeur | tous | - | Les conventions de nommage et de types, dont horodatages avec fuseau, montants exacts et identifiants, sont documentées et appliquées partout | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-004 | J3 | majeur | tous | - | Chaque jeu de données a un propriétaire métier nommé, une classification de sensibilité et une durée de rétention | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-005 | J3 | majeur | tous | - | Un dictionnaire de données décrit chaque champ avec son sens, son format, sa source et la règle de gestion associée | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-006 | J3 | majeur | tous | - | Chaque table majeure a une volumétrie estimée à un et trois ans et une stratégie d'archivage ou de partitionnement quand un seuil est dépassé | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-007 | J3 | bloquant | tous | donnees-perso | Chaque colonne de donnée personnelle porte sa catégorie, sa finalité, sa base légale et sa durée de conservation, reliées au registre des traitements | 03-conception/architecture/modele-donnees.md | RGPD art. 5 et 30 ; à valider |
| DON-008 | J3 | majeur | tous | donnees-perso | Le schéma permet l'effacement, l'anonymisation et l'export des données d'une personne sans rompre l'intégrité référentielle | 03-conception/architecture/modele-donnees.md | RGPD art. 17 et 20 ; à valider |
| DON-009 | J3 | majeur | tous | donnees-sensibles | Les colonnes de données sensibles sont chiffrées ou pseudonymisées, et leurs clés sont gérées hors de la base de données | 03-conception/architecture/modele-donnees.md | RGPD art. 32 ; à valider |
| DON-010 | J3 | majeur | tous | - | La stratégie de migration impose des scripts versionnés, rejouables, testés sur une copie, avec un chemin de retour pour chacun | 03-conception/architecture/modele-donnees.md | bonne pratique |
| DON-011 | J3 | majeur | saas,erp | - | Le cloisonnement entre locataires est décrit par le modèle choisi, avec la sécurité au niveau des lignes forcée et sans contournement pour le rôle applicatif | 03-conception/architecture/modele-donnees.md | PostgreSQL, sécurité au niveau des lignes |
| DON-012 | J4 | bloquant | saas,erp | - | Un test automatique prouve qu'un locataire ne peut ni lire ni modifier les données d'un autre locataire, y compris via les clés étrangères | rapport de test | bonne pratique |
| DON-013 | J4 | majeur | tous | - | Les changements de schéma incompatibles suivent expand, migrate, contract, avec deux versions applicatives compatibles pendant la bascule | rapport de test | Fowler, Parallel Change |
| DON-014 | J4 | majeur | tous | - | Les plans d'exécution des requêtes critiques sont vérifiés sur une volumétrie réaliste, et chaque index est justifié par une requête | rapport de test | bonne pratique |
| DON-015 | J4 | majeur | tous | donnees-perso | Les jeux de données de test et de recette sont synthétiques ou anonymisés, jamais des copies brutes de production | rapport de test | RGPD art. 5 et 32 ; à valider |
| DON-016 | J5 | majeur | tous | migration | La reprise des données de l'existant est rapprochée par comptages, sommes de contrôle et échantillon validé par le métier | rapport de test | bonne pratique |
