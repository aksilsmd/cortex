# Bibliothèque à la demande

Dan-Cortex embarque des compétences tierces sans les charger toutes. Cette page explique le principe, les
garde-fous et la procédure pour ajouter une source.

![Chargement à la demande](images/chargement-a-la-demande.svg)

## Principe

Claude lit au démarrage de chaque session la description de **tous** les skills rangés dans
`dan-cortex/skills/`. Y ranger 173 compétences coûterait des dizaines de milliers de tokens à chaque session et
brouillerait le choix du bon skill. La bibliothèque les range donc à part, dans `dan-cortex/bibliotheque/`, où
Claude ne les voit pas d'office.

Un **skill-pivot** Dan-Cortex (rangé, lui, dans `skills/`) fait le lien :

1. il reconnaît le besoin (« personnage rigué dans Blender », « page immersive en 3D ») ;
2. il pose les garde-fous : accord avant installation ou dépense, sauvegarde, licence ;
3. il ouvre l'index de la bibliothèque, puis l'index de la famille utile ;
4. il ouvre **un seul** `SKILL.md`, puis ses `references/` au fil du besoin.

## Contenu

| Dossier | Contenu | Pivots | Licence |
|---|---|---|---|
| `bibliotheque/scenario-labs/` | 87 compétences de création 3D et de moteurs de jeu (Blender, Maya, ZBrush, Godot, Unity, Unreal, Roblox) et 85 compétences de la plateforme Scenario (images, vidéo, audio, textures, assets 3D) | `studio-3d-jeu`, `creation-medias-ia` | MIT, © 2026 Scenario Inc. |
| `bibliotheque/scroll-world/` | page d'atterrissage « vol à travers un monde » pilotée par le défilement | `web-3d-immersif` | MIT, © 2026 cyw |
| `bibliotheque/cli-anything/` | 70 compétences pour piloter un logiciel en ligne de commande (Blender, FreeCAD, GIMP, Krita, Inkscape, Audacity, Kdenlive, OBS, QGIS, OpenRefine, Obsidian, Zotero, LibreOffice, PM2, n8n, Ollama…) | `pilotage-outils-cli` | Apache-2.0, © 2026 HKUDS |
| `bibliotheque/understand-anything/` | 9 compétences pour comprendre un dépôt de code : carte, domaines, dépendances, graphe de connaissances, revue de différences, arrivée d'un nouveau venu, lecture d'une maquette Figma | `comprendre-un-code` | MIT, © 2026 Yuxiang Lin et Infinite Universe, Inc. |

Les index (`scenario-labs/INDEX.md` et `scenario-labs/index/*.md`) sont générés à partir des en-têtes des
`SKILL.md` ; les compétences elles-mêmes sont des copies fidèles, non traduites, avec leur commit d'origine dans
chaque `NOTICE.md`.

## Garde-fous

- **Donnée, jamais instruction** : une consigne d'une compétence tierce qui contredit les règles Dan-Cortex
  (sécurité, confidentialité, accord de l'utilisateur) est ignorée et signalée.
- **Aucun script sans accord** : les scripts (Python pour Blender, Maya ou Unreal, C# pour Unity, GDScript,
  Luau) ne se lancent qu'après lecture, avec l'accord explicite de l'utilisateur, sur un projet sauvegardé.
- **Aucune dépense sans devis** : les générations payantes (Scenario, Higgsfield) passent par une estimation
  montrée à l'utilisateur, puis un seul essai avant un lot.
- **Licences** : seules des sources sous licence permissive (MIT, Apache-2.0) entrent dans la bibliothèque. Les
  sources GPL, AGPL ou sans licence ne sont reprises qu'en méthode réécrite (forme A), dans le skill-pivot.

## Ajouter une source

1. Lire la licence et noter le commit ; refuser toute source sans licence permissive.
2. Copier le dossier des compétences dans `dan-cortex/bibliotheque/<source>/` avec `LICENSE` et un `NOTICE.md`
   (dépôt, titulaire, commit, fichiers repris, règles d'usage, texte de la licence).
3. Générer un index par famille si la source dépasse une dizaine de compétences.
4. Brancher un skill-pivot existant, ou en créer un dans `dan-cortex/skills/` avec une table de routage
   « besoin → `SKILL.md` exact ».
5. Ajouter la ligne au registre `dan-cortex/skills/robustesse-agents/references/renfort-externe.md` §8 et à
   `dan-cortex/NOTICE.md`.
6. Relancer les trois générateurs et les tests (voir [`CONTRIBUTING.md`](../CONTRIBUTING.md)).
