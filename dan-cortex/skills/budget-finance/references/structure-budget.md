# Structure du budget : construction et exploitation sur trois ans

Référence du `controleur-financier` pour ne rien oublier dans le coût total (TCO) et pour chiffrer chaque poste avec sa source. Règle d'or : **un poste sans fourchette sourcée reste vide et marqué « non sourcé : devis à obtenir »**, il n'est jamais comblé de tête. État : octobre 2026 ; les fourchettes viennent d'agences et de plateformes (biais commercial, forte dispersion).

## Sommaire
1. Postes de construction
2. Postes d'exploitation
3. Fourchettes par type de projet
4. Coût du développement assisté par agents IA
5. Gabarit de `budget.md`
6. Contrôles avant de rendre
7. Sources

## 1. Postes de construction (année 0 et 1)

| Poste | Fourchette sourcée (date) | Source |
|---|---|---|
| Développeur freelance | junior (0–2 ans) 320 €, confirmé (3–7 ans) 575 €, senior (8+) 670 €+ par jour ; moyenne 520 € ; mobile 550 €, back-end 560 €, front 535 € (2026) | La Fabrique du Net, 8 juil. 2026, cite un baromètre Malt sans méthodologie |
| Confirmé Paris contre régions | 550–680 € (≈ 620 €) contre 450–580 € par jour (8 à 15 % sous Paris) | idem |
| Product owner | 532 € (direct), 581 € (intermédiaire) ; Île-de-France 410 € (< 1 an) à 696 € (> 15 ans) ; autres villes 450–544 € | Free-Work |
| DevOps ou SRE ; PO senior ; design produit senior ; UX senior | 600–950 € (+12 % en un an) ; 550–800 € ; 520–900 € ; 500–780 € par jour | Jobbers (méthodologie non vue) |
| Équipe hors de France | 195–570 € par jour (PO « hors France ») ; Maghreb, Malt, Silkhom : non sourcés | Free-Work |
| Cadrage, spécifications, tests, recette | non sourcé : charges du planning × TJM | — |
| Juridique (CGU, CGV, contrats), DPO et RGPD, sécurité (audit, test d'intrusion, WAF), contenus et traduction, marque et dépôt, design, marketing de lancement (`marketing-commercial`), formation et conduite du changement | non sourcé : un devis par poste, jamais comblé de tête | — |
| Comptes développeur des stores | non retrouvé : à vérifier sur les pages officielles | — |

## 2. Postes d'exploitation (années 1 à 3)

| Poste | Fourchette sourcée (date) | Source |
|---|---|---|
| Maintenance annuelle | 15–20 % du coût de développement (mobile) | Spop (agence) |
| Hébergement et cloud | non sourcé : demander l'estimation à l'`ingenieur-devops` | — |
| Pilotage des coûts cloud | méthode FinOps : visibilité, optimisation, exploitation continue | FinOps Foundation |
| Boutique SaaS (Shopify) | ≈ 36 €/mois (hébergement, SSL inclus) ; thèmes 0–500 € ; domaine ≈ 15 €/an | Shopify FR (éditeur) |
| Paiement en ligne | 1,5 % + 0,25 € (carte standard EEE) à 2,8 % + 0,25 € (premium) ; Managed Payments 3,5 % par transaction réussie (cumul avec d'autres frais : non vérifié) | Stripe, tarifs France et support |
| Commission Apple (UE, annonce août 2026) | achat intégré 26 % (15 % : Small Business Program, Mini Apps/Video Partner, abonnements après la 1re année) ; paiement alternatif 20 % (10 %) ; lien sortant 15 % (10 %) ; hors App Store 5 % (« Core Technology Commission », remplace la redevance par installation) | Apple Newsroom, Apple Developer |
| Commission Google Play (offres externes, EEE) | 10 % abonnements, 20 % autres biens numériques ; 15 % (nouveaux programmes) ; 10 % sur le 1er million de $ annuel ; 1,20 € par installation via lien | Play Console |
| Outils (gestion de projet, design, supervision, analytique), licences et composants (`dependances.md`), support et contenus, renouvellements, sécurité récurrente, marketing d'entretien, assurances et comptabilité | non sourcé : inventaire et devis | — |
| Équipes internes (ERP) | 7 ETP (PME) à 24 ETP (grandes entreprises), rapport 2019 | Panorama |

**Divergence de dates Apple.** FunnelFox (secondaire) date la bascule au 18 août et les frais de store « à partir du 1er octobre », cite Apple (88 % des développeurs UE sans commission) et compte deux restructurations en 2026 : date d'effet à confirmer sur la page Apple Developer, pas sur un blog. Commission standard Google Play (15 ou 30 %) : non retrouvée. Chaque commission figure en hypothèse de variation.

## 3. Fourchettes par type de projet

| Type | Fourchette (2025-2026) | Source et réserve |
|---|---|---|
| Site vitrine PME | 0,9–5 k€ HT ; one-page 0,5–2 k€ | France Num et Afnic, via Sortlist |
| Site grand compte | non sourcé | — |
| E-commerce PME | 3–10 k€ HT (prestataire) ; 5–15 k€ ; > 50 k€ sur mesure avancé | Sortlist ; L'Expert-comptable.com |
| E-commerce, trois ans tout compris | Shopify 15–60 k€, WooCommerce 12–50 k€, PrestaShop 25–120 k€, Adobe Commerce 200 k€+ | upwedo. (agence, PME de 1 à 10 M€ de CA) |
| E-commerce grand compte | non sourcé (seul repère : Adobe Commerce 200 k€+) | — |
| Mobile MVP | 5–30 k€ selon les agences (5–15, 10–25, 10–30) | Sortlist, Spop, Groupe 10X |
| Mobile complexe | 60–150 k€+ ; > 80 k€ sans plafond (marketplace, temps réel, paiement) | Spop, Groupe 10X, Bility |
| MVP SaaS | 15–180 k$+ ; 3 à 5 mois le plus souvent | DevioTech, TexvnX, Devs & Logics (USD) |
| ERP | ≈ 6,1 M$ en moyenne sur cinq ans d'études (date non précisée, miroir Academia) ; durée ≈ 17,4 mois (2018) | Panorama (anciennes éditions) |
| Produit de niche | non sourcé : partir du MVP SaaS ou mobile | — |

MVP SaaS : 20–100 k$ (DevioTech), 15–150 k$+ en 3 à 5 mois (TexvnX), 28–180 k$+ en 4 à 8 semaines (Devs & Logics). Shopify sur mesure : 5–20 k€ ou 3–30 k€ selon la source. Durées par type : non retrouvées, sauf SaaS et ERP.
**ERP.** Ratio 1:1 licences/intégration des éditeurs, « dérisoirement bas » : plancher. Coûts oubliés : conduite du changement, processus, backfilling, infrastructure, dépassement de durée. Coût par utilisateur : non trouvé.

**Sources divergentes.** Les écarts atteignent 1 à 10 entre agences : ils reflètent le périmètre, la localisation des équipes et la finition, pas un prix de marché. Calcul d'après les TJM (hypothèses : 3 développeurs confirmés à 575 €, 1 PO à 532 €, 0,5 designer à 600 €, 80 jours) ≈ 205 k€ ; version réduite à 60 jours (2 développeurs, 0,5 PO, 0,3 designer) ≈ 96 k€. Un MVP SaaS d'équipe française freelance se situe vers 100–200 k€, au-dessus des 15–100 k$ des blogs d'agences. Shopify : 15–60 k€ sur trois ans contre 5–20 k€ de développement suggère une exploitation majoritaire dans le TCO.

## 4. Coût du développement assisté par agents IA

| Élément | Valeur sourcée (juin 2026) |
|---|---|
| Abonnements | Copilot Pro 10 $/mois (1 000 crédits), Max 100 $ ; Cursor Pro 20 $, Pro+ 60 $, Ultra 200 $, Teams 40 $ par utilisateur ; Claude Pro 20 $, Max 100 $ et 200 $ (daily.dev, secondaire) ; plage 10–200 $/mois/développeur |
| Facturation | à l'usage depuis le 1er juin 2026 ; 1 crédit Copilot = 0,01 $ (Morph, secondaire), Pro+ à 39 $ absent de GitHub Docs : à vérifier |
| Prix par token, coût par fonctionnalité | non retrouvés |

- Même à 200 $/mois, le coût direct reste inférieur à une journée de TJM (≈ 550 €) : inscrire un **plafond d'usage par développeur**.
- Gain de productivité : METR, juillet 2025, 19 % de temps en plus (attendu +24 % de vitesse, perçu +20 % : biais de perception) ; METR le juge périmé. Mise à jour du 24 février 2026 : −18 % (intervalle −38 % à +9 %), −4 % pour les nouveaux recrutés, signe à vérifier. Enquête auto-déclarée du 11 mai 2026 : vitesse 3x, valeur 1,4 à 2x. **Ne rien déduire du budget** : tester 0 %, 15 % et 30 % de gain en sensibilité (seuils de travail). Le scénario prudent retient 0 %.
- L'IA réduit la construction, pas l'exploitation ; revue et tests restent budgétés. Qualité du code généré et études à l'échelle d'un projet : non établies.
- Produit qui embarque un modèle : marge brute ≈ 52 % (estimation) contre 77–81 % en SaaS classique (Digital Applied) ; ajouter le coût d'inférence aux postes d'exploitation.

## 5. Gabarit de `budget.md`

```markdown
# Budget — <projet>

## Synthèse
<12 lignes : construction et TCO sur trois ans en trois scénarios, réserves, écart avec le souhaité, décisions, rappel : ne vaut pas avis d'expert-comptable>

## Hypothèses et périmètre
## Scénarios
| Hypothèse | Prudent | Central | Optimiste |
|---|---|---|---|
## Construction
| Poste | Base | Prudent | Central | Optimiste | Source et date |
|---|---|---|---|---|---|
## Exploitation sur trois ans
| Poste | Base | An 1 | An 2 | An 3 | Source et date |
|---|---|---|---|---|---|
## Réserves
## Postes non sourcés et devis à obtenir
## Écart avec le budget souhaité
## Justification économique
<renvoi à justification-economique.md>
```

## 6. Contrôles avant de rendre

- Chaque poste des sections 1 et 2 est chiffré ou marqué non sourcé, avec devise, HT ou TTC, source, date.
- Hébergement repris de `infrastructure.md`, charges de `planning.md` ; trois scénarios.

## Sources

- La Fabrique du Net (8 juil. 2026) ; Free-Work, TJM product owner ; Jobbers, étude TJM.
- Sortlist (France Num, Afnic) ; L'Expert-comptable.com ; upwedo. ; Spop ; Groupe 10X ; Bility ; DevioTech, TexvnX, Devs & Logics.
- Panorama Consulting : coût d'un ERP, ERP Report 2018 et 2026.
- Stripe, tarifs France ; Apple Newsroom (août 2026) ; Play Console (offres externes) ; FunnelFox.
- METR (10 juil. 2025, 24 févr. et 11 mai 2026) ; GitHub Docs ; Morph ; Digital Applied.
