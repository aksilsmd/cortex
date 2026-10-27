# Revues croisées

Une revue croisée fait relire un livrable par un autre métier. C'est là que les compétences se croisent : le
juriste lit le plan marketing, le testeur lit les spécifications, le contrôleur financier lit l'architecture.
Les défauts trouvés ici coûtent dix fois moins que ceux trouvés en recette.

## Règles

- Les relecteurs d'une vague partent ensemble, dans un seul message.
- Un relecteur lit la synthèse, puis les sections qui concernent son métier, pas le document entier.
- Il rend une note de revue de 200 mots au plus dans `00-pilotage/audits/revue-<document>-<métier>.md` :
  verdict (accepté, accepté avec réserves, refusé), constats numérotés avec gravité, corrections demandées.
- Les constats `bloquant` et `majeur` vont au registre des constats ; l'auteur est repris pour corriger.
- En mode `eclair`, remplacer les relecteurs experts par un seul `verificateur` muni des critères ci-dessous.
- Deux allers-retours au plus entre auteur et relecteur. Un désaccord qui persiste après la seconde correction
  va en réunion ou à l'arbitrage du noyau : une boucle sans fin coûte plus qu'une décision.

## Matrice

| Livrable | Auteur | Relecteurs obligatoires | Ce que chaque relecteur cherche |
|---|---|---|---|
| Note d'opportunité | stratege-produit | controleur-financier, juriste-numerique, contradicteur | chiffres tenables ; obstacle légal ; hypothèses fragiles |
| Cahier des charges | expert-cahier-des-charges | architecte-solution, concepteur-tests, juriste-numerique, controleur-financier | faisabilité ; exigences testables ; conformité ; coût |
| SFG | redacteur-sfg | expert-cahier-des-charges, concepteur-ux, architecte-donnees | couverture des exigences ; cohérence des parcours ; données |
| SFD | redacteur-sfd | concepteur-tests, developpeur concerné, delegue-protection-donnees | règles sans ambiguïté et testables ; réalisables ; données personnelles |
| Spécifications techniques | redacteur-specs-techniques | architecte-solution, architecte-securite, automaticien-tests | conformité à l'architecture ; sécurité des interfaces ; testabilité |
| Workflows et matrice d'interactions | cartographe-interactions | redacteur-sfd, expert-accessibilite, concepteur-tests | accord avec les règles de gestion ; accessibilité ; chaque transition testable |
| Maquettes et système de design | maquettiste | concepteur-ux, expert-accessibilite, developpeur-frontend, stratege-marketing | parcours ; contrastes et lisibilité ; réalisable ; marque |
| Dossier d'architecture et décisions | architecte-solution | architecte-securite, ingenieur-devops, controleur-financier, gardien-des-normes | surface d'attaque ; exploitabilité ; coût total ; maintenabilité |
| Modèle de données | architecte-donnees | delegue-protection-donnees, developpeur-backend, architecte-securite | minimisation et durées ; performances ; chiffrement et accès |
| Normes de développement | gardien-des-normes | architecte-solution, relecteur-code, auditeur-securite | applicables ; vérifiables par outil ; règles de sécurité incluses |
| Infrastructure | ingenieur-devops | architecte-securite, controleur-financier, juriste-numerique | cloisonnement ; coût ; localisation des données et contrats |
| Modèle de menaces | architecte-securite | architecte-solution, developpeur-backend, delegue-protection-donnees | menaces réalistes ; parades réalisables ; données personnelles |
| Stratégie de test et cahier de recette | concepteur-tests | expert-cahier-des-charges, redacteur-sfd, auditeur-securite | exigences couvertes ; règles couvertes ; tests de sécurité prévus |
| Documents juridiques | juriste-numerique | stratege-marketing, responsable-commercial, delegue-protection-donnees | accord avec l'offre réelle ; avec la vente ; avec les traitements réels |
| Plan marketing et prix | stratege-marketing | juriste-numerique, controleur-financier, stratege-produit | allégations et prospection licites ; rentabilité ; cohérence du positionnement |
| Budget et justification économique | controleur-financier | architecte-solution, planificateur, contradicteur | charges réalistes ; calendrier ; hypothèses optimistes |
| Lot de code | développeur | relecteur-code, gardien-des-normes, auditeur-securite | justesse ; normes ; failles |
| Rapport de test d'intrusion | testeur-intrusion | architecte-securite, developpeur concerné | gravités justes ; corrections réalisables |
| Plan de lancement et plan de bascule | responsable-lancement | ingenieur-devops, stratege-marketing, responsable-support-formation, juriste-numerique | retour arrière ; synchronisation ; support prêt ; mentions en ligne |

## Binômes permanents

Certains métiers travaillent mieux à deux dès la production. Les lancer dans la même vague en donnant à chacun
le chemin du livrable de l'autre, pour une lecture mutuelle en fin de mission.

| Binôme | Pourquoi |
|---|---|
| architecte-solution et architecte-securite | la sécurité se conçoit avec l'architecture, pas après |
| redacteur-sfd et cartographe-interactions | chaque règle de gestion a son écran, chaque écran ses règles |
| delegue-protection-donnees et architecte-donnees | la minimisation se décide dans le schéma |
| stratege-marketing et juriste-numerique | promesses, prix et prospection doivent être licites |
| controleur-financier et ingenieur-devops | le coût d'hébergement se pilote dès la conception |
| concepteur-tests et redacteur-sfd | une règle qui ne se teste pas est mal écrite |
