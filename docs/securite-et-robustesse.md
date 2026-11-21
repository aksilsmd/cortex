# Sécurité et robustesse

Ce que Dan-Cortex s'interdit, ce qu'il vérifie, et ce que l'utilisateur doit savoir avant de lui confier un
projet. Pour signaler une faille du plugin lui-même : [`SECURITY.md`](../SECURITY.md).

## Sommaire

1. [Modèle de confiance](#modèle-de-confiance)
2. [Limites dures](#limites-dures)
3. [Injection d'instructions](#injection-dinstructions)
4. [Réglages de Claude Code et autonomie](#réglages-de-claude-code-et-autonomie)
5. [Confidentialité des traces](#confidentialité-des-traces)
6. [Tests de sécurité du projet](#tests-de-sécurité-du-projet)
7. [Contenus et scripts tiers](#contenus-et-scripts-tiers)
8. [Ce que Dan-Cortex ne garantit pas](#ce-que-dan-cortex-ne-garantit-pas)

## Modèle de confiance

```mermaid
flowchart LR
  subgraph Confiance["Fait foi"]
    U([Utilisateur])
    F[Fichiers du plugin]
  end
  subgraph Donnees["Données, jamais des ordres"]
    W[Pages web]
    G[Dépôts GitHub]
    O[Sorties d'outils]
    Dc[Documents fournis]
  end
  U -->|consignes, accords| C[Chef d'orchestre]
  F -->|méthode| C
  W & G & O & Dc -->|lus, cités, signalés| C
```

Une instruction trouvée dans une page, un avis, un fichier ou une sortie d'outil est **signalée dans le compte
rendu, jamais exécutée**. Cette règle figure dans la fiche de chaque agent et dans chaque ordre de mission qui
fait lire des sources extérieures.

## Limites dures

Six gestes ne se délèguent à aucun niveau d'autonomie et demandent toujours l'accord de l'utilisateur au moment
de l'action :

| # | Limite |
|---|---|
| 1 | dépenser de l'argent ou engager l'utilisateur (achat, contrat, abonnement) |
| 2 | toucher un système qui n'appartient pas au projet |
| 3 | tester la sécurité sans autorisation écrite du propriétaire |
| 4 | modifier les permissions de Claude Code |
| 5 | supprimer de façon irréversible |
| 6 | sortir un vrai secret (clé, mot de passe, jeton) |

En mode `autonome`, tout autre effet extérieur (push, publication, envoi) n'est permis que s'il figure dans les
**autorisations permanentes** écrites à J0, avec sa cible exacte et sa limite. Le mode autonome ne s'élargit
jamais en retirant une limite dure. Source :
[`autonomie.md`](../dan-cortex/skills/lancer-projet/references/autonomie.md).

## Injection d'instructions

Le pôle `robustesse-agents` (`/dan-cortex:robustesse-agents`) traite deux cibles :

- **les agents de la mission** : hygiène des ordres de mission, comptes rendus qui listent les instructions
  suspectes rencontrées ;
- **les fonctions d'IA du produit** (projets étiquetés `ia`) : modèle de menaces qui trace chaque point où un
  contenu non fiable atteint un modèle, corpus de scénarios, essais répétés.

Chaque scénario a un identifiant, une catégorie, une invite, un résultat attendu et un verdict `PASS`, `REVIEW`
ou `FAIL`. L'heuristique trie, l'humain tranche : un `REVIEW` se décide à la main, un `PASS` ne prouve pas la
sécurité. Seize contrôles `ROB-`, alignés sur l'OWASP Top 10 LLM 2025, ferment la couverture.

| Commande | Effet |
|---|---|
| `robustesse.py audit-config` | lecture seule des réglages ; code de sortie 2 si un constat `HIGH` |
| `robustesse.py scenarios --output <fichier.json>` | export du corpus, aucun appel de modèle |
| `robustesse.py evaluate --live --output-dir <dossier>` | appelle `claude -p` sans outils ; **accord explicite obligatoire** (consomme de l'usage) |

## Réglages de Claude Code et autonomie

L'autonomie passe par des **réglages ciblés**, jamais par un contournement des permissions : mode `auto`, bac à
sable, commandes dangereuses interdites. Le gabarit
[`reglages-autonomes.json`](../dan-cortex/skills/robustesse-agents/assets/reglages-autonomes.json) est proposé à
l'utilisateur, qui le pose lui-même ou donne son accord. L'audit ne modifie aucun réglage : il propose un écart
minimal. La CI du dépôt audite ce gabarit à chaque commit.

## Confidentialité des traces

`/dan-cortex:confidentialite-traces` masque secrets et données personnelles dans les sorties, journaux et
rapports, avec une conservation minimale. Le masquage est **explicite** (on voit qu'une valeur a été masquée) et
ne falsifie ni ne supprime en secret une trace d'audit. Les essais n'utilisent que des valeurs fictives.

## Tests de sécurité du projet

`/dan-cortex:securite-protection` couvre l'analyse de risques, les protections, les contrôles DevSecOps, les tests
de sécurité et le cadrage d'un test d'intrusion. Ces tests :

- ne visent que les environnements du projet, avec autorisation écrite de leur propriétaire ;
- restent défensifs et non destructifs ; le plugin ne contient aucune technique d'attaque ;
- ne remplacent pas un prestataire qualifié (PASSI ou équivalent) pour un enjeu fort : les agents ne délivrent
  aucune qualification.

## Contenus et scripts tiers

| Origine | Règle |
|---|---|
| Méthodes réécrites (forme A) | aucun texte copié ; section « Origine » et fiche de sources datée |
| Textes traduits (forme B) | licence permissive, `LICENSE.txt` et `NOTICE.md` dans le dossier, aucun script |
| 13 skills copiés d'Anthropic (exception du 12/11/2026) | copiés tels quels avec leurs scripts ; **ces scripts s'exécutent sur la machine de l'utilisateur** |
| Outils séparés (IT-Tools, Graphify, Twenty) | version figée, installation locale, aucun appel sortant non nécessaire, accord écrit avant installation |

Procédure complète (repérer, vérifier, réécrire, mesurer, retirer) :
[`renfort-externe.md`](../dan-cortex/skills/robustesse-agents/references/renfort-externe.md). Mentions de licence :
[`dan-cortex/NOTICE.md`](../dan-cortex/NOTICE.md).

## Ce que Dan-Cortex ne garantit pas

- Un résultat juridique, fiscal ou de sécurité certifiant : ce qui engage est marqué « à valider ».
- L'exactitude du droit et des versions d'outils après octobre 2026 : les points non confirmés sont marqués
  « à vérifier ».
- Le comportement d'un modèle : il n'est pas déterministe, les scénarios se rejouent et se mesurent en taux.
