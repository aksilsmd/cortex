# Architecture propre, DDD et hexagonal : vue d'ensemble

> Traduit et adapté de `ccheney/robust-skills`, `skills/clean-ddd-hexagonal/SKILL.md`, commit `0eea7b060d12`. © 2026 robust-skills contributors, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

Point d'entrée du dossier, à lire quand une tâche touche aux frontières du domaine ou au sens des dépendances côté serveur : modélisation d'agrégats, contextes délimités, isolement des cas d'usage, refonte d'architecture. Pas pour un changement CRUD ordinaire. Le résumé de méthode reste `../c4-ddd-hexagonal.md` §5 à §8 ; ce dossier en donne le détail.

## Sommaire
1. Choisir la portée
2. Garder les frontières qui comptent
3. Quel fichier lire

## 1. Choisir la portée

Ces modèles servent à résoudre un problème précis de domaine ou de dépendances. C'est une synthèse argumentée, pas une arborescence imposée ; l'ordre de mission et les ADR du projet priment.

Partir du comportement demandé, du modèle de domaine existant et des dépendances actuelles. Garder le langage et l'architecture du projet, sauf si les changer fait partie de la tâche. Un CRUD simple peut rester simple : ni la taille de l'équipe, ni le nombre d'entités, ni la longueur des fichiers ne décident à eux seuls de l'intérêt du DDD.

| Question de conception | Modèle concerné |
|---|---|
| Quel langage et quelles règles de cohérence décrivent le métier ? | DDD, contextes délimités, agrégats |
| Dans quel sens pointent les dépendances du code ? | architecture propre, en oignon |
| Comment l'application sert-elle plusieurs interfaces ou infrastructures ? | hexagonal, ports et adaptateurs |
| Lectures et écritures demandent-elles des modèles différents ? | CQRS |
| Faut-il reconstruire l'état depuis un historique d'événements ? | sourçage d'événements |

Si un invariant métier est inconnu, nommer la règle précise qui manque (question à l'utilisateur ou au `redacteur-sfd`, marquée « à valider ») et poursuivre ce qui n'en dépend pas. Ne pas inventer de comportement métier ; ne pas exiger un atelier de découverte pour un correctif local.

## 2. Garder les frontières qui comptent

- Le comportement du domaine ne dépend ni de HTTP, ni de la persistance, ni de la messagerie. L'orchestration va dans les cas d'usage de l'application ; les entrées-sorties externes dans les adaptateurs.
- L'identité d'une entité se modélise à part de l'égalité d'un objet-valeur. Les frontières d'agrégat se choisissent d'après les invariants transactionnels et la contention.
- Préférer les transactions contenues dans un agrégat. Quand une exigence impose l'atomicité entre agrégats, rendre ce compromis explicite (ADR) au lieu de passer en silence à la cohérence à terme.
- Utiliser une boîte d'envoi transactionnelle quand une modification validée en base et la livraison d'un événement externe doivent être fiables ensemble.
- CQRS, sourçage d'événements, interfaces de dépôt et dossiers de présentation séparés sont des choix justifiés par la tâche ; adapter les noms et dossiers des exemples au projet.

Livrer le modèle, le correctif ou la revue demandés avec les frontières touchées et les compromis qui les expliquent. Valider les invariants modifiés et les contrats d'adaptateurs au bon niveau de test. Une question d'architecture n'oblige pas à implémenter tous les modèles.

## 3. Quel fichier lire

Charger le fichier de la décision en cours, pas tout le dossier.

| Tâche | Fichier |
|---|---|
| Entités, objets-valeurs, agrégats, dépôts, événements, services, fabriques, spécifications | `ddd-tactique.md` |
| Ports, adaptateurs entrants et sortants, nommage, assemblage | `hexagonal.md` |
| CQRS, événements de domaine et d'intégration, boîte d'envoi, sagas, consommateur idempotent, sourçage d'événements | `cqrs-evenements.md` |
| Langage omniprésent, contextes, carte des contextes ; couches et sens des dépendances ; tests | `../c4-ddd-hexagonal.md` §5 et §7 |

Fondements : Eric Evans, *Domain-Driven Design* (2003) ; Alistair Cockburn, *Hexagonal Architecture* (2005) ; Robert C. Martin, *The Clean Architecture* (2012).
