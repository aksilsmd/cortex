# Exigences non fonctionnelles

Une exigence non fonctionnelle (`EXNF-`) décrit une qualité que le produit doit atteindre, pas une fonction. Elle se rattache à une caractéristique d'ISO/IEC 25010:2023, se chiffre, et se vérifie par une méthode nommée. Sans métrique et sans méthode, elle n'est qu'un souhait.

## Sommaire
1. Méthode
2. Catalogue par caractéristique
3. Chiffrer : les quatre questions
4. Gabarit d'une ligne
5. Pièges fréquents
6. Contrôles avant de rendre
7. Sources

## 1. Méthode

1. Parcourir les neuf caractéristiques du catalogue pour chaque projet : une caractéristique écartée l'est avec un motif.
2. Pour chacune, interroger le contexte : volumétrie, pics, population, pays, réglementation, criticité métier.
3. Fixer la **valeur cible** et la **valeur plancher** (en dessous : refus de recette). Chiffrer avec le `controleur-financier` les seuils qui coûtent cher (disponibilité, reprise, charge) : chaque « neuf » de disponibilité se paie.
4. Nommer la **méthode de vérification** et l'agent qui la jouera (test de charge, audit, revue, inspection, démonstration).
5. Écrire la ligne `EXNF-` au gabarit, critère d'acceptation en fin de ligne.

Les noms des caractéristiques et sous-caractéristiques ci-dessous sont à vérifier sur le texte de la norme avant toute clause contractuelle (la norme elle-même n'a pas été relue à la source).

## 2. Catalogue par caractéristique

| Caractéristique | Sous-caractéristiques utiles | Comment chiffrer | Comment vérifier |
|---|---|---|---|
| Functional suitability (adéquation fonctionnelle) | complétude, exactitude, pertinence | taux de couverture des `EX-` Must ; taux d'erreur de calcul toléré (souvent zéro) ; jeux d'exemples de référence | cahier de recette ; comparaison à des résultats attendus calculés indépendamment |
| Performance efficiency (efficacité de performance) | comportement temporel, utilisation des ressources, capacité | temps au 95e centile par opération clé ; débit (opérations par seconde) ; capacité (utilisateurs simultanés, volume de données) ; consommation maximale CPU et mémoire sous charge | test de charge et d'endurance avec modèle de charge écrit ; mesure sur parcours réels. Web : Core Web Vitals (LCP, INP, CLS), seuils « bon » publiés par Google, à vérifier à la date de rédaction |
| Compatibility (compatibilité) | coexistence, interopérabilité | liste fermée de navigateurs et versions, systèmes mobiles, formats d'échange ; versions d'API prises en charge | matrice de tests ; tests de contrat sur chaque interface |
| Interaction capability (capacité d'interaction, ex-utilisabilité) | apprentissage, utilisation, protection contre les erreurs, inclusivité, assistance | taux de réussite d'une tâche sans aide, temps moyen par tâche, nombre de clics maximal ; conformité WCAG 2.2 niveau AA et RGAA (version en vigueur à vérifier) | test utilisateur sur 5 à 8 personnes par profil ; audit d'accessibilité manuel + outil |
| Reliability (fiabilité) | disponibilité, tolérance aux pannes, récupérabilité | disponibilité mensuelle (99,9 % = 43 minutes d'arrêt par mois de 30 jours) ; fenêtres de maintenance exclues ou non ; RPO et RTO ; durée de dégradation tolérée | supervision, test de bascule, test de restauration chronométré ; en marché public, VSR : 30 jours, indisponibilité cumulée ≤ 2 % (CCAG-TIC 2021, art. 32.4) |
| Security (sécurité) | confidentialité, intégrité, non-répudiation, imputabilité, authenticité, résistance | exigence par risque de l'analyse (classification des données, chiffrement au repos et en transit, durée de session, politique de mot de passe, journalisation conservée N mois) ; référentiel de vérification visé (OWASP ASVS, niveau à choisir) | revue d'architecture, audit, test d'intrusion autorisé par écrit ; seuil : zéro vulnérabilité critique ou haute ouverte à la recette |
| Maintainability (maintenabilité) | modularité, analysabilité, modifiabilité, testabilité | couverture de tests minimale, complexité maximale, dette mesurée, délai de correction par gravité (délai de prise en compte et de résolution) | outils d'analyse statique, seuils de qualité, revue de code |
| Flexibility (flexibilité, ex-portabilité) | adaptabilité, scalabilité, installabilité, remplaçabilité | croissance supportée sans refonte (×N utilisateurs), temps d'installation d'un environnement, réversibilité (export complet des données en format ouvert sous N jours) | test de montée en charge, répétition de déploiement, essai d'export |
| Safety (sûreté) | contraintes opérationnelles, avertissement des dangers, intégration sûre | seulement si le produit peut causer un dommage physique ou financier grave (dispositif connecté, santé, paiement) : situations dangereuses recensées, comportement sûr par défaut | analyse de risques dédiée, revue par un spécialiste du domaine |

## 3. Chiffrer : les quatre questions

| Question | Pourquoi |
|---|---|
| Sous quelle charge ? | « 800 ms » sans charge ni jeu de données ne veut rien dire |
| Sur quel percentile ? | la moyenne cache les lenteurs ; fixer le 95e ou le 99e |
| Mesuré où et comment ? | environnement de recette, production, ou outil de mesure réel |
| Quelle conséquence en dessous du seuil ? | recette refusée, pénalité, réfaction : cela relie l'exigence au contrat (clause à valider par le juriste) |

Valeurs de départ en l'absence de donnée : prendre le benchmark de J1 ou l'existant mesuré, puis « hypothèse à confirmer ». Ne jamais recopier un chiffre d'un autre projet sans le dire.

## 4. Gabarit d'une ligne

````markdown
| ID | Caractéristique ISO/IEC 25010:2023 | Exigence | Source | Priorité | Métrique, seuil, conditions et méthode | Critère d'acceptation |
|---|---|---|---|---|---|---|
| EXNF-012 | Reliability, disponibilité | Le service doit être disponible 24 h sur 24 hors maintenance planifiée | contrat client A | Must | disponibilité mensuelle ≥ 99,9 % ; maintenance planifiée exclue si annoncée 5 jours avant ; sonde externe toutes les minutes | Sur 30 jours d'observation, l'indisponibilité cumulée mesurée par la sonde reste inférieure à 43 minutes |
````

Le `cortex.py tracabilite verifier` signale en **alerte** une `EXNF-` sans cas de test : le `concepteur-tests` doit la citer dans une ligne `CT-`.

## 5. Pièges fréquents

- Seuil de disponibilité choisi sans chiffrer l'architecture qu'il impose (redondance, astreinte).
- Exigence de sécurité réduite à « conforme aux bonnes pratiques » : la lier à une exigence de l'analyse de risques et à un référentiel.
- Accessibilité reportée « à la fin » ; la déclarer dès le cahier des charges avec son niveau.
- Performance mesurée sur l'ordinateur du développeur.
- RPO et RTO oubliés alors que la restauration est la seule preuve de sauvegarde.
- Confondre caractéristique de qualité (EXNF) et contrainte de projet (budget, délai, hébergement imposé) : les contraintes ont leur tableau.
- Utiliser la version 2011 de la norme (retirée) : les noms ont changé en 2023.

## 6. Contrôles avant de rendre

- Les neuf caractéristiques sont traitées ou écartées avec motif.
- Chaque ligne porte métrique, seuil, conditions de mesure, méthode et critère d'acceptation.
- Les seuils coûteux sont chiffrés ou marqués « décision de comité ».
- Les exigences de sécurité renvoient à l'analyse de risques ; celles de données personnelles sont « à valider ».
- Aucun adjectif sans valeur.

## Sources

- ISO/IEC 25010:2023, publiée le 15/11/2023, remplace la version 2011 (retirée).
- CCAG-TIC 2021, art. 32.3 et 32.4 (VSR après VA positive ; 30 jours ; 2 %).
- WCAG 2.2 (W3C) ; RGAA : version en vigueur à vérifier.
- OWASP ASVS : version à vérifier avant usage.
- Core Web Vitals (web.dev) : seuils à vérifier à la date de rédaction.
