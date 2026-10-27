# Spécifications techniques

Les spécifications techniques décrivent comment le système communique et traite, sans redire le métier : contrats d'interface, traitements non interactifs, formats, erreurs, paramétrage. Elles adaptent la conception fonctionnelle à l'architecture choisie (le « cahier des charges détaillé » ou CCTP de la pratique française). Elles se lisent avec le dossier d'architecture, jamais à sa place.

## Sommaire
1. Méthode
2. Contenu d'un contrat d'interface
3. Traitements, formats, paramétrage
4. Gabarit
5. Pièges fréquents
6. Contrôles avant de rendre
7. Sources

## 1. Méthode

1. **Partir des interfaces de la SFG** (section 8) et des décisions d'architecture (ADR). Ne rien décider de structurel : si un choix manque, le demander à l'`architecte-solution`.
2. **Un contrat par interface** : API exposée, API consommée, fichier échangé, événement, interface de reprise de données. Chacune reçoit une étiquette locale `IF-01`, `IF-02`…
3. **Décrire les traitements** hors interface : lots planifiés, files de messages, calculs lourds, purges, synchronisations. Chaque traitement : déclencheur, entrées, sorties, ordre, volumétrie, reprise.
4. **Fixer les formats** : encodage, dates (ISO 8601, fuseau), montants (devise, décimales), identifiants, énumérations.
5. **Normaliser les erreurs** : une table unique de codes, réutilisée par toutes les interfaces.
6. **Lister le paramétrage technique** : variables d'environnement, quotas, délais d'expiration, taille maximale, avec valeur par défaut par environnement. Aucun secret en clair dans le document.
7. **Rattacher à la chaîne** : toute règle technique devient une `RG-` (plage dédiée, par exemple RG-900 à RG-999) citant la `FN-` ou l'`EXNF-` qu'elle sert, pour être couverte par un `CT-`.
8. **Écrire pour le test** : chaque contrat a des exemples de requête et de réponse, valides et invalides, avec données fictives.

## 2. Contenu d'un contrat d'interface

| Rubrique | Ce qu'il faut écrire |
|---|---|
| Finalité et fonctions servies | `FN-` citées ; sens (entrant, sortant) ; propriétaire |
| Protocole et description formelle | REST, GraphQL, SOAP, fichier plat, message ; description exécutable (OpenAPI, AsyncAPI, JSON Schema) versionnée dans le dépôt, le document y renvoie |
| Authentification et autorisation | mécanisme (OAuth 2.0, clé, certificat), portées, rotation ; mécanismes validés par l'`architecte-securite` |
| Opérations | chemin ou nom, méthode, paramètres, corps, réponses, codes |
| Idempotence et ordre | clé d'idempotence, rejeu, traitement dans le désordre |
| Limites | taille maximale, quotas, pagination, délai d'expiration, relances (nombre, espacement) |
| Versionnement | règle de compatibilité, durée de support d'une version, préavis de retrait |
| Erreurs | codes propres, messages, comportement de l'appelant |
| Données personnelles | champs concernés, minimisation, journalisation proscrite des valeurs sensibles |
| Qualité de service | disponibilité, temps de réponse attendus (`EXNF-` citée), plan de repli si le tiers tombe |
| Tests | exemples, environnement bac à sable, tests de contrat |

## 3. Traitements, formats, paramétrage

| Sujet | Règle de décision |
|---|---|
| Traitement synchrone ou asynchrone | asynchrone dès que la durée dépasse le délai d'attente de l'appelant ou que la charge est en pics |
| Reprise après échec d'un lot | point de reprise ou traitement idempotent ; jamais « relancer à la main depuis le début » sans le décrire |
| Dates et heures | stockage en UTC, affichage dans le fuseau de l'utilisateur ; format ISO 8601 |
| Montants | entiers en plus petite unité ou décimal exact, jamais flottant ; devise explicite |
| Identifiants exposés | opaques, non devinables, pas de numéro séquentiel pour une ressource privée |
| Rétention et purge | durée, déclencheur, preuve de purge (à valider avec le `delegue-protection-donnees`) |
| Paramètre modifiable à chaud | oui si risque faible ; sinon livraison tracée |

## 4. Gabarit

````markdown
# Spécifications techniques — <nom du projet>

## Synthèse
<Nombre d'interfaces, de traitements ; ADR dont elles dépendent ; RG- techniques (plage) ;
 points en attente de l'architecte ; résultat du script de traçabilité.>

## 1. Périmètre et références
<ADR, modèle de données, infrastructure, versions des normes et des protocoles.>

## 2. Contrats d'interface
### IF-01 — <nom> (sortant, partenaire de paiement)
| Rubrique | Contenu |
|---|---|
| Fonctions servies | FN-021 |
| Protocole, description formelle | |
| Authentification | |
| Idempotence, limites, versionnement | |
| Exemple de requête valide | |
| Exemple de réponse en erreur | |

## 3. Traitements
| Traitement | Déclencheur | Entrées | Sorties | Volumétrie | Reprise | Règle |
|---|---|---|---|---|---|---|

## 4. Formats et conventions
## 5. Erreurs
| Code | Cause | Appelant doit | Journalisé | Message exposé | Règle |
|---|---|---|---|---|---|

## 6. Règles techniques
| ID | Fonction | Exigence non fonctionnelle | Règle | Exemple |
|---|---|---|---|---|
| RG-901 | FN-021 | EXNF-004 | Si le partenaire ne répond pas sous 5 s, alors l'appel est relancé deux fois avec 2 s d'écart, puis la commande passe en « paiement en attente » | délais simulés : 3e échec, statut en attente |

## 7. Paramétrage
| Paramètre | Défaut dev | Défaut recette | Défaut production | Modifiable par |
|---|---|---|---|---|

## 8. Questions ouvertes
````

## 5. Pièges fréquents

- Spécifier une interface sans exemple d'erreur : l'appelant improvise.
- Contrat décrit en prose seulement, sans description formelle exécutable.
- Aucun comportement prévu quand le tiers est indisponible.
- Secrets, jetons ou données réelles dans les exemples.
- Doublon avec l'architecture : le « pourquoi » reste dans les ADR, ici seul le « comment précis ».
- Règles techniques sans `FN-` ni `EXNF-` : elles échappent à la recette.
- Versions de protocole non datées.

## 6. Contrôles avant de rendre

- Toute interface de la SFG a son contrat, ses fonctions, ses exemples valides et invalides.
- Chaque traitement a un déclencheur, une volumétrie, une reprise.
- Une table d'erreurs unique ; tout code d'un contrat y figure.
- Chaque règle technique est une `RG-` dans la bonne plage, avec sa `FN-` sur la même ligne.
- Authentification validée par l'`architecte-securite` ; données personnelles signalées.

## Sources

- JDN, « Les dossiers techniques en gestion de projet informatique » (CCTP, adaptation à l'architecture).
- HERMES (2022, 3e tirage 31.12.2025) : « Detailed specifications », concepts d'exploitation et de déploiement.
- arc42 (12 sections) et C4 : pour le lien avec le dossier d'architecture.
- MADR : décisions d'architecture citées depuis les spécifications.
- OpenAPI, AsyncAPI, JSON Schema, ISO 8601, OAuth 2.0 (RFC 6749) : versions à fixer au projet.
