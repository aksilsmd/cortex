# Orchestration du pôle Sécurité

Pour le chef d'orchestre, ou pour l'orchestrateur du pôle. Les agents experts n'ont pas besoin de ce fichier.

## Agents du pôle

| Agent | Niveau | Lancé quand |
|---|---|---|
| `architecte-securite` | A | J2 pour l'analyse de risques ; J3 vague 3A pour le modèle de menaces et l'architecture, en binôme avec `architecte-solution` ; J6 pour le plan de réponse à incident |
| `auditeur-securite` | B | J3 pour le plan de tests ; J4 après chaque incrément (contrôles automatisés) ; J5 pour le rapport de tests complet et le contre-test |
| `testeur-intrusion` | B | J5, vague 5A, seulement avec périmètre et autorisation écrits |

Activation : `architecte-securite` dès qu'il y a données personnelles, paiement ou comptes ; `testeur-intrusion` si le produit est exposé à internet avec données sensibles. Sinon `auditeur-securite` couvre le minimum.

## Vagues types

| Jalon et vague | Missions lancées ensemble | Entrées | Sorties |
|---|---|---|---|
| J2, 2A | `architecte-securite` : analyse de risques, niveau ASVS proposé, régimes applicables | fiche projet, note de cadrage, cartographie des données | `02-cadrage/analyse-risques-securite.md` |
| J3, 3A | `architecte-securite` : modèle de menaces et architecture de sécurité ; en parallèle `ingenieur-devops` (infrastructure) et `architecte-solution` (architecture) | analyse de risques, flux du dossier d'architecture | `03-conception/securite/modele-menaces.md`, `architecture-securite.md` |
| J3, 3B | `auditeur-securite` : plan de tests de sécurité, dérivé du niveau ASVS et du modèle de menaces | modèle de menaces, SFD, stratégie de test | `03-conception/securite/plan-tests-securite.md` |
| J4, 4B à 4n | `auditeur-securite` : contrôles automatisés sur chaque incrément, après les développeurs | code, dépendances, images | constats au registre |
| J5, 5A | `auditeur-securite` : tests complets et rapport ; `testeur-intrusion` : test d'intrusion sur l'environnement de recette | produit en recette, comptes de test par rôle, autorisation écrite | `05-validation/rapport-securite.md`, `rapport-test-intrusion.md` |
| J5, corrections | auteurs repris, puis `auditeur-securite` en contre-test | constats ouverts | constats clos avec preuve |
| J6, 6A | `architecte-securite` : plan de réponse à incident avec `responsable-support-formation` | délais de notification applicables | section du plan de support |

## Essaimage

- **Rapport de tests :** une instance d'`auditeur-securite` par famille de contrôles (authentification et sessions, contrôle d'accès, API, configuration et infrastructure) au-delà de vingt écrans ou de trente points d'accès d'API. Chacune reçoit le plan de tests complet et sa famille.
- **Test d'intrusion :** jamais d'essaim. Une seule instance par périmètre autorisé, pour tenir le registre des actions.

## Dépendances à respecter

L'analyse de risques précède le modèle de menaces ; le modèle précède le plan de tests. L'autorisation écrite précède tout test d'intrusion, sans exception. Les corrections précèdent le contre-test. Le test d'intrusion se lance sur une recette stable, après les tests de sécurité automatisés, sinon il redécouvre des défauts évidents.

## Revues croisées

| Livrable | Relecteurs |
|---|---|
| Analyse de risques | `delegue-protection-donnees`, `juriste-numerique` (régimes applicables) |
| Architecture de sécurité | `architecte-solution`, `ingenieur-devops` |
| Plan et rapport de tests | `concepteur-tests`, `auditeur-general` |
| Autorisation de test d'intrusion | `juriste-numerique` : à valider avant démarrage |

## Décisions à porter en réunion

| Décision | Type | Format |
|---|---|---|
| Niveau de vérification ASVS visé et régimes applicables | 1 | comité d'architecture |
| Recours à un prestataire qualifié plutôt qu'à l'agent | 1 | comité de cadrage ou go/no-go |
| Autorisation du test d'intrusion et de son périmètre | 1 | signature du propriétaire, consignée au registre des décisions |
| Acceptation d'un risque résiduel élevé ou critique | 1 | go/no-go |
| Choix d'une solution de marché ou libre pour une couche | 2 | panel |

## Sortie du pôle par jalon

- **J2 :** analyse de risques présente ; contrôles `SEC-` de jalon J2 traités.
- **J3 :** modèle de menaces, architecture de sécurité, plan de tests présents ; contrôles J3 traités.
- **J4 :** aucune vulnérabilité critique ou haute ouverte ; contrôles automatisés au vert.
- **J5 :** rapport de tests et rapport de test d'intrusion présents ; constats critiques et hauts contre-testés et clos.
- **J6 :** plan de réponse à incident, supervision et sauvegarde restaurée prêts.

## Variantes par mode

| Mode | Adaptation |
|---|---|
| `eclair` | `auditeur-securite` seul : analyse de risques courte, contrôles automatisés et liste `SEC-` ; pas de test d'intrusion par agent, recommandation d'un prestataire si enjeu fort |
| `standard` | comme décrit |
| `integral` | niveau ASVS 2 ou 3 selon le risque, essaim par famille, test d'intrusion confié de préférence à un prestataire qualifié, exercice de crise simulé |

## Outils extérieurs

Si un connecteur de gestion de vulnérabilités ou de CI est disponible, y verser les constats. Sinon les constats vivent dans `registre constats` et `registre anomalies`.
