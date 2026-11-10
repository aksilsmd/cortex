# Mode universel : faire tourner Dan-Cortex sur n'importe quelle IA

Dan-Cortex est une méthode avant d'être un plugin. Là où l'IA hôte n'a pas de sous-agents, de fichiers ou de
recherche, la méthode reste la même et s'adapte ainsi.

| Capacité absente | Adaptation |
|---|---|
| Sous-agents | Jouer les rôles l'un après l'autre, en annonçant « Équipe Marché : … », « Contradicteur : … ». Séparer réellement la production et la vérification : rédiger, puis relire comme un autre expert avec une liste de critères. |
| Fichiers | Écrire les documents dans la conversation (ou un canevas), une section par message, numérotées ; finir par la table des matières. Proposer à l'utilisateur de copier chaque section dans son propre document. |
| Mémoire entre conversations | Terminer chaque séance par un bloc « ÉTAT DU PROJET » de dix lignes (étape, décisions, points ouverts, prochaine action) que l'utilisateur recolle au début de la suivante. |
| Recherche web | Le dire. Marquer « à vérifier » ; donner la liste des recherches à faire ; accepter les sources collées par l'utilisateur. |
| Questions à choix | Réponses numérotées ; un chiffre suffit pour répondre. |
| Exécution de code | Poser les calculs en clair, ligne par ligne, et demander à l'utilisateur de les contrôler dans un tableur. |
| Scripts `cortex.py` | Tenir à la main, en tableaux : registre des décisions, des risques, des points ouverts, et l'avancement par étape. |

## Bloc d'état (à produire à chaque fin de séance)
```
ÉTAT DU PROJET — <nom> — <date>
Étape en cours : n/9 — <intitulé>
Besoin validé : oui/non — <une phrase>
Décisions prises : …
Hypothèses à confirmer : …
Points ouverts : …
Documents produits : …
Prochaine action : …
```

## Ce qui ne change jamais
Saluer et demander le besoin brut ; reformuler et faire valider ; explorer avant d'interroger ; proposer avant
de questionner ; réponses suggérées ; une validation à chaque porte ; sources ou « non vérifié » ; l'utilisateur
décide.
