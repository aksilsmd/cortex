# Orchestration du pôle Stratégie et marché

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `analyste-marche` | B | J1, vague 1A, si le projet vise un marché externe |
| `analyste-concurrence` | B | J1, vague 1A ; produit d'abord la liste des concurrents si elle manque |
| `analyste-voix-client` | B | J1, vague 1A ; J7, vague 7A pour les premiers retours |
| `analyste-contexte` | B | J1, vague 1A, dès que plusieurs pays, un secteur régulé ou un sujet sensible sont en jeu |
| `collecteur-web` | C | J1, vague 1A ou 1A bis : une instance par concurrent ou par source, jamais en autonomie |
| `stratege-produit` | A | J1, vague 1B : tranche l'angle et écrit la note d'opportunité |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J1, 1A bis (si listes inconnues) | `analyste-concurrence` : liste des concurrents classés ; `analyste-voix-client` : liste des sources d'avis avec statut d'accès | fiche projet | listes dans les fiches de mission |
| J1, 1A | `collecteur-web` en essaim ; `analyste-marche` ; `analyste-contexte` ; `analyste-concurrence` et `analyste-voix-client` lancés en même temps que l'essaim ou repris à son retour | fiche projet, listes | `sources/concurrents/`, `sources/avis/`, `sources/marche/`, puis les quatre livrables d'analyse |
| J1, 1B | `stratege-produit`, puis `contradicteur` | les quatre analyses, avis du juriste et de l'architecte, ordres de grandeur du contrôleur financier | `01-decouverte/note-opportunite.md`, pré-mortem annexé |
| J7, 7A | `analyste-voix-client` : premiers retours comparés aux hypothèses de la note | avis réels, hypothèses `HYP-` | section de `07-exploitation/suivi-indicateurs.md` |

Les analystes synthétisent à partir des fiches et renvoient celles qui n'ont ni URL ni date.

## Essaimage

- **Concurrents :** une instance de `collecteur-web` par concurrent, gabarit de `references/veille-concurrentielle.md`, fiche dans `sources/concurrents/<slug>.md`. Retenir cinq à huit concurrents (direct d'abord), le reste en veille légère par l'analyste.
- **Voix du client :** une instance par couple source et concurrent, gabarit de `references/voix-du-client.md`, fiche dans `sources/avis/<slug>.md`. Ne lancer que les sources dont le statut d'accès autorise la lecture.
- **Marché et contexte :** une instance par pays ou par source statistique, gabarit de `references/sources-et-requetes.md`, dans `sources/marche/`.
- Donner à chaque instance : une cible, le gabarit, le budget de recherches (10 à 15), l'interdit de contournement. Bornes : 8 instances par essaim en `standard`, 16 en `integral`.

## Dépendances à respecter

La liste des concurrents et des sources précède l'essaim. Les fiches précèdent les analyses. Les quatre analyses précèdent la note d'opportunité. Les ordres de grandeur de coût du `controleur-financier` et les obstacles du `juriste-numerique` sont lus par le stratège avant de chiffrer les options. Les accès payants ou soumis à accord (licence Sensor Tower, accord écrit Reddit, outil de trafic) sont demandés à l'utilisateur avant la vague, pas pendant.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Benchmark concurrentiel | `juriste-numerique` (comparaisons, usage des marques), `architecte-solution` (pile et faisabilité) |
| Voix du client | `delegue-protection-donnees` (pseudonymisation, durée de conservation) |
| Analyse du contexte | `juriste-numerique` (facteurs légaux), `controleur-financier` (facteurs économiques) |
| Note d'opportunité | `controleur-financier` (options chiffrées), `contradicteur` (pré-mortem), `stratege-marketing` (positionnement) |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Y aller, pivoter ou renoncer | 1 | comité d'opportunité (collégiale) |
| Positionnement et segment visé | 1 | comité d'opportunité |
| Option de périmètre | 1 | comité d'opportunité, trois options chiffrées |
| Marchés et pays de la première version | 1 | comité d'opportunité, sur la base de `analyse-contexte.md` |
| Achat d'un accès de données (licence, outil de trafic) | 2 | arbitrage direct, après coût présenté |
| Lancer un test de demande auprès de prospects | 2 | arbitrage direct : l'utilisateur déclenche |

## Sortie du pôle par jalon

- **J1 :** quatre analyses, fiches de faits, note d'opportunité présentes ; contrôles `MAR-` et `CTX-` de jalon J1 traités ; décision du comité enregistrée au registre.
- **J2 :** `HYP-` restantes transmises à l'`expert-cahier-des-charges` et au `stratege-marketing` ; plan de veille périodique remis.
- **J7 :** retours réels comparés aux hypothèses de la note.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | un seul `analyste-concurrence` produit `etude-de-marche.md` couvrant marché, concurrence, voix du client et contexte (liste `MAR-` seulement, essaim de 3 collecteurs au plus), puis `stratege-produit` |
| `standard` | comme décrit |
| `integral` | essaims élargis (16), double collecte des deux concurrents principaux, entretiens ou sondage proposés à l'utilisateur, `contradicteur` sur le modèle de la session |

## Outils extérieurs

Si un connecteur de données de marché est disponible (par exemple Sensor Tower pour les applications), l'analyste le préfère au scraping. Sans accès, un échantillon lu à la main le remplace, et le livrable le dit.
