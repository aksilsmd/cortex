# Risque pénal et responsabilités

Ce qu'un projet numérique ne doit jamais faire, le texte qui le réprime, la peine encourue et le garde-fou à intégrer. État : 11 octobre 2026. Ce livrable prépare le travail d'un avocat pénaliste et ne vaut pas conseil juridique.

**État des vérifications.** Lus sur Légifrance : Code pénal 323-x, 226-x, 121-2, Code de la défense L2321-4 et L2321-4-1, LCEN, CGI 1743, jurisprudence sur la délégation. Tout ce qui est marqué « à vérifier » n'a pas été relu sur texte officiel (consommation, CPI, CMF, NIS2, directive 2024/2853, DSA, eIDAS, 121-3, 131-38, droits algérien et marocain, UE 2013/40, Budapest). Une peine citée est un plafond, jamais une prédiction.

## Tableau des comportements à risque

| Comportement à risque | Texte | Peine encourue (plafond) | Garde-fou dans le projet |
|---|---|---|---|
| Accès ou maintien frauduleux dans un système, y compris par un test sans autorisation | Code pénal, art. 323-1 | 3 ans, 100 000 € ; 5 ans, 150 000 € si données supprimées ou modifiées ou système altéré ; 7 ans, 300 000 € si système de l'État à données personnelles | Autorisation écrite du titulaire, périmètre et dates avant tout test |
| Entrave au système ; introduction, extraction, modification frauduleuse de données | Code pénal, art. 323-2, 323-3 | 5 ans, 150 000 € ; 7 ans, 300 000 € côté État | Débit limité, revue du code de collecte |
| Importer, détenir, céder un outil conçu pour ces atteintes « sans motif légitime » ; tentative (323-7) | Code pénal, art. 323-3-1 | peines de l'infraction visée ; interdiction d'exercer 5 ans, fermeture (323-5) | Outils inventoriés, motif légitime (recherche, sécurité) documenté |
| Plateforme permettant sciemment la cession de produits ou contenus manifestement illicites | Code pénal, art. 323-3-2 (loi 2025-532) | 7 ans, 500 000 € ; 10 ans, 1 M€ en bande organisée | Modération, registre des notifications |
| Défaut de mesures de sécurité, violation non notifiée | Code pénal, art. 226-17, 226-17-1 | 5 ans, 300 000 € | Mesures RGPD art. 32, procédure 72 h |
| Collecte déloyale, détournement de finalité, conservation excessive, données sensibles sans consentement, transfert hors UE illicite | Code pénal, art. 226-18, 226-21, 226-20, 226-19, 226-22-1 | 5 ans, 300 000 € | Finalités écrites, purge automatique |
| Formalités omises, divulgation à un tiers non habilité | Code pénal, art. 226-16, 226-22 | 5 ans, 300 000 € ; la négligence suffit (3 ans, 100 000 € pour 226-22) | Journaux d'accès, chiffrement |
| Atteinte à l'intimité, interception de correspondances (226-3 : appareils, 5 ans), usurpation d'identité | Code pénal, art. 226-1, 226-15, 226-4-1 | 1 an, 45 000 € ; 1 an, 15 000 € pour 226-4-1 | Aucune interception |
| Hypertrucage non signalé ou sans consentement | Code pénal, art. 226-8, 226-8-1 | 1 an, 15 000 € (2 ans, 45 000 € en ligne) ; sexuel : 2 ans, 60 000 € (3 ans, 75 000 € en ligne) | Étiquetage, consentement |
| Mentions légales absentes ; données d'identification non conservées | LCEN art. 1-1 ; art. 6 V | 1 an, 75 000 € (dirigeant de droit ou de fait) ; 1 an, 250 000 € | Mentions et directeur de publication (loi 82-652, art. 93-2) validés ; durée fixée par décret non lu |
| Défaut d'information sur un contenu terroriste (règlement (UE) 2021/784, art. 14.5) | LCEN | 1 an, 250 000 € ; 4 % du CA mondial en cas de manquement habituel (alinéa non lu en entier) | Point de contact, astreinte |
| Logiciel de caisse ou de comptabilité permettant la fraude | CGI 1743 | 5 ans, 150 000 € ; amende fiscale de 15 % du CA tiré du logiciel, distributeur compris s'il savait | Inaltérabilité attestée |
| Contrôle d'âge défaillant (majorité numérique) | loi promulguée le 25/08/2026 | jusqu'à 1 % du CA mondial ; interdiction aux moins de 15 ans censurée le 14/08/2026 | Réforme visée au printemps 2027 ; art. 227-24 CP non relu : à vérifier |
| Escroquerie, abus de confiance, blanchiment ; paiement sans agrément (CMF L561-2) | Code pénal, art. 313-1, 314-1, 324-1 (à vérifier) | 5 ans, 375 000 € ; 3 ans, 375 000 € ; 5 ans, 375 000 € | PSP agréé, descriptions vérifiées |
| Pratique commerciale trompeuse ou agressive, faux avis ; prospection sans consentement (CPCE L34-5) ; contrefaçon (CPI L335-3) | C. conso L121-2, L121-6 (à vérifier) | 2 ans, 300 000 €, jusqu'à 10 % du CA moyen ; contrefaçon 3 ans, 300 000 € (à vérifier) | Revue juridique des parcours, jamais d'avis inventé, licences inventoriées |
| Contrefaçon de logiciel | CPI L335-3 | 3 ans, 300 000 € (à vérifier) | Inventaire des licences |

## Signalement de vulnérabilités

- Aucun texte ne vaut immunité pour l'accès initial : seule l'autorisation préalable écrite retire le caractère frauduleux (à valider par avocat).
- Code de la défense, L2321-4 : la personne de bonne foi qui transmet à la seule ANSSI une vulnérabilité est dispensée de l'obligation de dénonciation de l'art. 40 CPP ; l'ANSSI garde son identité confidentielle.
- L2321-4-1 (loi 2023-703, art. 66) : l'éditeur de logiciel, payant ou gratuit, notifie à l'ANSSI toute vulnérabilité significative ou incident ; l'ANSSI peut enjoindre d'informer les utilisateurs ou de publier. Décret d'application et jurisprudence non vérifiés.
- Publier une politique de divulgation et une procédure de signalement.

## Responsabilités

| Qui | Régime | Conséquence pratique |
|---|---|---|
| Personne morale | Code pénal, art. 121-2 : responsable des infractions commises pour son compte par ses organes ou représentants, sans exclure les personnes physiques ; amende quintuple (131-38, à vérifier) | La société porte l'infraction ; le dirigeant reste exposé |
| Dirigeant, délégataire | Auteur ou complice ; faute non intentionnelle (121-3, à vérifier). Cass. crim., 26/06/2001 : représentant = compétence, autorité, moyens ; 28/11/2017, 16-85.414 : délégation sans moyens, condamnation maintenue | Délégation écrite avec budget : elle protège le dirigeant, pas la société |
| Prestataire | Complicité si la finalité frauduleuse est connue (121-6) ; clause limitative écartée en cas de faute lourde ou dolosive (C. civ. 1231-3) ou si elle vide l'obligation essentielle (1170) : à vérifier | Clause de conformité, recette, plafond négocié |
| Éditeur, hébergeur | Directeur de publication identifié (loi 82-652, art. 93-2) ; hébergeur responsable après connaissance d'un contenu manifestement illicite (DSA art. 8, 16, 18 : à vérifier) | Notification-action, registre des retraits |
| NIS2 | Art. 20 (dirigeants), amendes 10 M€ / 2 % et 7 M€ / 1,4 % : à vérifier ; en France, projet de loi « résilience » non adopté (examen reporté, 06/10/2026) | Ne pas invoquer un texte non transposé |
| Agents automatisés | Le projet répond de ce que font ses outils | Périmètre autorisé, journal des actions |

Directive (UE) 2024/2853 (produits défectueux, logiciel inclus) : transposition avant le 09/12/2026, aucun projet français déposé à notre connaissance. Tracer modèles, versions et correctifs.

## Preuve et conservation

- Horodater et conserver au moins 6 ans (prescription des délits, à vérifier) : autorisations et périmètres de test, consentements, oppositions, accès administrateur.
- À vérifier : eIDAS 910/2014 modifié, indemnisation cyber après plainte sous 72 h (loi 2023-22), Sapin II (500 salariés et 100 M€).
- Geler les purges dès qu'un litige se profile.

## Algérie et autres territoires

Montants divergents selon les sources : confirmer au JORADP avec un avocat local (code pénal et loi 09-04 non lus).

- Code pénal, art. 394 bis : accès frauduleux 3 mois à 1 an, 50 000 à 200 000 DA, doublé si données modifiées ; 394 bis 1 : 6 mois à 3 ans ; 394 bis 2 (outils) : 2 mois à 3 ans, 1 à 10 M DA ; 394 bis 4 : personne morale, cinq fois ; 394 bis 8 : fournisseur ne retirant pas un contenu illicite, 1 à 3 ans, 2 à 10 M DA.
- Loi 09-04 : trafic conservé 1 an. Loi 18-07 : collecte déloyale ou traitement sans consentement 1 à 3 ans, 100 000 à 300 000 DA. Loi 18-05 : registre du commerce, « .com.dz », produits interdits 200 000 à 1 M DA et fermeture.
- Maroc, loi 07-03 : outils 2 à 5 ans (version non datée). États-Unis : politique DOJ du 19/05/2022, pas une exemption légale. Royaume-Uni : statut 2026 d'une défense de recherche non vérifié.

## Pièges

- Croire qu'un « simple test » ou un bug bounty vaut autorisation.
- Oublier le dirigeant de fait ; déléguer sans moyens.
- Compter sur l'assurance pour les amendes pénales (à vérifier).
- Changements récents : 323-1 relevé (2023), 323-4-2 créé, 226-8-1 (2024), 323-3-2 réécrit (2025).

## Sources

- Légifrance : Code pénal, art. 323-1 à 323-8, 226-1 à 226-24, 121-2 ; Code de la défense, L2321-4 et L2321-4-1 ; LCEN.
- Légifrance : Cass. crim., 26/06/2001 ; Cass. crim., 28/11/2017, 16-85.414.
- BOFiP, BOI-CF-INF-20-10-20-20250416 (CGI 1743).
- Assemblée nationale, QE 11448 (directive 2024/2853) ; Vie publique, majorité numérique.
- JORADP, JO français 2018, fascicules F2018034 (loi 18-07) et F2018028 (loi 18-05) ; Conseil de l'Europe, profil légal de l'Algérie.
