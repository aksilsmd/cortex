# Stratégie et positionnement : de l'analyse aux décisions

Ce fichier guide `stratege-produit`. Il part des quatre analyses et des fiches, et produit `01-decouverte/note-opportunite.md` : ce qui manque, ce qu'il faut ajouter, supprimer, différencier, le positionnement, deux ou trois options de périmètre chiffrées et les tests de demande. Le stratège **tranche l'angle** et recommande ; la décision d'y aller reste à l'utilisateur.

## Sommaire
1. Entrées et vérification
2. Analyse d'écarts
3. Priorisation
4. Positionnement
5. Options de périmètre
6. Tests de demande
7. Critères d'aller, de pivot, de renoncement
8. Gabarit de la note d'opportunité
9. Pièges et contrôles
10. Sources

## 1. Entrées et vérification

Lire les synthèses des quatre analyses, puis seulement les lignes de détail dont dépend un choix. Avant de s'appuyer sur un constat, regarder son statut : un thème « indice » ou « anecdote » ne fonde pas une option à lui seul. Lire aussi le prédiagnostic juridique, la note de faisabilité technique et les ordres de grandeur de coût : une option infaisable ou illégale ne se recommande pas.

## 2. Analyse d'écarts

Construire le tableau besoin × concurrents × nous, une ligne par besoin (fonction, qualité ou service), puis classer :

| Cas | Condition observée | Décision |
|---|---|---|
| a | attendu partout, absent chez nous | **AJOUTER** (parité nécessaire) |
| b | mal servi partout, irritant récurrent et sévère | **DIFFÉRENCIER** : priorité n°1 |
| c | besoin fréquent que personne ne couvre | **AJOUTER après test de demande** |
| d | fonction coûteuse, rarement citée, ou jugée indifférente | **SUPPRIMER** ou ne pas copier |
| e | force actuelle ou satisfaction que les clients citent | **PROTÉGER** |

Chaque ligne reçoit un identifiant `ECA-` et cite les `THM-` (voix du client), les `CON-` (concurrents) et les `FAC-` (contexte) qui la fondent. Une ligne sans preuve est une hypothèse `HYP-`. Les lignes ajouter et différencier deviennent des candidates aux exigences `EX-` du cahier des charges, qui citera l'`ECA-`.

Classer chaque fonction selon Kano (attendue, proportionnelle, enthousiasmante, indifférente, rejetée) à partir des avis : une fonction attendue ne différencie pas, elle évite de perdre.

## 3. Priorisation

| Outil | Usage | Règle |
|---|---|---|
| RICE | ordre des candidats : Reach × Impact × Confidence ÷ Effort | Reach en clients par trimestre issu de l'étude de marché ; Effort en jours-personnes donnés par l'architecte ou le contrôleur financier ; **Confidence** reprend les preuves : 100 % pour un thème confirmé sur trois sources, 80 % pour deux, 50 % pour un indice, 20 % pour une anecdote (échelle de travail du plugin) |
| MoSCoW | périmètre de la première version | Must : sans cela l'offre ne se vend pas ou n'est pas légale ; Should ; Could ; Won't, avec la raison écrite |

Le score ordonne, il ne décide pas : un Must légal passe devant un score élevé. Toute fonction supprimée figure dans « ce qu'on ne fera pas », avec sa raison, pour éviter qu'elle revienne.

## 4. Positionnement

Cinq éléments, dans l'ordre (méthode Dunford, référence de mémoire, non vérifiée à la source) :
1. **Alternatives** réelles du client, y compris « ne rien faire » ;
2. **Attributs uniques** que ces alternatives n'ont pas, étayés par une preuve ;
3. **Valeur** que ces attributs apportent, dans les mots des clients (verbatims) ;
4. **Clients best-fit** : le segment pour qui cette valeur compte le plus (critères observables) ;
5. **Catégorie** dans laquelle le client nous comprend vite.

Retenir le couple **job × segment** où quatre conditions se combinent : irritant fréquent, alternatives faibles, canal accessible, consentement à payer observé. Écrire la phrase de positionnement en une ligne, plus la phrase qu'un concurrent ne pourrait pas dire. Le `stratege-marketing` la reprend en J2.

## 5. Options de périmètre

Proposer **deux ou trois options**, jamais une seule, présentées de façon comparable :

| Option | Contenu (Must et Should) | Ce qu'on ne fait pas | Coût de construction et d'exploitation (ordre de grandeur, du contrôleur financier) | Délai | Risque principal | Preuve de demande requise avant |
|---|---|---|---|---|---|---|

Typiquement : OPT-A minimale (le différenciant seul, vendable vite), OPT-B de parité plus différenciant, OPT-C ambitieuse. Si la meilleure option est de **ne pas construire** (acheter une solution, s'intégrer, renoncer), la présenter comme option à part entière. Recommander une option avec ses motifs et les options écartées.

## 6. Tests de demande

Du moins au plus engageant. **Fixer les seuils de succès par écrit avant le test**, sinon on interprète après coup.

| Test | Ce qu'il prouve | Seuil à écrire d'avance (exemple) |
|---|---|---|
| Entretiens sur faits passés (≥ 10, « la dernière fois que… ») | la douleur existe et coûte | 7 sur 10 décrivent un contournement actuel |
| Page d'attente | l'intérêt pour la promesse | taux d'inscription au-dessus de X % sur N visites qualifiées |
| Faux bouton (clic sur la fonction non construite) | l'intérêt pour une fonction précise | à fixer par fonction |
| Pré-vente ou lettre d'intention | le consentement à payer | nombre d'engagements ; un conseil anecdotique cité sur Hacker News (2013) évoque 30 engagements payants avant de coder |
| Prototype ou MVP « concierge » | l'usage réel | taux d'activation, retours |

L'agent prépare les tests (textes, pages, grilles d'entretien) ; l'utilisateur les lance. Aucun faux avis ni fausse rareté dans un test ; les entretiens respectent le consentement et le RGPD.

## 7. Critères d'aller, de pivot, de renoncement

Poser trois critères avant de recommander : **produit-marché** (douleur confirmée sur trois sources, segment accessible), **timing** (tendance et échéances réglementaires favorables), **économie unitaire** (prix observé supérieur au coût d'acquisition plausible sur douze mois). CB Insights (mars 2026) cite ces trois causes racines d'échec (43 %, 29 %, 19 %) ; le manque de capital, première cause terminale (70 %), en est la conséquence. Une option dont un critère échoue reçoit « pivoter » ou « renoncer », avec ce qui changerait l'avis.

## 8. Gabarit de la note d'opportunité

````markdown
# Note d'opportunité — <projet>

## Synthèse
<12 lignes : recommandation (aller, pivoter, renoncer, tester d'abord) ; positionnement en une phrase ; segment ; option recommandée ; 3 ajouts, 3 suppressions, 3 différenciations ; test de demande et seuils ; confiance ; décisions attendues du comité>

## Positionnement
Alternatives, attributs uniques, valeur, clients best-fit, catégorie, phrase.
## Ce qui manque sur le marché et écarts
| ID | Besoin | Concurrents | Nous | Décision (ajouter, supprimer, différencier, protéger) | Preuves (THM-, CON-, FAC-) | Kano | RICE |
|---|---|---|---|---|---|---|---|
| ECA-01 | | | | | | | |
## Options de périmètre
| ID | Contenu | Hors périmètre | Coût | Délai | Risque | Écarts couverts (ECA-) |
|---|---|---|---|---|---|---|
| OPT-A | | | | | | |
## Recommandation et options écartées
## Aller, pivoter, renoncer : critères et état
## Tests de demande : plan et seuils
## Hypothèses et ce qui changerait l'avis
## Annexe : pré-mortem du contradicteur
````

## 9. Pièges et contrôles

- Copier les concurrents au lieu de viser leurs irritants non résolus ; tout ajouter ; une seule option.
- Positionnement vague (« simple et puissant »).
- Confondre la cause terminale (argent) et les causes racines.
- Contrôles avant de rendre : chaque `ECA-` cite des preuves ; chaque suppression a une raison ; trois critères d'aller examinés ; options chiffrées avec source des coûts ; seuils écrits ; recommandation séparée de la décision.

## Sources

- CB Insights, causes d'échec (6 mars 2026) : https://www.cbinsights.com/research/report/startup-failure-reasons-top/
- Christensen et al., Jobs to be done, HBR, 2016 : https://hbr.org/2016/09/know-your-customers-jobs-to-be-done
- Post-mortem r/SaaS (anecdote, auto-déclaré) : https://www.reddit.com/r/SaaS/comments/1towpxq/im_shutting_down_my_ai_video_saas_after_1078_in/
- Commentaire Hacker News, 2013 (anecdote) : https://news.ycombinator.com/item?id=6585535
- RICE, MoSCoW, Kano, Dunford : aucune source primaire retrouvée (état : octobre 2026) ; références de mémoire, à vérifier.
