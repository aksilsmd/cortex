# Routage des skills et des outils

Les agents Dan-Cortex n'ont que leurs outils de métier et le skill de leur pôle : c'est ce qui les rend sobres. Les
skills et connecteurs extérieurs au plugin, eux, ne sont accessibles qu'à toi, le noyau, ou à un agent
généraliste. À J0, fais l'inventaire de ce que la session offre et décide qui s'en sert.

## Inventaire à J0

1. Parcourir la liste des skills disponibles dans la session et celle des connecteurs.
2. Retenir ceux qui servent le projet, les inscrire dans `00-pilotage/organigramme.md`, section « Skills et
   outils de la session mis à contribution ».
3. Appliquer la règle : **le skill extérieur finit le travail, l'agent Dan-Cortex le prépare.**

## Table de routage

| Besoin | Si disponible dans la session | Qui l'utilise | Repli sans cet outil |
|---|---|---|---|
| Recherche et lecture web | recherche web et lecture de page natives | agents d'analyse | demander à l'utilisateur les documents |
| Extraction de pages difficiles, sites dynamiques | connecteur d'extraction web (Firecrawl ou équivalent), navigateur | toi, ou un agent généraliste pour une collecte lourde | collecte manuelle par l'utilisateur |
| Document Word, PDF, présentation | skills de documents (`docx`, `pdf`, `pptx`) ou types de documents de l'application | toi, à partir du Markdown produit par l'agent | livrer le Markdown |
| Tableur (budget, planning, matrice) | skill `xlsx` ou type tableur | toi, à partir des tableaux du `controleur-financier` ou du `planificateur` | tableaux Markdown ou CSV |
| Maquettes | connecteur Figma, type Design de l'application | toi, à partir du cahier de maquettes du `maquettiste` | maquettes HTML ou SVG écrites par le `maquettiste` |
| Diagrammes | Mermaid dans le Markdown | tous les agents | description textuelle structurée |
| Suivi de tâches | connecteur de gestion de projet (Jira, Linear, Asana, monday…) | toi, après accord de l'utilisateur | registres du dossier projet |
| Dépôt de code | git local ; plateforme distante par son outil en ligne de commande | développeurs en local ; toi pour le distant, après accord | archive du code |
| Tests de navigateur | Playwright s'il est installé | `automaticien-tests`, `recetteur` | cas de test manuels décrits pas à pas |
| Analyse de sécurité | outils installés dans l'environnement (analyse statique, dépendances, secrets) | `auditeur-securite` | revue manuelle guidée par les listes de contrôle |
| Revue juridique, conformité | skills juridiques de la session s'il y en a | toi, en complément du `juriste-numerique` | références du skill `juridique-conformite` |
| Campagnes, contenus, visuels | skills marketing ou de création visuelle de la session | toi, à partir du plan du `stratege-marketing` | contenus Markdown |
| Données et tableaux de bord | skills de données de la session | toi, à partir du plan de marquage | spécification du tableau de bord |

## Quand lancer un agent généraliste

Seulement si une mission exige, en son cœur, un skill ou un connecteur extérieur et que tu ne peux pas la faire
toi-même sans encombrer ton contexte. Lui donner alors la fiche de l'agent Dan-Cortex correspondant à lire
(`agents/<nom>.md` à la racine du plugin) en plus du skill extérieur, et le même format d'ordre de mission. Son
contexte de départ est environ dix fois plus lourd : une mission, pas une habitude.

## Choisir les outils du projet lui-même

Le choix du langage, des frameworks, de la base de données, de l'hébergement, des dépendances et des outils de
test du projet n'est pas un routage de session : c'est une décision d'architecture, instruite par
`architecte-solution` et `gardien-des-normes`, tranchée en comité d'architecture (voir le skill
`architecture-normes`) et inscrite dans une décision d'architecture.
