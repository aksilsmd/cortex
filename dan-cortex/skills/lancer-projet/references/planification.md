# Planification : découpage, charges, chemin critique, jalons, RACI, risques

Référence du `planificateur`. Objet : produire `00-pilotage/planning.md` qu'on peut défendre devant un comité et
que le contrôleur financier peut chiffrer. Règle d'or : **un planning ne se comprime pas pour plaire, il se
renégocie en périmètre, en date ou en moyens.** L'état des méthodes citées est celui d'octobre 2026 ; ce qui n'est pas établi est marqué « hypothèse » ou « à vérifier ».

## Sommaire
1. Découper
2. Estimer à trois points
3. Ordonnancer et trouver le chemin critique
4. Jalons et instances
5. RACI
6. Registre des risques
7. Durées types par type de projet
8. Causes d'échec et garde-fous
9. Gabarit de `planning.md`
10. Contrôles avant de rendre

## 1. Découper

1. Partir des livrables, pas des activités : cahier des charges (EX-, EXNF-), puis lots livrables de 5 à 20 jours
   de charge. Un lot sans livrable vérifiable est mal découpé.
2. Découper sur trois axes : produit (modules), transverse (sécurité, juridique, données, infrastructure), et
   non technique (contenus, marketing, formation, recette, validations de l'utilisateur). Le troisième est celui
   qu'on oublie.
3. Numéroter les lots `L01`, `L02`… et les rattacher à un jalon J1 à J7.
4. Inscrire les **délais subis** (avis, revues de stores, observation) comme des tâches sans charge mais avec durée.

## 2. Estimer à trois points

| Étape | Règle |
|---|---|
| Trois valeurs par lot | optimiste O, probable M, pessimiste P, en jours-personnes |
| Charge attendue | E = (O + 4M + P) / 6 |
| Écart-type | σ = (P − O) / 6 ; pour un chemin, σ² = somme des σ² des lots |
| Base de l'estimation | une ligne : analogie (projet comparable), décompte (écrans, API, règles RG-), ou avis d'expert. Sans base, écrire « hypothèse » |
| Marge | la marge d'aléas se pose **sur le chemin critique, une seule fois**, pas dans chaque lot (sinon chacun consomme la sienne) |

Fixer P à au moins 2 fois O pour tout lot incluant une intégration, une migration de données ou un tiers : c'est
là que les estimations se trompent. Donner une fourchette (« 70 à 90 jours »), jamais une fausse précision.
Le contrôleur financier chiffre à partir de E et de P, pas de M.

## 3. Ordonnancer et trouver le chemin critique

1. Lister pour chaque lot ses prédécesseurs et le type de lien (fin-début par défaut ; décalage explicite sinon).
2. Calculer au plus tôt et au plus tard ; le **chemin critique** est la suite de lots à marge nulle. Le nommer.
3. Paralléliser ce qui ne dépend pas : cela suit la logique des vagues de `phases-et-jalons.md`.
4. Ne pas surcharger une même personne ou un même agent dans la même période : vérifier la charge par ressource.
5. Dépendances externes (fournisseur, validation, tiers) : une ligne chacune, avec propriétaire et date limite.
6. Schéma Mermaid du chemin critique obligatoire (`flowchart LR`), lots critiques marqués.

## 4. Jalons et instances

| Jalon Dan-Cortex | Décision de libération | Instance |
|---|---|---|
| J1 | y aller, pivoter ou renoncer | comité d'opportunité |
| J2 | périmètre, budget, calendrier, risques acceptés | comité de cadrage |
| J3 | architecture et conception | comité d'architecture |
| J5 | go/no-go de lancement | décision type 1 de l'utilisateur |
| J7 | clôture et feuille de route | rétrospective |

Transposition à valider, inspirée de HERMES (décisions de libération de phase par le sponsor) et PRINCE2 7 :
chaque passage de jalon est une décision écrite du porteur, et **l'arrêt est une option explicite** avec critères
écrits. Chaque instance a un mandat et des seuils d'escalade. Trois à quatre niveaux pour un grand compte
(stratégique, pilotage, opérationnel, suivi) ; deux suffisent sous quelques mois. Inscrire au planning les délais
de gouvernance : avis DINUM d'un mois pour un projet d'État de plus de 9 M€, admission sous 7 jours, cycles de
validation de l'utilisateur.

Recette : distinguer VABF (environnement de test, données de test) et VSR (production, données réelles). La VSR
ne démarre qu'après une VA positive ; le CCAG-TIC 2021 prévoit 30 jours d'observation et un seuil
d'indisponibilité de 2 % (marchés publics ; **à valider** par un juriste).

## 5. RACI

Une ligne par décision ou livrable majeur, une seule lettre **A** (approbateur) par ligne.

| Rôle | Tient |
|---|---|
| Porteur du projet | A des décisions de type 1 : périmètre, budget, date, go/no-go |
| Chef d'orchestre | R de la coordination, C de tout |
| Agents experts | R de leur livrable |
| Pôle d'audit | C, jamais R d'un livrable qu'il contrôle |
| Utilisateurs métier | C sur le besoin, A de la recette |

Séparer maîtrise d'ouvrage (besoin, recette) et réalisation ; le porteur ne délègue pas la recette. Une
responsabilité unique de bout en bout est la condition la plus citée de succès (Cour des comptes, 2020 : présente
sur 15 % seulement des projets examinés).

## 6. Registre des risques

Un risque : événement + cause + conséquence, impact et probabilité de 1 à 5, **propriétaire nommé, parade,
déclencheur observable**, date de revue. Saisie : `cortex.py registre risques ajouter …`.

| Score = impact × probabilité | Action |
|---|---|
| 15 et plus | parade engagée avant le jalon suivant, remonter au comité |
| 8 à 14 | parade planifiée, revue à chaque jalon |
| 7 et moins | surveillance |

Distinguer risque (peut arriver), hypothèse (tenue pour vraie), problème (arrivé), dépendance. Provision pour
risques calibrée sur la queue de distribution : Flyvbjerg et Budzier (1 471 projets IT) trouvent 1 projet sur 6
à +200 % de coût en moyenne.

## 7. Durées types par type de projet

**Aucune durée type fiable n'est établie** pour ERP, e-commerce, mobile, SaaS ou site :
ne pas en annoncer. Estimer par analogie avec les projets passés de l'utilisateur, puis par décompte. Ce qui est
sourcé, ce sont les délais incompressibles à inscrire :

| Type | Délais subis (état : octobre 2026) |
|---|---|
| mobile | test fermé Google de 14 jours continus avec 12 testeurs (compte personnel récent) ; revue Apple visée sous 24 h, Google jusqu'à 7 jours ; prévoir 3 à 4 semaines de marge (déduction) |
| saas | SOC 2 Type 1 : 3 à 6 mois ; Type 2 : observation de 3 à 12 mois (sources d'éditeurs) |
| ecommerce | tests de charge avant soldes ; échéances réglementaires datées (voir profil) |
| erp | migrations de données répétées, pilote avant bascule ; échéances de facturation électronique |
| site | observation SEO plusieurs semaines après bascule |
| niche | pré-paiement avant le code ; MVP en semaines (hypothèse) |

## 8. Causes d'échec et garde-fous

| Constat (source) | Garde-fou |
|---|---|
| 8,5 % des projets tenus en coût et délai, 0,5 % avec les bénéfices (Flyvbjerg et Gardner, 16 000 projets) | partir de la classe de référence, pas du cas particulier |
| Panorama d'État : retard moyen 26,6 %, dépassement 36,6 % | mesurer l'écart à la baseline à chaque jalon |
| Pas de responsable unique, projets trop longs (Cour des comptes) | un porteur nommé ; tranches courtes, valeur livrée en 18 mois à 3 ans |
| Dépendance aux prestataires : alerte à 60 % d'externalisation (circulaire d'État) | mesurer la part interne |
| ERP : technologie avant les personnes, reprise de données tardive, sur-personnalisation (Panorama) | données et formation au planning dès le début |
| Gate sans pouvoir d'arrêt | critères d'arrêt écrits |

Les chiffres CHAOS (Standish) ne servent que d'ordre de grandeur : leur méthode est contestée.

## 9. Gabarit de `planning.md`

```markdown
# Planning — <projet>

## Synthèse
<12 lignes : date de fin estimée en fourchette, chemin critique, 3 risques majeurs, écart avec le délai souhaité, décision attendue>

## Hypothèses
## Lots et charges
| Lot | Livrable | Jalon | O | M | P | E | Base |
|---|---|---|---|---|---|---|---|
## Dépendances et chemin critique
<schéma Mermaid, marge explicite>
## Jalons datés
| Jalon | Date cible | Décideur | Critères de passage | Délais subis |
|---|---|---|---|---|
## RACI
## Risques majeurs
<renvoi aux RSQ- du registre>
## Scénarios
<tenir le délai en réduisant le périmètre / décaler / renforcer, avec effet sur coût et risque>
```

## 10. Contrôles avant de rendre

- Chaque lot a une base d'estimation et un jalon ; aucune date sans charge derrière.
- Le chemin critique est nommé, la marge chiffrée ; les activités non techniques figurent au planning.
- Chaque ligne du RACI a un seul A ; chaque risque a propriétaire, parade, déclencheur.
- L'écart avec le délai ou le budget voulu est montré, jamais absorbé.

## Sources

- PMBOK Guide 8th Edition (fin 2025) ; PRINCE2 7 (septembre 2023) ; HERMES 2022, tirage du 31.12.2025 (eCH-0054).
- Cour des comptes, 2020, rapport sur les grands projets numériques de l'État (via Sénat, r20-047).
- Flyvbjerg et Budzier, arXiv 1304.0265 ; Flyvbjerg et Gardner, *How Big Things Get Done* (2023).
- McKinsey/Oxford (2012), grands projets IT : chiffres à vérifier.
- CCAG-TIC 2021, art. 32 à 33 (via code-commande-publique.com).
- Android Developers et Play Console Help (test fermé) ; Apple Developer (revue).
