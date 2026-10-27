# Conception du schéma de données

Méthode pour passer des fonctions et règles de gestion à un schéma robuste, évolutif, isolé entre locataires et respectueux des données personnelles. Moteur par défaut : PostgreSQL 18 (état : octobre 2026) ; le choix du moteur suit `references/choix-techniques.md`.

## Sommaire
1. Méthode
2. Conventions
3. Index
4. Migrations
5. Multi-locataire
6. Données personnelles
7. Gouvernance
8. Gabarit
9. Pièges et contrôles

## 1. Méthode

1. Lister les entités à partir de la SFG (`FN-`), de la cartographie des données et des règles de gestion (`RG-`) quand elles existent.
2. Modèle **conceptuel** (entités, relations, cardinalités), puis **logique** (attributs, clés, contraintes), puis **physique** (types, index, partitionnement), ce dernier après le comité d'architecture.
3. Pour chaque entité : propriétaire métier, cycle de vie (création, modification, archivage, suppression), volumétrie à un et trois ans.
4. Normaliser jusqu'à la troisième forme normale ; ne dénormaliser que sur mesure de performance, avec justification écrite.
5. Un moteur supplémentaire (cache, recherche, analytique) se justifie par une mesure : un PostgreSQL bien indexé avec JSONB, plein texte et pgvector couvre la plupart des MVP.

## 2. Conventions

Choisir, écrire dans le modèle, appliquer partout.

| Sujet | Règle |
|---|---|
| Noms | une seule langue, une seule casse (par exemple snake_case), pas de mots réservés |
| Clés primaires | identifiant technique sans signification métier ; UUIDv7 à évaluer (natif PostgreSQL 18, limite la fragmentation d'index) |
| Horodatages | type avec fuseau, en UTC ; colonnes de création et de modification |
| Montants | décimal exact ou entiers en unité mineure, avec devise ; jamais de flottant |
| Contraintes | NOT NULL, UNIQUE, clés étrangères, CHECK déclarés en base, pas seulement dans le code |
| JSON | pour l'attribut vraiment variable ; ce qu'on filtre ou joint devient colonne |
| Suppression | suppression logique seulement si l'historique l'exige ; elle ne dispense pas de l'effacement (section 6) |
| Énumérations | table de référence ou CHECK, pas de nombre magique |

## 3. Index

- Un index par requête identifiée, jamais « au cas où » : chaque index coûte en écriture.
- Indexer les clés étrangères, sauf justification.
- Index partiels pour les filtres fréquents ; index composites dans l'ordre de sélectivité et de tri.
- Vérifier le plan d'exécution des requêtes critiques sur une volumétrie réaliste, pas sur trois lignes.
- pgvector : HNSW (meilleur compromis, construction lente) ou IVFFlat ; limite de 2 000 dimensions (4 000 en halfvec) ; les filtres s'appliquent après l'index, d'où index partiels ou partitionnement.

## 4. Migrations

Toute évolution est un script **versionné, rejouable, testé sur une copie** de la base, avec chemin de retour. Outil au choix de la pile (Flyway, Liquibase, Alembic, ORM) : à vérifier, non lu à la source.

**Expand, migrate, contract** (parallel change, Fowler) pour tout changement incompatible :
1. *Expand* : ajouter la nouvelle structure sans retirer l'ancienne ; l'application écrit dans les deux.
2. *Migrate* : copier les données par lots, vérifier les comptages.
3. *Contract* : retirer l'ancienne structure une fois plus aucune version déployée ne la lit.

Règles : jamais de renommage ni de suppression de colonne en une seule étape ; les verrous longs sont interdits sur les tables volumineuses ; chaque migration indique sa durée estimée et son plan de retour.

## 5. Multi-locataire

| Modèle | Quand | Risque |
|---|---|---|
| Table partagée avec colonne locataire et sécurité au niveau des lignes (RLS) | beaucoup de petits clients | fuite entre clients si mal configurée ; voisin bruyant |
| Schéma par locataire | clients moyens, isolation modérée | migrations multipliées |
| Base par locataire | exigence réglementaire ou contractuelle | coût d'exploitation |
| Mono-locataire | très gros comptes, souveraineté | coût maximal |

RLS PostgreSQL : refus par défaut ; propriétaires de tables et rôles BYPASSRLS exemptés sauf `FORCE ROW LEVEL SECURITY` ; l'intégrité référentielle contourne la RLS ; les sous-requêtes de politique coûtent cher. Imposer : `FORCE`, rôle applicatif sans contournement (testé), revue des clés étrangères, test d'isolation automatique : un locataire A ne lit, ne modifie ni ne déduit rien d'un locataire B. Le modèle est une décision de type 1.

## 6. Données personnelles

À partir de `02-cadrage/cartographie-donnees.md` et avec `delegue-protection-donnees` :

1. Marquer chaque colonne de donnée personnelle : catégorie, finalité, base légale, durée de conservation, sensibilité. Cela alimente le registre des traitements (RGPD art. 30, à valider par un juriste).
2. Concevoir l'effacement et l'anonymisation d'une personne sans casser l'intégrité (références vers un identifiant anonymisé, pas de suppression en cascade aveugle), et l'export de ses données.
3. Séparer les identifiants directs des données d'usage quand c'est utile ; chiffrer ou pseudonymiser les données sensibles, clés gérées hors de la base.
4. Journaliser les accès aux données sensibles.
5. Tests et recette : données synthétiques ou anonymisées, jamais de copie brute de production.

## 7. Gouvernance

Chaque jeu de données a un propriétaire métier nommé, une classification, une durée de rétention, un dictionnaire (sens, format, source, règle `RG-`) et un contrôle de qualité. Vérifier la licence de chaque composant de données (Redis a changé de licence en 2024 puis 2025) et prévoir une sortie (Valkey, OpenSearch).

## 8. Gabarit de `modele-donnees.md`

```markdown
# Modèle de données — <projet>
## Synthèse
<entités, volumétrie, moteur et ADR, modèle de locataires, données personnelles, points ouverts>
## Moteur et conventions
## Modèle conceptuel
<schéma Mermaid erDiagram>
## Entités
| Entité | Propriétaire | Fonctions FN- | Règles RG- | Volumétrie 1 et 3 ans | Rétention |
## Dictionnaire de données
| Champ | Entité | Type | Sens | Source | Personnelle ? | Règle RG- |
## Index et requêtes critiques
## Locataires et isolation
## Données personnelles
## Migrations
## Gouvernance
```

## 9. Pièges et contrôles

Pièges : flottants pour des montants ; clé étrangère sans index ; JSON fourre-tout ; RLS sans FORCE ; migration destructive en une étape ; copie de production en recette. Avant de rendre : chaque entité relie une `FN-`, chaque colonne personnelle a sa durée, chaque index sa requête, chaque migration son retour, l'isolation est testée.

## Sources

- PostgreSQL 18 : https://postgresql.org/about/news/postgresql-18-released-3142/
- Sécurité au niveau des lignes : https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- pgvector : https://github.com/pgvector/pgvector
- Parallel change : https://www.martinfowler.com/bliki/ParallelChange.html
- Modèles de locataires : https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/considerations/tenancy-models
- RGPD, art. 5, 17, 20, 30, 32 : à vérifier sur EUR-Lex
