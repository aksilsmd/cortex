## Objet

<!-- Ce que change cette pull request, et pourquoi. Lier le ticket : « Corrige #12 ». -->

## Type de changement

- [ ] Correction (bogue, droit, norme, version d'outil)
- [ ] Ajout (contrôle, skill, agent, profil, gabarit)
- [ ] Documentation
- [ ] Outillage (scripts, tests, CI)

## Contrôles

- [ ] `python3 -m unittest discover -s tests -v` passe
- [ ] `python3 dan-cortex/skills/lancer-projet/scripts/cortex.py plugin verifier` passe
- [ ] `python3 scripts/generer_catalogues.py` relancé (catalogues et cartes à jour)
- [ ] `python3 scripts/construire_plugin.py` relancé après `git add` (archive `dist/` à jour)
- [ ] `python3 scripts/construire_universel.py` relancé si `accueil-recueil/references/` a changé
- [ ] `CHANGELOG.md` complété ; version alignée dans `plugin.json`, `marketplace.json` et le badge du README si elle change

## Garde-fous

- [ ] Aucun secret, aucune donnée personnelle, aucune invite privée
- [ ] Aucune limite dure retirée ; aucun hook, script tiers ou appel réseau automatique ajouté
- [ ] Tout contenu tiers suit `renfort-externe.md` (licence lue, `NOTICE.md` à jour) ; les skills copiés d'Anthropic restent inchangés
- [ ] Les affirmations de droit ou de norme citent leur source
