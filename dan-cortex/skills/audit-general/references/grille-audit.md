# Grille d'audit à 360°

Pour chaque domaine : les questions qui décident, la preuve à exiger, le signal d'alerte typique. La matrice de
couverture donne le détail des contrôles ; cette grille donne le regard d'ensemble. Ne traiter que les domaines
du périmètre de l'audit, mais ne jamais sauter Sécurité, Données personnelles, Juridique et pénal.

## Sommaire
Gouvernance · Marché et stratégie · Besoin et spécifications · Design, parcours et interactions · Architecture
et normes · Réalisation · Tests et recette · Sécurité et protection · Données personnelles · Juridique et pénal ·
Finance · Marketing et commercial · Social, culturel et éthique · Politique et réglementaire · Lancement et
exploitation · Cohérence transversale

## Gouvernance

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Qui décide, et l'a-t-il fait par écrit ? | registre des décisions, PV | décisions de type 1 jamais validées |
| Les risques majeurs ont-ils un propriétaire et une parade ? | registre des risques | risques sans propriétaire, scores jamais revus |
| Le planning tient-il compte des dépendances et d'une marge ? | planning | chemin critique sans marge, dates sans charge |
| Les jalons ont-ils été franchis ou forcés ? | `cortex.json`, tableau de bord | jalons forcés sans motif |

## Marché et stratégie

| Question | Preuve | Signal d'alerte |
|---|---|---|
| La douleur client est-elle prouvée par des sources datées ? | voix du client, fiches de sources | verbatims sans URL, avis inventés ou paraphrasés sans source |
| Les concurrents réels sont-ils tous là, y compris les substituts ? | benchmark | absence du leader ou du « ne rien faire » |
| La taille de marché est-elle calculée de deux façons ? | étude de marché | un seul chiffre repris d'un rapport |
| Le positionnement découle-t-il des analyses ? | note d'opportunité | positionnement sans lien avec les manques relevés |

## Besoin et spécifications

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Chaque exigence est-elle vérifiable et priorisée ? | cahier des charges | « ergonomique », « rapide », « sécurisé » sans mesure |
| La chaîne exigence, fonction, règle, cas de test est-elle complète ? | `tracabilite verifier` | exigences orphelines, identifiants fantômes |
| Les cas d'exception sont-ils spécifiés autant que le cas nominal ? | SFD | règles sans cas d'erreur |
| Les exigences non fonctionnelles sont-elles chiffrées ? | cahier des charges | performance, disponibilité, accessibilité sans seuil |

## Design, parcours et interactions

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Chaque élément interactif a-t-il une réaction et une destination ? | `interactions verifier` | culs-de-sac, écrans orphelins |
| Les états vide, chargement, erreur existent-ils pour chaque écran de données ? | inventaire des écrans | alertes d'états du script ignorées |
| Chaque fonctionnalité a-t-elle son workflow, exceptions comprises ? | workflows | workflows réduits au chemin heureux |
| Les maquettes respectent-elles l'accessibilité et la marque ? | note de revue accessibilité | contrastes non mesurés |

## Architecture et normes

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le choix du langage et de la pile est-il justifié contre une alternative ? | décisions d'architecture | décision sans option écartée |
| L'architecture répond-elle aux exigences non fonctionnelles chiffrées ? | dossier d'architecture | aucune correspondance exigence par exigence |
| Les normes sont-elles vérifiées par outil ? | configuration des contrôles, journal | normes déclaratives seulement |
| Les dépendances sont-elles saines et leurs licences compatibles ? | `dependances.md` | licences non relevées, paquets abandonnés |

## Réalisation

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Chaque lot livré correspond-il à son contrat d'interface ? | `lots.md`, revues | écarts non tracés |
| Les revues de code ont-elles eu lieu et leurs remarques été traitées ? | `04-realisation/revues/` | lots sans revue |
| Le dépôt contient-il des secrets ou du code mort ? | rapport de sécurité | clés en clair |

## Tests et recette

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Les tests passent-ils vraiment ? | rejouer une suite avec `essais.py` | tests désactivés, assertions vides |
| Chaque règle de gestion et chaque workflow ont-ils un cas de test ? | `tracabilite verifier` | couverture déclarée sans lien |
| La recette a-t-elle été menée sur un environnement représentatif ? | PV de recette | recette sur poste de développement |
| Les anomalies bloquantes sont-elles closes et vérifiées ? | registre des anomalies | « corrigée » sans « vérifiée » |

## Sécurité et protection

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le modèle de menaces couvre-t-il chaque flux de données sensible ? | modèle de menaces | modèle générique non relié à l'architecture |
| Authentification, autorisations et sessions sont-elles testées, y compris l'accès aux données d'autrui ? | rapport de sécurité | tests d'autorisation absents |
| Les protections périmétriques et la supervision sont-elles en place ? | infrastructure, architecture de sécurité | pare-feu applicatif, sauvegardes ou journaux non configurés |
| Le test d'intrusion était-il autorisé par écrit, sur un périmètre défini ? | rapport, autorisation | périmètre flou, cible tierce |
| Les vulnérabilités critiques et hautes sont-elles corrigées et recontrôlées ? | rapport, contre-test | corrections sans contre-test |
| Un plan de réponse à incident existe-t-il, avec les délais de notification ? | architecture de sécurité | aucun responsable désigné |
| Les réglages des agents de la mission ont-ils été audités, et les constats HIGH tranchés par l'utilisateur ? | audit des réglages des agents | mode de permission contourné ou règle `Bash(*)` sans décision écrite |
| Pour une fonction d'IA, l'injection d'instructions et les actions de l'agent sont-elles testées par des scénarios répétés ? | rapport de robustesse des agents | essai unique, verdict « sûr » fondé sur la seule heuristique |

## Données personnelles

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Chaque traitement a-t-il une finalité, une base légale, une durée ? | registre des traitements | « consentement » partout par défaut |
| Une analyse d'impact était-elle requise, et a-t-elle été faite ? | cartographie, analyse d'impact | données sensibles ou suivi à grande échelle sans analyse |
| Les sous-traitants et transferts hors Union sont-ils encadrés ? | contrats, registre | outils américains sans garantie de transfert |
| Le bandeau de consentement est-il conforme et le marquage le respecte-t-il ? | politique cookies, plan de marquage | traceurs déposés avant consentement |

## Juridique et pénal

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Les mentions et conditions correspondent-elles à l'offre réelle ? | documents juridiques, revue croisée | modèles génériques non adaptés |
| Marque, nom de domaine et droits sur le code et les contenus sont-ils sécurisés ? | propriété intellectuelle | recherche d'antériorité absente, licences non relevées |
| Une pratique du projet tombe-t-elle sous un texte pénal ? | conformité réglementaire | collecte déloyale, faux avis, allégations trompeuses, accès à un système tiers |
| Les obligations propres au secteur sont-elles identifiées ? | prédiagnostic | activité réglementée non reconnue |
| Ce qui exige un avocat est-il signalé ? | mentions « à valider » | aucun point « à valider » dans tout le dossier |

## Finance

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le budget couvre-t-il construction et exploitation, avec une réserve ? | budget | pas de coûts récurrents, pas de marge pour aléas |
| Les hypothèses de revenu sont-elles sourcées et testées en scénario bas ? | justification économique | un seul scénario |
| Un chiffre recalculé au hasard est-il juste ? | recalcul par l'auditeur | totaux faux |

## Marketing et commercial

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le plan vise-t-il la cible prouvée par l'étude ? | plan marketing | canaux choisis par habitude |
| Les promesses sont-elles tenues par le produit et licites ? | revue croisée juriste | allégations non vérifiables |
| La mesure est-elle prête le jour du lancement ? | plan de marquage | indicateurs non définis |
| Le support et la vente savent-ils quoi répondre ? | plan de support, plan commercial | pas de réponse prévue aux objections connues |

## Social, culturel et éthique

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le produit est-il adapté aux langues, usages et moyens de paiement de chaque marché ? | contenu et localisation | traduction seule |
| Des interfaces trompeuses sont-elles utilisées ? | matrice d'interactions | désabonnement plus dur que l'abonnement |
| Les publics fragiles (mineurs, personnes en situation de handicap) sont-ils pris en compte ? | accessibilité, conformité | « non applicable » sans motif |
| L'empreinte environnementale a-t-elle été considérée ? | dossier d'architecture | aucune mention |

## Politique et réglementaire

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Des sanctions, restrictions d'export ou règles de localisation touchent-elles un marché visé ? | analyse de contexte | pays visés sans vérification |
| Une réglementation à venir change-t-elle le projet dans les douze mois ? | conformité réglementaire | aucune veille datée |
| L'hébergement respecte-t-il les exigences de souveraineté du client ? | infrastructure | hébergeur choisi avant l'analyse |

## Lancement et exploitation

| Question | Preuve | Signal d'alerte |
|---|---|---|
| Le retour arrière a-t-il été répété ? | plan de bascule | « non testé » |
| Sauvegarde et restauration ont-elles été essayées ? | journal de l'essai | sauvegarde jamais restaurée |
| Supervision, alertes et astreinte sont-elles prêtes ? | infrastructure, plan de support | personne n'est alerté |
| Qui fait quoi le jour J et les jours suivants ? | plan de lancement | pas de noms |

## Cohérence transversale

Vérifier ces accords deux à deux ; chaque désaccord est un constat.

- périmètre du cahier des charges ↔ budget ↔ planning
- exigences non fonctionnelles ↔ architecture ↔ infrastructure ↔ coût d'hébergement
- traitements réels du code ↔ registre des traitements ↔ politique de confidentialité
- offre et prix du plan marketing ↔ conditions générales ↔ paramétrage du paiement
- matrice d'interactions ↔ SFD ↔ cahier de recette
- modèle de menaces ↔ tests de sécurité réalisés
- pays visés ↔ langues ↔ conformité ↔ fiscalité
