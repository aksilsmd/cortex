# Essai à blanc du 11 octobre 2026

Un essai en conditions réelles, sans intervention humaine en cours de route, pour vérifier que le plugin fait
bien ce qu'il annonce. Il ne couvre que le jalon J1 en mode `eclair` : c'est un essai, pas une évaluation.

## Demande soumise

> /dan-cortex:lancer-projet Je veux lancer un petit SaaS de prise de rendez-vous en ligne pour les toiletteurs
> canins indépendants, en France. J'ai 5 000 € et trois mois devant moi. Pour l'instant je veux seulement savoir
> si ça vaut le coup : étude d'opportunité (jalon J1), en mode éclair. Ne me pose pas de questions, pose tes
> hypothèses et avance.

Session sans interface, plugin chargé depuis son dossier, modèle intermédiaire pour le chef d'orchestre.

## Ce que le chef d'orchestre a fait

1. Il a chargé le skill `lancer-projet` et lu les seules références utiles : profil SaaS, section J1, format des
   ordres de mission, fusion des rôles en mode éclair.
2. Il a créé le dossier projet avec le script (`init`, types `saas` et `niche`), rempli la fiche projet et posé
   ses hypothèses par écrit.
3. Il a lancé une première vague de trois agents Dan-Cortex en parallèle, en arrière-plan, puis une seconde vague de
   deux agents qui dépendaient de la première.
4. Il a journalisé chaque agent, traité les 12 contrôles de couverture du jalon, vérifié le jalon par script et
   généré le tableau de bord.
5. Il a rendu compte : recommandation, trois options chiffrées, et la décision laissée à l'utilisateur.

## Agents lancés

| Vague | Agent | Mission | Contexte final | Appels d'outils | Durée |
|---|---|---|---|---|---|
| 1 | `dan-cortex:analyste-concurrence` | marché, concurrence, pré-diagnostic juridique (rôles fusionnés) | 81 879 tokens | 46 | 4 min 04 |
| 1 | `dan-cortex:architecte-solution` | faisabilité technique, acheter ou construire | 40 361 tokens | 26 | 1 min 54 |
| 1 | `dan-cortex:controleur-financier` | ordres de grandeur financiers | 22 356 tokens | 7 | 48 s |
| 2 | `dan-cortex:stratege-produit` | note d'opportunité | 55 689 tokens | 11 | 2 min 20 |
| 2 | `dan-cortex:contradicteur` | pré-mortem | 30 667 tokens | 7 | 29 s |

À titre de comparaison, les agents de recherche généralistes utilisés pour préparer ce plugin finissaient entre
220 000 et 340 000 tokens de contexte.

## Livrables produits

Neuf documents dans `01-decouverte/` (étude de marché, benchmark concurrentiel, analyse de contexte,
pré-diagnostic juridique, note de faisabilité technique, ordres de grandeur financiers, pré-mortem, note
d'opportunité, registre des sources), plus la fiche projet, l'organigramme, le journal des agents, la matrice de
couverture et le tableau de bord.

## Résultat

- Jalon J1 déclaré franchissable par le script : documents présents, 12 contrôles traités.
- Recommandation rendue : ne pas construire tout de suite, tester d'abord la demande sans code ; douze
  alternatives recensées, dont trois déjà spécialisées ; projet jugé « fragile » par le pré-mortem.
- Le chef d'orchestre a lui-même signalé que la confiance dans les preuves était faible et que la décision
  revenait à l'utilisateur.

## Coût

2,44 $ en équivalent API pour l'ensemble de la session (chef d'orchestre et cinq agents), en une dizaine de
minutes.

## Ce que l'essai a révélé

- Le chef d'orchestre a consulté l'aide du script avant de l'appeler : la commande d'aide est désormais citée
  dans le skill.
- Le journal attribuait les agents au jalon J0 parce que le jalon courant n'avait pas été avancé avant la
  vague : le skill demande maintenant de noter jalon et vague avant chaque lancement.

## Ce que l'essai ne prouve pas

Un seul scénario, un seul mode, un seul jalon, sans comparaison avec une session sans plugin. Les jalons J2 à J7
sont validés en structure, pas sur un projet complet.
