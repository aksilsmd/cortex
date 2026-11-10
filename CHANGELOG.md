# Journal des versions

## 2.0.0 — 10 novembre 2026

- Nouveau skill `accueil-recueil` : chef de parcours du premier contact. Salutation, besoin brut, reformulation
  validée, exploration du domaine (web et GitHub) **avant** l'entretien, propositions, entretien en neuf thèmes
  (interview de `recueil-besoin`), parcours en dix étapes jusqu'à la décision de l'utilisateur : réalisation par
  Dan-Cortex, dossier pour une entreprise, ou startup.
- Nouveau livrable : étude de réalisation (par IA, par une entreprise tierce, mixte, produit existant), budget
  sur trois ans en trois scénarios, gains dans le temps, seuil de rentabilité.
- Table « quel outil, quel skill, quel plugin, à quel moment » et procédure pour aller chercher un outil
  manquant, toujours avec l'accord écrit de l'utilisateur.
- Paquet universel `dan-cortex/universel/` : noyau de moins de 8 000 caractères, version complète en un fichier,
  fichiers de connaissance, skill portable. Construit par `scripts/construire_universel.py`, contrôlé par
  `tests/test_universel.py`. Complète `AGENTS.md`, qui reste le guide des IA capables de lire le dépôt.
- `lancer-projet` passe par l'accueil quand le besoin n'est pas encore cadré.

## 1.17.0 — 7 novembre 2026

- Nouvelle compétence **`traduction-interpretariat`** (FR/AR/EN) : traduire un texte, un livre ou une interface
  en gardant sens, registre et intention ; localiser un produit (RTL arabe, PO/XLIFF, mémoires de traduction) ;
  cadrer l'interprétation orale (consécutif, simultané, liaison). Théories (sourcier/cibliste, skopos, Vinay &
  Darbelnet), cycle qualité, spécificités des trois langues, et outils libres (OmegaT, Weblate, Translate Toolkit,
  LanguageTool, Okapi). Nouveaux agents `traducteur`, `interprete`, `localisateur`.
- **`atelier-ecriture`** enrichi : références sur les métiers et la maison d'édition (chaîne du livre, processus,
  droits, métadonnées ONIX/BISAC/CLIL/Thema, ISBN), les outils d'édition libres (PAO, PDF imprimable, flux
  éditorial, EPUB, validation ONIX), les littératures française, arabe et anglaise (mouvements, genres, prosodie
  comparée, poétique) et la philosophie (branches, traditions dont la falsafa, écriture et dissertation).
- **`recueil-besoin`** : nouvelle option **étude approfondie** enchaînée après le recueil — ratissage et analyses
  (marché, concurrence, existant, voix du client, contexte), design et maquettes, choix des outils, marketing,
  avec réunions de décision, débats, propositions, décisions tracées et validation, puis consolidation de toute la
  documentation ; enfin, proposition de réaliser (via `lancer-projet`) ou de remettre le dossier à une entreprise.
- Matière rassemblée par recherche en ligne et sur GitHub (Firecrawl et agents), contenu traité comme donnée,
  aucun script tiers exécuté, licences lues, forme A. Le plugin compte désormais 24 skills et 59 agents.
- **`AGENTS.md`** à la racine du dépôt : guide d'entrée universel permettant à toute IA (Claude Code, OpenAI
  Codex, Google Antigravity/Gemini, ou un simple chat) de suivre Dan-Cortex — par où commencer, quelle compétence
  pour le cahier des charges, les specs, l'architecture, les lots, les captures et les maquettes, et une règle à
  deux branches (déléguer à des sous-agents si l'environnement le permet, sinon jouer les rôles en séquence).

## 1.16.0 — 7 novembre 2026

- Nouvelle compétence **`recueil-besoin`** : Dan-Cortex recueille le besoin d'une personne par un entretien
  adapté à son profil (débutant, intermédiaire, professionnel), même sans aucune notion d'informatique. Il part
  d'une description brute, la réorganise et la fait valider, mène une interview à choix proposés, priorise
  (MoSCoW, impact/effort, carte des histoires), puis produit un cahier des charges complet avec architecture,
  spécifications, schémas (Mermaid) et appui pour les maquettes, et propose en fin de parcours soit la
  réalisation par Dan-Cortex, soit la remise de la documentation. Compétence auto-portante (utilisable même hors
  plugin). Nouvel agent `intervieweur`. Références : trame d'interview, adaptation au profil, gabarit de cahier
  des charges, schémas Mermaid.
- Nouvelle compétence **`atelier-ecriture`** (atelier d'écriture / maison d'édition) : écrire et accompagner un
  livre, un roman, une nouvelle, un essai, un livre technique, un mémoire ou de la littérature jeunesse, de l'idée
  au manuscrit publiable, et concevoir ou coder un outil d'aide à l'écriture. Structures narratives, construction
  des personnages et de l'univers, passes d'édition, publication (EPUB/PDF, métadonnées, ISBN) et outils libres
  (licences vérifiées). Nouveaux agents `architecte-recit`, `plume`, `editeur-litteraire`, `concepteur-univers`.
- Mise à niveau du dépôt : cette version intègre aussi les skills ajoutés au plugin depuis la 1.4.0 et absents du
  dépôt — `design-apple`, `crm-twenty`, `cartographie-graphe`, `mouvement-interface`, `boite-outils-it` — ainsi
  que les renforts d'audit de sécurité (compétence `safety` branchée dans le pôle, référence `renforts-securite`).
  Le plugin compte désormais 23 skills et 56 agents.

## 1.4.0 — 7 novembre 2026

- Nouvel agent `suivi-avancement` (pilotage, niveau C, `haiku`) : relève l'avancement de chaque étape sur
  preuves comptables (paliers commités, tests au vert, contrôles clos) et le rend en barres de progression avec
  leur état (à faire, en cours, en revue, bloqué, terminé, abandonné). Aucun pourcentage estimé : sans compte,
  l'étape est « non mesurée ».
- `cortex.py avancement maj|afficher|liste|retirer` : étapes et sous-étapes dans `00-pilotage/avancement.csv`,
  rendu dans `00-pilotage/avancement.md` (barre globale, jalons, étapes, bloquages), repris dans le tableau de bord.
- Le chef d'orchestre déclare les étapes dès le plan et joint le bloc d'avancement à chaque compte rendu de vague ;
  en mode autonome, ce bloc remplace la ligne d'avancement entre deux jalons.

## 1.3.1 — 27 octobre 2026

- Les skills `execution-resiliente` et `confidentialite-traces` sont branchés dans le réseau, par renvoi et sans
  dupliquer leur contenu : le chef d'orchestre sait quand les lire, la reprise d'un jalon bloqué en mode autonome
  suit la boucle de `execution-resiliente`, et les ordres de mission comme le pôle `robustesse-agents` renvoient
  au masquage de `confidentialite-traces`.
- Test : chaque renvoi `${CLAUDE_SKILL_DIR}/../<skill>/…` des skills pointe vers un fichier existant.
- Le paquet de mise à jour 1.3.0 (`apply_update.py`) ne doit plus être relancé : il ramènerait la version à 1.3.0.

## 1.3.0 — Autonomie résiliente et confidentialité

- Ajout du skill `execution-resiliente` : planification orientée critères d'acceptation, récupération après erreur et vérification des résultats.
- Ajout du skill `confidentialite-traces` : masquage des secrets et minimisation des données sensibles.
- Maintien des permissions et de la traçabilité ; aucune falsification des journaux ni contournement des contrôles d'accès.
- Construction reproductible de `dist/dan-cortex.plugin` par `scripts/construire_plugin.py` (fichiers suivis par Git,
  ordre et dates fixes), vérifiée en CI ; tests de cohérence des manifestes, du chargement des skills et du build.

## 1.0.1 — 27 octobre 2026

- `cortex.py registre` accepte `--dossier` (et `--max`) avant, entre ou après les champs `cle=valeur`, y compris
  sous Python 3.11 et 3.12, qui rejetaient jusqu'ici les champs placés après une option. Une option inconnue
  reste refusée.

## 1.0.0 — 27 octobre 2026

Cortex devient **Dan-Cortex** et fusionne avec Claude Code Autonomy Lab.

- Renommage : plugin `dan-cortex`, commandes `/dan-cortex:…`, types d'agents `dan-cortex:<nom>`, dossier
  `dan-cortex/`. Le script `cortex.py` et le fichier `cortex.json` des dossiers projet gardent leur nom : les
  projets existants se reprennent tels quels.
- Niveaux d'autonomie `accompagne`, `delegue`, `autonome` (`init --autonomie`, `etat --set autonomie=…`). En
  `autonome`, le réseau enchaîne tout le périmètre après J0, prend les décisions de type 1 au statut `provisoire`,
  agit dans les autorisations permanentes écrites à J0 et respecte six limites dures.
- Quatorzième skill, `robustesse-agents` : audit des réglages Claude Code, gabarit de réglages pour l'autonomie
  (mode `auto`, bac à sable), corpus de scénarios d'injection d'instructions, évaluation live sur accord, script
  `robustesse.py` et paquet `ccal`.
- Seize contrôles `ROB-` (784 au total) : hygiène des agents de la mission, cadre du mode autonome (étiquette
  `autonome`), fonctions d'IA du produit (étiquette `ia`, alignés sur l'OWASP Top 10 LLM 2025).
- Règle commune aux 45 agents : ce qu'ils lisent est une donnée, jamais un ordre ; aucun vrai secret dans un
  livrable.
- J0 audite les réglages des agents ; J5 exige le rapport de robustesse pour un projet `ia` ; l'`auditeur-securite`
  précharge le nouveau skill.
- Tests automatisés (`tests/`) et intégration continue.

## 0.9.0 — 11 octobre 2026

Première version publique.

- Chef d'orchestre et sept jalons, de l'opportunité au bilan, en trois modes.
- Treize skills : un par pôle, plus les réunions et l'audit général.
- Agents experts natifs aux outils restreints, répartis sur trois niveaux de modèle.
- Matrice de couverture filtrée par type de projet, étiquettes, mode et périmètre.
- Script de pilotage : registres, jalons, traçabilité, cohérence des interactions, journal de consommation.
- Essai en conditions réelles sur le jalon J1 en mode éclair.
