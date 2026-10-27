# Sobriété en tokens pendant le codage

Le code est la phase la plus coûteuse de Dan-Cortex. Ce fichier donne les réflexes qui réduisent la consommation sans réduire la qualité, par ordre de gain décroissant. L'utilisateur en fait une exigence explicite.

## Sommaire
1. Pourquoi
2. Contexte minimal par lot
3. `essais.py` pour toute commande
4. Générateurs officiels
5. Outils plutôt que relecture
6. Lecture ciblée
7. Modèle et effort
8. Reprise des agents
9. Ce qu'il ne faut jamais faire
10. Contrôles avant de rendre
11. Sources

## 1. Pourquoi

La fenêtre de contexte se remplit vite et la performance baisse avec elle ; le coût est proportionnel au contexte. Une sortie de test complète coûte des milliers de tokens là où un résumé d'échecs en coûte quelques centaines. Les agents repaient leur contexte de départ à chaque appel d'outil.

## 2. Contexte minimal par lot

L'ordre de mission d'un développeur liste **tout** ce qu'il lit : sa fiche de lot, ses contrats, les `RG-` et `CT-` de son lot, les passages utiles des normes. Il ne lit ni le code d'un autre lot, ni la SFG entière, ni le cahier des charges. S'il lui manque une information, il la demande dans « Renforts demandés » au lieu d'explorer. Ses commandes d'amorçage tiennent en quelques lignes : où lancer la vérification, où ranger le code.

## 3. `essais.py` pour toute commande

`${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/essais.py` lance une commande, range la sortie complète dans un journal et n'affiche que le code de retour, la durée, le résumé et les lignes d'échec (40 au plus par défaut).

```
python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/essais.py --journal 04-realisation/journaux/lot-004.log -- pytest -q tests/lot4
```

| Besoin | Réflexe |
|---|---|
| Test, build, lint, migration | toujours via `essais.py`, jamais en direct |
| Échec dont les lignes affichées ne suffisent pas | recherche ciblée dans le journal, jamais sa lecture complète |
| Commande qui doit rester longue | `--delai` explicite, `--max` si la sortie utile dépasse 40 lignes |
| Commande introuvable (code 127) | le signaler au compte rendu, ne pas deviner un équivalent |

Une commande de vérification unique par lot (format, statique, types, tests) évite de lancer cinq outils et de lire cinq sorties.

## 4. Générateurs officiels

Ne pas écrire à la main ce qu'un outil officiel produit : squelette de projet, migrations, clients d'API depuis OpenAPI, types partagés, écrans de saisie répétitifs. La sortie d'un générateur coûte une commande, pas des centaines de lignes de génération. L'agent vérifie la version du générateur à la source et écrit « à vérifier » s'il ne le peut pas. Le code répétitif (CRUD, migrations similaires) va à un agent sur modèle léger quand l'ordre de mission le prévoit.

## 5. Outils plutôt que relecture

| Défaut visé | Outil, pas relecture |
|---|---|
| Style, formatage | formateur automatique, en pré-commit et en intégration continue |
| Types, erreurs fréquentes | analyse statique et typage |
| Couches, cycles, imports interdits | tests d'architecture |
| Doublons | détection de duplication |
| Secrets, dépendances vulnérables | analyse de secrets, analyse de dépendances |
| Comportement | tests, et mutation pour juger la force des assertions |

La revue d'un modèle ne commence qu'après le vert des outils.

## 6. Lecture ciblée

- Chercher (recherche de texte, symbole) avant de lire ; lire une plage de lignes, pas un fichier de mille lignes.
- Lire une différence (`git diff --stat`, puis les fichiers utiles), jamais le dépôt entier.
- Ne pas relire un fichier qu'on vient d'écrire : l'outil d'écriture signale l'échec.
- Un journal de test se filtre (motif d'erreur) avant lecture ; les fichiers générés, verrous et dépendances installées ne se lisent jamais.
- Rédiger le compte rendu en 150 mots, sans recopier le code.

## 7. Modèle et effort

| Tâche | Modèle |
|---|---|
| Boilerplate, migrations répétitives, rejeu d'une suite | léger (`haiku`), `executant-tests` |
| Code et tests d'un lot, revue, automatisation | intermédiaire (`sonnet`) |
| Conception, débogage difficile, arbitrage d'architecture | modèle de la session |

Régler l'effort de réflexion par tâche : une réflexion longue est facturée en sortie. Tester par petits pas (un fichier, un test, puis la suite).

## 8. Reprise des agents

Corriger un lot, c'est **reprendre** le développeur d'origine : il a déjà le contexte et le cache de prompt. Un agent neuf relit tout. Seule exception : le relecteur, qui doit rester neuf pour juger sans biais.

## 9. Ce qu'il ne faut jamais faire

- Lancer une suite sans `essais.py`, ou coller une sortie de test entière dans le contexte.
- Dire à un agent « explore le dépôt » ou « prends connaissance du projet ».
- Relire plusieurs fois le même fichier ; recharger les mêmes documents d'un agent à l'autre.
- Confier à un modèle fort une tâche qu'un générateur ou un modèle léger traite.
- Lancer une vague de développeurs avant que les contrats soient figés : le travail sera refait.
- Réécrire un module entier pour corriger trois lignes.

## 10. Contrôles avant de rendre

- Chaque commande de test ou de build du compte rendu est passée par `essais.py`.
- La liste des fichiers lus tient dans l'ordre de mission.
- Aucun code généré à la main quand un générateur officiel existait.

## Sources

- Claude Code, coûts (contexte, sous-agents, hooks de filtrage, choix du modèle, effort) : https://code.claude.com/docs/en/costs
- Claude Code, bonnes pratiques (saturation du contexte) : https://code.claude.com/docs/en/best-practices
- Claude Code, sous-agents : https://code.claude.com/docs/en/sub-agents
- DORA 2025, rôle du retour rapide : https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Script `essais.py` du plugin Dan-Cortex (`skills/lancer-projet/scripts/`).
