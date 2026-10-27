# Cookies, traceurs et prospection

Cette référence couvre le consentement aux traceurs, la mesure d'audience exemptée, le plan de marquage conforme et la prospection par e-mail, SMS et téléphone. Le livrable prépare le travail d'un juriste ou d'un DPO et ne vaut pas avis juridique. État : octobre 2026.

## Sommaire
1. Traceurs : règles
2. Mesure d'audience exemptée
3. Plan de marquage conforme
4. Prospection
5. Gabarit `politique-cookies.md`
6. Pièges fréquents
7. Contrôles avant de rendre
8. Sources

## 1. Traceurs : règles

| Point | Règle | Territoire et texte |
|---|---|---|
| Fondement | Dépôt ou lecture d'un traceur sur le terminal : consentement, sauf exemption | France : art. 82 de la loi Informatique et Libertés ; consentement au sens des art. 4(11) et 7 du RGPD |
| Qui est tenu | Le responsable qui autorise le dépôt, y compris pour des traceurs lus par des régies | CNIL, « que dit la loi » |
| Cadre CNIL | Lignes directrices du 17 sept. 2020 et recommandation (exemples de modalités) | France |
| Directive | ePrivacy 2002/58/CE : art. 5(3) pour les traceurs (transposé par l'art. 82), art. 13 pour la prospection (transposé au CPCE, art. L.34-5). Rappel non rouvert sur texte officiel. Le projet de règlement ePrivacy n'a pas abouti (retrait annoncé en 2025, non vérifié) | UE |
| Sanctions UK | PECR : jusqu'à 17,5 M£ ou 4 % du CA mondial depuis le DUAA, en vigueur le 5 févr. 2026 (ICO) | Royaume-Uni |

**Consentement valide (CNIL)** :
- Liste à jour des responsables de traitement accessible dès le premier niveau.
- Acte positif clair : silence, poursuite de la navigation ou fermeture du bandeau valent refus.
- Refuser aussi simple qu'accepter : « Tout accepter » et « Tout refuser » au même niveau, même format.
- Choix conservé environ 6 mois, consentement comme refus (durée exacte à vérifier).
- Aucune interface trompeuse : bouton décoloré, curseur ambigu.
- Retrait aussi simple que l'octroi, accessible en permanence.

Pourquoi tant de rigueur : 21 sanctions cookies en 2025, dont Google 325 M€ et Shein 150 M€ (dépôt sans consentement, information insuffisante, refus ou retrait ignoré). La procédure simplifiée 2026 (23 sanctions, 133 750 € au total depuis janv., plafond 20 000 €) frappe les dépôts avant action et les refus plus difficiles que l'acceptation.

Durées maximales de vie des traceurs (13 et 25 mois, rappel non relu sur texte) : à vérifier. Consent Mode v2 de Google et position de la CNIL : non vérifiés, à vérifier. Volet cookies de l'Omnibus (règles ePrivacy déplacées vers le RGPD) : signalé « ouvert » par une source secondaire, ne pas s'y appuyer.

## 2. Mesure d'audience exemptée

L'exemption de consentement tient à toutes les conditions (CNIL) :
1. Traceurs indépendants entre eux et de tout autre traceur.
2. Données collectées, traitées et stockées séparément par éditeur.
3. Fournisseur sous-traitant, qui ne réutilise pas les données pour son compte (sauf désactivation configurable).
4. Finalité limitée à la mesure de l'audience du site.

Un outil non configuré « sans réutilisation » sort de l'exemption : bandeau exigé. L'exemption ne dispense pas de maîtriser les transferts hors UE (voir `international-donnees.md`). La CNIL propose un outil d'auto-évaluation pour fournisseurs. Pixels de suivi dans les e-mails : la CNIL a publié une FAQ le 22 juil. 2026 sur sa recommandation ; seule son existence est établie, contenu non lu : à vérifier avant tout e-mailing avec pixel.

## 3. Plan de marquage conforme

Produire, avec l'expert en acquisition, un tableau unique de tous les traceurs et balises :

| Colonne | Contenu |
|---|---|
| ID | `TRC-001`… |
| Traceur ou balise | Nom, éditeur, domaine |
| Finalité | Mesure, publicité, personnalisation, fonctionnel, sécurité |
| Régime | Exempté (strictement nécessaire ou audience conforme) ou consentement |
| Déclenchement | Jamais avant action pour les traceurs soumis à consentement |
| Durée de vie | Traceur et données |
| Destinataires et pays | Sous-traitant ou tiers, transfert |
| Preuve | Capture du comportement avant et après choix |

Règles de recette : aucun traceur soumis à consentement avant l'action de l'utilisateur ; bouton de refus au premier niveau ; preuve du consentement conservée ; retrait possible à tout moment ; refus respecté par les balises tierces et par les applications mobiles (SDK).

## 4. Prospection

La prospection n'est pas sourcée : tout ce qui suit est un rappel à valider par un juriste.

| Canal | Règle usuelle | Statut |
|---|---|---|
| E-mail et SMS vers un consommateur | Consentement préalable ; exception pour les produits ou services analogues d'un client existant, avec opposition simple à la collecte et à chaque envoi (art. L34-5 CPCE) | À vérifier |
| E-mail vers un professionnel | Information préalable et opposition possible ; message en rapport avec la fonction | À vérifier |
| Téléphone | Opposition préalable au démarchage téléphonique à respecter ; régime en évolution | À vérifier |
| Royaume-Uni | PECR, amendes jusqu'à 17,5 M£ ou 4 % du CA mondial depuis le DUAA, qui modifie PECR sans le remplacer | Voir §1 |
| États-Unis | CAN-SPAM : désinscription et adresse postale (FTC) | Rappel, à vérifier |
| Algérie | Prospection électronique : loi 18-07, art. 37 | Texte lu, détail non rapporté : à vérifier |
| Maroc, Tunisie | Droit local | À vérifier |

Constants : identité de l'expéditeur claire, lien de désinscription en un geste, liste de suppression conservée, source de la donnée traçable. La CNIL a prononcé 10 sanctions en prospection en 2025.

## 5. Gabarit `03-conception/juridique/politique-cookies.md`

```markdown
# Politique relative aux cookies et traceurs — <projet>
> Prépare le travail d'un juriste ; ne vaut pas avis juridique.
## Synthèse
Nombre de traceurs, exemptés, soumis à consentement ; outil de recueil ; écarts ouverts.
## Qu'est-ce qu'un traceur
## Traceurs utilisés
| ID | Traceur | Éditeur | Finalité | Régime | Durée | Pays |
|---|---|---|---|---|---|---|
## Gérer vos choix
Où et comment accepter, refuser, retirer. Conservation du choix.
## Mesure d'audience
Outil, conditions d'exemption, responsable.
## Contact
```

## 6. Pièges fréquents

- Bandeau conforme, mais balises chargées par le gestionnaire de balises avant le choix.
- Refus accessible seulement dans un sous-menu.
- Analytics non configuré, présenté à tort comme exempté.
- Choix non transmis aux SDK de l'application mobile.

## 7. Contrôles avant de rendre

- Chaque traceur du site et de l'application figure au plan de marquage, avec régime et preuve.
- Les durées, la prospection et tout point non confirmé portent « à vérifier ».
- Le texte de la politique correspond au comportement réel.

## Sources

- CNIL, cookies — que dit la loi : https://www.cnil.fr/fr/cookies-et-autres-traceurs/que-dit-la-loi
- CNIL, mise en conformité : https://www.cnil.fr/fr/cookies-et-autres-traceurs/regles/cookies/comment-mettre-mon-site-web-en-conformite
- CNIL, mesure d'audience : https://www.cnil.fr/fr/cookies-solutions-pour-les-outils-de-mesure-daudience
- CNIL, mesure d'audience et transferts : https://www.cnil.fr/fr/mesure-daudience-et-transferts-de-donnees-comment-mettre-son-outil-de-mesure-daudience-en-conformite
- CNIL, FAQ pixels dans les e-mails : https://www.cnil.fr/fr/faq-recommandation-pixels-courriers-electroniques
- ICO, DUAA : https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/02/statement-on-the-commencement-of-the-data-use-and-access-act-duaa/
- CNIL, bilan des sanctions 2025 : https://www.cnil.fr/fr/bilan-sanctions-2025
- CNIL, 23 sanctions simplifiées : https://cnil.fr/fr/23-nouvelles-sanctions-simplifiees
- Directive 2002/58/CE : https://eur-lex.europa.eu/eli/dir/2002/58/oj
- FTC, CAN-SPAM : https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
