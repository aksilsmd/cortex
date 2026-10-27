# Outils et skills par agent

Généré à partir des fiches d'agents : ce tableau dit, pour chaque agent, quelles compétences il précharge
et de quels outils il dispose. Un agent ne peut rien faire d'autre : ce qui exige un autre outil, un skill
extérieur ou un connecteur de la session revient au chef d'orchestre (voir `routage-skills-outils.md`).

| Agent | Pôle | Niveau et modèle | Skills préchargés | Outils |
|---|---|---|---|---|
| `auditeur-general` | Pilotage | A, `inherit`, effort high | `audit-general` | Read, Glob, Grep, Bash, Write |
| `contradicteur` | Pilotage | B, `sonnet`, effort medium | `reunion-decision` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `orchestrateur-de-pole` | Pilotage | B, `sonnet`, effort medium | aucun | Read, Write, Glob, Grep, Agent |
| `planificateur` | Pilotage | B, `sonnet`, effort medium | aucun | Read, Write, Edit, Glob, Grep, Bash |
| `rapporteur` | Pilotage | B, `sonnet`, effort medium | `reunion-decision` | Read, Write, Edit, Glob, Grep |
| `verificateur` | Pilotage | C, `haiku`, effort low | aucun | Read, Glob, Grep, Bash, Write |
| `analyste-concurrence` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-contexte` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-marche` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-voix-client` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `collecteur-web` | Stratégie et marché | C, `haiku`, effort low | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `stratege-produit` | Stratégie et marché | A, `inherit`, effort high | `veille-marche` | Read, Write, Edit, Glob, Grep |
| `expert-cahier-des-charges` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-sfd` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-sfg` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-specs-techniques` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `cartographe-interactions` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, Bash |
| `concepteur-ux` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `expert-accessibilite` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `maquettiste` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-contenu-localisation` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `architecte-donnees` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes` | Read, Write, Edit, Glob, Grep, Bash |
| `architecte-solution` | Architecture et normes | A, `inherit`, effort high | `architecture-normes` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `gardien-des-normes` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes`, `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `ingenieur-devops` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes`, `lancement-exploitation` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `automaticien-tests` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `concepteur-tests` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash |
| `developpeur-backend` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `developpeur-frontend` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `developpeur-mobile` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `executant-tests` | Réalisation et qualité | C, `haiku`, effort low | `usine-logicielle` | Read, Glob, Grep, Bash, Write |
| `integrateur` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `recetteur` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `relecteur-code` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `architecte-securite` | Sécurité | A, `inherit`, effort high | `securite-protection` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `auditeur-securite` | Sécurité | B, `sonnet`, effort medium | `securite-protection`, `robustesse-agents` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `testeur-intrusion` | Sécurité | B, `sonnet`, effort medium | `securite-protection` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `delegue-protection-donnees` | Juridique et conformité | B, `sonnet`, effort medium | `juridique-conformite` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `juriste-numerique` | Juridique et conformité | A, `inherit`, effort high | `juridique-conformite` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `controleur-financier` | Finance | B, `sonnet`, effort medium | `budget-finance` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `expert-acquisition` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `responsable-commercial` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `stratege-marketing` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `responsable-lancement` | Lancement et exploitation | B, `sonnet`, effort medium | `lancement-exploitation` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `responsable-support-formation` | Lancement et exploitation | B, `sonnet`, effort medium | `lancement-exploitation` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |

Lecture : `Read`, `Glob`, `Grep`. Écriture : `Write`, `Edit`. Terminal : `Bash` (scripts du plugin, tests,
outils du projet). Web : `WebSearch`, `WebFetch`. `Agent` n'est utile à l'orchestrateur de pôle que là où
l'imbrication des agents est permise.
