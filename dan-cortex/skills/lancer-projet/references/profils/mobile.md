# Profil — application mobile (type `mobile`)

Lu par le chef d'orchestre à J0 pour qualifier le projet et composer l'équipe. État : octobre 2026 ; les dates des magasins bougent, tout est à revérifier avant décision.

## Ce qui distingue ce type de projet

- La conformité aux magasins d'applications est un sous-projet : niveaux d'API et SDK datés, déclarations de confidentialité et d'âge, suppression de compte dans l'app, statut « trader » dans l'UE.
- Le framework se choisit d'abord selon les compétences de l'équipe, pas selon la mode.
- La publication dépend de décisions extérieures (revue) : le planning porte des marges.

## Étiquettes à poser

`stores` (toujours), `comptes`, `donnees-perso`, `hors-ligne` si usage sans réseau, `paiement` et `abonnement` si achats, `mineurs` si public jeune, `ia` si partage avec une IA tierce, `ue` pour le statut trader, `multilingue`, `integrations` (API, notifications), `code`.

## Acheter, configurer ou construire

| Option | À retenir si | Vigilance |
|---|---|---|
| React Native (Expo) | équipe JavaScript | code natif, permissions et SDK Expo exigent un nouveau binaire |
| Flutter | multi-plateformes, interface très personnalisée | compétences Dart |
| Kotlin Multiplatform, Swift et Kotlin natifs | équipes natives, fonctions système poussées | coût de deux bases de code ou de l'iOS partagé (état : à vérifier) |
| PWA ou site empaqueté | à écarter pour un magasin | rejet probable (guidelines 4.2) |

Sources de comparaison des frameworks : secondaires (blog) ; parts de marché non sourcées. Notifications push (APNs, FCM), hors-ligne, mises à jour forcées, Fastlane : non établis, **à vérifier**.

## Prérequis propres à ce type

1. Comptes développeur Apple et Google créés tôt (organisation ; statut trader DSA pour l'UE).
2. Compte Google personnel récent : test fermé de 12 testeurs pendant 14 jours continus, à lancer environ trois semaines avant la sortie.
3. Compte de démonstration stable et notes de revue claires.
4. Version minimale supportée et politique de mise à jour forcée définies.
5. Chaîne de livraison avec signature, pistes de test et déploiement progressif.

## Agents à renforcer et livrables spécifiques

- `developpeur-mobile` ; `architecte-solution` (choix du framework, hors-ligne, synchronisation).
- `delegue-protection-donnees` : fiche de confidentialité Apple, Data safety Google, privacy manifest, SDK tiers inclus.
- `expert-acquisition` : fiches de magasin, ASO ; `ingenieur-devops` : signature, intégration continue.
- `automaticien-tests` : parc d'appareils ; `testeur-intrusion` si données sensibles.
- Livrables : dossier de soumission par magasin, tableau des déclarations, plan de déploiement progressif.

## Exigences des plateformes et des tiers

- Apple : Xcode 26 et SDK 26 depuis le 28 avril 2026 ; cible iOS 13 minimum depuis le 9 septembre 2026 ; nouvelles questions de classification d'âge depuis le 31 janvier 2026 (sinon mises à jour bloquées). Une autre page Apple évoque Xcode 27 et iOS 15+ en avril 2027 : **à vérifier**.
- Guidelines Apple : 4.2 (pas de site empaqueté), 4.2.6 (modèles rejetés sauf éditeur du contenu), 5.1.1(v) (compte créé : suppression possible dans l'app).
- Google Play : API 36 pour apps nouvelles et mises à jour dès le 31 août 2026 (extension possible au 1er novembre) ; API 35 minimum pour rester visible des nouveaux utilisateurs sur OS récents.
- Vérification des développeurs Android : dès le 30 septembre 2026 au Brésil, en Indonésie, à Singapour et en Thaïlande ; tous les pays en 2027 ; portée ambiguë dans une source.
- Commissions : Apple UE, Core Technology Commission de 5 % hors App Store ; Google 20 % annoncés sur les achats in-app des nouvelles installations dès le 30 juin 2026 (source de presse, barème contradictoire : **à vérifier**).
- Revue : Apple vise 90 % en moins de 24 h ; Google jusqu'à 7 jours (sources secondaires).

## Pièges et causes d'échec fréquentes

- SDK ou niveau d'API périmé ; test fermé de 14 jours oublié.
- Suppression de compte absente ; déclarations incomplètes, notamment les SDK tiers.
- Application qui est un site empaqueté ; compte démo manquant (cause de rejet 2.1 fréquente).
- Mises à jour OTA hors limites : seuls JavaScript, styles et images passent (Expo EAS Update).
- Vérification Android ignorée pour une distribution hors Play.

## Planning type

Aucune durée type établie. Séquence : choix du framework et ouverture des comptes → conception → développement par incréments → recette sur appareils → test fermé et soumission → déploiement progressif. Prévoir 3 à 4 semaines de marge avant la sortie (déduction).

## Sources

- Apple Developer, « Upcoming requirements » et App Review Guidelines.
- Android Developers, target API et developer verification ; Play Console Help.
- Expo, EAS Update.
- Notes `specificites_par_type_de_projet.md`, §3, état au 11 octobre 2026.
