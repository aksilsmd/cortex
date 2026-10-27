# Tests de sécurité complets

Plan de tests fondé sur l'OWASP ASVS 5.0.0, du plan jusqu'au rapport. Il couvre le code, les dépendances, les secrets, la configuration et l'application en fonctionnement, au niveau des catégories de vérification.

## Sommaire
- Méthode
- Familles de contrôles
- Matrice des autorisations
- Configuration
- Environnement, comptes et données de test
- Gabarit `plan-tests-securite.md`
- Gabarit `rapport-securite.md`
- Pièges et contrôles
- Sources

## Méthode

1. Reprendre le niveau ASVS signé (`analyse-risques-menaces.md`) et le modèle de menaces.
2. Pour chaque famille ci-dessous, retenir les chapitres applicables au projet, et écrire pour les autres « non applicable » avec le motif.
3. Écrire chaque test comme une vérification : ce qu'on contrôle, ce qu'on attend, la preuve. Pas de mode opératoire d'attaque.
4. Faire jouer d'abord les contrôles automatisés (`devsecops.md`), puis les vérifications ciblées à la main sur ce que les outils voient mal : autorisations, logique métier, flux de paiement.
5. Consigner chaque constat au registre avec sa gravité (CVSS 4.0, groupe indiqué), une preuve non exploitable (capture, extrait de journal, identifiant de règle) et une recommandation.
6. Faire corriger, puis contre-tester. Clore avec preuve.

Les tests se jouent sur l'environnement de recette du projet. Jamais sur un système tiers ; la production seulement avec accord explicite écrit et lecture seule.

## Familles de contrôles

Les catégories suivent les chapitres de l'ASVS 5.0.0 (17 chapitres, intitulés et numérotation à reprendre de la norme) et l'OWASP Top 10:2025.

| Famille | Ce qu'on vérifie | Principales catégories associées |
|---|---|---|
| Contrôle d'accès | chaque objet et chaque fonction vérifie le droit de l'appelant côté serveur | A01 |
| Authentification et sessions | MFA, récupération de compte, verrouillage, durée et invalidation des sessions, jetons | A07 |
| Validation, encodage, injection | entrées validées, sorties encodées, requêtes paramétrées | A05 |
| Conception et logique métier | limites de débit, enchaînements interdits, abus de fonctionnalité | A06 |
| Cryptographie et données | algorithmes, gestion de clés, données sensibles non exposées | A04 |
| Configuration et déploiement | en-têtes, erreurs, comptes par défaut, ports, versions | A02 |
| Chaîne d'approvisionnement | dépendances, SBOM, intégrité des mises à jour | A03, A08 |
| Journalisation et alertes | événements de sécurité journalisés, alertes, pas de donnée sensible dans les journaux | A09 |
| Gestion des erreurs | échec sûr (fermeture par défaut), messages non verbeux | A10 |
| API | inventaire à jour, autorisation par objet et par fonction, quotas | API Security Top 10 2023 (à vérifier) |
| Mobile | stockage local, communications, protection du binaire | MASVS et MASTG (versions à vérifier) |
| IA et agents | actions bornées et journalisées, entrées non maîtrisées, droits minimaux | Top 10 LLM et Agentic (édition à vérifier) |
| Vie privée | minimisation, consentement technique, durées de conservation | LINDDUN, à croiser avec le pôle Juridique |

## Matrice des autorisations

C'est le test le plus rentable : le contrôle d'accès est la première catégorie du Top 10:2025. Construire une matrice rôle × ressource × action :

| ID | Ressource et action | Anonyme | Utilisateur | Autre utilisateur | Administrateur | Résultat attendu | Résultat observé |
|---|---|---|---|---|---|---|---|

- Un identifiant `SEC-` par ligne ; les rôles viennent de la SFD.
- Chaque cellule dit « autorisé » ou « refusé » avec le code de réponse attendu.
- Tester les trois dimensions : horizontale (autre utilisateur du même rôle), verticale (rôle supérieur), contexte (locataire d'un autre client en SaaS).
- Disposer de comptes de chaque rôle et d'au moins deux comptes par rôle.
- Chaque ligne « refusé » devient un cas de recette `CT-` : le concepteur de tests la reprend.

## Configuration

Vérifier en liste, par scan et par revue : en-têtes de sécurité du navigateur, politique de cookies de session, TLS (versions, certificats), pages d'erreur sans détails techniques, comptes et mots de passe par défaut absents, interfaces d'administration non exposées, listes de répertoires désactivées, versions affichées masquées, CORS restreint, stockages non publics, durcissement CIS mesuré, ports ouverts conformes à l'architecture, journalisation active.

## Environnement, comptes et données de test

- Environnement de recette distinct de la production, données fictives ou anonymisées.
- Comptes de test par rôle, créés pour l'occasion et supprimés après.
- Fenêtre convenue, contact d'urgence, procédure d'arrêt.
- Pour une API : spécification OpenAPI à jour ; pour du mobile : build de test.

## Gabarit `plan-tests-securite.md`

```markdown
# Plan de tests de sécurité

## Synthèse
(niveau ASVS, nombre de familles, de contrôles, de lignes de matrice, environnement, calendrier, prestataire éventuel)

## Périmètre et environnement
## Niveau de vérification et référentiels
## Contrôles par famille
| ID | Famille | Chapitre de la norme | Vérification | Menace du modèle | Méthode (auto, manuelle) | Preuve | Jalon |
|---|---|---|---|---|---|---|---|
## Matrice des autorisations
## Contrôles de configuration
## Comptes et données de test
## Critères de réussite et seuils de blocage
## Calendrier et responsabilités
```

## Gabarit `rapport-securite.md`

```markdown
# Rapport de tests de sécurité

## Synthèse
(périmètre, date, niveau visé, résultat par famille, constats par gravité, bloquants, décision recommandée)

## Périmètre, méthode, outils et versions
## Couverture : familles testées, non testées et pourquoi
## Constats
| ID AUD | Famille | Gravité (CVSS 4.0, groupe) | Description | Preuve | Recommandation | Responsable | Statut |
|---|---|---|---|---|---|---|---|
## Matrice des autorisations : résultat observé
## Contre-tests : constat, date, preuve de clôture
## Limites de l'audit
## Risques résiduels proposés à l'acceptation
```

## Pièges

- Scan automatisé présenté comme test complet.
- Tester seulement avec un compte administrateur : le contrôle d'accès reste invisible.
- Résultats sans versions d'outils ni date : impossibles à rejouer.
- Constats critiques clos sans contre-test.
- Preuves contenant des données réelles ou un détail réutilisable à des fins hostiles.

## Contrôles avant de rendre

- Chaque famille est testée ou écartée avec motif.
- La matrice des autorisations est complète pour tous les rôles.
- Chaque constat a gravité, preuve, responsable et statut.
- Le rapport écrit ce qui n'a pas été testé.
- Aucun détail d'exploitation n'est inclus.

## Sources

- OWASP ASVS 5.0.0 : https://owasp.org/www-project-ASVS/
- OWASP Top 10:2025 : https://top10.owasp.org/2025/0x00_2025-Introduction/
- OWASP WSTG v4.2 (v5.0 en développement) : https://owasp.org/projects/web-security-testing-guide
- OWASP MASTG : https://mas.owasp.org/MASTG/tests/
- FIRST, CVSS 4.0 : https://www.first.org/cvss/v4.0/
- OWASP GenAI, Top 10 LLM 2026 et Agentic 2026 : https://genai.owasp.org/
