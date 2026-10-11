# Traçabilité

La traçabilité relie chaque exigence à ce qui la réalise et à ce qui la prouve. Elle est vérifiée par `cortex.py tracabilite verifier` : le script lit les documents tels qu'ils sont écrits, donc le format des tableaux compte autant que leur contenu.

## Sommaire
1. La chaîne
2. Ce que lit le script
3. Matrice de traçabilité
4. Erreurs fréquentes
5. Faire évoluer sans casser
6. Contrôles avant de rendre
7. Sources

## 1. La chaîne

| Étage | Défini par | Défini dans | Cité par (même ligne ou même section) | Erreur si absent |
|---|---|---|---|---|
| `EX-` | `expert-cahier-des-charges` | `02-cadrage/cahier-des-charges.md` | une `FN-`, une `RG-` ou un `WF-` | erreur : exigence sans fonction |
| `EXNF-` | `expert-cahier-des-charges` | idem | un `CT-` | **alerte** seulement |
| `FN-` | `redacteur-sfg` | `03-conception/specifications/sfg.md` | une `RG-` ou un `WF-` | erreur |
| `RG-` | `redacteur-sfd`, `redacteur-specs-techniques` | `sfd/<module>.md`, `specs-techniques.md` | un `CT-` | erreur |
| `WF-` | `cartographe-interactions` | `design/workflows/<module>.md` | un `CT-` | erreur |
| `CT-` | `concepteur-tests` | `03-conception/tests/cahier-de-recette.md` | | |

Un étage n'est contrôlé que lorsque l'étage aval existe : tant qu'aucune `FN-` n'est écrite, l'absence de fonction pour une `EX-` n'est pas signalée. Ne pas en conclure que tout va bien ; relancer le script après chaque livrable.

Tout identifiant cité mais jamais défini est une erreur (« identifiant fantôme »).

## 2. Ce que lit le script

| Règle | Conséquence pratique |
|---|---|
| Un identifiant est **défini** quand il est exactement la première cellule d'une ligne de tableau, ou quand un titre `#` commence par lui | pas de gras, pas d'apostrophes inverses, pas de lien, pas de texte avant l'identifiant : `RG-101` seul dans la cellule ; titre `### FN-010 — Annuler` valable, `### Fonction FN-010` non |
| Un identifiant est **relié** aux identifiants cités sur sa ligne de tableau | l'amont se cite sur la ligne de l'aval : colonne « Exigences couvertes » d'une `FN-`, colonne « Fonction » d'une `RG-` |
| Un identifiant défini par un titre est relié à tous ceux cités dans sa section, jusqu'au titre suivant de niveau égal ou supérieur | une section `### FN-010` avec ses tableaux relie la fonction à toutes les règles citées dedans |
| Format reconnu : `EX`, `EXNF`, `FN`, `RG`, `WF`, `CT`, un tiret, trois ou quatre chiffres | `RG-01` n'existe pas pour le script ; `RG-0101` oui |
| Fichiers lus : sous `02-`, `03-`, `05-` du dossier projet | une exigence citée uniquement dans `04-realisation/` est ignorée |
| Tout le texte est lu, **blocs de code compris** | un identifiant d'exemple laissé dans le document devient un vrai identifiant |

Les doublons ne sont pas détectés : si `RG-101` est défini deux fois, la seconde définition est ignorée en silence. Les chercher dans les seuls tableaux de définition (la matrice et le tableau de droits répètent légitimement des `EX-` et des `FN-`) :

```
grep -hoE "^\| (EX|EXNF)-[0-9]+" 02-cadrage/cahier-des-charges.md | sort | uniq -d
grep -hoE "^\| FN-[0-9]+" 03-conception/specifications/sfg.md | sort | uniq -d
grep -rhoE "^\| RG-[0-9]+" 03-conception/specifications | sort | uniq -d
```

Le premier et le troisième ne doivent rien renvoyer ; pour le deuxième, ignorer les `FN-` du tableau de droits.

## 3. Matrice de traçabilité

La matrice est une vue, pas une source : elle se génère à partir des lignes sources, à la fin de la SFG puis après la recette. Elle vit dans `sfg.md`, section « Matrice de traçabilité ».

````markdown
## 10. Matrice de traçabilité
| Exigence | Fonctions | Règles de gestion | Workflows | Cas de test |
|---|---|---|---|---|
| EX-001 | FN-001 | RG-001, RG-002 | WF-001 | CT-001, CT-002 |
| EXNF-004 | FN-021 | RG-901 | | CT-040 |
````

Elle ne peut pas masquer un trou : le script ne la compte pas comme couverture (une ligne dont la tête est amont ne couvre rien). Mais elle devient fausse si une ligne source change : la régénérer avant de rendre, jamais la corriger à la main seule. Colonnes vides = manque visible ; les écrire telles quelles.

Pour le jalon J5, le PV de recette cite les `CT-` exécutés : la chaîne se prolonge jusqu'à la preuve.

## 4. Erreurs fréquentes

| Symptôme du script | Cause probable | Correction |
|---|---|---|
| exigence sans fonction | `EX-` jamais citée dans « Exigences couvertes » ; identifiant mal tapé ; cellule avec gras | citer sur la ligne `FN-` ; sinon créer la fonction ; si l'exigence est écartée, la retirer du tableau et la porter aux exclusions |
| fonction sans règle ni workflow | SFD du module absente ou règles sans colonne « Fonction » | citer la `FN-` sur chaque ligne `RG-`, ou créer le workflow |
| règle sans cas de test | cahier de recette pas encore écrit, ou `CT-` qui cite une plage « RG-101 à RG-110 » | citer chaque `RG-` nommément, jamais en plage |
| identifiant cité jamais défini | faute de frappe, exigence supprimée mais encore citée, identifiant d'exemple du gabarit laissé | corriger ou supprimer la citation |
| `EXNF-` sans cas de test (alerte) | exigence jamais testée | demander un `CT-` au `concepteur-tests` ou revoir la vérifiabilité |

Autres pièges : ancienne exigence retirée mais citée dans un commentaire de la forme « ex-EX-014 », lue comme une référence (écrire « ancienne exigence 14 ») ; exclusions numérotées `EX-` (les numéroter `X-01`) ; règle portée par un tableau dont la première colonne est un libellé et non l'identifiant.

## 5. Faire évoluer sans casser

- Un identifiant n'est jamais réutilisé ni renuméroté, même après suppression : les trous sont acceptables.
- Un changement d'exigence après J2 passe par une décision au registre ; l'expert met à jour dans l'ordre amont → aval, puis relance le script.
- La suppression d'une `EX-` impose de retirer ses citations et de vérifier que les `FN-` qui ne servaient qu'elle sont retirées ou rattachées.
- Un essaim de SFD fusionne sans conflit si chaque instance reste dans sa plage ; le chef d'orchestre vérifie les doublons après la vague.

## 6. Contrôles avant de rendre

- Le script s'exécute sans erreur : `python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/cortex.py tracabilite verifier --dossier <dossier projet>`.
- Les commandes de recherche de doublons ne renvoient rien d'anormal.
- Chaque alerte est traitée ou expliquée dans la synthèse.
- Aucun identifiant d'exemple de gabarit ne subsiste.

## Sources

- `cortex.py`, fonction `analyser_tracabilite` : règles de lecture ci-dessus (état du plugin à la rédaction).
- ISO/IEC/IEEE 29148:2018 : traçabilité des exigences ; 3e édition en DIS (14/09/2026).
- Chaîne documentaire : exigence → règle ou exemple Gherkin → test → PV (inférence à valider).
- Cucumber, Gherkin Reference : l'exemple sert de spécification et de test.
- CCAG-TIC 2021, art. 32 et 33 : VA, VSR et décision d'admission.
