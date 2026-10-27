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

## Comment ça marche

- **Un chef d'orchestre** parle avec toi, lance les agents par vagues parallèles et ne lit que des comptes rendus
  courts.
- **45 agents experts** répartis en pôles, chacun avec les compétences de son métier (le skill de son
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
| Skills | 16 | `skills/` |
| Agents | 45 | `agents/` |
| Contrôles de couverture | 784 | `skills/*/references/checklist-*.md` |
| Fichiers de référence et gabarits | 126 | `skills/*/references/`, `skills/*/assets/` |
| Scripts | 3 | `skills/lancer-projet/scripts/` (`cortex.py`, `essais.py`), `skills/robustesse-agents/scripts/` (`robustesse.py` et le paquet `ccal`) |

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
