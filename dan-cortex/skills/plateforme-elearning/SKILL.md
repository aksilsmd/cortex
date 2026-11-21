---
name: plateforme-elearning
description: "Choisir, déployer, intégrer et exploiter une plateforme d'apprentissage en ligne (LMS) avec Canvas LMS comme référence libre : auto-hébergé ou hébergé, alternatives, obligations AGPL, LTI 1.3, API REST, SSO, import de cours, données des apprenants. À utiliser pour « choisir un LMS », « plateforme e-learning », « Canvas », « LTI », « Moodle ou Canvas », « importer des cours », « notes et quiz »."
---

# Plateforme d'apprentissage en ligne (LMS)

Ce skill aide à décider si un projet doit s'appuyer sur un LMS existant, lequel, comment le déployer, le relier à d'autres outils et l'exploiter. La référence libre étudiée est Canvas LMS (Instructure, licence AGPL-3.0). Sa documentation d'API et de LTI sert de modèle pour toute plateforme comparable : cours, modules, devoirs, quiz, notes, rôles, intégrations, données des apprenants.

## Quand l'utiliser, quand ne pas l'utiliser

- Utiliser : cadrer un projet de formation en ligne, comparer des LMS, préparer un déploiement Canvas, brancher un outil par LTI, lire ou écrire des données par l'API, migrer des cours, évaluer le risque RGPD d'une plateforme.
- Ne pas utiliser : pour écrire un contenu pédagogique (voir `${CLAUDE_SKILL_DIR}/../atelier-ecriture/SKILL.md`), pour construire un LMS sur mesure sans avoir fait la comparaison (revenir d'abord à la grille), ni pour affirmer des prix, des versions ou des fonctions d'un produit sans les avoir revérifiés à la source.

## Règles d'or

1. **Rien d'inventé.** Chaque fait technique (version, commande, API) vient d'un document lu ; sinon il est marqué « à revérifier ». Les versions citées dans les fiches datent du 21 novembre 2026 et se contrôlent avant tout engagement.
2. **Licence AGPL.** Utiliser Canvas tel quel ne crée aucune obligation de publication. Le modifier et le servir à des utilisateurs par le réseau oblige à leur proposer les sources modifiées. Décider avant d'écrire la première ligne de code (voir `${CLAUDE_SKILL_DIR}/references/canvas-deploiement-exploitation.md`). Ce skill ne recopie ni texte ni code de Canvas.
3. **Données d'apprenants = données personnelles**, parfois de mineurs. Aucun déploiement ni aucune intégration sans passage par le délégué à la protection des données.
4. **Accord de l'utilisateur** avant toute installation, tout achat d'abonnement, tout appel à une API réelle ou tout export de données.
5. **Jamais de secret dans un rapport** : jetons d'API, clés de développeur, clés de chiffrement restent dans le coffre de la machine cible.
6. **Pas de jeton personnel partagé.** Une application utilisée par plusieurs personnes passe par OAuth2, pas par un jeton généré à la main.

## Méthode

1. **Cadrer le besoin.** Publics (élèves, étudiants, salariés, mineurs ?), volumétrie, contenus existants, notes et certificats, outils à relier (visio, plagiat, SIS), contraintes de langue, de lieu d'hébergement et d'accessibilité. S'appuyer sur `${CLAUDE_SKILL_DIR}/../recueil-besoin/SKILL.md`.
2. **Comparer** avec la grille de `${CLAUDE_SKILL_DIR}/references/choisir-un-lms.md` : trois voies (Canvas auto-hébergé, Canvas hébergé par Instructure, autre LMS à évaluer). Noter chaque critère avec une source.
3. **Décider et tracer** : un ADR via `${CLAUDE_SKILL_DIR}/../architecture-normes/SKILL.md`, avec le coût sur trois ans via `${CLAUDE_SKILL_DIR}/../budget-finance/SKILL.md`. Pour un arbitrage disputé, `${CLAUDE_SKILL_DIR}/../reunion-decision/SKILL.md`.
4. **Déployer** (voie auto-hébergée) : prérequis, services, fichiers de configuration, tâches d'arrière-plan, stockage, courrier. Voir la fiche déploiement.
5. **Intégrer** : LTI 1.3 pour brancher un outil, API REST pour automatiser, SSO pour l'identité, import de contenus. Voir la fiche API et LTI.
6. **Protéger les données** : minimiser ce que les outils reçoivent, fixer la durée de conservation, prévoir l'export et l'effacement.
7. **Exploiter** : sauvegardes testées, supervision, montée de version rejouée sur une copie, plan de retour arrière.
8. **Contrôler** avant de rendre (liste ci-dessous).

## Routage : besoin vers fichier

| Besoin | Fichier à ouvrir |
|---|---|
| Choisir entre Canvas hébergé, Canvas auto-hébergé, Moodle, Open edX ou autre | `${CLAUDE_SKILL_DIR}/references/choisir-un-lms.md` |
| Prérequis, architecture, configuration, AGPL, sauvegardes, montées de version | `${CLAUDE_SKILL_DIR}/references/canvas-deploiement-exploitation.md` |
| Jetons, portées, pagination, limites de débit, LTI 1.3, SSO, import de cours, événements | `${CLAUDE_SKILL_DIR}/references/canvas-api-lti.md` |
| Origine des faits, licence, commit, éléments non repris | `${CLAUDE_SKILL_DIR}/references/sources.md` |
| Cahier des charges d'une intégration | `${CLAUDE_SKILL_DIR}/../specifications/SKILL.md` |
| Réalisation et tests d'un connecteur | `${CLAUDE_SKILL_DIR}/../usine-logicielle/SKILL.md` |

## Renvois obligatoires

- **RGPD, mineurs, conservation, export, hébergeur** : agent `${CLAUDE_PLUGIN_ROOT}/agents/delegue-protection-donnees.md` et `${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md` (contrat avec l'hébergeur, sous-traitants, transferts hors Union européenne, obligations de l'AGPL).
- **Accessibilité (RGAA, WCAG)** : agent `${CLAUDE_PLUGIN_ROOT}/agents/expert-accessibilite.md`. L'accessibilité d'un outil branché par LTI n'est pas celle du LMS : à contrôler outil par outil.
- **Sécurité** : `${CLAUDE_SKILL_DIR}/../securite-protection/SKILL.md` (durcissement, secrets, tests d'intrusion sur accord).
- **Mise en production, sauvegardes, support, formation** : `${CLAUDE_SKILL_DIR}/../lancement-exploitation/SKILL.md`.

## Usage par pôle Dan-Cortex

| Pôle | Usage |
|---|---|
| Besoin et spécifications | exigences d'apprentissage, rôles, parcours, règles de notation |
| Architecture et normes | ADR de choix du LMS, schéma des flux de données, choix d'hébergement |
| Finance | coût de licence ou d'hébergement, temps d'administration, comparaison à trois ans |
| Juridique et données | AGPL, contrat d'hébergement, registre des traitements, mineurs |
| Réalisation | connecteurs LTI et API, scripts d'import, tests de bout en bout |
| Sécurité | portées minimales des clés, durcissement, journaux |
| Lancement | bascule, formation des enseignants, support |

## Contrôles avant de rendre

- Chaque affirmation de version, de prix ou de licence a une source ou la mention « à revérifier ».
- Le choix entre auto-hébergé et hébergé est justifié par des critères notés, pas par une préférence.
- L'obligation AGPL est tranchée : aucune modification, ou modifications publiées.
- Aucun jeton, mot de passe ou clé n'apparaît dans les livrables.
- Les données d'apprenants envoyées à chaque outil tiers sont listées, avec le niveau de confidentialité choisi.
- Une restauration de sauvegarde a été testée, ou le plan de test est écrit.
- Les renvois vers données, accessibilité, sécurité et exploitation sont faits.

## Références

| fichier | quand l'ouvrir |
|---|---|
| `references/choisir-un-lms.md` | comparer les voies et noter les critères |
| `references/canvas-deploiement-exploitation.md` | préparer, configurer, sauvegarder, mettre à jour un Canvas auto-hébergé |
| `references/canvas-api-lti.md` | intégrer par LTI, API, SSO, import, événements |
| `references/sources.md` | vérifier l'origine et la licence des faits retenus |
