# Contrôles — accessibilité

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| ACC-001 | J2 | bloquant | tous | - | Le niveau d'accessibilité visé (WCAG 2.2 AA, RGAA le cas échéant) est décidé et consigné, avec l'avis du juriste si une obligation s'applique | 03-conception/design/accessibilite.md | WCAG 2.2 ; RGAA 4.1.2 |
| ACC-002 | J3 | majeur | tous | - | Les exigences d'accessibilité sont déclinées par composant du système de design : bouton, champ, modale, tableau, navigation, média | 03-conception/design/accessibilite.md | WCAG 2.2 ; RGAA 4.1.2 |
| ACC-003 | J3 | bloquant | tous | - | Les contrastes de chaque paire de couleurs de chaque thème sont calculés et atteignent 4,5:1 pour le texte et 3:1 pour les composants | 03-conception/design/design-system.md | WCAG 2.2 critères 1.4.3 et 1.4.11 |
| ACC-004 | J3 | majeur | tous | - | Le focus visible est défini pour chaque composant interactif et n'est jamais masqué par un en-tête ou un bandeau fixe | 03-conception/design/accessibilite.md | WCAG 2.2 critère 2.4.11 |
| ACC-005 | J3 | majeur | tous | - | Les cibles interactives font au moins 24 par 24 pixels CSS, ou disposent d'un espacement suffisant autour d'elles | 03-conception/design/accessibilite.md | WCAG 2.2 critère 2.5.8 |
| ACC-006 | J3 | majeur | tous | - | Toute action possible par glissement ou glisser-déposer dispose d'une alternative au clic ou à l'appui simple | 03-conception/design/accessibilite.md | WCAG 2.2 critère 2.5.7 |
| ACC-007 | J3 | bloquant | tous | comptes | L'authentification n'impose aucun test cognitif et autorise le collage ainsi que les gestionnaires de mots de passe | 03-conception/design/accessibilite.md | WCAG 2.2 critère 3.3.8 |
| ACC-008 | J3 | majeur | tous | - | Aucune information déjà fournie n'est redemandée dans un même parcours, et l'aide est placée au même endroit sur tous les écrans | 03-conception/design/accessibilite.md | WCAG 2.2 critères 3.3.7 et 3.2.6 |
| ACC-009 | J3 | majeur | tous | - | Les erreurs de formulaire sont en texte, reliées à leur champ, annoncées aux lecteurs d'écran et résumées en tête de formulaire | 03-conception/design/accessibilite.md | WCAG 2.2 critère 3.3.1 |
| ACC-010 | J3 | majeur | tous | - | Les maquettes annotent le nom accessible, l'ordre de focus, les repères de page et le lien d'évitement de chaque écran | 03-conception/design/maquettes/cahier-maquettes.md | WCAG 2.2 critères 2.4.1 et 4.1.2 |
| ACC-011 | J3 | majeur | tous | - | Les modales déplacent le focus, le piègent, se ferment par Échap et rendent le focus à l'élément déclencheur | 03-conception/design/accessibilite.md | WCAG 2.2 critère 2.4.3 |
| ACC-012 | J3 | majeur | tous | - | La mise en page reste lisible à 320 px de large et avec un texte agrandi à 200 % sans perte de contenu | 03-conception/design/accessibilite.md | WCAG 2.2 critères 1.4.4 et 1.4.10 |
| ACC-013 | J3 | majeur | tous | - | Médias et mouvements : alternatives textuelles, sous-titres, aucune lecture automatique, et respect de prefers-reduced-motion | 03-conception/design/accessibilite.md | WCAG 2.2 critères 1.1.1, 1.2 et 2.2.2 |
| ACC-014 | J5 | bloquant | tous | - | Un audit d'accessibilité du produit construit porte sur un échantillon couvrant les parcours critiques, tous les gabarits et tous les rôles | 05-validation/rapport-accessibilite.md | WCAG 2.2 ; RGAA 4.1.2 |
| ACC-015 | J5 | bloquant | tous | - | Les parcours critiques sont accomplis au clavier seul et avec un lecteur d'écran, sans blocage ni piège de focus | 05-validation/rapport-accessibilite.md | WCAG 2.2 critères 2.1.1 et 2.1.2 |
| ACC-016 | J5 | majeur | tous | - | Les anomalies d'accessibilité bloquantes sont corrigées et contre-testées ; les autres figurent au plan de correction avec une échéance | 05-validation/rapport-accessibilite.md | bonne pratique |
| ACC-017 | J5 | majeur | tous | - | Le rapport combine outils automatiques, tests manuels et lecteurs d'écran, et précise ce qui n'a pas été testé | 05-validation/rapport-accessibilite.md | bonne pratique |
| ACC-018 | J5 | majeur | mobile | - | Les parcours critiques de l'application sont testés avec VoiceOver sur iOS et TalkBack sur Android | 05-validation/rapport-accessibilite.md | bonne pratique |
| ACC-019 | J5 | majeur | tous | fr | La grille RGAA 4.1.2 est renseignée critère par critère et la déclaration d'accessibilité est préparée pour validation du juriste | 05-validation/rapport-accessibilite.md | RGAA 4.1.2 |
