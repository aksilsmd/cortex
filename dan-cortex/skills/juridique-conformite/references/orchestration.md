# Orchestration du pôle Juridique et conformité

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier. Rappel à porter dans chaque ordre de mission : les livrables préparent le travail d'un avocat ou d'un expert-comptable et ne valent pas conseil juridique ou fiscal.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `juriste-numerique` | A | J1 pré-diagnostic ; J3 vagues 3A (conformité réglementaire) et 3B (documents) ; J5 dossier de conformité ; en continu pour les revues |
| `delegue-protection-donnees` | B | J2 cartographie des données ; J3 registre, AIPD, politiques ; J5 dossier de conformité (volet données) ; dès qu'il y a des données personnelles |

`juriste-numerique` est de niveau A et dispose d'un **droit d'opposition motivée** : sur un point bloquant (activité interdite, absence de base légale, infraction probable, obligation légale non traitée), il peut s'opposer en réunion ; l'opposition est inscrite au registre des décisions et ne se lève que par une décision de type 1 de l'utilisateur, prise en connaissance de la motivation.

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J1, 1A | `juriste-numerique` : pré-diagnostic (activité réglementée, pays, obstacles, obligations structurantes) | fiche projet, étude de marché | `01-decouverte/prediagnostic-juridique.md` |
| J2, 2A | `delegue-protection-donnees` : cartographie des données ; `juriste-numerique` relit le cahier des charges (conformité) | cahier des charges en cours | `02-cadrage/cartographie-donnees.md`, constats de revue |
| J3, 3A | `juriste-numerique` : conformité réglementaire, risque pénal, propriété intellectuelle ; `delegue-protection-donnees` : registre, AIPD si requise | cahier des charges, architecture en cours | `03-conception/juridique/conformite-reglementaire.md`, `registre-traitements.md`, `aipd.md` |
| J3, 3B | `juriste-numerique` : mentions, CGU, CGV, contrats, `propriete-intellectuelle.md` ; `delegue-protection-donnees` : politiques de confidentialité et de cookies | SFD, parcours d'achat, prix et offre | `mentions-legales.md`, `cgu.md`, `cgv.md`, `contrats.md`, `politique-confidentialite.md`, `politique-cookies.md` |
| J5, 5A | `juriste-numerique` et `delegue-protection-donnees` : dossier de conformité | recette, rapports de sécurité et d'accessibilité | `05-validation/dossier-conformite.md` |

## Essaimage

- **Plusieurs pays** : une instance de `juriste-numerique` par territoire au-delà de deux, avec le même pré-diagnostic en entrée ; Algérie, Maroc et Tunisie chacun sur son instance.
- **Plusieurs documents** : une instance par grand document (CGV, contrats, PI) si la vague 3B est lourde, sur le même plan type.
- Veille de textes : un `collecteur-web` avec la liste des sources officielles et les dates à retrouver.

## Dépendances à respecter

Le pré-diagnostic précède le cadrage. Les CGV attendent le modèle de prix, les moyens de paiement et les pays. Les mentions légales attendent l'hébergeur (`infrastructure.md`), la conformité des paiements le choix du prestataire, les licences `dependances.md`. Le dossier de conformité attend les rapports de sécurité, d'accessibilité et de recette.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Pré-diagnostic et conformité réglementaire | `architecte-solution` (faisabilité), `controleur-financier` (coût), `delegue-protection-donnees` |
| CGV, CGU, mentions | `stratege-marketing` (promesses, prix), `redacteur-contenu-localisation`, `concepteur-ux` (parcours d'achat) |
| Contrats et PI | `gardien-des-normes` (licences), `architecte-solution` |
| Plan marketing, prospection, avis, influence | `juriste-numerique` relit avant tout lancement de campagne |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Entrer sur un marché à régime strict (Algérie : hébergement local, paiement bancaire) ou une activité réglementée | 1 | comité d'opportunité ou de cadrage |
| Forme sociale, assurances, statut de marketplace ou d'intermédiaire de paiement | 1 | comité de cadrage, avis d'un professionnel |
| Licence du produit, politique de licences libres (copyleft accepté ou non) | 1 | comité d'architecture |
| Risque pénal ou fiscal accepté | 1 | collégiale, nom du décideur au registre |
| Niveau d'accessibilité visé | 1 si obligation légale | comité de cadrage |

## Sortie du pôle par jalon

- **J1 :** `prediagnostic-juridique.md` présent, contrôles `JUR-` de J1 traités, opposition éventuelle inscrite.
- **J2 :** exigences légales dans le cahier des charges ; contrôles `JUR-`, `PEN-`, `FIS-` de J2 traités.
- **J3 :** `conformite-reglementaire.md` et documents juridiques présents (projets « à valider ») ; `cortex.py docs verifier` sans erreur ; contrôles de J3 traités.
- **J5 :** `dossier-conformite.md` présent, aucune opposition ouverte, contrôles de J5 clos ou risque accepté nommément.
- **J6 :** documents publiés tels que validés, veille de textes datée de moins de 30 jours.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | `juriste-numerique` seul, fusion du rôle du délégué ; pré-diagnostic et documents essentiels (mentions, CGV, confidentialité) ; contrôles bloquants seulement |
| `standard` | comme décrit |
| `integral` | une instance par territoire, contrats détaillés, revue pénale complète, veille de textes à chaque jalon, avis d'un avocat recommandé avant J5 |

## Outils extérieurs

Aucun connecteur requis. Si la session offre Légifrance ou EUR-Lex, dater chaque texte avec ; sinon marquer « à vérifier » et lister les textes à recouper dans le dossier de conformité.
