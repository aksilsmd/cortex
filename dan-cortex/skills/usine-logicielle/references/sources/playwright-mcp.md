# Collecte — Playwright MCP et Playwright Test

Pages consultées le 2026-11-03 (outils : Firecrawl scrape/query, WebSearch, WebFetch). Résumés et reformulations ; aucune copie de page.

| URL | Titre | Apport |
|---|---|---|
| https://github.com/microsoft/playwright-mcp | microsoft/playwright-mcp | `npx @playwright/mcp@latest` ; pilotage par instantanés d'accessibilité (pas de modèle de vision) ; outils de base (navigate, click, type, fill_form, snapshot, screenshot, console, network, evaluate, wait_for, file_upload, handle_dialog…) ; capacités optionnelles `--caps` : config, network, storage, devtools (traces, vidéo), vision (coordonnées), pdf, testing (localisateurs, vérifications) ; nombreuses options (`--isolated`, `--user-data-dir`, `--storage-state`, `--allowed-origins`, `--blocked-origins`, `--allowed-hosts`, `--secrets`, `--output-dir`, `--save-session`, `--redact-url-params`, `--extension`, `--cdp-endpoint`, `--device`, `--test-id-attribute`…) ; « pas une frontière de sécurité » ; les agents de code privilégient de plus en plus une CLI exposée en skill, plus économe en tokens. |
| https://testdino.com/blog/playwright-2026-new-features/ | Playwright 2026 release summary (source secondaire) | 1.56 (nov. 2025) agents de test planner/generator/healer ; 1.57 (déc. 2025) Chrome for Testing ; 1.58 (janv. 2026) timeline, retrait des sélecteurs `_react`/`_vue` ; 1.59 (avr. 2026) `page.screencast`, `browser.bind()` pour partager un navigateur entre CLI, MCP et API, `npx playwright trace`. |
| https://currents.dev/posts/pw-1.60.0 | Playwright 1.60.0 (Currents) | Existence d'une version 1.60 ; contenu non vérifié : version exacte à confirmer avec `npx playwright --version`. |
| https://github.com/affaan-m/everything-claude-code | everything-claude-code | « ECC » = Everything Claude Code, collection de configuration pour Claude Code (agents, skills, commandes, hooks, règles). |
| https://dev.to/shimo4228/everything-claude-code-ecc-complete-cheatsheet-24ok | ECC complete cheatsheet (DEV) | Agents dont `e2e-runner`, commande `/e2e` qui génère et exécute des tests Playwright ; pas de mention MCP dans l'extrait ; licence non indiquée. |
| https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices | MCP Security Best Practices | Renvoi du dépôt Playwright MCP pour sécuriser un déploiement (non récupérée en détail). |
