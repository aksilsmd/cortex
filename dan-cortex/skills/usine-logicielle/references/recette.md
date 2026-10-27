# Recette : stratégie, cahier, campagnes, anomalies, procès-verbal

Organiser la recette de façon que « prêt à lancer » repose sur des preuves : un cahier tracé aux exigences, des campagnes menées par quelqu'un qui n'a pas codé, des anomalies au registre, un procès-verbal lié à la version testée. Vocabulaire ISTQB en français. Le cadre ci-dessous est une synthèse d'expert, non sourcée : le valider avec l'utilisateur.

## Sommaire
1. Stratégie de test
2. Cahier de recette
3. Campagnes
4. Anomalies
5. Critères d'entrée et de sortie
6. Procès-verbal de recette
7. Recette utilisateur
8. Gabarits
9. Pièges et contrôles

## 1. Stratégie de test

Écrite par le `concepteur-tests` à J3, avant le cahier. Elle fixe : niveaux et types retenus (voir `tests-par-niveau.md`), propriétaire et outil de chacun, environnements, données, seuils, rôles, calendrier, critères d'entrée et de sortie, risques produit classés (les risques dirigent l'effort de test) et l'outil de suivi (Xray, Squash TM, TestRail, ou le registre du script si le projet est petit). Choisir selon l'intégration au gestionnaire de tickets et l'exigence de traçabilité.

## 2. Cahier de recette

Fichier : `03-conception/tests/cahier-de-recette.md`. Un cas CT- par ligne, **identifiant en première colonne**, et sur la même ligne les identifiants couverts : RG-, WF-, EL-, EXNF-. Le script `cortex.py tracabilite verifier` lit ces liens : chaque RG- et chaque WF- doit être cité par un CT-, chaque EL- par un CT- ou par le CT- de son workflow.

Règles de rédaction d'un cas :
- Un objectif, une vérification. Préconditions (rôle, données), étapes numérotées dans une seule cellule séparées par « ; », résultat attendu observable et exact (texte du message, écran de destination).
- Priorité = ordre d'exécution et de correction : `critique` (parcours sans lequel le produit n'a pas de sens), `haute`, `normale`.
- Mode : `manuel` ou `auto` (référence du test automatisé).
- Pas de barre verticale dans une cellule.

## 3. Campagnes

| Campagne | Contenu | Quand |
|---|---|---|
| Fumée | une dizaine de cas critiques, prouve que la version est testable | à chaque déploiement en recette |
| Fonctionnelle (VABF) | tout le cahier, par module | J5, version figée |
| Non-régression | cas `auto` stables, étiquette `@regression` | après chaque lot de corrections |
| Non fonctionnelle | performance, accessibilité, compatibilité | J5, en parallèle |
| Service régulier (VSR) | exploitation : supervision, sauvegarde, restauration | J5, avec `ingenieur-devops` |
| Utilisateur (UAT) | scénarios métier par le client | voir section 7 |

Une campagne a un numéro, une version testée (commit ou étiquette), un environnement, des dates et un exécutant. Les cas manuels sont exécutés dans l'ordre de priorité. Un cas bloqué (dépendance en échec) est marqué `bloqué`, pas `échec`.

Statuts d'un cas : `à exécuter`, `passé`, `échec`, `bloqué`, `non applicable` (motif écrit).

## 4. Anomalies

Une anomalie par défaut distinct, au registre par script :

`python3 ${CLAUDE_PLUGIN_ROOT}/skills/lancer-projet/scripts/cortex.py registre anomalies ajouter titre="…" severite=majeure cas_de_test=CT-012 lot=… description="étapes, attendu, obtenu, version, preuve" responsable=…`

Le statut initial est `ouverte`. Mettre à jour avec `registre anomalies maj ANO-003 statut=…`. Toute anomalie cite son CT-, donc son exigence.

| Sévérité (impact) | Critère | Effet |
|---|---|---|
| `bloquante` | parcours critique impossible, perte ou fuite de données, faille exploitable | interdit le jalon |
| `majeure` | fonction dégradée, contournement lourd ou absent | corrigée ou contournement validé par écrit |
| `mineure` | gêne sans perte fonctionnelle | peut être reportée avec accord |

Distinguer sévérité (impact, fixée par le recetteur) et priorité (ordre de correction, fixée avec le chef de projet). Une faille de sécurité est aussi un constat : la signaler à `auditeur-securite`.

Cycle de vie : `ouverte` → qualifiée (reproductible, sévérité posée) → assignée → `corrigee` → `a-retester` → `fermee` (contre-test passé et non-régression au vert). Sorties : `rejetee` (non-défaut, avec motif) ou `reportee` (accord écrit, version cible). Seul le recetteur ferme une anomalie, jamais son auteur. Un contre-test ou une non-régression en échec rouvre l'anomalie.

## 5. Critères d'entrée et de sortie

**Entrée** (sinon la campagne n'est pas lancée) : version déployée et identifiée ; campagne de fumée au vert ; données chargées ; périmètre figé ; cahier relu ; aucune anomalie bloquante ouverte de J4.

**Sortie** (cibles chiffrées à confirmer dans la stratégie) :
- 100 % des cas critiques exécutés et passés ;
- 100 % des cas exécutés, ou écarts justifiés ;
- 0 anomalie bloquante ouverte ;
- anomalies majeures : corrigées, ou contournement validé par l'utilisateur ;
- non-régression au vert sur la version finale ;
- `tracabilite verifier` sans erreur : toute exigence a un cas, tout cas un résultat.

## 6. Procès-verbal de recette

Fichier : `05-validation/pv-recette.md`. Lié à une version précise : une autre version exige une nouvelle campagne au moins en fumée et non-régression. Signé par l'utilisateur ou son représentant, **avec ou sans réserves** ; les réserves sont des anomalies listées. La signature est un acte humain : le recetteur prépare, il ne signe pas à la place du client.

## 7. Recette utilisateur

Définir par écrit : panel (rôles, effectif), durée, scénarios métier (pas le cahier technique), canal de retour unique, critère de clôture (par exemple tous les scénarios exécutés, aucune anomalie bloquante). Une bêta ouverte est cadrée de même, avec information et consentement des testeurs si des données personnelles sont traitées. Les retours deviennent des anomalies au registre ou des évolutions hors périmètre.

## 8. Gabarits

### `03-conception/tests/strategie-de-test.md`

```markdown
# Stratégie de test — <projet>

## Synthèse
<12 lignes au plus : niveaux retenus, outils, risques majeurs, seuils, environnements, points « à vérifier ».>

## 1. Périmètre et risques produit
## 2. Niveaux, outils, propriétaires, temps cibles
## 3. Environnements et données de test
## 4. Critères d'entrée et de sortie
## 5. Gestion des anomalies (sévérité, priorité, cycle de vie, outil)
## 6. Rôles et indépendance
## 7. Calendrier des campagnes
## 8. Sources
```

### `03-conception/tests/cahier-de-recette.md`

```markdown
# Cahier de recette — <projet>

## Synthèse
<Nombre de cas, répartition manuel et auto, résultat de tracabilite verifier, règles sans cas.>

## Cas de test
| ID | Objectif | Couvre | Préconditions | Étapes | Résultat attendu | Priorité | Mode |
|---|---|---|---|---|---|---|---|
| CT-001 | Connexion valide | RG-001, WF-001, EL-001-01 | compte actif | saisir e-mail et mot de passe valides ; cliquer « Se connecter » | EC-002 s'affiche, session ouverte | critique | auto |
```

### `05-validation/pv-recette.md`

```markdown
# Procès-verbal de recette — <projet>

## Synthèse
<Version testée, verdict, nombre de cas passés et en échec, anomalies ouvertes par sévérité.>

## 1. Version et environnement testés (commit ou étiquette, date)
## 2. Campagnes menées
## 3. Résultats par module
## 4. Anomalies ouvertes et réserves
## 5. Écarts aux critères de sortie
## 6. Décision
Recette prononcée : sans réserve / avec réserves / refusée.
Signataire : <nom, fonction, date>
```

## 9. Pièges et contrôles

- Critères de sortie non chiffrés ; anomalie sans lien à l'exigence ; PV sans version ; non-régression oubliée après correctifs.
- Recetteur qui corrige : il constate et consigne, il ne répare pas.
- Cas écrits après coup pour épouser le code : concevoir depuis les RG- et la matrice.
- Avant de rendre : le script de traçabilité passe ; chaque cas a un résultat attendu exact ; chaque anomalie a un CT-.

## Sources

- ISTQB, syllabus CTFL v4.0.1 : niveaux et types de test, test de maintenance.
- ISO/IEC/IEEE 29119-1:2022 ; série 29119 pour le vocabulaire et les documents de test.
- DORA 2025 : sans tests automatisés ni retour rapide, plus de changements dégrade la stabilité.
- Cadre recette (VABF, VSR, UAT, critères) : synthèse d'expert non sourcée, à valider.
