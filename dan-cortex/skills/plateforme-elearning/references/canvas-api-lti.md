# Canvas LMS : API REST, LTI, SSO, import, événements

Méthode réécrite à partir de la documentation du dépôt (dossiers `doc/api` et `doc/lti`, commit 1c9f0bb). Les faits (noms de points d'accès, paramètres, en-têtes) sont cités ; la rédaction est la nôtre. Sur une instance hébergée par Instructure, certaines règles diffèrent : **à revérifier** en ligne.

## 1. API REST : principes généraux

- HTTPS uniquement, sur le domaine de l'instance (`/api/v1/...`), réponses en JSON, dates ISO 8601 en UTC. Un appel en HTTP est redirigé, mais le secret a déjà circulé en clair.
- Identifiants entiers sur 64 bits : demander des chaînes avec l'en-tête d'acceptation dédié (erreurs d'arrondi en JavaScript).
- Un objet peut être désigné par son identifiant interne ou par son identifiant SIS avec préfixe (`sis_course_id:`). Coder ces identifiants en UTF-8 puis en pourcentage ; les serveurs intermédiaires doivent laisser passer les barres obliques codées.
- GraphQL (`/api/graphql`) existe ; couverture partielle, mêmes droits.

## 2. Authentification et jetons

| Cas | Méthode |
|---|---|
| Essai personnel d'un développeur | jeton généré à la main depuis son profil ; il ne s'affiche qu'une fois ; équivaut à un mot de passe |
| Application utilisée par plusieurs personnes | OAuth2 « code d'autorisation » : redirection vers `login/oauth2/auth`, retour d'un code, échange sur `login/oauth2/token` |
| Services LTI Advantage | OAuth2 « client credentials » avec assertion signée (voir section 4) |
| Outil d'administration agissant pour un utilisateur | paramètre d'imitation `as_user_id` (droit « devenir un autre utilisateur » requis, appel journalisé avec les deux identités) |

Règles retenues :
- Les clés (identifiant et secret client) s'appellent **clés de développeur** et se créent par l'administrateur du compte racine ou du site.
- Les jetons des clés récentes durent **une heure** ; le jeton de rafraîchissement (inchangé) en obtient un nouveau sans nouvel accord.
- Envoyer le jeton dans l'en-tête `Authorization: Bearer`, jamais dans l'adresse (journaux, historiques).
- Un 401 accompagné de l'en-tête d'authentification signifie jeton expiré ou supprimé : refaire le flux. Sans cet en-tête, il s'agit d'un droit manquant.
- La politique d'API d'Instructure interdit de faire générer un jeton à la main par des tiers (à revérifier en auto-hébergement).

**Portées (scopes).** Une clé peut être limitée à une liste de points d'accès. Une portée a la forme `url:<verbe>|<chemin>`. Les portées demandées doivent être un sous-ensemble de celles de la clé ; retirer une portée invalide les jetons existants ; en ajouter n'élargit pas les anciens jetons. Environ 110 portées tiennent dans une demande (limite de taille d'en-tête) : au-delà, scinder. Principe : une clé par intégration, portées minimales.

## 3. Pagination et limites de débit

- Par défaut, 10 éléments par page ; `per_page` demande plus, avec un plafond non documenté. **Toujours suivre l'en-tête `Link`** et jamais construire les adresses de page soi-même.
- `Link` contient des adresses absolues opaques avec les relations `current`, `next`, `prev`, `first`, `last` (selon le cas ; `last` peut manquer si le total est coûteux à calculer). Lire l'en-tête sans tenir compte de la casse. Si le jeton était passé dans l'adresse, il doit être rajouté.
- Limitation de débit : chaque requête a un coût qui s'ôte d'un quota se reconstituant dans le temps. L'en-tête `X-Request-Cost` donne le coût, `X-Rate-Limit-Remaining` le quota restant. En cas de dépassement, la réponse est un 429 : l'application doit attendre et réessayer. Les requêtes parallèles subissent une pénalité préalable ; chaque jeton a son quota.
- Connecteur type : file de requêtes, un seul appel à la fois, recul sur 429, lecture de `Link`, reprise idempotente.

## 4. LTI : brancher un outil

LTI est une norme de 1EdTech (ex-IMS) pour lancer un outil externe dans la plateforme. Canvas décrit quatre vocables : outil, plateforme, lancement (souvent dans un cadre intégré), emplacement (endroit de l'interface où le lien apparaît).

Versions : la 1.1 (signature OAuth 1) et la 2.0 sont signalées comme dépréciées ; la 1.3 est la version courante et le choix par défaut. La 2.0 n'a plus qu'un usage cité : la plateforme anti-plagiat.

**Flux LTI 1.3** (OpenID Connect) : la plateforme appelle l'adresse d'initiation de l'outil (émetteur `iss`, `login_hint`, `target_link_uri`, `client_id`, `deployment_id`) ; l'outil renvoie une demande d'authentification vers le point d'autorisation de la plateforme ; la plateforme répond par un jeton JWT signé que l'outil valide avec les clés publiques de la plateforme. Sur une instance auto-hébergée, l'émetteur est la valeur de `lti_iss` dans `security.yml`, à fixer sur votre nom d'hôte.

**Installation**, deux voies :
1. Enregistrement dynamique : l'administrateur colle l'adresse d'enregistrement de l'outil ; l'outil lit la configuration OpenID de la plateforme et s'installe lui-même.
2. Manuelle : créer une clé de développeur de type LTI, y coller (ou pointer par adresse) la configuration JSON de l'outil (emplacements, adresses de redirection, clé publique JWK avec `alg` et `use`), noter l'identifiant de clé (c'est le `client_id`), puis déployer l'outil dans le compte ou le cours choisi par cet identifiant.

**Services LTI Advantage** : annuaire des participants (NRPS), notes (AGS : lignes de notes, scores, résultats), liens profonds (l'enseignant choisit un contenu dans l'outil, qui le renvoie à la plateforme). Authentification par jeton obtenu avec une assertion signée par la clé privée de l'outil ; il n'agit que dans le contexte où il est déployé. Un service de notification de plateforme permet des avis serveur à serveur.

**Niveau de confidentialité** : par outil, `anonymous` (rien d'identifiant), `name_only`, `email_only`, `public`. Il filtre les données envoyées au lancement et à l'annuaire. Règle : partir de `anonymous`, ne monter que pour une finalité inscrite au registre des traitements.

Les cookies tiers étant bloqués par les navigateurs, une norme de stockage côté plateforme sécurise les lancements.

## 5. SSO et comptes

Canvas gère : compte local, SAML, CAS, LDAP, OpenID Connect et plusieurs fournisseurs sociaux. Pour un organisme, retenir un seul fournisseur d'identité, déclarer identifiant de connexion et identifiant SIS, prévoir les comptes sans courriel (mineurs). SAML demande une identité d'entité et, pour chiffrer les assertions, une paire de clés. Activation par l'interface : à revérifier.

## 6. Provisionnement, import et notes

- **SIS** : import CSV (utilisateurs, cours, inscriptions), zippé, via l'administration ou l'API. Le mode « lot complet » supprime ce qui manque dans le fichier pour un trimestre : toujours fixer un seuil de changement (`change_threshold`) pour que le lot s'arrête s'il supprime trop.
- **Contenu de cours** : l'API de migration de contenu accepte les types suivants : cartouche Canvas, Common Cartridge, copie de cours, zip de fichiers, QTI (quiz) et convertisseur Moodle. Le fichier se dépose en trois étapes (déclaration, envoi, suivi de la redirection) ; l'import démarre à la fin de l'envoi.

## 7. Événements

Canvas émet des événements en direct (note modifiée, devoir rendu, connexion, quiz soumis, progression), aussi au format Caliper. Livraison par file SQS ou webhook HTTPS (charge utile signée en option) via un service d'abonnements ; la documentation du code décrit un flux Kinesis. Le flux est partiel et différé : pour des données à jour, interroger l'API. Disponibilité en auto-hébergement : **à revérifier**.

## 8. Données d'apprenants

Cartographier ce qui quitte Canvas (LTI, API, événements, courriels), vers quels tiers, sur quelle base légale. Mineurs, conservation, accès, effacement et export : `delegue-protection-donnees` et `juridique-conformite`. Les capacités d'export et de suppression de Canvas ne figurent pas dans les documents lus : **à revérifier**.
