# Dan-Cortex sur une autre IA que Claude

Dan-Cortex est une méthode. Sur Claude, le plugin apporte en plus les agents en parallèle et les scripts de
pilotage. Ailleurs, le paquet universel fait tourner la même méthode avec les moyens de l'IA hôte.

## Ce que contient ce dossier
| Fichier | Usage |
|---|---|
| `DAN-CORTEX-NOYAU.md` | les instructions, moins de 8 000 caractères : à coller dans le champ « instructions » d'un assistant personnalisé ou d'un projet |
| `connaissances/` | sept fichiers de méthode à joindre comme fichiers de connaissance |
| `DAN-CORTEX-COMPLET.md` | noyau et annexes en un seul fichier : à joindre ou à coller au début d'une conversation quand l'IA n'a pas d'instructions persistantes |
| `skill/dan-cortex/` | la même chose au format « skill » (`SKILL.md` + `references/`), pour les IA qui lisent ce format |

## Trois façons d'installer, de la plus simple à la plus complète
1. **Conversation simple** (toute IA) : joindre `DAN-CORTEX-COMPLET.md` et écrire « Applique ces instructions.
   Bonjour. ». À refaire à chaque nouvelle conversation, avec le dernier bloc « ÉTAT DU PROJET ».
2. **Assistant ou projet avec instructions persistantes** : coller `DAN-CORTEX-NOYAU.md` dans les instructions,
   joindre les sept fichiers de `connaissances/`. Activer la recherche web si elle existe.
3. **Skill** : importer le dossier `skill/dan-cortex/` là où l'IA accepte des skills au format `SKILL.md`.

## Par plateforme (état relevé le 10 novembre 2026, à vérifier dans l'aide officielle de chaque produit)
- **ChatGPT** : projet avec instructions, ou assistant personnalisé (instructions limitées à 8 000 caractères,
  une dizaine de fichiers de connaissance selon les sources). Les assistants personnalisés seraient en cours de
  remplacement par des plugins d'espace de travail : préférer un projet si c'est le cas.
- **Gemini** : les Gems passeraient en lecture seule le 17 novembre 2026 et seraient remplacés par des Skills
  au format `SKILL.md` (100 Mo de fichiers au plus) : utiliser `skill/dan-cortex/`.
- **Claude** : installer le plugin complet (README à la racine du dépôt) ; le paquet universel n'est utile que
  dans un projet sans plugin.
- **Autres** (Mistral, Copilot, modèles locaux…) : voie 1 ou 2 selon ce que le produit propose.

## Ce qui change sans le plugin
Pas d'agents en parallèle (les rôles sont joués l'un après l'autre), pas de scripts (registres et avancement
tenus en tableaux), pas de mémoire automatique (bloc « ÉTAT DU PROJET »). La réalisation du code par lots avec
tests, relecture indépendante et audit n'est pleinement outillée que dans le plugin Claude.

## Reconstruire
`python3 scripts/construire_universel.py` après toute modification de `skills/accueil-recueil/references/` ou
du noyau.
