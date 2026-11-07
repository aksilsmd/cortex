# Formation — UI/UX : recherche, conception, évaluation

Fiche de formation de haut niveau pour concepteur UX, maquettiste, développeurs front et mobile, testeurs et expert accessibilité. Elle complète `recherche-utilisateur.md` (gabarits et niveaux de preuve), `matrice-interactions.md` et `accessibilite.md`. Sources primaires en fin de fiche (consultées le 2026-11-03).

## Sommaire
1. Objectifs
2. Recherche utilisateur : choisir la bonne méthode
3. Personas, parcours, tâches
4. Architecture de l'information
5. Heuristiques de Nielsen
6. Lois de l'UX utiles (et leurs limites)
7. Formulaires
8. Microcopie et messages
9. États : vide, chargement, erreur, succès, hors-ligne
10. Accessibilité WCAG 2.2 AA intégrée à la conception
11. Tests d'utilisabilité : protocole, métriques, SUS
12. Mesure en production : conversion, tâches, indicateurs
13. Check-list d'audit UX
14. Anti-modèles et pièges
15. Sources

## 1. Objectifs

L'agent sait :
- choisir une méthode de recherche adaptée à la question et au budget, et qualifier le niveau de preuve d'un constat ;
- structurer navigation et vocabulaire à partir des données (tri de cartes, test d'arborescence) ;
- évaluer une interface avec les 10 heuristiques et noter la gravité ;
- concevoir formulaires, messages et états sans angle mort ;
- monter un test d'utilisabilité et en tirer des métriques (réussite, temps, SEQ, SUS) ;
- relier chaque décision UX à un indicateur mesurable en production.

## 2. Recherche utilisateur : choisir la bonne méthode

Deux axes (NN/g) : attitudinal (ce que les gens disent) / comportemental (ce qu'ils font) ; qualitatif (pourquoi) / quantitatif (combien).

| Question | Méthode | Effectif indicatif |
|---|---|---|
| Quels besoins, quel contexte, quel vocabulaire ? | entretiens semi-directifs, observation contextuelle | 5–8 par segment, jusqu'à saturation |
| Les gens réussissent-ils la tâche ? pourquoi échouent-ils ? | test d'utilisabilité qualitatif | ≈ 5 par itération et par profil |
| Combien réussissent, en combien de temps ? comparer deux versions | test quantitatif | ≈ 40 par variante (NN/g) |
| Comment les utilisateurs regroupent-ils les contenus ? | tri de cartes ouvert | ≈ 15 |
| Trouvent-ils l'information dans l'arborescence ? | test d'arborescence (tree test) | ≥ 50 recommandés pour des taux stables |
| Quelle est l'ampleur d'une attitude ? | questionnaire | dépend de la marge d'erreur visée (≈ 100+ pour ±10 %) |
| Quel est le comportement réel à l'échelle ? | analytique, A/B test | calcul de puissance statistique préalable |

Règles :
- « 5 utilisateurs » vaut pour un test qualitatif itératif sur un profil homogène : il révèle l'essentiel des problèmes fréquents, pas les problèmes rares ni des statistiques. Tester 3 fois 5 vaut mieux qu'une fois 15.
- Recruter sur des critères de comportement (fréquence d'achat en ligne, usage du back-office), pas sur la démographie seule. Toujours 1 profil « de bord » (faible littératie numérique, lecteur d'écran, petit écran, connexion lente).
- Distinguer preuve (observé chez des utilisateurs réels), indice (données indirectes, analytique, verbatims d'avis), hypothèse (opinion d'équipe). Un agent ne simule jamais un entretien et ne présente jamais des personas inventés comme issus d'une étude.
- Consentement et données personnelles : information, finalité, durée de conservation des enregistrements, anonymisation des verbatims (voir pôle juridique).

Guide d'entretien (structure) : contexte → dernière fois que… (récit concret) → difficultés → contournements → outils actuels → attentes. Questions ouvertes, pas de question suggestive (« Est-ce que ce serait pratique si… ? » est interdit), pas de démonstration du produit pendant l'entretien de découverte.

## 3. Personas, parcours, tâches

Persona utile :
- objectif principal, contexte d'usage (appareil, lieu, interruption), compétences, freins, critères de choix, citation réelle ; relié aux exigences qu'il justifie ; niveau de preuve indiqué.
- Pas de détails décoratifs (hobbies, photo de banque d'images) qui n'orientent aucune décision.
- 3 à 5 personas, dont un principal (celui pour qui on arbitre) et au moins un persona de bord.
- Alternative légère : « jobs to be done » — « Quand [situation], je veux [motivation], pour [résultat attendu] ».

Carte de parcours : étapes × (actions, pensées, émotions, points de contact, irritants, opportunités). Toujours partir de l'état actuel observé avant de dessiner l'état cible.

Tâches clés : liste des 5 à 10 tâches qui portent la valeur (et le chiffre d'affaires), chacune avec un critère de réussite observable. Elles servent ensuite aux tests et aux indicateurs (§11–12).

## 4. Architecture de l'information

- Vocabulaire des utilisateurs, pas de l'organisation (« Mes commandes », pas « Gestion des flux de vente »).
- Profondeur : préférer une arborescence large et peu profonde à une arborescence étroite et profonde, tant que chaque niveau reste scannable et que les libellés sont distincts.
- Tri de cartes ouvert (découvrir les catégories) → arborescence candidate → test d'arborescence (valider la trouvabilité) → navigation.
- Indicateurs du test d'arborescence : taux de réussite par tâche, réussite directe (sans retour arrière), premier clic. Viser ≥ 80 % de réussite sur les tâches clés ; un premier clic erroné prédit fortement l'échec.
- Navigation : position courante toujours visible (onglet actif, fil d'Ariane sur les sites profonds), recherche pour les catalogues > ~50 éléments, pas de libellés « fourre-tout » (« Divers », « Ressources »).
- Constance (WCAG 3.2.3, 3.2.4) : même navigation, même ordre, mêmes noms d'une page à l'autre. Aide constante (3.2.6, niveau A en 2.2) : le lien vers l'aide/contact est au même endroit sur chaque page qui le propose.

## 5. Heuristiques de Nielsen

| # | Heuristique | Question d'audit |
|---|---|---|
| 1 | Visibilité de l'état du système | L'utilisateur sait-il toujours ce qui se passe (chargement, enregistrement, étape) ? |
| 2 | Correspondance système / monde réel | Mots, icônes et ordre sont-ils ceux de l'utilisateur ? |
| 3 | Contrôle et liberté | Peut-il annuler, revenir, quitter sans perte ? |
| 4 | Cohérence et standards | Les conventions de la plateforme et du produit sont-elles respectées ? |
| 5 | Prévention des erreurs | L'interface empêche-t-elle l'erreur (contraintes, valeurs par défaut, confirmation de l'irréversible) ? |
| 6 | Reconnaissance plutôt que rappel | Les options et informations nécessaires sont-elles visibles ? |
| 7 | Flexibilité et efficacité | Raccourcis pour experts sans gêner les novices ? |
| 8 | Esthétique et design minimaliste | Chaque élément affiché sert-il la tâche ? |
| 9 | Aide à reconnaître, diagnostiquer et corriger les erreurs | Les messages disent-ils quoi, pourquoi, comment corriger ? |
| 10 | Aide et documentation | L'aide est-elle trouvable, contextuelle, orientée tâche ? |

Gravité (échelle de Nielsen) : 0 pas un problème ; 1 cosmétique ; 2 mineur ; 3 majeur (à corriger en priorité) ; 4 catastrophe (bloquant, à corriger avant mise en production). Noter selon fréquence × impact × persistance. Une évaluation heuristique se fait à 3–5 évaluateurs indépendants, puis consolidation ; un évaluateur seul trouve une minorité des problèmes.

## 6. Lois de l'UX utiles (et leurs limites)

| Loi | Énoncé | Application | Limite |
|---|---|---|---|
| Fitts | Temps d'atteinte ∝ log₂(distance/taille + 1) | Cibles grandes et proches des actions fréquentes ; bords et coins d'écran faciles à atteindre à la souris | Sur tactile, la zone du pouce compte autant |
| Hick-Hyman | Temps de décision ∝ log₂(n + 1) choix | Réduire et grouper les options, divulgation progressive | Ne s'applique pas à une liste triée connue (recherche dans une liste alphabétique) |
| Jakob | Les utilisateurs passent l'essentiel de leur temps sur d'autres sites | Suivre les conventions (panier en haut à droite, logo → accueil) | Innover seulement là où le gain est démontré |
| Miller (7 ± 2) | Capacité de la mémoire de travail | Ne pas exiger de mémoriser entre écrans | Souvent mal cité : ce n'est pas une limite de 7 éléments par menu |
| Seuil de Doherty | Productivité accrue quand la réponse est < 400 ms | Retour immédiat, optimisme d'interface | — |
| Temps de réponse (Nielsen) | 0,1 s : instantané ; 1 s : flux de pensée préservé ; 10 s : limite d'attention | < 1 s : pas d'indicateur ; 1–10 s : indicateur ; > 10 s : progression avec estimation et possibilité d'annuler | — |
| Tesler | Toute complexité irréductible doit être portée par quelqu'un | La porter côté système (valeurs par défaut, déduction) | — |
| Von Restorff | L'élément différent est mémorisé | Un seul élément saillant par zone (le CTA) | La saillance par la couleur seule est inaccessible |
| Pic-fin | On juge une expérience sur son pic et sa fin | Soigner confirmation, erreurs, fin de tunnel | — |
| Position sérielle | Premiers et derniers éléments mieux retenus | Actions clés en début/fin de barre de navigation | — |
| Gradient d'objectif | L'effort s'accélère près du but | Progression visible dans les tunnels | — |
| Esthétique-utilisabilité | Une interface belle est perçue plus utilisable | — | Masque des problèmes en test : observer le comportement, pas l'avis |

## 7. Formulaires

Règles opérationnelles :
- Demander le minimum : chaque champ justifié par un usage (et par une base légale s'il s'agit de données personnelles).
- Une colonne ; un champ par ligne (exceptions : code postal + ville, date en 3 champs si nécessaire).
- Libellé visible au-dessus du champ, toujours présent ; aide sous le libellé, avant le champ ; placeholder seulement pour un exemple de format.
- Marquer les champs obligatoires et les facultatifs (texte « facultatif » plutôt qu'un astérisque seul, ou astérisque expliqué en tête).
- Largeur du champ proportionnelle à la longueur attendue.
- `autocomplete` normalisé sur tous les champs d'identité, d'adresse et de paiement (WCAG 1.3.5) ; `type`/`inputmode` adaptés.
- Formats souples à l'entrée (espaces, tirets acceptés dans téléphone, IBAN, carte), normalisés côté système.
- Validation : à la sortie du champ ou à la soumission, jamais à la première frappe ; message à côté du champ, relié par `aria-describedby`, et résumé d'erreurs en tête lors de la soumission avec liens vers les champs ; focus déplacé sur le résumé ou le premier champ en erreur.
- Ne jamais effacer la saisie après une erreur ; ne pas redemander ce qui a été fourni (3.3.7).
- Authentification (3.3.8, AA) : pas de test cognitif sans alternative ; autoriser le collage et les gestionnaires de mots de passe ; codes à usage unique avec `autocomplete="one-time-code"` ; passkeys proposées quand le produit les supporte.
- Boutons : verbe explicite (« Créer mon compte ») ; un seul primaire ; « Annuler » en lien ou bouton secondaire.
- Formulaires longs : découpés en étapes logiques avec indicateur, sauvegarde automatique, reprise possible.

Code — champ accessible avec erreur :
```html
<label for="cp">Code postal</label>
<p id="cp-aide" class="aide">5 chiffres, par exemple 75011</p>
<input id="cp" name="cp" inputmode="numeric" autocomplete="postal-code"
       aria-describedby="cp-aide cp-err" aria-invalid="true">
<p id="cp-err" class="erreur">Le code postal doit contenir 5 chiffres. Vous avez saisi 4 chiffres.</p>
```

## 8. Microcopie et messages

- Clarté avant originalité ; phrases courtes ; voix active ; vocabulaire de l'utilisateur ; tutoiement ou vouvoiement décidé une fois pour tout le produit.
- Message d'erreur = ce qui s'est passé + pourquoi (si utile) + comment corriger. Jamais d'accusation (« Vous avez fait une erreur »), jamais de code technique seul (« Erreur 500 »), jamais d'humour sur une erreur coûteuse (paiement, perte de données).
  - Mauvais : « Saisie invalide. »
  - Bon : « La date de naissance doit être au format JJ/MM/AAAA, par exemple 07/03/1990. »
- Confirmation d'action destructrice : titre = question avec l'objet (« Supprimer le projet "Atelier" ? »), conséquence (« Les 12 fichiers seront supprimés définitivement »), boutons verbes (« Supprimer » / « Conserver »), pas « OK/Annuler ».
- Préférer l'annulation a posteriori (toast « Message archivé — Annuler ») à la confirmation a priori pour les actions réversibles.
- Libellés de liens explicites hors contexte (WCAG 2.4.4) : pas de « Cliquez ici », « En savoir plus » seuls.
- Nombres, dates, monnaies formatés selon la langue (`Intl`) ; pluriels gérés par règles ICU, pas par concaténation.
- Prévoir +30 à +40 % de longueur pour les traductions depuis l'anglais (davantage pour les chaînes courtes).

## 9. États : vide, chargement, erreur, succès, hors-ligne

Chaque écran et chaque composant de données a ces états, maquettés et testés :

| État | Contenu attendu |
|---|---|
| Vide (première utilisation) | Explication de la valeur + action principale (« Ajoutez votre premier produit ») ; illustration facultative |
| Vide (résultat de filtre/recherche) | Ce qui a été cherché + suggestions (élargir, corriger, effacer les filtres) |
| Chargement < 1 s | Rien (éviter le clignotement) ; au-delà de ~300 ms, indicateur discret |
| Chargement 1–10 s | Squelette fidèle à la mise en page ou indicateur ; zone annoncée `aria-busy` |
| Chargement > 10 s | Progression déterminée, estimation, possibilité d'annuler ou de continuer ailleurs |
| Erreur | Message humain, action (« Réessayer »), données conservées ; distinguer erreur réseau, droit, serveur |
| Partiel | Ce qui a chargé reste utilisable ; la partie en échec le dit |
| Succès | Confirmation proportionnée (toast pour une action mineure, page pour une commande) avec prochaine étape |
| Non autorisé | Pourquoi et comment obtenir l'accès ; jamais une page blanche |
| Hors-ligne | Bandeau d'état, actions mises en file avec indication, synchronisation visible au retour |

Messages d'état non focalisés (ajout au panier, résultats filtrés) : annoncés aux lecteurs d'écran par une région `role="status"` (WCAG 4.1.3, AA).

## 10. Accessibilité WCAG 2.2 AA intégrée à la conception

L'accessibilité se conçoit en maquette ; elle ne se « rajoute » pas au développement. Annoter chaque maquette : structure de titres, repères (`header`, `nav`, `main`, `footer`), ordre de focus, nom accessible des icônes, alternative des images, comportement au clavier, annonces dynamiques.

Points de conception à fort impact (critère WCAG 2.2) :
- Contrastes 1.4.3 / 1.4.11 ; pas d'information par la couleur seule 1.4.1.
- Redistribution à 320 px 1.4.10 ; zoom texte 200 % 1.4.4 ; espacement de texte 1.4.12.
- Tout au clavier 2.1.1, sans piège 2.1.2 ; ordre de focus logique 2.4.3 ; focus visible 2.4.7 et non masqué 2.4.11.
- Titres de page uniques 2.4.2 ; titres et libellés descriptifs 2.4.6 ; lien d'évitement 2.4.1.
- Cibles ≥ 24 × 24 px 2.5.8 ; alternative au glisser 2.5.7 ; nom accessible contenant le libellé visible 2.5.3.
- Erreurs identifiées et suggestions 3.3.1 / 3.3.3 ; libellés 3.3.2 ; saisie redondante évitée 3.3.7 ; authentification accessible 3.3.8.
- Aide constante 3.2.6 ; pas de changement de contexte au focus ou à la saisie 3.2.1 / 3.2.2.
- Médias : sous-titres 1.2.2, pas de lecture automatique sonore > 3 s sans contrôle 1.4.2 ; animations : pause des mouvements automatiques > 5 s 2.2.2, pas plus de 3 flashs par seconde 2.3.1.
- 4.1.1 « Parsing » a été retiré de WCAG 2.2 : ne plus le citer.

Le détail de l'audit (outils, lecteurs d'écran, grille, RGAA) est dans `accessibilite.md`.

## 11. Tests d'utilisabilité : protocole, métriques, SUS

Protocole (test modéré, 45–60 min) :
1. Objectifs et hypothèses écrits ; tâches clés (§3) ; critères de réussite définis avant le test.
2. Recrutement selon le profil (§2) ; consentement ; rémunération éventuelle.
3. Pilote avec une personne pour corriger les tâches ambiguës.
4. Accueil : « on teste l'interface, pas vous » ; réflexion à voix haute ; ne pas aider, ne pas guider (répondre à une question par une question).
5. Tâches formulées en scénarios réalistes sans les mots de l'interface (« Vous voulez offrir… » plutôt que « Cliquez sur Ajouter au panier »).
6. Après chaque tâche : SEQ ; à la fin : SUS et questions ouvertes.
7. Analyse : problèmes × fréquence × gravité ; vidéos courtes des moments clés ; recommandations priorisées.

Métriques :
| Mesure | Définition | Repère |
|---|---|---|
| Taux de réussite | tâches réussies sans aide / tâches tentées | moyenne inter-études ≈ 78 % (Sauro) ; viser ≥ 80–90 % sur les tâches critiques |
| Temps sur tâche | médiane ou moyenne géométrique (distributions asymétriques) | comparer à une référence ou à la version précédente |
| Erreurs | nombre et type par tâche | — |
| SEQ (Single Ease Question) | « Globalement, cette tâche était… » 1 (très difficile) à 7 (très facile) | moyenne ≈ 5,5 |
| SUS (System Usability Scale) | 10 affirmations alternées positives/négatives, échelle 1–5 | score 0–100 ; moyenne ≈ 68 |
| Taux d'abandon de tâche | tâches abandonnées / tâches tentées | — |

Calcul du SUS : items impairs → (réponse − 1) ; items pairs → (5 − réponse) ; somme × 2,5. Le score n'est pas un pourcentage. Interprétation indicative : < 51 très médiocre, 68 moyen, > 80 bon (quartile supérieur). Le SUS mesure la perception globale ; il ne dit pas quoi corriger.

Code — calcul SUS :
```python
def sus(reponses):  # 10 réponses de 1 à 5, dans l'ordre du questionnaire
    assert len(reponses) == 10
    total = sum((r - 1) if i % 2 == 0 else (5 - r) for i, r in enumerate(reponses))
    return total * 2.5
```

Test non modéré à distance : utile pour le volume et les métriques ; scénarios encore plus précis, questions de contrôle d'attention, vérification de la qualité des enregistrements.

## 12. Mesure en production : conversion, tâches, indicateurs

- Cadre HEART (Google) : Happiness (satisfaction, SUS/CSAT), Engagement, Adoption, Retention, Task success ; pour chaque dimension → objectif → signal → métrique.
- Entonnoirs : taux de passage à chaque étape (liste → fiche → panier → tunnel → confirmation) ; comparer par appareil et par source.
- Taux de conversion = conversions / sessions (ou visiteurs) sur une période, toujours avec le dénominateur explicité.
- Réussite de tâche observable : création de compte achevée, premier projet créé (activation), délai jusqu'à la première valeur.
- Signaux de friction : clics de rage, retours arrière, champs le plus souvent en erreur, recherches sans résultat, contacts au support par motif.
- A/B test : hypothèse écrite, métrique principale unique, taille d'échantillon calculée avant, durée ≥ un cycle hebdomadaire complet, pas d'arrêt dès que « ça a l'air significatif ».
- Consentement aux traceurs (CNIL/RGPD) : mesure d'audience exemptée seulement si configurée selon les conditions de la CNIL ; sinon consentement préalable (voir pôle juridique).
- Signaux Web Vitals (performance perçue) : LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 au 75e centile.

## 13. Check-list d'audit UX

Recherche et cadrage
- [ ] Chaque persona a une source et un niveau de preuve ; au moins un persona de bord.
- [ ] Tâches clés listées avec critère de réussite observable.
- [ ] Arborescence validée par test d'arborescence ou, à défaut, marquée hypothèse.

Interface
- [ ] Évaluation heuristique faite (≥ 3 évaluateurs ou marquée limitée), gravités 3–4 traitées.
- [ ] Conventions de plateforme respectées ; position courante visible.
- [ ] Formulaires : libellés visibles, obligatoires/facultatifs marqués, `autocomplete`, validation à la sortie du champ, données conservées.
- [ ] Messages d'erreur : quoi + comment corriger, sans jargon.
- [ ] États vide, chargement, erreur, partiel, succès, non autorisé, hors-ligne maquettés pour chaque écran de données.
- [ ] Actions destructrices : annulation ou confirmation explicite avec l'objet.

Accessibilité
- [ ] Maquettes annotées (titres, repères, ordre de focus, noms accessibles, annonces).
- [ ] Contrastes, cibles, focus, redistribution vérifiés en conception.

Mesure
- [ ] Test d'utilisabilité prévu avant développement des parcours critiques (paiement, inscription, récupération de compte).
- [ ] SEQ et SUS collectés ; réussite et temps sur tâche rapportés.
- [ ] Indicateurs de production définis (entonnoir, activation, erreurs), compatibles avec le consentement.

## 14. Anti-modèles et pièges

- Personas fictifs présentés comme des résultats de recherche ; persona « tout le monde ».
- Demander aux utilisateurs ce qu'ils veulent au lieu d'observer ce qu'ils font ; questions suggestives.
- Tester avec des collègues ou avec l'équipe projet.
- Conclure en pourcentages sur 5 participants.
- Placeholders comme libellés ; validation agressive pendant la frappe ; boutons désactivés muets.
- Modèles trompeurs (dark patterns) : case précochée, confirmation culpabilisante (« Non, je n'aime pas économiser »), désabonnement caché, urgence factice. Ils sont aussi un risque juridique (DSA, droit de la consommation).
- Squelettes de chargement pour des réponses de 100 ms (clignotement) ; animations décoratives bloquantes.
- « On ajoutera l'accessibilité plus tard ».
- A/B tests arrêtés au premier résultat favorable ; métriques de vanité (pages vues) sans lien avec la tâche.

## 15. Sources

Consultées le 2026-11-03.
- NN/g, 10 Usability Heuristics : https://www.nngroup.com/articles/ten-usability-heuristics/
- NN/g, Severity Ratings for Usability Problems : https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/
- NN/g, When to Use Which UX Research Methods : https://www.nngroup.com/articles/which-ux-research-methods/
- NN/g, Why You Only Need to Test with 5 Users : https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- NN/g, Quantitative Studies: How Many Users to Test : https://www.nngroup.com/articles/quantitative-studies-how-many-users/
- NN/g, Card Sorting: How Many Users : https://www.nngroup.com/articles/card-sorting-how-many-users-to-test/
- NN/g, Response Times: The 3 Important Limits : https://www.nngroup.com/articles/response-times-3-important-limits/
- NN/g, Error-Message Guidelines : https://www.nngroup.com/articles/error-message-guidelines/
- Laws of UX (Fitts, Hick, Jakob, Doherty, Tesler…) : https://lawsofux.com/
- MeasuringU (J. Sauro), SUS et SEQ : https://measuringu.com/sus/ et https://measuringu.com/seq10/
- W3C, WCAG 2.2 : https://www.w3.org/TR/WCAG22/
- W3C WAI, What's New in WCAG 2.2 : https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Baymard, Checkout flow UX optimization (formulaires, erreurs) : https://baymard.com/blog/checkout-flow-ux-optimization
- Google, HEART framework (K. Rodden et al.) : https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/
- web.dev, Web Vitals : https://web.dev/articles/vitals
