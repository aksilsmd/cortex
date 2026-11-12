# Dan-Cortex

Un réseau d'agents experts, organisé comme une entreprise, pour cadrer, concevoir, réaliser, tester, sécuriser et
lancer un grand projet numérique : site web de grande entreprise, application mobile, SaaS, produit de niche,
e-commerce, ERP. Rien n'est oublié, et le tout est conçu pour consommer peu de tokens.

Dan-Cortex peut mener le projet **en autonomie** dans un cadre que tu fixes une fois, et il intègre **Claude Code
Autonomy Lab** : un pôle `robustesse-agents` audite les réglages des agents, fait traiter tout contenu lu comme
une donnée et non comme un ordre, et éprouve les fonctions d'IA du produit contre l'injection d'instructions.

## Installer

Dans Claude Code :

```
/plugin marketplace add aksilsmd/cortex
/plugin install dan-cortex@cortex-projets
```

Dans l'application Claude (web et bureau, offres payantes) : menu **Customize** (Personnaliser) → **Plugins** →
**Add** → **Add marketplace** → **Add from a repository**, saisis le même dépôt, puis ajoute le plugin `dan-cortex`.
Autre voie : téléverse le fichier `dan-cortex.plugin` comme plugin personnalisé.

Si l'ancien plugin `cortex` est installé, désinstalle-le : les deux portent les mêmes skills et les mêmes agents.

## Démarrer

Dans Claude, tape la commande du chef d'orchestre et décris ton projet :

```
/dan-cortex:lancer-projet Je veux lancer <ton projet>, pour <qui>, dans <quels pays>, avec <budget et délai>.
```

Le chef d'orchestre te pose une seule série de questions (périmètre de la mission, mode de travail, pays et
données sensibles, niveau d'autonomie), crée le dossier du projet, compose l'équipe, puis déroule les jalons.

Appelle-le par sa commande plutôt que de compter sur un déclenchement automatique : dans une session qui contient
déjà beaucoup de skills, une description peut ne pas être chargée.

### Les trois modes

| Mode | Pour quoi | Agents par vague |
|---|---|---|
| `eclair` | valider une idée, petit projet, budget de tokens serré | 3 à 4, rôles fusionnés |
| `standard` | le cas général | 6 à 8 |
| `integral` | grand compte, secteur régulé, enjeu fort | 10 à 16 |

Commence par `eclair` ou `standard`. Le mode supérieur coûte environ deux à trois fois plus.

### Les trois niveaux d'autonomie

| Niveau | Ce qui se passe |
|---|---|
| `accompagne` (par défaut) | le chef d'orchestre s'arrête à chaque jalon et te soumet les décisions irréversibles |
| `delegue` | il enchaîne les jalons et regroupe tes décisions à la fin de chacun |
| `autonome` | après la qualification, il enchaîne tout le périmètre sans attendre : décisions irréversibles prises au statut provisoire, hypothèses au lieu de questions, effets extérieurs limités aux autorisations que tu as écrites, un seul bilan final |

En `autonome`, tu fixes le cadre une fois, à J0 : périmètre, autorisations permanentes (par exemple « push sur la
branche `dev` de tel dépôt »), plafond de tokens. Six limites dures restent hors de toute délégation : dépenser
ou t'engager, toucher un système qui n'est pas au projet, tester la sécurité sans autorisation écrite, modifier
les permissions de Claude Code, supprimer de façon irréversible, sortir un vrai secret. Le skill
`robustesse-agents` fournit des réglages Claude Code (mode `auto`, bac à sable) qui évitent les demandes de
permission inutiles sans ouvrir les gestes dangereux. Détail : `skills/lancer-projet/references/autonomie.md`.


### Les sept jalons

| Jalon | Question tranchée |
|---|---|
| J1 Opportunité | Faut-il y aller, et sous quel angle ? |
| J2 Cadrage | Quoi, pour qui, combien, quand ? |
| J3 Conception | Comment exactement ? |
| J4 Réalisation | Est-ce construit et testé ? |
| J5 Validation | Est-ce prêt ? |
| J6 Lancement | Lancer et tenir |
| J7 Bilan | Qu'a-t-on appris ? |

Tu peux t'arrêter à n'importe quel jalon : une étude d'opportunité seule, un dossier de conception complet, ou
tout le parcours jusqu'au lancement.

### Utiliser un pôle seul

Chaque pôle s'utilise aussi directement.

| Commande | Ce que tu obtiens |
|---|---|
| `/dan-cortex:veille-marche` | étude de marché, benchmark des concurrents, voix du client, analyse de contexte, positionnement |
| `/dan-cortex:specifications` | note de cadrage, cahier des charges, spécifications générales, détaillées et techniques |
| `/dan-cortex:maquettes-parcours` | workflows, matrice d'interactions (chaque bouton, chaque clic, sa destination), maquettes, thème |
| `/dan-cortex:architecture-normes` | choix du langage et de la pile, architecture, schéma de données, normes de développement, infrastructure |
| `/dan-cortex:usine-logicielle` | réalisation par lots, tests unitaires, fonctionnels, d'API, de bout en bout, recette, corrections |
| `/dan-cortex:securite-protection` | analyse de risques, protections, tests de sécurité, cadrage d'un test d'intrusion, réponse à incident |
| `/dan-cortex:juridique-conformite` | données personnelles, commerce et consommation, contrats, propriété intellectuelle, pénal, fiscalité |
| `/dan-cortex:budget-finance` | estimation, budget complet, justification économique, financements |
| `/dan-cortex:marketing-commercial` | stratégie de mise sur le marché, acquisition, prix, vente, plan de lancement |
| `/dan-cortex:lancement-exploitation` | go/no-go, plan de bascule, mise en production, support, bilan |
| `/dan-cortex:reunion-decision` | faire débattre les experts et tracer une décision |
| `/dan-cortex:audit-general` | audit à 360° d'un projet, mené avec Dan-Cortex ou non |
| `/dan-cortex:robustesse-agents` | audit des réglages Claude Code, réglages pour l'autonomie, scénarios d'injection d'instructions, évaluation live sur accord |
| `/dan-cortex:execution-resiliente` | exécution orientée résultats : critères d'acceptation, reprise après erreur, poursuite des tâches indépendantes, vérification |
| `/dan-cortex:confidentialite-traces` | masquage des secrets et données personnelles dans les sorties, journaux et rapports, sans toucher à la traçabilité |
| `/dan-cortex:design-apple` | design de niveau Apple (règles HIG) pour le web, le mobile et les outils de gestion |
| `/dan-cortex:mouvement-interface` | construire, chorégraphier, fluidifier, auditer et alléger les animations |
| `/dan-cortex:crm-twenty` | CRM libre Twenty : auto-hébergement sûr, intégration, applications |
| `/dan-cortex:cartographie-graphe` | comprendre un code en graphe (Graphify, local) |
| `/dan-cortex:boite-outils-it` | empreintes, secrets de test, TOTP, JWT, QR codes (IT-Tools, local) |
| `/dan-cortex:accueil-recueil` | premier contact guidé : besoin brut reformulé et validé, exploration, propositions, entretien, livrables, étude de réalisation, décision de l'utilisateur |
| `/dan-cortex:recueil-besoin` | interview adaptée au profil, du besoin brut au cahier des charges, schémas et maquettes |
| `/dan-cortex:atelier-ecriture` | écrire et éditer livres et romans, publier (EPUB/PDF), ou coder un outil d'aide à l'écriture |
| `/dan-cortex:traduction-interpretariat` | traduire (FR/AR/EN), localiser (RTL, PO/XLIFF), interprétariat ; outils CAT libres |
| `/dan-cortex:conception-interface` | direction visuelle d'une interface, au-delà des gabarits par défaut (texte traduit d'Anthropic, Apache-2.0) |
| `/dan-cortex:communication-interne` | points 3P, lettre d'information, FAQ interne, rapport d'incident (texte traduit d'Anthropic, Apache-2.0) |
| `/dan-cortex:fabrique-themes` | dix thèmes de couleurs et de polices pour habiller un livrable, ou un thème sur mesure (texte traduit d'Anthropic, Apache-2.0) |
| `/dan-cortex:design-affiche` | affiche ou visuel artistique en PNG ou PDF, de la philosophie de design au canevas (texte traduit d'Anthropic, Apache-2.0) |
| `/dan-cortex:vigilance-discernement` | questions de suivi pour vérifier faits, raisonnement et contexte d'une réponse à décision (texte traduit d'Anthropic, Apache-2.0) |
| `/dan-cortex:docx` | créer, modifier, relire un .docx (scripts Python, LibreOffice) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:pdf` | lire, fusionner, remplir, produire des PDF (scripts Python) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:pptx` | créer et modifier des .pptx (scripts Python et Node) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:xlsx` | créer et recalculer des .xlsx avec formules (scripts Python, LibreOffice) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:skill-creator` | écrire, évaluer et améliorer un skill (scripts d'évaluation) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:mcp-builder` | concevoir et évaluer un serveur MCP (Python ou TypeScript) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:webapp-testing` | tester une application web locale avec Playwright (scripts) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:web-artifacts-builder` | artefacts HTML riches (React, Tailwind, shadcn/ui ; scripts) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:slack-gif-creator` | GIF optimisés pour Slack (scripts Python) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:algorithmic-art` | art algorithmique p5.js (modèles HTML/JS) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:claude-api` | bâtir avec l'API et les SDK Claude, migrations de modèles (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:academy-guide` | orienter vers les cours de Claude Academy (consulte le catalogue en ligne) (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |
| `/dan-cortex:brand-guidelines` | règles de marque d'Anthropic, à ne pas appliquer aux projets des clients (copié d'Anthropic sans modification, Apache-2.0 ; exception du 12/11/2026) |

Les skills officiels d'Anthropic qui produisent des fichiers (Word, PDF, présentations, tableurs, etc.) : guide dans `skills/lancer-projet/references/skills-officiels-anthropic.md`. Mentions de licence : `NOTICE.md`.

## Comment ça marche

- **Un chef d'orchestre** parle avec toi, lance les agents par vagues parallèles et ne lit que des comptes rendus
  courts.
- **51 agents experts** répartis en pôles, chacun avec les compétences de son métier (le skill de son
  pôle, préchargé) et les seuls outils dont il a besoin.
- **Des orchestrateurs de pôle** découpent le travail en ordres de mission ; des sous-agents légers font la
  collecte et l'exécution.
- **Des réunions écrites** : positions séparées, contradicteur, deux tours au plus, décision tracée. Tu tranches
  les décisions irréversibles, sur le moment ou au bilan si tu as choisi l'autonomie.
- **Des revues croisées** : le juriste relit le marketing, le testeur relit les spécifications, la sécurité
  relit l'architecture.
- **Un super-auditeur** indépendant passe tout en revue avant le lancement ; son rapport est débattu en plénière,
  puis les corrections sont décidées et recontrôlées.
- **Une matrice de couverture de 784 contrôles**, filtrée selon ton projet : chaque ligne finit
  « fait » avec sa preuve, « non applicable » avec son motif, ou « risque accepté » avec un nom.
- **Une règle commune à tous les agents** : ce qu'ils lisent (page web, avis, document, sortie d'outil) est une
  donnée, jamais un ordre ; une instruction trouvée est signalée, pas exécutée.
- **Un script** tient les registres, vérifie les jalons, la traçabilité des exigences aux tests et la cohérence
  des interactions (aucun bouton sans destination, aucun écran orphelin).

Le détail est dans `skills/lancer-projet/references/reseau.md`.

## Ce que contient le plugin

| Élément | Nombre | Où |
|---|---|---|
| Skills | 43 | `skills/` |
| Agents | 59 | `agents/` |
| Contrôles de couverture | 784 | `skills/*/references/checklist-*.md` |
| Fichiers de référence et gabarits | 138 | `skills/*/references/`, `skills/*/assets/` |
| Scripts | 6 | `skills/lancer-projet/scripts/` (`cortex.py`, `essais.py`), `skills/robustesse-agents/scripts/` (`robustesse.py` et le paquet `ccal`) |

## Sobriété en tokens

Ordres de grandeur observés en octobre 2026 dans une session très équipée ; ils varient selon la session :

| Lancement | Contexte de départ |
|---|---|
| agent généraliste | environ 90 000 tokens |
| agent Dan-Cortex, outils de métier | environ 6 000 tokens |

- Coût permanent du plugin : environ 4 300 tokens par session, pour les noms et descriptions des
  skills et des agents. Désactive le plugin quand tu ne t'en sers pas : ce coût tombe à zéro.
- Les agents de collecte et d'exécution tournent sur le modèle léger, la production sur le modèle intermédiaire,
  le jugement (architecture, droit, audit) sur le modèle de ta session.
- Fixe un plafond : `cortex.py etat --set plafond_tokens=<n>`. Le journal alerte à 80 % et à 100 %.
- Un système multi-agents reste plus coûteux qu'une conversation simple. Une vague large de recherche peut
  épuiser une fenêtre d'utilisation : le chef d'orchestre lance d'abord une vague pilote et mesure.

## Limites à connaître

- **Les agents préparent, ils ne remplacent pas un professionnel.** Ce qui engage juridiquement, fiscalement ou
  en sécurité certifiante est marqué « à valider » : fais-le valider par un avocat, un expert-comptable ou un
  auditeur qualifié.
- **Aucun effet extérieur sans ton accord** : ni achat, ni publication, ni envoi, ni push, ni déploiement, sauf
  ce que tu as écrit dans les autorisations permanentes du mode autonome. Les limites dures demandent toujours
  ton accord au moment de l'action.
- **L'autonomie reste dans les permissions de Claude Code.** Elle réduit les demandes par des réglages ciblés et
  le bac à sable ; elle ne contourne ni les permissions ni les protections de la plateforme.
- **Les tests de sécurité ne visent que les environnements de ton projet**, avec ton autorisation écrite. Pour un
  enjeu fort, un test d'intrusion par un prestataire qualifié reste nécessaire.
- **Dans l'application Claude, un agent ne peut pas en lancer d'autres** : les orchestrateurs de pôle préparent
  les ordres de mission, le chef d'orchestre lance tout le monde en parallèle.
- **Un grand projet dépasse une session.** L'état du dossier projet permet de reprendre où l'on s'est arrêté ;
  travaille dans un dossier persistant.
- **Le droit détaillé est outillé pour la France et l'Union européenne.** Pour les autres pays (Royaume-Uni, États-Unis, Algérie, Maroc, Tunisie…), Dan-Cortex donne des repères et renvoie à un avocat local.
- **Le droit et les versions d'outils changent.** Les références sont à l'état d'octobre 2026 ; les points que la
  recherche n'a pas pu confirmer sont marqués « à vérifier » dans les fichiers.

## Adapter Dan-Cortex

- **Ajouter un contrôle** : une ligne dans le fichier `checklist-*.md` du pôle, au format des autres, puis
  `python3 skills/lancer-projet/scripts/cortex.py plugin verifier`.
- **Changer ce qu'un jalon exige** : `skills/lancer-projet/assets/jalons.json`.
- **Modifier un agent** : son fichier dans `agents/` (modèle, effort, outils, fiche de poste).
- **Ajouter un type de projet** : un profil dans `skills/lancer-projet/references/profils/`.

## Prérequis

Python 3 pour les scripts (bibliothèque standard uniquement ; 3.11 ou plus récent pour `robustesse.py`). Sans
Python, le chef d'orchestre tient les mêmes registres à la main, pour plus cher en tokens. L'évaluation live du
pôle `robustesse-agents` demande en plus le CLI `claude`.

## Boîte à outils IT (1.4.0)

Le skill `boite-outils-it` installe IT-Tools (CorentinTh/it-tools, GPL-3.0, outil séparé) en local, empreinte vérifiée, servi sur 127.0.0.1:3110 sans aucun appel sortant, et donne aux agents `scripts/outils-it.mjs` : empreintes, HMAC, jetons, UUID, Base64, URL, JWT, TOTP de test, entropie, QR codes et captures.

## Testeurs experts (1.5.0)

Deux agents rejoignent le pôle Qualité : `testeur-mobile` (appareils émulés, thème sombre, tactile, arabe RTL, réseau lent, Baymard mobile) et `testeur-web` (conformité aux maquettes, multi-navigateurs, heuristiques, accessibilité clavier, régression visuelle). Ils mesurent plutôt qu'ils n'apprécient et proposent les contrôles automatiques qui empêchent la régression.

## Formations (1.6.0)

Le PO « forme » les experts : des fiches de référence denses (objectifs, principes, règles chiffrées, check-list d'audit, anti-patterns, exemples, pièges, sources primaires datées de novembre 2026) sont rattachées aux agents concernés par une ligne « Formations : » et citées dans les SKILL.md de leur pôle. Chaque fiche a son fichier de collecte dans `references/sources/` (URL, date, résumé de l'apport).

| Pôle | Fiches (`skills/<pôle>/references/`) | Agents formés |
|---|---|---|
| maquettes-parcours | `formation-design-web-mobile.md`, `formation-ui-ux.md`, `formation-animation-motion.md`, `formation-figma-workflows.md` | maquettiste, concepteur-ux, cartographe-interactions, developpeur-frontend, developpeur-mobile, testeur-web, testeur-mobile, expert-accessibilite |
| usine-logicielle | `formation-types-de-tests.md`, `formation-chrome-devtools.md`, `formation-playwright-mcp.md`, `formation-robot-framework.md`, `formation-cypress-typescript-cucumber.md`, `formation-postman.md`, `formation-tosca.md` | concepteur-tests, automaticien-tests, executant-tests, recetteur, testeur-web, testeur-mobile |
| architecture-normes | `formation-architectures-web-mobile.md` | architecte-solution, architecte-donnees, ingenieur-devops, developpeur-backend, developpeur-frontend, developpeur-mobile |
| architecture-normes | `formation-vercel.md`, `formation-supabase.md` (localisation des données, cas d'un client en Algérie) | architecte-solution, ingenieur-devops, architecte-donnees |
| architecture-normes | `formation-keycloak.md` | architecte-solution, architecte-securite, developpeur-backend, ingenieur-devops |
| architecture-normes | `formation-datocms.md` (bandeaux et promotions ; comparaison avec un module natif et des CMS libres) | architecte-solution, developpeur-frontend, redacteur-contenu-localisation, responsable-support-formation |
| securite-protection | `formation-passi.md` (référentiel PASSI v2.2 ; les agents ne délivrent aucune qualification) | architecte-securite, auditeur-securite, testeur-intrusion |

Les versions, prix et limites cités sont ceux constatés à la date des sources : ils se revérifient à la source avant toute décision.

## Graphe du code et design Apple (1.10.0)

- **`cartographie-graphe`** : Graphify (Graphify-Labs/graphify, Apache-2.0) est un outil séparé, installé en version figée (`graphifyy==0.9.103`) dans un environnement isolé. Il transforme le code en graphe de connaissances que les agents interrogent (`graphify query`, `path`, `explain`) au lieu de lire des fichiers entiers. Il fonctionne seulement en analyse locale du code (`GRAPHIFY_BACKEND=none`, `--code-only`, journal des requêtes coupé), sans skill amont, sans crochets git et sans service en ligne. Rattaché aux architectes, au planificateur, à l'organisateur, au relecteur, à la vigie, aux auditeurs de sécurité et aux développeurs.
- **`design-apple`** : principes des Human Interface Guidelines appliqués au web, au mobile et aux outils de gestion sur grand écran (maître-détail, clavier, données denses, planning). Les règles numérotées `HIG-n.m` et `HGE-n.m` se citent dans les constats. Elles sont réécrites en français d'après ehmo/platform-design-skills (MIT, forme A) ; le PDF d'Apple n'est pas repris. Rattaché au maquettiste, au concepteur UX, aux développeurs interface et mobile, au testeur visuel, à l'expert accessibilité et aux testeurs web et mobile.

## CRM Twenty (1.11.0)

Le skill `crm-twenty` aide à décider si un CRM est utile, puis à installer Twenty (twentyhq/twenty, AGPL-3.0 avec une exception pour les applications) sur ses propres serveurs, en version figée, avec des secrets générés sur place, une connexion chiffrée, des sauvegardes testées et des mises à jour rapides. Il couvre aussi l'intégration par API REST, GraphQL, webhooks signés ou MCP, et les règles de développement des applications Twenty. Il inclut une alerte de sécurité (CVE-2026-26720, fonctions de workflow) et les obligations de la licence AGPL. Règles `TW-n.m` réécrites en français (forme A), sans code ni texte embarqué. Il est rattaché aux architectes, au DevOps, à l'intégrateur, au développeur serveur, à la sécurité, au délégué à la protection des données, au juriste et au responsable commercial.

## Mouvement et données extrêmes (1.12.0)

Le plugin compte désormais 21 skills.

- **`mouvement-interface`** (nouveau skill) : décider s'il faut animer, puis construire, chorégraphier, fluidifier, alléger et réviser le mouvement d'une interface. Six références chargées à la demande : construction d'une animation, chorégraphie, mouvement fluide à la manière d'Apple (ressorts, passage de vitesse, projection d'inertie, élastique), performance, vocabulaire du mouvement (glossaire inversé français-anglais) et audit du mouvement (règles `MV-n.m`). `design-apple` y renvoie pour le mouvement et reste la référence pour la mise en page. Aucune bibliothèque imposée ; `prefers-reduced-motion`, accessibilité et RTL font partie de chaque règle. Rattaché au maquettiste, au concepteur UX, aux développeurs interface et mobile, au testeur visuel, à l'expert accessibilité et aux testeurs web et mobile.
- **`usine-logicielle`** : `donnees-extremes-ui.md` (casser une interface avec des données extrêmes réalistes, rattachée aux testeurs visuel, web et mobile et au recetteur), `mobile-react-native-animation.md` et `swift-moderne.md` (développeur mobile).
- **`maquettes-parcours`** : `web-mobile-natif.md` (une application web qui se comporte comme une application installée), `prototypes-en-variantes.md` (plusieurs directions comparées dans un sélecteur) et `choisir-une-bibliotheque-ui.md` (options commentées avec licence et poids).

Méthodes réécrites en français (forme A) d'après emilkowalski/skills (MIT, commit `c8a7962`), sans texte, exemple ni code repris ; chaque référence fait 1 500 mots au plus et se termine par sa section « Origine ».

## Choix de l'outillage (1.13.0)

`usine-logicielle/references/selection-outillage.md` dit qui choisit les skills, plugins et outils de navigateur, et quand : le chef d'orchestre au plan de chaque lot, la vigie à chaque porte. Les scripts Playwright du projet font foi ; Playwright MCP et le navigateur servent à explorer un cas, et Chrome DevTools à mesurer les performances réelles. La recherche de nouveaux plugins suit `renfort-externe.md`. Aucune installation n'a lieu sans accord écrit de l'utilisateur. ECC (everything-claude-code) n'est pas installé, à cause de ses crochets et de son exécution automatique : il sert seulement de source de méthodes, au cas par cas.
