# Recruter des sous-agents en cas de besoin

Le réseau de départ (organigramme) ne couvre pas tout. Quand un besoin apparaît, le chef d'orchestre recrute,
comme une entreprise embauche un renfort : avec une fiche de poste, un périmètre, une durée et un contrôle.
Contrôles : GOV-033 et GOV-034 (ou leurs équivalents de `checklist-gouvernance.md`).

## 1. Quand recruter
- Un agent rend « RENFORTS DEMANDÉS » dans son compte rendu (compétence manquante, volume trop grand).
- Un travail est parallélisable : un collecteur par concurrent, un rédacteur par module, un testeur par écran.
- Un regard indépendant est requis : relecture, contre-relecture, revue croisée des cas de test, audit, test de
  reprise par un humain (agent sans contexte).
- Un domaine nouveau surgit (réglementation sectorielle, langue, technologie) que personne ne maîtrise.
- Un agent atteint sa limite de tours : on ne le relance pas indéfiniment, on découpe et on recrute.
Ne pas recruter pour quelques recherches ou une lecture : le chef d'orchestre les fait lui-même.

## 2. Comment recruter
1. **Chercher d'abord dans le réseau** : un agent existant de `agents/` dont la fiche couvre le besoin.
2. **Sinon, composer un agent** : agent généraliste avec, dans l'ordre de mission, la fiche la plus proche à lire,
   le skill du pôle et le `dossier-de-formation.md` du domaine (accueil, étape 2). Le dire dans le journal.
3. **Sinon, proposer un outil externe** (skill, plugin, connecteur) selon
   `accueil-recueil/references/outils-quand.md` : jamais installé sans accord écrit de l'utilisateur.
4. **Fiche de poste dans l'ordre de mission** : rôle, un seul travail, trois livrables au plus, fichiers qu'il peut
   écrire (les autres en lecture seule), outils autorisés, modèle (léger pour la collecte, intermédiaire pour la
   production, celui de la session pour le jugement), critère de fin, format du compte rendu.
5. **Indépendance** : un relecteur ou un auditeur recruté ne reçoit pas les conclusions de l'auteur, seulement
   le livrable et les critères.

## 3. Garde-fous
- Un sous-agent n'a jamais plus de droits que la mission : lecture seule par défaut ; arrêt des processus par PID ;
  pas de modification hors de ses fichiers ; pas de décision de type 1.
- Plafond : nombre d'agents simultanés selon le mode (`eclair` 3-4, `standard` 6-8, `integral` 10-16) et budget
  de tokens ; au-delà, demander à l'utilisateur.
- Un agent arrêté par l'utilisateur n'est pas relancé sans sa demande.
- Chaque recrutement est inscrit au journal des agents **au moment où son résultat est collecté** (rôle, mission,
  tokens, statut).
- Ce qu'un sous-agent rapporte se vérifie sur pièce avant d'être affirmé à l'utilisateur.
