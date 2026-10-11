# Choisir langage, frameworks, base de données et outils

Méthode pour instruire un choix technique avec au moins deux options, le noter sur une grille pondérée et le soumettre au comité d'architecture. État des chiffres : octobre 2026, extraits automatiquement, à recouper avant publication.

## Sommaire
1. Acheter, configurer ou construire
2. Panorama des langages
3. Versions de référence
4. Grille de décision pondérée
5. Capacité des agents à produire et tester
6. Piles de référence par contexte
7. Dépendances et outils
8. Pièges et contrôles

## 1. Acheter, configurer ou construire

Première décision d'architecture, à traiter en J1 (note de faisabilité) et à confirmer en J3. Chiffrer trois options au minimum sur 3 à 5 ans : licences ou abonnements, intégration, exploitation, évolution, sortie.

| Situation | Choix | Pourquoi |
|---|---|---|
| Besoin générique, bien couvert par le marché (paie, comptabilité, CMS, messagerie, paiement) | acheter (SaaS) | le coût de maintenance est mutualisé |
| Besoin standard avec particularités de processus | configurer un progiciel ou une plateforme | écart au standard limité à l'extension, jamais au cœur |
| Cœur différenciant, avantage concurrentiel | construire | c'est la valeur du produit |
| Fournisseur unique sans export de données | éviter, ou plan de sortie chiffré | le verrouillage est un coût futur |

Pour « acheter » : export complet des données en format ouvert ? continuité du fournisseur ? hébergement et sous-traitants conformes ? coût à dix fois le volume ? Écrire le résultat dans `01-decouverte/note-faisabilite-technique.md`, puis en ADR.

## 2. Panorama des langages

Croiser au moins trois classements datés : Stack Overflow 2026 (JavaScript 62,0 %, Python 58,0 %, TypeScript 43,8 %), TIOBE sept. 2026 (Python 1er), RedMonk janv. 2026, GitHub Octoverse 2025 (TypeScript 1er en contributeurs), JetBrains 2025. Ils mesurent des choses différentes : aucun ne désigne le meilleur langage.

| Langage | Usage de prédilection | Limites | Mémoire |
|---|---|---|---|
| TypeScript, JavaScript | web, Node, full-stack | typage effacé à l'exécution, écosystème npm volatil | sûr |
| Python | données, IA, scripts, API | lent en calcul pur | sûr |
| Java | systèmes d'information d'entreprise, banque | verbeux, démarrage lourd | sûr |
| C# et .NET | systèmes d'information, API, jeux | écosystème Microsoft | sûr |
| Kotlin, Ruby | Android et JVM, KMP ; web Rails | vivier plus étroit ou en recul | sûr |
| Go | services réseau, outils cloud | abstractions limitées | sûr |
| Rust | systèmes, composants critiques | courbe d'apprentissage, vivier rare | sûr hors `unsafe` |
| PHP | web, CMS, e-commerce | héritage hétérogène | sûr |
| Swift, Dart | iOS ; Flutter | périmètre Apple ; marginal hors Flutter | sûr |
| C, C++ | systèmes, embarqué, moteurs | mémoire manuelle | non sûr |

La CISA et la NSA (juin 2025) recommandent les langages à mémoire sûre : justifier par écrit tout code C ou C++. Vivier sûr pour un grand compte : Java, C#, TypeScript, Python ; Go et Rust pour des composants ciblés. Le vivier local (France, Maghreb) n'a pas été trouvé : à vérifier.

## 3. Versions de référence (octobre 2026)

| Composant | Version et support | Remarque |
|---|---|---|
| Java | 25 LTS (Premier Support jusqu'en sept. 2030) ; 27 courante ; prochaine LTS : 29 (sept. 2027) | ne pas mettre une non-LTS en production |
| Spring Boot | 4.1.1 courante ; 4.0 OSS jusqu'en déc. 2026 ; 3.5 hors support libre depuis juin 2026 | support commercial payant ensuite |
| .NET | 10 LTS jusqu'au 14 nov. 2028 ; 8 et 9 s'arrêtent le 10 nov. 2026 | |
| Node.js | 24 et 22 LTS ; 26 courante ; dès Node 27, majeure annuelle toujours LTS | |
| Python | 3.15 (9 oct. 2026) ; 3.10 en fin de vie le 1er oct. 2026 | |
| Django | 6.1.2 ; LTS 5.2 jusqu'en avr. 2028 ; LTS 6.2 prévue avr. 2027 | |
| PHP | 8.5 (sécurité jusqu'au 31 déc. 2029) ; 8.2 s'arrête le 31 déc. 2026 | |
| React, Next.js | React 19.3.0 ; Next.js 16 en LTS active, 15 en maintenance | |
| Angular | 22 (LTS jusqu'en juin 2028) ; 21 et 20 en LTS | |
| React Native, Flutter | 0.84 ; Flutter 3.47 | |
| PostgreSQL | 18 (support jusqu'au 14 nov. 2030) ; 14 close le 12 nov. 2026 ; 19 en bêta | |

À vérifier à la source avant décision : Vue/Nuxt, Svelte, Astro, NestJS, FastAPI, Symfony, Rails, Kotlin, SwiftUI, Compose, Expo, Laravel 13.

## 4. Grille de décision pondérée

Synthèse sans standard sourcé : calibrer les poids en atelier, puis les figer avant de noter. Note de 1 (très défavorable) à 5 (très favorable), justifiée en une ligne. Score sur 100 = somme(poids × note) ÷ 5.

| Critère | Poids | Option A | Option B | Justification des notes |
|---|---|---|---|---|
| Adéquation au domaine | 15 | | | |
| Vivier et coût des compétences (humaines et agents) | 15 | | | |
| Maturité et support à long terme | 12 | | | |
| Sécurité et conformité (CRA, mémoire sûre) | 12 | | | |
| Performance et scalabilité | 10 | | | |
| Maintenabilité et évolutivité | 10 | | | |
| Écosystème, santé des dépendances, licences | 8 | | | |
| Coût total sur 3 à 5 ans | 8 | | | |
| Intégration au système d'information, verrouillage | 6 | | | |
| Délai de mise sur le marché | 4 | | | |
| **Total** | 100 | | | |

Éliminatoires, vérifiés avant de noter : support de moins de trois ans, licence incompatible, non-conformité réglementaire, échec de la tranche verticale (section 5). Un écart de moins de 5 points est un ex æquo (hypothèse à calibrer) : départager par la réversibilité et le coût de sortie.

## 5. Capacité des agents à produire et tester

Les agents écrivent et testent le code : une pile mal maîtrisée coûte en corrections. Noter l'axe « agents » du critère Vivier avec ces cinq tests.

| Test | Réussi si |
|---|---|
| Typage statique | un vérificateur de types détecte les erreurs avant l'exécution (étude citée par GitHub : 94 % des erreurs de compilation des modèles sont des échecs de typage) |
| Écosystème courant | framework répandu, documentation à jour |
| Tests en terminal | tous les types de tests lançables sans interface graphique |
| Garde-fous automatiques | formateur, analyseur et vérificateur de types lancés par un seul script |
| Dépendances vérifiables | chaque paquet existe (45,1 % des répondants constatent des paquets « hallucinés ») |

**Tranche verticale obligatoire :** faire écrire à un agent, par option, un cas réel (un écran ou une route, une table, une migration, un test d'API) et mesurer : passe au premier essai ? nombre de corrections ? temps ? Conserver le résultat dans le dossier d'architecture.

## 6. Piles de référence par contexte

Illustrations à adapter, jamais des préférences.

| Contexte | Pile de référence (octobre 2026) |
|---|---|
| MVP de startup | TypeScript (Next.js 16 et React 19, ou SvelteKit) ou Python avec FastAPI, sur Node 24 LTS ; PostgreSQL 18 managé avec pgvector ; monolithe modulaire ; REST et OpenAPI ; mobile avec Expo ou Flutter |
| Scale-up | monolithe modulaire et services ciblés (Go, Java, Kotlin) ; PostgreSQL et Redis ou Valkey ; recherche dédiée ; Kafka, RabbitMQ ou NATS si événements ; BFF ; C4 et ADR |
| Grand compte | Java 25 avec Spring Boot 4.1, ou .NET 10 ; Angular 22 ou Next.js 16 ; PostgreSQL, Oracle ou SQL Server selon l'existant ; Kafka ; évaluation de scénarios, arc42, C4, ADR, fitness functions |
| Secteur régulé | LTS à support commercial, langages à mémoire sûre, dépendances épinglées avec SBOM et seuil de score, isolation forte des locataires, ADR tracées |
| Mobile | Expo ou Flutter ; SwiftUI ou Compose en natif si matériel ou expérience pointus ; KMP si l'équipe est Kotlin |
| Site vitrine ou e-commerce | plateforme du marché configurée d'abord ; code sur mesure limité aux écarts (versions : à vérifier) |

## 7. Dépendances et outils

Pour chaque dépendance directe : licence compatible, plusieurs mainteneurs, publication récente, fenêtre de support, score OpenSSF Scorecard (0 à 10, seuil à calibrer), version épinglée avec empreinte, SBOM à chaque build. Les attaques npm de septembre 2025 (plus de 500 paquets) et le changement de licence de Redis (fork Valkey) justifient ces seuils. Règles détaillées : `references/normes-developpement.md`.

## 8. Pièges et contrôles

- Confondre popularité et adéquation ; copier les géants.
- Fixer les poids après avoir vu les options : la grille note alors un favori.
- Choisir un moteur sans lire sa licence ni prévoir la sortie.
- Avant de rendre : deux options notées, éliminatoires vérifiés, tranche verticale jointe, dates de fin de support notées, ADR écrite.

## Sources

- Stack Overflow Developer Survey 2026 : https://survey.stackoverflow.co/2026/technology/data
- TIOBE Index, sept. 2026 : https://www.tiobe.com/tiobe-index/
- CISA, mémoire sûre, 24 juin 2025 : https://www.cisa.gov/news-events/alerts/2025/06/24/new-guidance-released-reducing-memory-related-vulnerabilities
- Calendriers de support : https://www.oracle.com/java/technologies/java-se-support-roadmap.html ; https://dotnet.microsoft.com/en-us/platform/support/policy/dotnet-core ; https://www.postgresql.org/support/versioning/
- OpenSSF Scorecard : https://github.com/ossf/scorecard
