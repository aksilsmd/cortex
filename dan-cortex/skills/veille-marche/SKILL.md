---
name: veille-marche
description: >
  Pôle Stratégie et marché de Dan-Cortex : taille du marché, démontage des concurrents, voix du client, contexte
  politique, économique et culturel, puis décision. À utiliser pour étude de marché, benchmark, avis clients,
  « que manque-t-il », « quoi ajouter ou supprimer », positionnement, PESTEL.
---

# Veille de marché — pôle Stratégie et marché

Ce pôle épluche le marché, les concurrents, les avis et le contexte pour aboutir à des décisions : y aller ou non, sous quel angle, avec quoi ajouter, supprimer ou différencier. Règle d'or : **chaque chiffre, prix, fonction ou verbatim porte son URL et sa date de consultation, et chaque analyse se termine par une décision ou par un test qui la permettra.**

## Principes

1. **Une analyse sans décision est un rapport.** Chaque constat se range dans une ligne d'écarts « ajouter, supprimer, différencier, protéger » ; sinon il sort du livrable.
2. **Les faits d'abord, l'interprétation ensuite.** Les `collecteur-web` écrivent des fiches de faits au gabarit ; les analystes synthétisent à partir des fiches. Pourquoi : c'est moins cher et chaque affirmation reste vérifiable.
3. **Jamais d'avis inventé.** Un verbatim est une citation exacte courte ou une reformulation signalée ; l'absence se note « non trouvé ». Un avis fictif fausse toute la chaîne de décision.
4. **Deux méthodes valent mieux qu'une.** Taille de marché par le haut et par le bas ; trafic ou SEO sur deux outils ; manque « confirmé » seulement avec trois sources de nature différente.
5. **Les estimations restent des estimations.** Trafic, SEO et parts de marché sont des modèles : les étiqueter « estimation » avec leur fourchette.
6. **Collecte loyale et licite.** Conditions d'utilisation, `robots.txt`, données personnelles : pas de contournement, pas de collecte nominative, pas d'aspiration massive (`references/sources-et-requetes.md`).
7. **Les biais sont écrits.** Note moyenne trompeuse (distribution en J), minorité vocale, audience propre à chaque plateforme : le livrable les nomme et dit ce qu'ils changent.
8. **Le substitut et « ne rien faire » sont des concurrents.** Le tableur et l'agence comptent autant que l'éditeur direct.

## Méthode

1. **Cadrer** : formuler le job à accomplir, le segment visé et l'alternative actuelle en trois phrases ; lister les concurrents (au moins dix, classés direct, indirect, substitut) et les sources d'avis, avec leur statut d'accès (`references/sources-et-requetes.md`, `references/veille-concurrentielle.md`).
2. **Collecter** : une fiche par concurrent et par source, écrite par un `collecteur-web` au gabarit, dans `01-decouverte/sources/`.
3. **Mesurer le marché** : TAM, SAM, SOM calculés de deux façons, segments, tendances (`references/etude-de-marche.md`).
4. **Démonter l'offre** : matrice fonctionnelle avec preuve par cellule, prix sur un cas d'usage, positionnements (`references/veille-concurrentielle.md`).
5. **Écouter le client** : coder les avis en irritants, attentes, manques, satisfactions ; quantifier ; nommer les biais (`references/voix-du-client.md`).
6. **Lire le contexte** : facteurs politiques, économiques, sociaux, culturels, technologiques, environnementaux et légaux, par marché visé (`references/analyse-contexte.md`).
7. **Décider** : écarts, priorisation, positionnement, deux ou trois options de périmètre chiffrées, tests de demande avec seuils fixés d'avance (`references/strategie-positionnement.md`).
8. **Contrôler** : parcourir `references/checklist-marche.md` (MAR) et `references/checklist-contexte.md` (CTX) pour le jalon.

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Étude de marché | `01-decouverte/etude-de-marche.md` | `HYP-` |
| Benchmark concurrentiel | `01-decouverte/benchmark-concurrentiel.md` | `CON-` |
| Voix du client | `01-decouverte/voix-du-client.md` | `THM-` |
| Analyse du contexte | `01-decouverte/analyse-contexte.md` | `FAC-` |
| Note d'opportunité | `01-decouverte/note-opportunite.md` | `ECA-`, `OPT-` |
| Fiches de faits | `01-decouverte/sources/concurrents/`, `avis/`, `marche/` | |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/etude-de-marche.md` | pour chiffrer le marché, les segments, les tendances |
| `${CLAUDE_SKILL_DIR}/references/veille-concurrentielle.md` | pour repérer et démonter les concurrents, écrire une fiche concurrent |
| `${CLAUDE_SKILL_DIR}/references/voix-du-client.md` | pour dépouiller des avis et écrire une fiche de source ou la synthèse |
| `${CLAUDE_SKILL_DIR}/references/analyse-contexte.md` | pour le contexte par facteur et par pays |
| `${CLAUDE_SKILL_DIR}/references/strategie-positionnement.md` | pour passer des constats aux décisions (stratège) |
| `${CLAUDE_SKILL_DIR}/references/sources-et-requetes.md` | avant toute collecte : sources, requêtes, règles, accès fermés |
| `${CLAUDE_SKILL_DIR}/references/checklist-marche.md` | contrôles MAR du jalon |
| `${CLAUDE_SKILL_DIR}/references/checklist-contexte.md` | contrôles CTX du jalon |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

## Garde-fous

- Le pôle livre un dossier de décision (options, preuves, confiance) ; la décision d'y aller, de pivoter ou de renoncer appartient à l'utilisateur.
- Aucune collecte hors des règles de `references/sources-et-requetes.md` : pas de scraping d'un site qui l'interdit, pas de faux compte, pas de données nominatives conservées.
- Le contexte légal, fiscal et réglementaire est un repérage pour le `juriste-numerique` et le `controleur-financier`, marqué « à valider » ; il ne vaut pas avis professionnel.
- Un chiffre sans source datée est une hypothèse (`HYP-`) ou « non trouvé », jamais un fait.
