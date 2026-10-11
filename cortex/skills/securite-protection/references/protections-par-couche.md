# Protections par couche et par taille de projet

Choisir, couche par couche, les protections contre l'intrusion, les logiciels malveillants, le déni de service et le piratage de comptes, à la taille du projet. Les noms de produits sont des options du marché (état : octobre 2026, positions et rachats non vérifiés : à vérifier avant achat).

## Sommaire
- Couches et choix
- Pare-feu, détection et prévention d'intrusion
- Anti-malware, anti-déni de service, anti-robots
- Identités, secrets, chiffrement
- Durcissement, sauvegardes, journalisation
- Dosage par taille de projet
- Gabarit `architecture-securite.md`
- Pièges et contrôles
- Sources

## Couches et choix

| Couche | Protection | Solutions du marché | Alternatives libres |
|---|---|---|---|
| Bordure | CDN, anti-DDoS, pare-feu applicatif et d'API (WAAP) | Cloudflare, Akamai, Imperva, F5, Fastly, AWS WAF et Shield, Google Cloud Armor | Coraza avec OWASP CRS ; ModSecurity n'a plus de support commercial (Trustwave, 2024) |
| Anti-robots | gestion des robots, limitation de débit | DataDome, HUMAN, modules des WAAP | limitation de débit au proxy |
| Réseau | pare-feu de nouvelle génération, segmentation | Palo Alto, Fortinet, Stormshield | OPNsense, groupes de sécurité du cloud |
| Intrusion | détection et prévention (IDS, IPS) | modules des pare-feu | Suricata, Zeek |
| Postes et serveurs | anti-malware et détection (EDR) | CrowdStrike, SentinelOne, Microsoft Defender, HarfangLab | Wazuh, Velociraptor |
| Identités | gestion des identités, authentification forte | Entra ID, Okta, Auth0, CyberArk | Keycloak |
| Secrets, clés | coffre, KMS, HSM | HashiCorp Vault, KMS du cloud | OpenBao, SOPS |
| Charges cloud | posture et conteneurs (CNAPP) | Wiz, Prisma Cloud, Defender for Cloud | Kubescape, Falco, Prowler |
| Sauvegardes | sauvegarde immuable | Veeam, Rubrik, Cohesity | verrouillage d'objet du stockage, Restic ou Borg |
| Supervision | collecte et alertes (SIEM) | Splunk, Sentinel, Elastic | Wazuh, Graylog, OpenSearch |

Le WAF est devenu WAAP (API, robots, déni de service) : demander la protection des API dans l'appel d'offres.

## Pare-feu, détection et prévention d'intrusion

- **Pare-feu réseau :** refus par défaut, flux autorisés documentés, segmentation entre exposition, applications, données et administration. L'administration passe par un bastion ou une solution d'accès privilégié, jamais par une ouverture directe.
- **Pare-feu applicatif :** en mode blocage dès la recette, pas en simple détection. Passer d'abord en détection une à deux semaines pour mesurer les faux positifs, puis bloquer. Revoir les faux positifs chaque mois ; chaque exception porte une date.
- **Origine non joignable en direct :** n'accepter que les adresses du fournisseur de bordure. Sinon le pare-feu est contournable.
- **IDS/IPS :** utile à partir d'un réseau à gérer ; sur du cloud managé, les journaux et la détection de la plateforme suffisent souvent au départ.

## Anti-malware, anti-déni de service, anti-robots

- **Anti-malware :** EDR sur 100 % des serveurs et postes d'administration, couverture contrôlée chaque mois. Si le projet accepte des dépôts de fichiers (`ugc`, documents) :
  - analyser le flux de dépôt avec un antivirus avant toute mise à disposition (moteur libre type ClamAV ou service d'analyse de l'hébergeur) ;
  - mettre en quarantaine tout fichier non analysé ou détecté, sans accès public ;
  - contrôler côté serveur une liste blanche de types et une taille maximale (le navigateur n'est pas une preuve) ;
  - stocker hors de la racine web, sans droit d'exécution, de préférence sur un domaine séparé ;
  - régénérer le nom du fichier (identifiant aléatoire), sans reprendre celui de l'utilisateur.
- **Anti-déni de service :** protection volumétrique chez le fournisseur de bordure, limitation de débit par client et par route, mise en cache, dégradation maîtrisée. Un plan de montée en charge d'urgence est écrit avant le lancement.
- **Anti-robots :** limitation de débit sur connexion, inscription, réinitialisation et recherche ; défi proportionné au risque ; pas de blocage qui exclut l'accessibilité (voir les contrôles du pôle Design).

## Identités, secrets, chiffrement

- **Authentification forte :** MFA obligatoire pour tous les comptes à privilèges et accès distants ; passkeys (FIDO2) proposées aux utilisateurs si `comptes`. Un SMS est un dernier recours.
- **Secrets :** aucun secret dans le code, les images ou les journaux de CI ; coffre ou KMS, rotation planifiée et testée.
- **Chiffrement :** TLS 1.2 minimum en transit (TLS 1.3 préféré) ; chiffrement au repos ; clés en KMS ou HSM, accès journalisés. Suivre les recommandations cryptographiques de l'ANSSI en France (à vérifier).

## Durcissement, sauvegardes, journalisation

- **Durcissement :** CIS Benchmarks ou recommandations ANSSI ; écarts mesurés par scan automatisé ; images conteneur minimales, non-root.
- **Sauvegardes :** règle 3-2-1 avec une copie immuable ou hors ligne ; comptes de sauvegarde distincts de ceux de la production ; restauration testée au moins deux fois par an, RTO et RPO mesurés.
- **Journalisation :** authentification, administration, pare-feu applicatif, cloud, centralisés, rétention définie (cohérente avec la protection des données), au moins une alerte testée par trimestre. Un journal sans alerte ni propriétaire ne protège pas (OWASP A09:2025).

## Dosage par taille de projet

| Couche | Site vitrine | Petit e-commerce ou SaaS de niche | SaaS, ERP, grand compte, régulé |
|---|---|---|---|
| Bordure | CDN avec protection de base, TLS | WAAP géré, limitation de débit, anti-robots sur formulaires | WAAP complet API et robots, anti-DDoS dimensionné |
| Réseau | pare-feu de l'hébergeur | groupes de sécurité, segmentation simple | segmentation, pare-feu nouvelle génération, IDS/IPS |
| Postes et serveurs | mises à jour automatiques | EDR sur serveurs et administrateurs | EDR, CNAPP, durcissement mesuré |
| Identités | MFA sur l'administration | MFA, passkeys proposées | IAM central, accès privilégiés, revue périodique des droits |
| Secrets, clés | variables protégées | coffre ou secrets du cloud | KMS ou HSM, rotation automatisée |
| Sauvegardes | sauvegarde hébergeur testée | copie immuable | copie immuable, plan de reprise testé |
| Supervision | alertes de l'hébergeur | journaux centralisés, alertes | SIEM, astreinte, éventuellement SOC externe |

Pour du paiement, privilégier la page de paiement hébergée par le prestataire : elle réduit le périmètre PCI DSS (voir `obligations-cyber.md`).

## Gabarit `architecture-securite.md`

```markdown
# Architecture de sécurité

## Synthèse
(niveau ASVS, couches retenues, solutions choisies, écarts acceptés, décisions attendues)

## Principes retenus
## Protections par couche
| ID | Couche | Protection | Solution retenue | Alternative écartée et motif | Menaces couvertes | Coût et exploitation |
|---|---|---|---|---|---|---|
## Segmentation et flux autorisés
(schéma Mermaid)
## Identités et accès
## Secrets et chiffrement
## Sauvegarde et reprise (RTO, RPO)
## Journalisation et supervision
## Écarts et risques résiduels
## Décisions d'architecture liées (ADR)
```

## Pièges

- WAF en simple détection, ou contournable par accès direct à l'origine.
- Sauvegardes accessibles avec les identifiants de la production.
- Protection achetée mais non configurée : exiger une recette de configuration.
- Dosage grand compte imposé à un site vitrine : filtrer par étiquettes.

## Contrôles avant de rendre

- Chaque menace de haut niveau du modèle de menaces a une couche qui la traite.
- Chaque solution a une alternative écartée avec son motif et son coût d'exploitation.
- Le dimensionnement correspond à la taille du projet.
- La décision de solution est tracée en ADR.

## Sources

- OWASP ModSecurity et CRS : https://owasp.org/projects/modsecurity ; https://coreruleset.org/20211222/talking-about-modsecurity-and-the-new-coraza-waf/
- Gartner, Market Guide WAAP 2026 (via éditeurs, cité sous réserve)
- ANSSI, recommandations d'architecture des SI sensibles v1.2 et guide d'hygiène (42 mesures) : https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-recommandations_architectures_systemes_information_sensibles_ou_diffusion_restreinte-v1.2.pdf
- ANSSI, ReCyF v2.5 (17 mars 2026)
- CIS Controls v8.1 et CIS Benchmarks
- NIST SP 800-207 (zero trust), non relu : à vérifier
