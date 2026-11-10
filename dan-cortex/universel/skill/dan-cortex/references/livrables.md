# Catalogue des livrables remis à l'utilisateur

Règles communes : une synthèse d'une page en tête, écrite pour un non-spécialiste ; un sommaire ; des schémas
là où une image vaut mieux qu'un paragraphe ; un glossaire ; les hypothèses et les points ouverts listés ; les
sources en fin. Aucune note de travail d'agent, aucun identifiant interne sans son explication, aucun mot comme
« hypothèse de conception » laissé sans phrase qui dise quoi faire. Le document remis est relu par un
`verificateur` qui joue le lecteur débutant.

## 1. Cahier des charges (étape 5)
1. Synthèse : le projet en dix lignes, pour qui, pourquoi, ce qui sera livré.
2. Contexte et description du projet ; objectifs mesurables.
3. Analyse du marché en résumé (renvoi à l'étude de marché) ; manques du marché que le projet comble.
4. Utilisateurs : profils, parcours principaux illustrés.
5. Périmètre : ce qui est dans la première version, ce qui viendra après, ce qui est exclu.
6. Fonctionnalités : par famille, chacune avec description, règle, priorité (indispensable, important,
   souhaitable), critère d'acceptation, maquette ou schéma associé.
7. Prérequis et dépendances : contenus, comptes, services tiers, autorisations, matériel, ce que l'utilisateur
   doit fournir et pour quand.
8. Maquettes prévues : écrans clés sur ordinateur et sur téléphone, états (vide, chargement, erreur, succès).
9. Architecture expliquée simplement : schéma d'ensemble, briques, données, hébergement ; choix et raisons.
10. Normes de développement : qualité du code, tests, sécurité, accessibilité, performances, langues, et
    **reprise par un humain** (documentation d'entrée, nommage par le métier, dépendances déclarées, test de
    reprise par un développeur qui ne connaît pas le projet).
11. Exigences non fonctionnelles : sécurité, données personnelles, disponibilité, sauvegardes.
12. Conformité : obligations légales par pays, « à valider par un professionnel ».
13. Organisation : étapes, planning macro, rôles, validations attendues de l'utilisateur.
14. Budget en résumé (renvoi à l'étude de réalisation) ; risques et parades.
15. Annexes : glossaire, hypothèses, points ouverts, sources.

Illustrations attendues : schéma de contexte, parcours utilisateur, carte de navigation, schéma d'architecture,
modèle de données simplifié, maquettes. Maquettes tierces : jamais reproduites, seulement décrites.

## 2. Étude de marché (étape 6)
1. Synthèse et verdict : y a-t-il une place, pour qui, à quelles conditions.
2. Le domaine et ses acteurs (carte).
3. Taille du marché en deux méthodes (descendante et ascendante), hypothèses visibles.
4. Segments de clients et leurs besoins.
5. Concurrents : fiches, tableau comparatif fonctions et prix, carte de positionnement.
6. Voix du client : irritants et attentes, citations courtes sourcées.
7. Manques du marché et opportunités, classés par valeur et difficulté.
8. Contexte : politique, économique, social, technologique, légal, par pays.
9. Tendances et scénarios à trois ans.
10. Recommandation de positionnement et de prix ; risques.
11. Méthode suivie pas à pas et limites ; sources datées.

## 3. Dossier de conception (étape 7)
Spécifications fonctionnelles générales (acteurs, fonctions, processus) et détaillées (règles, cas nominaux et
d'exception), spécifications techniques (interfaces, formats), dossier d'architecture et décisions tracées,
normes de code, schéma de données, workflows et matrice écran-action-destination, maquettes, analyse de risques
de sécurité, **planning de Gantt** (lots, dépendances, jalons, chemin critique, fourchettes), **stratégie de
test** (niveaux, environnements, données, critères d'entrée et de sortie, cahier de recette tracé aux exigences).

## 4. Étude de réalisation (étape 8)
Voir `etude-realisation.md`.

## 5. Paquet « à remettre à une entreprise » (étape 9, chemin 2)
Cahier des charges, conception, maquettes, planning, plus : lettre de consultation, grille de comparaison des
devis (critères pondérés), vingt questions à poser au prestataire, clauses à exiger (propriété du code,
réversibilité, garantie, recette), plan de recette pour contrôler la livraison.

## 6. Paquet « startup » (étape 9, chemin 3)
Note d'opportunité, offre et prix, plan de lancement, plan marketing et commercial, budget sur trois ans en
trois scénarios, financements possibles, feuille de route à 12 mois.

## Formats
Par défaut, des documents que l'utilisateur peut ouvrir, modifier et partager (document, PDF sur demande,
tableur pour budget et planning). Sur une IA sans fichiers : sections successives dans la conversation, avec à
la fin une table des matières récapitulative pour l'assemblage.
