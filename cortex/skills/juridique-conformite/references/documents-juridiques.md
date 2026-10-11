# Documents juridiques à produire

Plan type de chaque document du pôle, avec ses titres exacts. Chaque document commence par `## Synthèse` (12 lignes au plus) et porte en tête la mention : « Projet à valider par un avocat ; ce document prépare son travail et ne vaut pas conseil juridique ». Les documents destinés au public (mentions, CGU, CGV, confidentialité) sont des projets : ils ne sont publiés qu'après validation et accord explicite de l'utilisateur.

## Sommaire
- Règles communes
- Pré-diagnostic juridique
- conformite-reglementaire.md
- Mentions légales, CGU, CGV
- Politique de confidentialité
- Contrats
- propriete-intellectuelle.md
- dossier-conformite.md
- Contrôles avant de rendre
- Sources

## Règles communes

- Rédiger à partir des faits du dossier (fiche projet, cahier des charges, `dependances.md`, `infrastructure.md`, `prix-offre.md`), pas de modèle générique non adapté. Lorsqu'un fait manque, laisser un champ `[à compléter : …]` et le lister en synthèse.
- Chaque obligation porte son texte, son article et sa date d'application ; chaque point non confirmé, « à vérifier ».
- Chaque document est daté (« état : <mois année> ») et versionné ; une version acceptée par un utilisateur est conservée.
- Langues : un document par langue de marché ; la version arabe fait foi pour l'Algérie (à confirmer par l'avocat local).
- Les identifiants de contrôle (JUR-, PEN-, FIS-, RGP-) sont cités à côté de chaque exigence qu'ils couvrent.

## Pré-diagnostic juridique

`01-decouverte/prediagnostic-juridique.md`, en une à deux pages, avant tout investissement.

```markdown
# Pré-diagnostic juridique — <projet>
## Synthèse
## Qualification du projet
(type, clientèle, territoires, flux d'argent, données, contenus tiers, IA)
## Obstacles bloquants
(activité interdite ou réglementée, pays fermé, agrément requis)
## Obligations structurantes
(tableau : obligation, texte, date, impact produit, coût ordre de grandeur « à chiffrer »)
## Classement des pays
## Risques pénaux saillants
## Avis de professionnels à demander
## Hypothèses et points à vérifier
```

## conformite-reglementaire.md

`03-conception/juridique/conformite-reglementaire.md` : le document pivot du pôle.

```markdown
# Conformité réglementaire — <projet>
## Synthèse
## Périmètre et qualifications
## Obligations commerce et consommation
## Contrats et propriété intellectuelle
## Accessibilité
## Fiscalité et paiements
## Risque pénal et garde-fous
## Politique, sanctions et secteurs
## Territoires (une sous-section par pays, avec étiquette)
## Exigences transmises à la spécification
(tableau : ID de contrôle en première colonne, exigence, RG- ou FN- visés, jalon)
## Veille : textes suivis et dates
## Décisions et oppositions
```

## Mentions légales, CGU, CGV

| Document | Titres exacts |
|---|---|
| `mentions-legales.md` | `## Synthèse`, `## Éditeur`, `## Directeur de la publication`, `## Hébergeur`, `## Activité réglementée et autorité`, `## Propriété intellectuelle`, `## Contact`, `## Données personnelles (renvoi)` |
| `cgu.md` | `## Synthèse`, `## Objet et acceptation`, `## Accès et compte`, `## Règles d'usage et contenus interdits`, `## Contenus des utilisateurs et licence`, `## Propriété intellectuelle`, `## Disponibilité et responsabilité`, `## Suspension et résiliation`, `## Modification des conditions`, `## Droit applicable et juridiction` |
| `cgv.md` | `## Synthèse`, `## Identité du vendeur`, `## Offre, prix et taxes`, `## Commande et confirmation`, `## Paiement`, `## Livraison ou fourniture`, `## Droit de rétractation et fonction « renoncer au contrat ici »`, `## Garanties légales et commerciales`, `## Abonnement, durée et résiliation en ligne`, `## Service après-vente et médiation`, `## Données personnelles (renvoi)`, `## Droit applicable` |

Pour un SaaS B2B, remplacer rétractation et garanties de consommation par SLA, responsabilité, réversibilité. Les CGU ne sont pas imposées par la loi comme les CGV : elles encadrent l'usage et la responsabilité.

## Politique de confidentialité

Rédigée avec `delegue-protection-donnees` sur la base de `donnees-personnelles.md`.

```markdown
# Politique de confidentialité — <projet>
## Synthèse
## Responsable du traitement et contact
## Données collectées, finalités et bases légales
## Destinataires et sous-traitants
## Transferts hors Union européenne
## Durées de conservation
## Vos droits et comment les exercer
## Sécurité
## Cookies et traceurs (renvoi)
## Mise à jour et réclamation
```

## Contrats

`03-conception/juridique/contrats.md` liste les contrats à signer et les clauses clés, sans rédiger de contrat complet sans accord.

```markdown
# Contrats — <projet>
## Synthèse
## Registre des contrats
(tableau : ID, partie, objet, échéance de signature, responsable, statut)
## Contrat client (SaaS ou prestation)
## Contrat prestataire ou agence
## Contrat d'hébergement et de sous-traitance de données
## Contrats des partenaires de paiement et d'influence
## Clauses sensibles (responsabilité, SLA, cession, réversibilité, changement de loi)
## Points à négocier
```

## propriete-intellectuelle.md

Plan dans `contrats-propriete-intellectuelle.md` : `## Synthèse`, `## Titularité du code et des contenus`, `## Marques et noms de domaine`, `## Inventaire des licences tierces`, `## Contenus générés par IA`, `## Contrats à signer et clauses de cession`, `## Points à vérifier`.

## dossier-conformite.md

`05-validation/dossier-conformite.md`, remis à J5 avec la liste des textes recoupés.

```markdown
# Dossier de conformité — <projet>
## Synthèse
(état par domaine, nombre de contrôles faits, non applicables, risques acceptés, oppositions)
## Périmètre et version du produit
## Couverture des contrôles
(tableau : ID en première colonne, statut, preuve, vérificateur)
## Preuves par domaine
(commerce, contrats et PI, pénal, fiscalité et paiements, données personnelles, accessibilité, sécurité)
## Risques acceptés
(nom du décideur, date, motif)
## Écarts et plan de correction
## Veille : textes recoupés et date
## Avis de professionnels obtenus ou à obtenir
```

## Contrôles avant de rendre

- Le rappel « à valider » figure en tête ; aucun article ni montant inventé.
- Aucune marque ni identité réelle d'un tiers n'est présentée comme concurrente ou cliente.
- Les tableaux n'ont pas de barre verticale dans une cellule ; chaque ID est en première colonne.
- `cortex.py docs verifier` ne signale aucune synthèse manquante.

## Sources

- Service-Public F23455 et F33527 ; economie.gouv.fr, « Mentions sur votre site internet ».
- `lancer-projet/references/dossier-projet.md` (emplacements et identifiants).
- `references/commerce-consommation.md`, `contrats-propriete-intellectuelle.md`, `penal-responsabilites.md`.
