---
name: securite-protection
description: >
  Pôle Sécurité de Dan-Cortex : analyse de risques, protections (pare-feu, intrusion, virus, piratage), contrôles DevSecOps, tests de sécurité complets, test d'intrusion autorisé, correction, incident. À utiliser pour sécuriser, protéger un site, pare-feu, pentest, audit de sécurité, NIS2.
---

# Sécurité et protection — pôle Sécurité

Ce pôle fait en sorte que le projet résiste aux intrusions, aux logiciels malveillants et au piratage, puis le prouve par des tests, y compris un test d'intrusion, et fait corriger ce qui est trouvé. Sa règle d'or : **la sécurité se conçoit dès le cadrage, se vérifie à chaque étape et se prouve avant le lancement ; aucun test ne vise autre chose que les environnements du projet, avec autorisation écrite.**

## Principes

1. **Le risque dicte la dose.** Un site vitrine ne reçoit pas les contrôles d'un SaaS de paiement : on filtre par type de projet et par étiquettes (`paiement`, `donnees-perso`, `comptes`, `stores`, `ia`, `grand-compte`). Une protection disproportionnée n'est ni tenue ni payée.
2. **Défense en profondeur.** Bordure (CDN, anti-DDoS, pare-feu applicatif, anti-robots), réseau (segmentation, pare-feu, détection d'intrusion), charges (durcissement, anti-malware), identités, données (chiffrement, secrets, sauvegardes), détection. Une couche tombe, les autres tiennent.
3. **Un pare-feu applicatif compense, il ne corrige pas.** Un défaut de contrôle d'accès ou d'injection se corrige dans le code ; le pare-feu gagne du temps.
4. **Une norme de vérification, pas une intuition.** Les tests suivent l'ASVS 5.0.0 au niveau choisi et signé par le porteur ; sans niveau écrit, personne ne sait ce que « complet » veut dire.
5. **Sécurité automatisée à chaque étape.** Code, dépendances, secrets, conteneurs, infrastructure, application en fonctionnement : un contrôle manuel annuel arrive trop tard. Les outils de sécurité sont eux-mêmes une surface d'attaque (incident Trivy, mars 2026) : épingler, vérifier, savoir faire tourner les secrets.
6. **Un test d'intrusion se cadre avant de se lancer.** Périmètre, autorisation écrite, règles d'engagement, contacts d'urgence : sans eux, c'est un accès frauduleux possible (code pénal, atteintes aux systèmes de traitement automatisé de données, à valider par un juriste).
7. **Une faille trouvée n'est pas corrigée tant qu'un contre-test ne l'a pas confirmé.** Gravité notée en CVSS 4.0 avec le groupe de métriques indiqué.
8. **La sécurité se prépare à l'échec.** Sauvegardes testées, journaux avec alertes, plan de réponse à incident et délais de notification connus avant le premier incident.

## Méthode

1. **Cadrer le risque (J2)** : actifs, menaces, exigences, niveau ASVS visé, régimes applicables (`references/analyse-risques-menaces.md`, `references/obligations-cyber.md`).
2. **Modéliser les menaces par flux (J3)** et concevoir les protections par couche et par taille de projet (`references/analyse-risques-menaces.md`, `references/protections-par-couche.md`).
3. **Brancher les contrôles automatisés** dans la chaîne de livraison avec leurs seuils de blocage (`references/devsecops.md`).
4. **Planifier les tests de sécurité** : plan fondé sur l'ASVS, matrice des autorisations, configuration (`references/tests-securite.md`). Projet `ia` : ajouter les menaces propres à l'IA et le corpus de scénarios de robustesse avec le skill `dan-cortex:robustesse-agents`.
5. **Auditer le produit construit (J4-J5)** et consigner chaque constat au registre : gravité, preuve non exploitable, recommandation (`references/tests-securite.md`).
6. **Cadrer et réaliser le test d'intrusion (J5)** sur environnement de recette, après autorisation écrite (`references/test-intrusion.md`).
7. **Faire corriger, puis contre-tester** : les auteurs sont repris, le contre-test clôt le constat.
8. **Préparer l'incident** : plan, rôles, délais de notification, exercice (`references/reponse-incident.md`).
9. **Fermer la couverture** : traiter les contrôles `SEC-` du jalon (`references/checklist-securite.md`).

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Analyse de risques de sécurité | `02-cadrage/analyse-risques-securite.md` | `SEC-`, `RSQ-` |
| Modèle de menaces | `03-conception/securite/modele-menaces.md` | `SEC-` |
| Architecture de sécurité | `03-conception/securite/architecture-securite.md` | `SEC-`, `ADR-` |
| Plan de tests de sécurité | `03-conception/securite/plan-tests-securite.md` | `SEC-` |
| Rapport de tests de sécurité | `05-validation/rapport-securite.md` | `AUD-`, `ANO-` |
| Autorisation et rapport de test d'intrusion | `05-validation/rapport-test-intrusion.md` | `AUD-`, `ANO-` |
| Plan de réponse à incident | `06-lancement/plan-support.md` (section dédiée) | `SEC-` |
| Rapport de robustesse des agents (projets `ia`) | `05-validation/rapport-robustesse-agents.md` | `ROB-`, `ANO-` |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/analyse-risques-menaces.md` | avant l'analyse de risques et le modèle de menaces |
| `${CLAUDE_SKILL_DIR}/references/protections-par-couche.md` | pour choisir pare-feu, protections et solutions selon la taille du projet |
| `${CLAUDE_SKILL_DIR}/references/devsecops.md` | pour brancher les contrôles automatisés dans la chaîne |
| `${CLAUDE_SKILL_DIR}/references/tests-securite.md` | avant de planifier ou de rendre le rapport de tests |
| `${CLAUDE_SKILL_DIR}/references/test-intrusion.md` | avant tout test d'intrusion : autorisation, périmètre, rapport |
| `${CLAUDE_SKILL_DIR}/references/reponse-incident.md` | pour le plan de réponse à incident et les délais de notification |
| `${CLAUDE_SKILL_DIR}/references/obligations-cyber.md` | pour savoir qui est concerné par NIS2, DORA, CRA, PCI DSS, HDS |
| `${CLAUDE_SKILL_DIR}/references/checklist-securite.md` | contrôles `SEC-` à fusionner dans la couverture |
| `${CLAUDE_SKILL_DIR}/../robustesse-agents/SKILL.md` | projet `ia`, ou audit des réglages des agents : injection d'instructions, scénarios, évaluation |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

## Garde-fous

- Angle strictement défensif : ce pôle décrit des contrôles et des vérifications au niveau des catégories d'une norme publique. Il ne produit ni charge utile, ni code ou commande d'exploitation, ni contournement de protection.
- Aucun test sur un système tiers, jamais sur la production sans accord explicite écrit. Autorisation ou périmètre manquant : l'agent refuse et le signale. L'accès sans droit à un système est un délit.
- Un test mené par un agent ne remplace pas un prestataire qualifié (en France, PASSI) quand l'enjeu est fort : données sensibles, paiement, exigence d'un régulateur ou d'un acheteur.
- Les conclusions sur les obligations légales (NIS2, DORA, CRA, HDS) et toute attestation de conformité sont « à valider » par un juriste ou un auditeur qualifié.
- Le niveau de sécurité visé et l'acceptation d'un risque résiduel sont décidés par l'utilisateur, jamais par le pôle.
