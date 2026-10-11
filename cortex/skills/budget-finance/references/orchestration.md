# Orchestration du pôle Finance

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `controleur-financier` | B | J1 (ordres de grandeur), J2 vague 2B (budget), J3 vague 3B (budget révisé), J5 (budget de lancement), J7 (réel contre budget) |

Un seul agent : il travaille en binôme avec `planificateur` (charges), `architecte-solution` et `ingenieur-devops` (architecture, hébergement), et `responsable-commercial` (prix).

## Vagues types

| Jalon et vague | Mission | Entrées | Sorties |
|---|---|---|---|
| J1, 1A | ordres de grandeur de coût et modèle économique | fiche projet, étude de marché, note de faisabilité technique | section versée dans `01-decouverte/note-opportunite.md` |
| J2, 2B | budget complet, trois scénarios, justification, financements | cahier des charges, `planning.md` (O, M, P), architecture préliminaire, stratégie de marché | `02-cadrage/budget.md` |
| J3, 3B | budget révisé et découpage par lot | `infrastructure.md`, `dependances.md`, SFD, `planning.md` détaillé, `prix-offre.md` | `budget.md` révisé, écarts expliqués |
| J5, 5A | budget de lancement et du premier trimestre | `checklist-go-no-go.md`, coûts engagés | contrôle `FIN-029` |
| J7, 7A | réel contre budget | factures, `suivi-indicateurs.md` | partie financière de `bilan-de-projet.md` |

## Essaimage

Aucun en général : un budget cohérent a un seul auteur. En mode `integral`, une seconde instance produit la **contre-estimation indépendante** sans lire la première, puis le contrôleur compare les écarts.

## Dépendances à respecter

Le budget de J2 attend les charges du `planificateur` : en mode `eclair` seulement, le contrôleur produit budget et planning ensemble. L'hébergement vient de l'`ingenieur-devops`, qui chiffre à partir de la volumétrie ; si l'architecture n'existe pas encore, le budget pose une hypothèse écrite et marque le poste « à confirmer en J3 ». Le prix de l'offre précède le modèle économique.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Budget et trésorerie | `planificateur` (charges), `architecte-solution` (hébergement, dépendances), `contradicteur` (hypothèses de revenu) |
| Postes juridique, sécurité, données | `juriste-numerique`, `architecte-securite`, `delegue-protection-donnees` |
| Hypothèses de prix, CAC, acquisition | `responsable-commercial`, `stratege-marketing` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Budget de la première version et réserves | 1 | comité de cadrage |
| Seuil d'arrêt et jalons go/no-go chiffrés | 1 | comité de cadrage |
| Plan de financement : dette, aides, levée de fonds | 1 | comité de cadrage |
| Acheter, configurer ou construire, sur le coût sur trois ans | 1 | comité d'architecture |
| Hypothèse de gain de productivité des agents IA | 2 | arbitrage direct |

Présenter le budget en trois scénarios, l'écart avec le budget souhaité et les options de périmètre.

## Sortie du pôle par jalon

- **J1 :** ordres de grandeur dans la note d'opportunité, contrôles `FIN-` de jalon J1 traités.
- **J2 :** `budget.md` présent avec synthèse, trois scénarios, trésorerie, sensibilité ; contrôles `FIN-` de J2 traités, dont les bloquants.
- **J3 :** budget révisé, écarts expliqués ; demandes de changement chiffrées.
- **J5 :** budget de lancement confirmé. **J7 :** réel contre budget.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | le contrôleur produit budget et planning ; deux méthodes remplacées par une seule justifiée ; trois scénarios gardés, sensibilité sur les trois leviers dominants |
| `standard` | comme décrit |
| `integral` | estimation à trois points complète, analyse de sensibilité par script, contre-estimation indépendante, ateliers simulés avec les pôles |

## Outils extérieurs

Un tableur ou un script Python (`python3`) produit les calculs ; le joindre au dossier. Aucun accès bancaire, comptable ou de facturation n'est utilisé sans accord explicite de l'utilisateur.
