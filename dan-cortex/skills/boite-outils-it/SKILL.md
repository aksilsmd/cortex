---
name: boite-outils-it
description: "Boîte à outils IT de Dan-Cortex, bâtie sur IT-Tools (CorentinTh/it-tools, GPL-3.0) servi en local : empreintes et sommes de contrôle, jetons et secrets, UUID, Base64, encodage d'URL, lecture de JWT, codes TOTP de test, entropie d'un mot de passe, QR codes, et 90 outils de développeur dans le navigateur. À utiliser pour « génère un secret », « somme de contrôle », « QR code du lien », « décode ce JWT », « code TOTP de test », « it-tools »."
---

# Boîte à outils IT (IT-Tools en local)

Donne aux agents et à l'utilisateur les outils de développeur d'IT-Tools sans service en ligne : tout tourne en local, aucune donnée ne sort de la machine. Règle d'or : **un secret réel ne passe jamais par un outil en ligne ni dans un rapport ; on calcule en local et on n'écrit que le résultat utile (empreinte, verdict, fichier).**

## Installer et démarrer

1. `node ${CLAUDE_PLUGIN_ROOT}/skills/boite-outils-it/scripts/installer-it-tools.mjs <projet>/outils/it-tools`
   — télécharge la version construite officielle depuis GitHub, **vérifie l'empreinte SHA-256** (refus sinon), extrait, ajoute `serveur.cjs`, `demarrer-it-tools.cmd` et un LISEZMOI. Si github.com est bloqué, demander le zip à l'utilisateur et le déposer dans le dossier : l'empreinte est contrôlée de la même façon.
2. `node <projet>/outils/it-tools/serveur.cjs` → `http://127.0.0.1:3110/` (variable `IT_TOOLS_PORT`). Le serveur n'écoute que 127.0.0.1 et sa CSP interdit tout appel sortant : le module de mesure d'audience présent dans le code d'IT-Tools ne peut rien envoyer.
3. Contrôle : `node scripts/outils-it.mjs verifier` doit répondre `hotes_externes: []`. Sinon arrêter et rendre compte.

## Appeler un outil depuis un agent

`node ${CLAUDE_PLUGIN_ROOT}/skills/boite-outils-it/scripts/outils-it.mjs <commande>` (liste : `aide`). Lancer depuis le dossier du projet quand la commande utilise Playwright (`qr`, `capture`, `verifier`).

- **Calcul pur** (hash, hmac, jeton, uuid, base64, url, jwt, totp, entropie) : équivalents natifs Node des outils IT-Tools du même nom, sans dépendance, résultat reproductible. Préférer ces commandes dans les scripts et les preuves.
- **Résultat visuel** (qr, capture) : pilote l'interface IT-Tools locale. Le PNG d'un QR est contrôlable en le décodant (OpenCV `QRCodeDetector`) avant remise.
- **Autres outils** (90 au total : convertisseurs de dates, cron, regex, JSON/YAML/TOML, en-têtes HTTP, codes de statut, chmod, IPv4/sous-réseaux, user-agent, etc.) : les ouvrir dans l'interface ou en faire une capture avec `capture <outil>`. Catalogue et usage par pôle : `references/catalogue.md`.

## Règles

- **Secrets** : `entropie` et `hash` lisent plutôt un fichier (`--fichier`) que la ligne de commande, pour que le secret n'apparaisse pas dans l'historique ni dans les journaux. Ne jamais recopier un secret, un mot de passe ou une clé TOTP dans un rapport ; écrire l'empreinte ou le verdict.
- **Jetons générés** : `jeton` sert aux secrets de test ou de configuration ; en production, les secrets se génèrent sur la machine cible et restent dans son coffre.
- **JWT** : `jwt` décode sans vérifier la signature ; ne jamais en conclure qu'un jeton est valide.
- **TOTP** : réservé aux comptes de test ou jetables du projet (périmètre DEC-001 des tests de sécurité).
- **Licence** : IT-Tools est sous GPL-3.0. Il reste un **outil séparé** : ne pas copier son code dans le produit livré au client (sinon le produit hérite de la GPL). Conserver la mention de licence et le lien vers les sources dans le LISEZMOI installé.
- **Aucune publicité, aucun traceur** : ne pas lever la CSP du serveur local.

## Où s'en servir dans Dan-Cortex

| Pôle | Usage type |
|---|---|
| Usine logicielle / DevOps | SHA-256 des paquets livrés (fichier `SHA256SUMS.txt`), UUID, secrets de configuration de test, conversion JSON/YAML |
| Sécurité, test d'intrusion | codes TOTP des comptes de test, lecture d'un JWT, entropie des mots de passe imposés, HMAC de contrôle de webhooks |
| Recette | QR codes des liens de test remis au client, captures d'outils pour les PV |
| Lancement, support | QR code du site et des liens d'aide, vérification des empreintes du paquet chez le client |
