# Choisir un LMS : voies et grille de critères

Cette fiche sert à décider, avec preuves, entre trois voies. Elle n'affirme rien sur les prix, les versions ou les fonctions de produits que le dépôt de Canvas ne documente pas : ces points sont à relever à la source par le collecteur web (`${CLAUDE_PLUGIN_ROOT}/agents/collecteur-web.md`) et datés.

## 1. Les trois voies

| Voie | Quand elle convient | Points de vigilance |
|---|---|---|
| **Canvas hébergé par Instructure** | pas d'équipe technique, besoin de démarrer vite, volume qui justifie un abonnement, acceptation d'un hébergement et d'un contrat chez un fournisseur | prix et durée d'engagement à obtenir par devis ; lieu d'hébergement des données, sous-traitants, transferts hors Union européenne ; marge de personnalisation limitée à ce que le fournisseur autorise ; clés de développeur délivrées par l'administrateur de l'établissement ; réversibilité (export) à contractualiser |
| **Canvas auto-hébergé** | maîtrise des données et du lieu d'hébergement exigée, équipe capable d'exploiter une application Ruby on Rails avec PostgreSQL et Redis, besoin de modifier le produit | charge d'exploitation réelle (montées de version, sauvegardes, supervision, sécurité) ; obligation de publier les sources si l'on modifie et que l'on sert en réseau (AGPL) ; la procédure de production officielle est sur un wiki à lire à part ; certains services annexes (événements en direct) reposent sur des briques séparées |
| **Autre LMS à évaluer** | exigences que Canvas ne couvre pas, écosystème déjà installé, préférence de gouvernance | à évaluer avec la même grille, sans présupposé |

Alternatives à inscrire dans la comparaison, **sans préjuger du résultat** : **Moodle** et **Open edX**. Seul fait vérifié dans le dépôt de Canvas : il sait importer des cours depuis un format Moodle et sa documentation cite Moodle comme référence d'explication de LTI ; cela ne dit rien de la qualité de Moodle. Pour chacune de ces plateformes (et toute autre), relever à la source officielle : licence et obligations, version actuelle et calendrier de support, pile technique, hébergement possible, prise en charge de LTI 1.3 et de ses services, accessibilité déclarée, communauté et prestataires. Dater chaque relevé.

## 2. Pré-questions qui évitent un mauvais choix

1. Un LMS est-il nécessaire ? Si l'on ne propose que quelques vidéos et un quiz, un site simple peut suffire (retour à `recueil-besoin`).
2. Le public inclut-il des mineurs ? Si oui, le délégué à la protection des données intervient avant la comparaison.
3. Qui administrera la plateforme dans trois ans ? Sans personne identifiée, l'auto-hébergement est écarté ou chiffré avec un prestataire.
4. Faut-il modifier le produit ? Si oui, mesurer l'obligation AGPL (publication) et le coût d'entretien d'un correctif à chaque montée de version.
5. Faut-il relier un SIS, un annuaire, une visio, un outil anti-plagiat, un portfolio ? Lister les outils et leur compatibilité LTI 1.3.

## 3. Grille de critères

Noter chaque critère de 0 à 3 (0 : non couvert ; 1 : partiel ou contournement ; 2 : couvert ; 3 : couvert et prouvé). Pondérer de 1 à 3 avec l'utilisateur. Chaque note a une source (document, essai, devis) et une date. Un critère éliminatoire à 0 écarte la voie, quelle que soit la somme.

| Famille | Critère | Preuve attendue |
|---|---|---|
| Pédagogie | cours, modules, pages, devoirs, quiz, notation, barèmes, rubriques, groupes, discussions | essai d'un cours type de bout en bout |
| Pédagogie | rôles (apprenant, enseignant, assistant, concepteur, observateur, administrateur) et droits fins | liste des rôles et essai de droits |
| Pédagogie | parcours conditionnels, suivi de progression, certificats ou attestations | démonstration |
| Intégration | LTI 1.3 et services (annuaire, notes, liens profonds), enregistrement dynamique | documentation et essai avec un outil réel |
| Intégration | API REST complète, pagination, limites, portées, événements | documentation lue et appel de test |
| Intégration | SSO (SAML, CAS, LDAP, OpenID Connect), import SIS | essai avec l'annuaire de l'organisme |
| Contenus | import et export de cours (Common Cartridge, QTI), reprise de l'existant | import d'un cours réel, écarts relevés |
| Données | lieu d'hébergement, sous-traitants, durée de conservation, export, effacement, journaux d'accès | contrat et registre ; avis du délégué |
| Données | niveau de confidentialité réglable par outil tiers | essai |
| Accessibilité | conformité déclarée, essais clavier et lecteur d'écran | avis de l'expert en accessibilité |
| Sécurité | correctifs, politique de vulnérabilités, authentification forte, journalisation | revue par le pôle sécurité |
| Exploitation | effort d'installation et de montée de version, sauvegarde, supervision, besoin de compétences | estimation de jours-homme et essai de restauration |
| Licence | licence, obligations, risque de verrouillage, marque | lecture de la licence ; avis du juriste |
| Coût | licence ou abonnement, hébergement, exploitation, formation, intégrations, sur trois ans | scénarios du pôle finance |
| Durabilité | vitalité du projet, feuille de route, support, prestataires locaux, langue française | relevé daté |

## 4. Procédure de décision

1. Remplir la grille pour chaque voie, une personne remplissant, une autre contre-vérifiant (`contradicteur`).
2. Écarter les voies qui ont un critère éliminatoire à 0.
3. Chiffrer le coût sur trois ans (`${CLAUDE_SKILL_DIR}/../budget-finance/SKILL.md`), y compris le temps d'administration, souvent oublié.
4. Si deux voies sont à moins de 10 % d'écart, organiser une réunion de décision (`${CLAUDE_SKILL_DIR}/../reunion-decision/SKILL.md`) et proposer un essai limité (un cours, un mois) avec critères de sortie.
5. Consigner dans un ADR : contexte, voies comparées, notes, décision, conséquences, conditions de réexamen (`${CLAUDE_SKILL_DIR}/../architecture-normes/SKILL.md`).
6. Faire valider par l'utilisateur avant tout achat, installation ou migration.

## 5. Erreurs fréquentes

- Choisir sur la démonstration d'un vendeur plutôt que sur un essai avec ses propres contenus.
- Sous-estimer l'auto-hébergement : le coût réel est celui de l'exploitation, pas de la licence.
- Oublier que chaque outil LTI branché a sa propre politique de données et d'accessibilité.
- Modifier le produit sans avoir tranché l'AGPL.
- Ne prévoir ni export ni sortie : toujours tester l'export complet d'un cours avant de s'engager.
