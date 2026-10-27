# Spécifications fonctionnelles générales (SFG)

La SFG décrit le produit vu de l'extérieur : qui l'utilise, quelles fonctions il offre, quels processus et quels objets métier il manipule. Elle est la charpente : elle découpe le produit en modules, fixe les identifiants `FN-` et prépare l'essaim de la SFD. Elle ne contient ni règle de calcul détaillée, ni écran, ni technologie.

## Sommaire
1. Méthode
2. Granularité d'une fonction
3. Gabarit
4. Pièges fréquents
5. Contrôles avant de rendre
6. Sources

## 1. Méthode

1. **Lire** le cahier des charges, les personas, les workflows en cours. Dresser la liste des `EX-` et `EXNF-` à couvrir : la SFG doit les épuiser.
2. **Lister les acteurs** : utilisateurs par rôle, administrateurs, systèmes externes, tâches planifiées. Un acteur système est un acteur à part entière : il déclenche des fonctions (import nocturne, relance automatique).
3. **Découper en modules** cohérents (un module = un domaine métier = un propriétaire = une SFD). Prévoir le module `commun` (comptes, droits, notifications, consentement, journal d'audit, paramétrage, administration). Attribuer une **plage de `RG-`** à chaque module (cent par module) : c'est ce qui permet l'essaim sans collision.
4. **Dériver les fonctions** par acteur et par objectif, puis par objet métier avec la matrice objets × fonctions (section 3) : un objet sans création, sans fin de vie ou sans consultation révèle une fonction oubliée.
5. **Décrire les processus** de bout en bout (commande, onboarding, remboursement, clôture), chacun cité par les fonctions qu'il traverse. Le détail pas à pas des écrans revient au `cartographe-interactions` (workflows `WF-`).
6. **Décrire les objets métier** : définition, attributs principaux, cycle de vie (états et transitions), propriétaire, durée de conservation à proposer au `delegue-protection-donnees`.
7. **Lister les interfaces externes** (nom, sens, finalité, données) : le détail est dans les spécifications techniques.
8. **Écrire la matrice de droits** acteur × fonction. Les règles fines vont en SFD.
9. **Tracer** : chaque `FN-` cite sur sa ligne les `EX-` qu'elle couvre ; chaque `EX-` doit être couverte au moins une fois. Poser les questions ouvertes.

## 2. Granularité d'une fonction

| Test | Verdict |
|---|---|
| Un acteur peut l'accomplir en une intention avec un résultat observable | bonne taille |
| Elle se décrit en 3 à 15 règles de gestion | bonne taille |
| Elle cumule plusieurs acteurs ou plusieurs objets sans lien | trop grosse : scinder |
| Elle se réduit à une seule règle ou à un champ | trop fine : la fondre dans la fonction voisine |
| Son intitulé contient « gérer » | trop vague : « créer, modifier, annuler… » |

Nommer par verbe + objet : « Annuler une commande », pas « Gestion des commandes ».

## 3. Gabarit

````markdown
# Spécifications fonctionnelles générales — <nom du projet>

## Synthèse
<Nombre de modules, de fonctions, d'acteurs, d'objets métier ; EX- non couvertes (doit être zéro) ;
 plages de RG- par module ; questions ouvertes ; résultat de `cortex.py tracabilite verifier`.>

## 1. Modules et plages d'identifiants
| Module | Périmètre | Plage de RG- | Propriétaire de SFD |
|---|---|---|---|
| commun | comptes, droits, notifications, journal | RG-001 à RG-099 | |
| commande | panier, paiement, suivi | RG-100 à RG-199 | |

## 2. Acteurs
| Acteur | Type | Description | Objectifs |
|---|---|---|---|

## 3. Glossaire
| Terme | Définition | Synonymes interdits |
|---|---|---|

## 4. Fonctions
| ID | Intitulé | Module | Acteurs | Description | Exigences couvertes | Priorité |
|---|---|---|---|---|---|---|
| FN-001 | Créer un compte | commun | visiteur | Le visiteur crée un compte client à partir de son e-mail | EX-001, EX-002 | Must |

## 5. Processus
| Processus | Déclencheur | Fonctions traversées | Résultat |
|---|---|---|---|
| Commande | clic sur « Commander » | FN-010, FN-011, FN-012 | commande confirmée |

## 6. Objets métier
### Commande
| Attribut | Description | Obligatoire | Donnée personnelle |
|---|---|---|---|
États : brouillon → payée → expédiée → livrée ; annulée possible avant expédition.
Conservation : à proposer (durée et base légale à valider par le juriste).

### Matrice objets × fonctions
| Objet | Créer | Consulter | Modifier | Supprimer ou archiver |
|---|---|---|---|---|
| Commande | FN-010 | FN-014 | FN-015 | FN-016 |

## 7. Droits
| Fonction | Visiteur | Client | Gestionnaire | Administrateur |
|---|---|---|---|---|
| FN-001 | oui | non | non | non |

## 8. Interfaces externes
| Interface | Système | Sens | Finalité | Données | Fonctions |
|---|---|---|---|---|---|

## 9. Règles et contraintes transverses
<Renvois aux EXNF- ; règles valables partout ; langue, fuseau, devise.>

## 10. Matrice de traçabilité
| Exigence | Fonctions | Règles de gestion | Workflows | Cas de test |
|---|---|---|---|---|
| EX-001 | FN-001 | | | |

## 11. Questions ouvertes
````

La matrice (section 10) est une vue : la créer à la fin de la SFG avec les colonnes amont, la compléter après la SFD et le cahier de recette. Vérifier qu'elle reste en accord avec les lignes sources (voir `tracabilite.md`).

## 4. Pièges fréquents

- Un copier-coller du cahier des charges sous un autre titre : la SFG apporte la structure, pas des phrases recyclées.
- Fonctions oubliées : administration, export, suppression de compte, relance automatique, reprise après erreur, consultation de l'historique.
- Acteurs systèmes absents, donc interfaces sans fonction.
- Plages de `RG-` non attribuées : l'essaim produit des doublons.
- Objets métier sans cycle de vie : les transitions interdites ne seront écrites nulle part.
- Détails d'écran ou choix techniques glissés dans la description.
- Cas d'usage rédigés comme des récits utilisateurs : garder la fonction, citer le récit en source si nécessaire.

## 5. Contrôles avant de rendre

- Toute `EX-` est citée sur au moins une ligne `FN-`.
- Toute `FN-` a un module, au moins un acteur et ses droits.
- Chaque module a une plage de `RG-`, un propriétaire et au plus 15 fonctions.
- Chaque objet métier a un cycle de vie et un propriétaire.
- Chaque interface externe est rattachée à au moins une fonction.
- `cortex.py tracabilite verifier` ne signale aucune exigence sans fonction.

## Sources

- Cahier des charges fonctionnel et chaîne MOA–MOE : JDN, « Les dossiers techniques en gestion de projet informatique ».
- CREDAF (2019) : rôles MOA, MOE, métiers, validation de la conception fonctionnelle par les métiers.
- HERMES (2022, 3e tirage 31.12.2025) : livrables Concept, solution requirements.
- ISO/IEC/IEEE 29148:2018 : traçabilité entre exigences et spécifications.
- Plan type de la SFG : aucune norme lue ; ce gabarit est une convention de pratique à adapter au contrat (à vérifier).
