# Sources — skill crm-twenty

Dépôt consulté en lecture seule le 2026-11-07 (clone superficiel et partiel, aucun script exécuté, aucune dépendance installée). Forme A de `robustesse-agents/references/renfort-externe.md` : méthodes reformulées en français, aucun texte copié (licence copyleft AGPL-3.0, la forme B est exclue).

| Dépôt | Licence (fichier) | Commit consulté | Fichiers lus | Reprise |
|---|---|---|---|---|
| https://github.com/twentyhq/twenty | AGPL-3.0 + permission additionnelle (section 7, applications) ; fichiers `@license Enterprise` sous licence commerciale ; SDK, CLI, twenty-ui et applications sous MIT (fichier LICENSE) | `eda542a5f242e137c68f841140d230dfbaada58f` (dernière étiquette : v2.9.0) | `LICENSE`, `README.md`, `SKILLS.md`, `packages/twenty-docker/docker-compose.yml`, `packages/twenty-docker/.env.example`, `packages/twenty-agent-skills/references/concepts/how-apps-work.md`, `operating-rules.md`, `use-twenty-mcp/setup.md`, `develop-app/data-model.md` (début), titres de `workflows.md` et `logic.md` | règles réécrites : `crm-twenty/SKILL.md`, `references/exploitation-securite.md` |

Sources de sécurité :
- CVE-2026-26720, « Twenty CRM RCE via Serverless Workflow Functions » (v1.15.0, critique), selon https://cve.imfht.com/intel/553212 (consulté le 2026-11-07). La version corrigée est à vérifier sur les avis GitHub du dépôt avant chaque installation.

Exclus : tout script, image ou fichier Docker du dépôt (Dan-Cortex n'embarque rien) ; les compétences officielles `npx skills add …` (non installées à côté de Dan-Cortex) ; `AGENTS.md` et `CLAUDE.md` du dépôt (consignes destinées aux contributeurs de Twenty). Filtres §3 : licence lue dans LICENSE ; aucun hook ; aucune consigne reprise ; caractères invisibles recherchés dans les fichiers reformulés.

Prochaine revue : à chaque usage réel, et au plus tard 2027-02 (version, avis de sécurité, licence).
