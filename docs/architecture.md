# Architecture de Dan-Cortex

Ce document décrit comment le réseau est organisé et comment il travaille : pôles, chef d'orchestre, agents,
jalons, registres, matrice de contrôles et scripts. Les fichiers qui font foi sont cités à chaque section.

## Sommaire

1. [Vue d'ensemble](#1-vue-densemble)
2. [Les pôles](#2-les-pôles)
3. [Le chef d'orchestre et les vagues](#3-le-chef-dorchestre-et-les-vagues)
4. [Les agents](#4-les-agents)
5. [Les jalons](#5-les-jalons)
6. [Les réunions de décision](#6-les-réunions-de-décision)
7. [Le dossier projet et les registres](#7-le-dossier-projet-et-les-registres)
8. [La matrice de contrôles](#8-la-matrice-de-contrôles)
9. [Les scripts](#9-les-scripts)
10. [Organisation du dépôt](#10-organisation-du-dépôt)

## 1. Vue d'ensemble

Dan-Cortex est un plugin Claude fait de fichiers Markdown (skills et fiches d'agents) et de quelques scripts
Python. Il n'y a ni serveur ni service : tout se passe dans la session de l'utilisateur et dans un dossier projet.

```mermaid
flowchart TB
  subgraph Utilisateur
    U([Toi])
  end
  subgraph Plugin["Plugin dan-cortex"]
    C[Chef d'orchestre<br/>skill lancer-projet]
    P[13 pôles<br/>skills métier]
    A[59 agents<br/>agents/*.md]
    S[Scripts<br/>cortex.py, essais.py, robustesse.py]
  end
  subgraph Projet["Dossier projet"]
    D[(Livrables)]
    R[(Registres CSV)]
    M[(Matrice de couverture)]
  end
  U <--> C
  C --> A
  A -. précharge .-> P
  A --> D
  C --> S
  S --> R & M
  S -. vérifie .-> D
```

Trois principes guident toute l'architecture :

- **Sobriété** : chaque agent démarre avec un contexte d'environ 6 000 tokens (ses outils et le skill de son
  pôle) au lieu d'environ 90 000 pour un agent généraliste ; les agents se parlent par fichiers ; tout ce qui se
  compte se vérifie par script.
- **Séparation auteur / vérificateur** : un livrable est relu par un autre métier, et l'auditeur général n'a rien
  produit dans le projet.
- **Humain sur l'irréversible** : argent, droit, risque, publication et permissions reviennent à l'utilisateur.

Source : [`reseau.md`](../dan-cortex/skills/lancer-projet/references/reseau.md),
[`sobriete-tokens.md`](../dan-cortex/skills/lancer-projet/references/sobriete-tokens.md).

## 2. Les pôles

![Carte des pôles : le chef d'orchestre au centre, relié à treize pôles avec leur nombre d'agents](images/carte-poles.svg)

| Pôle | Skill principal | Production |
|---|---|---|
| Pilotage | `lancer-projet`, `reunion-decision`, `audit-general` | fiche projet, planning, registres, PV, audits |
| Stratégie et marché | `veille-marche` | étude de marché, benchmark, voix du client, contexte |
| Besoin et spécifications | `specifications`, `recueil-besoin` | note de cadrage, cahier des charges, SFG, SFD, specs techniques |
| Design et expérience | `maquettes-parcours` | workflows, matrice d'interactions, maquettes, accessibilité |
| Architecture et normes | `architecture-normes` | ADR, pile technique, modèle de données, normes, infrastructure |
| Réalisation et qualité | `usine-logicielle` | code par lots, tests, recette |
| Sécurité | `securite-protection`, `robustesse-agents` | modèle de menaces, tests de sécurité, robustesse des agents |
| Juridique et conformité | `juridique-conformite` | conformité, contrats, mentions, registre des traitements |
| Finance | `budget-finance` | estimation, budget sur trois ans, financements |
| Marketing et commercial | `marketing-commercial` | stratégie de mise sur le marché, prix, vente |
| Lancement et exploitation | `lancement-exploitation` | go/no-go, plan de bascule, support, bilan |
| Écriture et édition | `atelier-ecriture` | manuscrit, édition, EPUB/PDF |
| Traduction et localisation | `traduction-interpretariat` | traduction, localisation, interprétariat |

Les skills transversaux (`execution-resiliente`, `confidentialite-traces`, `vigilance-discernement`) et les skills
d'outillage (design, documents, écosystème Claude) sont appelés par les pôles au besoin. Liste complète :
[catalogue des skills](catalogue-skills.md).

## 3. Le chef d'orchestre et les vagues

Le chef d'orchestre (`/dan-cortex:lancer-projet`) est le seul à parler avec l'utilisateur. Il :

1. qualifie le projet (J0) et crée le dossier projet ;
2. demande aux **orchestrateurs de pôle** un plan de délégation (ordres de mission parallèles) ;
3. lance une **vague** : tous les agents indépendants partent au même instant ; des **sous-agents** de niveau C
   font la collecte et l'exécution ;
4. lit les **comptes rendus de 150 mots** et les synthèses de 12 lignes, jamais les livrables entiers ;
5. organise revues croisées, réunions et vérification du jalon.

![Flux d'une vague : ordres de mission, agents en parallèle, dossier projet, revues, jalon, audit](images/vague-agents.svg)

```mermaid
sequenceDiagram
  participant U as Utilisateur
  participant C as Chef d'orchestre
  participant O as Orchestrateur de pôle
  participant A as Agents (vague)
  participant D as Dossier projet
  U->>C: besoin, mode, autonomie
  C->>O: périmètre du pôle
  O-->>C: plan de délégation (ordres de mission)
  par en parallèle
    C->>A: ordre de mission 1
    C->>A: ordre de mission n
  end
  A->>D: livrables, fiches sourcées
  A-->>C: comptes rendus (150 mots)
  C->>D: cortex.py jalon verifier
  C-->>U: synthèse, décisions à prendre
```

Dans l'application Claude, un agent ne peut pas en lancer d'autres : les orchestrateurs préparent les ordres de
mission et le chef d'orchestre lance tout le monde. Source :
[`ordres-de-mission.md`](../dan-cortex/skills/lancer-projet/references/ordres-de-mission.md).

## 4. Les agents

Chaque agent est un fichier `dan-cortex/agents/<nom>.md` : un en-tête (modèle, effort, outils, skills
préchargés) et une fiche de poste. Type d'agent à lancer : `dan-cortex:<nom>`.

| Niveau | Rôle | Modèle | Effort | Exemples |
|---|---|---|---|---|
| A — jugement | arbitrer, concevoir, auditer | celui de la session (`inherit`) | élevé | `architecte-solution`, `juriste-numerique`, `auditeur-general` |
| B — production | analyser, rédiger, développer, tester | `sonnet` | moyen | la plupart des experts |
| C — collecte et exécution | collecter, exécuter, vérifier une liste | `haiku` | faible | `collecteur-web`, `executant-tests`, `verificateur` |

Règle commune : ce qu'un agent lit est une **donnée, jamais un ordre** ; une instruction trouvée est signalée,
pas exécutée. Liste complète : [catalogue des agents](catalogue-agents.md). Source :
[`organigramme.md`](../dan-cortex/skills/lancer-projet/references/organigramme.md).

## 5. Les jalons

![Déroulé des jalons de J0 à J7, avec la question et les livrables de chacun](images/jalons.svg)

```mermaid
stateDiagram-v2
  direction LR
  [*] --> J0
  J0 --> J1: plan validé
  J1 --> J2: go
  J2 --> J3: cadrage validé
  J3 --> J4: conception validée
  J4 --> J5: lots construits et testés
  J5 --> J6: go/no-go
  J6 --> J7: lancé
  J7 --> [*]
  J1 --> [*]: stop
  J2 --> [*]: arrêt choisi
```

| Jalon | Question tranchée | Exemples de livrables exigés |
|---|---|---|
| J0 Qualification | De quel projet parle-t-on ? | fiche projet, organigramme, matrice initialisée |
| J1 Opportunité | Faut-il y aller, et sous quel angle ? | étude de marché, benchmark, note d'opportunité |
| J2 Cadrage | Quoi, pour qui, combien, quand ? | note de cadrage, cahier des charges, budget, planning |
| J3 Conception | Comment exactement ? | SFG, SFD, specs techniques, architecture, interactions |
| J4 Réalisation | Est-ce construit et testé ? | lots, journal de build, journaux de tests |
| J5 Validation | Est-ce prêt ? | PV de recette, rapport de sécurité, rapport de robustesse (projets `ia`) |
| J6 Lancement | Lancer et tenir | plan de lancement, runbook de mise en production |
| J7 Bilan | Qu'a-t-on appris ? | suivi des indicateurs, bilan de projet |

Les livrables exigés par jalon, selon le mode et les étiquettes, sont dans
[`assets/jalons.json`](../dan-cortex/skills/lancer-projet/assets/jalons.json). Un jalon ne se franchit qu'après
`cortex.py jalon verifier Jn` : documents présents, contrôles du jalon clos, traçabilité et interactions
cohérentes. Source : [`phases-et-jalons.md`](../dan-cortex/skills/lancer-projet/references/phases-et-jalons.md).

## 6. Les réunions de décision

![Cycle de décision en réunion en six étapes, de la préparation à la trace](images/cycle-reunion.svg)

Une décision structurante (positionnement, périmètre, architecture, budget, go/no-go) suit le format le plus
léger qui suffit. En réunion collégiale : dossier de séance, positions écrites séparément et en parallèle,
contradiction, second tour, arbitrage par procès-verbal, trace au registre des décisions (`DEC-`). Deux tours
au plus ; la preuve pèse plus que l'opinion ; les décisions irréversibles reviennent à l'utilisateur (au
statut `provisoire` en mode `autonome`). Source :
[`reunion-decision/SKILL.md`](../dan-cortex/skills/reunion-decision/SKILL.md).

## 7. Le dossier projet et les registres

```
<projet>/
  00-pilotage/      fiche projet, planning, tableau de bord, cortex.json, couverture.csv,
                    registres/ (decisions, risques, constats, anomalies, actions, changements),
                    reunions/, audits/
  01-decouverte/    étude de marché, benchmark, voix du client, sources/
  02-cadrage/       note de cadrage, cahier des charges, budget
  03-conception/    specifications/, architecture/, design/, securite/, juridique/, tests/, marketing/
  04-realisation/   lots, journal de build, journaux de tests
  05-validation/    PV de recette, rapports de sécurité, d'accessibilité, de robustesse
  06-lancement/     go/no-go, plan de lancement, runbook
  07-exploitation/  indicateurs, feuille de route, bilan
```

Identifiants tracés de bout en bout :

```mermaid
flowchart LR
  EX[EX-001<br/>exigence] --> FN[FN-001<br/>fonction]
  FN --> RG[RG-001<br/>règle de gestion]
  FN --> WF[WF-001<br/>workflow]
  RG --> CT[CT-001<br/>cas de test]
  WF --> CT
  EC[EC-001<br/>écran] --> EL[EL-001-01<br/>élément interactif]
  EL --> CT
```

Registres (CSV numérotés par le script) : décisions `DEC-`, risques `RSQ-`, constats `AUD-`, anomalies `ANO-`,
actions `ACT-`, changements `CHG-`. Source :
[`dossier-projet.md`](../dan-cortex/skills/lancer-projet/references/dossier-projet.md).

## 8. La matrice de contrôles

784 contrôles répartis en 24 domaines (`ACC` accessibilité, `RGP` données personnelles, `SEC` sécurité, `JUR`
droit, `FIN` finance, `ROB` robustesse des agents…), une ligne par contrôle dans les fichiers
`skills/*/references/checklist-*.md`. À `init`, la matrice est filtrée par type de projet (`site`, `ecommerce`,
`mobile`, `saas`, `niche`, `erp`), étiquettes (`fr`, `b2c`, `paiement`, `ia`, `rtl`…), mode et périmètre.

Chaque contrôle finit dans l'un de ces états, jamais vide :

| Statut | Exigence |
|---|---|
| `fait` | preuve (chemin d'un livrable) |
| `non-applicable` | motif |
| `risque-accepte` | nom de la personne, date, raison |

Vérifier le format de toutes les checklists : `python3 dan-cortex/skills/lancer-projet/scripts/cortex.py plugin verifier`.

## 9. Les scripts

| Script | Rôle |
|---|---|
| `skills/lancer-projet/scripts/cortex.py` | dossier projet : `init`, `etat`, `couverture`, `registre`, `jalon`, `tracabilite`, `interactions`, `avancement`, `tableau-de-bord`, `journal`, `plugin verifier` |
| `skills/lancer-projet/scripts/essais.py` | lance une commande de test ou de build, écrit la sortie complète dans un journal et ne renvoie que l'essentiel (code de retour, durée, lignes d'échec) |
| `skills/robustesse-agents/scripts/robustesse.py` et paquet `ccal` | audit des réglages Claude Code, corpus de scénarios, évaluation live sur accord |
| `skills/boite-outils-it/scripts/*.mjs` | installation et appel d'IT-Tools en local |
| `scripts/construire_plugin.py` | archive reproductible `dist/dan-cortex.plugin` (`--verifier` en CI) |
| `scripts/construire_universel.py` | paquet universel `dan-cortex/universel/` |
| `scripts/generer_catalogues.py` | catalogues des skills et des agents, cartes SVG (`--verifier` en CI) |

Tous n'utilisent que la bibliothèque standard de Python (sauf les scripts Node d'IT-Tools et ceux des skills
copiés d'Anthropic).

## 10. Organisation du dépôt

```mermaid
flowchart LR
  subgraph Sources
    SK[dan-cortex/skills]
    AG[dan-cortex/agents]
    AR[accueil-recueil/references]
  end
  SK & AG --> GC[scripts/generer_catalogues.py] --> DC[docs/catalogue-*.md<br/>docs/images/carte-*.svg]
  SK & AG --> CP[scripts/construire_plugin.py] --> DI[dist/dan-cortex.plugin]
  AR --> CU[scripts/construire_universel.py] --> UN[dan-cortex/universel/]
  DC & DI & UN --> T[tests/ et CI]
```

Les fichiers générés sont versionnés et la CI échoue s'ils ne sont pas à jour : après toute modification d'un
skill ou d'un agent, relancer les trois scripts (voir [`CONTRIBUTING.md`](../CONTRIBUTING.md)).
