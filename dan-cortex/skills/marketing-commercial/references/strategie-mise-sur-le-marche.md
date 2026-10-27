# Stratégie de mise sur le marché

Cette référence fixe la méthode pour décider qui viser, quoi dire, comment croître et par paliers de quelle ampleur lancer. Elle s'appuie sur les analyses du pôle Stratégie et marché, qu'on lit sans les refaire.

## Sommaire
1. Cible
2. Positionnement et message
3. Modèle de croissance
4. Paliers de lancement
5. Gabarit de `strategie-marche.md`
6. Gabarit de `plan-marketing.md`
7. Pièges et contrôles

## 1. Cible

1. Relire la note d'opportunité, la voix du client et le benchmark : en extraire les irritants, les segments et les concurrents. Ne pas relancer de collecte.
2. Écrire le **client idéal (ICP)** : profil, déclencheur d'achat, problème, alternative actuelle, raison de choisir ce produit. Un seul segment prioritaire.
3. En B2B, cartographier le comité d'achat : il compte 5 à 16 personnes sur jusqu'à quatre fonctions, et 74 % des équipes montrent un conflit interne (Gartner, mai 2025). Un message par rôle : décideur, utilisateur, financeur, technique, juridique.
4. Nommer les segments écartés et pourquoi : cela évite l'élargissement spontané.

## 2. Positionnement et message

| Élément | Règle |
|---|---|
| Phrase de positionnement | pour [ICP] qui [problème], [produit] est [catégorie] qui [bénéfice], contrairement à [alternative] |
| Preuve | chaque promesse a une preuve vérifiable (démonstration, chiffre sourcé, cas réel) ; sinon elle est retirée |
| Message par rôle | un bénéfice, une preuve, un appel à l'action par rôle d'achat |
| Différenciation | fondée sur ce que le benchmark montre que les concurrents font mal ou ne font pas |

Toute allégation (performance, comparaison, environnement, « meilleur », « gratuit », « garanti ») est listée dans le tableau des allégations du plan marketing et relue par le juriste (à valider). Les allégations environnementales sont particulièrement surveillées en 2026 : la directive « Empowering consumers » est annoncée applicable fin septembre 2026 (à vérifier, source non lue en entier).

## 3. Modèle de croissance

| Critère | Modèle dominant |
|---|---|
| SaaS, application, niche à essai simple | produit (essai ou gratuité, activation guidée) |
| ERP, grand compte, valeur de contrat élevée | vente et marketing de comptes (ABM) |
| Niche à public passionné | communauté, construction en public |
| Valeur de contrat croissante | hybride : produit pour l'entrée, vente pour l'expansion |

Même en produit-led, construire la capacité commerciale avant d'en avoir besoin (cas Twilio). Définir **une métrique de référence (North Star)** par produit, ses leviers et sa cible à J+90 : une seule, propre à la stratégie.

## 4. Paliers de lancement

| Palier | Période | Public | Condition pour passer au suivant |
|---|---|---|---|
| Lancement discret | J-60 à J-30 | 20 à 100 utilisateurs ciblés | part de « très déçus » mesurée, au moins 40 % |
| Bêta ouverte ou liste d'attente | J-30 à J0 | liste consentie, communauté | rétention stable, support prêt |
| Disponibilité générale | J0 | marché visé | payback sous 18 mois sur les canaux ouverts |

Pas d'acquisition payante tant que le seuil de 40 % n'est pas atteint (hypothèse de travail sur ~100 startups, à adapter à un projet non startup). Le budget d'un canal est un budget test avant d'être un budget d'échelle.

## 5. Gabarit de `strategie-marche.md`

```markdown
# Stratégie de mise sur le marché — <projet>

## Synthèse
<12 lignes au plus : ICP, positionnement, modèle de croissance, canaux, prix envisagé, paliers, décisions à prendre>

## Entrées lues
<fichiers amont et dates ; contradictions relevées>

## Cible
### Client idéal
### Comité d'achat et message par rôle
### Segments écartés

## Positionnement
<phrase, preuves, différenciation>

## Modèle de croissance et métrique de référence

## Canaux envisagés
<canal, rôle, indicateur, budget test (hypothèse)>

## Modèle de prix envisagé
<métrique, ordre de grandeur, à confirmer dans prix-offre.md>

## Paliers de lancement et seuils

## Risques et hypothèses
```

## 6. Gabarit de `plan-marketing.md`

```markdown
# Plan marketing — <projet>

## Synthèse
<12 lignes au plus : objectifs à J+90, canaux retenus, budget, mesure, risques juridiques, décisions>

## Objectifs chiffrés à J+90
<métrique de référence, activation, coût d'acquisition cible, payback>

## Message et allégations
<tableau : allégation, preuve, source, statut juridique à valider>

## Canaux et budgets
<renvoie à acquisition-par-type.md : canal, budget test, indicateur, seuil de coupure>

## Plan de marquage et mesure
<événements, consentement, outil, recette>

## Marque et réputation
<nom, ton, avis, crise>

## Calendrier J-90 à J+90
<renvoie à plan-de-lancement-marketing.md>

## Conformité
<grille prospection, influence, avis, cookies : validée par le juriste le …>

## Risques, hypothèses, décisions en attente
```

## 7. Pièges et contrôles

- Acheter de l'acquisition avant d'avoir 40 % de « très déçus », ou avec un payback au-delà de 18 à 24 mois.
- Refaire l'étude de marché au lieu de la lire ; changer de segment sans décision tracée.
- Un seul interlocuteur dans un grand compte : le conflit du comité est ignoré.
- Trop de chantiers à la fois, produit et marketing : post-mortem courant.
- Avant de rendre : ICP unique, phrase de positionnement, métrique de référence, seuils de passage chiffrés, tableau des allégations relu par le juriste, aucune dépense lancée.

## Sources

- Product Hunt, guides de lancement : producthunt.com/launch (consulté en octobre 2026)
- First Round Review, « How Superhuman built an engine to find product-market fit »
- First Round Review, leçons de Twilio sur le go-to-market
- Gartner, communiqué du 7 mai 2025 sur les comités d'achat B2B
- CB Insights, raisons d'échec des startups (millésime non vérifié)
