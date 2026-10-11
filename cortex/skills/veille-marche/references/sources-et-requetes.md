# Sources, requêtes et règles de collecte

Ce fichier est lu avant toute collecte, par les analystes et les `collecteur-web`. État des accès : octobre 2026 ; les conditions des sites changent, relire celles de la source avant chaque collecte et noter la date de lecture.

## Sommaire
1. Besoin, source, méthode
2. Requêtes et opérateurs
3. Règles de collecte loyale et licite
4. Fermé, payant ou soumis à accord
5. Fiche de source de marché (gabarit)
6. Registre des sources
7. Pièges et contrôles
8. Sources

## 1. Besoin, source, méthode

| Besoin | Source | Méthode |
|---|---|---|
| Taille du marché (exemple e-commerce français) | Fevad, data.gouv.fr, fédérations, statistiques officielles | TAM par le haut, SAM par segment, SOM par le bas ; vérifier l'édition et les séries révisées |
| Annonceurs et messages publicitaires dans l'UE | Meta Ad Library, TikTok Commercial Content Library | recherche par annonceur et par pays ; archiver visuel et date (fenêtre d'un an pour Meta) |
| Pile et trafic d'un concurrent | BuiltWith, Wappalyzer, Similarweb | recherche du domaine ; croiser deux outils ; marquer « estimation » |
| Applications mobiles et avis | Sensor Tower (licence) | données sous licence ; sinon lecture manuelle d'un échantillon |
| Avis G2, Capterra, Trustpilot | pages publiques de ces sites | lecture manuelle par une personne, ou export ou licence ; aucun scraping |
| Irritants sur Reddit et X | fils publics | accord écrit pour Reddit en usage commercial ; X à l'usage avec budget ; sinon lecture manuelle |
| Distribution des notes | page de la source | relever la répartition par étoile, pas seulement la moyenne |
| Fonctions et prix d'un concurrent | pages produit, tarifs, documentation, notes de version | lecture, archive datée |
| Emploi et financement | pages carrières, communiqués, presse | faits datés avec URL ; bases de levées (Crunchbase, Dealroom) non vérifiées |
| Positionnement | page d'accueil, publicités, vidéos de démonstration | citation exacte courte |
| Contexte légal, fiscal | textes officiels, autorités | repérage pour le juriste, marqué « à valider » |
| Risque d'échec | CB Insights et retours de fondateurs | trois causes racines contrôlées avant construction |

## 2. Requêtes et opérateurs

- **Une requête, un sujet.** Les requêtes qui mêlent plusieurs sujets séparés par des points-virgules ont renvoyé zéro résultat dans l'outil de recherche testé ; les découper.
- Opérateurs acceptés par cet outil : guillemets, `-terme`, `site:`, `inurl:`, `intitle:`, `related:`, filtre par domaines. À tester sur chaque moteur disponible.
- Gabarits à adapter (remplacer X par le nom du produit) : `"alternative to X"`, `"X vs"`, `"switched from X"`, `"X cancel"`, `"X pricing" expensive`, `"I wish X"`, `site:reddit.com "X"`, `site:news.ycombinator.com "Show HN"`, `intitle:"best" <catégorie>`, `filetype:pdf <secteur> 2026`, `site:fevad.com <thème>`.
- N'ouvrir que des URL issues des résultats de recherche ou des fiches : l'outil de lecture de pages a refusé des URL construites par l'agent.
- Les API de recherche changent : Bing Search APIs retirées le 11 août 2025 ; Google Custom Search JSON API fermée aux nouveaux clients, clients existants jusqu'au 1er janvier 2027 (annonce relayée par des tiers, page de Google non lue : à vérifier). Utiliser le fournisseur de recherche de la session, interchangeable, et **journaliser requête, URL, date et extrait** dans la fiche.
- Budget fixé par l'ordre de mission (10 à 15 recherches par fiche) ; s'arrêter quand trois sources répètent la même chose.

## 3. Règles de collecte loyale et licite

1. **Conditions d'utilisation d'abord.** Lire celles de la source ; si elles interdisent la collecte automatisée, ne pas collecter par agent. Un contenu public n'est pas pour autant réutilisable (RGPD, conditions, droit d'auteur, droit des bases de données).
2. **`robots.txt`, CAPTCHA et signaux d'opposition** (`ai.txt`, TDMRep, balise `noai`) : respectés ; leur présence arrête la collecte de ce site.
3. **Pas de contournement :** ni proxys rotatifs, ni faux comptes, ni résolution de CAPTCHA, ni accès par compte emprunté. Un compte d'essai ouvert honnêtement par l'utilisateur est possible si les conditions l'autorisent.
4. **Pas de données nominatives.** Ne noter ni auteur, ni pseudonyme, ni lien de profil ; supprimer à l'ingestion ce qui identifie une personne ; exclure santé, mineurs, profils privés ; données sensibles découvertes par hasard : ne pas les conserver.
5. **Pas d'aspiration massive :** lecture ciblée et échantillonnée, quelques dizaines de pages par fiche, pas de parcours en série d'un site.
6. **Contenus accessibles sans compte** uniquement.
7. **Loyauté :** aucun faux avis, aucun faux profil ; lors d'un entretien, dire qui l'on est et pourquoi l'on demande.
8. **Citer et dater.** Citation exacte de 25 mots au plus ou reformulation signalée « (R) » ; pas de reproduction de pages entières.
9. **Conservation courte** des fiches brutes ; durée et base légale notées au registre. Cadre : la fiche de la CNIL du 19 juin 2025 sur le moissonnage vise le développement d'IA ; l'appliquer par analogie à la veille ne vaut pas garantie de conformité. Validation par le `delegue-protection-donnees`. Une note CNIL et CIANum sur l'IA agentique (20 juillet 2026) a été repérée sans être lue : à lire.

## 4. Fermé, payant ou soumis à accord

| Source | État | Conséquence |
|---|---|---|
| G2, Capterra, Trustpilot | scraping interdit, y compris pour entraîner ou évaluer un modèle | lecture manuelle ou licence ; ne pas lancer de collecteur automatisé |
| Reddit | accord écrit pour l'usage commercial | demander à l'utilisateur ; sinon lecture manuelle |
| X | 0,005 $ par ressource lue, plafond de 3 M de lectures par mois | fixer un budget avant |
| TikTok Research API | réservée aux chercheurs éligibles | utiliser la Commercial Content Library |
| BuiltWith | environ 295 $ et 495 $ par mois selon l'offre (extrait de l'été 2026, à revérifier) | version gratuite pour un domaine, ou demander l'accès |
| Similarweb, Sensor Tower, Semrush | gratuit limité ou payant ; Semrush racheté par Adobe selon une source secondaire, date à vérifier | croiser deux outils ; accès à demander |
| API d'avis des magasins d'applications | réputées limitées aux applications de l'éditeur (non vérifié) | licence ou lecture manuelle |
| Hacker News, Product Hunt, GitHub, YouTube, TikTok, Instagram, LinkedIn | conditions et API non vérifiées | lire les conditions avant |

Quand un accès est fermé, **le dire** dans « non trouvé et limites » et proposer à l'utilisateur la voie d'accès (licence, export de ses propres tickets, entretiens).

## 5. Fiche de source de marché (gabarit)

Pour `01-decouverte/sources/marche/<slug>.md`, 40 lignes au plus.

````markdown
# Fiche de source — <organisme ou étude>
Collecté le : <date> par collecteur-web · URL : <url> · Édition ou millésime : <> · Nature : primaire | secondaire

## Chiffres relevés
| Donnée | Valeur et unité | Périmètre | Page ou tableau | Consulté le |
|---|---|---|---|---|

## Faits datés (contexte)
Fait, échéance, URL, date.

## Limites
Séries révisées, définition du périmètre, accès partiel, non trouvé.
````

## 6. Registre des sources

Dans la synthèse de chaque livrable, un tableau : source, statut (API officielle, licence, conditions interdisant le scraping, lecture manuelle, ouvert), date de lecture des conditions, décision de collecte. C'est lui que le délégué à la protection des données relit.

## 7. Pièges et contrôles

Chiffres périmés ou accès changés ; fiche remplie de mémoire sans URL ; confondre « public » et « réutilisable » ; oublier la date de consultation.

Contrôles avant de rendre une fiche : toute valeur a URL et date ; conditions lues et notées ; aucune donnée nominative ; « non trouvé » écrit là où c'est le cas.

## Sources

- CNIL, focus sur le moissonnage (19 juin 2025) : https://www.cnil.fr/fr/focus-interet-legitime-collecte-par-moissonnage
- CNIL, base légale de l'intérêt légitime : https://www.cnil.fr/fr/base-legale-interet-legitime-developpement-systeme
- Microsoft Learn, retrait des API Bing : https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement
- Meta Ad Library API : https://www.facebook.com/ads/library/api/
- Reddit, Data API Terms : https://redditinc.com/policies/data-api-terms
- X API, tarifs : https://docs.x.com/x-api/getting-started/pricing
- Directive (UE) 2019/790, considérant 18 sur l'opposition lisible par machine, via la fiche CNIL ci-dessus.
