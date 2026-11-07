# Choisir l'outillage : skills, plugins et outils de navigateur

Le choix de l'outil fait partie de la méthode. Un mauvais outil coûte des jetons, produit des preuves fragiles ou ouvre une porte (crochets, scripts tiers). Cette référence dit **qui décide, quand et sur quels critères**.

## Qui décide

| Rôle | Responsabilité |
|---|---|
| Chef d'orchestre et `orchestrateur-de-pole` | Choisissent l'outillage de chaque lot au moment du plan (porte 1) et l'inscrivent dans le plan du lot : outil, moment, preuve attendue. |
| `vigie-oublis` | Contrôle à chaque porte que l'outil prévu a bien servi, au bon moment, et qu'aucun outil plus adapté n'a été oublié. Un écart est un constat de méthode. |
| `organisateur` | Range l'outillage dans le plan de campagne et évite deux outils qui produisent la même preuve. |
| Utilisateur | Seul à autoriser l'installation d'un plugin tiers ou d'un serveur MCP nouveau. |

Un outil n'est utilisé que s'il est **réellement présent dans la session** : outils listés, skills préchargés, serveurs MCP connectés. Sinon, on prend le repli indiqué. Aucun agent n'installe un outil de lui-même.

## Grille de choix (outils de navigateur et de test)

| Besoin | Outil de premier choix | Repli |
|---|---|---|
| Test répétable, en intégration continue, ou rejoué à chaque lot (E2E, régression, smoke) | scripts Playwright du projet | aucun : c'est la référence |
| Explorer une page ou reproduire un bogue signalé, de façon interactive et ponctuelle | Playwright MCP, ou le navigateur intégré, ou Claude in Chrome selon le navigateur préféré de l'utilisateur | script Playwright jetable dans le bloc-notes |
| Mesurer les performances réelles d'une page (trace, LCP, CLS, INP, longues tâches, mémoire) | Chrome DevTools (MCP ou protocole DevTools via Playwright) | `perf-pages` et mesures Playwright |
| Inspecter la console, le réseau, le stockage et les en-têtes (DEC-054 et équivalents) | audit d'inspection automatisé du projet | Chrome DevTools pour le diagnostic d'un cas |
| Vérifier le rendu (captures multi-écrans, régression visuelle) | `controle-visuel.md` et scripts de captures | agent `testeur-visuel` |
| Comprendre un code inconnu ou l'impact d'un changement | skill `cartographie-graphe` (Graphify, local) | lecture ciblée et `grep` |
| Empreintes, secrets de test, QR codes | skill `boite-outils-it` | commandes Node natives |

Règles :
- **La preuve qui fait foi est toujours un test ou un script versionné.** Une exploration MCP ou DevTools sert à comprendre, puis on la transforme en test.
- **Navigateur de l'utilisateur** : toute action sur un site public, une connexion ou un formulaire suit les règles de sécurité de la session (confirmation explicite, aucun mot de passe saisi, aucun site de production pour les tests). Les tests de sécurité restent en local.
- **Une seule source de mesure par indicateur**, pour éviter deux chiffres contradictoires.

## Plugins et skills tiers

### Chercher

Quand un manque est constaté (une compétence absente, un livrable faible), le chef d'orchestre peut envoyer `collecteur-web` ou un agent de veille chercher des skills ou des plugins : forges, index de skills, documentation des éditeurs. La recherche suit `robustesse-agents/references/renfort-externe.md` §2 et §3 : licence lue dans le fichier, crochets, scripts, appels réseau, injection, caractères invisibles.

### Décider de la forme

| Forme | Quand | Exemple |
|---|---|---|
| A, méthode réécrite dans Dan-Cortex | cas par défaut | design Apple, mouvement d'interface, CRM Twenty |
| Outil séparé, local, version figée, sans crochet | un outil apporte une capacité que le texte ne remplace pas | IT-Tools, Graphify |
| Plugin ou serveur MCP installé à côté | seulement avec l'accord explicite de l'utilisateur, après revue de sécurité, s'il n'a ni crochet ni script lancé automatiquement, ou si l'utilisateur accepte ce risque par écrit | Playwright MCP, Chrome DevTools MCP (éditeurs reconnus) |
| Refus | crochets ou exécution automatique, licence absente ou incompatible, appels réseau non maîtrisés, consigne d'injection | voir ci-dessous |

### Cas d'ECC (everything-claude-code)

Le dépôt (affaan-m/everything-claude-code, MIT, plus de 80 000 étoiles) est un harnais complet : plusieurs dizaines d'agents et de skills, des commandes, plus de cinquante crochets (hooks), des scripts, une mémoire persistante et un tableau de bord. **Il n'est pas installé à côté de Dan-Cortex** : ses crochets et son exécution automatique contreviennent à `renfort-externe.md` §1. Il sert de **source de méthodes** (forme A), au cas par cas, quand un manque précis le justifie. Exemples de thèmes : revue de code par langage, audit d'accessibilité, tests de régression des agents. Chaque reprise passe par le banc et la relecture de non-copie.

## Contrôles de la vigie à chaque porte

1. L'outil prévu au plan a servi, et la preuve est versionnée.
2. Aucun outil absent de la session n'a été supposé présent.
3. Aucune installation ni aucun crochet n'a été ajouté sans accord écrit de l'utilisateur.
4. Une exploration interactive qui a trouvé un défaut a donné un test rouge.
5. Les mesures de performance citées viennent de la source unique déclarée.

## Origine

Rédigé pour Dan-Cortex le 2026-11-07, à la demande du PO. Dépôt ECC consulté en lecture seule (commit `d2ef268`, inventaire des dossiers et de `hooks/hooks.json`). Aucun texte n'est repris. Voir `references/sources/renfort-github.md`.
