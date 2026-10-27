# Profil — ERP full stack (type `erp`)

Lu par le chef d'orchestre à J0 pour qualifier le projet et composer l'équipe. État : octobre 2026.

## Ce qui distingue ce type de projet

- Les échecs viennent d'inadéquations découvertes tard, de sur-personnalisation, de reprise de données et de conduite du changement, pas de la technologie. Panorama (2026 ERP Report, 4 mars 2026) : plus d'un quart des organisations dépassent leur budget ; un chiffre de « 189 % » circule via un revendeur, absent du communiqué : **à vérifier**.
- En France s'ajoutent facturation électronique, fichier des écritures comptables (FEC) et, si encaissement, certification des logiciels de caisse.
- Développer son propre ERP peut faire de l'entreprise l'« éditeur » au sens fiscal (**à valider**).

## Étiquettes à poser

`fr`, `b2b`, `progiciel` (cas par défaut) ou `code`, `migration`, `integrations`, `donnees-perso` (salariés, clients), `finance`, `multilingue` et `international` selon les filiales, `grand-compte`, `paiement` si caisse ou encaissement.

## Acheter, configurer ou construire

| Option | Cas par défaut en PME ? | Vigilance |
|---|---|---|
| Configurer un progiciel (Odoo, ERPNext, Dolibarr, Business Central, NetSuite, Sage) | oui | viser un maximum de standard et gouverner chaque écart |
| Construire | seulement pour un cœur métier unique | coûts de conformité (FEC, Factur-X, caisse) budgétés |

Critères : TCO, écart au standard chiffré, localisation France, intégrateur expérimenté dans le secteur. Rechercher les « fatal misfits » **avant signature**, par démonstrations sur scénarios réels. Versions et prix d'ERPNext, Dolibarr, Dynamics 365, NetSuite, Sage : non vérifiés, **à vérifier**.

## Prérequis propres à ce type

1. Sponsor exécutif nommé, comité de pilotage régulier.
2. Processus actuels et cibles cartographiés avant le choix.
3. Équipe projet dédiée : métier, informatique, intégrateur.
4. Migration de données : nettoyage, mapping, plusieurs répétitions, rapprochement comptable.
5. Intégrations inventoriées (banque, paie et DSN, e-commerce, WMS, plateforme agréée), chacune avec un responsable.

## Agents à renforcer et livrables spécifiques

- `integrateur` : paramétrage, reprise de données ; `architecte-donnees` : modèle et gouvernance.
- `expert-cahier-des-charges`, `redacteur-sfg`, `redacteur-sfd` : processus, écarts au standard.
- `concepteur-tests` et `recetteur` : cycles complets (order-to-cash, procure-to-pay) et pilote.
- `responsable-support-formation` : formation par rôle avant et après la mise en production, conduite du changement.
- `juriste-numerique` : conformité France ; `controleur-financier` : bénéfices suivis 6 à 12 mois.
- Livrables : registre des écarts validés en comité, plan de migration avec répétitions, plan de retour arrière et d'hypercare.

## Exigences des plateformes et des tiers

- Facturation électronique (source secondaire, page officielle illisible : **à vérifier**) : dès le 1er septembre 2026, toutes les entreprises doivent pouvoir recevoir ; grandes entreprises et ETI émettent ; PME et micro dès le 1er septembre 2027 ; format structuré ou hybride (Factur-X) via une plateforme agréée.
- FEC : art. L. 47 A-I du LPF et A. 47 A-1, 18 premières colonnes réglementées (BOFIP).
- Caisse : un logiciel doté d'une fonction de caisse doit garantir inaltérabilité, sécurisation, conservation et archivage ; modifié au point d'altérer ces garanties, le certificat est invalidé. La certification par organisme accrédité était prévue au 1er septembre 2026 ; la loi de finances 2026 la rétablit après sa suppression : le BOFIP d'octobre 2025 est dépassé sur ce point. **À valider.**
- SAP : maintenance standard d'ECC jusqu'à fin 2027, étendue payante jusqu'à fin 2030 (EHP 6-8).
- Odoo 20 (septembre 2026, résumé tiers) : règles d'accès refondues, modules sur mesure à revoir avant migration ; localisation française non détaillée.

## Pièges et causes d'échec fréquentes

- Les huit causes de Panorama : technologie avant les personnes, processus non gérés, attentes irréalistes, direction peu impliquée, ressources inadéquates, formation insuffisante, sur-personnalisation, reprise de données tardive.
- Conformité française découverte à la fin ; confusion entre échéances SAP 2027 et 2030.
- Recette limitée aux fonctions au lieu de cycles complets.

## Planning type

Aucune durée type établie. Séquence : cartographie et choix → conception des écarts → paramétrage par lots → migration répétée (chemin critique probable, hypothèse) → recette par cycles → pilote → formation → bascule, hypercare, suivi des bénéfices 6 à 12 mois.

## Sources

- Panorama Consulting, 2026 ERP Report et « Why ERP projects go over budget ».
- SAP Support, stratégie de maintenance ; Odoo 20 via Ecosire (secondaire).
- BOFIP, FEC et logiciels de caisse ; economie.gouv.fr, certification caisse.
- Previssima, facturation électronique 2026 (secondaire).
- Notes `specificites_par_type_de_projet.md`, §6, état au 11 octobre 2026.
