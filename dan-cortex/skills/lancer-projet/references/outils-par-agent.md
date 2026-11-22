# Outils et skills par agent

Tiré des fiches d'agents (`agents/*.md`), qui font foi ; un test vérifie qu'il les suit. Ce tableau dit, pour chaque agent, quelles compétences il précharge
et de quels outils il dispose. Un agent ne peut rien faire d'autre : ce qui exige un autre outil, un skill
extérieur ou un connecteur de la session revient au chef d'orchestre (voir `routage-skills-outils.md`).

| Agent | Pôle | Niveau et modèle | Skills préchargés | Outils |
|---|---|---|---|---|
| `orchestrateur-de-pole` | Pilotage | B, `sonnet`, effort medium | aucun | Read, Write, Glob, Grep, Agent |
| `planificateur` | Pilotage | B, `sonnet`, effort medium | `cartographie-graphe` | Read, Write, Edit, Glob, Grep, Bash |
| `rapporteur` | Pilotage | B, `sonnet`, effort medium | `reunion-decision` | Read, Write, Edit, Glob, Grep |
| `contradicteur` | Pilotage | B, `sonnet`, effort medium | `reunion-decision` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `auditeur-general` | Pilotage | A, `inherit`, effort high | `audit-general` | Read, Glob, Grep, Bash, Write |
| `verificateur` | Pilotage | C, `haiku`, effort low | aucun | Read, Glob, Grep, Bash, Write |
| `suivi-avancement` | Pilotage | C, `haiku`, effort low | aucun | Read, Glob, Grep, Bash, Write |
| `vigie-oublis` | Pilotage | A, `inherit`, effort high | `audit-general`, `cartographie-graphe` | Read, Glob, Grep, Bash, Write |
| `analyste-marche` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-concurrence` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-voix-client` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `analyste-contexte` | Stratégie et marché | B, `sonnet`, effort medium | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `stratege-produit` | Stratégie et marché | A, `inherit`, effort high | `veille-marche` | Read, Write, Edit, Glob, Grep |
| `collecteur-web` | Stratégie et marché | C, `haiku`, effort low | `veille-marche` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `expert-cahier-des-charges` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-sfg` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-sfd` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `redacteur-specs-techniques` | Besoin et spécifications | B, `sonnet`, effort medium | `specifications` | Read, Write, Edit, Glob, Grep, Bash |
| `intervieweur` | Besoin et spécifications | B, `sonnet`, effort medium | `recueil-besoin`, `specifications` | Read, Write, Edit, Glob, Grep |
| `concepteur-ux` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours`, `design-apple`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `cartographe-interactions` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, Bash |
| `maquettiste` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours`, `design-apple`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash |
| `expert-accessibilite` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours`, `design-apple`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `redacteur-contenu-localisation` | Design et expérience | B, `sonnet`, effort medium | `maquettes-parcours` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `architecte-solution` | Architecture et normes | A, `inherit`, effort high | `architecture-normes`, `cartographie-graphe`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `architecte-donnees` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes`, `cartographie-graphe`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash |
| `gardien-des-normes` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes`, `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `ingenieur-devops` | Architecture et normes | B, `sonnet`, effort medium | `architecture-normes`, `lancement-exploitation`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `developpeur-backend` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `cartographie-graphe`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `developpeur-frontend` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `design-apple`, `cartographie-graphe`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `developpeur-mobile` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `design-apple`, `cartographie-graphe`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `integrateur` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `relecteur-code` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `cartographie-graphe`, `design-apple` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `concepteur-tests` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash |
| `automaticien-tests` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `recetteur` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `executant-tests` | Réalisation et qualité | C, `haiku`, effort low | `usine-logicielle` | Read, Glob, Grep, Bash, Write |
| `organisateur` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `cartographie-graphe` | Read, Write, Edit, Glob, Grep, Bash |
| `testeur-web` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `maquettes-parcours`, `design-apple`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `testeur-mobile` | Réalisation et qualité | B, `sonnet`, effort medium | `usine-logicielle`, `maquettes-parcours`, `design-apple`, `mouvement-interface` | Read, Write, Edit, Glob, Grep, Bash, WebFetch |
| `testeur-visuel` | Réalisation et qualité | B, `sonnet`, effort medium | `design-apple`, `mouvement-interface` | Read, Glob, Grep, Bash, Write |
| `architecte-securite` | Sécurité | A, `inherit`, effort high | `securite-protection`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `auditeur-securite` | Sécurité | B, `sonnet`, effort medium | `securite-protection`, `robustesse-agents`, `cartographie-graphe`, `crm-twenty` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `testeur-intrusion` | Sécurité | B, `sonnet`, effort medium | `securite-protection`, `cartographie-graphe` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `juriste-numerique` | Juridique et conformité | A, `inherit`, effort high | `juridique-conformite`, `crm-twenty` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `delegue-protection-donnees` | Juridique et conformité | B, `sonnet`, effort medium | `juridique-conformite`, `crm-twenty` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `controleur-financier` | Finance | B, `sonnet`, effort medium | `budget-finance` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `stratege-marketing` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `expert-acquisition` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `responsable-commercial` | Marketing et commercial | B, `sonnet`, effort medium | `marketing-commercial`, `crm-twenty` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `responsable-lancement` | Lancement et exploitation | B, `sonnet`, effort medium | `lancement-exploitation` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `responsable-support-formation` | Lancement et exploitation | B, `sonnet`, effort medium | `lancement-exploitation` | Read, Write, Edit, Glob, Grep, WebSearch, WebFetch |
| `architecte-recit` | Écriture et édition | B, `sonnet`, effort medium | `atelier-ecriture` | Read, Write, Edit, Glob, Grep |
| `plume` | Écriture et édition | B, `sonnet`, effort medium | `atelier-ecriture` | Read, Write, Edit, Glob, Grep |
| `editeur-litteraire` | Écriture et édition | B, `sonnet`, effort medium | `atelier-ecriture` | Read, Write, Edit, Glob, Grep, Bash |
| `concepteur-univers` | Écriture et édition | B, `sonnet`, effort medium | `atelier-ecriture` | Read, Write, Edit, Glob, Grep |
| `traducteur` | Traduction et localisation | B, `sonnet`, effort medium | `traduction-interpretariat` | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch |
| `interprete` | Traduction et localisation | B, `sonnet`, effort medium | `traduction-interpretariat` | Read, Write, Edit, Glob, Grep |
| `localisateur` | Traduction et localisation | B, `sonnet`, effort medium | `traduction-interpretariat`, `usine-logicielle` | Read, Write, Edit, Glob, Grep, Bash |

Lecture : `Read`, `Glob`, `Grep`. Écriture : `Write`, `Edit`. Terminal : `Bash` (scripts du plugin, tests,
outils du projet). Web : `WebSearch`, `WebFetch`. `Agent` n'est utile à l'orchestrateur de pôle que là où
l'imbrication des agents est permise.
