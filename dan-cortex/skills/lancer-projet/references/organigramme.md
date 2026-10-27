# Organigramme du réseau Dan-Cortex

## Sommaire
1. Trois niveaux d'agents
2. Les pôles et leurs agents
3. Qui activer selon le type de projet
4. Fusion des rôles en mode éclair
5. Ajustements de modèle selon le mode

## 1. Trois niveaux d'agents

| Niveau | Rôle | Modèle | Effort | Exemples |
|---|---|---|---|---|
| A — jugement | arbitrer, concevoir, auditer | celui de la session (`inherit`) | élevé | architecte-solution, juriste-numerique, auditeur-general |
| B — production | analyser, rédiger, développer, tester | `sonnet` | moyen | la plupart des experts |
| C — collecte et exécution | collecter, exécuter, vérifier une liste | `haiku` | faible | collecteur-web, executant-tests, verificateur |

Le modèle et l'effort sont déjà inscrits dans chaque fiche d'agent : un lancement sans paramètre applique ce
tableau. Ne passer un modèle à l'appel que pour appliquer les ajustements de la section 5.

Chaque agent précharge le skill de son pôle (ses compétences dédiées) et n'a que les outils de son métier. C'est
ce qui rend son contexte de départ environ dix fois plus petit que celui d'un agent généraliste.

## 2. Les pôles et leurs agents

Type d'agent à lancer : `dan-cortex:<nom>`.

### Pilotage (skills `lancer-projet`, `reunion-decision`, `audit-general`)

| Agent | Niveau | Mission |
|---|---|---|
| `orchestrateur-de-pole` | B | Découpe le travail d'un pôle en ordres de mission parallèles, puis consolide les résultats du pôle |
| `planificateur` | B | Découpage du projet, planning, jalons, RACI, registre des risques et des dépendances |
| `rapporteur` | B | Prépare les réunions, synthétise les positions, rédige le PV et le projet de décision |
| `contradicteur` | B | Avocat du diable : cherche les failles d'une position, d'un plan, d'une décision |
| `auditeur-general` | A | Super-auditeur indépendant : audit à 360° avant lancement et à la clôture |
| `verificateur` | C | Contrôle un livrable contre sa liste de critères, à bas coût |

### Stratégie et marché (skill `veille-marche`)

| Agent | Niveau | Mission |
|---|---|---|
| `analyste-marche` | B | Taille et dynamique du marché, segments, tendances |
| `analyste-concurrence` | B | Démontage des offres concurrentes, matrice fonctionnelle, prix, positionnements |
| `analyste-voix-client` | B | Avis, commentaires, réseaux, forums : irritants, attentes, manques |
| `analyste-contexte` | B | Contexte politique, économique, social, culturel, technologique, environnemental |
| `stratege-produit` | A | Positionnement, proposition de valeur, périmètre, ce qu'il faut ajouter, supprimer, différencier |
| `collecteur-web` | C | Sous-agent de collecte ciblée : une source ou un concurrent, une fiche de faits sourcée |

### Besoin et spécifications (skill `specifications`)

| Agent | Niveau | Mission |
|---|---|---|
| `expert-cahier-des-charges` | B | Expression du besoin, note de cadrage, cahier des charges fonctionnel |
| `redacteur-sfg` | B | Spécifications fonctionnelles générales : fonctions, acteurs, processus, données |
| `redacteur-sfd` | B | Spécifications fonctionnelles détaillées : règles de gestion, cas nominaux et d'exception |
| `redacteur-specs-techniques` | B | Spécifications techniques : contrats d'interface, traitements, formats, paramétrage |

### Design et expérience (skill `maquettes-parcours`)

| Agent | Niveau | Mission |
|---|---|---|
| `concepteur-ux` | B | Recherche utilisateur, personas, parcours, architecture de l'information |
| `cartographe-interactions` | B | Workflow de chaque fonctionnalité ; matrice écran, élément, action, réaction, destination |
| `maquettiste` | B | Maquettes filaires puis haute fidélité, thème, système de design |
| `expert-accessibilite` | B | Exigences et audit d'accessibilité (WCAG, RGAA) |
| `redacteur-contenu-localisation` | B | Microcopie, contenus, traduction, adaptation culturelle |

### Architecture et normes (skill `architecture-normes`)

| Agent | Niveau | Mission |
|---|---|---|
| `architecte-solution` | A | Architecture, choix du langage, des frameworks, de la structure ; décisions d'architecture |
| `architecte-donnees` | B | Schéma et modèle de données, migrations, gouvernance des données |
| `gardien-des-normes` | B | Rédige le référentiel de normes du projet, outille son contrôle, surveille son respect |
| `ingenieur-devops` | B | Infrastructure, environnements, intégration et déploiement continus, supervision |

### Réalisation et qualité (skill `usine-logicielle`)

| Agent | Niveau | Mission |
|---|---|---|
| `developpeur-backend` | B | Lot serveur : code et tests unitaires |
| `developpeur-frontend` | B | Lot interface web : code et tests unitaires |
| `developpeur-mobile` | B | Lot application mobile : code et tests unitaires |
| `integrateur` | B | Intégrations, paramétrage de progiciel, reprise de données |
| `relecteur-code` | B | Revue de code indépendante d'un lot |
| `concepteur-tests` | B | Stratégie de test, cas de test, cahier de recette, traçabilité |
| `automaticien-tests` | B | Tests fonctionnels, d'API, de bout en bout, de performance automatisés |
| `recetteur` | B | Recette globale : campagne, anomalies, PV |
| `executant-tests` | C | Sous-agent : lance une suite de tests et rapporte les échecs |

### Sécurité (skills `securite-protection`, `robustesse-agents`)

| Agent | Niveau | Mission |
|---|---|---|
| `architecte-securite` | A | Analyse de risques, modèle de menaces, architecture de protection, réponse à incident |
| `auditeur-securite` | B | Tests de sécurité complets : code, dépendances, secrets, configuration, application ; robustesse des fonctions d'IA |
| `testeur-intrusion` | B | Test d'intrusion autorisé sur le périmètre du projet, rapport, contre-test |

### Juridique et conformité (skill `juridique-conformite`)

| Agent | Niveau | Mission |
|---|---|---|
| `juriste-numerique` | A | Droit du numérique, de la consommation, des contrats, propriété intellectuelle, pénal, réglementaire |
| `delegue-protection-donnees` | B | Données personnelles : registre, bases légales, analyse d'impact, cookies, IA |

### Finance (skill `budget-finance`)

| Agent | Niveau | Mission |
|---|---|---|
| `controleur-financier` | B | Estimation, budget, justification économique, indicateurs unitaires, financements |

### Marketing et commercial (skill `marketing-commercial`)

| Agent | Niveau | Mission |
|---|---|---|
| `stratege-marketing` | B | Stratégie de mise sur le marché, marque, message, plan de lancement marketing |
| `expert-acquisition` | B | Référencement, contenu, publicité, e-mail, stores, plan de marquage |
| `responsable-commercial` | B | Offre et prix, processus de vente, partenariats |

### Lancement et exploitation (skill `lancement-exploitation`)

| Agent | Niveau | Mission |
|---|---|---|
| `responsable-lancement` | B | Plan de lancement coordonné, plan de bascule, go/no-go, période de surveillance renforcée |
| `responsable-support-formation` | B | Support, documentation utilisateur, formation, conduite du changement |

## 3. Qui activer selon le type de projet

● toujours — ○ si la condition est vraie — · rarement utile

| Agent | site | ecommerce | mobile | saas | niche | erp | Condition du ○ |
|---|---|---|---|---|---|---|---|
| analyste-marche | ○ | ● | ● | ● | ● | ○ | projet tourné vers un marché externe |
| analyste-concurrence | ● | ● | ● | ● | ● | ○ | solutions du marché à comparer |
| analyste-voix-client | ○ | ● | ● | ● | ● | ○ | utilisateurs existants ou avis publics disponibles |
| analyste-contexte | ○ | ○ | ○ | ○ | ○ | ○ | plusieurs pays, secteur régulé, sujet sensible |
| stratege-produit | ● | ● | ● | ● | ● | ○ | périmètre à arbitrer |
| expert-cahier-des-charges | ● | ● | ● | ● | ● | ● | |
| redacteur-sfg | ● | ● | ● | ● | ○ | ● | au-delà d'un produit minimal |
| redacteur-sfd | ● | ● | ● | ● | ○ | ● | au-delà d'un produit minimal |
| redacteur-specs-techniques | ○ | ● | ● | ● | ○ | ● | interfaces ou intégrations à spécifier |
| concepteur-ux | ● | ● | ● | ● | ○ | ○ | parcours nouveaux à concevoir |
| cartographe-interactions | ● | ● | ● | ● | ● | ● | |
| maquettiste | ● | ● | ● | ● | ○ | ○ | interface sur mesure |
| expert-accessibilite | ● | ● | ● | ○ | ○ | ○ | public large ou obligation légale |
| redacteur-contenu-localisation | ● | ● | ○ | ○ | ○ | ○ | plusieurs langues ou contenu éditorial |
| architecte-solution | ● | ● | ● | ● | ● | ● | |
| architecte-donnees | ○ | ● | ○ | ● | ○ | ● | modèle de données non trivial |
| gardien-des-normes | ● | ● | ● | ● | ○ | ● | code produit par plusieurs agents |
| ingenieur-devops | ● | ● | ● | ● | ○ | ● | hébergement à concevoir |
| developpeur-backend | ○ | ○ | ○ | ● | ● | ○ | code serveur sur mesure |
| developpeur-frontend | ● | ● | · | ● | ● | ○ | interface web sur mesure |
| developpeur-mobile | · | ○ | ● | ○ | ○ | ○ | application mobile |
| integrateur | ○ | ● | ○ | ○ | ○ | ● | progiciel, intégrations, reprise de données |
| relecteur-code | ● | ● | ● | ● | ○ | ● | dès qu'il y a du code |
| concepteur-tests | ● | ● | ● | ● | ● | ● | |
| automaticien-tests | ● | ● | ● | ● | ○ | ● | |
| recetteur | ● | ● | ● | ● | ● | ● | |
| architecte-securite | ● | ● | ● | ● | ○ | ● | données personnelles, paiement ou comptes |
| auditeur-securite | ● | ● | ● | ● | ● | ● | |
| testeur-intrusion | ○ | ● | ● | ● | ○ | ● | exposition à internet et données sensibles |
| juriste-numerique | ● | ● | ● | ● | ● | ● | |
| delegue-protection-donnees | ○ | ● | ● | ● | ○ | ● | données personnelles traitées |
| controleur-financier | ● | ● | ● | ● | ● | ● | |
| stratege-marketing | ○ | ● | ● | ● | ● | · | lancement vers un public externe |
| expert-acquisition | ● | ● | ● | ● | ○ | · | acquisition en ligne |
| responsable-commercial | · | ○ | ○ | ● | ○ | ○ | vente à des entreprises |
| responsable-lancement | ● | ● | ● | ● | ○ | ● | mise en production réelle |
| responsable-support-formation | ○ | ● | ○ | ● | ○ | ● | utilisateurs à accompagner |
| planificateur | ● | ● | ● | ● | ○ | ● | au-delà de quelques semaines |
| auditeur-general | ● | ● | ● | ● | ● | ● | |

`rapporteur`, `contradicteur`, `verificateur`, `collecteur-web`, `executant-tests` et `orchestrateur-de-pole`
sont des agents de service, activés par les protocoles (réunions, essaimage, revues, orchestration déléguée).

## 4. Fusion des rôles en mode éclair

En mode `eclair`, une mission regroupe plusieurs rôles voisins. Lancer l'agent indiqué en lui donnant les
missions fusionnées, et lui indiquer les références de l'autre rôle à lire.

| Agent lancé | Rôles absorbés |
|---|---|
| analyste-concurrence | analyste-marche, analyste-voix-client, analyste-contexte |
| expert-cahier-des-charges | redacteur-sfg |
| redacteur-sfd | redacteur-specs-techniques |
| cartographe-interactions | concepteur-ux, maquettiste (maquettes filaires seulement) |
| architecte-solution | architecte-donnees, gardien-des-normes, ingenieur-devops |
| developpeur-backend ou developpeur-frontend | relecteur-code remplacé par les contrôles automatiques |
| concepteur-tests | automaticien-tests, recetteur |
| auditeur-securite | architecte-securite, testeur-intrusion (contrôles automatisés seulement) |
| juriste-numerique | delegue-protection-donnees |
| stratege-marketing | expert-acquisition, responsable-commercial, responsable-lancement |

## 5. Ajustements de modèle selon le mode

| Mode | Ajustement |
|---|---|
| `eclair` | Si la session tourne sur un modèle haut de gamme et que l'enjeu est modeste, lancer les agents de niveau A avec `model: sonnet`. |
| `standard` | Aucun : appliquer les fiches. |
| `integral` | Lancer `contradicteur` et `testeur-intrusion` sur le modèle de la session. Pour une décision de type 1, le `rapporteur` aussi. |
