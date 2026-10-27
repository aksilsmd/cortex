# Analyse de risques et modélisation des menaces

Méthode pour établir, dès le cadrage, ce qu'il faut protéger, contre quoi, et à quel niveau de preuve. Sans cela, les protections sont choisies par habitude et les tests n'ont pas de cible.

## Sommaire
- Analyse de risques initiale
- Niveau de vérification visé
- Modélisation des menaces par flux
- Exigences de sécurité
- Gabarit `analyse-risques-securite.md`
- Gabarit `modele-menaces.md`
- Pièges et contrôles avant de rendre
- Sources

## Analyse de risques initiale

1. **Inventorier les actifs** : données (personnelles, paiement, secrets métier), services, domaines et sous-domaines, API, applications mobiles, comptes à privilèges, SaaS tiers, chaîne de livraison. Un propriétaire par actif ; un actif sans propriétaire n'est pas protégé.
2. **Classer chaque actif** par besoin de confidentialité, d'intégrité, de disponibilité (échelle 1 à 4).
3. **Identifier les sources de menace** pertinentes : criminels opportunistes (la grande majorité), fraudeurs, concurrents, initiés, prestataires, accidents.
4. **Écrire les scénarios** de la forme « source → moyen → actif → impact », sans détail d'attaque : le niveau d'un scénario de risque est celui d'un événement redouté, pas d'un mode opératoire.
5. **Coter** vraisemblance et impact (1 à 4) ; le niveau de risque est leur produit. Reporter chaque risque supérieur ou égal à 9 au registre `RSQ-`.
6. **Choisir le traitement** : réduire, éviter, transférer (assurance, prestataire), accepter. L'acceptation est tracée avec nom et motif (`risque-accepte`).
7. **Déduire les exigences** (voir ci-dessous) et les régimes applicables (`references/obligations-cyber.md`).

Méthode : EBIOS Risk Manager (cadre français, atelier par atelier) pour un grand compte ou un régulé ; ISO/IEC 27005 ou fiche simple pour le reste.

| Projet | Profondeur de l'analyse |
|---|---|
| Site vitrine sans compte | une page : actifs, 5 scénarios, mesures de base |
| E-commerce, application avec comptes | actifs, scénarios, cotation, exigences ASVS niveau 2 |
| SaaS B2B, santé, finance, grand compte | EBIOS RM complète, revue par un auditeur qualifié, mise à jour annuelle |

## Niveau de vérification visé

Choisir un niveau de l'ASVS 5.0.0 (mai 2025) par application, le justifier par le risque et le faire signer par le porteur du projet.

| Critère | Niveau |
|---|---|
| Aucune donnée personnelle sensible, pas de compte, enjeu faible | 1 |
| Comptes utilisateurs, données personnelles, paiement délégué, SaaS standard | 2 |
| Santé, finance, grandes quantités de données sensibles, fonctions critiques | 3 |

Un niveau 1 est la base minimale de tout ce qui est exposé à internet. Pour une application mobile, ajouter MASVS ; pour des API, croiser avec l'OWASP API Security Top 10 (2023, à vérifier avant publication) ; pour des fonctions d'IA, vérifier l'édition en vigueur du Top 10 LLM et du Top 10 Agentic (à vérifier). Citer les exigences par identifiant versionné (par exemple v5.0.0-1.2.5). Ne plus citer ASVS 4.0.3 ni Top 10:2021 comme référence en vigueur.

## Modélisation des menaces par flux

1. **Dessiner le diagramme de flux** : acteurs, processus, magasins de données, flux, frontières de confiance (internet, réseau interne, tiers, poste d'administration). Un diagramme Mermaid suffit.
2. **Pour chaque flux qui franchit une frontière**, appliquer STRIDE : usurpation, falsification, répudiation, divulgation, déni de service, élévation de privilèges. Appliquer LINDDUN pour la vie privée si `donnees-perso`.
3. **Formuler la menace en une phrase** et lui donner un identifiant. Pas de technique d'exploitation : « un utilisateur authentifié accède aux données d'un autre » est suffisant.
4. **Lier chaque menace** à une mesure (existante, prévue ou à décider) et à un contrôle de test futur.
5. **Mettre à jour** à chaque changement de flux ou de fournisseur, et avant la conception de toute fonction majeure.

PASTA convient si l'analyse doit partir du risque métier ; STRIDE reste le choix par défaut pour la rapidité.

## Exigences de sécurité

Une exigence de sécurité est une phrase vérifiable, rattachée à une menace et à un chapitre de la norme. Elle rejoint le cahier des charges comme exigence non fonctionnelle `EXNF-` : l'identifiant y est défini par l'expert du cahier des charges, le pôle fournit le contenu. Exemple : « Chaque accès à un objet métier est contrôlé côté serveur selon le rôle de l'appelant ».

## Gabarit `analyse-risques-securite.md`

```markdown
# Analyse de risques de sécurité

## Synthèse
(12 lignes : nombre d'actifs, de scénarios, de risques supérieurs ou égaux à 9, niveau ASVS proposé, régimes applicables, décisions attendues)

## Périmètre et hypothèses
## Actifs
| ID | Actif | Propriétaire | C | I | D | Remarque |
|---|---|---|---|---|---|---|
## Sources de menace
## Scénarios de risque
| ID | Scénario | Actif | Vraisemblance | Impact | Niveau | Traitement | RSQ |
|---|---|---|---|---|---|---|---|
## Exigences de sécurité
| ID | Exigence | Menace couverte | Chapitre de la norme | EXNF |
|---|---|---|---|---|
## Niveau de vérification visé
(niveau, justification, signature du porteur, date)
## Régimes applicables
(NIS2, DORA, CRA, PCI DSS, HDS, RGPD : applicable ou non, motif, à valider)
## Risques acceptés et décisions à prendre
```

## Gabarit `modele-menaces.md`

```markdown
# Modèle de menaces

## Synthèse
(nombre de flux, de menaces, de menaces sans mesure, décisions attendues)

## Diagramme de flux
(schéma Mermaid avec frontières de confiance)
## Flux et frontières
| ID | Flux | Franchit | Données | Authentification |
|---|---|---|---|---|
## Menaces
| ID | Flux | Catégorie STRIDE ou LINDDUN | Menace | Mesure | Contrôle de test | Statut |
|---|---|---|---|---|---|---|
## Menaces non couvertes
```

## Pièges

- Analyse copiée d'un autre projet : elle ne reflète ni les données ni les flux réels.
- Périmètre oublié : sous-domaines, API héritées, préproduction, SaaS tiers.
- Niveau ASVS choisi par défaut sans signature : personne ne sait ensuite ce qui est attendu.
- Modèle de menaces écrit après le code : il décrit l'existant au lieu de le guider.

## Contrôles avant de rendre

- Chaque actif a un propriétaire et une classification.
- Chaque risque supérieur ou égal à 9 a un traitement et une ligne au registre.
- Chaque flux franchissant une frontière a ses menaces.
- Le niveau de vérification est écrit, justifié et soumis à signature.
- Aucun détail d'exploitation n'apparaît dans les scénarios.

## Sources

- OWASP ASVS 5.0.0 (mai 2025) : https://owasp.org/www-project-ASVS/
- OWASP Top 10:2025 : https://top10.owasp.org/2025/0x00_2025-Introduction/
- ANSSI, EBIOS Risk Manager (catalogue MesServicesCyber) : https://messervices.cyber.gouv.fr/catalogue
- ISO/IEC 27005 (gestion des risques) : édition à vérifier
- ISO/IEC 27002:2022 : https://www.iso.org/standard/75652.html
- CIS Controls v8.1 : https://www.cisecurity.org/controls/implementation-groups
