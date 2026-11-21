# Sources du skill plateforme-elearning

| Élément | Valeur |
|---|---|
| Dépôt | Instructure, canvas-lms (clone local `/home/claude/ext/instructure_canvas-lms`) |
| Licence | GNU Affero General Public License version 3 (fichier LICENSE, texte standard ; fichier COPYRIGHT : notice Instructure, sans exception ajoutée) |
| Commit lu | 1c9f0bb8013ed69c4f2efe11fd483025469b7e6c |
| Forme | **A stricte** : méthode réécrite, aucun texte ni code recopié. Seuls des faits (noms de paramètres, d'en-têtes, de fichiers, versions) sont cités. |
| Date de référence | 21 novembre 2026 |

## Ce qui a été lu et retenu

- `README.md` : nature du projet, licence, renvoi des procédures d'installation vers le wiki (non présent dans le clone).
- `LICENSE`, `COPYRIGHT` : AGPL-3.0, article 13 (interaction réseau) ; aucune exception.
- `Gemfile`, `Dockerfile`, `.nvmrc`, `package.json`, `docker-compose.yml`, image PostgreSQL de développement : Rails 8.0, Ruby 3.4, Node 20, Yarn 1.x, PostgreSQL 14 (développement), Redis.
- `config/*.example` : liste et rôle des fichiers de configuration (base, domaine, sécurité, Redis, stockage, courrier, tâches, SAML, paramètres dynamiques).
- `app/models/authentication_provider/` : fournisseurs d'authentification disponibles.
- `app/controllers/content_migrations_controller.rb` (documentation en commentaires) : types de migration de contenu.
- `doc/api/` : README, oauth, developer_keys, pagination, throttling, object_ids, masquerading, file_uploads, sis_csv, graphql, provisioning, registration, lti_dev_key_config, lti_launch_overview, canvas_roles, pns, xapi, data_services, changelog.
- `doc/lti/` : vue d'ensemble, installation des outils, lancements, liens profonds, niveau de confidentialité, stockage de plateforme.
- `doc/live_events.md` : flux d'événements en direct.
- `SECURITY.md` : politique de signalement de vulnérabilités.

## Non repris

- Les cinq skills internes de `.claude/skills` (create_commit_msg, ketchup, rspec, squash-migrations, update-gems) sont propres au développement de Canvas lui-même. Ils ne sont pas repris, pas plus que l'agent et la commande de ce même dossier.
- Les dossiers de développement et de test (Jenkins, Selenium, profilage, i18n, interface React) : hors sujet pour l'usage d'une plateforme.
- Le code source de l'application.

## Points à revérifier (non documentés dans les fichiers lus)

- Procédure de production officielle (wiki du projet) et versions minimales supportées de PostgreSQL et Redis en production.
- Calendrier de support et de publication des versions.
- Disponibilité des événements en direct hors du service hébergé.
- Capacités d'export et de suppression de données personnelles.
- Usage de la marque Canvas dans une offre tierce.
- Politique d'API d'Instructure pour les instances auto-hébergées.
- Offres, prix et conditions de l'hébergement par Instructure.
- Toute information sur Moodle et Open edX (non étudiés ici).
