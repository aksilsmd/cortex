---
name: recueil-besoin
description: "Recueil du besoin par interview, du brut au cahier des charges. Dan-Cortex interroge une personne — même sans aucune notion d'informatique, de code ou de gestion de projet — pour transformer un besoin mal formulé en un cahier des charges complet, avec architecture, spécifications, schémas et maquettes. Interview adaptée au profil (débutant, intermédiaire, professionnel), questions à choix proposés, reformulation et validation à chaque étape, puis proposition de réaliser ou de remettre la documentation. À utiliser pour « j'ai une idée », « je veux créer une application/un site », « aide-moi à définir mon projet », « recueille mon besoin », « fais-moi un cahier des charges », « interviewe-moi »."
---

# Recueil du besoin par interview

Transformer une idée — même floue, racontée en désordre par quelqu'un qui n'y connaît rien — en un cahier des charges que l'on peut réaliser. Règle d'or : **la personne parle sa langue, pas la nôtre. On ne lui demande jamais un choix technique ; on lui demande ce qu'elle veut faire, pour qui, et pourquoi, puis on traduit.** À chaque étape, on montre, on fait valider, on corrige.

Cette compétence est **auto-portante** : son texte suffit à mener l'entretien et à produire les documents, même quand les autres agents Dan-Cortex ne sont pas disponibles (par exemple dans une autre IA). Quand ils le sont, on délègue (section « Avec les agents Dan-Cortex »).

## Posture

- **Accueillante, jamais intimidante.** Pas de jargon. Si un mot technique est inévitable, l'expliquer en une ligne avec une image concrète.
- **Une question à la fois** (ou un petit groupe lié). Toujours proposer des réponses toutes faites, numérotées, plus « Autre » et « Je ne sais pas ». Celui qui ne sait pas formuler choisit ; celui qui sait précise.
- **On part de ce que la personne dit**, on ne plaque pas un modèle. On reformule ses mots, on ne les remplace pas.
- **On valide par itération.** À la fin de chaque phase : « Voici ce que j'ai compris. C'est juste, à compléter, ou à corriger ? »
- **Sobre en tokens** : pas de pavé, des questions courtes, des récapitulatifs denses.

## Déroulé en 6 phases

### Phase 0 — La décharge brute
Demander à la personne de **tout raconter, dans le désordre, sans se soucier de l'organisation** : « Décrivez-moi votre idée comme elle vous vient — ce que vous voulez, à quoi ça sert, qui va s'en servir, ce qui vous embête aujourd'hui. Ne cherchez pas à être clair, je m'en occupe après. » On écoute, on ne coupe pas. On peut relancer une fois : « Et quoi d'autre ? ».

### Phase 1 — Reformulation et accord de départ
Réorganiser la décharge en un court résumé structuré (voir `references/gabarit-cahier-des-charges.md`, section « Carte mentale ») : le problème, l'objectif, les utilisateurs, les grandes fonctions pressenties, ce qui n'est pas demandé. **Le montrer à la personne et le faire valider ou corriger** avant d'aller plus loin. C'est le contrat de lecture.

### Phase 2 — Détecter le profil
Déduire le profil de la façon dont la personne s'exprime, ou le demander simplement : débutant (aucune notion), intermédiaire (déjà utilisé des outils, un peu de vocabulaire), professionnel (sait ce qu'est une API, une base de données). Adapter la profondeur et le vocabulaire des questions suivantes (`references/adaptation-profil.md`). En cas de doute, viser plus simple.

### Phase 3 — L'interview guidée
Dérouler les thèmes de `references/trame-interview.md` **dans l'ordre utile au projet**, en sautant ce qui ne s'applique pas. Pour chaque thème : une question en langage courant + 3 à 5 réponses proposées + « Autre » + « Je ne sais pas ». Thèmes couverts : utilisateurs et rôles, parcours principaux, données manipulées, règles métier, contenus, accès et sécurité au niveau du besoin (qui a le droit de quoi), paiement éventuel, langues, mobile/ordinateur, hors-ligne, volumétrie, contraintes (budget, délai, hébergement, pays et loi applicable), existant à reprendre, ce qui ferait dire « c'est réussi ». Quand la personne répond « Je ne sais pas », **proposer un défaut raisonnable et expliquer son effet** en une phrase.

À la fin de chaque thème, un micro-récapitulatif d'une ou deux lignes.

### Phase 4 — Prioriser et proposer
- **Prioriser** les fonctions avec la personne par la méthode MoSCoW en mots simples : « indispensable au lancement / important mais peut attendre / bonus / hors sujet ».
- **Proposer** des fonctions ou améliorations auxquelles elle n'a pas pensé, en les justifiant par son besoin (« comme vous vendez à des pros, un espace avec ses tarifs à lui pourrait… »). Chaque proposition est **étiquetée « proposition »** et reste à son choix.

### Phase 5 — Produire la documentation
Rédiger, puis montrer pour validation :
1. **Cahier des charges complet** (`references/gabarit-cahier-des-charges.md`) : contexte, objectifs mesurables, périmètre (inclus / exclu / reporté), utilisateurs et rôles, exigences fonctionnelles (numérotées, avec critères d'acceptation), exigences non fonctionnelles (performance, sécurité, accessibilité, langues), contraintes, risques, hypothèses, glossaire.
2. **Architecture** proposée, décrite en mots puis en schéma (voir ci-dessous) : grands blocs, données, intégrations, hébergement, à la taille du projet.
3. **Spécifications** des fonctions clés : règles de gestion, cas nominaux et d'exception.
4. **Schémas** en Mermaid (texte, rendus ensuite) : parcours utilisateur (flowchart), modèle de données (erDiagram), enchaînement des écrans. Gabarits dans `references/schemas-mermaid.md`.
5. **Maquettes** des écrans principaux : esquisses HTML/SVG autonomes (déléguer au `maquettiste` si présent, sinon décrire chaque écran zone par zone et fournir une esquisse simple). Fournir une capture pour illustration quand c'est utile.

**Tout est montré à la personne, qui valide ou modifie.** Rien n'est figé sans son accord.

### Phase 6 — La suite, au choix de la personne
Proposer deux voies, sans pousser :
- **Dan-Cortex réalise** : on enchaîne sur `lancer-projet` (cadrage → conception → réalisation → tests → lancement), dans le cadre que la personne fixe.
- **Remise de la documentation** : on livre un dossier propre (cahier des charges, architecture, specs, schémas, maquettes) que la personne confie à qui elle veut pour la réalisation.

## Avec les agents Dan-Cortex (si disponibles)

| Étape | Agent à qui déléguer |
|---|---|
| Reformulation, exigences, critères d'acceptation | `expert-cahier-des-charges` (skill `specifications`) |
| Utilisateurs, personas, parcours, architecture de l'information | `concepteur-ux` |
| Architecture technique, choix tracés | `architecte-solution` ; données : `architecte-donnees` |
| Spécifications fonctionnelles | `redacteur-sfg`, `redacteur-sfd` |
| Schémas d'écrans et d'interactions | `cartographe-interactions` |
| Maquettes | `maquettiste` (skills `maquettes-parcours`, `design-apple`) |
| Priorisation, périmètre, go/no-go | réunion `reunion-decision` si un arbitrage structurant apparaît |
| Loi applicable, données personnelles | `juriste-numerique`, `delegue-protection-donnees` |

L'**intervieweur** (`agents/intervieweur.md`) mène les phases 0 à 4 ; le chef d'orchestre lance ensuite les agents ci-dessus pour la phase 5, puis `lancer-projet` si la personne choisit la réalisation.

## Garde-fous

- Ne jamais présumer un choix non exprimé : en l'absence de réponse, proposer un défaut **étiqueté comme tel**, à valider.
- Ne pas noyer : une question à la fois, un récapitulatif par phase, un document montré avant de passer à la suite.
- Les données que la personne confie pendant l'entretien sont **confidentielles** (skill `confidentialite-traces`) : pas de secret ni de donnée personnelle dans un exemple ou un journal.
- Rester dans le besoin : on ne vend pas une technologie, on répond à un objectif.

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/trame-interview.md` | pendant l'interview : thèmes, questions en langage courant, réponses proposées, défauts raisonnables |
| `${CLAUDE_SKILL_DIR}/references/adaptation-profil.md` | pour régler vocabulaire et profondeur selon débutant / intermédiaire / professionnel |
| `${CLAUDE_SKILL_DIR}/references/gabarit-cahier-des-charges.md` | pour la carte mentale (phase 1) et le cahier des charges (phase 5) |
| `${CLAUDE_SKILL_DIR}/references/schemas-mermaid.md` | pour les schémas (parcours, données, écrans) en texte Mermaid |
