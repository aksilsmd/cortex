# DevSecOps : contrôles de sécurité automatisés dans la chaîne

Placer à chaque étape de la livraison le contrôle qui y est le moins cher, avec un seuil de blocage écrit. Un contrôle sans seuil est un voyant que personne n'écoute.

## Sommaire
- Chaîne de contrôles
- Seuils de blocage
- Protéger la chaîne elle-même
- Traitement des constats
- Gabarit de configuration de la chaîne
- Pièges et contrôles
- Sources

## Chaîne de contrôles

Outils cités comme options (versions et état non vérifiés : à vérifier). Choisir un outil par ligne, pas tous.

| Étape | Contrôle | Outils possibles |
|---|---|---|
| Conception | modèle de menaces, exigences ASVS | STRIDE, LINDDUN, EBIOS RM |
| Poste, avant commit | détection de secrets, analyse légère | Gitleaks, TruffleHog, Semgrep |
| Demande de fusion, intégration continue | analyse statique du code (SAST) | Semgrep, CodeQL |
| | dépendances connues vulnérables (SCA) | OSV-Scanner, Dependabot, Trivy |
| | secrets dans l'historique | Gitleaks, TruffleHog |
| | infrastructure décrite en code (IaC) | Checkov |
| | revue de code obligatoire | par un humain ou un agent distinct de l'auteur |
| Construction | inventaire des composants (SBOM) | CycloneDX ou SPDX |
| | analyse d'image de conteneur | Trivy et équivalents |
| | signature et provenance | Sigstore et cosign ; SLSA niveau 2 minimum |
| Préproduction | test dynamique authentifié (DAST) | OWASP ZAP |
| | tests d'API et d'autorisation | suite de tests du projet |
| Déploiement | vérification de signature à l'admission, posture cloud | CNAPP, politiques d'admission |
| Exploitation | pare-feu applicatif, SIEM, nouveau scan continu du SBOM | voir `protections-par-couche.md` |

Un contrôle dynamique tourne seulement sur un environnement du projet, jamais sur un tiers.

## Seuils de blocage

| Constat | Seuil | Action |
|---|---|---|
| Secret détecté | tout secret réel | bloque la fusion ; secret considéré compromis et renouvelé, pas seulement supprimé |
| SAST critique ou haut | tout constat confirmé | bloque la fusion |
| SAST moyen | à partir de 5 non traités | alerte, ticket avec échéance |
| Dépendance critique avec correctif ou exploitation connue | tout | bloque la fusion |
| Dépendance haute | délai de 15 jours | alerte ; blocage au dépassement |
| IaC en défaut critique (stockage public, port d'administration ouvert) | tout | bloque le déploiement |
| Image avec vulnérabilité critique corrigeable | tout | bloque la publication |
| Image exécutée en administrateur | tout | bloque la publication |
| DAST haut ou critique | tout | bloque la mise en recette suivante |
| Artefact sans signature valide | tout | bloque le déploiement |

Valeurs de départ proposées (jugement, à ajuster par l'architecte-securite et validées en comité d'architecture). Les délais de correction par gravité (par exemple critique 7 jours, haut 30 jours) sont fixés dans la politique de vulnérabilités ; l'exception porte un ticket, un propriétaire et une date d'expiration.

Calibrage : sur une base existante, démarrer en mode alerte, mesurer le bruit une semaine, puis bloquer. Le blocage immédiat d'un tas de constats anciens fait contourner l'outil.

## Protéger la chaîne elle-même

L'incident Trivy du 19 mars 2026 (binaire, action de CI et installateur compromis après vol d'un identifiant) montre que les outils de sécurité sont une cible. À appliquer :

- épingler les actions et outils de CI sur leur empreinte complète (SHA), pas sur une étiquette modifiable ;
- mettre à jour par demande de fusion relue ;
- utiliser des identifiants de pipeline éphémères (OIDC) ; permissions minimales par tâche ;
- savoir faire tourner tous les secrets de pipeline en une heure si un outil est compromis ;
- vérifier les signatures au déploiement, pas seulement les produire ;
- séparer le compte qui construit du compte qui déploie.

## Traitement des constats

1. Dédoublonner et noter : CVSS 4.0, avec le groupe indiqué (B, BT, BE ou BTE) ; enrichir par la menace et l'environnement pour prioriser. La note de base seule surestime les cas non exploitables en pratique.
2. Verser au registre : constats d'audit pour les écarts de sécurité, anomalies pour les défauts à corriger par un développeur.
3. Reprendre le développeur d'origine ; faire contre-tester par l'`auditeur-securite`.
4. Clore avec preuve (sortie de l'outil après correction), jamais sur déclaration.
5. Sur un faux positif, documenter la règle écartée et la date de réexamen.

## Gabarit de configuration de la chaîne

À ajouter à la section sécurité de `03-conception/architecture/infrastructure.md` (propriétaire : `ingenieur-devops`).

```markdown
## Chaîne de contrôles de sécurité
| Étape | Contrôle | Outil | Seuil de blocage | Propriétaire | Exceptions |
|---|---|---|---|---|---|
```

## Pièges

- Outil branché mais en mode alerte pour toujours.
- Analyse de dépendances ponctuelle sans nouveau scan quotidien du SBOM : une faille publiée après la livraison reste invisible.
- Secret supprimé du dépôt mais non renouvelé : il reste dans l'historique.
- Exceptions sans date de fin.
- Mélange CVSS 3.1 et 4.0 dans le même tableau.

## Contrôles avant de rendre

- Chaque étape du tableau a un outil ou un motif d'absence.
- Chaque seuil de blocage est écrit et validé.
- Les actions et outils de CI sont épinglés.
- Le tableau des exceptions porte propriétaire et date d'expiration.

## Sources

- OWASP Top 10:2025, A03 Software Supply Chain Failures : https://top10.owasp.org/2025/0x00_2025-Introduction/
- Avis de sécurité Trivy : https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23
- SLSA : https://slsa.dev/spec/v1.0/levels
- NIST SP 800-218 SSDF v1.1 (2022) ; Rev.1 en projet (décembre 2025, à vérifier) : https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
- FIRST, CVSS 4.0 : https://www.first.org/cvss/v4.0/
