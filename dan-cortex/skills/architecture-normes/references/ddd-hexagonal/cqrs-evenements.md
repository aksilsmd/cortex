# CQRS et événements : séparer lectures et écritures, livrer les événements de façon fiable

> Traduit et adapté de `ccheney/robust-skills`, `skills/clean-ddd-hexagonal/references/CQRS-EVENTS.md`, commit `0eea7b060d12`. © 2026 robust-skills contributors, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire avant d'introduire CQRS, une file d'événements, une boîte d'envoi transactionnelle, une saga ou le sourçage d'événements. Sources d'origine : Martin Fowler (*CQRS*, *Event Sourcing*) ; Chris Richardson (*Transactional Outbox*) ; Udi Dahan et Jimmy Bogard (événements de domaine) ; documentation d'architecture Microsoft (CQRS, événements de domaine).

## Sommaire
1. CQRS en bref
2. Commandes et requêtes
3. Modèle de lecture
4. Événements de domaine
5. Événements de domaine ou d'intégration
6. Répartiteur d'événements
7. Boîte d'envoi transactionnelle
8. Quand utiliser CQRS
9. Sourçage d'événements
10. Saga
11. Consommateur idempotent
12. Contrôles avant de rendre

## 1. CQRS en bref

Séparer la responsabilité des commandes et des requêtes : deux modèles. Côté écriture, la commande passe par un gestionnaire (cas d'usage), modifie le modèle de domaine (agrégats) et la base d'écriture. Côté lecture, la requête passe par un gestionnaire qui lit une base optimisée. Les événements de domaine mettent à jour la base de lecture.

## 2. Commandes et requêtes

- **Commande** : intention de changer l'état (`PasserCommande`, `ConfirmerCommande`, `AnnulerCommande` avec motif). Le gestionnaire crée ou charge l'agrégat, vérifie les références (produit introuvable : erreur explicite), enregistre, puis publie les événements de l'agrégat.
- Publier **après** l'enregistrement peut perdre des événements si le processus tombe entre les deux. Acceptable pour un effet interne au processus ; pour un événement vers un autre service, utiliser la boîte d'envoi (§7).
- **Requête** : lit sans effet de bord, ne modifie **jamais** l'état. Elle renvoie un DTO (identifiant, client et son nom, statut, lignes avec nom de produit et sous-total, total, dates) ; pagination par défaut explicite (page 1, 20 éléments).

## 3. Modèle de lecture

Structure optimisée pour les requêtes, dénormalisée si utile : `parId`, `parClient(id, statut?, page?, taille?)`, `rechercher(critères)`. Bases d'écriture et de lecture séparées : facultatif (écriture normalisée pour les transactions, lecture dénormalisée pour les requêtes).

## 4. Événements de domaine

Servent à mettre à jour les modèles de lecture, à faire communiquer des agrégats, à s'intégrer avec d'autres contextes. Structure : identifiant unique, date de survenue, identifiant d'agrégat, type, charge (`versCharge()`). Exemples : `commande.créée` (commande, client) ; `commande.confirmée` (total, lignes) ; `commande.expédiée` (numéro de suivi, transporteur).

Gestionnaires types : insérer la ligne de lecture à la création (statut brouillon) ; mettre à jour statut, total et date à la confirmation ; envoyer la notification d'expédition (rechercher la commande, ne rien faire si elle est absente, envoyer le gabarit avec suivi et transporteur).

## 5. Événements de domaine ou d'intégration

| | Domaine | Intégration |
|---|---|---|
| Portée | reste dans le contexte délimité | franchit la frontière du contexte |
| Grain | fin (`QuantitéLigneAugmentée`, ancienne et nouvelle valeur) | plus gros |
| Transport | interne | courtier de messages |
| Schéma | langage du domaine | **versionné** (`ventes.commande.confirmée`, version `1.0`) |

Un gestionnaire traduit l'événement de domaine en événement d'intégration : il recharge l'agrégat, construit la charge (commande, client, total, lignes, adresse de livraison ou `rien`), lui donne son propre identifiant et sa date, puis le publie sur le canal du contexte. Les données personnelles de la charge suivent `../donnees-schema.md`.

## 6. Répartiteur d'événements

Un registre `type -> liste de gestionnaires` : `inscrire(type, gestionnaire)`, `répartir(événement)` (tous les gestionnaires du type), `répartirTous(liste)` dans l'ordre. L'inscription se fait au démarrage, avec l'assemblage des adaptateurs.

## 7. Boîte d'envoi transactionnelle

Écrire l'événement dans une table de boîte d'envoi **dans la même transaction** que l'agrégat supprime le problème de double écriture (panne entre la validation en base et la publication : événement perdu).

- Garantie : **au moins une fois**, pas exactement une fois. Le relais peut tomber après la publication et avant le marquage « traité », et republier. Les consommateurs doivent donc être idempotents (§11).
- Relais : soit **scrutation** de la table, soit **lecture du journal de transactions** (capture de changements, outil de type Debezium, à retenir par ADR).

```
message de boîte d'envoi : id ; type ; charge ; crééLe ; traitéLe | rien
gestionnaire PasserCommande :
    transaction(tx) : dépôt.enregistrer(commande, tx) ; pour chaque événement : boîte.enregistrer(e, tx)
relais.traiter() :
    messages = boîte.nonTraités(limite 100, ordre crééLe, verrou en écriture)
    pour chaque message : publier ; marquerTraité(id) ; en cas d'échec : journaliser l'id et réessayer plus tard
```

## 8. Quand utiliser CQRS

CQRS ajoute une complexité forte ; Fowler appelle à la plus grande prudence. La plupart des applications n'en ont pas besoin.

| Utiliser si | S'abstenir si |
|---|---|
| charges de lecture et d'écriture **très** différentes | CRUD simple (cas le plus fréquent) |
| requêtes complexes qui collent mal au modèle de domaine | usages de lecture et d'écriture proches |
| équipes distinctes pour la lecture et l'écriture | petite équipe, domaine simple |
| sourçage d'événements retenu | base de reporting simple pas encore essayée |
| approches simples prouvées insuffisantes | ajout « au cas où » |

Décider par contexte délimité, jamais pour tout le système parce qu'un contexte en profite. Commencer simple : même base, chemins de lecture différents (le service enregistre par le dépôt, lit par le modèle de lecture). Séparer les bases seulement quand le besoin est mesuré.

## 9. Sourçage d'événements

Très difficile à greffer après coup sur un système qui n'a pas été conçu ainsi (Fowler).

- **Pertinent** : piste d'audit complète exigée par le métier ; état à reconstituer à toute date ; domaine événementiel par nature (transactions financières, workflows) ; besoin de comprendre « comment en est-on arrivé là ».
- **À éviter** : CRUD sans exigence d'audit ; équipe peu familière des modèles événementiels ; ajout rétroactif ; aucun besoin de requête temporelle.
- **Exigences** : les événements stockent des écarts, pas l'état final ; instantanés pour reconstruire vite ; pendant un rejeu, couper les notifications et mettre en cache, horodatés, les résultats des systèmes externes ; stratégie de versionnement des schémas, car un événement est éternel.

## 10. Saga

Pour un workflow qui traverse plusieurs agrégats, une saga plutôt qu'une coordination par événements bruts. Exemple : réserver le stock, encaisser le paiement, confirmer la commande, avec une action de compensation pour chaque étape si une suivante échoue.

- **Chorégraphie** : chaque service écoute et publie ; plus simple, plus dur à suivre.
- **Orchestration** : un coordinateur pilote les étapes ; explicite, plus facile à déboguer.

Le workflow et ses compensations se décrivent aussi côté fonctionnel (`maquettes-parcours/references/workflows-fonctionnels.md`).

## 11. Consommateur idempotent

**Obligatoire** : courtiers et relais livrent au moins une fois, chaque consommateur doit tolérer les doublons.

```
gérer(événement) :
    transaction(tx) :
        si non tx.messagesTraités.insérerSiAbsent(événement.id) : retour    # doublon déjà traité
        faireLeTravail(événement, tx)
```

La trace de déduplication et le travail se valident **dans la même transaction**. Un ensemble en mémoire ou une écriture séparée réintroduit la course (panne après le travail, avant l'enregistrement de l'identifiant : travail fait deux fois). Autres options : déduplication du courtier (souvent limitée dans le temps) ; gestionnaires idempotents par nature (insertion-ou-mise-à-jour, gardes d'état).

## 12. Contrôles avant de rendre

- CQRS, saga ou sourçage d'événements : une ADR qui cite le besoin mesuré.
- Tout événement vers un autre service passe par la boîte d'envoi ; tout consommateur est idempotent, avec un test de doublon.
- Événements d'intégration versionnés ; données personnelles minimisées.
