# Profil — SaaS (type `saas`)

Lu par le chef d'orchestre à J0 pour qualifier le projet et composer l'équipe. État : octobre 2026.

## Ce qui distingue ce type de projet

- Trois sujets structurent l'architecture dès le premier jour : l'isolation des clients (tenants), la préparation aux grands comptes (SSO, SCIM, journaux d'audit, droits) et la facturation récurrente avec taxation internationale.
- Les ajouter après coup coûte cher : l'isolation en particulier.

## Étiquettes à poser

`b2b`, `abonnement`, `paiement`, `comptes`, `donnees-perso`, `international` si vente hors du pays d'établissement, `grand-compte` si cible entreprise, `integrations` (API publique, SSO), `ia` le cas échéant, `code`, et `donnees-sensibles`, `sante` ou `finance` selon le secteur.

## Acheter, configurer ou construire

| Choix | Options | Critère |
|---|---|---|
| Isolation | silo (pile dédiée), pool (infra partagée), bridge (mixte) | conformité exigée par les clients, coût par client, rayon d'impact |
| SSO, SCIM, journaux | construire ou acheter une brique | délai et complexité : les schémas SCIM varient selon Okta, Entra, Google |
| Facturation | prestataire de paiement seul, ou marchand d'enregistrement (MoR) | qui porte taxes, remboursements et litiges |
| Départ de produit | modèle de démarrage (starter kit) | un modèle comme celui de Vercel est « intentionnellement minimal » : ni SSO, ni SCIM, ni facturation à l'usage |

Défaut raisonnable (déduction) : pool avec identifiant de tenant et contrôles d'accès, option silo ou bridge pour comptes régulés, décidée avant le premier client entreprise. Acheter SSO, SCIM et audit plutôt que les construire. Avec Stripe en simple prestataire, l'entreprise reste marchand d'enregistrement ; Stripe Managed Payments déplace ce rôle (par transaction, marché ou produit), au prix d'une commission plus élevée (TVA : **à valider** par un expert-comptable). Mesure d'usage, API publique, SLA, Paddle, Chargebee : non couverts, **à vérifier**.

## Prérequis propres à ce type

1. Modèle d'isolation décidé, documenté et testé contre les fuites entre tenants.
2. Identifiant de tenant propagé dans requêtes, journaux, caches, files et stockage.
3. Choix prestataire de paiement ou MoR tranché avant le premier client étranger.
4. Onboarding et offboarding de tenant (export, suppression) spécifiés.
5. SLA, page de statut et procédure d'incident définis.

## Agents à renforcer et livrables spécifiques

- `architecte-solution` et `architecte-donnees` : isolation, modèle de données par tenant.
- `architecte-securite` et `auditeur-securite` : tests d'isolation, journaux d'audit immuables ; `testeur-intrusion` avant les grands comptes.
- `responsable-commercial` : plans, essais, prix ; `controleur-financier` : indicateurs unitaires.
- `ingenieur-devops` : supervision, SLA ; `responsable-support-formation` : support client.
- Livrables : ADR sur l'isolation, matrice « enterprise readiness », réponses aux questionnaires de sécurité (politiques, schémas, sous-traitants).

## Exigences des plateformes et des tiers

- Liste d'attentes grands comptes (WorkOS, éditeur de briques) : SSO SAML et OIDC par organisation, SCIM, journaux d'audit exportables avec rétention d'un an ou plus, RBAC, portail d'administration.
- SOC 2 Type 1 : 3 à 6 mois ; Type 2 : observation de 3 à 12 mois, 6 à 15 mois au total, renouvellement annuel (sources d'éditeurs d'outils). Ne jamais présenter un Type 1 comme un Type 2. Une certification est délivrée par un auditeur qualifié : **à valider**.
- ISO 27001 : non couvert, à vérifier.

## Pièges et causes d'échec fréquentes

- Isolation ajoutée après coup.
- SSO et SCIM sous-estimés.
- SOC 2 démarré après le gros contrat : l'observation du Type 2 est incompressible.
- Taxes internationales improvisées.
- Quotas appliqués côté client plutôt que côté serveur ; offboarding oublié.

## Planning type

Aucune durée type établie. Séquence : décision d'isolation et de facturation → socle (comptes, tenants, facturation) → fonctions cœur → préparation grands comptes (SSO, SCIM, audit) → SOC 2 lancé en parallèle, bien avant le premier gros contrat → ouverture progressive. Chemin critique probable : socle multi-tenant (hypothèse).

## Sources

- AWS, « SaaS tenant isolation strategies » (silo, pool, bridge).
- WorkOS, « Enterprise readiness checklist 2026 ».
- Drata et Scrut, calendrier SOC 2 (éditeurs).
- Stripe, merchant of record et Managed Payments ; Vercel, Next.js SaaS starter.
- Notes `specificites_par_type_de_projet.md`, §4, état au 11 octobre 2026.
