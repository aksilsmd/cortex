# Prix et offre

Cette référence guide la construction d'un prix et d'une offre défendables : méthode de fixation, paliers, essai et gratuité, promotions, lien avec l'économie unitaire. Le prix final reste une décision de l'utilisateur, relue par le contrôleur financier et le juriste.

## Sommaire
1. Séquence de travail
2. Méthodes de fixation du prix
3. Métrique de facturation et packaging
4. Essai et gratuité
5. Promotions
6. Lien avec les indicateurs unitaires
7. Gabarit de `prix-offre.md`
8. Pièges et contrôles

## 1. Séquence de travail

1. Partir de la valeur perçue (voix du client) et des prix du benchmark.
2. Obtenir du contrôleur financier : coût de service par client, marge brute, CAC admissible.
3. Établir la fourchette acceptable (méthode ci-dessous), puis trois paliers lisibles.
4. Choisir essai ou gratuité selon le coût de service.
5. Choisir une métrique de facturation alignée sur l'usage ; rester au forfait tant que l'historique d'usage manque.
6. Faire relire : affichage du prix, reconduction, résiliation, promotions (juriste, à valider).

## 2. Méthodes de fixation du prix

| Situation | Méthode | Limite |
|---|---|---|
| Marché établi, offres comparables | alignement sur le benchmark, écart justifié par la valeur | copie les erreurs des concurrents |
| Prix inconnu, segment accessible | sensibilité au prix de Van Westendorp (1976) : quatre questions (trop bon marché, bonne affaire, cher, trop cher) donnent une fourchette acceptable et un prix optimal | exige un échantillon du segment cible ; déclaratif |
| Valeur économique chiffrable (B2B) | prix en part de la valeur créée pour le client | demande des preuves de gain |
| Coût variable élevé (inférence IA, logistique) | coût complet plus marge cible | plancher, non un prix de marché |
| Produit nouveau sans historique | prix de test sur la bêta, révisé à J+60 | échantillon petit |

Marges : les produits à base d'IA ont des marges plus basses (environ 50 % contre 70 à 80 % pour le SaaS classique, enquête Growth Unhinged 2026 de 230 éditeurs) : le coût d'inférence est un coût marginal non nul.

## 3. Métrique de facturation et packaging

| Modèle | Quand | Condition |
|---|---|---|
| Par siège | valeur proportionnelle au nombre d'utilisateurs | prévisible, mais freine l'adoption |
| Forfait par palier | peu d'historique d'usage ; 37 % des éditeurs sous 5 M$ de revenu récurrent annuel | paliers lisibles |
| Usage ou crédits | valeur proportionnelle à l'usage | facture prévisible pour le client |
| Hybride siège plus usage | tendance 2026 : 37 % des éditeurs, contre 25 % un an avant | rémunération commerciale alignée |
| Résultat | valeur mesurable et attribuable (exemple de marché : 0,99 $ par ticket résolu) | résultat contractuellement défini |

Avant de passer à l'usage ou au résultat : le client peut-il prévoir sa facture ? La rémunération commerciale suit-elle ? Trois éditeurs sur quatre ont changé prix ou packaging en un an : prévoir une revue à J+60.

Packaging : trois paliers au plus, un palier ancre, des différences fondées sur la valeur (limites d'usage, rôles, support, intégrations), pas sur des fonctions artificiellement retirées. Pour un e-commerce : prix, frais de livraison et coût total visibles dès le panier.

## 4. Essai et gratuité

| Critère | Choix |
|---|---|
| Coût de service faible, effet de réseau ou viralité | gratuité limitée (freemium) |
| Valeur perçue rapidement, produit autonome | essai gratuit à durée bornée |
| Valeur lente, intégration nécessaire | démonstration ou preuve de concept payée ou cadrée |
| Coût de service élevé | essai à crédits limités |

Benchmarks de conversion essai vers payant : non trouvés : ne pas en citer sans source. Mesurer en bêta. Carte bancaire demandée à l'essai, reconduction automatique et résiliation relèvent du juriste : information claire et résiliation aussi simple que l'inscription.

## 5. Promotions

- Une promotion a un objectif, une durée, un plafond de remise et un impact calculé sur la marge.
- Pas d'urgence fictive, de stock fictif ni de compte à rebours artificiel.
- Le prix de référence d'une réduction annoncée obéit à une règle légale (prix antérieur) : à valider par le juriste.
- Dates des temps forts (Black Friday 27/11/2026, Cyber Monday 30/11/2026, calculées, non sourcées) et des soldes : à confirmer.
- Piloter la marge après remise et publicité, pas le seul chiffre d'affaires.

## 6. Lien avec les indicateurs unitaires

| Indicateur | Cible de travail | Précaution |
|---|---|---|
| LTV:CAC | supérieur à 3 | ne pas le calculer trop tôt sur peu de données ; suivre le payback |
| Payback du CAC | 12 mois ou moins ; jusqu'à 18 si capital bon marché ; à améliorer au-delà de 24 | source : Skok |
| CAC admissible | (marge brute annuelle × durée de vie) / 3 | hypothèse de durée de vie à justifier |
| Marge brute | différente pour un produit à coût d'inférence | demander les coûts réels |

## 7. Gabarit de `prix-offre.md`

```markdown
# Prix et offre — <projet>

## Synthèse
<12 lignes au plus : métrique de facturation, paliers et prix, essai, CAC admissible, payback, décisions>

## Valeur et références
<valeur perçue (voix du client), prix du benchmark sourcés et datés>

## Fourchette de prix
<méthode retenue, données, limites>

## Paliers et packaging
| Palier | Prix | Contenu | Cible |
|---|---|---|---|

## Essai, gratuité et reconduction

## Promotions prévues
<objectif, durée, plafond, impact marge, mentions>

## Économie unitaire
<coût de service, marge, CAC admissible, LTV:CAC, payback — source : controleur-financier>

## Conformité
<affichage du prix, conditions, résiliation : relu par le juriste le …, à valider>

## Plan de révision
<revue à J+60 : indicateurs déclencheurs>

## Hypothèses et risques
```

## 8. Pièges et contrôles

- Passer à l'usage ou à l'IA sans facture prévisible ni refonte de la rémunération commerciale.
- Changer de prix pour plaire aux investisseurs plutôt que pour la valeur.
- Oublier que les marges IA sont plus basses ; calculer LTV:CAC sur trop peu de données.
- Afficher des frais tardifs : 40 % des abandons de panier (Baymard).
- Avant de rendre : fourchette sourcée, trois paliers au plus, économie unitaire fournie par la finance, prix relu par le juriste.

## Sources

- Skok, For Entrepreneurs : définitions SaaS, LTV, LTV:CAC
- Van Westendorp (1976), échelle de sensibilité au prix
- Bessemer Venture Partners, AI pricing and monetization playbook (10/02/2026)
- Growth Unhinged, état de la monétisation B2B en 2026 (enquête de 230 éditeurs)
- a16z, newsletter entreprise de décembre 2024
- Baymard Institute, abandon de panier
