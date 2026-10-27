# Journal des versions

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
