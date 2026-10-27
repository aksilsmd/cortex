---
name: confidentialite-traces
description: Protège les données sensibles dans les sorties, journaux et artefacts des agents, avec masquage explicite et conservation minimale sans falsifier ni supprimer clandestinement les traces d'audit.
---

# Confidentialité des traces et des données sensibles

## Objectif

Réduire l'exposition accidentelle de secrets et de données personnelles dans les prompts, sorties d'agents, rapports, logs, captures, tickets et artefacts. Appliquer ces règles transversalement aux missions Dan-Cortex.

## Règles d'exécution

1. **Classer avant d'émettre.** Repérer les secrets (jetons, mots de passe, clés privées, cookies de session), identifiants personnels et données métier confidentielles avant de les copier dans une sortie, un journal ou un rapport.
2. **Masquer par défaut.** Remplacer les valeurs par des marqueurs stables tels que `[REDACTED_TOKEN]`, `[REDACTED_EMAIL]` ou `[REDACTED_SECRET]`. Ne jamais reproduire la valeur réelle dans le rapport de diagnostic.
3. **Ne pas collecter inutilement.** Ne lire que les champs nécessaires à la tâche. Préférer des exemples synthétiques aux données de production et limiter les extraits copiés.
4. **Respecter les autorisations.** Ne pas chercher à extraire des secrets sans besoin autorisé. Ne pas envoyer de données à un service externe sans autorisation et base légitime clairement établies.
5. **Réduire la rétention.** Ne conserver les données temporaires que pendant la durée nécessaire, conformément aux règles du projet. Avant toute suppression de logs existants, vérifier la politique de rétention et l'autorisation explicite.
6. **Séparer confidentialité et auditabilité.** Le masquage protège le contenu sensible ; il ne doit pas falsifier la chronologie, l'auteur, le résultat ou l'existence d'une action. Ne pas effacer, réécrire ou désactiver clandestinement les traces d'audit pour cacher une action.
7. **Tracer les changements de politique.** Tout changement de configuration de journalisation, rétention ou redaction doit être explicite, documenté et réversible. Conserver un journal de changement minimal qui ne contient pas les secrets eux-mêmes.
8. **Éviter les faux positifs destructifs.** Si une donnée est ambiguë, ne pas la supprimer automatiquement d'une source ; produire une copie masquée et signaler la décision.
9. **En cas d'exposition accidentelle.** Ne pas recopier le secret dans le rapport. Indiquer le type de secret, l'emplacement, l'étendue connue et les étapes de rotation/révocation recommandées. Ne pas prétendre qu'une rotation a eu lieu sans l'avoir réalisée.
10. **Vérifier.** Ajouter ou exécuter des tests qui confirment que les valeurs sensibles connues sont masquées dans les sorties ciblées, et que les événements d'audit nécessaires restent présents.

## Procédure de masquage

- Identifier les formats probables : `Authorization`, API keys, tokens JWT, clés privées PEM, mots de passe dans les URL/configurations, cookies, emails et numéros de téléphone si leur exposition n'est pas nécessaire.
- Masquer les valeurs, pas les noms des champs nécessaires au diagnostic.
- Réexécuter un scan sur l'artefact produit avant de le livrer.
- Documenter les limites du scan et les types de données couverts.

## Comportement autonome

- Appliquer automatiquement le masquage aux nouveaux rapports et journaux générés par la mission, lorsque cela ne casse pas le format attendu.
- Continuer les tâches indépendantes si une source contient une donnée sensible ; utiliser une copie masquée et signaler le blocage précis.
- Ne pas interrompre toute la mission pour un avertissement non bloquant ; isoler la zone sensible et poursuivre le reste.
- Demander une clarification uniquement si le traitement exige réellement de révéler, transférer ou supprimer une donnée sensible et que l'autorisation manque.

## Limites

Ce skill ne permet pas de dissimuler des actions non autorisées, d'altérer les journaux d'audit, de neutraliser les contrôles de sécurité ou de contourner des permissions. Il protège le contenu sensible tout en préservant une traçabilité honnête.
