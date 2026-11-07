# Sources externes du pôle Sécurité

Trace des apports externes consultés, selon `robustesse-agents/references/renfort-externe.md`.

## claude-red — SnailSploit/Claude-Red

- Dépôt : https://github.com/SnailSploit/Claude-Red
- Nature : bibliothèque externe de compétences de sécurité **offensive** pour le système de skills de Claude.
- Date d'identification : 2026-11-07 (recherche web, à la demande de l'utilisateur).
- État : **non installé**, non invocable. Aucun fichier, script ni texte repris. Licence non lue ; forme B interdite tant qu'elle ne l'est pas.
- Usage retenu : forme A, au seul niveau de la **taxonomie des classes d'attaques à couvrir**, reformulée de notre propre connaissance et mappée sur nos tests locaux V10 (voir `references/renforts-securite.md`).
- Écarté comme dangereux (décision utilisateur « retire ce que tu vois dangereux ») : charges utiles prêtes à l'emploi, scripts d'exploitation, techniques hors périmètre applicatif (deauth, MITM, cassage de mots de passe réels).
- Raison : règle d'or du pôle (angle strictement défensif), DEC-001 (tests en local sur le périmètre du projet), et « pas de destruction ».

## safety — compétence du compte (VigieTrace)

- Nature : référentiel **défensif** (détection, forensic, trafic/protocoles, CVE, crypto à clés fournies, audit d'identifiants, MITRE ATT&CK), excluant l'outillage offensif opérationnel.
- État : compétence activée sur le compte, invocable. Inscrite dans la liste `skills` des agents du pôle Sécurité.
