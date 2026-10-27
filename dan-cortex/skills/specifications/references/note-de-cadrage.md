# Note de cadrage

La note de cadrage officialise la mission : pourquoi le projet existe, ce qu'il couvre, qui décide, avec quelles bornes. Dans la pratique française elle est validée en COPIL et fonde la mission du chef de projet. Elle précède le cahier des charges et ne détaille aucune exigence.

## Sommaire
1. Méthode
2. Choix du cycle de vie
3. Garde-fous de gouvernance
4. Gabarit
5. Pièges fréquents
6. Contrôles avant de rendre
7. Sources

## 1. Méthode

1. Lire la fiche projet, la note d'opportunité et la décision d'option de périmètre (J1). Ne rien redécouvrir.
2. Formuler le **problème** en une phrase, puis les **objectifs** chiffrés avec date et indicateur de mesure (un objectif sans indicateur est un vœu).
3. Poser le **périmètre** en trois colonnes : inclus V1, exclu, reporté. L'exclu explicite évite 80 % des dérives.
4. Nommer les **rôles** : sponsor, responsable unique de bout en bout, MOA (distincte de la MOE et des métiers), MOE, AMOA le cas échéant, représentant des utilisateurs. Si la décision n'est pas prise, la poser en question ouverte, pas en blanc.
5. Définir les **instances** (3 à 4 niveaux, chaque président siégeant au niveau supérieur), leur mandat et leurs seuils d'escalade.
6. Choisir et justifier le **cycle de vie** (section 2).
7. Poser **contraintes, hypothèses, dépendances** : chacune avec un responsable et une date de levée.
8. Écrire les **critères de succès** et les **critères d'arrêt** : l'arrêt est une option explicite de chaque jalon.
9. Donner **budget et délai en fourchette**, avec leur niveau de confiance, et les délais de gouvernance (avis, validations) qui entrent dans le planning.

## 2. Choix du cycle de vie

| Situation | Choix |
|---|---|
| Besoin stable, contrat au forfait, recette contractuelle, secteur régulé | séquentiel avec jalons formels |
| Besoin incertain, valeur à découvrir, équipe produit stable | agile, avec les mêmes jalons de libération (le cycle ne supprime pas la gouvernance) |
| Socle stable (ERP, intégrations, migration) et interface changeante | hybride : socle séquentiel, couches utilisateur en incréments |

Justifier le choix par écrit : c'est une décision de gouvernance, de type 1 (état : octobre 2026, cycles classique et agile partageant les mêmes décisions de libération dans HERMES).

## 3. Garde-fous de gouvernance

Repères issus des audits publics français, à adapter ; ils valent comme alertes, pas comme loi pour un projet privé.

| Repère | Valeur | Source |
|---|---|---|
| Responsable unique nommé | condition essentielle de succès | Cour des comptes, 2020 |
| Durée d'une tranche | 5 ans au plus sans dérogation tracée | idem |
| Taille d'une tranche, livraison de valeur | 5 à 20 M€ ; valeur tous les 18 mois à 3 ans | idem |
| Part de ressources internes | au moins 38 % (repère) | idem |
| Externalisation | alerte à 60 %, lancement exclu au-delà de 80 % | circulaire du 7 février 2023 (État) |
| Projet numérique de l'État supérieur à 9 M€ | avis DINUM, un mois à prévoir | questions parlementaires |

Pour un projet privé, retenir le principe (responsable unique, tranches courtes, critère d'arrêt écrit), pas les seuils d'État.

## 4. Gabarit

````markdown
# Note de cadrage — <nom du projet>

## Synthèse
<Trois à cinq lignes : problème, objectif principal chiffré, périmètre V1, budget et délai en fourchette,
 décision attendue du comité de cadrage, questions ouvertes.>

## 1. Contexte et problème
## 2. Objectifs et indicateurs
| Objectif | Indicateur | Valeur de départ | Cible | Échéance | Source de mesure |
|---|---|---|---|---|---|

## 3. Périmètre
| Inclus en V1 | Exclu | Reporté (version et condition) |
|---|---|---|

## 4. Gouvernance
### Rôles
| Rôle | Nom ou fonction | Responsabilité | Décide de |
|---|---|---|---|
### Instances
| Instance | Fréquence | Participants | Mandat | Seuil d'escalade |
|---|---|---|---|---|
### Cycle de vie : <choix> — justification

## 5. Parties prenantes
| Partie prenante | Intérêt | Influence | Attente | Mode d'implication |
|---|---|---|---|---|

## 6. Contraintes, hypothèses, dépendances
| Type | Énoncé | Responsable | Date de levée ou de contrôle |
|---|---|---|---|

## 7. Jalons macro, budget, délai
## 8. Risques majeurs
<Cinq au plus, avec renvoi au registre RSQ-
## 9. Critères de succès et d'arrêt
## 10. Décisions attendues et questions ouvertes
````

## 5. Pièges fréquents

- Des objectifs de moyens (« refondre le site ») au lieu de résultats (« +15 points de conversion »).
- Une gouvernance décorative : instances sans mandat écrit ni seuil d'escalade.
- Une MOA confondue avec la MOE ou avec le métier ; une AMOA qui se substitue à la MOA au lieu de la renforcer.
- Un périmètre sans colonne « exclu ».
- Des délais de validation absents du planning.
- Des objectifs repris du marketing sans indicateur ni source de mesure.

## 6. Contrôles avant de rendre

- Chaque objectif a un indicateur, une cible et une échéance.
- Un sponsor et un responsable unique sont nommés, ou la question est ouverte et datée.
- Le cycle de vie est choisi et justifié.
- Critères d'arrêt et de succès écrits.
- Le document tient en dix pages au plus.

## Sources

- JDN, « Les dossiers techniques en gestion de projet informatique » (séquence note de cadrage → faisabilité → cahier des charges).
- CREDAF, « Les prérequis d'une bonne maîtrise d'ouvrage informatique » (2019, émetteur à vérifier).
- Cour des comptes, rapport 2020 sur les grands projets numériques de l'État (via Sénat, r20-047).
- HERMES, édition 2022, 3e tirage du 31.12.2025 (eCH-0054) : décisions de libération.
- PRINCE2 7 (septembre 2023) ; PMBOK Guide 8th edition (fin 2025, date à vérifier).
