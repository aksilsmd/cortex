# Justification économique : modèle, seuil, trésorerie, rentabilité

Référence du `controleur-financier` pour démontrer qu'un projet vaut son coût. Règle d'or : **chaque hypothèse de revenu est nommée, datée, et testée en sensibilité ; aucun benchmark n'est inventé.** État : octobre 2026. Les benchmarks SaaS ci-dessous viennent de blogs et d'études d'investisseurs, aux définitions différentes : fixer les formules avant de comparer. Aucun benchmark de conversion, de churn des petites entreprises ni de e-commerce (panier moyen, taux de conversion, FEVAD) n'est établi : ces valeurs viennent de l'utilisateur, d'un test ou restent « à vérifier ».

## Sommaire
1. Modèle économique
2. Indicateurs unitaires et benchmarks
3. Seuil de rentabilité
4. Trésorerie
5. Rentabilité
6. Scénarios et sensibilité
7. Gabarit
8. Contrôles
9. Sources

## 1. Modèle économique

- ecommerce : marge sur ventes ; coûts variables : paiement, logistique, retours, acquisition.
- saas, niche : abonnement, usage ; variables : hébergement, inférence IA, support, paiement.
- mobile : achats intégrés, abonnement, publicité ; variables : commission de store, notifications, support.
- site : leads, ventes, économies (revenu indirect : l'écrire comme tel).
- erp : pas de revenu, raisonner en gains et coûts évités.

Écrire en une page qui paie, pour quoi, combien, à quelle fréquence, par quel canal, avec quelle commission. Le prix vient de `prix-offre.md` : ne pas le fixer ici.

## 2. Indicateurs unitaires et benchmarks

Calculer par script, sur une unité claire (client, commande, abonné).

| Indicateur | Formule | Seuil de lecture |
|---|---|---|
| Marge brute unitaire | prix net − coûts variables (paiement, commission, hébergement, inférence, support) | à partir de la ligne de ventes réelles |
| CAC | dépenses d'acquisition ÷ clients acquis | hypothèse tant qu'aucun canal n'est testé |
| LTV | (revenu moyen × marge brute) ÷ churn ; exemple : (500 × 0,75) ÷ 0,20 = 1 875 $ | churn : hypothèse jusqu'à la mesure |
| LTV ÷ CAC ; délai de récupération | LTV ÷ CAC (CAC de 600 $ : 3,1) ; CAC ÷ (revenu mensuel par client × marge brute) | repères d'investisseur, pas une distribution observée : LTV ÷ CAC ≥ 3 ; délai < 18 mois (mid-market) ou < 24 mois (entreprise) (Bessemer, via pmtoolkit) |

- **Commission.** Sur 10 € de bien numérique, net ≈ 7,40 € (achat intégré Apple à 26 %), 8,50 € (15 %), ≈ 9,60 € (Stripe, carte standard EEE), hors TVA et règles de redirection : la mettre en scénario.
- **IA embarquée.** Remplacer la marge de 77–81 % par ≈ 52 % dans la LTV si le produit appelle un modèle.

**Benchmarks SaaS : les sources divergent, donner les deux valeurs.**

| Indicateur | Valeur A | Valeur B | Valeur C |
|---|---|---|---|
| LTV ÷ CAC médian | 4,1x (Aleph × Benchmarkit, 342 sociétés, exercice 2025) | 3,2x (Optifai, 939 sociétés) | — |
| Délai de récupération | 16 mois (ScaleXP, exercice 2025) | 18 mois (Digital Applied, 2024) | 28 mois (OpenView, via CFO Advisors) |
| Rétention brute | 84 % (ScaleXP, 2025) | 88 % (Digital Applied, 2024) | — |
| Rétention nette (NRR) | 101 % (Digital Applied, 2024) | 103 % (SaaS Capital, via CFO Advisors) | — |
| Ventes-marketing par $ de nouvel ARR | 1,30 $ ; 1,63 $ pour de nouveaux clients (ScaleXP, 2025) | 2,00 $ (Digital Applied, 2024) | — |
| Marge brute médiane | 77 % (total), 81 % (abonnements) (Digital Applied) | ≈ 52 % avec modèle de langage (estimation) | — |

Délai selon la valeur contractuelle annuelle (Digital Applied) : < 15 k$ 8–12 mois ; 15–100 k$ 14–18 mois ; > 100 k$ 18–24 mois et plus. Les écarts tiennent aux définitions, à l'année et à l'échantillon : choisir une valeur, citer l'autre, écrire la formule.

**Pièges.** LTV sur le chiffre d'affaires ; CAC sans salaires (il est entièrement chargé) ; marge de SaaS classique sur un produit à forte inférence.

## 3. Seuil de rentabilité

1. Charges fixes annuelles = exploitation hors coûts variables + amortissement de la construction sur trois ans.
2. Seuil en volume = charges fixes ÷ marge brute unitaire. Pour un abonnement : clients nécessaires = charges fixes annuelles ÷ (revenu annuel par client × marge brute − coûts variables par client). Le traduire en clients, commandes ou abonnés par mois.
3. Date de franchissement : courbe d'acquisition réaliste du plan marketing.
4. Seuil pour chacun des trois scénarios ; s'il n'est atteint dans aucun, le dire en synthèse.

## 4. Trésorerie

- Tableau mensuel sur 36 mois ; le **point bas** du solde cumulé fixe le besoin de financement.
- Décaler les encaissements (délais clients, versements des stores et du paiement : non sourcés, à vérifier) et placer les décaissements lourds à leur date réelle.
- Les aides (`financements-aides.md`) n'entrent qu'une fois octroyées.
- Besoin de financement = point bas du solde cumulé + réserve de gestion.

## 5. Rentabilité de l'investissement

| Mesure | Calcul | Usage |
|---|---|---|
| Valeur actuelle nette (VAN) et taux de rentabilité interne (TRI) | flux de construction et d'exploitation actualisés sur 3 à 5 ans | décider entre options |
| Retour sur investissement | (gains cumulés − coûts cumulés) ÷ coûts cumulés sur trois ans | lecture rapide |
| Délai de récupération | mois où le solde cumulé redevient positif | comparaison avec la trésorerie |
| ERP | gains en heures économisées, erreurs évitées, conformité : à justifier par mesure de l'existant | pas de revenu à modéliser |

- **Taux d'actualisation** : définitions financières standard (non sourcées) ; aucun taux public de référence n'est établi. Ancrage : taux débiteur bancaire aux entreprises de 3,8 % (juin-juillet 2026, BCE), plus une prime de risque de projet à documenter. Un taux inférieur à 3,8 % est difficile à justifier. La BCE a relevé ses taux de 25 points de base le 10 sept. 2026 : revoir le taux après chaque décision.
- **Macro** (sept. 2026) : inflation France 2,3 % en 2026 (Banque de France), zone euro 3,0 % (BCE) ; rémunération par tête +3,3 % au T2 2026. Indexer les TJM pluriannuels d'environ 3 % par an, avec un scénario haut. Isoler les coûts en dollars (cloud, SaaS, tokens) avec un change EUR/USD daté (non sourcé).
- **Projet de l'État** : MAREVA, méthode interministérielle d'analyse de la valeur depuis 2007, a été refondue en 2025. « MAREVA produit » (outils intégrés à Grist) est exigé depuis janvier 2026 pour les dossiers de saisine avant lancement. L'audit « article 3 » (décret 2019-1088) impose l'avis préalable de la DINUM dès 15 M€ de budget prévisionnel en coûts complets (DINUM, 7 août 2026). Ne pas confondre avec MAREVA 2 (Excel, historique). Grille de notation : non retrouvée. Sous 15 M€, garder le principe (lier ressources consommées et impacts attendus, en mode produit) comme gabarit de dossier de décision.

Séparer gains **mesurables** (chiffrés avec une base) et gains **espérés** (image, satisfaction). Seuls les premiers entrent dans le calcul. Actualisation et effets fiscaux : à valider par l'expert-comptable.

## 6. Scénarios et sensibilité

- Trois scénarios, aux hypothèses écrites en tableau : prudent (dérive de 27 % sur la construction, 0 % de gain IA, commission haute, acquisition lente), central, optimiste.
- Sensibilité : faire varier de −30 % à +30 % (seuil de travail) chaque levier (prix, conversion, churn, CAC, commission, coût de construction, gain IA), classer par effet sur la VAN ou le seuil (tornade, par script).
- Les leviers dominants sont les **hypothèses à tester en premier** (maquette, pré-vente, pilote), avec leur jalon.
- Inclure un scénario d'arrêt : coût engagé à chaque jalon go/no-go et ce qui reste récupérable.

## 7. Gabarit (section « Justification économique » de `budget.md`)

```markdown
## Justification économique
### Synthèse
<modèle, marge unitaire, seuil, point bas de trésorerie, retour à trois ans, levier dominant>
### Modèle économique
### Indicateurs unitaires
| Indicateur | Prudent | Central | Optimiste | Source ou « hypothèse » |
|---|---|---|---|---|
### Seuil de rentabilité
### Trésorerie sur 36 mois
### Rentabilité de l'investissement
### Sensibilité
| Levier | Variation | Effet sur le résultat à trois ans | Test prévu |
|---|---|---|---|
### Scénario d'arrêt
```

## 8. Contrôles avant de rendre

- Formules dans un script ou tableur joint ; aucun chiffre de conversion, de churn ou de CAC sans mesure ou « hypothèse ».
- Commissions et marge IA aux indicateurs ; gains espérés séparés des gains mesurables.
- Rappel : le livrable ne vaut pas avis d'expert-comptable ; l'actualisation et la fiscalité sont à valider.

## Sources

- Digital Applied, économie unitaire SaaS 2026 (marge brute 77–81 % contre ≈ 52 % avec LLM).
- Stripe, tarifs France ; Apple Newsroom (août 2026) : commissions utilisées dans l'exemple.
- Panorama Consulting : coûts oubliés et bénéfices ERP.
- DINUM, « MAREVA : refonte de l'audit des grands projets SI de l'État » (7 août 2026), numerique.gouv.fr.
- ScaleXP ; Digital Applied ; CFO Advisors ; pmtoolkit (Bessemer) : benchmarks SaaS 2026.
- Banque de France (15 sept. 2026) ; Bulletin économique de la BCE 6/2026.
- Flyvbjerg et Gardner (2023) : 0,5 % des projets tiennent aussi les bénéfices, via `planification.md`.
- Formules de VAN, TRI : pratique courante, non sourcée, à valider avec l'expert-comptable.
