# Norme de reprise par un humain

But : un développeur qui n'a jamais vu le projet, et qui n'a ni les agents ni leur historique, doit pouvoir
installer, comprendre, modifier et livrer sans se perdre. Le code produit par des agents est lu un jour par une
personne : il s'écrit pour elle. Cette norme s'ajoute à `normes-developpement.md` ; ses contrôles sont NOR-024 à
NOR-033 de `checklist-normes.md`.

## Sommaire
1. Le test de reprise · 2. Documentation d'entrée · 3. Structure et nommage · 4. Code lisible · 5. Traçabilité
règle ↔ code ↔ test · 6. Environnement reproductible · 7. Historique et branches · 8. Exploitation ·
9. Ce qui est interdit · 10. Contrôle

## 1. Le test de reprise (critère d'acceptation)
Avant chaque jalon de réalisation et avant toute remise du code à un tiers, un agent **neuf** (aucun contexte du
projet, seulement le dépôt) joue le développeur qui reprend. En une session, il doit :
1. installer et lancer le projet en suivant la seule documentation, sur une machine standard ;
2. lancer les tests et obtenir le même résultat que la chaîne d'intégration ;
3. retrouver où est codée une règle de gestion tirée au sort (RG-…) et le test qui la vérifie ;
4. faire une petite modification (un libellé, une règle simple) avec son test, sans casser le reste ;
5. noter chaque endroit où il a hésité, deviné ou dû lire du code faute de documentation.
Chaque hésitation devient une correction de documentation ou de nommage. Le rapport va dans
`05-validation/reprise-humaine-<date>.md`. Échec du point 1 ou 2 = bloquant pour la remise.

## 2. Documentation d'entrée (à la racine du dépôt)
| Fichier | Contenu minimal |
|---|---|
| `README.md` | ce que fait le produit en cinq lignes ; prérequis exacts (versions) ; installation et premier lancement en dix minutes au plus ; commandes usuelles ; où trouver la suite |
| `docs/ARCHITECTURE.md` | schéma d'ensemble ; carte des dossiers (« pour changer X, aller dans Y ») ; flux d'une requête de bout en bout ; principes (couches, dépendances autorisées) ; liens vers les ADR |
| `docs/DEMARRER.md` | parcours du nouvel arrivant : jour 1 (installer, lancer, tester), première modification guidée, à qui ou à quoi se référer |
| `docs/GLOSSAIRE.md` | mots du métier ↔ noms dans le code (« créance » ↔ `receivable`…), identifiants de documents (RG-, FN-, ADR-, ANO-…) et leur sens |
| `docs/adr/` | une décision d'architecture par fichier : contexte, décision, conséquences, statut |
| `CONTRIBUTING.md` | conventions de nommage, de commit et de branche ; comment ajouter un module, une migration, une traduction, un test |
| `CHANGELOG.md` | ce qui a changé, par version, en langage clair |
| `docs/EXPLOITATION.md` | démarrer, arrêter, sauvegarder, restaurer, lire les journaux, faire tourner une clé, que faire en cas d'incident |
Chaque module (paquet, application, service) a un `README.md` de dix à trente lignes : rôle, ce qu'il expose,
de quoi il dépend, où sont ses tests, pièges connus.

## 3. Structure et nommage
- **Nommer par le métier, jamais par la chronologie** : `commande/`, `facturation/`, `stock/` ; jamais
  `lot003.ts`, `v7h.test.ts`, `sprint2/`, `nouveau-final.ts`. Les numéros de lot, de vague, de porte ou d'ordre
  de mission restent dans l'historique et les documents de pilotage, pas dans les noms de fichiers ni de fonctions.
- Une **langue d'identifiants** unique, décidée et écrite (souvent l'anglais pour le code, la langue de
  l'utilisateur pour les textes et les commentaires) ; les écarts sont dans le glossaire.
- Un dossier par domaine ; la profondeur reste faible (trois niveaux sous `src/` au plus) ; un fichier, une
  responsabilité ; au-delà de 400 lignes, découper ou justifier.
- Les tests sont à côté du code qu'ils vérifient et portent le même nom.

## 4. Code lisible
- Fonctions courtes (≈ 50 lignes), complexité bornée par l'outil de lint ; pas d'astuce sans commentaire.
- Commentaires : le **pourquoi** (règle, contrainte, décision), pas le quoi. Une règle de gestion implémentée cite
  son identifiant (`// RG-1409 : refus journalisé avec pseudonyme`), une décision cite son ADR.
- En-tête d'une ligne par fichier non évident : à quoi il sert.
- Pas de code mort, pas de code commenté, pas de « TODO » sans identifiant de ticket.
- Erreurs explicites (message, code, cause) ; pas d'exception avalée sans trace.
- Les noms des tests décrivent un comportement (« refuse une commande d'un pro non validé »), pas un numéro.

## 5. Traçabilité règle ↔ code ↔ test
Une table, générée par script de préférence, relie chaque RG- à son ou ses fichiers et à ses tests
(`docs/tracabilite.md` ou sortie de l'outil de traçabilité). Un humain qui lit une spécification retrouve le
code, et inversement.

## 6. Environnement reproductible
- Toutes les dépendances sont **déclarées** dans le manifeste du langage avec des versions exactes et un fichier
  de verrouillage commité (`package-lock.json`, `poetry.lock`, `go.sum`…). Un environnement qui ne fonctionne que
  par un lien vers un dossier propre à une machine, ou par un outil d'agent, est un écart bloquant pour la remise.
- Versions des outils fixées (`.nvmrc`, `.tool-versions`, image de conteneur) ; une seule commande pour
  installer, une pour tester, une pour construire, une pour lancer, toutes au `README`.
- Configuration par variables d'environnement documentées (nom, rôle, valeur par défaut, obligatoire ou non),
  avec un fichier d'exemple sans secret.
- La chaîne d'intégration exécute exactement les commandes documentées.

## 7. Historique et branches
- Commits atomiques, messages qui disent pourquoi ; la branche principale est toujours verte.
- Aucune branche morte non expliquée : chaque branche non fusionnée est fusionnée, abandonnée par écrit, ou
  listée dans `docs/BRANCHES.md` avec son état.
- Les étiquettes de version correspondent au `CHANGELOG`.

## 8. Exploitation
Procédures pas à pas dans `docs/EXPLOITATION.md`, rejouées au moins une fois (sauvegarde puis restauration
réelle sur une copie). Journaux structurés et lisibles par un humain.

## 9. Interdits
Dépendre du contexte d'un agent pour comprendre le code ; laisser dans le code des références internes au
pilotage sans glossaire (OM-, porte n, vague n) ; fichiers ou fonctions nommés par lot ; dépendances non
déclarées ; procédures connues d'un seul agent ou d'une seule session.

## 10. Contrôle
Le `gardien-des-normes` vérifie cette norme à chaque fin de lot (documentation de module à jour, nommage) ; le
test de reprise (§1) est joué avant J5 et avant toute remise à un tiers ; le `verificateur` en contrôle le
rapport. Les écarts vont au registre des anomalies, comme un défaut du produit.
