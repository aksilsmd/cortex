# Phases et jalons

Lire uniquement la section du jalon en cours. Chaque section donne les vagues types du mode `standard` ; les
variantes `eclair` et `integral` sont indiquées en fin de section. Le détail des missions de chaque pôle est dans
le fichier `references/orchestration.md` du skill du pôle.

## Sommaire
- J0 Qualification
- J1 Opportunité
- J2 Cadrage
- J3 Conception
- J4 Réalisation
- J5 Validation
- J6 Lancement
- J7 Bilan
- Règles communes à tous les jalons

## J0 Qualification

**But :** savoir de quel projet on parle et comment on va travailler. Tu le fais seul, sans agent.

**Prérequis à réunir avant toute vague** (les demander ou les poser en hypothèse) :

- un porteur du projet qui décide (l'utilisateur ou la personne qu'il désigne) ;
- le problème à résoudre et pour qui, en une phrase ;
- l'ordre de grandeur du budget et du délai, même approximatif ;
- les pays visés et la nature des données traitées ;
- ce qui existe déjà : marque, site, données, équipe, outils, contrats ;
- le périmètre confié à Cortex et le niveau d'autonomie.

**Livrables :** `00-pilotage/fiche-projet.md`, `00-pilotage/organigramme.md`, matrice de couverture initialisée.

**Passage :** l'utilisateur a validé le plan annoncé. En mode `standard` ou `integral`, ne lancer aucune vague
sans confirmation explicite du mode et du périmètre : une vague large sur une hypothèse non confirmée est le
gaspillage le plus coûteux. S'il ne peut pas répondre (session sans interlocuteur), écrire les hypothèses et
rester en mode `eclair`.

## J1 Opportunité

**Question tranchée :** faut-il y aller, et sous quel angle ?

**Vague 1A — collecte et analyses, en parallèle**

| Agent | Livrable |
|---|---|
| analyste-marche | `01-decouverte/etude-de-marche.md` |
| analyste-concurrence, avec un essaim de collecteur-web par concurrent | `01-decouverte/benchmark-concurrentiel.md`, fiches dans `sources/concurrents/` |
| analyste-voix-client, avec un essaim de collecteur-web par source | `01-decouverte/voix-du-client.md`, fiches dans `sources/avis/` |
| analyste-contexte | `01-decouverte/analyse-contexte.md` |
| juriste-numerique | `01-decouverte/prediagnostic-juridique.md` : obstacles légaux, activité réglementée, obligations structurantes |
| architecte-solution | `01-decouverte/note-faisabilite-technique.md` : solutions existantes, acheter ou construire, risques techniques |
| controleur-financier | ordres de grandeur de coût et modèle économique, versés dans la note d'opportunité |

L'essaim de collecte part dans la même vague que les analystes si la liste des concurrents et des sources est
connue ; sinon les analystes la produisent d'abord et l'essaim part en vague 1A bis.

**Vague 1B — synthèse**

| Agent | Livrable |
|---|---|
| stratege-produit | `01-decouverte/note-opportunite.md` : positionnement, proposition de valeur, ce qui manque sur le marché, ce qu'il faut ajouter, supprimer, différencier, deux ou trois options de périmètre chiffrées |
| contradicteur | pré-mortem annexé à la note : « le projet a échoué dans dix-huit mois, pourquoi ? » |

**Réunion :** comité d'opportunité (collégiale). Décisions de type 1 : y aller, pivoter ou renoncer ;
positionnement ; option de périmètre.

**Passage :** documents présents, contrôles J1 traités, décision validée par l'utilisateur.

**Variantes.** `eclair` : un seul `analyste-concurrence` produit `etude-de-marche.md` (marché, concurrence, voix
du client en un document), puis `stratege-produit` ; décision par arbitrage direct. `integral` : orchestrateur du
pôle Stratégie, essaims élargis, entretiens ou sondage proposés à l'utilisateur, `contradicteur` sur le modèle de
la session.

## J2 Cadrage

**Question tranchée :** quoi exactement, pour qui, pour combien, pour quand ?

**Vague 2A — en parallèle**

| Agent | Livrable |
|---|---|
| expert-cahier-des-charges | `02-cadrage/note-de-cadrage.md` puis `02-cadrage/cahier-des-charges.md` (exigences EX- et EXNF-) |
| concepteur-ux | `02-cadrage/personas-parcours.md` |
| architecte-securite | `02-cadrage/analyse-risques-securite.md` : actifs, menaces, exigences de sécurité |
| delegue-protection-donnees | `02-cadrage/cartographie-donnees.md` : données, finalités, bases légales, besoin d'analyse d'impact |
| stratege-marketing | `02-cadrage/strategie-marche.md` : cible, message, canaux, modèle de prix envisagé |

**Vague 2B — dépend du cahier des charges**

| Agent | Livrable |
|---|---|
| planificateur | `00-pilotage/planning.md` : découpage, jalons datés, RACI, dépendances ; registre des risques alimenté |
| controleur-financier | `02-cadrage/budget.md` : budget de construction et d'exploitation, justification économique, scénarios |

**Revues croisées :** le cahier des charges est relu par l'architecte (faisabilité), le concepteur de tests
(testabilité), le juriste (conformité), le contrôleur financier (coût).

**Réunion :** comité de cadrage (collégiale). Décisions de type 1 : périmètre de la première version, budget,
calendrier, risques acceptés.

**Passage :** documents présents, contrôles J2 traités, décisions validées.

**Variantes.** `eclair` : `expert-cahier-des-charges` produit note de cadrage et cahier des charges ;
`controleur-financier` produit budget et planning ; pas de vague 2B séparée. `integral` : ateliers simulés par
pôle, estimation à trois points, analyse de sensibilité, contre-estimation indépendante du budget.

## J3 Conception

**Question tranchée :** comment exactement ? C'est le jalon le plus dense : deux vagues.

**Vague 3A — conception générale, en parallèle**

| Agent | Livrable |
|---|---|
| redacteur-sfg | `03-conception/specifications/sfg.md` (fonctions FN-) |
| cartographe-interactions | `03-conception/design/workflows/` (WF-) et `03-conception/design/interactions/ecrans.md` (EC-) |
| maquettiste | maquettes filaires dans `03-conception/design/maquettes/`, `03-conception/design/design-system.md` |
| architecte-solution | `03-conception/architecture/dossier-architecture.md`, décisions dans `adr/` |
| architecte-donnees | `03-conception/architecture/modele-donnees.md` |
| gardien-des-normes | `03-conception/architecture/normes-developpement.md`, `dependances.md` |
| ingenieur-devops | `03-conception/architecture/infrastructure.md` |
| architecte-securite | `03-conception/securite/modele-menaces.md`, `architecture-securite.md` |
| juriste-numerique et delegue-protection-donnees | `03-conception/juridique/conformite-reglementaire.md`, `registre-traitements.md`, analyse d'impact si requise |
| concepteur-tests | `03-conception/tests/strategie-de-test.md` |
| expert-accessibilite | `03-conception/design/accessibilite.md` |

**Réunion intermédiaire :** comité d'architecture (collégiale). Décisions de type 1 : langage, frameworks,
structure, schéma de données, hébergement, dépendances majeures, niveau de sécurité visé.

**Vague 3B — conception détaillée, dépend de 3A**

| Agent | Livrable |
|---|---|
| redacteur-sfd, en essaim par module | `03-conception/specifications/sfd/<module>.md` (règles RG-) |
| redacteur-specs-techniques | `03-conception/specifications/specs-techniques.md`, contrats d'interface |
| cartographe-interactions, en essaim par module | `03-conception/design/interactions/<module>.md` (éléments EL-) |
| maquettiste | maquettes haute fidélité des écrans clés |
| redacteur-contenu-localisation | `03-conception/design/contenu-localisation.md` |
| concepteur-tests | `03-conception/tests/cahier-de-recette.md` (cas CT-) |
| juriste-numerique | documents juridiques : mentions légales, conditions générales, politique de confidentialité, contrats |
| stratege-marketing, expert-acquisition, responsable-commercial | `03-conception/marketing/plan-marketing.md`, `plan-commercial.md`, `prix-offre.md` |
| planificateur et controleur-financier | planning détaillé, découpage en lots, budget révisé |

**Contrôles mécaniques :** `cortex.py interactions verifier`, `cortex.py interactions graphe`,
`cortex.py tracabilite verifier`, `cortex.py docs verifier`. Toute erreur retourne à son auteur.

**Revues croisées :** matrice complète de `revues-croisees.md`.

**Audit de jalon :** `auditeur-general` en audit allégé (cohérence entre documents, couverture).

**Passage :** documents présents, contrôles mécaniques sans erreur, contrôles J3 traités, décisions
d'architecture validées, constats bloquants de l'audit levés.

**Variantes.** `eclair` : une seule vague, rôles fusionnés, spécifications détaillées limitées au parcours
principal, pas d'audit de jalon. `integral` : orchestrateurs de pôle, deux options d'architecture instruites et
comparées, maquettes de tous les écrans, analyse d'impact complète, audit de jalon complet.

## J4 Réalisation

**Question tranchée :** est-ce construit, testé, conforme aux normes ? Suivre le skill `usine-logicielle`.

**Vague 4A — préparation**

| Agent | Livrable |
|---|---|
| planificateur avec architecte-solution | `04-realisation/lots.md` : lots, contrats d'interface, dépendances, ordre |
| ingenieur-devops | dépôt, intégration continue, environnements |
| gardien-des-normes | outils de contrôle des normes branchés : formatage, analyse statique, seuils de qualité |
| concepteur-tests | harnais de tests et jeux de données |

**Vagues 4B à 4n — un incrément par vague**

Pour chaque ensemble de lots indépendants, en parallèle : un développeur par lot (tests unitaires et code), puis
dans la vague suivante `relecteur-code` et `gardien-des-normes` sur les différences, `automaticien-tests` pour les
tests fonctionnels, d'API et de bout en bout du lot, `auditeur-securite` pour les contrôles de sécurité
automatisés. Les anomalies vont au registre ; le développeur d'origine est repris pour corriger ; un
`executant-tests` rejoue la non-régression.

En parallèle du code, hors atelier : contenus, documents juridiques définitifs, supports marketing, documentation
utilisateur, préparation du support.

**Journal :** `04-realisation/journal-de-build.md`, une ligne par lot et par incrément.

**Passage :** tous les lots livrés ; tests unitaires, fonctionnels, d'API et de bout en bout au vert ; normes
respectées ; aucune anomalie bloquante ; aucune vulnérabilité critique ou haute ouverte.

**Variantes.** `eclair` : lots plus gros, contrôles automatiques à la place de la revue par agent. `integral` :
revue de chaque lot par deux relecteurs, tests de mutation sur le cœur métier, isolement des lots par worktree.

## J5 Validation

**Question tranchée :** est-ce prêt à être lancé ?

**Vague 5A — en parallèle**

| Agent | Livrable |
|---|---|
| recetteur | `05-validation/pv-recette.md` : campagne complète du cahier de recette |
| automaticien-tests | `05-validation/rapport-performance.md` |
| expert-accessibilite | `05-validation/rapport-accessibilite.md` |
| auditeur-securite | `05-validation/rapport-securite.md` |
| testeur-intrusion | `05-validation/rapport-test-intrusion.md` (périmètre et autorisation écrits d'abord) |
| juriste-numerique et delegue-protection-donnees | `05-validation/dossier-conformite.md` |
| ingenieur-devops | répétition de déploiement, sauvegarde et restauration testées |

**Corrections** par les auteurs repris, puis contre-tests et non-régression.

**Audit général :** suivre le skill `audit-general` : rapport de l'`auditeur-general`, réunion plénière, décisions,
corrections, recontrôle. Livrable : `00-pilotage/audits/audit-general.md`.

**Réunion :** go/no-go de lancement (collégiale, type 1), sur la base de `06-lancement/checklist-go-no-go.md`
préparée par `responsable-lancement`.

**Passage :** PV de recette signé par l'utilisateur, aucun constat bloquant, décision go validée.

## J6 Lancement

**Vague 6A :** `responsable-lancement` (`06-lancement/plan-de-lancement.md`,
`runbook-mise-en-production.md`), `stratege-marketing` et `expert-acquisition` (campagne et
`plan-communication.md`), `responsable-support-formation` (`plan-support.md`), `ingenieur-devops`
(supervision, alertes, retour arrière prêt).

**Mise en production :** jamais sans accord explicite de l'utilisateur, étape par étape selon le plan de bascule.

**Surveillance renforcée :** pendant la période fixée par le plan, points de situation, anomalies au registre.

## J7 Bilan

**Vague 7A :** `analyste-voix-client` (premiers retours), `controleur-financier` (réel contre budget),
`responsable-lancement` (`07-exploitation/suivi-indicateurs.md`), `planificateur`
(`07-exploitation/feuille-de-route.md`).

**Réunion :** rétrospective (panel). **Audit de clôture** allégé. **Livrable :**
`07-exploitation/bilan-de-projet.md`, bilan de consommation compris.

## Règles communes à tous les jalons

1. Entrée de jalon : `cortex.py etat`, lecture de la section du jalon, plan de vagues annoncé en trois lignes.
2. Une vague = un message de lancements. Une vague qui dépend d'une autre attend ses comptes rendus.
3. Sortie de jalon : `cortex.py jalon verifier Jn`, point utilisateur, `cortex.py jalon franchir Jn`,
   `cortex.py tableau-de-bord`, `cortex.py docs index`. Mettre à jour les décisions structurantes de la fiche
   projet et ajouter trois lignes à `00-pilotage/lecons.md` : ce qui a marché, ce qui a coûté, ce qu'on change.
4. Un jalon peut être franchi en force sur décision explicite de l'utilisateur
   (`jalon franchir Jn --force "motif, décidé par …"`) : les manques restent visibles au tableau de bord.
5. Si le périmètre de la mission s'arrête avant J7, s'arrêter au jalon convenu et remettre la liste de ce qui
   resterait à faire.
