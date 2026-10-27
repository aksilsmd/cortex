# Spécifications fonctionnelles détaillées (SFD)

La SFD décrit, module par module, le comportement exact du produit : règles de gestion, cas nominaux et d'exception, données, messages, droits. Un développeur la lit sans rien deviner ; un testeur en tire ses cas sans poser de question. Elle est écrite en essaim : **un fichier par module, qui se suffit à lui-même.**

## Sommaire
1. Méthode
2. Écrire une règle de gestion
3. Autoportance du module
4. Gabarit
5. Pièges fréquents
6. Contrôles avant de rendre
7. Sources

## 1. Méthode

1. **Lire** la SFG : les fonctions `FN-` du module, les acteurs, les objets métier et leur cycle de vie, le glossaire, les droits. Lire seulement les `EX-` citées par ces fonctions.
2. **Pour chaque fonction**, écrire le cas nominal en étapes, puis chercher les déviations avec les cinq questions : donnée absente ou invalide ? droit insuffisant ? système ou tiers indisponible ? abandon ou retour arrière ? double action ou action concurrente ?
3. **Extraire les règles** : chaque décision, calcul, contrôle, changement d'état, notification devient une `RG-` numérotée dans la plage du module.
4. **Donner un exemple** par règle : valeurs d'entrée, résultat attendu. Pour un calcul, au moins un exemple chiffré avec arrondi, et un cas limite.
5. **Compléter** données (champs, formats), messages exacts, droits, paramétrage (valeurs modifiables sans livraison, et par qui).
6. **Se coordonner** avec le `cartographe-interactions` : chaque règle a son écran, chaque écran ses règles. Une décision d'interface sans règle est une règle manquante ; une règle sans écran, un écran manquant.
7. **Se faire relire** par le testeur : une règle qu'il ne sait pas tester est mal écrite.

## 2. Écrire une règle de gestion

| Exigence de forme | Exemple |
|---|---|
| Une règle = une condition, un effet | « Si le total du panier dépasse 500 €, alors le paiement par virement est proposé en plus de la carte » |
| Valeurs, unités, bornes incluses ou non, arrondi | « de 18 ans révolus ; arrondi au centime supérieur » |
| Sujet explicite : qui, quoi, quand | « Le système refuse… », « Le gestionnaire peut… » |
| Ordre d'évaluation et priorité si plusieurs règles s'appliquent | « RG-104 prime sur RG-102 » |
| Temporalité : fuseau, heure d'effet, durée | « à 23 h 59 heure de Paris » |
| Pas de renvoi flou : citer l'identifiant | « selon RG-110 », non « comme vu plus haut » |

Types à penser : contrôle de saisie, calcul, état et transition, droit d'accès, déclenchement automatique, notification, audit, conservation et purge, idempotence (un double envoi ne duplique rien).

Mots interdits sans valeur : « rapidement », « automatiquement » (préciser quand et par quoi), « le cas échéant », « etc. », « approprié », « raisonnable ».

Correspondance agile : la règle plus son exemple équivaut à une règle Gherkin avec ses exemples ; le `concepteur-tests` en tire les `CT-`. Écrire l'exemple en « Étant donné / Quand / Alors », trois à cinq étapes.

## 3. Autoportance du module

Le fichier doit se lire seul. Il contient donc : l'extrait de la SFG utile (acteurs, objets, glossaire du module), la liste de ses fonctions avec leurs exigences, ses plages d'identifiants, et ses **dépendances** (ce qu'il attend des autres modules, citées par `FN-` ou `RG-`). Il ne redéfinit jamais une règle d'un autre module : il la cite. Si une règle manque chez un voisin, l'écrire en question ouverte adressée à son propriétaire.

## 4. Gabarit

````markdown
# SFD — module <nom>

## Synthèse
<Fonctions couvertes ; nombre de RG- ; plage utilisée ; cas d'exception traités ; questions ouvertes ;
 règles demandées à d'autres modules ; résultat du script de traçabilité.>

## 1. Contexte du module
| Élément | Contenu |
|---|---|
| Plage de RG- | RG-100 à RG-199 |
| Fonctions | FN-010, FN-011, FN-012 (copier l'intitulé de chacune) |
| Acteurs et rôles | extrait de la SFG |
| Objets métier et états | extrait de la SFG |
| Termes du glossaire | |
| Dépendances (ce que le module attend d'autres modules) | FN-0xx, RG-0xx du module commun |

## 2. Règles de gestion
| ID | Fonction | Type | Règle | Exemple | Priorité |
|---|---|---|---|---|---|
| RG-101 | FN-010 | contrôle | Si la quantité saisie dépasse le stock disponible, alors le système refuse l'ajout et affiche MSG-101-01 | stock 3, quantité 4 : refus ; quantité 3 : accepté | Must |

## 3. Cas par fonction
### FN-010 — <intitulé>
**Nominal.** 1. … 2. … (une action par étape, avec la règle appliquée : RG-101).

| Cas | Règle | Étant donné | Quand | Alors |
|---|---|---|---|---|
| Exception : stock insuffisant | RG-101 | un article au stock de 3 | le client demande 4 | refus, MSG-101-01, panier inchangé |

## 4. Données
| Champ | Objet | Type | Obligatoire | Format, longueur, valeurs | Règle | Donnée personnelle |
|---|---|---|---|---|---|---|

## 5. Messages
| Code | Déclencheur | Texte exact | Nature | Règle |
|---|---|---|---|---|
| MSG-101-01 | refus de stock | « Il ne reste que {n} exemplaire(s). » | erreur | RG-101 |

## 6. Droits
| Fonction | Rôle | Autorisé | Condition (propriétaire de la ressource, état de l'objet…) | Règle |
|---|---|---|---|---|

## 7. Paramétrage
| Paramètre | Valeur initiale | Modifiable par | Effet | Règle |
|---|---|---|---|---|

## 8. Questions ouvertes et règles demandées
````

Les codes `MSG-`, `CAS-` et autres étiquettes locales ne sont pas tracés par le script ; seuls `EX-`, `EXNF-`, `FN-`, `RG-`, `WF-`, `CT-` le sont. **L'ID `RG-` est en première colonne, la fonction sur la même ligne.**

## 5. Pièges fréquents

- Le cas nominal seul : les exceptions sont écrites « par le développeur ».
- Une règle qui contient deux conditions et trois effets : à scinder.
- Messages d'erreur génériques (« Une erreur est survenue ») au lieu d'un texte exact par cause et d'une action possible.
- Rôles et droits dits « selon profil » sans tableau.
- Valeurs en dur dans le texte alors qu'elles devraient être paramétrables (taux, durées, seuils).
- Oublier concurrence et reprise : deux validations simultanées, expiration en cours de saisie.
- Données personnelles dans les champs sans signalement : le `delegue-protection-donnees` ne peut pas relire.
- Règle qui renvoie à un écran : elle décrit le comportement, l'écran la présente.

## 6. Contrôles avant de rendre

- Chaque `FN-` du module a au moins une `RG-` ou un `WF-`, un cas nominal et au moins une exception.
- Chaque `RG-` est dans la plage du module, cite sa fonction, porte un exemple.
- Chaque erreur possible a un message exact ; chaque rôle a une ligne de droits.
- Aucun terme interdit sans valeur ; aucune règle dupliquée d'un autre module.
- `cortex.py tracabilite verifier` : aucune fonction sans règle ni workflow dans ce module.

## Sources

- JDN, « Les dossiers techniques en gestion de projet informatique ».
- Cucumber, Gherkin Reference (Rule depuis Gherkin 6, 2018) ; « Gherkin Rules ».
- HERMES (2022, 3e tirage 31.12.2025) : « Detailed specifications » dans la phase Implementation.
- ISO/IEC/IEEE 29148:2018 : qualité des énoncés de besoin et traçabilité.
- Plan type de la SFD : non sourcé par une norme ; convention de pratique à adapter au contrat (à vérifier).
