# Formation — PASSI : audit de sécurité qualifié ANSSI et préparation d'un projet

Fiche de formation pour architecte sécurité, auditeur sécurité et testeur d'intrusion. Elle complète `test-intrusion.md`, `tests-securite.md`, `obligations-cyber.md` et `checklist-securite.md` (SEC-034, SEC-050, SEC-051). Sources ANSSI en fin de fiche (consultées le 2026-11-03) ; collecte : `sources/passi.md`.

**Limite absolue** : les agents Dan-Cortex ne sont pas un prestataire qualifié. Ils ne délivrent ni qualification PASSI, ni « audit PASSI », ni attestation équivalente, et n'écrivent jamais qu'un livrable est « conforme PASSI ». Ils préparent le projet (préaudit interne, dossier de preuves, correctifs) et aident le client à cadrer, choisir et exploiter un audit réalisé par un prestataire qualifié.

## Sommaire
1. Objectifs
2. Ce qu'est PASSI et le référentiel en vigueur
3. Les cinq activités (portées)
4. Niveaux substantiel et élevé ; LPM, RGS, sécurité nationale
5. Exigences sur le prestataire
6. Exigences sur les auditeurs
7. Convention de service et note de cadrage
8. Déroulé d'une prestation en 7 étapes
9. Livrables, rapport et échelles
10. Quand recourir à un PASSI
11. Préparation côté client
12. Méthode Dan-Cortex : préaudit, preuves, correctifs, contre-audit
13. Coûts et délais indicatifs
14. Check-list
15. Anti-patterns et pièges
16. Sources

## 1. Objectifs

L'agent sait :
- citer le référentiel en vigueur (PASSI v2.2) et vérifier une qualification à date ;
- choisir les activités et le niveau adaptés aux enjeux du projet, et rédiger le besoin (cahier des charges) ;
- préparer le projet pour que l'audit soit efficace (périmètre, accès, documentation, environnements, autorisations) ;
- mener un préaudit interne aligné sur les cinq activités, sans jamais le présenter comme qualifié ;
- transformer le rapport en plan de correction suivi et préparer l'audit de contrôle.

## 2. Ce qu'est PASSI et le référentiel en vigueur

- **PASSI** = Prestataires d'audit de la sécurité des systèmes d'information. Qualification délivrée par l'ANSSI, après évaluation par un organisme de qualification habilité, à des prestataires (personnes morales) sur la base d'un référentiel d'exigences.
- **Référentiel en vigueur (novembre 2026)** : « Prestataires d'audit de la sécurité des systèmes d'information – Référentiel d'exigences », **version 2.2**, datée du 1er août 2024, annoncée par l'ANSSI le 29 novembre 2024 (avec PRIS v3.0). Accompagné d'une trame d'évaluation v1.3 et d'une version anglaise.
- **Transition** : v2.0 obsolète ; plus de qualification v2.0 pour un contrat de qualification signé après le 31 janvier 2025 (note ANSSI du 13/12/2024). Une version 2.1-a (septembre 2023) a circulé : ne pas la citer comme référence.
- Objectif de la v2.2 : alignement sur le Cybersecurity Act européen (deux niveaux), offre élargie à davantage de bénéficiaires, prise en compte des contraintes opérationnelles.
- Toujours revérifier à la source avant d'écrire une version ou une date dans un livrable (page « Référentiels d'exigences pour la qualification » de cyber.gouv.fr).

## 3. Les cinq activités (portées)

| Sigle | Activité | Ce que l'auditeur examine | Entrées attendues du client |
|---|---|---|---|
| ARCHI | Audit d'architecture | adéquation de l'architecture (réseau, cloisonnement, flux, équipements et logiciels de sécurité, administration, sauvegardes) aux besoins de sécurité et à l'état de l'art | schémas à jour, matrice des flux, inventaire, dossier d'architecture, analyse de risques |
| CONF | Audit de configuration | configuration des équipements réseau, systèmes, middleware, couche applicative, cloud ; durcissement | accès en lecture, exports de configuration, référentiels de durcissement visés |
| CODE | Audit de code source | développement sécurisé, vulnérabilités (injections, XSS, authentification, cryptographie, gestion des secrets), revue outillée + manuelle | dépôt ou archive du code à une version figée, dépendances, documentation, moyens de build |
| INTRUSION | Tests d'intrusion | identification et exploitation de vulnérabilités, élévation de privilèges, en boîte noire, grise ou blanche, par simulation d'attaquants | périmètre exact (URL, IP, applications), comptes de test par rôle, fenêtres, fiche d'autorisation signée |
| ORGAPHY | Audit organisationnel et physique | politiques (PSSI), organisation, gestion des risques, processus (droits, incidents, sauvegardes, fournisseurs), sécurité physique par visites et entretiens | PSSI, procédures, registres, organigramme, accès aux sites et aux personnes |

Règles :
- Une activité entièrement automatisée (scanner seul) n'est pas une activité au sens du référentiel.
- Systèmes industriels : compétences supplémentaires exigées (automates, SCADA, protocoles industriels, IEC 61508/62443) — demander au prestataire de les démontrer.
- Le responsable d'équipe corrèle les résultats de toutes les activités pour une appréciation globale des risques critiques.
- Pas de portée « mobile », « cloud » ou « IA » distincte : ces objets s'auditent via les cinq activités (ex. application mobile : CODE + INTRUSION + CONF du back-end).
- Le catalogue des prestataires qualifiés indique pour chacun les activités, le niveau et la période de validité : vérifier que l'activité commandée y figure.

## 4. Niveaux substantiel et élevé ; LPM, RGS, sécurité nationale

| | Substantiel | Élevé |
|---|---|---|
| Menace visée | systémique, hacktiviste, isolée | risques élevés, menace stratégique |
| Prestataire | SI homologué, hygiène informatique niveau standard | SI homologué Diffusion Restreinte, hygiène niveau renforcé, revue des droits tous les 6 mois, contrôles d'antécédents |
| Auditeurs | compétences démontrées | attestation individuelle de compétence en vigueur (responsable d'équipe et auditeurs) |
| Exécution | — | restitution « à chaud » quotidienne, support écrit pour les risques critiques, traçabilité renforcée, PV de destruction recommandé |

- Un prestataire est qualifié à un seul niveau pour toutes ses activités ; l'élevé couvre le substantiel.
- **LPM** (opérateurs d'importance vitale, SIIV) : recours à un prestataire de niveau élevé satisfaisant aux exigences complémentaires LPM (document en diffusion restreinte). **Sécurité nationale / informations classifiées** : niveau élevé + référentiel distinct en DR.
- **RGS** (référentiel général de sécurité) : les administrations et autorités administratives s'appuient sur des prestataires qualifiés pour l'homologation ; le RGS fait partie des connaissances exigées des auditeurs.
- **NIS 2** (transposition française en cours ou achevée selon la date : vérifier) : l'audit qualifié est un moyen de preuve recommandé pour les entités concernées ; voir `obligations-cyber.md`.
- Santé : le programme Ségur exige des tests d'intrusion par prestataire PASSI pour certains logiciels (FAQ de l'ANS).

## 5. Exigences sur le prestataire (à vérifier lors du choix)

- Personne morale soumise au droit d'un État membre de l'UE ; droit applicable à la convention : celui d'un État membre.
- Devoir de conseil ; impartialité démontrée et gestion des conflits d'intérêts (recommandation ANSSI : PASSI et PACS distincts sur un même périmètre ; ne pas faire auditer par celui qui a conçu ou intégré).
- Gestion des plaintes, avec information de l'ANSSI.
- Vérification des diplômes, compétences et CV au recrutement ; sensibilisation à la réglementation.
- Appréciation des risques de son propre SI, moindre privilège, revue des droits, SI homologué ; conservation des informations d'audit sur un système hors ligne.
- Protection des informations du commanditaire à toutes les étapes ; destruction ou restitution en fin de prestation.
- Peut réaliser des prestations non qualifiées, mais ne peut alors s'en prévaloir : le contrat doit dire explicitement « prestation qualifiée », avec niveau, activités et attestation jointe.

## 6. Exigences sur les auditeurs

- Lien contractuel avec le prestataire (contrat de travail ; cadre contractuel pour les experts ponctuels, avec accord du commanditaire).
- Maîtrise de l'ISO/IEC 19011 (lignes directrices d'audit) et qualités personnelles (rédaction, synthèse, oral).
- Recommandations : formation en SSI, au moins un an d'expérience en audit ; formation continue et veille obligatoires.
- Niveau élevé : attestation individuelle de compétence en vigueur.
- Connaissances réglementaires : secret de la défense nationale, LPM/SIIV, directives NIS, RGS, RGPD, informations classifiées OTAN/UE.
- **Responsable d'équipe** : organise, constitue et pilote l'équipe, valide note de cadrage, plan d'audit et rapport ; peut auditer seul s'il a toutes les compétences.
- Le référentiel ne fixe pas un nombre minimal d'auditeurs par activité : le dimensionnement se discute dans l'offre.

## 7. Convention de service et note de cadrage

Contenu minimal de la **convention** :
- mention de la qualification, du niveau, des activités ; attestation de qualification jointe ;
- droit applicable (UE), périmètre, démarche, activités, livrables, pays d'exécution ;
- recours à des experts ou sous-traitants : accord écrit du commanditaire ;
- propriété intellectuelle, responsabilités, confidentialité (liste des destinataires, partage possible avec le CERT-FR pour une vulnérabilité, destruction en fin de prestation) ;
- modalités de la note de cadrage.

**Note de cadrage** (rédigée en préparation, annexée au rapport) : objectifs, périmètre précis et exclusions, correspondants des deux côtés, marquage et circuit des informations, gouvernance, contraintes légales et contractuelles (hébergeurs, infogérants, éditeurs à prévenir), fenêtres d'intervention, mesures de précaution.

**Fiche d'autorisation de tests d'intrusion** : signée par le commanditaire (et par les tiers propriétaires des infrastructures si nécessaire : hébergeur, cloud), elle fixe adresses, dates, heures, sources des tests, contacts d'urgence, actions interdites. Un test pouvant provoquer un déni de service n'est mené qu'avec accord écrit.

## 8. Déroulé d'une prestation en 7 étapes

1. **Qualification préalable d'aptitude** : le prestataire n'accepte que s'il peut tout réaliser (compétences, disponibilité, impartialité).
2. **Convention de service**.
3. **Préparation** : responsable d'équipe désigné, note de cadrage, mesures de précaution (sauvegardes, environnement de test comparable à la production, contacts d'urgence), plan d'audit, réunion d'ouverture recommandée.
4. **Exécution** : méthodes par activité (entretiens, revue documentaire, revue de configuration, revue de code, tests) ; tests d'intrusion en boîte noire, grise ou blanche ; notification immédiate d'une vulnérabilité critique ; signalement à l'ANSSI des vulnérabilités non publiques selon les règles du référentiel.
5. **Restitution** des constats (quotidienne en élevé ; support écrit pour les risques critiques).
6. **Rapport d'audit**.
7. **Clôture** : réunion recommandée, restitution ou destruction des informations, conservation hors ligne de ce qui est autorisé, PV de destruction (recommandé en élevé), recommandation d'un audit de contrôle.

## 9. Livrables, rapport et échelles

Contenu du **rapport** :
- mentions de qualification (niveau, activités, équipe) ; cadre (objectifs, périmètre, dates, documents de référence) ;
- **synthèse managériale** compréhensible par des non-spécialistes : risques critiques, appréciation globale, réserves (exhaustivité, phases automatisées, limites de temps) ;
- **constats** : identifiant unique, description, preuves, gravité, priorité, recommandation ; catégorisation des vulnérabilités recommandée ;
- plan d'action priorisé ; recommandation d'un **audit de contrôle** ;
- annexes obligatoires : plan d'audit et note de cadrage.

**Échelles** : la v2.2 exige des échelles de gravité et de priorité explicites, sans en imposer une. Convention Dan-Cortex pour le préaudit et pour lire un rapport (alignée sur `test-intrusion.md`) :
- gravité technique en **CVSS 4.0** avec le groupe indiqué (B, BT, BE, BTE) ;
- traduction en 4 niveaux pour la direction : **critique / élevée / moyenne / faible** ;
- priorité de correction : P1 immédiat (≤ 7 jours, ou mesure compensatoire sous 24–72 h pour un critique exposé), P2 ≤ 30 jours, P3 prochain cycle, P4 opportunité — délais à fixer dans la politique de vulnérabilités du projet ;
- si le rapport du prestataire utilise sa propre échelle (souvent gravité × difficulté d'exploitation), conserver son échelle et ajouter la correspondance, sans renoter ses constats.

## 10. Quand recourir à un PASSI

| Situation | Recommandation |
|---|---|
| OIV/SIIV (LPM), informations classifiées | obligatoire : niveau élevé + exigences LPM / sécurité nationale |
| Administration (homologation RGS), entité NIS 2 essentielle ou importante | fortement recommandé, souvent exigé par le donneur d'ordre |
| Exigence d'un client, d'un appel d'offres public, d'un programme sectoriel (santé Ségur, etc.) | obligatoire si le texte le dit ; vérifier l'activité et le niveau demandés |
| E-commerce, SaaS B2B, données personnelles sensibles, paiement | recommandé avant la mise en production à fort enjeu, puis annuel ou à chaque changement majeur |
| Prototype, site vitrine sans données sensibles | préaudit interne + scanners ; audit qualifié non nécessaire |
| Client hors de France (ex. Algérie) | PASSI est une qualification française : utile si le client la demande ou si le service vise le marché français/européen ; sinon équivalent local ou prestataire certifié (ex. CREST, ISO 27001 du prestataire) à discuter |

La décision est tracée (SEC-034), et la qualification vérifiée à date dans le catalogue des prestataires qualifiés de l'ANSSI (MesServicesCyber) (SEC-051).

## 11. Préparation côté client

Avant consultation :
- objectifs de l'audit (preuve réglementaire, assurance client, avant mise en production) et activités visées ;
- périmètre : liste exhaustive des actifs (domaines, IP, applications, API, applications mobiles, comptes cloud), exclusions motivées ;
- niveau visé et contraintes (LPM, données de santé, sous-traitants) ;
- cahier des charges (guide ANSSI pour les commanditaires ; l'ANSSI peut appuyer certains commanditaires).
Avant exécution :
- documentation à jour : dossier d'architecture, matrice des flux, inventaire, analyse de risques, PSSI, procédures ;
- environnement de test représentatif de la production (mêmes versions, configurations, données fictives) ; sauvegarde vérifiée ;
- comptes de test pour chaque rôle (dont administrateur si boîte grise/blanche), jeux de données fictives ;
- autorisations des tiers (hébergeur, cloud, éditeurs SaaS, CDN, WAF) et désactivation ou mise en liste blanche des protections si le plan le prévoit ;
- fiche d'autorisation signée, contacts d'urgence 24/7 pendant les fenêtres de test ;
- code source figé (tag) pour l'audit de code ; accès en lecture aux configurations ;
- équipe disponible pour les entretiens (ORGAPHY) et pour corriger rapidement les critiques.

## 12. Méthode Dan-Cortex : préaudit, preuves, correctifs, contre-audit

Le pôle sécurité prépare le projet, il ne se substitue pas au prestataire.

1. **Cadrage** (architecte-securite) : enjeux, obligations (`obligations-cyber.md`), décision « audit qualifié oui/non, activités, niveau » tracée ; rédaction du projet de cahier des charges et de note de cadrage.
2. **Préaudit interne aligné sur les 5 activités** (auditeur-securite, testeur-intrusion), sur les seuls environnements du projet, avec autorisation écrite :
   - ARCHI : revue du dossier d'architecture, cloisonnement, flux, administration, sauvegardes, contre les guides ANSSI pertinents ;
   - CONF : durcissement (CIS Benchmarks, guides ANSSI), en-têtes HTTP, TLS, cloud (IAM, stockage public, journaux) ;
   - CODE : SAST, SCA, secrets, revue manuelle des zones à risque (authentification, autorisation, paiement, téléversements) ;
   - INTRUSION : tests en boîte grise selon OWASP WSTG/ASVS (web) et MASTG (mobile), dans `test-intrusion.md` ;
   - ORGAPHY : existence et application de la PSSI, gestion des droits, incidents, sauvegardes, fournisseurs.
   Livrable : `05-validation/preaudit-securite.md`, intitulé « préaudit interne non qualifié ».
3. **Dossier de preuves** (pour l'auditeur) : documentation à jour, inventaire, matrice des flux, configurations exportées, résultats d'outils datés, politique de vulnérabilités, registre des correctifs, PSSI et procédures, comptes de test préparés — tout sans secret réel.
4. **Correctifs** : critiques et élevés corrigés et contre-testés avant l'audit ; les autres planifiés ; exceptions datées et signées.
5. **Pendant l'audit** : point de contact unique, réponse rapide aux demandes, correction immédiate des critiques notifiés (traçée).
6. **Après le rapport** : import des constats avec l'ID du prestataire, plan de correction priorisé (propriétaire, échéance), contre-test interne, puis **audit de contrôle** par le prestataire pour attester du statut des corrections ; mise à jour de la couverture (SEC-045, SEC-050).

## 13. Coûts et délais indicatifs (à vérifier par devis)

- Exemple public : pour le périmètre Ségur vague 2, l'ANS indique en moyenne 5 000 à 10 000 € et environ une semaine ouvrée pour un test d'intrusion qualifié (FAQ mise à jour en août 2026). Ce chiffre ne vaut que pour ce périmètre.
- Le coût dépend du nombre d'activités, de la taille du périmètre, du niveau (élevé plus cher et moins de prestataires), du mode (boîte blanche plus long), des déplacements (ORGAPHY).
- Délais : compter la disponibilité des prestataires (souvent plusieurs semaines), la préparation (1–3 semaines), l'exécution, le rapport (souvent 1–3 semaines après la fin des tests), puis l'audit de contrôle. Toute estimation chiffrée dans un livrable porte « hypothèse — à confirmer par devis » et passe par le pôle finance.

## 14. Check-list

- [ ] Référentiel cité : PASSI v2.2 (1er août 2024), vérifié à la source à la date du livrable.
- [ ] Décision de recours tracée, avec activités et niveau justifiés par les enjeux et obligations.
- [ ] Qualification du prestataire vérifiée à date (activités, niveau, validité) dans le catalogue ANSSI.
- [ ] Contrat mentionnant « prestation qualifiée », niveau, activités, attestation jointe.
- [ ] Indépendance : prestataire distinct du concepteur, de l'intégrateur et du PACS éventuel.
- [ ] Note de cadrage et plan d'audit validés ; tiers informés ; fiche d'autorisation signée ; contacts d'urgence.
- [ ] Environnement représentatif, sauvegardé, données fictives ; comptes de test par rôle.
- [ ] Préaudit interne réalisé et étiqueté « non qualifié » ; critiques/élevés corrigés et contre-testés.
- [ ] Dossier de preuves complet, sans secret réel.
- [ ] Rapport reçu : synthèse, constats identifiés et prouvés, échelles explicites, plan d'action.
- [ ] Plan de correction suivi ; audit de contrôle planifié ; PV de destruction ou modalités de conservation reçus.

## 15. Anti-patterns et pièges

- Présenter un préaudit d'agents comme un « audit PASSI » ou écrire « conforme PASSI » : interdit.
- Citer la v2.0 ou la 2.1-a ; recopier une date sans vérifier (la note de transition elle-même contient des dates incohérentes).
- Commander « un PASSI » sans préciser activités et niveau ; supposer que tout prestataire qualifié couvre toutes les activités.
- Croire qu'un scan automatisé suffit : une activité entièrement automatisée n'est pas une activité PASSI.
- Tester en production sans fiche d'autorisation, sans prévenir l'hébergeur ou le fournisseur cloud.
- Environnement d'audit non représentatif (versions différentes) : constats inutilisables.
- Faire auditer par le prestataire qui a construit le système.
- Rapport rangé sans plan de correction ni audit de contrôle.
- Diffuser le rapport largement : il décrit comment attaquer le système ; diffusion restreinte et marquage.
- Promettre un prix ou un délai sans devis.

## 16. Sources

Consultées le 2026-11-03.
- ANSSI, Référentiels d'exigences pour la qualification : https://cyber.gouv.fr/referentiels-dexigences-pour-la-qualification
- ANSSI, PASSI – Référentiel d'exigences v2.2 (PDF) : https://cyber.gouv.fr/sites/default/files/document/PASSI_Referentiel-exigences_v2.2.pdf
- ANSSI, L'ANSSI met à jour les référentiels PASSI (v2.2) et PRIS (v3.0) : https://cyber.gouv.fr/actualites/lanssi-met-jour-les-referentiels-passi-version-22-et-pris-version-30
- ANSSI, Note aux organismes de qualification – Transition PASSI : https://cyber.gouv.fr/sites/default/files/document/Note-aux-organismes-de-qualification-PASSI-Transition-PASSI.pdf
- ANSSI, Référentiel PASSI version 2.1-a (historique) : https://cyber.gouv.fr/sites/default/files/document/R%C3%A9f%C3%A9rentiel%20PASSI%20%E2%80%93%20version%202.1-a%20%E2%80%93%20sans%20marque%20de%20r%C3%A9vision.pdf
- ANSSI, Note – Portées de qualification des services v2.1 : https://cyber.gouv.fr/sites/default/files/document/QUAL_SERV_PORTEES_v2.1.pdf
- ANS (esante.gouv.fr), Coût et durée d'un test d'intrusion : https://esante.gouv.fr/faq/quel-est-le-cout-du-test-d-intrusion-et-quelle-est-sa-duree-de-realisation
- FIRST, CVSS 4.0 : https://www.first.org/cvss/v4.0/
