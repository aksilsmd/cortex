# CLAUDE.md

Deux lectures, selon ce que tu fais.

- **Tu te sers de Dan-Cortex** pour mener un projet : lis [`AGENTS.md`](AGENTS.md). Il dit quelle compétence
  charger pour quelle demande, et comment jouer les rôles avec ou sans sous-agents.
- **Tu travailles sur ce dépôt** : lis [`CONTRIBUTING.md`](CONTRIBUTING.md), puis respecte ce qui suit.

## Les règles qui cassent la publication si on les enfreint

1. `dan-cortex/` ne se déplace ni ne se renomme : `.claude-plugin/marketplace.json`, `scripts/construire_plugin.py`
   et `pyproject.toml` le nomment ainsi.
2. Les fichiers dérivés se régénèrent, jamais à la main : catalogues et cartes
   (`scripts/generer_catalogues.py`), paquet universel (`scripts/construire_universel.py`), archive
   `dist/dan-cortex.plugin` (`scripts/construire_plugin.py`). L'archive se bâtit sur les fichiers **suivis par
   Git** : `git add -A` avant. `make build` fait la chaîne entière.
3. La version s'écrit à quatre endroits qui doivent concorder : `dan-cortex/.claude-plugin/plugin.json`, les deux
   champs de `.claude-plugin/marketplace.json`, la première entrée du `CHANGELOG.md`, le badge
   `badge/version-<x.y.z>-` du `README.md`.
4. Les chiffres annoncés par le `README.md` sont vérifiés contre le plugin : compteurs de skills, d'agents et de
   contrôles, en français comme dans le résumé « In English ».
5. La page d'accueil reste légère : six images au plus, et aucun diagramme `mermaid` — il est rendu par le
   navigateur après le chargement, ce qui retarde la page et peut en tronquer la fin sur mobile. Les diagrammes
   vivent dans `docs/`.
6. Aucun secret, aucune donnée personnelle, aucune charge utile visant un système tiers. Les notices de licence
   de `dan-cortex/NOTICE.md` et des fichiers `OFL.txt` se conservent telles quelles.

## Commandes

```bash
make build    # régénère catalogues, paquet universel et archive
make verify   # rejoue les cinq contrôles de l'intégration continue
make help     # la liste des cibles
```

Lance `make verify` avant de conclure, et cite son résultat réel — jamais un résultat supposé.

## Style

Français, tutoiement, phrases courtes. Messages de commit en français, préfixés de la version quand elle change
(`Dan-Cortex 2.2.0 : …`). Toute affirmation de droit, de norme ou de version cite sa source et sa date ; ce qui
n'est pas confirmé est marqué « à vérifier ».
