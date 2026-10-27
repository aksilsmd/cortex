# Audit des réglages Claude Code

## Synthèse

- L'audit lit les fichiers de réglages JSON de Claude Code et signale les motifs trop larges ; il ne modifie rien.
- Commande : `python3 ${CLAUDE_SKILL_DIR}/scripts/robustesse.py audit-config [--path F] [--format json]`.
- Code de sortie 0 sans constat `HIGH`, 2 avec au moins un constat `HIGH`.
- Aucun constat ne veut pas dire « sûr » : l'outil ne connaît que les motifs de sa liste.
- Chaque constat `HIGH` finit corrigé, ou accepté par l'utilisateur et inscrit au registre des risques.

## Fichiers lus

Sans `--path`, dans cet ordre et seulement s'ils existent :

| Fichier | Portée |
|---|---|
| `.claude/settings.json` | réglages partagés du projet (dossier courant) |
| `.claude/settings.local.json` | réglages personnels du projet |
| `~/.claude/settings.json` | réglages de l'utilisateur |

Les politiques gérées par une organisation et les réglages d'une session distante ne sont pas lus : les signaler
comme « non vérifiés » dans le rapport. `--path` permet d'auditer un autre fichier, à condition que l'utilisateur
y ait accès et l'ait demandé.

## Constats possibles

| Code | Gravité | Ce qui est repéré | Recommandation |
|---|---|---|---|
| `BROAD_PERMISSION_MODE` | HIGH | un mode de permission `bypassPermissions` ou `dontAsk` | réserver ce mode à un espace jetable et isolé ; préférer des règles d'autorisation ciblées et le bac à sable |
| `WILDCARD_ALLOW_RULE` | HIGH | une règle `Bash(*)` ou `*` | la remplacer par des commandes précises, propres à la tâche |
| `INVALID_JSON` | HIGH | un fichier illisible | corriger la syntaxe : un fichier invalide peut être ignoré en silence |
| `READ_ERROR` | HIGH | un fichier inaccessible | vérifier le chemin et les droits |
| `BYPASS_MODE_NOT_DISABLED` | MEDIUM | `disableBypassPermissionsMode` à `false` | envisager une politique gérée qui interdit ce mode |
| `SANDBOX_DISABLED` | MEDIUM | un réglage de bac à sable explicitement à `false` | rétablir des frontières de fichiers et de réseau quand c'est possible |
| `SENSITIVE_COMMAND_ALLOW` | MEDIUM | une autorisation commençant par `Bash(rm`, `Bash(sudo`, `Bash(curl` ou `Bash(wget` | vérifier la portée exacte du motif et s'il est nécessaire |
| `NO_MATCHING_PATTERNS` | INFO | aucun motif connu | ce n'est pas une preuve de sécurité ; vérifier les réglages effectifs dans la documentation officielle |

## Après l'audit

1. Ranger la sortie texte, ou JSON avec `--format json`, dans `00-pilotage/audits/audit-reglages-agents.md`,
   précédée d'une `## Synthèse` : fichiers lus, constats par gravité, décisions prises, points non vérifiés.
2. Pour chaque constat `HIGH` ou `MEDIUM`, proposer un **écart minimal** (la ligne à retirer ou à resserrer) et
   attendre l'accord de l'utilisateur. Ne jamais éditer un fichier de réglages de sa propre initiative.
3. Un constat que l'utilisateur garde volontairement devient un risque :
   `cortex.py registre risques ajouter titre="…" domaine=ROB cause="…" parade="…" proprietaire="<nom>"`.
4. Cocher `ROB-001` dans la couverture avec le fichier d'audit pour preuve.

## Réglages pour le mode autonome

`${CLAUDE_SKILL_DIR}/assets/reglages-autonomes.json` est un point de départ pour travailler avec peu de demandes de
permission sans élargir la surface d'attaque :

| Réglage | Effet |
|---|---|
| `permissions.defaultMode: auto` | un classifieur approuve les actions courantes ; remplacer par `acceptEdits` si la version de Claude Code ne propose pas ce mode |
| `sandbox.enabled: true` et `autoAllowBashIfSandboxed: true` | les commandes tournent dans le bac à sable, sans demande, avec des frontières de fichiers et de réseau |
| `allow` : `WebSearch`, `WebFetch`, lecture de l'état Git | la collecte web des analystes ne s'arrête pas à chaque page |
| `deny` : fichiers de secrets, `sudo`, `git push --force`, `git reset --hard` | les gestes dangereux restent impossibles, même en autonomie |

Le fichier se pose dans `.claude/settings.json` du projet (partagé) ou `.claude/settings.local.json` (personnel),
par l'utilisateur ou avec son accord explicite, jamais d'office. Relancer ensuite l'audit : il ne doit remonter
aucun constat `HIGH` (contrôle `ROB-005`). Les noms de réglages évoluent : vérifier contre la documentation de la
version installée.

## Limites

- Contrôles statiques consultatifs : ce n'est pas un analyseur complet de la hiérarchie des réglages.
- Les noms et la syntaxe des réglages évoluent avec les versions de Claude Code : vérifier chaque recommandation
  contre la documentation officielle en vigueur.
- L'audit ne voit ni les hooks d'un plugin, ni les serveurs MCP, ni ce qu'une session autorise à la volée.

## Sources

- Anthropic, *Claude Code sandboxing* : https://www.anthropic.com/research/claude-code-sandboxing
- Anthropic, conseils pour les utilisateurs avancés de Claude Code : https://support.claude.com/fr/articles/14554000-conseils-pour-les-utilisateurs-avances-de-claude-code
- Exemples de réglages Claude Code : https://github.com/anthropics/claude-code/tree/main/examples/settings
