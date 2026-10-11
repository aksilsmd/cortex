# Réunions types

Pour chaque réunion : la question, les participants en mode `standard`, les critères usuels de décision. En mode
`eclair`, remplacer la collégiale par un panel ; en mode `integral`, ajouter les participants entre parenthèses.

## Réunion de lancement (J0, arbitrage direct ou panel)

- **Question :** l'équipe, le mode et le plan conviennent-ils au projet ?
- **Participants :** noyau, `planificateur` (`stratege-produit`).
- **Sortie :** organigramme et plan de vagues confirmés, hypothèses listées.

## Comité d'opportunité (J1, collégiale, type 1)

- **Question :** y aller, pivoter ou renoncer ; quel positionnement ; quelle option de périmètre ?
- **Participants :** `stratege-produit`, `analyste-concurrence`, `analyste-voix-client`, `controleur-financier`,
  `juriste-numerique`, `architecte-solution` (`analyste-contexte`, `stratege-marketing`).
- **Critères :** taille et accessibilité du marché ; intensité concurrentielle et angle libre ; douleur client
  prouvée ; faisabilité technique ; obstacle juridique ; coût et délai avant premier revenu ; adéquation aux
  moyens du porteur.

## Comité de cadrage (J2, collégiale, type 1)

- **Question :** quel périmètre pour la première version, pour quel budget, à quelle date, avec quels risques acceptés ?
- **Participants :** `expert-cahier-des-charges`, `controleur-financier`, `planificateur`, `architecte-solution`,
  `architecte-securite`, `stratege-produit` (`delegue-protection-donnees`, `stratege-marketing`).
- **Critères :** valeur pour l'utilisateur cible ; coût ; risque ; dépendances ; délai de mise sur le marché.
  Méthode : classer chaque exigence en indispensable, important, souhaitable, écarté.

## Comité d'architecture (J3, collégiale, type 1)

- **Question :** quel langage, quels frameworks, quelle structure, quel schéma de données, quel hébergement,
  quelles dépendances majeures ?
- **Participants :** `architecte-solution` (porte deux options au moins), `architecte-securite`,
  `architecte-donnees`, `gardien-des-normes`, `ingenieur-devops`, `controleur-financier`
  (un développeur de la pile envisagée, `delegue-protection-donnees`).
- **Critères :** adéquation aux exigences non fonctionnelles ; maturité et pérennité ; vivier de compétences ;
  coût total sur trois ans ; sécurité ; réversibilité ; délai de réalisation ; capacité des agents à produire et
  tester dans cette pile.
- **Sortie :** une décision d'architecture (ADR) par choix structurant.

## Revue de conception (J3, panel ou collégiale)

- **Question :** la conception est-elle complète, cohérente et réalisable ?
- **Participants :** `redacteur-sfd`, `cartographe-interactions`, `concepteur-tests`, `architecte-solution`,
  `auditeur-general` en audit de jalon.
- **Entrées :** résultats des contrôles mécaniques (interactions, traçabilité), notes de revue croisée.

## Point d'incrément (J4, arbitrage direct)

- **Question :** l'incrément est-il accepté ; quelles anomalies bloquent ; quel est le lot suivant ?
- **Entrées :** journal de build, registre des anomalies, notes de revue de code.

## Plénière d'audit (J5, collégiale)

- **Question :** pour chaque constat de l'audit général : corriger avant lancement, corriger après à date fixée,
  ou accepter le risque ?
- **Participants :** `auditeur-general` et un représentant de chaque pôle visé par un constat ; `contradicteur`.
- **Particularité :** le tour 1 est la réponse de chaque pôle à ses constats (accepte avec plan de correction, ou
  conteste avec preuve) ; l'auditeur réplique aux contestations ; le noyau arbitre, l'utilisateur tranche les
  constats bloquants. Détail dans le skill `audit-general`.

## Go/no-go de lancement (J5, collégiale, type 1)

- **Question :** lance-t-on à la date prévue ?
- **Participants :** `responsable-lancement`, `recetteur`, `architecte-securite`, `juriste-numerique`,
  `ingenieur-devops`, `stratege-marketing`, `responsable-support-formation`, `auditeur-general`.
- **Critères :** PV de recette ; anomalies ouvertes ; constats d'audit ; sécurité ; conformité ; retour arrière
  prêt et répété ; supervision ; support ; communication. Un seul « non » motivé de la sécurité ou du juridique
  sur un point bloquant suffit à reporter, sauf risque accepté par l'utilisateur.

## Cellule de crise (à tout moment, panel immédiat puis collégiale courte)

- **Déclencheurs :** faille de sécurité, fuite de données, obstacle juridique découvert, dérive forte du budget
  ou du délai, incident de production.
- **Participants :** selon la nature ; toujours `architecte-securite` ou `juriste-numerique` si données ou droit
  sont en cause.
- **Sortie :** mesures conservatoires immédiates, obligations de notification et leurs délais, plan de
  correction, communication.

## Rétrospective (J7, panel)

- **Question :** que garder, que changer, que mesurer la prochaine fois ?
- **Entrées :** registres, journal des agents, bilan de consommation, retours utilisateurs.
- **Sortie :** trois à cinq enseignements actionnables dans le bilan de projet.
