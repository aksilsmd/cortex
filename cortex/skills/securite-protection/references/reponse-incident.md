# Plan de réponse à incident

Préparer avant le lancement ce qu'on fera le jour d'une intrusion, d'un logiciel malveillant ou d'une fuite : qui décide, quoi isoler, qui prévenir et dans quel délai. Le plan vit dans une section dédiée de `06-lancement/plan-support.md`.

## Sommaire
- Cadre et phases
- Rôles
- Qualification et horloge de notification
- Délais par régime
- Communication
- Exercices
- Gabarit du plan
- Pièges et contrôles
- Sources

## Cadre et phases

Suivre NIST SP 800-61r3 (avril 2025, qui remplace la r2) : la réponse à incident s'intègre à la gestion des risques et aux six fonctions du CSF 2.0 (gouverner, identifier, protéger, détecter, répondre, rétablir). Phases utiles pour le plan : préparer ; détecter et qualifier ; contenir ; éradiquer et rétablir ; retour d'expérience. Le détail des phases de la r3 est à relire dans la norme (à vérifier).

## Rôles

| Rôle | Mission | Suppléant |
|---|---|---|
| Responsable de crise | décide, arbitre, rend compte à la direction | obligatoire |
| Responsable technique | contient, éradique, rétablit | obligatoire |
| Responsable de la communication | messages internes, clients, presse | obligatoire |
| Référent juridique et données personnelles | qualifie les obligations, rédige les notifications | obligatoire |
| Scribe | tient le journal horodaté des décisions | recommandé |
| Contact du prestataire de réponse | intervient sur appel | contrat signé avant l'incident |

Pour un petit projet, un binôme technique et décisionnel et un contact juridique suffisent ; l'essentiel est que les noms et numéros soient écrits et joignables hors du système touché.

## Qualification et horloge de notification

1. **Fixer T0** : l'instant où l'organisation prend connaissance de l'incident. Un registre unique d'incident le consigne ; il déclenche tous les compteurs.
2. **Qualifier dans l'heure** : incident de sécurité, violation de données personnelles, incident majeur ou significatif au sens d'un régime applicable.
3. **Décider qui notifie quoi** avec le référent juridique ; chaque notification est tracée.

## Délais par régime

État : octobre 2026. Les textes n'ont pas tous été relus à la source : « à valider » par le juriste.

| Régime | Délais | Autorité |
|---|---|---|
| RGPD, violation de données personnelles | 72 h après connaissance, si risque pour les personnes (article 33, à vérifier) ; un projet européen évoque 96 h, ce n'est qu'une proposition | CNIL en France |
| NIS2 | alerte précoce 24 h, notification 72 h, rapport final 1 mois après | ANSSI en France ; la loi française n'est pas encore adoptée au 11 octobre 2026 |
| DORA, incident majeur | initiale 4 h après classification « majeur » et au plus tard 24 h après connaissance ; intermédiaire 72 h après l'initiale ; final 1 mois après le dernier intermédiaire | autorité financière compétente |
| Cyber Resilience Act, depuis le 11 septembre 2026 | alerte 24 h, notification 72 h, rapport final 14 jours après correctif (vulnérabilité exploitée) ou 1 mois (incident grave) | plateforme de l'ENISA |

Une proposition de guichet unique (Digital Omnibus) n'est pas en vigueur : ne pas bâtir le plan sur elle. Les délais se cumulent : un même incident peut déclencher plusieurs compteurs.

## Communication

- **Interne :** un canal hors du SI touché (téléphone, messagerie séparée) ; message court, factuel, sans spéculation.
- **Clients et utilisateurs :** informer sans délai injustifié quand leurs données sont touchées, avec ce qui s'est passé, ce qui est concerné, ce qu'ils doivent faire. Texte validé par le juridique.
- **Autorités :** par le référent juridique seulement.
- **Presse :** un seul porte-parole.
- **Éléments préparés à l'avance :** modèles de messages, liste des clients et contacts, coordonnées des autorités.

Ne pas payer de rançon ni négocier sans décision de la direction et conseil juridique.

## Exercices

- Exercice de crise annuel avec la direction, un scénario écrit à l'avance, retour d'expérience tracé.
- Test trimestriel d'une alerte de bout en bout.
- Test de restauration d'une sauvegarde au moins deux fois par an.
- Les canaux de secours sont testés pendant l'exercice.

## Gabarit du plan

```markdown
## Plan de réponse à incident

### Synthèse
(rôles nommés, régimes applicables, délais, date du dernier exercice, points à décider)

### Rôles et contacts
| Rôle | Titulaire | Suppléant | Joignable par |
|---|---|---|---|
### Qualification
(définition de T0, arbre de décision, gravités)
### Délais de notification
| Régime | Applicable | Déclencheur | Délai | Qui notifie | Modèle |
|---|---|---|---|---|---|
### Fiches réflexes
(compte compromis, logiciel malveillant, fuite de données, déni de service, secret exposé, fournisseur compromis)
### Communication
### Prestataire de réponse (contrat, contact)
### Exercices et retour d'expérience
```

Chaque fiche réflexe tient en une page : détecter, contenir, préserver les preuves, rétablir, notifier.

## Pièges

- Horloge mal initialisée : T0 flou, délais cumulés ignorés.
- Prestataire de réponse choisi pendant la crise.
- Communication sur le système compromis.
- Sauvegardes accessibles avec les identifiants compromis.
- Plan jamais exercé.
- Attendre la loi NIS2 pour agir alors que les clients l'exigent déjà.

## Contrôles avant de rendre

- Chaque rôle a un titulaire, un suppléant et un moyen de joindre hors SI.
- Le tableau des délais correspond aux régimes qualifiés (`obligations-cyber.md`).
- Un exercice est planifié avec une date.
- Un juriste valide les modèles de notification.

## Sources

- NIST SP 800-61r3 (3 avril 2025) : https://nist.gov/news-events/news/2025/04/nist-revises-sp-800-61-incident-response-recommendations-and-considerations
- ESAs, JC 2024-33, rapport final sur la notification des incidents : https://www.esma.europa.eu/sites/default/files/2024-07/JC_2024-33_-_Final_report_on_the_draft_RTS_and_ITS_on_incident_reporting.pdf
- Commission européenne, CRA, notification : https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- ANSSI, MesServicesCyber, NIS2 : https://messervices.cyber.gouv.fr/nis2
- ANSSI, PRIS v3.0 (prestataires de réponse) : https://cyber.gouv.fr/actualites/lanssi-met-%C3%A0-jour-les-referentiels-passi-version-22-et-pris-version-30/
- RGPD article 33 : texte à relire (à vérifier)
