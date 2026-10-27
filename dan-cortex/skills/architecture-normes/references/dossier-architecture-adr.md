# Dossier d'architecture et décisions d'architecture

Gabarits du dossier d'architecture (vues C4, arc42 condensé) et d'une décision d'architecture (ADR) avec options écartées. Un dossier court et à jour vaut mieux qu'un dossier exhaustif et périmé.

## Sommaire
1. Principes de rédaction
2. Gabarit du dossier d'architecture
3. Vues C4
4. Gabarit d'une ADR
5. Du comité au registre
6. Pièges et contrôles

## 1. Principes de rédaction

- Le dossier est écrit pour le développeur, l'exploitant et l'auditeur qui arrivent après vous.
- Chaque affirmation structurante renvoie à une ADR ; chaque exigence non fonctionnelle (`EXNF-`) à une décision ou à un scénario.
- Les schémas sont en Mermaid, au plus quinze éléments chacun.
- Les décisions vivent avec le code : `03-conception/architecture/adr/ADR-<n>-<sujet>.md`, numérotées sans trou, jamais supprimées (statut « remplacée »).

## 2. Gabarit du dossier d'architecture

arc42 compte 12 sections (titres de la version courante : à vérifier sur arc42.org). Le gabarit les condense en les rattachant aux vues C4.

````markdown
# Dossier d'architecture — <projet>
## Synthèse
<style retenu, pile, hébergement, 3 décisions clés avec ADR-, risques principaux, points ouverts>
## 1. Objectifs et contraintes
Objectifs métier, parties prenantes, contraintes techniques, légales, budgétaires. EX- et EXNF- structurants.
## 2. Contexte et périmètre
Vue C4 niveau 1 (contexte) : le système, ses utilisateurs, les systèmes externes.
## 3. Stratégie de solution
Acheter, configurer ou construire (ADR-), style, pile, grille de décision résumée.
## 4. Vue des briques
Vue C4 niveau 2 (conteneurs) : applications, bases, files, services ; technologies et protocoles.
Vue C4 niveau 3 (composants) pour chaque conteneur complexe seulement. Niveau 4 (code) : jamais écrit à la main.
## 5. Vue d'exécution
Trois à cinq scénarios clés en diagramme de séquence (connexion, paiement, traitement asynchrone).
## 6. Vue de déploiement
Environnements, hébergement, réseau, zones de confiance (renvoi à `infrastructure.md`).
## 7. Concepts transverses
Sécurité, gestion des erreurs, journalisation, authentification, internationalisation, tenancy, données (renvoi à `modele-donnees.md`).
## 8. Décisions d'architecture
| ADR | Sujet | Exigences EXNF- couvertes | Statut |
## 9. Qualité
Arbre d'utilité, scénarios, résultats d'évaluation, fitness functions en place.
## 10. Risques et dette technique
| Risque | Origine | Parade | Responsable |
## 11. Fins de support
| Composant | Version | Fin de support | Échéance de migration |
## 12. Glossaire
````

## 3. Vues C4

| Niveau | Montre | Public |
|---|---|---|
| 1 Contexte | le système au milieu de ses utilisateurs et systèmes voisins | tous |
| 2 Conteneurs | ce qui s'exécute et se déploie séparément | développeurs, exploitants |
| 3 Composants | les blocs internes d'un conteneur | développeurs du conteneur |
| 4 Code | classes et fonctions | généré par l'outil, si besoin |

Chaque flèche porte un verbe et un protocole. Les frontières de confiance sont tracées et validées par `architecte-securite`.

## 4. Gabarit d'une ADR

Une ADR par décision architecturalement significative : langage, framework structurant, base, broker, style, hébergement, tenancy, acheter ou construire, dépendance majeure.

````markdown
# ADR-001 — <sujet de la décision>
## Synthèse
<décision en une phrase, option retenue, score, statut>
| Champ | Valeur |
|---|---|
| Statut | proposée, acceptée, remplacée par ADR-n ou rejetée |
| Date et décideur | <date>, <nom ou comité d'architecture> |
| Type | 1 (irréversible ou coûteuse) ou 2 |
| Registre | DEC-<n> |
| Exigences | EXNF-001, EXNF-004 |
## Contexte
Problème, contraintes, exigences et scénarios de qualité concernés.
## Options étudiées
| Option | Description | Score sur 100 | Forces | Faiblesses |
(au moins deux ; notes détaillées par critère en annexe, grille de `choix-techniques.md`)
## Décision
Option retenue, en une phrase active.
## Options écartées
| Option | Motif d'exclusion | Ce qui la ferait reconsidérer |
## Conséquences
Positives, négatives, risques acceptés, dette créée.
## Coût de sortie et réversibilité
Ce qu'il faudrait pour changer, en durée et en coût.
## Réexamen
Date ou événement (fin de support, changement de licence, seuil de volumétrie).
## Vérification
Fitness function, test ou revue qui contrôle que la décision est respectée.
````

## 5. Du comité au registre

1. L'architecte écrit les ADR au statut « proposée », une par décision.
2. Le comité d'architecture (collégiale) examine les options, les risques, le coût de sortie. Le `rapporteur` rédige le PV.
3. Décision de type 1 : soumise à l'utilisateur avant le statut « acceptée ».
4. Enregistrer : `python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/cortex.py registre decisions ajouter titre="…" type=1 decision="…" motifs="…" options_ecartees="…" decideur="…" statut=a-valider`, puis noter le `DEC-` dans l'ADR.
5. Une décision remplacée n'est pas effacée : nouvelle ADR, ancienne marquée « remplacée par ».

## 6. Pièges et contrôles

Pièges : ADR écrite après coup pour justifier ; une seule option « comparée » à un homme de paille ; options écartées sans motif ; dossier qui décrit l'intention et non le système livré ; diagramme sans légende. Avant de rendre : chaque ADR a deux options, son score, son coût de sortie et un statut ; le dossier cite toutes les ADR ; la section fins de support est remplie ; le script `docs verifier` ne signale rien.

## Sources

- C4 model : https://c4model.com/introduction
- arc42 : https://arc42.org/overview/
- ADR : https://adr.github.io/
- Fowler, ADR avec le code : https://martinfowler.com/articles/scaling-architecture-conversationally.html
- Thoughtworks, techniques durables : https://www.thoughtworks.com/en-us/insights/articles/enduring-techniques-technology-radar
