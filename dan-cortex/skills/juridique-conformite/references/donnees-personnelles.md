# Données personnelles — méthode de mise en conformité d'un projet

Cette référence guide la mise en conformité RGPD d'un projet, de la cartographie à la violation. Le livrable prépare le travail d'un juriste ou d'un délégué à la protection des données (DPO) ; il ne vaut pas avis juridique. État : octobre 2026.

## Sommaire
1. Cadre et qualification
2. Méthode en huit étapes
3. Gabarits
4. Pièges fréquents
5. Contrôles avant de rendre
6. Sources

## 1. Cadre et qualification

Le RGPD (règlement (UE) 2016/679) est inchangé en octobre 2026. Le volet « données » du Digital Omnibus (proposition du 19 nov. 2025) est bloqué : première lecture, plus de 1 750 amendements au Parlement, mandat du Conseil annulé, aucun trilogue, adoption fin 2026 au plus tôt (source secondaire). Ne bâtir aucune exigence dessus. Seul le volet IA de l'Omnibus est adopté : voir `ia-plateformes.md`.

Les sanctions CNIL visent les fondamentaux : à traiter en exigence « jour 1 ».

| Sanctions CNIL | Faits |
|---|---|
| 2025 | 259 décisions (83 sanctions, 143 mises en demeure) ; amendes d'environ 486,8 M€ (486,6 M€ sur une autre page CNIL : écart à signaler) ; dont 21 cookies, 16 vidéosurveillance, 14 sécurité, 14 droits, 10 prospection ; mises en demeure pour registre et AIPD absents |
| 2026 | Free Mobile 27 M€ et Free 15 M€ (sécurité après fuite ; date non relevée) ; France Travail 5 M€ le 22 janv. (sécurité) ; EXTIA 300 000 € le 21 juil. (droits, effacement, récidive) |
| Procédure simplifiée 2026 | 23 sanctions pour 133 750 € depuis janv. (plafond 20 000 €) : vidéosurveillance, cookies déposés avant action ou refus plus difficile qu'accepter, droits d'accès et d'effacement |

Sous-traitants sanctionnés pour : sécurité, traitement hors instructions, données non supprimées en fin de contrat.

Qualifier le rôle avant tout :

| Situation | Rôle du projet | Conséquence |
|---|---|---|
| Compte, facturation, télémétrie, marketing | Responsable de traitement | Tous les livrables ci-dessous |
| Données des clients d'un SaaS ou d'un ERP | Sous-traitant (art. 28) | Contrat, instructions, registre des catégories ; livrables en double |
| Hébergeur, PSP, outil d'e-mail | Sous-traitant du projet | Contrat art. 28 à obtenir |
| Rôle ambigu ou coresponsabilité | À valider | Avis du juriste |

## 2. Méthode en huit étapes

1. **Cartographier** chaque donnée : source, finalité, systèmes, destinataires, pays, durée. Partir du modèle de données et des écrans. Gabarit 3.1.
2. **Fixer une finalité par traitement,** déterminée et explicite. Scinder une finalité vague (« améliorer nos services »).
3. **Choisir la base légale** (art. 6) : une seule principale par finalité, justifiée par écrit.

| Cas | Base usuelle | Point de vigilance |
|---|---|---|
| Exécuter une commande ou un abonnement | Contrat | Ne couvre pas le marketing |
| Obligation comptable, fiscale | Obligation légale | Durée fixée par le texte (à vérifier) |
| Sécurité, lutte contre la fraude | Intérêt légitime | Test de mise en balance consigné |
| Traceurs publicitaires, newsletters B2C | Consentement (art. 7) | Retrait aussi simple que l'octroi |
| Données sensibles (art. 9) | Consentement explicite ou exception de l'art. 9(2) | AIPD probable ; étiquettes `donnees-sensibles`, `sante` |

4. **Minimiser et protéger dès la conception** (art. 25) : ne collecter que le nécessaire, champs facultatifs signalés, pseudonymisation, accès par rôle, journaux sans donnée inutile. Chaque champ renvoie à une finalité.
5. **Fixer les durées** (art. 5(1)(e)) : durée active, archivage intermédiaire, suppression ou anonymisation. Prévoir la purge dans le code et les sauvegardes. Durées légales : « à vérifier ».
6. **Organiser les droits** (art. 15 à 22) : accès, rectification, effacement, limitation, portabilité, opposition. Réponse sous un mois (art. 12(3)). Prévoir un point d'entrée unique, une vérification d'identité proportionnée, une recherche dans tous les systèmes (sauvegardes, outils tiers). Information : art. 13-14.
7. **Encadrer les sous-traitants** (art. 28) : contrat avec objet, durée, instructions, sécurité, sous-traitants ultérieurs, audit, restitution ou suppression en fin de contrat. Manquements sanctionnés : voir §1. Transferts hors UE : voir `international-donnees.md`.
8. **Décider de l'AIPD** (art. 35-36) et **préparer la violation** (art. 33-34).

**Seuil de l'AIPD.** Consulter les listes de la CNIL (traitements soumis ou non à AIPD ; existence confirmée, contenu non lu : à vérifier). Au moins deux critères du G29 (à vérifier) parmi : données sensibles, grande échelle, personnes vulnérables, croisement de jeux de données, scoring, surveillance systématique, usage innovant. Aucun critère : consigner le motif. Si le risque résiduel reste élevé, consulter l'autorité (art. 36).

**Violation.** Notification à l'autorité sous 72 h après en avoir pris connaissance (art. 33), information des personnes si risque élevé (art. 34). Prévoir un registre des violations, un modèle de notification et une astreinte. Technique : pôle Sécurité.

**DPO** (art. 37-39) : obligatoire pour une autorité publique, un suivi systématique ou des données sensibles à grande échelle (rappel, à valider) ; contact publié et déclaré à la CNIL. **Représentant** dans l'UE si le projet est établi hors UE (art. 27).

## 3. Gabarits

### 3.1 `02-cadrage/cartographie-donnees.md`

```markdown
# Cartographie des données — <projet>
> Prépare le travail du juriste ou du DPO ; ne vaut pas avis juridique.
## Synthèse
Nombre de traitements, de données sensibles, de transferts hors UE ; AIPD : oui, non ou à valider ; points « à vérifier ».
## Rôles
Responsable de traitement ou sous-traitant, par flux.
## Données
| ID | Donnée | Source | Finalité | Base légale | Systèmes | Destinataires | Pays | Durée | Sensible |
|---|---|---|---|---|---|---|---|---|---|
| DON-001 | E-mail du compte | Inscription | Gérer le compte | Contrat | Base clients | Hébergeur | UE | Durée du compte + 3 ans (à vérifier) | non |
## Besoin d'AIPD
Critères retenus, décision, motif.
## Questions ouvertes
```

### 3.2 `03-conception/juridique/registre-traitements.md`

```markdown
# Registre des traitements — <projet>
## Synthèse
Nombre de traitements, rôle, dernière mise à jour, écarts.
## Traitements
| ID | Traitement | Finalité | Base légale | Catégories de personnes | Catégories de données | Destinataires | Transferts hors UE | Durée | Mesures de sécurité | Source DON- |
|---|---|---|---|---|---|---|---|---|---|---|
| TRT-001 | Gestion des comptes | Fournir le service | Contrat | Clients | Identité, e-mail | Hébergeur | Aucun | 3 ans après inactivité (à vérifier) | Chiffrement, accès par rôle | DON-001 |
```

### 3.3 `03-conception/juridique/aipd.md`

```markdown
# Analyse d'impact — <traitement>
## Synthèse
Décision (poursuivre, modifier, consulter l'autorité), risques résiduels, avis du DPO, validateur.
## Description du traitement
## Nécessité et proportionnalité
Finalité, base légale, minimisation, durée, droits, transferts.
## Risques pour les personnes
| ID | Événement redouté | Gravité | Vraisemblance | Mesures | Risque résiduel |
|---|---|---|---|---|---|
## Plan d'action et avis du DPO
```

## 4. Pièges fréquents

- Copier le registre d'un autre projet : il doit refléter les champs réels.
- Invoquer l'intérêt légitime pour du ciblage publicitaire sans mise en balance.
- Oublier sauvegardes, journaux et outils tiers dans l'effacement.
- Traiter un SaaS en simple responsable : les données clients relèvent de l'art. 28.
- Appuyer la conformité sur l'Omnibus « données » : non adopté.
- Négliger la sécurité de base (mots de passe, comptes partagés) : Free 42 M€ cumulés, France Travail 5 M€.
- Produire registre et AIPD après le lancement, sans versions datées.

## 5. Contrôles avant de rendre

- Chaque donnée du modèle figure dans la cartographie, avec finalité, base légale et durée.
- Chaque point non confirmé porte « à vérifier » ; chaque décision d'AIPD est motivée.
- Le rappel « ne vaut pas avis juridique » figure en tête.

## Sources

- RGPD, règlement (UE) 2016/679 : art. 5, 6, 7, 9, 12 à 22, 25, 27, 28, 30, 32 à 39 (rappels de droit stable).
- CNIL, bilan des sanctions 2025 : https://www.cnil.fr/fr/bilan-sanctions-2025
- CNIL, listes des traitements pour lesquels une AIPD est requise ou non : https://www.cnil.fr/fr/listes-des-traitements-pour-lesquels-une-aipd-est-requise-ou-non
- CNIL, sanctions 2026 : https://www.cnil.fr/fr/sanction-free-2026 ; https://www.cnil.fr/fr/sanction-non-respect-droits-personnes-extia ; https://cnil.fr/fr/23-nouvelles-sanctions-simplifiees
- Digital Omnibus « données », proposition du 19 nov. 2025 : statut selon Acompli, 24/09/2026 (source secondaire) : https://acompli.ie/news/digital-omnibus-gdpr-cookies-status-september-2026/
