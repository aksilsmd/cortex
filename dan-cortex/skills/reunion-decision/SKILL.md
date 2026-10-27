---
name: reunion-decision
description: >
  Réunion entre agents experts Dan-Cortex : positions séparées, débat contradictoire, arbitrage, décision tracée. À
  utiliser pour trancher un choix structurant (positionnement, périmètre, architecture, budget, go/no-go),
  départager des experts, ou quand l'utilisateur dit « réunis les experts », « fais débattre », « aide-moi à
  décider ».
---

# Réunion et décision

Une réunion Dan-Cortex sert à prendre une décision meilleure que celle d'un expert seul, pas à échanger. Elle est
écrite, bornée, et finit toujours par une décision tracée. Si aucune décision n'est en jeu, il ne faut pas de
réunion : une revue croisée suffit.

## Classer la décision

| | Type 1 | Type 2 |
|---|---|---|
| Nature | irréversible ou coûteuse à défaire : positionnement, périmètre, langage et architecture, budget, engagement juridique, go/no-go | réversible à faible coût |
| Qui tranche | l'utilisateur, sur proposition du réseau | le noyau, ou l'expert propriétaire du sujet |
| Format | collégiale | arbitrage direct ou panel |

## Choisir le format le plus léger qui suffit

| Format | Agents lancés | Quand |
|---|---|---|
| **Arbitrage direct** | aucun | décision de type 2, comptes rendus concordants : le noyau tranche avec la grille de critères |
| **Panel** | un seul (`rapporteur`) | décision de type 2 avec plusieurs métiers concernés, ou type 1 en mode `eclair` : le rapporteur instruit chaque point de vue à partir des documents, puis recommande |
| **Collégiale** | un par métier concerné (2 à 5, de métiers différents), plus `contradicteur` et `rapporteur` | décision de type 1, désaccord entre pôles, plénière d'audit |

## Déroulé d'une collégiale

1. **Dossier de séance** (noyau). Écrire `00-pilotage/reunions/<aaaammjj>-<sujet>/dossier.md` : la question en une
   phrase, les options (deux à quatre, dont « ne rien faire » si pertinent), les critères de choix pondérés, les
   pièces à lire (chemins), le décideur. 200 mots au plus.
2. **Tour 1 : positions séparées, en parallèle.** Chaque participant écrit `position-<agent>.md` sans voir celles
   des autres, pour que les avis restent indépendants. Reprendre l'agent qui a produit le livrable concerné
   quand c'est possible. Format imposé, 200 mots au plus :
   option recommandée ; trois arguments avec leur preuve ; risques de cette option ; conditions de réussite ;
   ce qui me ferait changer d'avis ; confiance.
3. **Contradiction.** Le `contradicteur` lit le dossier et toutes les positions, puis écrit `contradiction.md` :
   les objections les plus fortes à l'option majoritaire, les angles morts communs, les questions restées sans
   réponse. 250 mots au plus.
4. **Tour 2 : réponses, en parallèle.** Le `rapporteur` rédige `synthese-tour-1.md` (300 mots : accords,
   désaccords, objections). Chaque participant est repris, la lit, et écrit `reponse-<agent>.md` en 120 mots :
   je maintiens ou j'évolue, et ma réponse aux objections qui me visent. Il n'y a pas de troisième tour.
   Si toutes les positions concordaient au tour 1 et que la contradiction ne soulève aucune objection de nature
   à changer la décision, passer directement à l'arbitrage : un second tour n'apporterait que du coût.
5. **Arbitrage.** Le `rapporteur` rédige le procès-verbal (gabarit dans `references/gabarits.md`) : grille de
   critères notée par option, points d'accord, désaccords persistants avec leurs auteurs, recommandation.
   Le décideur tranche. Pour un type 1, présenter à l'utilisateur les options, la recommandation, les désaccords
   et ce que coûterait un changement d'avis ultérieur. En autonomie `autonome`, le chef d'orchestre tranche
   lui-même sur la recommandation, en préférant l'option la plus facile à défaire, et l'utilisateur reçoit ces
   éléments au bilan final.
6. **Trace.** PV dans `00-pilotage/reunions/PV-<aaaammjj>-<sujet>.md` ; décision au registre
   (`cortex.py registre decisions ajouter …`, statut `a-valider` tant que l'utilisateur n'a pas confirmé un
   type 1, ou `provisoire` en autonomie `autonome`, avec l'option de repli et le coût d'annulation dans « motifs ») ; actions au registre des actions ; contrôles de couverture concernés mis à jour.

## Règles du débat

- **La preuve pèse plus que l'opinion.** Un argument cite un document, une mesure, un texte, une source.
- **Le métier concerné pèse plus sur son terrain.** Sécurité sur un risque de sécurité, juriste sur la légalité,
  finance sur les coûts. Une opposition motivée du juriste ou de la sécurité sur un point bloquant ne se lève que
  par une décision explicite de l'utilisateur, inscrite comme risque accepté.
- **Le désaccord se consigne, il ne se dissout pas.** Le PV nomme qui n'était pas d'accord et pourquoi. Une fois
  la décision prise, tout le monde l'applique.
- **Des avis réellement indépendants.** Des experts de même métier qui lisent les positions des autres se
  rangent vite à l'avis dominant, pour plus cher. La valeur vient de métiers différents qui écrivent séparément,
  puis d'un contradicteur : l'unanimité rapide est un signal d'angle mort à lui faire examiner, pas une preuve.
- **Une décision peut être « pas encore ».** Si une information manquante changerait le choix et peut être
  obtenue à bas coût, la décision est de l'obtenir, avec un responsable et une échéance.

## Si tu es rapporteur ou contradicteur

Le skill est préchargé pour toi. Applique le format de ta pièce (synthèse, PV, contradiction) et tiens-toi aux
longueurs : la réunion doit rester lisible d'un coup d'œil par le décideur.

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/types-de-reunions.md` | pour choisir les participants et l'ordre du jour d'une réunion type : comité d'opportunité, de cadrage, d'architecture, go/no-go, plénière d'audit, rétrospective, cellule de crise |
| `${CLAUDE_SKILL_DIR}/references/gabarits.md` | pour écrire un dossier de séance, une position, un PV |
