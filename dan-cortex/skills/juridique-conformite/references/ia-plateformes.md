# IA, plateformes, Data Act et mineurs

Cette référence dit qui est concerné par le règlement sur l'IA, les textes de plateformes (DSA, DMA, DGA, P2B), le Data Act et la protection des mineurs, ce qu'il faut faire et quand. Le livrable prépare le travail d'un juriste ou d'un DPO ; il ne vaut pas avis juridique. État : octobre 2026. La qualification fournisseur ou déployeur est à valider par un avocat.

## 1. Règlement sur l'IA : calendrier

Base : règlement (UE) 2024/1689. Le règlement (UE) 2026/1744 (« Digital Omnibus on AI », 8 juil. 2026, en vigueur le 27 juil. 2026, lu sur EUR-Lex) le modifie. Il ne reporte que le haut risque, par des dates fixes.

| Échéance | Quoi | Statut |
|---|---|---|
| 2 févr. 2025 | Interdictions (art. 5), littératie (art. 4) | Applicable |
| 2 août 2025 | Gouvernance, modèles à usage général (GPAI, art. 51-56), sanctions | Applicable |
| 2 août 2026 | Application générale, dont art. 50 (transparence) | Applicable |
| 2 déc. 2026 | Fin du délai de grâce de 4 mois (cons. 38) pour marquer les systèmes génératifs déjà sur le marché avant le 2 août 2026 | Texte lu |
| 2 déc. 2026 | Nouvelle interdiction art. 5(1)(ba)-(bb) : images intimes réalistes sans consentement, matériel pédopornographique | Sources secondaires, texte lu muet : à vérifier |
| 2 août 2027 | Bacs à sable nationaux reportés | Source secondaire |
| 2 déc. 2027 | Haut risque, Annexe III (art. 6(2)) | Texte lu (cons. 40) |
| 2 août 2028 | Haut risque, Annexe I (art. 6(1)) | Texte lu (cons. 40) |

Sanctions inchangées : 35 M€ ou 7 % du CA mondial (source secondaire). **À vérifier** : art. 113 modifié et clause transitoire de l'art. 50(2) (fin du texte non parcourue) ; votes du Parlement (16 juin) et du Conseil (29 juin 2026), une seule source secondaire. **Sources divergentes** : accord politique le 6 mai (Gibson Dunn) ou le 7 mai (Usercentrics) ; code de bonnes pratiques « fin 2026 » (Usercentrics) alors que la Commission en cite déjà environ 190 signataires : suivre EUR-Lex et la Commission.

## 2. Obligations selon le rôle et le risque

Qualifier d'abord : fournisseur (met le système sur le marché sous son nom), déployeur (l'utilise), intégrateur d'un modèle tiers. Un intégrateur de modèle GPAI n'est pas fournisseur GPAI mais obtient la documentation du modèle (art. 53, rappel) ; à valider.

| Niveau | Exemples | Que faire | Quand |
|---|---|---|---|
| Interdit (art. 5) | Manipulation, images intimes non consenties | Exclure du périmètre ; inscrire le risque à l'analyse de risques, outils généralistes d'image ou de vidéo compris | Depuis le 2 févr. 2025 |
| Haut risque (Annexe III) | RH, scoring de crédit, éducation, biométrie | Classer, documenter, système qualité, gestion des risques | Préparer ; échéance 2 déc. 2027 |
| Transparence (art. 50) | Chatbot, contenu généré, hypertrucage | Voir §3 | Depuis le 2 août 2026 |
| GPAI | Modèle de fondation | Seul le fournisseur du modèle est tenu | Depuis le 2 août 2025 |
| Autre | Recommandation simple | Littératie (art. 4) : mesures de soutien, sans niveau individuel garanti | Depuis le 2 févr. 2025 |

Textes lus : art. 4a (remplace l'art. 10(5) : correction des biais sur données sensibles, six conditions) ; PME et « small mid-caps » (art. 3, points 14a-14b), documentation simplifiée (art. 11(1)), qualité proportionnée (art. 17(2)), enregistrement simplifié (art. 6(3)). Bureau de l'IA seul compétent pour les systèmes bâtis sur le modèle GPAI du même fournisseur et ceux des très grandes plateformes (cons. 31-32, source secondaire). Lignes directrices art. 6 : statut non vérifié.

## 3. Transparence (art. 50)

- Art. 50(1) : informer la personne qu'elle interagit avec une IA, dès le premier échange.
- Art. 50(2) : marquage lisible par machine des sorties génératives (fournisseur).
- Art. 50(4) : étiqueter hypertrucages et textes d'intérêt public (déployeur).
- Commission : code de bonnes pratiques sur le marquage et l'étiquetage, lignes directrices sur le champ de l'art. 50, icônes UE facultatives (l'étiquetage est obligatoire).
- Modèle tiers : obtenir par contrat ce que le fournisseur garantit en marquage.

## 4. DSA, DMA, DGA, P2B, Data Act

Seul le Data Act est vérifié ; le reste est un rappel de droit stable non rouvert sur texte officiel : contrôle par avocat.

| Texte | À faire | Statut |
|---|---|---|
| DSA, règlement (UE) 2022/2065, applicable à tous depuis le 17 févr. 2024 | Intermédiaires : point de contact et représentant légal (art. 11-13), CGU (art. 14), transparence (art. 15). Hébergeurs : notification et action (art. 16), motivation (art. 17). Plateformes (`ugc`) : réclamations (art. 20), pas d'interface trompeuse (art. 25), publicité et recommandations (art. 26-27), mineurs (art. 28). Places de marché (`marketplace`) : traçabilité des professionnels (art. 30-32). Micro et petites entreprises exclues des art. 19 et 29 | Rappel |
| DMA, règlement (UE) 2022/1925 | Vise les contrôleurs d'accès ; le projet y est exposé comme utilisateur professionnel (magasins, publicité) : vérifier les droits ouverts | Rappel |
| DGA, règlement (UE) 2022/868, depuis le 24 sept. 2023 | Notification des services d'intermédiation de données | Rappel |
| P2B, règlement (UE) 2019/1150, depuis le 12 juil. 2020 | Intermédiaires en ligne : CGU claires, préavis, transparence du classement, plaintes | Rappel |
| Data Act, règlement (UE) 2023/2854, depuis le 12 sept. 2025 | Art. 3(1) : accès aux données par conception pour les produits connectés et services liés mis sur le marché après le 12 sept. 2026. SaaS : préavis de changement de fournisseur de 2 mois au plus, aucun frais dès le 12 janv. 2027 (art. 29), information précontractuelle sur frais standard et pénalités | Commission lue ; détail en sources secondaires |
| Digital Fairness Act | Proposition attendue au T4 2026 : ne pas l'invoquer | Suivre |

Une marketplace cumule DSA, P2B et RGPD (coresponsabilité possible, art. 26). Le Digital Omnibus reste en discussion pour le Data Act ; effet sur P2B et DGA non vérifié. Interfaces : EDPB, lignes directrices 03/2022 v2.0. Statut de professionnel (« trader ») à déclarer dans les magasins d'applications.

## 5. Mineurs et vérification d'âge

**France.** Aucune interdiction légale des réseaux sociaux aux moins de 15 ans : la décision 2026-911 DC du 14 août 2026 a censuré en totalité l'article 1er de la loi n° 2026-813 du 24 août 2026 (promulguée le 24 ou le 25 selon les pages), pour atteinte non proportionnée à la liberté d'expression et sans garanties pour la vie privée. Reste l'interdiction du téléphone au lycée (code de l'éducation, art. L.511-5) ; autres dispositions survivantes non lues, à vérifier.

La version votée en juillet (source secondaire) imposait aux plateformes au moins deux solutions de vérification d'âge, sans liste Arcom. Elle a probablement disparu avec l'article 1er : à confirmer sur le texte promulgué (avocat). Référentiel Arcom/CNIL, vérification d'âge européenne et loi du 7 juil. 2023 sur la majorité numérique : statut non vérifié.

Ce qui reste exigible :
- Consentement conjoint du titulaire de l'autorité parentale sous 15 ans (RGPD art. 8, loi Informatique et Libertés art. 45, rappel).
- LCEN (loi 2004-575) : mentions légales, régime des hébergeurs. Loi SREN (n° 2024-449) : âge des sites pornographiques, sous contrôle de l'Arcom (rappel).
- CNIL : mises en demeure 2025 visant applications mobiles et jeux en ligne (contrôle de l'âge, transparence).
- Lignes directrices de la Commission du 14 juil. 2025 (art. 28 DSA), non contraignantes : assurance de l'âge précise, fiable, robuste, non intrusive ; auto-déclaration seule insuffisante.
- Réglages protecteurs par défaut : compte privé, ni lecture automatique ni défilement infini, pas de profilage publicitaire.
- Apple : classification d'âge obligatoire depuis le 31 janv. 2026.
- Étiquette `mineurs`, AIPD probable. COPPA, ECA Digital, DUAA : `international-donnees.md`.

## 6. Pièges fréquents

- Croire l'AI Act « reporté » en bloc : seul le haut risque l'est.
- Se dire déployeur alors que l'assistant est vendu sous sa marque.
- Compter sur l'auto-déclaration de l'âge, ou supposer une interdiction française des réseaux sociaux.
- Baser un plan sur le Digital Fairness Act ou l'Omnibus « données ».

## 7. Contrôles avant de rendre

- Chaque fonction d'IA est classée (niveau, rôle) et datée.
- Chaque date a sa source ou « à vérifier » ; les divergences sont signalées.
- Le public mineur possible est tranché par écrit.

## Sources

- Règlement (UE) 2024/1689 : https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Règlement (UE) 2026/1744 : https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
- Commission, code et lignes directrices art. 50 : https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content ; https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations
- Gibson Dunn (source secondaire) : https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Data Act : https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302854
- Conseil constitutionnel, 2026-911 DC : https://www.conseil-constitutionnel.fr/decision/2026/2026911DC.htm
- Commission, mineurs (art. 28 DSA) : https://digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors
