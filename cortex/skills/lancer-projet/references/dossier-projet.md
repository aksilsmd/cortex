# Dossier projet : arborescence, identifiants, registres, script

## Arborescence

Créée par `cortex.py init`. Les chemins sont ceux qu'attend la vérification des jalons : les respecter.

```
<projet>/
  00-pilotage/     fiche-projet.md, organigramme.md, planning.md, tableau-de-bord.md, index-documents.md,
                   lecons.md, cortex.json, couverture.csv, journal-agents.csv,
                   registres/ (decisions, risques, constats, anomalies, actions, changements : fichiers .csv),
                   plans/ (plans de délégation et synthèses de pôle),
                   reunions/ (PV-<aaaammjj>-<sujet>.md), audits/ (revues, audits de jalon, audit-general.md)
  01-decouverte/   etude-de-marche.md, benchmark-concurrentiel.md, voix-du-client.md, analyse-contexte.md,
                   prediagnostic-juridique.md, note-faisabilite-technique.md, note-opportunite.md,
                   sources/ (concurrents/, avis/, marche/ : fiches de collecte datées et sourcées)
  02-cadrage/      note-de-cadrage.md, cahier-des-charges.md, personas-parcours.md, budget.md,
                   analyse-risques-securite.md, cartographie-donnees.md, strategie-marche.md
  03-conception/   specifications/ (sfg.md, sfd/<module>.md, specs-techniques.md)
                   architecture/ (dossier-architecture.md, adr/ADR-<n>-<sujet>.md, modele-donnees.md,
                                  normes-developpement.md, dependances.md, infrastructure.md)
                   design/ (workflows/<module>.md, interactions/ecrans.md, interactions/<module>.md,
                            interactions/commun.md, interactions/navigation.md, maquettes/ (dont
                            cahier-maquettes.md), design-system.md, accessibilite.md,
                            contenu-localisation.md)
                   securite/ (modele-menaces.md, architecture-securite.md, plan-tests-securite.md)
                   juridique/ (conformite-reglementaire.md, registre-traitements.md, aipd.md,
                               mentions-legales.md, cgu.md, cgv.md, politique-confidentialite.md,
                               politique-cookies.md, contrats.md, propriete-intellectuelle.md)
                   tests/ (strategie-de-test.md, cahier-de-recette.md)
                   marketing/ (plan-marketing.md, plan-commercial.md, prix-offre.md)
  04-realisation/  lots.md, journal-de-build.md, journaux/ (sorties de tests écrites par essais.py), revues/
  05-validation/   pv-recette.md, rapport-performance.md, rapport-accessibilite.md, rapport-securite.md,
                   rapport-test-intrusion.md, dossier-conformite.md
  06-lancement/    checklist-go-no-go.md, plan-de-lancement.md, runbook-mise-en-production.md,
                   plan-communication.md, plan-support.md
  07-exploitation/ suivi-indicateurs.md, feuille-de-route.md, bilan-de-projet.md
```

Le code vit dans le dépôt du projet : soit un dossier `code/` à côté, soit un dépôt séparé dont le chemin est
noté dans la fiche projet.

## Types et étiquettes

Les types et étiquettes passés à `init` filtrent la matrice de couverture. Mieux vaut une étiquette de trop
qu'un contrôle oublié.

**Types** (`--types`, plusieurs possibles) : `site` (site web d'entreprise), `ecommerce`, `mobile`, `saas`,
`niche` (produit ou micro-SaaS de niche), `erp`.

**Étiquettes** (`--tags`) :

| Famille | Étiquettes |
|---|---|
| Territoires | `fr`, `ue`, `uk`, `us`, `dz`, `ma`, `tn`, `international` |
| Clientèle | `b2c`, `b2b`, `secteur-public`, `grand-compte` |
| Données | `donnees-perso`, `donnees-sensibles`, `sante`, `mineurs`, `finance` |
| Fonctions | `paiement`, `abonnement`, `marketplace`, `ugc` (contenus publiés par les utilisateurs), `ia`, `comptes` (comptes utilisateurs), `multilingue`, `rtl` (écriture de droite à gauche), `stores` (publication sur les magasins d'applications), `hors-ligne` |
| Réalisation | `code` (code sur mesure), `progiciel` (solution du marché paramétrée), `migration` (reprise de données), `integrations` |

Changer d'avis : `cortex.py couverture resync --types … --tags …` ajoute les contrôles devenus applicables sans
perdre les statuts.

## Identifiants

Un identifiant se définit une seule fois, en première colonne d'un tableau ou en titre de section, puis se cite
partout ailleurs. C'est ce qui permet au script de vérifier la traçabilité.

| Préfixe | Objet | Défini dans |
|---|---|---|
| `EX-001` | exigence fonctionnelle | cahier des charges |
| `EXNF-001` | exigence non fonctionnelle | cahier des charges |
| `FN-001` | fonction | SFG |
| `RG-001` | règle de gestion | SFD |
| `WF-001` | workflow d'une fonctionnalité | `design/workflows/` |
| `EC-001` | écran | `design/interactions/ecrans.md` |
| `EL-001-01` | élément interactif de l'écran EC-001 | `design/interactions/<module>.md` |
| `CT-001` | cas de test | cahier de recette |
| `ADR-001` | décision d'architecture | `architecture/adr/` |
| `LOT-001` | lot de réalisation | `04-realisation/lots.md` |
| `DEC-`, `RSQ-`, `AUD-`, `ANO-`, `ACT-`, `CHG-` | décision, risque, constat, anomalie, action, demande de changement | registres, numérotés par le script |
| `XXX-001` | contrôle de couverture (trois lettres de domaine) | matrice de couverture |

Chaîne vérifiée par `cortex.py tracabilite verifier` : chaque exigence est reprise par une fonction, chaque
fonction par une règle ou un workflow, chaque règle et chaque workflow par un cas de test ; chaque élément
interactif est couvert par un cas de test, directement ou par son workflow.

## Commandes du script

`python3 <chemin du skill lancer-projet>/scripts/cortex.py aide` affiche la liste complète. Les plus utiles :

| Besoin | Commande |
|---|---|
| Où en est-on ? | `etat` |
| Noter où l'on s'arrête | `etat --set vague=2 note="vague 3A lancée, attendre les comptes rendus"` |
| Contrôles restant pour un domaine | `couverture liste --domaine SEC --jalon J3 --statut a-faire --court` |
| Clore des contrôles | `couverture maj SEC-001,SEC-004 --nouveau fait --preuve 03-conception/securite/modele-menaces.md` |
| Écarter un contrôle | `couverture maj JUR-031 --nouveau non-applicable --note "pas de vente aux consommateurs"` |
| Accepter un risque | `couverture maj SEC-044 --nouveau risque-accepte --note "accepté par <nom> le <date> : <raison>"` |
| Ajouter un contrôle propre au projet | `couverture ajouter --domaine SEC --controle "…" --jalon J4 --criticite majeur` |
| Tracer une décision | `registre decisions ajouter titre="…" type=1 decision="…" motifs="…" options_ecartees="…" decideur="…" statut=a-valider` |
| Valider une décision | `registre decisions maj DEC-003 statut=validee` |
| Risque | `registre risques ajouter titre="…" domaine=… impact=4 probabilite=2 parade="…" proprietaire=…` |
| Constat d'audit ou de revue | `registre constats ajouter source=… gravite=majeur domaine=… constat="…" preuve="…" responsable=… recommandation="…"` |
| Anomalie de test | `registre anomalies ajouter titre="…" severite=bloquante cas_de_test=CT-012 lot=… description="…" responsable=…` |
| Demande de changement | `registre changements ajouter titre="…" demandeur=… impact="périmètre, coût, délai" decision="…"` |
| Ce qui est ouvert | `registre constats liste --ouverts` |
| Journal d'un agent | `journal ajouter --agent … --modele … --tokens … --duree …` ; `journal bilan` |
| Synthèses présentes ? | `docs verifier` ; index : `docs index` |
| Interactions cohérentes ? | `interactions verifier` ; carte : `interactions graphe` |
| Traçabilité complète ? | `tracabilite verifier` |
| Jalon franchissable ? | `jalon verifier J3` ; puis `jalon franchir J3` |
| Vue pour l'utilisateur | `tableau-de-bord` |

Statuts d'un contrôle : `a-faire`, `en-cours`, `fait` (preuve obligatoire), `non-applicable` (motif obligatoire),
`risque-accepte` (nom et raison obligatoires).

Sans Python disponible, tenir les mêmes registres à la main en Markdown dans `00-pilotage/` et vérifier les jalons
à partir de `assets/jalons.json` : le résultat est le même, le coût en tokens plus élevé.
