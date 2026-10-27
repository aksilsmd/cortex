# Styles d'architecture, API, messagerie et évaluation

Comment passer d'exigences chiffrées à un style d'architecture, des interfaces et une messagerie, puis comment évaluer le résultat avant de s'engager.

## Sommaire
1. Attributs de qualité et scénarios
2. Choisir le style
3. Styles d'API
4. Messagerie
5. Évaluer l'architecture
6. Anti-modèles

## 1. Attributs de qualité et scénarios

ISO/IEC 25010:2023 (2e édition) fixe le vocabulaire : adéquation fonctionnelle, efficacité de performance, compatibilité, capacité d'interaction, fiabilité, sécurité, maintenabilité, flexibilité, sûreté. Depuis 2011, la sûreté est ajoutée, l'utilisabilité devient capacité d'interaction (accessibilité incluse), la portabilité devient flexibilité. Traiter explicitement sûreté et capacité d'interaction.

Écrire chaque exigence comme un **scénario** : stimulus, contexte, réponse, mesure. Exemple fictif : « Un jour de promotion (contexte), 2 000 commandes par minute (stimulus) : 95 % des paiements confirmés en moins de 3 secondes (mesure) ». Sans mesure, le scénario n'est pas testable : le renvoyer à `expert-cahier-des-charges`.

Construire l'**arbre d'utilité** : les caractéristiques en racine, un à trois scénarios par feuille, chacun noté par importance pour le métier et difficulté technique (haute, moyenne, basse). Les scénarios « haute importance, haute difficulté » dictent le style.

## 2. Choisir le style

| Contexte | Style | Condition d'usage |
|---|---|---|
| Défaut, une équipe ou quelques-unes | monolithe modulaire, modules par sous-domaine | frontières vérifiées automatiquement |
| Équipes autonomes nombreuses, scalabilité indépendante démontrée, livraison continue mûre | microservices | observabilité, CI/CD et culture DevOps déjà là |
| Migration d'un existant | Strangler Fig : remplacer morceau par morceau | routage progressif et retour arrière |
| Contexte borné à lecture et écriture très différentes | CQRS, éventuellement event sourcing | uniquement ce contexte, jamais le système entier |
| Plusieurs clients aux besoins divergents (web, mobile) | un BFF par client | sinon, un seul back-end |
| Plusieurs équipes sur une même interface web | micro-frontends | intégration à l'exécution, pas au build |
| Code, hexagonal ou en couches | ports et adaptateurs autour du domaine | combine bien avec le monolithe modulaire (synthèse) |

Fowler : la plupart des systèmes devraient être un monolithe unique ; les microservices apportent déploiement indépendant et diversité technique, au prix de la distribution, de la cohérence à terme et de l'exploitation. Shopify (2020) a découpé un monolithe de ~2,8 M de lignes en 37 composants plutôt qu'en services. Le choix est une décision de type 1 : ADR et comité.

Modèle de locataires (SaaS, ERP multi-sociétés) : partagé (économique, isolation faible, voisin bruyant), base ou schéma par locataire, mono-locataire (isolation forte, coûteux). Critères : nombre de clients, conformité, capacité d'exploitation. Mise en œuvre : `references/donnees-schema.md`.

## 3. Styles d'API

| Besoin | Choix | Précaution |
|---|---|---|
| API publique ou partenaires | REST décrit en OpenAPI 3.x (3.2 : événements SSE, méthode QUERY) | contrat avant code, versionné |
| Clients multiples, besoins de données variables | GraphQL (synthèse) | limites de profondeur et de coût |
| Appels internes entre services | gRPC (synthèse) | schémas partagés versionnés |
| Monorepo entièrement TypeScript | tRPC (synthèse) | couplage fort assumé |
| Notifier un tiers | webhooks signés, idempotents, avec reprise | clé d'idempotence |
| Événements | AsyncAPI | un schéma par message |

Les critères GraphQL, gRPC, tRPC et AsyncAPI n'ont pas été lus à la source : à vérifier avant décision. Décrire toute API dans un contrat exploitable par les outils de test ; règle de compatibilité écrite (ajout permis, suppression par expand, migrate, contract).

## 4. Messagerie

| Besoin | Choix (synthèse) |
|---|---|
| Journal rejouable, fort débit, plusieurs consommateurs | Kafka (4.3.1, juin 2026 ; trois versions par an) |
| Routage fin, files de travail | RabbitMQ |
| Messagerie légère, faible latence | NATS |
| Une file managée suffit | SQS ou équivalent du fournisseur |
| Moins de quelques milliers de tâches par jour | table de tâches dans la base principale |

Imposer : messages versionnés, consommateurs idempotents, file des messages morts surveillée, ordre garanti seulement par clé. Ne pas ajouter de broker sans besoin mesuré. Critères RabbitMQ, NATS, SQS : à vérifier.

## 5. Évaluer l'architecture

Avant l'engagement, pas après.

1. Présenter l'architecture candidate et l'arbre d'utilité.
2. Dérouler chaque scénario prioritaire contre l'architecture.
3. Consigner : **risques**, **non-risques**, **points de sensibilité** (un paramètre dont dépend une qualité), **compromis** (une décision qui améliore une qualité en dégradant une autre). Méthode ATAM du SEI ; étapes complètes à vérifier.
4. Transformer les risques en actions au registre et en ADR mises à jour.

Les **fitness functions** surveillent ensuite l'intégrité : règles de dépendances, budgets de performance, absence de cycle entre modules, exécutés en intégration continue. Ce sont les capteurs de retour qui encadrent aussi les agents de code (Thoughtworks Radar 34).

## 6. Anti-modèles

| Anti-modèle | Signal | Remède |
|---|---|---|
| Monolithe distribué | services qui se déploient ensemble | revenir au monolithe modulaire |
| Microservices prématurés | plus de services que d'équipes | fusionner |
| CQRS ou event sourcing généralisé | partout, sans besoin d'audit ou de relecture | limiter à un contexte |
| Base partagée entre services | deux services écrivent la même table | une base par propriétaire |
| Architecture par la mode | justification : « tout le monde le fait » | exiger un scénario mesuré |
| Pas de décision écrite | contexte « dans la tête des gens » (61 % des répondants SO 2026) | une ADR par choix |
| Micro-frontends au build | bundles dupliqués, gouvernance lourde | intégration à l'exécution |

## Contrôles avant de rendre

Chaque scénario est mesurable ; le style est relié à des scénarios ; toute exception au monolithe est justifiée ; chaque interface a un contrat ; risques et compromis sont au registre.

## Sources

- ISO/IEC 25010:2023 : https://www.iso.org/standard/78176.html
- SEI, ATAM : https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/
- Fowler, Microservice Premium : https://martinfowler.com/bliki/MicroservicePremium.html
- Fowler, CQRS : https://martinfowler.com/bliki/CQRS.html
- Microsoft, BFF et tenancy : https://learn.microsoft.com/en-us/azure/architecture/patterns/backends-for-frontends
- Shopify, monolithe modulaire : https://shopify.engineering/shopify-monolith
- Evolutionary Architectures : https://evolutionaryarchitecture.com/precis.html
