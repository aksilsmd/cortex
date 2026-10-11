# Accessibilité : exigences par composant, audit, rapport

Ce fichier donne le savoir-faire de conception et d'audit. Les obligations légales, échéances et sanctions relèvent du pôle juridique (`juridique-conformite`) : ne pas les trancher ici. Livrables : `03-conception/design/accessibilite.md` (exigences, J3) et `05-validation/rapport-accessibilite.md` (audit, J5).

## Sommaire
1. Référentiel visé
2. Exigences par composant
3. Critères WCAG 2.2 à ne pas rater
4. Méthode d'audit
5. Gabarit du rapport
6. Pièges et contrôles avant de rendre

## 1. Référentiel visé

État : octobre 2026.

| Référentiel | Situation |
|---|---|
| WCAG 2.2 niveau AA | cible de conception, quel que soit le pays |
| RGAA 4.1.2 | version en vigueur en France (106 critères) ; sa base WCAG est 2.1 (à vérifier) |
| RGAA 5 | intègre WCAG 2.2, publication annoncée fin 2026 : suivre |
| EN 301 549 | V4.1.1 adoptée en août 2026, WCAG 2.2 A et AA ; tant qu'elle n'est pas citée au JOUE, la référence légale reste la V3.2.1 (WCAG 2.1 AA) |

Conséquence : concevoir à WCAG 2.2 AA dès maintenant ; auditer en RGAA 4.1.2 si le projet est soumis au RGAA, en ajoutant les critères WCAG 2.2 absents de la grille. Niveau visé : décision de type 1 quand une obligation légale s'applique, à porter au comité de cadrage avec l'avis du juriste.

## 2. Exigences par composant

| Composant | Exigences de conception |
|---|---|
| Bouton, lien | nom accessible explicite (pas « cliquez ici ») ; cible d'au moins 24×24 px CSS ; focus visible et non masqué ; un lien navigue, un bouton agit |
| Champ | étiquette visible reliée au champ ; `autocomplete` adapté ; format attendu indiqué avant la saisie ; obligatoire signalé en texte |
| Erreur | message en texte relié au champ, annoncé ; résumé d'erreurs en tête avec liens vers les champs ; focus déplacé ; ne repose pas sur la couleur seule |
| Modale | focus déplacé dedans et piégé, fermeture par Échap, focus rendu à l'élément déclencheur, arrière-plan inerte |
| Tableau | en-têtes de colonnes et de lignes, légende ; pas de tableau pour la mise en page |
| Navigation | repères (`header`, `nav`, `main`, `footer`), lien d'évitement, ordre de tabulation égal à l'ordre visuel, page courante signalée |
| Média | alternative textuelle, sous-titres, transcription ; aucune lecture automatique ; pause possible |
| Formulaire long | étapes annoncées, données conservées, pas de limite de temps sans possibilité de la prolonger |
| Notification, chargement | annoncés aux lecteurs d'écran sans voler le focus (région `aria-live` polie) |
| Graphique | alternative textuelle ou tableau de données ; motifs en plus de la couleur |
| Mobile | orientation libre, gestes simples avec alternative, étiquettes lues par le lecteur d'écran de la plateforme |

Valeurs transversales : contraste 4,5:1 pour le texte, 3:1 pour le texte large et pour les composants et indicateurs d'état ; reflow sans défilement horizontal à 320 px ; zoom du texte à 200 % sans perte ; `prefers-reduced-motion` respecté ; langue de page déclarée (`lang`), et de chaque passage dans une autre langue.

## 3. Critères WCAG 2.2 à ne pas rater

Liste de conception ; vérifier la formulation officielle avant citation dans un rapport.

| Critère | Niveau | À concevoir |
|---|---|---|
| 2.4.11 Focus non masqué (minimum) | AA | bandeaux et en-têtes fixes ne recouvrent pas l'élément focalisé |
| 2.5.7 Déplacements par glissement | AA | toute action au glisser-déposer a une alternative au clic |
| 2.5.8 Taille de la cible (minimum) | AA | 24×24 px CSS ou espacement suffisant |
| 3.2.6 Aide cohérente | A | l'aide est au même endroit sur tous les écrans |
| 3.3.7 Saisie redondante | A | ne pas redemander une information déjà fournie dans le même parcours |
| 3.3.8 Authentification accessible (minimum) | AA | collage et gestionnaire de mots de passe autorisés, aucun test cognitif (pas de CAPTCHA à déchiffrer) |

Le critère 4.1.1 Parsing est supprimé de WCAG 2.2.

## 4. Méthode d'audit

1. **Périmètre** : échantillon de pages et de parcours (accueil, parcours critiques, formulaires, tableaux, états d'erreur, gabarits uniques), version du référentiel, navigateurs et lecteurs d'écran. Écrire ce qui est exclu.
2. **Automatique** : outils d'analyse sur chaque page de l'échantillon. Ils ne couvrent qu'une partie des critères : jamais suffisants seuls.
3. **Clavier** : parcourir chaque parcours sans souris (Tab, Maj+Tab, Entrée, Espace, Échap, flèches) ; vérifier focus visible, ordre, absence de piège.
4. **Lecteur d'écran** : NVDA, VoiceOver, TalkBack selon la plateforme ; vérifier noms, rôles, états, annonces d'erreur.
5. **Manuel par critère** : contraste, reflow, zoom, espacement du texte, cibles, alternatives, mouvement.
6. **Grille** : RGAA 4.1.2 (conforme, non conforme, non applicable par critère) ou WCAG 2.2.
7. **Personnes concernées** : proposer un test avec des utilisateurs en situation de handicap ; sans lui, le dire.
8. **Anomalies** : une par défaut, avec critère, page, reproduction, gravité, correction proposée ; au registre via `cortex.py registre anomalies ajouter`. Bloquante si elle empêche d'accomplir un parcours critique.
9. **Contre-test** après correction.

Taux de conformité : s'il est calculé, indiquer la méthode (RGAA : critères conformes sur critères applicables). Une déclaration d'accessibilité est à valider par le juriste.

## 5. Gabarit du rapport

````markdown
# Rapport d'accessibilité — <projet>

## Synthèse
<référentiel et version, périmètre, date, résultat par niveau, nombre d'anomalies par gravité, parcours critiques accomplis (oui/non), limites de l'audit, décision proposée>

## Périmètre et méthode
Échantillon, outils (version), navigateurs, lecteurs d'écran, ce qui n'a pas été testé.

## Résultats par critère
| Critère | Résultat | Pages concernées | Constat |
|---|---|---|---|

## Anomalies
| ID | Critère | Gravité | Page ou écran | Reproduction | Correction proposée |
|---|---|---|---|---|---|

## Parcours critiques
| Parcours | Clavier | Lecteur d'écran | Zoom 200 % | Résultat |
|---|---|---|---|---|

## Plan de correction et contre-test
````

## 6. Pièges et contrôles avant de rendre

- Se fier au score d'un outil automatique ; tester seulement la page d'accueil.
- Contraste vérifié en thème clair seulement ; focus supprimé par la feuille de style.
- Message d'erreur affiché sans être annoncé ; modale sans retour du focus ; CAPTCHA cognitif.
- Viser seulement WCAG 2.1 ou croire l'EN 301 549 V4.1.1 déjà opposable.
- Contrôles : chaque composant de `design-system.md` a ses exigences ; les six critères WCAG 2.2 sont couverts ; l'échantillon couvre tous les rôles ; le rapport dit ce qui n'a pas été testé.

## Sources
- WCAG 2.2 (W3C Recommandation) : https://www.w3.org/TR/WCAG22/ (liste officielle des critères à relire, état : octobre 2026).
- RGAA : https://accessibilite.numerique.gouv.fr/ (4.1.2 en vigueur ; RGAA 5 annoncé fin 2026) ; présentation du RGAA 5 : https://design.numerique.gouv.fr/articles/2026-03-02-rgaa5/
- EN 301 549 V4.1.1 (ETSI, CEN, CENELEC, septembre 2026) ; V3.2.1 (2021) toujours référence tant que la V4 n'est pas citée au JOUE.
