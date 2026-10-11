# Cadrer et conduire un test d'intrusion autorisé

Un test d'intrusion vérifie qu'une vulnérabilité du système audité est exploitable et mesure son impact. Ce fichier traite le cadrage, l'autorisation, les familles de vérifications au niveau des catégories, la notation et le rapport. Il ne contient aucune technique d'attaque, et n'en doit pas recevoir.

## Sommaire
- Conditions préalables non négociables
- Décider : agent ou prestataire qualifié
- Cadrage et règles d'engagement
- Gabarit d'autorisation écrite
- Familles de vérifications
- Notation de la gravité
- Gabarit `rapport-test-intrusion.md`
- Contre-test
- Pièges et contrôles
- Sources

## Conditions préalables non négociables

1. **Autorisation écrite** du propriétaire de chaque actif testé, signée avant tout test. Y ajouter l'hébergeur ou le fournisseur de service (cloud, CDN, SaaS) si ses conditions exigent une notification ou un accord : lire ses règles de test.
2. **Périmètre fermé** : liste explicite d'adresses, domaines, API, applications et environnements. Ce qui n'est pas listé est interdit.
3. **Environnements du projet seulement** : recette ou préproduction par défaut. Production uniquement avec accord explicite écrit, fenêtre dédiée et exclusion du déni de service.
4. **Jamais un système tiers**, même lié (fournisseur, prestataire de paiement, SaaS) : le périmètre s'arrête à la frontière du projet.
5. **Refus et signalement :** si l'autorisation ou le périmètre manque, l'agent ne teste rien, l'écrit dans sa synthèse et alerte le chef d'orchestre.

Accéder à un système sans droit, ou s'y maintenir, est un délit (Code pénal, art. 323-1 : 3 ans et 100 000 €, jusqu'à 5 ans si des données sont modifiées ou le système altéré). L'entrave et l'atteinte aux données (art. 323-2, 323-3) montent à 5 ans et 150 000 €. Importer ou détenir un outil conçu pour ces atteintes est puni de la même peine « sans motif légitime, notamment de recherche ou de sécurité informatique » (art. 323-3-1). Aucun texte ne vaut immunité : seule l'autorisation écrite préalable du titulaire écarte le caractère frauduleux. Peines et jurisprudence récente : « à valider » par le juriste du projet.

## Décider : agent ou prestataire qualifié

| Situation | Choix |
|---|---|
| Site vitrine sans compte, sans donnée sensible | test par l'agent sur la recette, suffisant |
| Comptes et données personnelles, e-commerce avec paiement délégué | agent, puis prestataire recommandé avant un lancement majeur |
| Santé, finance, paiement direct, SaaS d'un grand compte, exigence d'un régulateur ou d'un acheteur | prestataire qualifié obligatoire pour la preuve |
| France, preuve demandée par un client ou un régulateur | prestataire PASSI qualifié pour l'activité « tests d'intrusion » ; vérifier la qualification à date dans l'annuaire MesServicesCyber de l'ANSSI |

Un test conduit par un agent ne remplace jamais ce prestataire pour un enjeu fort. Un audit de code n'est pas un test d'intrusion : vérifier que la qualification couvre l'activité visée. Fréquence : annuelle et après changement majeur ; en continu, une politique de divulgation coordonnée et un fichier security.txt (RFC 9116, domaine servi, champs Contact et Expires à jour).

## Cadrage et règles d'engagement

| Point | À fixer |
|---|---|
| Objectif | exemple : vérifier l'isolement entre clients du SaaS |
| Type | boîte noire (vue externe), grise (comptes de plusieurs rôles, meilleur rapport couverture/coût pour le contrôle d'accès), blanche (code fourni) |
| Fenêtre | dates et heures, hors pics, équipe d'exploitation prévenue |
| Interdits | déni de service, hameçonnage de personnes, accès physique, tiers, données réelles exfiltrées |
| Volumétrie | débit maximal des requêtes |
| Contacts | deux contacts d'urgence joignables pendant la fenêtre |
| Arrêt immédiat | à la moindre dégradation, ou sur demande du propriétaire |
| Données | aucune donnée réelle copiée ; preuves sans données personnelles |
| Confidentialité | rapport diffusé à une liste restreinte, chiffré ; clauses RGPD de sous-traitance si un prestataire est en jeu |

## Gabarit d'autorisation écrite

À écrire dans `05-validation/rapport-test-intrusion.md` avant le moindre test, et à faire valider par le juriste.

```markdown
## Autorisation de test d'intrusion
- Propriétaire des actifs : (nom, fonction, signature, date)
- Hébergeur ou fournisseur informé ou ayant donné son accord : (nom, date, référence)
- Exécutant : (agent ou prestataire, qualification)
- Objectif :
- Périmètre autorisé : (adresses, domaines, API, applications, environnements)
- Exclusions explicites :
- Type de test : (noire, grise, blanche) ; comptes fournis par rôle :
- Fenêtre : du … au … ; heures :
- Règles d'engagement : (interdits, volumétrie, arrêt immédiat)
- Contacts d'urgence : (deux noms, téléphones)
- Gestion des données et des preuves :
- Confidentialité et diffusion du rapport :
- Accord de production : (non, ou oui avec conditions écrites)
```

Sans toutes ces lignes remplies et signées, le test ne démarre pas.

## Familles de vérifications

Au niveau des catégories des normes publiques (WSTG v4.2, MASTG, API Security Top 10 2023, à vérifier). Pour chacune : on vérifie l'exposition, l'exploitabilité sur le périmètre et l'impact, sans publier de mode opératoire.

| Famille | Objet |
|---|---|
| Cartographie de la surface exposée | domaines, sous-domaines, API, applications mobiles, services accessibles |
| Configuration et déploiement | interfaces d'administration, versions, en-têtes, erreurs |
| Identités et authentification | politiques de mot de passe, MFA, récupération de compte |
| Gestion des sessions | durée, invalidation, jetons |
| Contrôle d'accès | isolation entre rôles et entre clients (verticale, horizontale, contexte) |
| Validation des entrées | exposition aux défauts d'injection, au niveau de la catégorie |
| Logique métier | enchaînements interdits, abus de fonctionnalités |
| API | autorisation par objet et par fonction, quotas |
| Cryptographie | protocoles et certificats |
| Côté client et mobile | stockage local, communications |
| Segmentation | isolement des environnements, tests de segmentation si PCI DSS |

## Notation de la gravité

Noter en CVSS 4.0 et **indiquer le groupe employé** : CVSS-B (base), BT (menace), BE (environnement), BTE. Enrichir par Threat puis Environmental quand l'organisation l'utilise pour prioriser ; ne pas mélanger avec la version 3.1. Délais de correction par gravité à fixer dans la politique de vulnérabilités.

## Gabarit `rapport-test-intrusion.md`

```markdown
# Rapport de test d'intrusion

## Synthèse
(périmètre, dates, type de test, exécutant, constats par gravité, risque global, décision recommandée, limites)

## Autorisation et règles d'engagement
(gabarit ci-dessus renseigné)
## Périmètre et méthode (référentiels et versions)
## Chronologie
## Constats
| ID AUD | Famille | CWE | Vecteur CVSS 4.0 et groupe | Description | Preuve non exploitable | Recommandation | Effort | Statut |
|---|---|---|---|---|---|---|---|---|
## Plan d'action priorisé
## Contre-test
| ID AUD | Date | Résultat | Preuve de clôture |
|---|---|---|---|
## Limites et éléments non testés
## Annexes
```

## Contre-test

Rejouer, après correction, chaque constat critique et haut sur le même périmètre, avec la même autorisation prolongée. Clore avec preuve ; un constat corrigé en apparence, mais non rejoué, reste ouvert. La non-régression s'ajoute à la recette.

## Pièges

- Périmètre incomplet : sous-domaines, API héritées, préproduction oubliés.
- Hébergeur non informé alors que ses conditions l'exigent.
- Test sur la production sans fenêtre ni arrêt immédiat.
- Preuves qui contiennent des données réelles ou un détail réutilisable.
- Rapport sans vecteur complet ni groupe CVSS.

## Contrôles avant de rendre

- L'autorisation signée précède la première action.
- Le périmètre et les exclusions sont écrits.
- La mention des limites et de la recommandation d'un prestataire qualifié figure à la synthèse.
- Chaque constat a une recommandation et un statut.

## Sources

- ANSSI, référentiels PASSI v2.2 et PRIS v3.0 : https://cyber.gouv.fr/offre-de-service/solutions-certifiees-et-qualifiees/comprendre-levaluation-de-securite/qualification-de-produit-et-services/referentiels-qualification/
- ANSSI, annuaire des prestataires : https://messervices.cyber.gouv.fr/prestataires-labellises
- FIRST, CVSS 4.0 : https://www.first.org/cvss/v4.0/specification-document
- RFC 9116 (security.txt) : https://www.rfc-editor.org/info/rfc9116/
- PCI SSC, Penetration Testing Guidance v1.1 : https://www.pcisecuritystandards.org/documents/Penetration-Testing-Guidance-v1_1.pdf
- Légifrance, Code pénal, articles 323-1 à 323-8 (version en vigueur au 11 octobre 2026) ; Code de la défense, L2321-4 (signalement à l'ANSSI)
