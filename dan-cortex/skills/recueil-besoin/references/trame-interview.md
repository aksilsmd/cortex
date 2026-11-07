# Trame d'interview — thèmes, questions en langage courant, réponses proposées

Chaque thème : une question simple, 3 à 5 réponses proposées, toujours « Autre (précisez) » et « Je ne sais pas / aide-moi à choisir ». Suivre l'**entonnoir** : ouvert d'abord, fermé ensuite pour confirmer. Sauter les thèmes hors sujet. Après chaque thème, un micro-récapitulatif d'une ligne. Quand la réponse est « Je ne sais pas », proposer le **défaut raisonnable** indiqué et expliquer son effet en une phrase.

Techniques à garder en tête (BABOK / ISO 29148) : questions ouvertes puis fermées ; les 5 W + comment ; les **5 pourquoi** pour atteindre le besoin racine ; faire raconter un **cas concret de A à Z** (les non-initiés pensent en histoires, pas en fonctions) ; reformuler sans cesse.

## 1. Le but
« En une phrase, qu'est-ce que ça doit permettre de faire ? » — puis 5 pourquoi pour le besoin racine (« pourquoi est-ce important ? » jusqu'à la vraie valeur).

## 2. Les utilisateurs et leurs rôles
« Qui va s'en servir ? »
1. Le grand public / des clients  2. Des professionnels / entreprises  3. Vous et votre équipe seulement  4. Un mélange.
Puis : « Y a-t-il plusieurs sortes d'utilisateurs avec des droits différents ? » (ex. un responsable qui voit tout, un employé qui voit une partie). *Défaut : un seul type d'utilisateur + un administrateur.*

## 3. Le parcours principal
« Racontez-moi, étape par étape, ce qu'un utilisateur ferait du début à la fin. » Laisser raconter, reformuler en étapes numérotées. C'est la colonne vertébrale (user story mapping).

## 4. Les choses manipulées (données)
« De quoi parle-t-on ? Des produits ? des clients ? des rendez-vous ? des documents ? » Lister les objets métier. Pour chacun : « qu'a-t-on besoin de savoir dessus ? ». Ces objets deviendront le modèle de données.

## 5. Les règles
« Y a-t-il des règles à respecter ? » (ex. « un client ne voit pas les prix de gros », « une commande ne part pas si elle n'est pas payée »). Ce sont les règles de gestion.

## 6. Contenus et apparence
« Des textes, photos, vidéos à afficher ? » / « Une charte, des couleurs, un logo existants ? » *Défaut : style sobre et moderne, à affiner en maquette.*

## 7. Accès et sécurité (au niveau du besoin, sans jargon)
« Qui a le droit de voir quoi, et de modifier quoi ? » / « Faut-il se connecter ? » / « Des informations sensibles (données personnelles, paiement) ? » *Défaut : connexion par e-mail + mot de passe, droits par rôle, pas de donnée sensible non justifiée.*

## 8. Argent
« Y a-t-il un paiement en ligne ? un abonnement ? des devis/factures ? » *Défaut : pas de paiement en ligne au lancement.*

## 9. Langues et appareils
« En quelles langues ? » / « Plutôt sur téléphone, ordinateur, ou les deux ? » / « Besoin que ça marche sans connexion ? » *Défauts : une langue, mobile + ordinateur, en ligne.*

## 10. Volume et échelle
« Combien d'utilisateurs et d'éléments, à peu près, au début puis plus tard ? » Ordre de grandeur suffit. Sert à dimensionner.

## 11. Contraintes
« Un budget, un délai, une date ? » / « Où ça doit être hébergé, dans quel pays ? » / « Des lois particulières (données personnelles, secteur réglementé) ? » Signaler qu'on fera valider le volet légal par un juriste.

## 12. L'existant
« Y a-t-il déjà quelque chose à reprendre ou à remplacer ? un fichier, un ancien outil, un site ? »

## 13. La réussite
« À quoi verrez-vous que c'est réussi ? » Transformer en critères d'acceptation testables.

## Proposer (phase 4)
À partir des réponses, suggérer des fonctions ou garde-fous non demandés, **étiquetés « proposition »** : sauvegarde/export des données, journal des modifications, gestion des droits, accessibilité, respect des données personnelles, notifications, tableau de bord. Chaque proposition est justifiée par le besoin exprimé et reste au choix de la personne.
