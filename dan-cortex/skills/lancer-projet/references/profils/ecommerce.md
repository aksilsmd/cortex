# Profil — site e-commerce (type `ecommerce`)

Lu par le chef d'orchestre à J0 pour qualifier le projet et composer l'équipe. État : octobre 2026.

## Ce qui distingue ce type de projet

- Le risque se concentre dans les intégrations (PIM, OMS ou WMS, ERP), les retours, la fraude et le paiement, plus que dans la vitrine.
- Le marché français a pesé environ 196 Md€ en 2025 selon la Fevad (relayé par un média, 175,3 Md€ annoncés pour 2024 : écart de périmètre possible, à vérifier).
- 2026 impose des chantiers datés : fonction de rétractation, droit de douane, checkout Shopify, facturation électronique pour le B2B.

## Étiquettes à poser

`b2c` et/ou `b2b`, `paiement`, `comptes`, `donnees-perso`, `integrations`, `fr` ou `ue`, `international` si vente hors UE, `multilingue`, `abonnement` si récurrent, `marketplace` si vendeurs tiers, `ugc` si avis, `progiciel` si solution du marché, `migration` si reprise de catalogue et de clients, `mineurs` si produits concernés.

## Acheter, configurer ou construire

| Option | À retenir si | Vigilance |
|---|---|---|
| SaaS (Shopify) | délai prioritaire, besoins standards | checkout cadré par la plateforme |
| Composable (commercetools, Medusa, Adobe Commerce) | équipe d'ingénierie, B2B ou multi-marques | coût d'intégration et d'exploitation |
| Open source (PrestaShop, WooCommerce, Sylius) | maîtrise du code | maintenance et sécurité à charge |

Gartner MQ Digital Commerce 2025 (3 nov. 2025) : Adobe Leader, VTEX Challenger. Non couverts : PIM, OMS ou WMS, Mirakl, antifraude, tarifs, état de PrestaShop, WooCommerce, Sylius, BigCommerce : **à vérifier**. Critères : équipe, B2B, volumes, international, intégrations. Documenter le choix.

## Prérequis propres à ce type

1. Prestataire de paiement retenu, 3-D Secure 2 et exemptions testés, webhooks idempotents.
2. Règles antifraude et traitement des litiges configurés avant ouverture.
3. Catalogue, stocks et prix : source de vérité unique décidée.
4. Logistique, retours et remboursements spécifiés de bout en bout.
5. Entité vendeuse, TVA et mentions de vente validées par un professionnel (**à valider**).

## Agents à renforcer et livrables spécifiques

- `integrateur` et `redacteur-specs-techniques` : flux PIM, boutique, OMS ou WMS, ERP (stocks, prix, commandes, retours).
- `architecte-securite`, `testeur-intrusion` : paiement et comptes ; `automaticien-tests` : test de charge avant soldes.
- `juriste-numerique` : conditions générales de vente, rétractation, droit de la consommation ; `delegue-protection-donnees` : cookies, marquage.
- `expert-acquisition` : suivi de conversion compatible avec le checkout ; `responsable-support-formation` : service client.
- Livrables : cahier des flux d'intégration, plan de continuité, fonction de rétractation testée.

## Exigences des plateformes et des tiers

- Depuis le 19 juin 2026, l'interface de vente à distance doit offrir une fonction de rétractation clairement identifiable (ordonnance n° 2026-2, relayée par des cabinets ; texte primaire non lu : **à valider**).
- Shopify : `checkout.liquid` non supporté pour Information, Livraison, Paiement (Shopify Dev). Pages Thank you et Order status à migrer avant le 26 août 2026, selon un éditeur d'application, non confirmé par Shopify : **à vérifier**.
- SCA (PSD2) en vigueur dans l'EEE depuis le 14 septembre 2019 (Stripe).
- Droits de douane UE : 3 € par article dès le 1er juillet 2026 sur les envois ≤ 150 € (source secondaire, à vérifier).
- B2B : facturation électronique, réception dès le 1er septembre 2026 (voir profil `erp`).

## Pièges et causes d'échec fréquentes

- Découvrir tard la rétractation, le checkout Shopify ou le droit de douane.
- Sous-estimer intégrations, retours et fraude.
- Casser le suivi de conversion en changeant de checkout.
- Oublier le test de charge et la supervision avant les soldes et le Black Friday.
- Ignorer TVA et guichet OSS à l'international (à valider).

## Planning type

Aucune durée type établie. Séquence : choix de plateforme et de prestataire de paiement → modèle de catalogue et flux d'intégration → boutique et checkout → intégrations (chemin critique probable, hypothèse) → recette avec paiements réels de test, retours, charge → ouverture avant la période de pointe, avec marge.

## Sources

- Fevad, chiffres clés du e-commerce ; Gartner MQ Digital Commerce 2025.
- Shopify Dev, `checkout.liquid` ; Stripe, 3-D Secure.
- Village de la Justice et ek avocat, fonction de rétractation (juin 2026).
- Notes `specificites_par_type_de_projet.md`, §2, état au 11 octobre 2026.
