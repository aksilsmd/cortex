# Contrôles — robustesse des agents

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.
Les contrôles sans condition portent sur le réseau d'agents qui mène la mission ; ceux marqués `autonome` s'ajoutent
quand le chef d'orchestre travaille en autonomie ; ceux marqués `ia` portent sur les fonctions d'IA du produit et
complètent `SEC-025`.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| ROB-001 | J1 | majeur | tous | - | Les réglages Claude Code de la mission sont audités avant la première vague, et chaque constat HIGH est corrigé ou accepté par l'utilisateur au registre des risques | 00-pilotage/audits/audit-reglages-agents.md | Anthropic, Claude Code sandboxing |
| ROB-002 | J1 | majeur | tous | - | Les ordres de mission des agents qui lisent des sources extérieures posent que ces contenus sont des données non fiables, et les comptes rendus signalent toute instruction trouvée sans l'exécuter | 00-pilotage/audits/audit-reglages-agents.md | OWASP LLM01:2025 |
| ROB-003 | J1 | mineur | tous | - | Aucun secret réel (clé d'API, mot de passe, jeton) ne figure dans les ordres de mission, les journaux d'agents ni les rapports du dossier projet | 00-pilotage/audits/audit-reglages-agents.md | OWASP LLM02:2025 |
| ROB-004 | J1 | bloquant | tous | autonome | Les autorisations permanentes (effet, cible exacte, limite) et les limites dures sont écrites dans la fiche projet et approuvées par l'utilisateur avant la première vague | 00-pilotage/fiche-projet.md | bonne pratique |
| ROB-005 | J1 | majeur | tous | autonome | Les réglages Claude Code de la mission reposent sur des règles ciblées et le bac à sable, sans mode de contournement des permissions, et leur audit ne remonte aucun constat HIGH | 00-pilotage/audits/audit-reglages-agents.md | Anthropic, Claude Code sandboxing |
| ROB-006 | J2 | majeur | tous | autonome | Chaque décision de type 1 prise en autonomie figure au registre au statut provisoire, avec son option de repli et son coût d'annulation, jusqu'à confirmation par l'utilisateur | 00-pilotage/registres/decisions.csv | bonne pratique |
| ROB-010 | J3 | bloquant | tous | ia | Le modèle de menaces trace chaque point où un contenu non fiable atteint un modèle d'IA et y traite l'injection d'instructions directe et indirecte | 03-conception/securite/modele-menaces.md | OWASP LLM01:2025 |
| ROB-011 | J3 | majeur | tous | ia | Les sorties d'un modèle d'IA sont validées ou échappées avant tout affichage, requête, commande ou appel d'outil | 03-conception/securite/architecture-securite.md | OWASP LLM05:2025 |
| ROB-012 | J3 | majeur | tous | ia | Toute action destructive, financière ou à effet extérieur déclenchée par un agent d'IA exige une confirmation humaine explicite | 03-conception/securite/architecture-securite.md | OWASP LLM06:2025 |
| ROB-013 | J3 | majeur | tous | ia | L'invite système ne contient aucun secret, et les données sensibles visibles du modèle sont limitées au besoin de la fonction | 03-conception/securite/architecture-securite.md | OWASP LLM07:2025 ; LLM02:2025 |
| ROB-014 | J3 | majeur | tous | ia | Les appels aux modèles sont bornés par utilisateur (taille d'entrée, quotas, plafond de coût) avec une alerte avant dépassement | 03-conception/securite/architecture-securite.md | OWASP LLM10:2025 |
| ROB-015 | J3 | majeur | tous | ia | Le plan de tests de sécurité contient un corpus de scénarios de robustesse identifiés, un par menace retenue, avec leurs critères PASS, REVIEW et FAIL | 03-conception/securite/plan-tests-securite.md | OWASP DevSecOps Guideline, tests IA/LLM |
| ROB-016 | J5 | bloquant | tous | ia | Le corpus est joué en recette avec modèle, invite système et configuration notés, et chaque FAIL ouvre une anomalie corrigée puis rejouée | 05-validation/rapport-robustesse-agents.md | OWASP DevSecOps Guideline, tests IA/LLM |
| ROB-017 | J5 | majeur | tous | ia | Chaque scénario est répété plusieurs fois et son taux de réussite est consigné, pour tenir compte du caractère non déterministe des modèles | 05-validation/rapport-robustesse-agents.md | bonne pratique |
| ROB-018 | J5 | majeur | tous | ia | Chaque résultat REVIEW est tranché par une personne nommée, et aucun verdict de sécurité ne repose sur la seule notation heuristique ou un modèle juge | 05-validation/rapport-robustesse-agents.md | OWASP DevSecOps Guideline, tests IA/LLM |
| ROB-019 | J7 | mineur | tous | ia | Les scénarios en échec restent au corpus de non-régression et sont rejoués à chaque changement de modèle, d'invite système ou d'outil | 07-exploitation/bilan-de-projet.md | bonne pratique |
