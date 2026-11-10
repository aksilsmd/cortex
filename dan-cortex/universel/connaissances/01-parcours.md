# Le parcours Dan-Cortex, étape par étape

Chaque étape a : un but, les équipes mobilisées, ce qui est produit, ce qui est dit à l'utilisateur, et une porte.
On ne franchit pas une porte sans la réponse de l'utilisateur. L'ordre va du plus facile au plus difficile.

## Sommaire
Étape 0 Accueil · 1 Reformulation · 2 Exploration · 3 Propositions · 4 Entretien · 5 Cahier des charges ·
6 Étude de marché · 7 Conception · 8 Étude de réalisation · 9 Décision · Correspondance avec les jalons J0 à J7

## Étape 0 — Accueil
- **But :** mettre à l'aise, obtenir le besoin brut.
- **Équipe :** le noyau seul.
- **Dit à l'utilisateur :** le message d'accueil du skill. Aucune question technique.
- **Porte :** un besoin, même d'une ligne.

## Étape 1 — Reformulation
- **But :** transformer le vrac en besoin clair, sans rien ajouter que l'utilisateur n'ait dit, sauf hypothèses
  signalées.
- **Équipe :** noyau ; `expert-cahier-des-charges` si le texte est long ou contradictoire.
- **Gabarit de la fiche « Votre besoin, reformulé » :**

```
Votre besoin en une phrase : …
Le problème à résoudre : …
Pour qui (utilisateurs, clients) : …
Ce que vous voulez obtenir : …            (3 à 7 résultats concrets)
Ce qui existe déjà chez vous : …
Vos contraintes connues : budget … · délai … · pays … · langues …
Ce que j'ai supposé (à confirmer) : …
Ce qu'il me manque encore : …             (sera demandé à l'étape 4, pas maintenant)
Type de projet reconnu : site · boutique en ligne · application mobile · logiciel en ligne (SaaS) ·
  outil de gestion (ERP) · produit de niche · autre
```
- **Porte :** « Oui, c'est bien cela ». Sinon corriger et remontrer.
- **Trace :** fiche rangée dans `01-cadrage/besoin-reformule.md`.

## Étape 2 — Exploration (se former sur le domaine)
- **But :** que Dan-Cortex connaisse le domaine aussi bien qu'un professionnel du secteur avant d'interroger.
- **Équipes (en parallèle) :** `collecteur-web` (un par concurrent ou source), `analyste-concurrence`,
  `analyste-marche`, `analyste-voix-client`, `analyste-contexte`, `juriste-numerique` (règles du secteur et du
  pays), `architecte-solution` (techniques, projets libres sur GitHub), `concepteur-ux` (parcours et designs
  observés), `controleur-financier` (ordres de grandeur de prix et de coûts). Méthode : `exploration.md`.
- **Produit :** `01-decouverte/dossier-exploration.md` + un résumé « Ce que nous avons appris » (15 lignes).
- **Dit à l'utilisateur avant :** « Je lance N équipes pendant environ X minutes sur : … ».
- **Porte :** aucune décision ; l'utilisateur lit, peut corriger une erreur de compréhension.

## Étape 3 — Propositions
- **But :** revenir avec de la valeur, pas avec des questions.
- **Équipes :** `stratege-produit`, `contradicteur` (objections et angles morts).
- **Produit :** note de propositions : 3 à 5 améliorations de l'idée, 2 ou 3 positionnements possibles (avec pour
  qui, promesse, différence), les manques du marché à saisir, les fonctions « à avoir absolument », « à
  différencier », « à éviter », les risques principaux, et une recommandation motivée.
- **Porte :** l'utilisateur choisit un positionnement ou demande un mélange.

## Étape 4 — Entretien approfondi
- **But :** recueillir tout le besoin, thème par thème. Méthode et banque de questions : `entretien.md`.
- **Équipes :** noyau pour le dialogue ; les experts préparent les réponses suggérées de leur thème.
- **Produit :** `01-cadrage/compte-rendu-entretien.md` (questions, réponses, décisions, points ouverts).
- **Porte :** relecture du compte rendu.

## Étape 5 — Cahier des charges
- **Équipes :** `expert-cahier-des-charges` (rédaction), `concepteur-ux` + `maquettiste` (maquettes prévues),
  `architecte-solution` (architecture et normes), `juriste-numerique`, `controleur-financier`, puis
  `verificateur` (rien d'oublié, rien de contradictoire).
- **Produit :** cahier des charges illustré (structure dans `livrables.md`).
- **Porte :** **validation formelle** par l'utilisateur. Ses remarques sont intégrées et le document remontré.

## Étape 6 — Étude de marché
- **Équipes :** pôle Stratégie et marché (skill `veille-marche`).
- **Produit :** étude de marché autonome, illustrée (structure dans `livrables.md`). Peut être remise dès qu'elle
  est prête, sans attendre la conception.

## Étape 7 — Conception
- **Équipes :** `redacteur-sfg`, `redacteur-sfd`, `redacteur-specs-techniques`, `architecte-solution`,
  `architecte-donnees`, `gardien-des-normes`, `cartographe-interactions`, `maquettiste`, `planificateur`
  (planning de Gantt), `concepteur-tests` (stratégie de test et cahier de recette), `architecte-securite`.
- **Produit :** spécifications fonctionnelles générales et détaillées, spécifications techniques, dossier
  d'architecture, normes de code, maquettes, planning, stratégie de test, analyse de risques.
- **Porte :** validation de la conception (maquettes vues, périmètre de la première version confirmé).

## Étape 8 — Étude de réalisation
- **Équipes :** `controleur-financier`, `planificateur`, `responsable-commercial`. Méthode : `etude-realisation.md`.
- **Produit :** comparaison chiffrée « par IA (Dan-Cortex) », « par une entreprise tierce », « mixte », avec budget
  prévisionnel sur trois ans et gains potentiels dans le temps.

## Étape 9 — À vous de décider
Présenter trois chemins, sans pousser :
1. **Dan-Cortex réalise** : passage au skill `lancer-projet`, jalon J4, par lots validés un à un.
2. **Vous emportez le dossier** : paquet complet prêt à remettre à une entreprise (cahier des charges,
   spécifications, maquettes, planning, grille de comparaison des devis, questions à poser au prestataire).
3. **Vous lancez une startup** : en plus, plan de lancement, offre et prix, plan marketing (skill
   `marketing-commercial`), budget et financements (skill `budget-finance`).
Rappeler ce que chaque chemin coûte et engage. La décision est notée au registre.

## Correspondance avec les jalons du chef d'orchestre
| Étapes d'accueil | Jalon `lancer-projet` |
|---|---|
| 0, 1 | J0 Qualification |
| 2, 3, 6 | J1 Opportunité |
| 4, 5 | J2 Cadrage |
| 7 | J3 Conception |
| 8, 9 | porte entre J3 et J4 |
| réalisation | J4 à J7 |
