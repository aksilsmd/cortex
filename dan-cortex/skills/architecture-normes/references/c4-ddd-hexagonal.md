# Vues C4 approfondies, choix du gabarit d'ADR, DDD et architecture hexagonale

Approfondit la section « Vues C4 » et le gabarit d'ADR de `dossier-architecture-adr.md`, et complète `styles-architecture.md`. Lecture à la demande : la section utile seulement. Le rendu Mermaid des vues C4 est décrit dans `maquettes-parcours/references/schemas-mermaid.md`.

## Sommaire
1. C4 : règles communes
2. C4 niveau par niveau
3. Vues complémentaires
4. Choisir le gabarit d'une ADR
5. DDD stratégique
6. DDD tactique
7. Architecture hexagonale (ports et adaptateurs)
8. Quand ne pas appliquer DDD ni hexagonal
9. Contrôles avant de rendre
10. Origine

## 1. C4 : règles communes

- Un diagramme = un niveau de zoom = un public. Ne jamais mélanger conteneurs et composants sur la même vue.
- Chaque vue a un titre, une légende (formes, couleurs, traits) et une date ou une version.
- Chaque élément porte : nom, type (personne, système, conteneur, composant), technologie (dès le niveau 2), responsabilité en une phrase.
- Chaque relation porte un verbe orienté (« envoie la commande à ») et, dès le niveau 2, le protocole (HTTPS/JSON, SQL, AMQP, SMTP).
- Les frontières de confiance et les systèmes externes sont visibles ; `architecte-securite` les valide.
- Au plus une vingtaine d'éléments par vue ; au-delà, découper.
- La vue se contrôle contre le code ou le déploiement réel : un conteneur dessiné qui n'existe pas est un défaut.

## 2. C4 niveau par niveau

| Niveau | Question | Éléments | Ce qu'on n'y met pas | Quand le produire |
|---|---|---|---|---|
| 1 Contexte | qui utilise le système et avec quoi échange-t-il ? | personnes, système étudié, systèmes externes | technologies, bases, protocoles détaillés | toujours, dès J1 |
| 2 Conteneurs | quelles unités s'exécutent ou stockent séparément ? | applications web, mobiles, API, tâches planifiées, bases, files, stockage objet | classes, modules internes | toujours, dès J3 |
| 3 Composants | comment un conteneur est-il découpé ? | modules, services internes, ports, adaptateurs, avec leurs dépendances | détails de déploiement | pour les conteneurs complexes ou risqués seulement |
| 4 Code | comment un composant est-il implémenté ? | classes, interfaces, tables | — | rarement ; généré par un outil si besoin |

**Méthode de production** : partir du niveau 1 avec le cahier des charges ; dériver le niveau 2 des exigences non fonctionnelles (disponibilité, hébergement, sécurité) ; ne descendre au niveau 3 que là où une décision ou un risque l'exige. Pour un système existant, procéder à l'inverse : lire le code (dossiers, points d'entrée, configuration de déploiement), en tirer composants puis conteneurs, puis le contexte, et signaler les écarts avec la documentation.

## 3. Vues complémentaires

| Vue | Montre | Usage |
|---|---|---|
| Paysage | plusieurs systèmes d'une même organisation | ERP, boutique, outils internes |
| Dynamique | un scénario numéroté sur une vue statique | parcours critique (commande, paiement) |
| Déploiement | conteneurs placés sur nœuds, environnements, réseau | hébergement, sauvegarde, zones |

## 4. Choisir le gabarit d'une ADR

Le gabarit de `dossier-architecture-adr.md` reste la règle. Ce tableau aide à l'alléger ou à l'enrichir selon l'enjeu. Formes d'origine : forme courte de Michael Nygard (2011), forme complète de Jeff Tyree et Art Akerman (2005), forme à options de MADR (Markdown Architectural Decision Records, Oliver Kopp et coll.) :

| Situation | Forme recommandée |
|---|---|
| Décision locale, réversible, peu d'options | forme courte : contexte, décision, conséquences |
| Choix entre plusieurs options comparables | forme avec options pondérées, avantages et inconvénients de chacune, options écartées |
| Décision lourde, coûteuse à défaire, plusieurs parties prenantes | forme complète : hypothèses, contraintes, positions, implications, décisions liées, coût de sortie |
| Décision à justification économique | ajouter coûts, bénéfices et seuil de rentabilité (skill `budget-finance`) |
| Décision imposée par une contrainte externe (loi, client) | forme courte, avec la source de la contrainte en tête |

Règles transverses : une décision par ADR ; on écrit l'ADR quand la décision est prise, pas après coup ; une ADR acceptée ne se réécrit pas, une nouvelle la remplace et le lien est tracé dans les deux sens ; statut toujours visible (proposée, acceptée, remplacée, abandonnée). Mérite une ADR une décision qui touche la structure, une interface, une dépendance majeure, un attribut de qualité, ou qui serait coûteuse à défaire.

## 5. DDD stratégique

- **Langage omniprésent** : un glossaire par contexte, employé tel quel dans les spécifications, le code, les tests et les écrans. Deux sens pour un mot = deux contextes, ou un mot à renommer.
- **Sous-domaines** : cœur (ce qui distingue le produit, construit avec soin), support (nécessaire, spécifique, construit simplement), générique (acheté ou repris : authentification, paiement, envoi de SMS).
- **Contextes délimités** : frontière dans laquelle un modèle et son langage sont cohérents. Signes d'une frontière : vocabulaire qui change, équipe ou rythme différents, règles qui se contredisent.
- **Carte des contextes** : relations entre contextes, chacune nommée : partenariat, noyau partagé (à limiter), client-fournisseur, conformiste, couche anticorruption (traduire un modèle externe pour ne pas le subir), service ouvert avec langage publié.

Exemple Parapro (hypothèse d'illustration) : contextes Catalogue, Commande, Paiement, Livraison, Back-office ERP ; le prestataire de paiement et la passerelle SMS sont derrière une couche anticorruption.

## 6. DDD tactique

| Brique | Rôle | Règle |
|---|---|---|
| Entité | objet à identité durable | égalité par identifiant |
| Objet-valeur | concept défini par ses valeurs (montant, adresse, quantité) | immuable, égalité par valeur, valide dès sa création |
| Agrégat | grappe d'objets modifiés ensemble, avec une racine | une transaction = un agrégat ; les autres agrégats sont référencés par identifiant ; invariants vérifiés par la racine |
| Événement de domaine | fait passé qui intéresse d'autres parties (« commande validée ») | nommé au passé, immuable ; cohérence à terme entre agrégats |
| Dépôt | accès à la persistance d'un agrégat | un par racine d'agrégat ; interface dans le domaine |
| Service de domaine | règle qui n'appartient à aucune entité | sans état |
| Service d'application | orchestre un cas d'usage | ne contient pas de règle métier |

Pièges : agrégat trop gros (contention, verrous) ; modèle anémique (données sans comportement, règles dispersées dans les services) ; objets-valeurs remplacés par des types primitifs.

## 7. Architecture hexagonale (ports et adaptateurs)

- **Domaine au centre**, sans dépendance vers les frameworks, la base ou le réseau.
- **Ports** : interfaces définies par le domaine ou l'application. Ports entrants (cas d'usage offerts) ; ports sortants (besoins : dépôt, envoi de SMS, paiement, horloge).
- **Adaptateurs** : implémentations à l'extérieur. Entrants : contrôleur HTTP, interface en ligne de commande, consommateur de file. Sortants : dépôt SQL, client du prestataire de paiement.
- **Règle de dépendance** : les dépendances du code pointent toujours vers le centre ; l'assemblage se fait au démarrage (injection).
- **Tests** : domaine testé sans infrastructure ; adaptateurs testés en intégration contre la vraie technologie (conteneur de base de test) ; un adaptateur factice par port sortant pour les tests d'application.
- **Contrôle automatique** : une règle d'architecture (analyse des imports) interdit au domaine d'importer l'infrastructure ; à placer dans les contrôles de `normes-developpement.md`.

Structure type : `domaine/` (entités, objets-valeurs, événements, ports sortants), `application/` (cas d'usage, ports entrants), `adaptateurs/entrants/`, `adaptateurs/sortants/`, `demarrage/`.

Détail (agrégats, ports, CQRS, boîte d'envoi, sagas) : `ddd-hexagonal/vue-ensemble.md`.

## 8. Quand ne pas appliquer DDD ni hexagonal

- Application essentiellement de saisie et de consultation (CRUD) sans règles riches : couches simples suffisent.
- Prototype jetable, script, outil interne à courte durée de vie.
- Équipe ou agents sans temps pour tenir le langage commun : le coût dépasse le gain.

Le choix se trace par une ADR, avec ce critère : le gain attendu (règles métier isolées, testabilité, remplacement d'un prestataire) doit justifier la structure supplémentaire.

## 9. Contrôles avant de rendre

- Vues 1 et 2 présentes, légendées, contrôlées contre le code ou le déploiement.
- Chaque relation a un verbe et, au niveau 2, un protocole.
- Chaque contexte délimité a son glossaire ; la carte des contextes nomme chaque relation.
- Si hexagonal : règle de dépendance contrôlée par un outil, pas seulement décrite.

## 10. Origine

Méthode reformulée en français pour Dan-Cortex ; aucun texte copié. Idées inspirées de :
- `wshobson/agents` (MIT, © 2024 Seth Hobson), plugin `c4-architecture` (approche de bas en haut par niveau) — https://github.com/wshobson/agents, commit `7e2fb55`. Agents non repris.
- `softaworks/agent-toolkit` (MIT, © 2026 Leonardo Flores), skill `c4-architecture` — https://github.com/softaworks/agent-toolkit, commit `3027f20`.
- `ccheney/robust-skills` (MIT, © 2026 robust-skills contributors), skill `clean-ddd-hexagonal` — https://github.com/ccheney/robust-skills, commit `0eea7b0`.
- Choix du gabarit d'ADR : **idées seulement**, sans texte repris, d'après `architecture-decision-record/architecture-decision-record` (CC BY-NC-SA) — https://github.com/architecture-decision-record/architecture-decision-record, commit `86893bc`.
- Détail : `sources/renfort-github.md`. Décision d'origine : réunion « renfort GitHub » du 2026-11-03 (projet Parapro, DEC-042).
