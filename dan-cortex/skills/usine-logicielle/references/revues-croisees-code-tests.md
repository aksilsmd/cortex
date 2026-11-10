# Revues croisées du code et des tests, règles des tests unitaires

Trois règles obligatoires dans chaque lot, quel que soit le mode. Elles complètent `boucle-build-test.md` et
`revue-multi-angles.md`. Contrôles : TST-041 à TST-045, DEV-029 et DEV-030.

## Sommaire
1. Revue de code croisée · 2. Tests unitaires · 3. Revue croisée des cas de test · 4. Qui relit qui ·
5. Ce qui bloque une fusion

## 1. Revue de code croisée
- **Personne ne valide son propre travail.** Le code d'un développeur est relu par un `relecteur-code` qui ne
  l'a pas écrit, avec un contexte neuf (la fiche du lot, les RG-, la différence ; pas l'historique du développeur).
- **Le chef d'orchestre ne se substitue jamais au relecteur.** Il peut constater, il ne peut pas déclarer
  « FUSIONNABLE ».
- **Le correctif est relu par le même relecteur** (ou un second relecteur indépendant), jamais par l'auteur ni
  par le chef d'orchestre. Un « CORRECTIF REQUIS » se lève par un nouveau verdict écrit.
- **Contre-relecture** pour les lots à risque (sécurité, argent, droits, données personnelles, migrations) : un
  second relecteur d'un autre métier (`auditeur-securite`, `architecte-donnees`) relit le même hash.
- **Relecture par mutation** : le relecteur casse volontairement le code relu (dans une copie hors du dépôt) et
  vérifie que les tests rougissent. Un test qui reste vert sous mutation est un constat.
- **Hash gelé** : le verdict porte le hash relu ; la fusion se fait sur ce hash (ou un arbre identique), sinon
  nouvelle relecture de la différence.
- **Sur une IA sans sous-agents** : relire après une coupure nette, en changeant de rôle (« Relecteur : … »),
  avec la liste de contrôle ci-dessous, et le dire dans le rapport : la revue est moins indépendante.
- Liste de contrôle minimale : règle contre code ; tests qui prouvent le comportement ; échecs silencieux ;
  failles évidentes ; périmètre des fichiers ; lisibilité pour un humain qui reprend (`architecture-normes/references/reprise-humaine.md`).

## 2. Tests unitaires
1. **Écrits avant le code et constatés rouges** ; la sortie rouge est enregistrée au journal du lot avant le
   premier commit de code.
2. **Un test vert d'emblée ne compte pas** tant qu'un **témoin** ne l'a pas fait échouer (mutation du code ou
   donnée qui viole la règle), témoin noté au journal.
3. **Chaque règle de gestion a au moins un test nominal et un test d'exception**, nommés par le comportement et
   citant la RG- (`refuse une commande d'un pro non validé (RG-0712)`).
4. **Isolés et déterministes** : pas de réseau, pas d'horloge réelle, pas d'ordre d'exécution, pas de donnée
   réelle ; un test instable est une anomalie, pas un « relancer ».
5. **Assertions sur le résultat observable**, pas sur l'implémentation ; une assertion ne s'affaiblit pas pour
   passer (changement justifié par écrit et relu).
6. **Seuils** : couverture de lignes et de branches du code nouveau fixée dans les normes ; score de mutation sur
   les modules critiques ; mesurés par outil, pas déclarés.
7. **Lisibles par un humain** : structure préparer / agir / vérifier, données d'exemple nommées, un
   comportement par test.

## 3. Revue croisée des cas de test
- Les **cas de test** (CT-) d'un lot sont écrits par `concepteur-tests` **avant le code**, à partir des RG- et des
  critères d'acceptation.
- Ils sont **relus par un autre métier** avant la porte 2 :
  - `redacteur-sfd` (ou l'expert du domaine) vérifie que chaque RG- est couverte, cas limites compris, et que le
    test ne réinterprète pas la règle ;
  - `recetteur` vérifie que chaque cas est exécutable et que le résultat attendu est observable ;
  - pour un lot à risque, `auditeur-securite` ajoute les cas d'abus (droits, saisies hostiles, volumes).
- Le développeur peut **contester** un cas (ambigu, faux) : la question remonte au rédacteur, jamais tranchée par
  le développeur seul.
- Les tests automatiques sont ensuite comparés aux cas relus : un CT- sans test automatique ou sans vérification
  manuelle planifiée est un écart.
- Sortie : `04-realisation/lots/<lot>-revue-cas-de-test.md` (couverture RG ↔ CT, constats, verdict).

## 4. Qui relit qui
| Produit | Auteur | Relu par (autre métier) |
|---|---|---|
| Code d'un lot | développeur | `relecteur-code` ; + contre-relecteur si lot à risque |
| Correctif après revue | développeur | le même relecteur |
| Cas de test | `concepteur-tests` | `redacteur-sfd` + `recetteur` (+ `auditeur-securite`) |
| Tests automatiques | développeur ou `automaticien-tests` | `relecteur-code` (angle « analyse des tests ») |
| Migration de données | développeur | `architecte-donnees` |
| Contrôle visuel | `testeur-visuel` | `expert-accessibilite` sur échantillon |

## 5. Ce qui bloque une fusion
Absence de verdict écrit d'un relecteur indépendant sur le hash fusionné ; correctif non relu ; test rouge non
enregistré ; test vert d'emblée sans témoin ; cas de test non relus ; un CT- de priorité haute sans test.
