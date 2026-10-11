# Cortex

Un réseau d'agents experts, organisé comme une entreprise, pour cadrer, concevoir, réaliser, tester, sécuriser et
lancer un grand projet numérique : site web de grande entreprise, application mobile, SaaS, produit de niche,
e-commerce, ERP. Rien n'est oublié, et le tout est conçu pour consommer peu de tokens.

## Installer

Dans Claude Code :

```
/plugin marketplace add aksilsmd/cortex
/plugin install cortex@cortex-projets
```

Dans l'application Claude (web et bureau, offres payantes) : menu **Customize** (Personnaliser) → **Plugins** →
**Add** → **Add marketplace** → **Add from a repository**, saisis le même dépôt, puis ajoute le plugin `cortex`.
Autre voie : téléverse le fichier `cortex.plugin` comme plugin personnalisé.

## Démarrer

Dans Claude, tape la commande du chef d'orchestre et décris ton projet :

```
/cortex:lancer-projet Je veux lancer <ton projet>, pour <qui>, dans <quels pays>, avec <budget et délai>.
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
| `/cortex:veille-marche` | étude de marché, benchmark des concurrents, voix du client, analyse de contexte, positionnement |
| `/cortex:specifications` | note de cadrage, cahier des charges, spécifications générales, détaillées et techniques |
| `/cortex:maquettes-parcours` | workflows, matrice d'interactions (chaque bouton, chaque clic, sa destination), maquettes, thème |
| `/cortex:architecture-normes` | choix du langage et de la pile, architecture, schéma de données, normes de développement, infrastructure |
| `/cortex:usine-logicielle` | réalisation par lots, tests unitaires, fonctionnels, d'API, de bout en bout, recette, corrections |
| `/cortex:securite-protection` | analyse de risques, protections, tests de sécurité, cadrage d'un test d'intrusion, réponse à incident |
| `/cortex:juridique-conformite` | données personnelles, commerce et consommation, contrats, propriété intellectuelle, pénal, fiscalité |
| `/cortex:budget-finance` | estimation, budget complet, justification économique, financements |
| `/cortex:marketing-commercial` | stratégie de mise sur le marché, acquisition, prix, vente, plan de lancement |
| `/cortex:lancement-exploitation` | go/no-go, plan de bascule, mise en production, support, bilan |
| `/cortex:reunion-decision` | faire débattre les experts et tracer une décision |
| `/cortex:audit-general` | audit à 360° d'un projet, mené avec Cortex ou non |

## Comment ça marche

- **Un chef d'orchestre** parle avec toi, lance les agents par vagues parallèles et ne lit que des comptes rendus
  courts.
- **45 agents experts** répartis en pôles, chacun avec les compétences de son métier (le skill de son
  pôle, préchargé) et les seuls outils dont il a besoin.
- **Des orchestrateurs de pôle** découpent le travail en ordres de mission ; des sous-agents légers font la
  collecte et l'exécution.
- **Des réunions écrites** : positions séparées, contradicteur, deux tours au plus, décision tracée. Tu tranches
  les décisions irréversibles.
- **Des revues croisées** : le juriste relit le marketing, le testeur relit les spécifications, la sécurité
  relit l'architecture.
- **Un super-auditeur** indépendant passe tout en revue avant le lancement ; son rapport est débattu en plénière,
  puis les corrections sont décidées et recontrôlées.
- **Une matrice de couverture de 768 contrôles**, filtrée selon ton projet : chaque ligne finit
  « fait » avec sa preuve, « non applicable » avec son motif, ou « risque accepté » avec un nom.
- **Un script** tient les registres, vérifie les jalons, la traçabilité des exigences aux tests et la cohérence
  des interactions (aucun bouton sans destination, aucun écran orphelin).

Le détail est dans `skills/lancer-projet/references/reseau.md`.

## Ce que contient le plugin

| Élément | Nombre | Où |
|---|---|---|
| Skills | 13 | `skills/` |
| Agents | 45 | `agents/` |
| Contrôles de couverture | 768 | `skills/*/references/checklist-*.md` |
| Fichiers de référence et gabarits | 119 | `skills/*/references/` |
| Scripts | 2 | `skills/lancer-projet/scripts/` (`cortex.py`, `essais.py`) |

## Sobriété en tokens

Ordres de grandeur observés en octobre 2026 dans une session très équipée ; ils varient selon la session :

| Lancement | Contexte de départ |
|---|---|
| agent généraliste | environ 90 000 tokens |
| agent Cortex, outils de métier | environ 6 000 tokens |

- Coût permanent du plugin : environ 3 601 tokens par session, pour les noms et descriptions des
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
- **Aucun effet extérieur sans ton accord** : ni achat, ni publication, ni envoi, ni push, ni déploiement.
- **Les tests de sécurité ne visent que les environnements de ton projet**, avec ton autorisation écrite. Pour un
  enjeu fort, un test d'intrusion par un prestataire qualifié reste nécessaire.
- **Dans l'application Claude, un agent ne peut pas en lancer d'autres** : les orchestrateurs de pôle préparent
  les ordres de mission, le chef d'orchestre lance tout le monde en parallèle.
- **Un grand projet dépasse une session.** L'état du dossier projet permet de reprendre où l'on s'est arrêté ;
  travaille dans un dossier persistant.
- **Le droit détaillé est outillé pour la France et l'Union européenne.** Pour les autres pays (Royaume-Uni, États-Unis, Algérie, Maroc, Tunisie…), Cortex donne des repères et renvoie à un avocat local.
- **Le droit et les versions d'outils changent.** Les références sont à l'état d'octobre 2026 ; les points que la
  recherche n'a pas pu confirmer sont marqués « à vérifier » dans les fichiers.

## Adapter Cortex

- **Ajouter un contrôle** : une ligne dans le fichier `checklist-*.md` du pôle, au format des autres, puis
  `python3 skills/lancer-projet/scripts/cortex.py plugin verifier`.
- **Changer ce qu'un jalon exige** : `skills/lancer-projet/assets/jalons.json`.
- **Modifier un agent** : son fichier dans `agents/` (modèle, effort, outils, fiche de poste).
- **Ajouter un type de projet** : un profil dans `skills/lancer-projet/references/profils/`.

## Prérequis

Python 3 pour les scripts (bibliothèque standard uniquement). Sans Python, le chef d'orchestre tient les mêmes
registres à la main, pour plus cher en tokens.
