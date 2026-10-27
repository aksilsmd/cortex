# Plan de lancement marketing

Cette référence donne le calendrier de J-90 à J+90, la checklist marketing de lancement et le gabarit de `plan-communication.md`. J0 est le jour de disponibilité générale ; le plan de bascule technique appartient au pôle Lancement et exploitation.

## Sommaire
1. Principes de calendrier
2. Calendrier J-90 à J+90
3. Product Hunt
4. Checklist marketing de lancement
5. Gabarit de `plan-communication.md`
6. Pièges et contrôles

## 1. Principes de calendrier

- Préparer au moins trois mois avant : communauté, liste d'attente, comptes.
- Le jour J concentre une audience déjà réchauffée ; il ne la crée pas.
- Chaque palier a un seuil de passage chiffré (voir `strategie-mise-sur-le-marche.md`). Le calendrier recule si le seuil n'est pas atteint.
- Aucune publication ni aucun envoi n'est déclenché par un agent : le plan donne la date, le texte prêt et le responsable humain.

## 2. Calendrier J-90 à J+90

| Échéance | Actions | Preuve |
|---|---|---|
| J-90 | ICP et positionnement écrits ; métrique de référence ; modèle de croissance et budget test ; liste d'attente ouverte avec case non pré-cochée et preuve horodatée ; plan de marquage validé ; comptes Product Hunt créés | `strategie-marche.md`, `plan-marketing.md` |
| J-75 | CMP et Consent Mode v2 testés accepté et refusé ; outil de mesure choisi et décision documentée | rapport de test, note de décision |
| J-60 | bêta fermée de 20 à 100 utilisateurs ; balisage serveur déployé ou absence justifiée, recette des balises ; SPF, DKIM, DMARC et désabonnement en un clic ; grille de prospection validée ; robots.txt et CDN autorisent Googlebot et OAI-SearchBot | captures, grille signée |
| J-45 | part de « très déçus » mesurée ; étude de prix menée ; paliers et métrique définis ; CAC, LTV:CAC et payback par canal ; contrats d'influence et d'agences signés ; pages de preuve publiées ; fiches de store prêtes | tableau d'indicateurs, contrats |
| J-30 | budget test publicitaire alloué, suivi de conversion validé ; dossier presse, embargo et témoignages vérifiables prêts ; lancement Product Hunt programmé | dossier presse |
| J-14 | support prêt et délais publiés ; recette bout en bout (acquisition, activation, paiement) consentement accepté puis refusé | `plan-support.md`, rapport de recette |
| J-7 | tableau de bord de lancement en production ; plan de crise écrit | capture, plan de crise |
| J0 | disponibilité générale ouverte ; annonce envoyée aux seuls contacts consentants ; avis et commentaires traités sous 24 h | journal de lancement |
| J+1 | rétention J1 et taux d'erreur relus ; correctifs sous 48 h | tableau de bord |
| J+7 | rétention J7 et activation lues par canal ; canaux sous seuil coupés ; satisfaction courte après intégration et après ticket | tableau de bord |
| J+14 | séquence d'activation ou relance de paniers abandonnés (consentie) active | configuration |
| J+30 | rétention J30, première cohorte et NPS (au moins 30 jours d'usage) lus ; CAC et payback recalculés, budgets réalloués | revue de canaux |
| J+45 | demandes d'avis et de références envoyées ; aucun avis acheté ni rédigé | journal |
| J+60 | revue des opportunités B2B sur grille MEDDICC ; prix et paliers révisés d'après essai vers payant et retours | compte rendu |
| J+90 | bilan : métrique de référence, payback, rétention, coût du support ; décision d'échelle ; post-mortem écrit | bilan |

## 3. Product Hunt

Applicable aux produits utilisables (les bêtas fermées sont généralement refusées).

- S'inscrire et être actif au moins trois mois avant ; programmer jusqu'à un mois avant.
- Lancer à 12 h 01 heure du Pacifique pour avoir 24 heures complètes.
- Seule règle : ne pas demander de votes ; demander de visiter et de commenter. Ne pas payer de promoteurs (bots, concours).
- Description de 500 caractères au plus ; premier commentaire : cible, fonctions, demande de retours.
- Pour une niche : les cent premiers vrais fans comptent plus que l'engagement artificiel.

## 4. Checklist marketing de lancement

Voir `checklist-marketing.md` pour les contrôles numérotés. Résumé à relire à J-7 :

1. Marque, noms de domaine et comptes en place ; mentions légales publiées.
2. Allégations et prix relus par le juriste ; aucune urgence ni preuve fictive.
3. Consentement testé ; mesure active ; tableau de bord en production.
4. Canaux prioritaires prêts, budgets test alloués par l'utilisateur.
5. Support, avis, crise : prêts.

## 5. Gabarit de `plan-communication.md`

```markdown
# Plan de communication de lancement — <projet>

## Synthèse
<12 lignes au plus : objectif, audiences, canaux, messages clés, dates, responsables, risques, ce que l'utilisateur doit déclencher>

## Audiences et messages
| Audience | Message | Preuve | Canal |
|---|---|---|---|

## Calendrier
| Date | Action | Canal | Texte prêt (lien) | Responsable humain | Déclenché par l'utilisateur le |
|---|---|---|---|---|---|

## Contacts autorisés
<sources de consentement, date, durée, preuve ; liste repoussoir>

## Kit presse
<communiqué, visuels, faits vérifiables, embargo, contacts>

## Réseaux et communauté
<ton, fréquence, modération>

## Influence et partenaires
<contrats signés, mentions obligatoires>

## Veille et réponse
<lieux surveillés, délais, procédure d'avis>

## Plan de crise
<porte-parole, seuils, messages types>

## Indicateurs de lancement
<volume et coût par canal, activation, erreurs, plaintes, satisfaction>

## Validation
<revue du juriste le …, accord de l'utilisateur le …>
```

## 6. Pièges et contrôles

- Annonce envoyée à une liste sans consentement ; consentement de plus d'un an.
- Votes sollicités ou promoteurs payés sur Product Hunt : risque de retrait.
- Lancement avec support, base de connaissances et plan de crise absents.
- Recette de bout en bout faite seulement avec le consentement accepté.
- Calendrier maintenu malgré un seuil non atteint.
- Avant de rendre : chaque ligne du calendrier a un responsable humain, un texte prêt et une preuve ; revue juridique faite.

## Sources

- Product Hunt : avant le lancement, préparation, guide de lancement, fonctionnement (producthunt.com/launch)
- First Round Review, Superhuman et le seuil de 40 %
- Gmail et Yahoo, exigences des expéditeurs ; RFC 8058
- DGCCRF et CNIL, règles de prospection (octobre 2026)
