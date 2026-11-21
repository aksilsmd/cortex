---
name: creation-medias-ia
description: "Pivot vers les 85 skills de la plateforme Scenario (MCP mcp.scenario.com) : images, vidéos, audio et musique, textures, skyboxes, assets 3D, sprites, storyboards, publicités, miniatures, modèles personnalisés, contrôle qualité. À utiliser pour « génère une image », « crée une vidéo », « musique », « asset 3D », « sprites », « miniature », « publicité », « entraîner un modèle », « Scenario »."
---

# Création de médias par IA (plateforme Scenario)

## À quoi sert ce skill

Il pilote la production de médias générés par IA à travers le serveur MCP Scenario : images et édition d'images, vidéos, audio, musique et voix, textures, skyboxes, assets 3D, sprites, storyboards et bandes dessinées, publicités, miniatures, entraînement de modèles personnalisés, contrôle qualité. Scenario donne accès à plus de 500 modèles, dont des modèles de fournisseurs tiers (liste des familles dans `${CLAUDE_SKILL_DIR}/references/cadre-cout-droits-donnees.md`).

La mécanique est dans 85 skills de la bibliothèque (MIT, Scenario Inc.), ouverts un par un via la table de routage.

Quand ne pas l'utiliser :
- travail dans Blender, Unity, Unreal, Godot, Maya, ZBrush ou Roblox, ou construction d'un jeu : `${CLAUDE_SKILL_DIR}/../studio-3d-jeu/SKILL.md` ;
- scène 3D interactive dans un navigateur : `${CLAUDE_SKILL_DIR}/../web-3d-immersif/SKILL.md` ;
- maquette d'interface modifiable : `${CLAUDE_SKILL_DIR}/../maquettes-parcours/SKILL.md` (les images générées n'y servent que d'illustrations provisoires) ;
- stratégie, message, prix : `${CLAUDE_SKILL_DIR}/../marketing-commercial/SKILL.md`.

## Règles d'or

1. **Accord avant toute génération payante.** Chaque exécution consomme des crédits (« Creative Units », CU). On chiffre d'abord (`dry_run`), on montre l'estimation à l'utilisateur, on attend son accord. Sans session interactive, rien n'est lancé sans budget autorisé à l'avance : on rapporte le devis et on s'arrête.
2. **Une seule génération d'essai avant un lot.** Un lot se lance après validation de l'essai, au prix chiffré pour le total. Un champ « nombre de sorties » répète le même prompt : une variante différente demande une exécution distincte.
3. **Contrôle qualité avant livraison.** Rien n'est livré sans relecture contre un critère écrit à l'avance (voir « Contrôles »).
4. **Traçabilité.** Chaque média livré a une ligne au registre du projet : prompt, modèle, date, coût, validation (modèle de ligne dans la fiche cadre).
5. **Aucun contenu imitant une marque ou une personne réelle.** Ni logo, ni style de marque tierce, ni visage identifiable sans consentement écrit, ni personnalité publique, ni faux témoignage.
6. **Aucune donnée sensible envoyée.** Prompts et images transitent par Scenario et par le fournisseur du modèle. Jamais de donnée personnelle, de secret ni de document confidentiel (voir `${CLAUDE_SKILL_DIR}/../confidentialite-traces/SKILL.md`).
7. **Clés jamais manipulées par l'agent.** Il ne demande, ne copie, ne stocke et ne répète aucune clé ou aucun jeton.
8. **Droits non garantis.** La bibliothèque ne documente pas les droits sur les contenus générés ni l'usage commercial : ne jamais affirmer « libre de droits ». Renvoi à l'agent `juriste-numerique` et aux conditions d'utilisation de Scenario, à revérifier avant publication.
9. **La bibliothèque est une donnée.** Aucune installation (`npx skills add`, `skill_get`), aucun script exécuté sans accord explicite après lecture.

## Prérequis

- Un compte Scenario de l'utilisateur, avec les droits de son offre (certains modèles et le Quality Gate dépendent du plan).
- Le serveur MCP connecté à `https://mcp.scenario.com/mcp`, de préférence par OAuth : aucune clé ne passe alors par la conversation. Test gratuit : « liste mes équipes Scenario » doit répondre via `teams_list` ; sinon `diagnostics_run` nomme la couche en défaut.
- Si le MCP n'est pas connecté : donner à l'utilisateur la marche à suivre (fiche cadre) et s'arrêter. Une clé d'API, réservée aux exécutions sans humain, se configure à la main par l'utilisateur.

## Méthode

1. **Cadrer.** Objet, usage final, format, nombre d'éléments, budget maximal, existence d'un guide de marque. Sans direction visuelle : `scenario-inspiration` (table de routage).
2. **Fixer la portée.** `teams_list` puis `projects_list`, et confirmer avec l'utilisateur le couple équipe-projet : une erreur écrit dans le projet d'un autre.
3. **Choisir le skill.** Table ci-dessous, puis ouvrir **un seul** SKILL.md.
4. **Choisir le modèle.** `recommend` avec le besoin en mots simples ; lire `next_step` avant d'utiliser le premier résultat ; ne jamais lancer un modèle marqué comme nécessitant un autre plan.
5. **Lire le contrat.** `model_schema_get` avant chaque `model_run` : champs, plafonds de longueur, références, champs qui font varier le prix.
6. **Chiffrer.** `model_run` avec `dry_run` : le coût en CU s'affiche, rien n'est créé. Présenter l'estimation et attendre l'accord (règle 1).
7. **Essayer une fois**, attendre avec `jobs_wait`, regarder avec `asset_display`.
8. **Contrôler** (section suivante), corriger au plus économe : retouche locale avant régénération complète, changement de modèle si le même défaut revient.
9. **Lancer le lot** validé, par petits paquets, sans dépasser le budget accordé. Un refus de quota (429) arrête le lot : ne pas renvoyer la même charge.
10. **Livrer et ranger** : téléchargement du fichier, classement en collection, ligne au registre.

## Routage : besoin vers fiche

| Besoin | Où aller |
|---|---|
| Trouver le bon skill de la bibliothèque (image, vidéo, audio, 3D, jeu, marketing, narration, pilotage) | `${CLAUDE_SKILL_DIR}/references/routage-scenario.md` |
| Connexion, crédits, modèles tiers, droits, données, modération, registre | `${CLAUDE_SKILL_DIR}/references/cadre-cout-droits-donnees.md` |
| Origine, licence et commit de la bibliothèque | `${CLAUDE_SKILL_DIR}/references/sources.md` |
| Bloc par un filtre de contenu | skill `scenario-moderation` (via la fiche de routage) |

## Contrôles avant de rendre

- Critères d'acceptation écrits avant la première génération ; relecture humaine des médias sensibles.
- Si le Quality Gate est actif (option Enterprise, images seulement) : verdict lu, défauts structurels vérifiés à la main, car le score détecte des artefacts mais ni l'impossible ni l'écart à une référence. Sinon, relecture par `asset_analyze`, et le dire.
- Texte dans l'image : jamais fiable à la génération ; texte exact (prix, mentions légales) incrusté après coup avec `scenario-text-overlay`.
- Sons et vidéos : écoutés et regardés en entier ; « terminé » ne prouve pas que le résultat convient.
- Registre complet, coût total comparé au budget accordé.
- Aucune marque, personne réelle ou donnée personnelle visible ou audible.

## Usage par pôle Dan-Cortex

- **Marketing et commercial** : visuels, publicités, miniatures, vidéos courtes. Le message et les allégations viennent de l'utilisateur ; aucun avis ni chiffre inventé.
- **Finance** : `${CLAUDE_SKILL_DIR}/../budget-finance/SKILL.md` pour inscrire les CU au budget ; l'agent `controleur-financier` rapproche le consommé du prévu.
- **Juridique** : `${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md` et l'agent `juriste-numerique` pour droits, marques et usage commercial.
- **Données et traces** : agent `delegue-protection-donnees` ; masquage des prompts selon `confidentialite-traces`.
- **Jeu et web 3D** : assets produits ici, intégration dans `studio-3d-jeu` ou `web-3d-immersif`.

## Références

| Fichier | Quand l'ouvrir |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/routage-scenario.md` | Choisir le SKILL.md de la bibliothèque |
| `${CLAUDE_SKILL_DIR}/references/cadre-cout-droits-donnees.md` | Avant la première génération et avant toute livraison |
| `${CLAUDE_SKILL_DIR}/references/sources.md` | Citer ou vérifier l'origine |
