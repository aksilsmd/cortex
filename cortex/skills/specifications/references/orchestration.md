# Orchestration du pôle Besoin et spécifications

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `expert-cahier-des-charges` | B | J2, vague 2A : note de cadrage puis cahier des charges |
| `redacteur-sfg` | B | J3, vague 3A, dès que le cahier des charges est accepté |
| `redacteur-sfd` | B | J3, vague 3B, en essaim : une instance par module |
| `redacteur-specs-techniques` | B | J3, vague 3B, une instance (deux au-delà de dix interfaces externes) |

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J2, 2A | `expert-cahier-des-charges` : note de cadrage, puis cahier des charges, dans la même mission | fiche projet, note d'opportunité, analyses de J1, `personas-parcours.md` si déjà disponible | `02-cadrage/note-de-cadrage.md`, `02-cadrage/cahier-des-charges.md` |
| J3, 3A | `redacteur-sfg` : acteurs, fonctions, processus, objets métier, liste des modules ; en binôme `cartographe-interactions` (workflows) | cahier des charges, personas, dossier d'architecture en cours | `03-conception/specifications/sfg.md` |
| J3, 3B | `redacteur-sfd` en essaim, un module chacun ; `redacteur-specs-techniques` | SFG, workflows, ADR, modèle de données | `specifications/sfd/<module>.md`, `specifications/specs-techniques.md` |

Après la vague 3B, lancer toi-même, sans agent : `cortex.py tracabilite verifier`, `cortex.py docs verifier`.
Renvoyer chaque erreur à l'auteur de la ligne en cause. Le cahier de recette (`concepteur-tests`) vient après la
SFD : la chaîne n'est complète qu'à ce moment-là.

## Essaimage

- **SFD :** une instance de `redacteur-sfd` par module de la SFG, plus une pour le module `commun` (comptes,
  droits, notifications, consentement, journalisation, paramétrage). Donner à chacune : la SFG complète (sections
  acteurs, glossaire, objets métier), les `FN-` de son module, le cahier des charges limité aux `EX-` concernés,
  sa **plage d'identifiants `RG-`** (par exemple 100 par module : RG-100 à RG-199, RG-200 à RG-299 ; le module
  `commun` reçoit la première plage) et le chemin des SFD voisines pour les renvois.
- Un module se découpe au plus à 15 fonctions `FN-`. Au-delà, scinder, sinon l'instance dérive.
- **Cahier des charges :** une seule instance. En mode `integral` et au-delà de 80 exigences, une instance par
  thème (exigences non fonctionnelles à part), consolidée par la première.
- **Spécifications techniques :** une instance par famille d'interfaces (externes, internes, traitements par lots)
  si plus de dix contrats.

## Dépendances à respecter

La note de cadrage précède le cahier des charges. Celui-ci précède la SFG. La SFG (liste des modules et plages
d'identifiants) précède l'essaim de SFD. L'architecture validée en comité (langage, structure, données) précède
les spécifications techniques. Le binôme `redacteur-sfd` et `cartographe-interactions` partage le chemin des
livrables : une règle sans écran et un écran sans règle sont des manques à se signaler mutuellement.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Cahier des charges | `architecte-solution`, `concepteur-tests`, `juriste-numerique`, `controleur-financier` |
| SFG | `expert-cahier-des-charges`, `concepteur-ux`, `architecte-donnees` |
| SFD | `concepteur-tests`, développeur concerné, `delegue-protection-donnees` |
| Spécifications techniques | `architecte-solution`, `architecte-securite`, `automaticien-tests` |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Périmètre de la première version, priorités MoSCoW du cahier des charges | 1 | comité de cadrage |
| Seuils des exigences non fonctionnelles qui coûtent cher (disponibilité, temps de reprise, charge) | 1 | comité de cadrage, avec chiffrage du `controleur-financier` |
| Cycle de vie : séquentiel, agile, hybride | 1 | comité de cadrage |
| Découpage en modules et plages d'identifiants | 2 | arbitrage direct du chef d'orchestre |
| Règle de gestion en conflit entre deux modules | 2 | arbitrage direct, ou panel si l'enjeu est financier |

## Sortie du pôle par jalon

- **J2 :** note de cadrage et cahier des charges présents ; contrôles `SPC-` de jalon J2 traités ; chaque `EX-` et
  `EXNF-` porte un critère d'acceptation ; périmètre V1 validé.
- **J3 :** SFG, SFD de tous les modules, spécifications techniques présentes ; `tracabilite verifier` sans
  erreur de l'amont (exigences, fonctions, règles) ; contrôles `SPC-` de jalon J3 traités.
- **J4 et J5 :** toute modification d'une exigence passe par une demande de changement au registre des décisions ;
  l'expert est repris pour mettre à jour les identifiants touchés.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | un seul `expert-cahier-des-charges` produit note de cadrage et cahier court (30 exigences au plus) ; un seul `redacteur-sfd` pour le parcours principal ; spécifications techniques limitées aux interfaces externes ; `redacteur-specs-techniques` omis s'il n'y en a pas |
| `standard` | comme décrit |
| `integral` | cahier des charges par thème, atelier simulé par métier avant rédaction, SFD avec exemples chiffrés par règle, spécifications techniques avec jeux de messages d'exemple, revue croisée complète |

## Outils extérieurs

Aucun requis. Si l'utilisateur tient déjà ses exigences dans un outil (tableur, Jira, Azure DevOps, Doors), importer
l'export en entrée et conserver ses identifiants comme « source » dans la colonne prévue : ne jamais renuméroter à
sa place.
