# Niveaux d'autonomie

## Synthèse

- Trois niveaux : `accompagne` (par défaut), `delegue`, `autonome`. Ils règlent quand le chef d'orchestre s'arrête
  pour te consulter, pas ce que le réseau a le droit de faire.
- En `autonome`, J0 est la seule conversation obligatoire : ensuite le réseau enchaîne tous les jalons du périmètre
  sans attendre, tranche lui-même et te remet un bilan.
- Ce qui a un effet hors de l'espace de travail ne part que s'il figure dans les **autorisations permanentes**
  écrites et approuvées à J0. Le reste attend, sans bloquer le travail.
- Six **limites dures** ne se délèguent à aucun niveau.
- L'autonomie s'appuie sur des réglages Claude Code ciblés et le bac à sable, jamais sur un contournement des
  permissions.

## Les trois niveaux

| | `accompagne` | `delegue` | `autonome` |
|---|---|---|---|
| Pause entre deux jalons | oui : compte rendu, puis attente de ton accord | non : compte rendu, puis enchaînement | non : une ligne d'avancement, puis enchaînement |
| Décisions de type 2 | prises par le réseau, tracées | prises par le réseau, tracées | prises par le réseau, tracées |
| Décisions de type 1 | soumises à toi | regroupées et soumises à la fin de chaque jalon | prises en réunion collégiale, au statut `provisoire`, confirmées par toi au bilan |
| Question qui surgit en cours de route | posée tout de suite | posée à la fin du jalon | jamais posée : hypothèse écrite dans la fiche projet, travail poursuivi |
| Effet extérieur (push, déploiement…) | demandé à chaque fois | demandé à chaque fois | exécuté s'il figure dans les autorisations permanentes, sinon mis en attente |
| Jalon bloqué | arrêt et compte rendu | arrêt et compte rendu | deux tours de correction, puis poursuite de tout ce qui ne dépend pas du blocage |

Le niveau se fixe à l'initialisation (`cortex.py init … --autonomie autonome`) ou plus tard
(`cortex.py etat --set autonomie=autonome`). Le niveau `autonome` ajoute l'étiquette `autonome` : les contrôles
`ROB-004` à `ROB-006` entrent alors dans la matrice.

## J0 en mode autonome

La qualification reste une vraie conversation, la seule. Dans la même série de questions, obtenir :

1. le périmètre, le mode et le niveau `autonome`, confirmés explicitement ;
2. les **autorisations permanentes** : pour chacune, l'effet, la cible exacte et la limite. Exemples :
   « push sur la branche `dev` de `github.com/<compte>/<dépôt>` », « déploiement sur l'environnement de recette
   `<url>` », « création de tickets dans le projet `<nom>` ». Une autorisation vague (« fais ce qu'il faut »)
   ne vaut rien : la reformuler et la faire confirmer ;
3. le plafond de tokens (`cortex.py etat --set plafond_tokens=<n>`) : en autonome, c'est le frein principal ;
4. l'accord pour installer les réglages recommandés par `robustesse-agents` (`assets/reglages-autonomes.json`),
   que l'utilisateur pose lui-même ou te demande de poser.

Écrire le tout dans la section « Niveau d'autonomie convenu » de `00-pilotage/fiche-projet.md`, puis lancer l'audit
des réglages. Sans ces réponses, rester en `accompagne`.

## Règles de conduite en mode autonome

1. **Enchaîner.** Après chaque `jalon franchir`, passer au jalon suivant dans le même tour. L'utilisateur reçoit
   une ligne : jalon franchi, livrables, décisions provisoires prises.
2. **Trancher sans attendre.** Une décision de type 1 passe par une réunion collégiale. Retenir l'option la plus
   facile à défaire quand deux options se valent, puis l'inscrire au registre avec `statut=provisoire`, son option
   de repli et son coût d'annulation. `cortex.py etat` liste les décisions provisoires.
3. **Supposer plutôt que demander.** Une information manquante devient une hypothèse numérotée dans la fiche
   projet, avec sa conséquence si elle est fausse.
4. **Agir dans le cadre écrit.** Un effet extérieur couvert par une autorisation permanente est exécuté puis
   journalisé au registre des actions. Un effet non couvert va au registre des actions avec `statut=ouverte` et
   la mention « en attente d'accord » ; le travail continue sur le reste.
5. **Réparer avant de s'arrêter.** Un jalon que le script refuse déclenche deux tours de correction par les auteurs.
   S'il reste bloqué, poursuivre les missions indépendantes, puis s'arrêter et rendre compte. Ne jamais forcer un
   jalon (`--force`) sans accord : forcer, c'est accepter un risque à la place de l'utilisateur.
6. **Tenir le budget.** À 80 % du plafond de tokens, passer en mode `eclair` pour la suite ; à 100 %, s'arrêter et
   rendre compte.
7. **Bilan final.** À la fin du périmètre, un seul compte rendu : livrables, décisions provisoires à confirmer ou
   annuler, hypothèses à valider, actions en attente d'accord, risques ouverts, tokens consommés.

## Limites dures

Aucune autorisation permanente ni aucun niveau d'autonomie ne couvre :

1. dépenser de l'argent ou engager l'utilisateur : achat, abonnement, contrat, signature ;
2. agir sur un système, un compte ou des données qui n'appartiennent pas au projet ;
3. un test de sécurité sans l'autorisation écrite du propriétaire de la cible ;
4. modifier les réglages de permissions de Claude Code ou contourner une protection de la plateforme ;
5. une suppression irréversible : données de production, réécriture de l'historique d'une branche partagée ;
6. manipuler un vrai secret hors de son coffre, ou l'écrire dans un livrable.

Chacune demande un accord explicite au moment de l'action, même en mode autonome.

## Réglages Claude Code

Moins de demandes de permission, c'est d'abord des réglages adaptés, pas une consigne dans l'invite. Le skill
`robustesse-agents` fournit `assets/reglages-autonomes.json` : mode `auto` (ou `acceptEdits` si ta version ne le
propose pas), bac à sable activé avec exécution automatique des commandes qui y tournent, recherche web autorisée,
lecture des fichiers de secrets et commandes dangereuses interdites. L'audit des réglages ne doit remonter aucun
constat `HIGH`. Le mode `bypassPermissions` reste à proscrire hors d'un conteneur jetable.
