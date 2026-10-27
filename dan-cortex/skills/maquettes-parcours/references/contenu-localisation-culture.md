# Contenu, localisation, culture, éthique d'interface, sobriété

Ce fichier couvre ce que dit l'interface, dans quelles langues et pour quels marchés, sans manipuler et sans gaspiller. Livrable : `03-conception/design/contenu-localisation.md`. Les mentions légales et promesses commerciales sont validées par le juriste.

## Sommaire
1. Microcopie et messages d'erreur
2. Internationalisation (i18n)
3. Écriture de droite à gauche
4. Adaptation culturelle par marché
5. Interfaces trompeuses à proscrire
6. Sobriété numérique
7. Gabarit de `contenu-localisation.md`
8. Pièges et contrôles avant de rendre

## 1. Microcopie et messages d'erreur

1. **Définir voix et ton** (3 à 5 adjectifs, avec un exemple « oui / non » chacun), puis un lexique : un concept = un mot (« Panier » et jamais « Caddie » ailleurs).
2. **Libellé d'action = verbe + objet** (« Envoyer le lien »), jamais « OK » ou « Valider » seul.
3. **Erreur = cause + action**, dite sans reproche et sans jargon : « L'adresse e-mail doit contenir @, par exemple nom@domaine.fr ». Le texte exact est celui de la colonne « Erreurs et états » de la matrice : une seule source.
4. **Messages sans fuite** : connexion et récupération de compte ne révèlent pas si un compte existe.
5. **Langage clair** : phrases courtes, mots courants ; version FALC pour les publics qui le requièrent.
6. **États vides** qui proposent l'action suivante ; confirmations qui disent ce qui s'est passé et la suite.
7. **Inclusion** : formulaires sans genre obligatoire, formulations épicènes, un champ « nom complet » plutôt que prénom et nom séparés, adresses et noms non occidentaux acceptés.

## 2. Internationalisation (i18n)

| Règle | Détail |
|---|---|
| Chaînes externalisées | aucune phrase dans le code ; une clé par chaîne avec contexte pour le traducteur (écran `EC-`, longueur maximale, variables) |
| Pas de concaténation | l'ordre des mots change selon la langue : une phrase entière avec variables |
| Format unique par projet | ICU MessageFormat ou MessageFormat 2 (déclaré stable avec CLDR 47, mars 2025) : choisir et le noter dans une ADR |
| Pluriels | règles CLDR par langue : le polonais a des formes « few » et « many », l'arabe une forme « zéro » ; dans ICU, `select` à l'extérieur, `plural` à l'intérieur |
| Formats locaux | dates, nombres, monnaies, téléphones, adresses via CLDR et `Intl`, jamais codés en dur |
| Extension du texte | prévoir de la marge : un libellé traduit peut être nettement plus long (allemand, finnois) ; pas de largeur fixe ; vérifier par **pseudo-localisation** en recette |
| Langue | `lang` sur la page et sur chaque passage étranger ; choix de langue mémorisé, accessible sur chaque écran, libellé dans sa propre langue |
| Contenu non textuel | images sans texte incrusté, symboles testés, exemples adaptés |

Une traduction machine non relue ne s'emploie ni pour le juridique ni pour la santé. Commencer par les langues et marchés de la première version : décision de type 1, comité de cadrage.

## 3. Écriture de droite à gauche

Applicable aux projets étiquetés `rtl` (arabe, hébreu, persan, ourdou).

1. `lang` et `dir="rtl"` sur la page ; propriétés CSS logiques (`margin-inline-start`) au lieu de gauche/droite.
2. Refléter la mise en page, la navigation, les barres de progression ; refléter **seulement** les icônes directionnelles (flèche, retour) ; ne pas refléter logos, horloges, lecteurs multimédias, icônes de produits.
3. **Isolation bidirectionnelle** des nombres, URL, e-mails, noms latins et références (`bdi` ou `dir="auto"`) ; champs de numéros de téléphone et de carte en sens gauche-droite.
4. Polices couvrant l'écriture, interlignage ajusté, pas d'italique ni de capitales simulées.
5. Tableaux, graphiques, curseurs et pagination relus dans le sens inversé.
6. Faire maquetter les écrans clés en variante miroir dès J3, et **relire par un locuteur natif**. Le RTL traité en fin de projet coûte cher.

## 4. Adaptation culturelle par marché

« Maghreb » ou « Europe » ne sont pas des marchés : un marché = un pays, une langue ou des langues, des usages. Les dimensions de Hofstede (distance hiérarchique, individualisme, masculinité, contrôle de l'incertitude, orientation long terme, indulgence) servent d'**hypothèses à valider par recherche locale**, jamais de stéréotypes. Valider auprès d'au moins 5 utilisateurs locaux avant de figer la direction artistique.

| Domaine | À examiner par marché |
|---|---|
| Couleurs, symboles, images | pas de sens universel ; vérifier avec des locuteurs |
| Paiement | moyens réellement utilisés, à fonder sur des données locales vérifiées |
| Formats | adresses, noms, téléphone, calendrier, premier jour de la semaine |
| Confiance | preuves attendues : avis, labels, mentions, paiement à la livraison |
| Ton | formel ou familier, vouvoiement, titres |
| Contenu sensible | religion, politique, humour, représentations |

Paiements (octobre 2026, sources secondaires, **à vérifier avant décision**) : rails locaux en Europe (iDEAL aux Pays-Bas, Bancontact en Belgique), PayPal en Allemagne, cartes en France ; portefeuilles et paiement échelonné aux États-Unis ; paiement à la livraison encore dominant en Algérie, avec cartes CIB et Edahabia. Maroc, Tunisie : non établi, à vérifier.

## 5. Interfaces trompeuses à proscrire

Cadre : DSA art. 25 (plateformes en ligne, interfaces qui trompent ou manipulent), RGPD pour les données, lignes directrices EDPB 03/2022 v2.0. Le juriste précise ce qui s'applique au projet. Digital Fairness Act : proposition attendue au T4 2026, à suivre (état : octobre 2026).

Six catégories EDPB, à croiser avec chaque écran :

| Catégorie | Exemples à proscrire |
|---|---|
| Overloading | harcèlement par demandes répétées, labyrinthe de réglages |
| Skipping | options protectrices cachées, valeurs par défaut défavorables |
| Stirring | culpabilisation (« Non, je préfère payer plus cher »), fausse urgence, stock ou compte à rebours fictif |
| Obstructing | résiliation plus difficile que l'inscription, impasse |
| Fickle | interface incohérente qui déroute, emplacements changeants |
| Left in the dark | information partielle, langue différente selon l'étape |

Règles de conception : refuser aussi simple qu'accepter, au même niveau visuel ; se désabonner aussi court que s'abonner ; aucune case précochée ; prix TTC dès la liste ; aucun compte à rebours ou stock fictif. Ajouter à la matrice, pour les écrans à risque, une mention « risque : <catégorie> » dans « Erreurs et états ». **Mineurs possibles** : analyse de risque, assurance de l'âge conforme aux lignes directrices de la Commission du 14 juillet 2025 (l'auto-déclaration ne suffit pas), réglages protecteurs par défaut (compte privé, notifications limitées, ni lecture automatique ni défilement infini).

## 6. Sobriété numérique

Référentiels : RGESN 2024 (version 2, 28 mai 2024, 9 familles ; famille UX/UI : pas de lecture automatique ni de défilement infini, parcours optimisé, composants natifs, polices et notifications limitées), GR491, ISO/IEC 21031:2024 (Software Carbon Intensity). Gestes : poids de page annoncé, images au bon format, une ou deux familles de polices, mode économe en données. Impact social : illectronisme, alternative non numérique, appareils d'entrée de gamme.

## 7. Gabarit de `contenu-localisation.md`

````markdown
# Contenu et localisation — <projet>

## Synthèse
<langues et marchés, format de messages, nombre de chaînes, revue des interfaces trompeuses (résultat), points de vigilance culturelle, hypothèses non validées>

## Voix, ton et lexique
## Messages d'erreur et états
| Clé | Écran | Élément | Texte | Cause + action |
## Langues et marchés
| Marché | Langue | Sens | Paiements | Formats | Statut de validation |
## Revue des interfaces trompeuses
| Écran | Catégorie EDPB | Constat | Correction |
## Sobriété
Critères RGESN retenus, budget de poids.
````

## 8. Pièges et contrôles avant de rendre

- Phrases concaténées ; pluriels codés « s » ; dates en dur ; texte dans les images.
- Hofstede pris pour un portrait de peuple ; « Maghreb » traité comme un marché.
- Messages d'erreur différents dans la maquette, la matrice et le code.
- Contrôles : tous les `EL-` à message ont leur clé ; une langue relue par un natif ; revue des six catégories consignée.

## Sources
- DSA art. 25 : https://www.eu-digital-services-act.com/Digital_Services_Act_Article_25.html
- EDPB, lignes directrices 03/2022 v2.0 (février 2023) sur les interfaces trompeuses.
- Commission européenne, lignes directrices art. 28 DSA (14 juillet 2025).
- CLDR 47 : http://blog.unicode.org/2025/03/unicode-cldr-47-release-messageformat-2.html
- RGESN 2024 : https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/ ; GR491 : https://gr491.isit-europe.org/
