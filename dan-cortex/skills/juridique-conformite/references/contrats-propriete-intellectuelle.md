# Contrats et propriété intellectuelle

Contrats du projet (SaaS, prestation, développement, cession), marques et noms de domaine, droit d'auteur sur le logiciel, licences libres, contenus produits par IA. État : octobre 2026. Les textes de propriété intellectuelle n'ont pas été vérifiés à la source : tout ce qui n'est pas daté ici est une connaissance établie, **à vérifier** et à valider par un avocat ou un conseil en propriété industrielle. Ce livrable ne vaut pas conseil juridique.

## Sommaire
- Contrats : clauses à traiter
- Titularité du code et cession
- Marques et noms de domaine
- Licences libres
- Contenus produits par IA
- Gabarit
- Pièges
- Sources

## Contrats : clauses à traiter

Pas de régime légal unique : le contrat fait la loi, dans la limite de l'ordre public.

| Contrat | Clauses qui changent le risque |
|---|---|
| SaaS B2B (éditeur vers client) | SLA (disponibilité, pénalités, crédits), plafond de responsabilité, propriété et usage des données (client contre dérivées et agrégées), sous-traitants et localisation, sécurité, réversibilité, changement de loi, suspension |
| Prestation et développement (client vers prestataire) | Périmètre et critères de recette, obligation de moyens ou de résultat, propriété et cession du code, licences tierces, garanties, confidentialité, sous-traitance, pénalités, réversibilité |
| Hébergement et cloud | Localisation, sous-traitants ultérieurs, audit, sortie des données, Data Act |
| Contrats avec salariés, freelances, influenceurs | Cession écrite des droits, confidentialité, non-concurrence (à vérifier), indépendance |

Règles :
- **Data Act** (règlement (UE) 2023/2854), applicable depuis le 12 septembre 2025 : un fournisseur de services de traitement de données (cloud, SaaS) prévoit un contrat de changement de fournisseur, préavis maximal 2 mois ; frais de changement, sortie des données comprise, **supprimés au 12 janvier 2027** ; information précontractuelle sur frais standard et pénalités de résiliation (art. 29 d'après la note infrastructures).
- **CGV B2B** : clauses de transport et de force majeure ; CGV distinctes par catégorie de clients possibles (Service-Public F23455).
- Références de mémoire, non vérifiées : délais de paiement (C. com. L441-10), déséquilibre significatif (L442-1), clauses limitatives de responsabilité (C. civ. art. 1170). **À vérifier.**
- Clause de changement de loi dans les contrats longs : les règles de 2025-2027 bougent (caisse, facture électronique, PSD3).

## Titularité du code et cession

- Le droit d'auteur naît sur l'œuvre sans dépôt. Le logiciel est protégé par le droit d'auteur (CPI : articles à vérifier).
- Le prestataire reste titulaire sauf cession écrite. Une cession précise chaque droit, son étendue, sa destination, son lieu et sa durée (CPI L131-3, de mémoire, à vérifier). Un contrat muet sur ces points est fragile.
- Les salariés : règle spéciale pour les logiciels créés dans l'exercice des fonctions (CPI, article à vérifier) ; l'écrire quand même.
- Freelances, agences, contributeurs open source : cession écrite avant le premier commit, ou licence explicite ; accord de contributeur (CLA ou DCO) pour un projet ouvert.
- Décision de type 1 : le projet est-il propriétaire, sous licence libre, ou en double licence ? Elle conditionne les dépendances admises.

## Marques et noms de domaine

| Étape | Action |
|---|---|
| Antériorités | Rechercher marques identiques ou proches, dénominations, noms de domaine, dans les classes et territoires visés (INPI, EUIPO, OMPI/Madrid) avant d'investir dans le nom |
| Dépôt | Territoires selon les marchés : France (INPI), UE (EUIPO), international (OMPI). Taxes et délais : à vérifier ; ne rien chiffrer sans source |
| Noms de domaine | Réserver variantes et extensions des marchés ; titulaire = la société, pas le prestataire ; Algérie : « .com.dz » exigé pour l'activité locale (voir `politique-reglementaire-international.md`) |
| Réseaux sociaux | Comptes au nom de la société ; accès tenus en gestionnaire de mots de passe |
| Bases de données | Droit sui generis du producteur (CPI, articles à vérifier) : à opposer au moissonnage, à respecter dans la collecte |

## Licences libres

| Licence | Obligations clés | Effet sur un produit fermé |
|---|---|---|
| MIT, BSD | Conserver la mention de copyright et la licence | Compatible |
| Apache-2.0 | Mention, notice, clause de brevet ; compatible avec GPL-3.0, pas avec GPL-2.0 seule | Compatible |
| MPL-2.0 | Copyleft au niveau du fichier | Compatible si les fichiers modifiés restent ouverts |
| LGPL | Copyleft de la bibliothèque ; liaison dynamique recommandée | Compatible sous conditions |
| GPL-2.0 ou 3.0 | Copyleft fort : l'œuvre dérivée distribuée est sous GPL, sources fournies | Incompatible avec la distribution fermée (application mobile, logiciel installé) |
| AGPL-3.0 | Copyleft étendu à l'usage en réseau : l'utilisateur distant peut demander les sources | Visé pour un SaaS : exclure ou isoler (décision type 1) |
| SSPL, BSL, licences « source disponible » | Non libres au sens de l'OSI ; restrictions d'usage commercial ou de service | Lire chaque licence ; à valider |

Méthode : partir de `dependances.md` du gardien des normes, générer l'inventaire (outil de nomenclature SBOM), classer chaque dépendance directe et transitive, trancher les cas copyleft. Les versions de licences et leur compatibilité sont des connaissances établies : **à vérifier** par le conseil avant décision. Les magasins d'applications imposent des conditions de distribution : GPL et stores, à vérifier.

## Contenus produits par IA

- La protection d'un contenu généré sans apport créatif humain est incertaine (notes : « protection incertaine sans apport créatif humain », mémoire). Ne pas promettre d'exclusivité sur un contenu entièrement généré.
- Lire les conditions du fournisseur d'IA : propriété des sorties, garantie contre la contrefaçon, usage des données pour l'entraînement.
- Code généré : risque de reproduction de code sous licence ; faire passer l'analyse des licences sur le code généré comme sur le reste.
- Documenter l'apport humain (choix, retouches, prompts conservés) : c'est la preuve en cas de litige.
- Transparence et règles propres à l'IA : voir `ia-plateformes.md`.

## Gabarit de propriete-intellectuelle.md

```markdown
## Synthèse
(titularité, marques, licences à risque, décisions attendues, rappel : projet à valider par un conseil en propriété industrielle)
## Titularité du code et des contenus
## Marques et noms de domaine
## Inventaire des licences tierces
## Contenus générés par IA
## Contrats à signer et clauses de cession
## Points à vérifier
```

## Pièges fréquents

- Payer une agence sans cession écrite : le code ne vous appartient pas.
- Nom de domaine ou dépôt de marque au nom du prestataire ou d'un fondateur.
- Dépendance AGPL ou GPL découverte la veille du lancement.
- Plafond de responsabilité sans exception pour dol, faute lourde et données personnelles (à valider).
- Réversibilité absente ou payante : contraire au Data Act pour les fournisseurs concernés.

## Sources

- Règlement (UE) 2023/2854 (Data Act), EUR-Lex ; Commission, « Data Act explained ».
- Service-Public F23455 (CGV, droits sur images et textes tiers).
- Texte des licences : opensource.org et gnu.org (versions à relever à la date de l'étude).
- Code de la propriété intellectuelle (Légifrance) : articles à relever à la rédaction.
