---
name: architecture-normes
description: >
  Pôle Architecture et normes de Dan-Cortex : choix tracés du langage, des frameworks, de la base de données, de la structure et des outils ; schéma de données ; normes de code ; infrastructure. À utiliser pour « quelle techno choisir », « quelle architecture », « modèle de données », « ADR », « stack technique », « hébergement ».
---

# Architecture et normes — pôle Architecture

Ce pôle décide comment le produit est construit, sur quelle pile, avec quelles données, selon quelles règles de code et sur quelle infrastructure. Sa règle d'or : **aucun choix technique sans au moins deux options comparées sur critères, débattues et tracées dans une décision d'architecture.**

## Principes

1. **Acheter, configurer, construire : dans cet ordre.** C'est la première décision d'architecture. Chaque ligne de code sur mesure est un passif à maintenir ; on ne construit que ce qui différencie le produit.
2. **Deux options au moins, toujours.** Une option unique est une préférence, pas une décision. Les options écartées sont écrites avec leur motif : c'est ce qu'on relira dans trois ans.
3. **Les exigences non fonctionnelles chiffrées précèdent le style.** Sans cible mesurable (latence, disponibilité, volumétrie), on suit une tendance, on ne conçoit pas une architecture.
4. **Monolithe modulaire par défaut.** Les microservices se justifient par écrit (équipes autonomes, scalabilité indépendante, maturité de livraison continue), jamais par imitation.
5. **La pile doit être maîtrisée par les agents qui la produiront.** Typage statique, framework courant, tests exécutables en terminal : c'est vérifié par une tranche verticale avant l'engagement.
6. **Versions à support long, datées.** Retenir une LTS (ou un support d'au moins trois ans à la mise en production) et noter sa date de fin. Les versions de ce pôle sont celles d'octobre 2026 : les recouper avant de décider.
7. **Une règle d'architecture qui ne se vérifie pas par machine n'existe pas.** Frontières de modules, dépendances interdites, budgets de performance deviennent des tests en intégration continue.
8. **Aucune pile « préférée ».** Les piles de référence illustrent des contextes ; le choix naît des critères du projet.

## Méthode

1. **Acheter, configurer ou construire** (J1, puis J3) : trois options chiffrées sur 3 à 5 ans, `references/choix-techniques.md`, section 1.
2. **Fixer les exigences d'architecture** : exigences non fonctionnelles chiffrées, arbre d'utilité, style et API, `references/styles-architecture.md`.
3. **Instruire les options** : grille pondérée, éliminatoires, tranche verticale confiée à un agent, `references/choix-techniques.md`.
4. **Débattre et tracer** : comité d'architecture, une ADR par choix, `references/dossier-architecture-adr.md`.
5. **Documenter** : dossier d'architecture en vues C4, `references/dossier-architecture-adr.md`.
6. **Concevoir les données** : modèle, conventions, migrations, locataires, données personnelles, `references/donnees-schema.md`.
7. **Écrire les normes, dépendances et l'infrastructure** : `references/normes-developpement.md`, `references/infrastructure-hebergement.md`.
8. **Contrôler** : parcourir les listes de contrôles ; lancer `python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/cortex.py couverture liste --domaine ARC --jalon J3 --statut a-faire --court` (idem avec le préfixe de chaque liste de contrôles du pôle).

## Livrables

| Livrable | Emplacement dans le dossier projet | Identifiants |
|---|---|---|
| Note de faisabilité technique | `01-decouverte/note-faisabilite-technique.md` | |
| Dossier d'architecture | `03-conception/architecture/dossier-architecture.md` | |
| Décisions d'architecture | `03-conception/architecture/adr/ADR-<n>-<sujet>.md` | `ADR-` |
| Modèle de données | `03-conception/architecture/modele-donnees.md` | |
| Normes de développement | `03-conception/architecture/normes-developpement.md` | |
| Dépendances | `03-conception/architecture/dependances.md` | |
| Infrastructure | `03-conception/architecture/infrastructure.md` | |

## Références

| Fichier | Quand le lire |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/choix-techniques.md` | acheter ou construire ; choisir langage, framework, base, outils ; grille ; piles de référence |
| `${CLAUDE_SKILL_DIR}/references/styles-architecture.md` | choisir un style, une API, une messagerie ; attributs de qualité ; évaluer ; anti-modèles |
| `${CLAUDE_SKILL_DIR}/references/donnees-schema.md` | concevoir le schéma, les migrations, les locataires, les données personnelles |
| `${CLAUDE_SKILL_DIR}/references/dossier-architecture-adr.md` | rédiger le dossier d'architecture ou une décision |
| `${CLAUDE_SKILL_DIR}/references/normes-developpement.md` | écrire ou contrôler les normes de code et les dépendances |
| `${CLAUDE_SKILL_DIR}/references/infrastructure-hebergement.md` | concevoir hébergement, environnements, déploiement, supervision |
| `${CLAUDE_SKILL_DIR}/references/checklist-architecture.md` | contrôles ARC avant chaque jalon |
| `${CLAUDE_SKILL_DIR}/references/checklist-donnees.md` | contrôles DON avant chaque jalon |
| `${CLAUDE_SKILL_DIR}/references/checklist-normes.md` | contrôles des normes de développement |
| `${CLAUDE_SKILL_DIR}/references/checklist-infrastructure.md` | contrôles d'infrastructure |
| `${CLAUDE_SKILL_DIR}/references/orchestration.md` | chef d'orchestre seulement : agents du pôle, vagues, essaimage, revues |

## Garde-fous

- Une décision de type 1 (langage, framework structurant, schéma, hébergement, tenancy) n'est jamais prise seul : elle passe en comité d'architecture et à l'utilisateur.
- Versions, dates de support et statistiques viennent de sources datées d'octobre 2026, extraites automatiquement : écrire « à vérifier » plutôt que d'affirmer ce qui n'est pas confirmé.
- Les pondérations de la grille sont une synthèse à calibrer en atelier, pas une norme.
- Conformité (CRA, RGPD, certifications) : le pôle prépare le travail du juriste et de l'auditeur ; marquer « à valider ».
- Ne jamais installer ni recommander un paquet sans avoir vérifié qu'il existe, est maintenu et sous licence compatible.
