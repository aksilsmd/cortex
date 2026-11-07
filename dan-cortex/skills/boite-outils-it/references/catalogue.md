# Catalogue IT-Tools utile à Dan-Cortex

Adresse : `http://127.0.0.1:3110/<outil>`. Les outils marqués « CLI » ont un équivalent natif dans `scripts/outils-it.mjs`.

| Outil (chemin) | CLI | Pôle | Quand s'en servir |
|---|---|---|---|
| hash-text | hash | DevOps, recette | empreinte d'un livrable, preuve d'intégrité |
| hmac-generator | hmac | Sécurité | contrôler la signature d'un webhook (paiement, transporteur) |
| token-generator | jeton | DevOps | secret de session ou de pseudonymisation **de test** |
| uuid-generator | uuid | Données | identifiants de jeux de données fictifs |
| base64-string-converter | base64 | Tous | lire une pièce encodée d'un journal ou d'un e-mail |
| url-encoder | url | Recette | construire une URL de test avec paramètres |
| jwt-parser | jwt | Sécurité | lire l'en-tête et la charge d'un jeton (signature non vérifiée) |
| otp-generator | totp | Sécurité, recette | code de double authentification d'un compte de test |
| password-strength-analyser | entropie | Sécurité | vérifier qu'une politique de mot de passe tient |
| qrcode-generator | qr | Recette, lancement | QR des liens de test ou du site |
| bcrypt | — | Sécurité | comparer un hachage bcrypt d'un système tiers |
| crontab-generator | — | DevOps | écrire une planification de sauvegarde |
| regex-tester | — | Développement | mettre au point une validation de champ |
| json-to-yaml-converter, yaml-to-json-converter, json-prettify | — | DevOps | configurations |
| http-status-codes, mime-types, user-agent-parser | — | Recette, sécurité | qualifier une anomalie réseau |
| ipv4-subnet-calculator, ipv4-range-expander | — | DevOps, sécurité | listes de proxys de confiance, pare-feu |
| chmod-calculator | — | DevOps | droits de fichiers sur le serveur |
| date-converter | — | Données | horodatages ISO, Unix |
| text-diff | — | Recette | comparer deux sorties |
| email-normalizer | — | Données | dédoublonnage d'adresses fictives |

Source : https://github.com/CorentinTh/it-tools (GPL-3.0), version construite 2024.10.22-7ca5933, SHA-256 eef276d675db6053bdc65cd8482a566785561c70eed5035a0e05b0e627b0989d.
