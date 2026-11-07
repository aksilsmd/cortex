# Contrôle visuel — liste de contrôle, protocole de capture et régression

## Synthèse

- Un écran n'est pas « conforme » parce que son code passe les tests : il l'est quand sa capture, comparée à la maquette, ne présente aucun écart bloquant.
- Cette fiche fixe la règle de fusion : **tout écran nouveau ou modifié est capturé et comparé à la maquette avant fusion.**
- Elle donne une liste de contrôle à identifiants `VIS-`, un protocole multi-écrans (tailles, états, thèmes, langues), une régression visuelle par capture de référence, et un verdict.
- Cas de référence : une page de connexion où le champ e-mail occupe toute la largeur, le mot de passe est étroit, le bouton « Afficher » est détaché du champ et le conteneur est absent. Ce défaut a traversé une revue design : la liste le décrit ligne à ligne (`VIS-CHA-01`, `VIS-ALI-02`, `VIS-MAQ-01`).
- Les seuils chiffrés sont des repères de départ marqués « à valider » ; les règles de forme et de procédure sont obligatoires.

## Principes

1. **La maquette fait foi pour la conformité ; la capture de référence fait foi pour la non-régression.** Deux comparaisons distinctes, deux questions distinctes : « est-ce ce qui a été dessiné ? » et « est-ce ce qui était déjà validé ? ».
2. **Regarder avant de mesurer.** Un agent lit la capture et la maquette côte à côte avant tout test automatique. Un écart flagrant se voit à l'œil ; une mesure seule le manque si on ne la cherche pas.
3. **Chaque état est un écran.** Un champ en erreur, un bouton désactivé, un écran de chargement sont des captures à part entière.
4. **Les tolérances sont explicites et versionnées.** Aucune tolérance implicite ; toute mise à jour d'une référence est relue, jamais acceptée à l'aveugle.
5. **Un écart sans gravité est un écart non classé.** Chaque constat reçoit `bloquant`, `majeur` ou `mineur`, avec une capture et un identifiant.
6. **Le contenu est fictif.** Données de test anonymisées, aucune donnée personnelle réelle dans les captures.

## Règle de fusion : tout écran nouveau ou modifié

1. Un lot qui crée ou modifie un écran (page, composant de formulaire, état, gabarit, thème) n'est pas fusionné tant que :
   - toutes les captures prévues par la matrice de ce protocole ont été produites pour cet écran ;
   - l'agent `testeur-visuel` a comparé chaque capture à sa maquette et rendu une note avec verdict ;
   - aucun constat `bloquant` n'est ouvert ; les constats `majeur` sont corrigés ou acceptés par écrit par le PO, avec motif.
2. Si l'écran n'a pas de maquette, le lot est bloqué avant fusion : le constat est « maquette absente », pas « conforme ». Le PO décide alors s'il faut la produire ou accepter l'écran sans référence.
3. Une modification d'un composant partagé (champ, bouton, carte) déclenche la capture de **tous** les écrans qui l'utilisent, pas seulement de celui qui a été touché.

## Protocole de capture multi-écrans

### Matrice minimale

| Axe | Valeurs | Remarque |
|---|---|---|
| Largeur de fenêtre | 375 px (téléphone), 768 px (tablette), 1280 px (ordinateur portable), 1920 px (grand écran) | les quatre tailles, même si la maquette n'en montre qu'une |
| État | par défaut, focus clavier, saisie, erreur de validation, désactivé, chargement, succès | un état absent de la maquette se signale : « état non maquetté » |
| Thème | clair, sombre si le produit en propose un | le thème sombre est un écran à part entière |
| Langue | français, et langue à écriture de droite à gauche si le produit en propose une | voir `VIS-RTL` |
| Préférence de mouvement | réduite | les animations ne doivent pas changer la mise en page finale |

Pour une page de connexion, la matrice complète fait 4 tailles × (1 état par défaut + focus + erreur + chargement + désactivé) × 2 thèmes × 2 langues : 80 captures. Un sous-ensemble raisonné est permis si le lot le justifie par écrit, avec au minimum : les 4 tailles en défaut, l'erreur et le focus à 1280 px, les deux thèmes à 1280 px, et les deux langues à 375 px.

### Préparation avant capture (Playwright, à adapter au projet)

- Attendre la fin du chargement réseau et des polices : `await page.waitForLoadState('networkidle')` puis `await page.evaluate(() => document.fonts.ready)`.
- Figer les animations : `animations: 'disabled'` dans `toHaveScreenshot`, et `page.emulateMedia({ reducedMotion: 'reduce' })`.
- Masquer les contenus volatils (dates, compteurs, identifiants de session, publicités) par `mask` ou par une feuille de style de test, pas en les supprimant.
- Fixer le thème par `page.emulateMedia({ colorScheme: 'dark' })` ou `'light'`, et la langue par la configuration du contexte, non par un clic.
- Un jeu de données fictif et stable est chargé avant chaque capture ; aucun compte réel.
- Nommer les captures par écran, état, taille, thème, langue : `connexion__erreur__1280__sombre__fr.png`. Le nom suffit à retrouver l'écran sans ouvrir l'image.
- Toute capture est rangée sous `05-validation/<campagne>/captures/` avec la date et la version du commit testé.

### Mesures complémentaires (non visuelles)

Une capture ne dit pas tout. Pour les constats d'alignement et de largeur, mesurer la boîte de chaque élément :

```ts
// Sélecteurs à adapter au projet. Mesure des bords gauche et droit des champs d'un même formulaire.
const champs = ['#email', '#password'];
const boites = await Promise.all(champs.map((s) => page.locator(s).boundingBox()));
// Les bords gauches doivent être alignés (écart ≤ 1 px, à valider) ; les largeurs comparées à la règle du formulaire.
```

## Liste de contrôle

Gravité : **bloquant** = empêche la tâche, trompe l'utilisateur, ou s'écarte flagrant de la maquette sur un élément d'action ou de saisie ; **majeur** = dégrade nettement la lecture ou la cohérence ; **mineur** = défaut de finition sans effet sur la tâche. Chaque ligne se contrôle sur la capture et, si indiqué, par mesure.

### VIS-MEP — Mise en page

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-MEP-01 | L'écran respecte la structure de la maquette (zones, ordre, présence des blocs). | Comparaison côte à côte avec la maquette ; aucun bloc absent ou ajouté. | bloquant |
| VIS-MEP-02 | Le contenu principal est dans une zone de lecture lisible, sans étirement sur grand écran. | Largeur du conteneur principal à 1920 px ; une ligne de texte dépasse rarement 80 caractères (repère, à valider). | majeur |
| VIS-MEP-03 | Le conteneur d'un formulaire (carte, panneau, encadré) est présent ou absent comme la maquette le prévoit. | Vérification explicite de la présence de la carte ou du panneau à chaque taille. | bloquant si le formulaire perd sa délimitation prévue |
| VIS-MEP-04 | Aucun défilement horizontal non voulu à aucune taille. | Largeur du document comparée à la fenêtre (`scrollWidth` ≤ `clientWidth`). | bloquant |
| VIS-MEP-05 | Aucun élément ne déborde ni ne se chevauche. | Capture à 375 px ; recherche de texte coupé ou superposé. | bloquant |
| VIS-MEP-06 | Le bas de page ne laisse pas de zone vide inexpliquée ni de contenu coupé. | Inspection de la fin de page ; marge basse cohérente avec la maquette. | mineur |
| VIS-MEP-07 | Les zones de respiration (marges de page) sont identiques d'un écran à l'autre du même gabarit. | Mesure de la marge gauche du contenu sur deux écrans du même gabarit. | majeur |

### VIS-GRI — Grilles et colonnes

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-GRI-01 | Les éléments d'un même bloc s'appuient sur la grille du projet (colonnes, gouttières). | Superposer la grille de tokens sur la capture ; repérer les bords hors grille. | majeur |
| VIS-GRI-02 | La grille change de nombre de colonnes aux points de rupture prévus, sans saut. | Captures aux quatre tailles ; comparer la répartition. | majeur |
| VIS-GRI-03 | Un élément de même rôle occupe la même place d'un écran à l'autre. | Comparaison des coordonnées du titre, du bouton principal, du lien secondaire. | majeur |

### VIS-CHA — Largeurs de champs

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-CHA-01 | Les champs d'un même formulaire ont une largeur cohérente selon une règle unique et déclarée : pleine largeur pour tous, ou largeur proportionnée à la saisie attendue pour chacun. | Mesure de `boundingBox` de chaque champ. Un champ pleine largeur à côté d'un champ étroit, sans règle affichée, est un écart. | bloquant si la maquette montre une règle différente |
| VIS-CHA-02 | La largeur d'un champ est proportionnée à la saisie attendue (courte pour un code, plus longue pour une adresse). | Observation ; le choix de largeur fixe pour guider la saisie est une option, pas une obligation (règle de design system publique, S2 et S3). | majeur |
| VIS-CHA-03 | Les champs de même nature (deux champs de texte, deux champs de mot de passe) ont la même hauteur et la même largeur, sauf règle contraire. | Mesure de hauteur et de largeur par paire. | majeur |
| VIS-CHA-04 | Les champs ont une hauteur qui permet la saisie tactile sur mobile. | Hauteur mesurée à 375 px ; cible tactile minimale à valider contre le référentiel retenu. | majeur |
| VIS-CHA-05 | Un champ de saisie ne se découpe pas en plusieurs champs pour une donnée continue (numéro, code). | Observation ; à valider contre la maquette. | mineur |

### VIS-ALI — Alignements

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-ALI-01 | Les bords gauches des libellés et des champs d'un formulaire sont alignés. | Mesure des `x` gauches ; écart ≤ 1 px (à valider). | majeur |
| VIS-ALI-02 | Une action liée à un champ (afficher le mot de passe, effacer, aide) est fixée à ce champ : à l'intérieur de la zone du champ, ou collée à son bord droit. | Mesure de la distance entre le bord droit du champ et le bord de l'action ; une action à plusieurs centaines de pixels du champ est un écart. S3 place l'action secondaire à droite du champ. | bloquant pour une action de mot de passe ou de saisie |
| VIS-ALI-03 | Les éléments d'une même ligne partagent leur ligne de base ou leur centre vertical. | Mesure des centres verticaux des éléments d'une ligne. | mineur |
| VIS-ALI-04 | Les boutons d'un même groupe ont la même largeur minimale et le même alignement. | Mesure des boutons du groupe. | mineur |
| VIS-ALI-05 | Le texte d'aide ou d'erreur est aligné sur le champ qu'il concerne. | Observation. | majeur |

### VIS-ESP — Espacements

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-ESP-01 | Les espacements utilisent les valeurs des tokens (multiples de l'unité de base du projet, à valider). | Mesure des marges et paddings calculés ; valeurs hors tokens listées. | majeur |
| VIS-ESP-02 | L'espacement entre un libellé et son champ est constant d'un formulaire à l'autre. | Mesure entre libellé et champ sur deux formulaires. | majeur |
| VIS-ESP-03 | L'espacement entre deux champs est plus petit que l'espacement entre deux groupes de champs. | Observation et mesure ; la proximité traduit l'appartenance. | majeur |
| VIS-ESP-04 | Les espacements ne varient pas avec le zoom au point de faire chevaucher les éléments. | Zoom de 200 % ; aucun chevauchement. | bloquant |

### VIS-TYP — Typographie

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-TYP-01 | Les tailles de texte suivent l'échelle typographique du projet ; aucun écart hors échelle. | Mesure de `font-size` par rôle (titre, libellé, aide, bouton). | majeur |
| VIS-TYP-02 | Un libellé est lisible : taille et graisse cohérentes avec le rôle, pas plus petit que le texte de saisie. | Observation ; comparaison libellé et saisie. | majeur |
| VIS-TYP-03 | Le contraste texte/fond atteint le seuil du référentiel retenu (WCAG 2.2 AA : 4,5:1 pour le texte normal, 3:1 pour le grand texte et les composants, à valider). | Mesure à l'outil de contraste sur les états par défaut et focus. | bloquant pour une action ou un libellé de saisie |
| VIS-TYP-04 | Les polices se chargent avant la capture ; aucun texte affiché dans une police de repli par accident. | Capture après `document.fonts.ready`, comparaison à la maquette. | majeur |
| VIS-TYP-05 | Les longues chaînes (traductions) ne cassent pas la mise en page. | Captures dans la langue la plus longue du produit. | majeur |

### VIS-HIE — Hiérarchie

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-HIE-01 | Le titre principal est l'élément le plus visible de l'écran. | Observation : le titre domine les autres éléments. | majeur |
| VIS-HIE-02 | L'action principale est identifiable en un coup d'œil et une seule à l'être. | Observation : une action primaire par écran ou par bloc. | majeur |
| VIS-HIE-03 | Les actions secondaires (mot de passe oublié, changement de langue) ont un rang visuel inférieur à l'action principale, sans être cachées. | Comparaison des contrastes et des tailles. | majeur |
| VIS-HIE-04 | Les éléments de navigation secondaire (sélecteur de langue) ne rivalisent pas avec le titre. | Observation. | mineur |

### VIS-ETA — États

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-ETA-01 | Chaque état maquetté existe et est conforme (défaut, focus, saisie, erreur, désactivé, chargement, succès). | Une capture par état, comparée à la maquette ; état manquant noté. | bloquant si l'état est une étape de la tâche |
| VIS-ETA-02 | Le focus clavier est visible sur chaque élément interactif. | Capture après tabulation ; contour visible, contraste à valider. | bloquant |
| VIS-ETA-03 | Une erreur est signalée près du champ, en texte et pas seulement en couleur. | Capture de l'état erreur ; message présent et lisible. | bloquant |
| VIS-ETA-04 | Un bouton désactivé se distingue d'un bouton actif sans être confondu avec lui. | Comparaison des deux captures. | majeur |
| VIS-ETA-05 | Le chargement n'entraîne pas de saut de mise en page à la fin. | Capture avant et après ; décalage de plus de 2 px = écart (à valider). | majeur |

### VIS-FOR — Formulaires

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-FOR-01 | Chaque champ a un libellé visible ; le placeholder ne remplace pas le libellé. | Observation et lecture du DOM (libellé relié par `for`/`id`). | bloquant |
| VIS-FOR-02 | Les champs obligatoires sont marqués de la même façon sur tout le produit. | Comparaison des marques d'obligation. | majeur |
| VIS-FOR-03 | L'ordre de tabulation suit l'ordre visuel. | Parcours clavier, capture à chaque saut. | bloquant |
| VIS-FOR-04 | Le bouton de soumission est au bout logique du formulaire, à la même place d'un écran à l'autre. | Mesure de la position relative. | majeur |
| VIS-FOR-05 | Le coller est permis dans les champs d'identifiants. | Vérification de l'absence d'attribut bloquant (règle générale, à valider). | majeur |

### VIS-AUT — Authentification

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-AUT-01 | Le mot de passe peut être révélé par une action explicite à côté ou dans le champ, libellée (« Afficher », « Masquer »). | Observation ; action présente et accessible au clavier. S3 et S5 recommandent ce bouton. | bloquant si absent ou détaché (cas de référence) |
| VIS-AUT-02 | L'action d'affichage a une cible tactile suffisante et reste dans le champ visuellement. | Mesure de la cible à 375 px ; position par rapport au champ (`VIS-ALI-02`). | bloquant |
| VIS-AUT-03 | Les règles du mot de passe s'affichent près du champ pendant la saisie, et pas seulement à l'erreur. | Capture de l'état focus ; règle présente. S5 le recommande. | majeur |
| VIS-AUT-04 | Le lien « mot de passe oublié » est proche du champ mot de passe et distinct du bouton principal. | Mesure de la distance et observation de la hiérarchie. | majeur |
| VIS-AUT-05 | Le message d'échec de connexion ne révèle pas si l'identifiant existe. | Lecture du texte d'erreur ; formulation générique. | bloquant |
| VIS-AUT-06 | Les champs d'identifiant et de mot de passe ont les bons types et attributs de saisie (adresse, mot de passe, saisie automatique). | Lecture du DOM. | majeur |
| VIS-AUT-07 | La page de connexion ne montre aucune information de l'espace sécurisé avant authentification. | Observation de la capture non connectée. | bloquant |

### VIS-RTL — Écriture de droite à gauche

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-RTL-01 | En langue de droite à gauche, la direction du texte, des champs et des icônes est inversée là où le sens l'exige. | Capture dans la langue ; comparaison à la maquette RTL. | bloquant si la maquette RTL existe |
| VIS-RTL-02 | Les actions suivent le sens de lecture (action principale, icônes de flèche). | Observation. | majeur |
| VIS-RTL-03 | Le libellé et le champ restent liés, et les chiffres et adresses restent lisibles. | Observation ; une adresse e-mail reste lisible dans son sens. | majeur |
| VIS-RTL-04 | Le sélecteur de langue reste accessible et identifiable dans les deux directions. | Observation. | majeur |

### VIS-DEN — Densité selon la taille d'écran

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-DEN-01 | À 375 px, un écran n'empile pas plus d'éléments qu'il n'en tient sans défilement inutile. | Capture à 375 px ; nombre de défilements pour la tâche principale. | majeur |
| VIS-DEN-02 | Sur grand écran, la densité ne rend pas la page vide ni trop chargée. | Capture à 1920 px ; zone vide ou entassement notés. | mineur |
| VIS-DEN-03 | Les éléments conservent leur ordre à toutes les tailles. | Comparaison de l'ordre de lecture entre tailles. | majeur |

### VIS-SOM — Mode sombre

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-SOM-01 | Le mode sombre applique les couleurs du thème sombre des tokens, sans couleur codée en dur. | Lecture des valeurs calculées ; comparaison avec les tokens. | majeur |
| VIS-SOM-02 | Le contraste reste conforme en mode sombre (VIS-TYP-03). | Mesure sur les états par défaut et focus. | bloquant |
| VIS-SOM-03 | Les champs se distinguent de leur fond en mode sombre (bordure ou fond). | Observation de la capture ; un champ à peine distinct du fond est un écart majeur. | majeur |
| VIS-SOM-04 | Les images et logos restent lisibles en mode sombre. | Observation. | mineur |

### VIS-COH — Cohérence entre écrans

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-COH-01 | Un même composant (champ, bouton, carte, titre) a le même aspect partout. | Comparaison des captures d'écrans différents ; mesure des tailles, couleurs, rayons. | majeur |
| VIS-COH-02 | Les écrans d'un même parcours (connexion, inscription, réinitialisation) partagent le même gabarit. | Comparaison côte à côte. | majeur |
| VIS-COH-03 | Les couleurs viennent des tokens du projet ; aucune couleur hors palette. | Lecture des valeurs calculées. | majeur |
| VIS-COH-04 | Les rayons, ombres et épaisseurs de bordure suivent les tokens. | Mesure. | mineur |

### VIS-MAQ — Conformité à la maquette

| ID | Contrôle | Mesure ou observation | Gravité |
|---|---|---|---|
| VIS-MAQ-01 | Chaque écran capturé correspond à sa maquette pour la structure, la largeur des éléments, l'ordre et les états. | Lecture côte à côte de la capture et de la maquette ; liste des écarts, chacun avec sa zone. | bloquant si un écart touche un élément de saisie ou d'action |
| VIS-MAQ-02 | Aucun élément ajouté, retiré ou déplacé sans décision écrite. | Liste des différences. | bloquant pour un élément d'action ou de saisie |
| VIS-MAQ-03 | Les textes correspondent à la maquette ou au texte validé. | Comparaison textuelle. | majeur |
| VIS-MAQ-04 | Une maquette absente ou incomplète est signalée, pas remplacée par un jugement. | Constat « maquette absente » ou « état non maquetté ». | bloquant pour l'écran concerné avant fusion |

## Régression visuelle

### Outils et principe

- L'outil retenu pour les tests de non-régression est celui du projet. Repère de départ : le test de capture de Playwright (`toHaveScreenshot`), qui compare une capture à une référence versionnée (S1).
- Un outil autonome (BackstopJS, MIT, auto-hébergé, selon S6 à vérifier) peut servir aux pages complètes. Les services SaaS (Argos) et les dépôts archivés (Lost Pixel, archivé selon S6 à vérifier) ne sont pas retenus sans décision du PO.
- Le moteur d'essai est le même que celui de la référence : même image Docker, même système, même navigateur. Un écart de rendu entre systèmes d'exploitation est un faux positif, pas une régression (S1).

### Seuils de départ (à valider)

| Paramètre | Valeur de départ | Pourquoi |
|---|---|---|
| `maxDiffPixelRatio` | 0,001 (0,1 %) pour une page, 0 pour un composant isolé | tolère l'anticrénelage, pas un décalage de bloc |
| `threshold` | valeur par défaut de l'outil, à réduire si les faux positifs sont rares | sensibilité couleur par pixel |
| `animations` | `disabled` | évite les captures en plein mouvement |
| `mask` | dates, compteurs, identifiants volatils | S1 |

### Mise à jour d'une référence

1. Une référence ne se met à jour que si l'écart est attendu et lié à une demande de changement identifiée.
2. La mise à jour produit un diff relu visuellement par un agent ou une personne différente de celui qui a changé le rendu.
3. La mise à jour est versionnée et motivée dans le journal de build (`LOT-`).
4. Une mise à jour globale (tous les écrans d'un coup) est refusée sans revue de chaque diff.

### Exécution

- Les tests visuels portent un tag dédié (par exemple `@visual`) et tournent dans une étape propre, à la fusion et chaque nuit, pas à chaque sauvegarde.
- Un test visuel en échec n'est pas relancé jusqu'à passer : la cause est trouvée (animation, police, donnée volatile) puis corrigée.

## Verdict

| Verdict | Condition |
|---|---|
| **refusé** | au moins un constat `bloquant` ouvert |
| **accepté avec réserves** | aucun `bloquant`, au moins un `majeur` ouvert, accepté par écrit par le PO avec motif |
| **accepté** | aucun constat ouvert, ou seulement des `mineur` notés |

Un écran sans maquette ou sans capture est « non vérifiable » : il n'est jamais « accepté ».

## Cas de référence : page de connexion (capture 2026-11-04)

Constats relevés sur la capture seule (aucune mesure DOM faite) :

| Constat | Identifiant | Gravité |
|---|---|---|
| Champ e-mail pleine largeur, champ mot de passe étroit, sans règle affichée | `VIS-CHA-01` | bloquant si la maquette montre une règle |
| Bouton « Afficher » détaché, à l'extrémité droite de la page, loin du champ | `VIS-ALI-02`, `VIS-AUT-01`, `VIS-AUT-02` | bloquant |
| Conteneur (carte) absent | `VIS-MEP-03` | bloquant si la maquette le prévoit |
| Écart à la maquette non vérifié faute de maquette jointe | `VIS-MAQ-01` | bloquant tant que la maquette n'est pas comparée |
| Zone vide au bas de la page | `VIS-MEP-06` | mineur |

Le constat « champ e-mail pleine largeur » n'est pas en soi une faute : S2 et S3 retiennent le champ fluide comme défaut. Le défaut est l'incohérence entre les deux champs, sans règle déclarée. La règle à arbitrer appartient au concepteur (`VIS-CHA-01`).

## Non-applicable et limites

- Les seuils sont des repères, pas des normes lues ; ils sont à valider contre le référentiel d'accessibilité et le design system du projet.
- Les constats d'aspect sont appuyés sur une capture ; une mesure DOM complète demande l'application en environnement de test.
- Les règles de RTL, de mode sombre et de densité ne s'appliquent que si le produit les prévoit : un écran qui ne les prévoit pas le note « non applicable (motif) ».
- Les sources et les accès restreints sont décrits dans `00-pilotage/renfort/controle-visuel-sources.md` (projet Parapro).

## Processus et serveurs de test

Noter le PID de chaque serveur ou navigateur lancé et n'arrêter que ces PID (`kill <pid>`). Jamais `pkill`, `killall` ni `pgrep -f` par nom ou par motif : d'autres lots tournent en parallèle dans le même environnement (ANO-099 du projet Parapro, 2026-11-07).
