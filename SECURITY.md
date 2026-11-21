# Politique de sécurité

## Versions prises en charge

| Version | Correctifs de sécurité |
|---|---|
| 2.1.x | oui |
| 2.0.x | oui, jusqu'à la publication de la 2.2.0 |
| < 2.0 | non |

## Signaler une vulnérabilité

**N'ouvre pas de ticket public.** Utilise le signalement privé de GitHub :
[Security → Report a vulnerability](https://github.com/aksilsmd/cortex/security/advisories/new).

Indique, sans aucun vrai secret ni donnée personnelle :

- la version et le fichier concernés (skill, agent, script) ;
- le scénario : ce qu'un attaquant contrôle (page web lue, document, sortie d'outil, dépôt) et ce qu'il obtient ;
- les étapes pour reproduire, avec des valeurs fictives ;
- l'impact estimé et, si tu en as une, une piste de correction.

## Délais

| Étape | Délai visé |
|---|---|
| Accusé de réception | 5 jours ouvrés |
| Première évaluation (recevable, gravité) | 10 jours ouvrés |
| Correctif ou mesure de contournement | selon la gravité, 30 jours au plus pour une faille grave |

Le projet est maintenu bénévolement : ces délais sont des engagements de moyens. Tu es crédité dans le
`CHANGELOG.md` si tu le souhaites.

## Périmètre

Dans le périmètre :

- les scripts du dépôt (`cortex.py`, `essais.py`, `robustesse.py` et le paquet `ccal`, `scripts/*.py`) ;
- les consignes des skills et des agents qui pourraient conduire un agent à contourner une limite dure, à exécuter
  une instruction lue dans une donnée, ou à exposer un secret ;
- le gabarit de réglages `robustesse-agents/assets/reglages-autonomes.json` ;
- l'archive `dist/dan-cortex.plugin`.

Hors périmètre (à signaler à leur projet d'origine) :

- les skills copiés sans modification d'[anthropics/skills](https://github.com/anthropics/skills) (`docx`, `pdf`,
  `pptx`, `xlsx`, `skill-creator`, `mcp-builder`, `webapp-testing`, `web-artifacts-builder`, `slack-gif-creator`,
  `algorithmic-art`, `claude-api`, `academy-guide`, `brand-guidelines`) — un signalement ici reste utile pour que
  nous puissions retirer ou geler un dossier ;
- les outils séparés (IT-Tools, Graphify, Twenty) ;
- Claude, Claude Code et l'application Claude eux-mêmes.

## Règles de test

Teste seulement sur ta propre installation et tes propres projets. N'utilise jamais Dan-Cortex pour éprouver un
système dont tu n'as pas l'autorisation écrite du propriétaire. Voir aussi
[`docs/securite-et-robustesse.md`](docs/securite-et-robustesse.md).
