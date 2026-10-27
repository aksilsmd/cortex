# Recherche utilisateur, personas, parcours, architecture de l'information

Ce fichier cadre la phase « comprendre » (jalon J2) : qui sont les utilisateurs, ce qu'ils cherchent à accomplir, comment organiser le contenu. Livrable : `02-cadrage/personas-parcours.md`.

## Sommaire
1. Ce qu'on peut établir sans utilisateurs
2. Personas
3. Parcours cibles
4. Architecture de l'information
5. Validation et niveau de preuve
6. Gabarit de `personas-parcours.md`
7. Pièges et contrôles avant de rendre

## 1. Ce qu'on peut établir sans utilisateurs

Un agent n'interroge personne : il travaille sur la voix du client (`01-decouverte/voix-du-client.md`), le benchmark, le cahier des charges et les données fournies par l'utilisateur. Tout ce qui en découle est une **hypothèse de conception**, à écrire comme telle. Pourquoi : un persona inventé qui se présente comme un fait fausse toutes les décisions en aval.

| Matière disponible | Usage | Niveau de preuve |
|---|---|---|
| Avis et verbatims collectés (sourcés, datés) | motivations, irritants, vocabulaire | indice |
| Entretiens ou tests menés par l'utilisateur | personas, parcours | preuve |
| Statistiques du site ou du produit existant | volumes, appareils, abandons | preuve si l'outil est fiable |
| Benchmark concurrentiel | attentes de marché, conventions | indice |
| Rien | personas de travail | hypothèse |

Quand les données manquent, proposer à l'utilisateur un plan minimal : 5 entretiens par segment principal, puis un test d'utilisabilité sur le filaire. Ne pas annoncer de taille d'échantillon « statistiquement valable » pour du qualitatif.

## 2. Personas

1. **Segmenter par comportement et objectif**, pas par âge ou profession. Deux personnes de profil différent qui poursuivent le même but suivent le même parcours.
2. **Limiter** : 3 à 5 personas, dont un seul principal (celui pour qui l'on dessine d'abord). Un persona secondaire ne doit pas dégrader le parcours du principal.
3. **Ajouter les personas de bord** : personne en situation de handicap, utilisateur peu à l'aise avec le numérique, administrateur, support. Ce sont eux que les maquettes oublient.
4. **Documenter par persona** : objectif principal, contexte d'usage (appareil, lieu, connexion, langue), compétences numériques, freins, déclencheurs, critère de réussite mesurable, source et niveau de preuve.
5. **Relier chaque persona aux exigences** `EX-` qu'il justifie. Un persona sans exigence est décoratif.

## 3. Parcours cibles

Un parcours cible est la suite d'étapes qui mène un persona de son déclencheur à son résultat, avec ce qu'il fait, pense et ressent.

1. Choisir 3 à 7 parcours : ceux qui portent la valeur (achat, première utilisation, tâche principale) et ceux qui coûtent cher en cas d'échec (paiement, récupération de compte, résiliation).
2. Pour chaque parcours : déclencheur, étapes, canaux, points de douleur, moments clés, résultat, mesure de succès.
3. Marquer les **moments de vérité** : étapes où l'on gagne ou perd la personne.
4. Prévoir l'adoption dès ici : valeur perçue en un écran, premier succès en quelques minutes, aide à la demande plutôt que tutoriel bloquant, états vides qui proposent l'action suivante (hypothèse de conception).
5. Chaque parcours cible devient au moins un workflow `WF-` (`workflows-fonctionnels.md`). Citer la fonction `FN-` quand elle existe, sinon l'exigence `EX-`.

## 4. Architecture de l'information

| Étape | Méthode | Sortie |
|---|---|---|
| Inventorier les contenus et fonctions | liste issue du cahier des charges et des parcours | inventaire |
| Regrouper | tri de cartes ouvert (grouper et nommer) | groupes candidats |
| Valider les libellés | test d'arborescence (trouver une cible dans le plan) | taux de réussite par tâche |
| Fixer la navigation | principale, secondaire, pied de page, recherche, fil d'Ariane | plan du site |
| Rattacher aux écrans | un écran `EC-` par feuille du plan | lien avec `ecrans.md` |

Règles : profondeur de trois niveaux au plus pour la navigation principale ; libellés dans le vocabulaire des utilisateurs relevé dans la voix du client, pas dans celui de l'organisation ; un contenu a une seule adresse canonique ; la navigation est identique sur tous les écrans (aide cohérente, WCAG 2.2 critère 3.2.6) ; prévoir la recherche quand le catalogue dépasse ce que le menu peut montrer. Décision « navigation principale » : type 2, à porter en panel.

## 5. Validation et niveau de preuve

Chaque test se consigne : date, méthode, nombre de participants, tâches, résultats, décisions. Sans test réalisé, écrire « hypothèse de conception » en tête de document. Les tests sur filaire coûtent peu et évitent de corriger en haute fidélité. Hypothèses culturelles : à valider auprès d'au moins 5 utilisateurs locaux avant de figer une direction (voir `contenu-localisation-culture.md`).

## 6. Gabarit de `personas-parcours.md`

````markdown
# Personas et parcours — <projet>

## Synthèse
<nombre de personas, de parcours, niveau de preuve global (preuve, indice, hypothèse), sources utilisées, ce qui reste à valider, exigences EX- sans persona>

## Méthode et sources
| Source | Date | Nature | Niveau de preuve |
|---|---|---|---|

## Personas
### PER-01 — <prénom fictif>, <rôle> (principal)
| | |
|---|---|
| Objectif | |
| Contexte d'usage | appareil, lieu, connexion, langue |
| Compétences numériques | |
| Freins et irritants | |
| Critère de réussite | mesurable |
| Exigences liées | EX-001, EX-004 |
| Niveau de preuve | |

## Parcours cibles
### PAR-01 — <intitulé> (persona PER-01)
| Étape | Action | Pensée ou émotion | Point de douleur | Opportunité |
|---|---|---|---|---|
Déclencheur, résultat, mesure de succès, workflow à produire (WF- à venir).

## Architecture de l'information
Plan du site (liste hiérarchique ou Mermaid), navigation principale, résultat des tests d'arborescence.

## Hypothèses et validations à mener
| Hypothèse | Comment la valider | Quand |
|---|---|---|
````

## 7. Pièges et contrôles avant de rendre

- Personas fictifs présentés comme issus d'une étude ; photos de personnes réelles ; stéréotypes de genre ou d'âge.
- Parcours limités au chemin heureux : ajouter échec de paiement, abandon, retour, interruption.
- Menu calqué sur l'organigramme de l'entreprise.
- Contrôles : chaque persona a une source et un niveau de preuve ; chaque parcours renvoie à un workflow à produire ; au moins un persona de bord ; l'utilisateur sait ce qui n'a pas été testé.

## Sources
- Voix du client : `01-decouverte/voix-du-client.md` du projet (avis sourcés et datés).
- WCAG 2.2, critère 3.2.6 Aide cohérente (W3C).
- Méthodes de tri de cartes et de test d'arborescence : bonne pratique, source primaire à citer par le projet.
