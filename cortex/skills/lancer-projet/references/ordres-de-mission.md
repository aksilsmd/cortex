# Ordres de mission et comptes rendus

Un agent démarre sans rien savoir du projet : son ordre de mission est tout ce qu'il a. Un ordre flou produit un
travail flou et des lectures inutiles ; un ordre précis est le premier levier de qualité et de sobriété.

## Format de l'ordre de mission

Écrire l'ordre directement dans le prompt de lancement, dans cet ordre :

```
ORDRE DE MISSION OM-<jalon>-<n>
PROJET : <nom> — dossier : <chemin absolu du dossier projet>
MISSION : <le résultat attendu, en une à trois phrases>
À LIRE D'ABORD : <chemins de fichiers, avec la section utile si le fichier est long>
RÉFÉRENCES MÉTIER : <fichiers de référence du pôle à consulter, s'il y en a au-delà du skill préchargé>
OUTILS ET SKILLS : <outils du métier à privilégier pour cette mission ; ce que le noyau fera avec un skill ou un connecteur extérieur>
LIVRABLE : <chemin du fichier à écrire> ; gabarit : <chemin du gabarit, s'il existe>
PÉRIMÈTRE : <ce qui est inclus> — HORS PÉRIMÈTRE : <ce qui ne l'est pas, et qui le traite>
CRITÈRES D'ACCEPTATION : <trois à six critères vérifiables>
CONTRÔLES DE COUVERTURE À TRAITER : <identifiants, par exemple SEC-001, SEC-004>
BUDGET : <au plus N recherches web ou N appels d'outils> ; livrable de <N> mots au plus
```

Règles d'écriture :

- **Dire quel outil sert à quoi.** Les skills et les outils de chaque agent sont dans
  `outils-par-agent.md`. La rubrique « Outils et skills » précise ceux qui comptent pour la mission (recherche
  web bornée, script de contrôle, `essais.py`…) et ce que tu prendras toi-même en charge avec un skill ou un
  connecteur de la session, selon `routage-skills-outils.md`.
- **Un livrable principal par mission.** Si la mission produit quatre documents sans lien, ce sont quatre missions.
- **La fiche projet d'abord.** `00-pilotage/fiche-projet.md` est la constitution du projet : but, cible,
  non-objectifs, décisions structurantes en vigueur. Elle ouvre la rubrique « À lire d'abord » de chaque ordre,
  et tu la tiens à jour à chaque jalon.
- **Les entrées sont des chemins, pas des résumés.** Ne recopie pas le contenu des documents amont dans l'ordre :
  donne le chemin et la section. La seule exception est une décision récente qui n'est pas encore écrite.
- **Le hors-périmètre évite les doublons.** Deux agents de la même vague ne doivent jamais écrire le même fichier.
- **Le budget protège la session.** Valeurs usuelles : collecte 8 à 12 recherches ; analyse 15 à 25 appels
  d'outils ; rédaction d'une spécification 20 à 30 ; lot de code 60 à 100.
- **Les contrôles de couverture** viennent de `cortex.py couverture liste --domaine <XXX> --jalon <Jn> --statut a-faire --court`.

## Exemple

```
ORDRE DE MISSION OM-J1-02
PROJET : Agenda Véto — dossier : /travail/agenda-veto
MISSION : Démonter les cinq offres concurrentes listées et produire le benchmark concurrentiel :
matrice fonctionnelle, prix, positionnements, forces, faiblesses, angles laissés libres.
À LIRE D'ABORD : 00-pilotage/fiche-projet.md (sections Synthèse et Ce que l'on sait)
LIVRABLE : 01-decouverte/benchmark-concurrentiel.md ; fiches par concurrent dans 01-decouverte/sources/concurrents/
PÉRIMÈTRE : les cinq concurrents A à E listés dans la fiche projet, dont les logiciels de gestion de clinique avec module agenda
HORS PÉRIMÈTRE : taille du marché (analyste-marche), avis clients détaillés (analyste-voix-client)
CRITÈRES D'ACCEPTATION : chaque prix et chaque fonction cités avec l'URL source et la date ; matrice d'au moins
20 fonctions ; trois angles de différenciation argumentés ; ce qui n'a pas pu être vérifié est listé
CONTRÔLES DE COUVERTURE À TRAITER : MAR-004, MAR-005, MAR-006
BUDGET : au plus 20 recherches web ; livrable de 1 800 mots au plus, hors matrice
```

## Format du compte rendu

Chaque agent termine par ce compte rendu, de 150 mots au plus. Il figure dans la fiche de chaque agent.

```
STATUT : terminé | partiel | bloqué
LIVRABLES : chemins des fichiers écrits
ESSENTIEL : 3 à 5 constats ou choix clés
À ARBITRER : décisions qui n'appartiennent pas à l'agent
RISQUES : alertes
COUVERTURE : ID → fait | non-applicable (motif)
RENFORTS DEMANDÉS : sous-missions utiles, ou « aucun »
CONFIANCE : haute | moyenne | faible, et ce qu'il reste à vérifier
```

## Ce que tu fais d'un compte rendu

1. `STATUT : partiel` ou `bloqué` : reprendre le même agent avec une consigne ciblée, ou réattribuer.
2. `À ARBITRER` : décision de type 2, trancher et l'inscrire au registre ; décision de type 1, la porter en réunion.
3. `RISQUES` : inscrire au registre des risques ce qui est sérieux.
4. `COUVERTURE` : après la revue croisée, appliquer en une seule commande Bash regroupée
   (`cortex.py couverture maj <ID,ID> --nouveau fait --preuve <chemin>`).
5. `RENFORTS DEMANDÉS` : les lancer dans la vague suivante si le gain justifie le coût.
6. `CONFIANCE : faible` : faire vérifier par un `verificateur` ou un second expert avant d'en dépendre.

## Essaimage

Pour répartir une collecte ou un travail divisible :

1. l'expert, ou toi, liste les parts : un concurrent, une source d'avis, un module, un lot ;
2. tu lances une instance par part dans la même vague, avec le même gabarit de fiche pour toutes ;
3. chaque instance écrit sa fiche dans `sources/` ou dans le dossier du module ;
4. l'expert est lancé, ou repris, pour synthétiser à partir des fiches, sans refaire la collecte.

Borne : au plus 8 instances par essaim en mode `standard`, 16 en mode `integral`.

## Orchestration déléguée

Ordre de mission d'un `orchestrateur-de-pole` : lui donner le chemin du fichier `orchestration.md` de son pôle, le
jalon, le mode, la fiche projet et la liste des contrôles de couverture du domaine. Il renvoie un plan de
délégation : la liste des ordres de mission prêts à lancer, au format ci-dessus, avec pour chacun le type d'agent
et les dépendances. Tu lances tous les ordres sans dépendance dans la même vague. À la fin, tu reprends
l'orchestrateur pour la consolidation du pôle : cohérence entre livrables, synthèse de pôle, points à arbitrer.

Là où l'imbrication des agents est permise, l'orchestrateur lance lui-même ses agents et te rend directement la
consolidation.
