# Cahier des charges

Le cahier des charges exprime le besoin en exigences vérifiables, priorisées et identifiées. Dans la pratique française c'est le cahier des charges fonctionnel (CdCF), contrat entre la MOA et la MOE. Il dit quoi et pourquoi, jamais comment.

## Sommaire
1. Méthode d'expression du besoin
2. Écrire une exigence vérifiable
3. Priorisation
4. Correspondances avec la pratique agile
5. Gabarit
6. Pièges fréquents
7. Contrôles avant de rendre
8. Sources

## 1. Méthode d'expression du besoin

1. **Collecter** à partir des livrables amont (note d'opportunité, voix du client, personas, analyse du contexte, pré-diagnostic juridique). Chaque exigence cite sa source ; sans source, c'est une hypothèse.
2. **Identifier les acteurs** et leurs objectifs : un objectif d'acteur donne une ou plusieurs exigences.
3. **Dire le besoin sans solution** : « permettre à un client de retrouver une commande » et non « ajouter un champ de recherche ». Une solution imposée n'entre que comme **contrainte** justifiée (existant, réglementation, standard de l'entreprise).
4. **Parcourir les thèmes à ne pas oublier** : comptes et droits, données personnelles, historique et audit, notifications, import et export, administration et paramétrage, multilingue, accessibilité, reprise de données, fin de vie (clôture de compte, archivage), support.
5. **Rédiger** chaque exigence (section 2), puis ses critères d'acceptation.
6. **Prioriser** (section 3) avec la MOA ; tout ce qui est « Won't » en V1 va au tableau des exclusions.
7. **Faire relire** : testabilité, faisabilité, conformité, coût (revues croisées).

## 2. Écrire une exigence vérifiable

Caractéristiques d'un bon énoncé selon ISO/IEC/IEEE 29148:2018 (clause à vérifier) : nécessaire, non ambiguë, complète, singulière, réalisable, vérifiable, correcte, conforme. Application :

| Règle | Mauvais | Bon |
|---|---|---|
| Un seul verbe, un seul sujet | « Le système gère et archive les commandes » | deux exigences |
| « Doit » pour l'obligatoire, « devrait » pour le souhaitable, jamais « peut » | « Le système peut envoyer un e-mail » | « Le système doit envoyer un e-mail de confirmation » |
| Un seuil et une méthode pour tout adjectif | « Réponse rapide » | « 95 % des recherches répondent en moins de 800 ms sous 200 utilisateurs simultanés, mesuré par test de charge » |
| Pas de formules vagues : « etc. », « notamment », « si possible », « adapté », « convivial » | « paiements par carte, etc. » | liste fermée des moyens de paiement |
| Sujet actif : qui fait quoi | « Les droits sont vérifiés » | « Le système doit refuser l'export à tout utilisateur sans le rôle Gestionnaire » |

Syntaxe contrôlée recommandée (EARS, Mavin et al.) : « Quand <événement>, le système doit <réponse> » ; « Tant que <état>, le système doit … » ; « Si <condition indésirable>, alors le système doit … ».

**Le critère d'acceptation** termine la ligne. Il décrit l'observation qui prouve la satisfaction : état initial, action, résultat mesurable. Écrire en « Étant donné / Quand / Alors » dès que l'exigence a un comportement ; avec une valeur et une méthode quand elle est chiffrée. Pas de pipe `|` dans une cellule. Trois à cinq étapes au plus (repère Gherkin) ; au-delà, l'exigence est trop grosse.

## 3. Priorisation

| Méthode | Quand | Précaution |
|---|---|---|
| MoSCoW (Must, Should, Could, Won't) | par défaut | Must ≤ 60 % du périmètre V1, sinon tout est prioritaire et rien ne l'est |
| Valeur × coût (échelles 1 à 5) | arbitrer entre Should et Could | coût donné par le `controleur-financier` ou l'`architecte-solution`, pas deviné |
| Kano | produit grand public, différenciation | à compléter par la voix du client |

Une priorité se justifie en une phrase (obligation légale, revenu, risque, engagement contractuel). Un Must sans justification est rétrogradé en Should jusqu'à preuve.

## 4. Correspondances avec la pratique agile

| Pratique française | Pratique agile | Dans Dan-Cortex |
|---|---|---|
| Exigence fonctionnelle | récit utilisateur (« En tant que… je veux… afin de… ») | ligne `EX-` ; le récit peut figurer en colonne « Exigence » |
| Critère de recette | critères d'acceptation | colonne finale |
| Lot ou module | epic, feature | module de SFD |
| Cas de recette VABF | scénario Gherkin | `CT-` du cahier de recette |
| Réserve de recette | anomalie | registre des anomalies |

Un récit utilisateur est un artefact de planification transitoire : l'exigence, elle, est durable et tracée. Vérifier INVEST (indépendant, négociable, valuable, estimable, small, testable) avant de reprendre un récit.

## 5. Gabarit

````markdown
# Cahier des charges — <nom du projet>

## Synthèse
<Périmètre V1 ; nombre d'EX- par priorité ; nombre d'EXNF- ; hypothèses ; questions ouvertes ;
 exigences à valider par un juriste ; décisions attendues.>

## 1. Contexte et objectifs
<Renvoi à la note de cadrage ; objectifs repris, pas réécrits.>

## 2. Acteurs
| Acteur | Description | Objectifs |
|---|---|---|

## 3. Exigences fonctionnelles
| ID | Intitulé | Exigence | Source | Priorité | Critère d'acceptation |
|---|---|---|---|---|---|
| EX-001 | Connexion | Le système doit permettre à un client enregistré de se connecter par e-mail et mot de passe | persona P1 ; voix du client | Must | Étant donné un compte actif, quand le client saisit des identifiants valides, alors il accède à son espace en moins de 3 secondes (95e centile) |

## 4. Exigences non fonctionnelles
| ID | Caractéristique ISO/IEC 25010:2023 | Exigence | Source | Priorité | Métrique, seuil, conditions et méthode | Critère d'acceptation |
|---|---|---|---|---|---|---|
| EXNF-001 | Performance efficiency | Les pages de catalogue doivent s'afficher rapidement | benchmark | Must | LCP au 75e centile, mobile 4G | LCP inférieur à 2,5 s sur 95 % des mesures du test de charge à 500 utilisateurs |

## 5. Contraintes
| ID | Contrainte | Origine | Justification |
|---|---|---|---|
| CONT-01 | Hébergement dans l'UE | RGPD, politique interne | à valider par le juriste |

## 6. Exclusions et reports
| Réf. | Élément | Décision | Condition de reprise |
|---|---|---|---|
| X-01 | Application mobile native | Won't en V1 | succès de la V1 |

## 7. Recette
<Conditions de VABF (environnement, données de test), de VSR (production, durée d'observation), critères d'admission.>

## 8. Hypothèses et questions ouvertes
## 9. Glossaire
````

Les exclusions n'ont pas d'identifiant `EX-` : une `EX-` sans fonction en aval fait échouer le script.

## 6. Pièges fréquents

- Exigence-solution (« utiliser telle base de données ») sans contrainte justifiée.
- Adjectif sans seuil ; seuil sans méthode de mesure.
- Critère d'acceptation qui répète l'exigence au lieu de la prouver.
- Tout en Must ; priorités jamais arbitrées avec le coût.
- Exigences réglementaires oubliées (consentement, accessibilité, conservation) ou non marquées « à valider ».
- Exigences d'administration, d'audit, d'export et de fin de vie absentes parce qu'aucun utilisateur ne les demande.
- Mélanger plusieurs objets dans une ligne : le test d'une moitié bloque l'autre.

## 7. Contrôles avant de rendre

- Chaque `EX-` et `EXNF-` a une source, une priorité justifiée et un critère d'acceptation mesurable.
- Aucun terme de la liste interdite sans seuil : rapide, ergonomique, sécurisé, intuitif, robuste, simple, convivial, performant, standard.
- Les thèmes de la méthode (étape 4) sont couverts ou écartés avec motif.
- Les exigences réglementaires sont marquées « à valider ».
- Les identifiants sont uniques et sans trou inutile ; les exclusions sont hors `EX-`.

## Sources

- NF EN 16271 (AFNOR, février 2013) : expression fonctionnelle du besoin et cahier des charges fonctionnel ; remplace NF X50-151.
- ISO/IEC/IEEE 29148:2018 ; 3e édition au stade DIS depuis le 14/09/2026 (état : octobre 2026).
- ISO/IEC 25010:2023, publiée le 15/11/2023.
- Cucumber, Gherkin Reference et « Gherkin Rules » (cucumber.io/docs/gherkin/reference/).
- JDN, « Les dossiers techniques en gestion de projet informatique ».
- Mavin et al., EARS (2009) : référence à vérifier avant citation formelle.
