# Gabarits : carte mentale et cahier des charges

Ossature inspirée du modèle Volere (Atlantic Systems Guild) et de la norme ISO/IEC/IEEE 29148. Reformulé, à remplir avec les mots de la personne.

## A. Carte mentale (phase 1 — à valider avant d'aller plus loin)

Court, une demi-page au plus :
- **Le problème** : ce qui coince aujourd'hui, en une ou deux phrases.
- **L'objectif** : ce que ça doit permettre.
- **Les utilisateurs** : qui s'en sert.
- **Les grandes fonctions pressenties** : liste à puces, non figée.
- **Ce qui n'est pas demandé** : pour cadrer tout de suite.

Finir par : « Est-ce juste, à compléter ou à corriger ? »

## B. Cahier des charges complet (phase 5)

1. **Contexte et problème** — situation actuelle, douleur, déclencheur.
2. **Objectifs et valeur attendue** — résultats **mesurables** (le pourquoi).
3. **Périmètre** — inclus / exclu / reporté (lien avec MoSCoW).
4. **Parties prenantes et acteurs** — commanditaire, utilisateurs, rôles et droits.
5. **Exigences fonctionnelles** — numérotées `EF-01…`, en user stories « En tant que <rôle>, je veux <action> afin de <bénéfice> », chacune avec ses **critères d'acceptation** testables (idéalement Given/When/Then).
6. **Exigences non fonctionnelles** `ENF-01…` — performance, sécurité, confidentialité et données personnelles, disponibilité, ergonomie et accessibilité, compatibilité, volumétrie, langues.
7. **Contraintes** — budget, délai, techniques, réglementaires, hébergement et pays, existant à respecter.
8. **Règles de gestion et données** — objets métier, cycles de vie, règles (`RG-01…`).
9. **Critères d'acceptation globaux** — ce qui fait dire « c'est fini et conforme ».
10. **Risques, hypothèses, questions ouvertes**.
11. **Glossaire** — chaque terme métier défini simplement.

## C. Traçabilité des choix

Pour chaque décision structurante, une fiche courte (patron ADR / MADR) : contexte, options envisagées, décision, conséquences. Permet de savoir plus tard **pourquoi** un choix a été fait.

## D. Priorisation (à joindre)

- **MoSCoW** en mots simples : indispensable au lancement / important mais peut attendre / bonus / hors sujet. Plafonner les « indispensables » pour garder une première version atteignable.
- **Impact / effort** : repérer les gains rapides (fort impact, faible effort) pour la première version.
- **Carte des histoires utilisateur** : colonne = parcours de bout en bout ; tranches horizontales = versions successives (première version puis incréments).
