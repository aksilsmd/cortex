# Craft Anything : l'outil optionnel

Application libre, écrite en Rust, qui automatise le cycle étudier, construire, vérifier, affiner. Source : dépôt `storytold/craft-anything`, double licence MIT ou Apache-2.0, commit `e64d7cb`. État relevé dans ses documents au 9 novembre 2026 : **alpha précoce**.

## Règle d'usage

- Ne rien installer sans l'accord de l'utilisateur ; lui présenter d'abord le statut alpha, les coûts éventuels et les limites ci-dessous.
- Ne jamais exécuter de script du dépôt sans l'avoir lu et sans accord.
- L'outil est un **accélérateur**, pas une garantie juridique : voir « Écarts avec notre méthode ».

## Ce que fait l'outil

On désigne une cible (adresse d'un site, programme, jeu), on décrit ce qu'on veut, et l'outil suit quatre étapes affichées dans une page de projet :

1. **Étudier** : inspecter l'original. Pour un site : captures à plusieurs largeurs, texte visible, mise en page mesurée, couleurs, polices, espacements, menus et fenêtres ouverts un par un, quelques autres pages du site.
2. **Construire** : un agent de codage (Claude Code en premier, avec la connexion de l'utilisateur) crée un nouveau projet dans le langage ou le moteur demandé.
3. **Vérifier** : comparaison de la version construite à l'original.
4. **Prêt** : ouvrir, jouer ou prévisualiser ; demander des changements, ce qui relance un affinage.

Types de cibles : **site web** (comparé par captures à trois largeurs, valeurs par défaut 1440, 768 et 390 px), **application** (la construction doit réussir ; un programme en console est comparé par ses exécutions, entrées et sorties), **jeu** (moteurs Unity, Unreal ou Godot, ou Rust ; un autotest `--self-test` joue la boucle de base et une feuille de mécaniques `mechanics.json` doit citer une source ou marquer « estimé »).

## Les deux modes

| mode | ce qui est lu | usage dans ce skill |
|---|---|---|
| **Clean room** (par défaut) | seulement ce qu'un visiteur voit : captures, texte visible, mesures, images fournies ; les outils qui regarderaient à l'intérieur sont refusés | seul mode admis sur une cible tierce |
| **Deep** | tout : code JavaScript d'un site, décompilation d'un programme (Ghidra si installé), fichiers d'un jeu | uniquement sur un logiciel dont l'utilisateur est titulaire ou a un droit écrit |

Le mode Clean room est une règle de ce que l'outil offre ou refuse ; ce n'est pas un bac à sable du système : un agent de codage lancé agit avec les droits de l'utilisateur.

## Garde-fous de l'outil

- **Approbations avant exécution.** Les actions de l'agent passent par un outil d'approbation (`core_action_approve`). Les modifications dans le dossier `app/` du projet et une liste fixe de commandes de construction sont admises ; les serveurs de développement sont refusés ; le reste est décidé par type (web, commandes, fichiers hors projet, publication, suppression, changements système) : autoriser, demander ou refuser, par projet. Une carte demande « une fois », « toujours pour ce projet » ou « refuser ». Choisir « toujours » pour une catégorie est une confiance durable : à éviter sans raison.
- **Questions à l'utilisateur** par cartes (`core_person_ask`) pour les choix qui changent le résultat ; rien d'omis en silence.
- **Plan par étapes** : l'agent tient une liste de 3 à 7 étapes lisibles, mise à jour en direct.
- **Inconnues consignées** : chaque question laissée sans réponse est enregistrée, avec ce qui la lèverait ; une absence de preuve n'est jamais une preuve.
- **Usage responsable** (déclaré par l'outil) : pas de contournement de gestion des droits numériques, d'identification ou d'anti-triche ; l'agent doit éviter de copier logos, photos et textes, sauf confirmation de droits.
- **Installation de dépendances = exécution de code.** Les gestionnaires de paquets peuvent lancer des scripts. L'outil demande avant un type de commande nouveau ; pour npm, `npm install --ignore-scripts` limite le risque.

## Vérification et score de ressemblance

Pour un site, chaque largeur donne une ressemblance de mise en page et de détail ; s'y ajoutent la ressemblance du texte visible, celle de la structure (zones, titres, listes, formulaires, dans l'ordre), et des notes de santé (erreurs de console, requêtes en échec, contrôles sans nom, images sans texte alternatif, langue absente). Réglages par défaut : seuil « assez proche » 90 %, six tours d'affinage au maximum, quatre pages étudiées (jusqu'à douze).

Ces mesures guident un clone fidèle. Pour une reconstruction **originale**, les lire autrement : garder les notes de structure, de santé et d'accessibilité ; traiter une ressemblance de texte ou d'image élevée comme un signal d'alerte.

## Écarts avec notre méthode

- L'outil étudie et construit dans la même chaîne : l'agent constructeur reçoit les captures et le texte visible de l'original. Notre méthode exige une **spécification neutre intermédiaire** et un constructeur qui ne voit rien de l'original. Utiliser l'outil pour l'étape d'observation (relevé), puis rédiger et relire la spécification, et construire à part.
- En mode Deep, la lecture du code et la décompilation sortent du cadre d'une salle blanche.
- Sa consigne autorise la reprise de logos ou de textes avec confirmation de droits ; la nôtre l'interdit pour une cible tierce.
- Ses scores favorisent la ressemblance ; les nôtres, le comportement.

## Mise en route (si l'utilisateur accepte)

Prérequis relevés : Rust 1.97 ou plus récent ; un agent de codage connecté sur la machine ; sous Debian ou Ubuntu, des bibliothèques graphiques pour l'application de bureau. Des installateurs signés (Windows, macOS, Linux, FreeBSD), tous marqués alpha, sont publiés sur la page des versions du dépôt (à revérifier avant usage).

Commandes de la ligne de commande, relevées dans le README :

```
craft-anything-cli doctor
craft-anything-cli commands
craft-anything-cli rebuild <adresse> "<demande>" --clean-room
```

`doctor` contrôle l'installation, les agents et les moteurs ; `commands` liste les outils ; `rebuild` lance le cycle complet ; l'option `--clean-room` (ou `--deep`) fixe le mode pour une exécution. Un projet crée un dossier avec `craft.json`, `capture/`, `app/`, `checks/`, `investigation.cany/` et `inbox/`. Le dossier `capture/` est une donnée interne : ne pas le transmettre au constructeur.

## Points à revérifier

- Le comportement actuel des options en ligne de commande (relire le README et `doctor` avant usage).
- Les fonctions marquées « partielles » dans l'état du projet : construction avec clés d'API ou autres agents, vérifications de comportement d'applications et de jeux.
- La génération d'images et de modèles 3D (clé fal.ai personnelle, budget) : payante, à n'activer qu'avec accord explicite ; chaque création doit être originale, jamais une imitation reconnaissable.
- Le nom et les logos de la marque ArtCraft ne sont pas couverts par la licence : ne pas les réutiliser.
