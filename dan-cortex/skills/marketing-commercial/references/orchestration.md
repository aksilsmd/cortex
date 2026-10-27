# Orchestration du pôle Marketing et commercial

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `stratege-marketing` | B | J2, vague 2A (stratégie de marché) ; J3, vague 3B (plan marketing) ; J6, vague 6A (plan de communication) |
| `expert-acquisition` | B | J3, vague 3B (canaux, mesure, plan de marquage) ; J6, vague 6A (campagne) |
| `responsable-commercial` | B | J3, vague 3B (prix, offre, plan commercial) ; seulement si vente à des entreprises, comptes à accompagner ou prix à construire |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J2, 2A | `stratege-marketing` : cible, positionnement, message, canaux, modèle de prix envisagé | note d'opportunité, benchmark, voix du client, fiche projet | `02-cadrage/strategie-marche.md` |
| J3, 3B | `stratege-marketing` : plan marketing ; `expert-acquisition` : canaux, indicateurs, plan de marquage ; `responsable-commercial` : prix et offre, plan commercial | strategie-marche, cahier des charges, budget, indicateurs unitaires du contrôleur financier | `03-conception/marketing/plan-marketing.md`, `prix-offre.md`, `plan-commercial.md` |
| J6, 6A | `stratege-marketing` : plan de communication ; `expert-acquisition` : campagne prête à lancer | plan-marketing, plan de lancement, checklist go/no-go | `06-lancement/plan-communication.md` |

Au jalon J3, le pôle part dans la même vague que les rédacteurs de spécifications : il lit le cahier des charges et la stratégie de marché, pas les SFD.

## Essaimage

- Un `expert-acquisition` par canal lourd (référencement et contenu, stores, publicité) seulement si plus de trois canaux prioritaires et un budget d'acquisition significatif.
- Un `responsable-commercial` par segment si le projet vise des segments aux processus d'achat différents (PME et grand compte).
- Un `stratege-marketing` par marché ou langue au-delà de deux, avec le même fichier de stratégie en entrée.

## Dépendances à respecter

La stratégie de marché précède le plan marketing. Le prix et l'offre précèdent le plan commercial et le message de lancement. Le plan de marquage précède la recette des balises (pôle Lancement). Les indicateurs unitaires (marge, coût de service, coût d'acquisition admissible) viennent de `controleur-financier` : si absents, les demander avant de fixer un prix. Les documents juridiques (CGV, CGU, politique de cookies) doivent être cohérents avec l'offre réelle : fournir le prix et les paliers au `juriste-numerique` dès que stabilisés.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Stratégie de marché et plan marketing | `juriste-numerique` (allégations, prospection, influence), `controleur-financier` (rentabilité), `stratege-produit` (cohérence du positionnement) |
| Prix et offre | `controleur-financier`, `juriste-numerique` (affichage du prix, essai, reconduction, promotions) |
| Plan commercial | `juriste-numerique` (contrats, appels d'offres), `responsable-support-formation` (service promis) |
| Plan de marquage | `delegue-protection-donnees` (consentement, exemption), `architecte-securite` (balisage serveur) |
| Plan de communication | `juriste-numerique`, `responsable-lancement` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Positionnement et segment prioritaire | 1 | comité d'opportunité ou de cadrage |
| Modèle de prix et métrique de facturation | 1 | collégiale ; présenter deux ou trois options chiffrées |
| Nom de marque | 1 si création, sinon 2 | trois options à l'utilisateur, antériorités vérifiées par le juriste |
| Budget d'acquisition et répartition des canaux | 1 | comité de cadrage |
| Seuil de passage à l'acquisition payante | 2 | arbitrage direct |
| Partenariats exclusifs ou revendeurs | 1 | collégiale |

## Sortie du pôle par jalon

- **J2 :** `strategie-marche.md` présent, avec ICP, positionnement, modèle de croissance et paliers.
- **J3 :** plan marketing, prix et offre, plan commercial (si applicable) présents ; contrôles `MKT-` et `COM-` de jalon J3 traités ; revue du juriste faite.
- **J6 :** plan de communication prêt, validé par l'utilisateur ; contrôles de jalon J5 et J6 traités.
- **J7 :** bilan des indicateurs par canal fourni à `responsable-lancement`.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | `stratege-marketing` seul, rôles fusionnés (acquisition, commercial, lancement) ; un fichier `strategie-marche.md` étoffé tient lieu de plan marketing ; prix par méthode simple, sans étude de sensibilité |
| `standard` | comme décrit |
| `integral` | essaims par canal et par segment ; étude de prix par questionnaire proposée à l'utilisateur ; contre-lecture du plan par `contradicteur` ; plan de crise simulé |

## Outils extérieurs

Si des connecteurs de gestion de campagnes, d'e-mailing, d'analytique ou de CRM sont présents, les agents préparent les contenus et la configuration, sans jamais publier ni envoyer : l'utilisateur déclenche. Sans connecteur, livrer des fichiers prêts à importer (calendrier, textes, tableau de marquage).
