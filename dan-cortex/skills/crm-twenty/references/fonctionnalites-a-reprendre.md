# Reprendre les fonctionnalités d'un CRM sans le déployer

À utiliser quand le produit (e-commerce, ERP, back-office) contient déjà les données clients. Ajouter un CRM séparé créerait une double saisie, une synchronisation à maintenir, un serveur de plus à sécuriser et une copie supplémentaire de données personnelles. On reprend alors dans le produit les fonctionnalités qui font la valeur d'un CRM, sur le modèle de Twenty, sans en copier le code ni le texte.

## Grille de décision

| Question | Si oui | Si non |
|---|---|---|
| Les données clients vivent-elles déjà dans le produit ? | reprise native (ce document) | évaluer le déploiement (`SKILL.md`, §1 et §2) |
| Plusieurs équipes commerciales, prospection hors clients existants ? | évaluer le déploiement | reprise native |
| Besoin de synchroniser messageries et agendas ? | évaluer le déploiement | reprise native |

## Fonctionnalités à reprendre (par valeur décroissante)

1. **Fiche client unique** : identité, statut, commandes, encours et échéances, devis, retours, notes, tâches, sur une seule vue maître-détail.
2. **Chronologie** : événements datés du client, lus depuis le journal existant, sans nouvelle donnée sensible.
3. **Tâches liées** à un client, une commande ou une créance, avec échéance, visibles sur la fiche et dans la liste personnelle.
4. **Relances à règles fixes**, activables une par une : créance échue, demande en attente, commande non retirée. Pas d'éditeur de workflow avec exécution de code : c'est la leçon de la CVE-2026-26720 de Twenty.
5. **Notes multiples** horodatées, avec auteur et un rappel des données interdites (santé, mots de passe).
6. **Suivi en colonnes** (kanban) des demandes et des propositions, avec motif obligatoire au refus.
7. **Vues enregistrées** : filtres sauvegardés par utilisateur.
8. **Import CSV** de la clientèle existante : aperçu, détection des doublons, rapport d'erreurs.

## Fonctionnalités à écarter par défaut

- Synchronisation des messageries et des agendas.
- Objets et champs créés par l'utilisateur.
- Agents d'IA et accès par MCP, tant qu'ils ne sont pas validés par le juriste et le délégué à la protection des données.
- Place de marché d'applications.

## Règles communes

- **Droits** : par rôle, avec journal avant/après sur chaque modification.
- **Données** :
  - aucune donnée de santé dans les notes ni dans la chronologie ;
  - en pharmacie ou en parapharmacie, l'historique d'achats est réservé aux rôles qui en ont besoin ;
  - les relances commerciales exigent un consentement ; les relances de paiement contractuelles n'en exigent pas.
- **Livraison** : chaque fonctionnalité retenue entre au carnet de demandes, avec sa priorité, son lot et sa trace vers la carte des fonctionnalités.

## Origine

Fonctionnalités observées sur Twenty (https://github.com/twentyhq/twenty, AGPL-3.0) et reformulées en français (forme A), sans texte copié. Voir `sources/renfort-github.md`.
