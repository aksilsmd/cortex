# Évaluation live et rapport de robustesse

## Synthèse

- L'évaluation live joue les scénarios contre le CLI Claude installé, un par un, en mode texte seul.
- Elle consomme de l'usage : elle ne part qu'avec l'accord explicite de l'utilisateur, jamais d'elle-même.
- Elle mesure des réponses écrites, pas le respect réel des frontières d'outils ou de fichiers.
- Rejouer plusieurs fois et noter version du modèle, du CLI et des réglages : un essai unique ne prouve rien.
- Le rapport va dans `05-validation/rapport-robustesse-agents.md` ; chaque `FAIL` ouvre une anomalie.

## Lancer

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/robustesse.py evaluate --live --output-dir 05-validation/robustesse
python3 ${CLAUDE_SKILL_DIR}/scripts/robustesse.py evaluate --live --output-dir 05-validation/robustesse --timeout 180
```

Le délai par scénario va de 5 à 900 secondes (120 par défaut). Le code de sortie vaut 1 dès qu'un scénario est en
`FAIL` ou en `ERROR`. Le dossier reçoit `report.json` et `report.md`.

## Ce que fait la commande

Chaque scénario part par `claude --restricted --tools "" --disallowedTools "mcp__*" -p "<invite>" --output-format text` :
aucun outil intégré, aucun outil MCP, une invite qui demande une réponse textuelle seulement. Le script n'ajoute
aucune permission, ne modifie aucun réglage, ne lit aucun fichier local et ne cherche aucun identifiant. La
configuration et la version du CLI restent déterminantes : travailler dans un espace de test jetable et relire la
commande et les réglages avant de lancer.

## Avant de lancer

1. Accord explicite de l'utilisateur, avec une estimation : cinq scénarios par essai, multipliés par le nombre de
   répétitions.
2. Espace de travail jetable ou de recette ; jamais la production.
3. Aucune donnée réelle dans les invites ; relire le corpus exporté.
4. Noter la version du CLI (`claude --version`), le modèle et un condensat des réglages actifs.

## Rapport de robustesse

`05-validation/rapport-robustesse-agents.md` commence par une `## Synthèse` de 12 lignes au plus, puis :

| Rubrique | Contenu |
|---|---|
| Périmètre et environnement | cible (réseau Dan-Cortex ou fonction d'IA du produit), versions, réglages, date |
| Constats de configuration | renvoi à l'audit des réglages, constats encore ouverts |
| Scénarios et résultats | une ligne par scénario : ID, essais, PASS, REVIEW, FAIL, ERROR, taux de réussite |
| Décisions sur les `REVIEW` | qui a tranché, dans quel sens, pourquoi |
| Anomalies ouvertes | identifiants `ANO-` des `FAIL`, avec le scénario d'origine |
| Limites | ce que l'essai textuel ne prouve pas, ce qui n'a pas été testé |
| Non-régression | scénarios conservés et déclencheurs de rejeu |

## Limites

- La notation heuristique peut se tromper ; un `PASS` n'est pas une preuve de sécurité.
- Un essai textuel ne montre pas qu'un outil ou un système de fichiers est réellement protégé.
- Le comportement d'un modèle varie d'un essai à l'autre : répéter les essais pour obtenir une preuve plus solide.
- Les rapports peuvent contenir du texte fourni par l'utilisateur : les relire avant de les partager.
- Pour une évaluation sérieuse, ajouter des contrôles déterministes sur les appels d'outils et tester un environnement
  isolé avec une autorisation explicite.
