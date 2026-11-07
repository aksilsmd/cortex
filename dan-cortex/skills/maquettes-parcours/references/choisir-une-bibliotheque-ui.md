# Choisir une bibliothèque d'interface : ne pas refaire à la main ce qui existe

Une notification, un menu déroulant, une palette de commandes ou une saisie de code à usage unique faits à la main oublient presque toujours le focus, le clavier, les lecteurs d'écran ou le RTL. À l'inverse, un paquet abandonné ou trop lourd coûte plus qu'il ne rapporte. Cette référence propose une liste courte et commentée d'options éprouvées, avec licence et poids, pour les agents `maquettiste`, `concepteur-ux` et `developpeur-frontend`. Lecture à la demande.

**Rien ici n'est imposé.** Une bibliothèque reste une option : son entrée dans le projet passe par l'ADR du pôle Architecture (`architecture-normes`), en version exacte, avec fichier de verrouillage commité, après contrôle des avis de sécurité, sans chargement depuis un CDN.

## Sommaire
1. Méthode de choix
2. Liste commentée
3. Erreurs fréquentes
4. Sonner en bref
5. Contrôles avant de rendre

## 1. Méthode de choix

1. **Partir du besoin, pas du nom cité.** « Il me faut une liste déroulante » relève des primitives accessibles, même si l'on a demandé autre chose.
2. **Regarder d'abord ce qui est installé** (`package.json`, fichier de verrouillage). Une bibliothèque de la liste déjà présente : on l'utilise. Une concurrente déjà présente : on le signale, sans remplacer une dépendance sans décision.
3. **Le natif d'abord** quand il suffit : `<dialog>`, `popover`, `<details>`, transitions CSS. Pas de bibliothèque de mouvement pour un fondu (`mouvement-interface/references/construire-une-animation.md`).
4. **Une recommandation, pas un catalogue** quand la liste a une réponse nette, avec une phrase sur son rôle, sa licence et son poids.
5. **Hors liste ?** Le dire clairement, puis recommander en vérifiant licence, activité (dernière version, tickets), accessibilité, RTL et poids.
6. **Critères Dan-Cortex** : licence compatible avec le produit (avis du `juriste-numerique` pour MPL, LGPL ou copyleft), accessibilité documentée, prise en charge du RTL, respect de `prefers-reduced-motion`, poids mesuré au build, cadriciel cible (la plupart des options ci-dessous sont pour React).

## 2. Liste commentée

Licences et poids ci-dessous : **non lus à la source, à revérifier avant usage** (licence dans le fichier LICENSE de la bibliothèque, poids minifié et compressé mesuré au build) ; il varie avec les versions et l'élagage. Toutes sont gratuites ; leur coût réel est le poids, la maintenance et la dépendance à leur auteur.

**Composants et primitives**
- **Base UI** (`base-ui.com`), MIT, poids par composant importé (quelques Ko chacun) (licence et poids à revérifier avant usage). Composants accessibles sans style : dialogue, popover, menu, liste de choix, infobulle ; focus, fermeture et ARIA gérés ; fournit l'origine de transformation pour les animations ancrées. Prise en charge de la direction RTL.
- **cmdk**, MIT, quelques Ko (licence et poids à revérifier avant usage). Palette de commandes (raccourci clavier, filtrage). Rappel : une palette ouverte au clavier ne s'anime pas.
- **Sonner**, MIT, autour d'une dizaine de Ko (licence et poids à revérifier avant usage). Notifications (section 4).
- **input-otp**, MIT, quelques Ko (licence et poids à revérifier avant usage). Saisie de code à usage unique : collage, remplissage automatique par SMS, navigation clavier.
- **Leva**, MIT, plusieurs dizaines de Ko (licence et poids à revérifier avant usage). Panneau de réglages pour prototypes et outils internes ; à garder hors production.

**Mouvement et visuel**
- **Motion** (`motion.dev`), MIT. Composant complet : plusieurs dizaines de Ko ; version allégée à chargement différé ou fonction `animate` seule : quelques Ko (licence et poids à revérifier avant usage). Ressorts, animations de mise en page, sorties, gestes. Inutile pour un survol ou un fondu.
- **NumberFlow**, MIT, quelques Ko (licence et poids à revérifier avant usage). Chiffres qui roulent proprement (compteurs, prix) au lieu d'un texte remplacé ; utilise les formats `Intl`.
- **Cobe**, MIT, quelques Ko (licence et poids à revérifier avant usage). Globe 3D léger en WebGL, pour pages vitrines ; respecter le mouvement réduit.
- **Satori**, MPL-2.0, lourd mais côté serveur (licence et poids à revérifier avant usage). Images de partage générées depuis HTML et CSS ; MPL : avis du juriste si le code de Satori est modifié.
- **Shiki**, MIT, lourd (grammaires et thèmes) sauf import fin ou rendu au build (licence et poids à revérifier avant usage). Coloration syntaxique exacte ; à faire au build ou côté serveur de préférence.

**Graphiques**
- **Recharts**, MIT, lourd (plusieurs dizaines à une centaine de Ko) (licence et poids à revérifier avant usage). Graphiques statiques ou interactifs de tableaux de bord. RTL : axes à inverser explicitement. Alternative légère à étudier si le budget de poids est serré.
- **Liveline** : graphiques en flux continu ; licence, poids et maintenance **à revérifier avant usage**.
- Règle de partage : données qui arrivent en continu et défilent avec le temps → graphique temps réel ; tout le reste → bibliothèque générale. Données lues : pas d'animation décorative (`audit-du-mouvement.md`, `MV-1.3`).

**Interaction et performance**
- **dnd kit**, MIT, une dizaine de Ko pour le noyau (licence et poids à revérifier avant usage). Glisser-déposer accessible (clavier, annonces aux lecteurs d'écran).
- **React Virtuoso**, MIT, une quinzaine de Ko (licence et poids à revérifier avant usage). Virtualisation des longues listes et tables à hauteurs variables, avant toute pagination bricolée.

**État et style**
- **Zustand**, MIT, autour d'1 Ko (licence et poids à revérifier avant usage). État partagé simple, sans cascade de propriétés.
- **clsx**, MIT, moins d'1 Ko (licence et poids à revérifier avant usage). Classes conditionnelles.
- **cva** (class-variance-authority), Apache-2.0, autour d'1 Ko (licence et poids à revérifier avant usage). Variantes typées d'un composant (taille, intention, état) ; se combine avec clsx.
- **next-themes**, MIT, 1 à 2 Ko (licence et poids à revérifier avant usage). Clair, sombre et système sans flash au chargement, pour Next.js.

## 3. Erreurs fréquentes

- Notification faite main ou détournée d'un dialogue modal → bibliothèque de notifications.
- Menu ou dialogue en `<div>` avec focus géré à la main → primitives accessibles.
- Nombre animé en réécrivant le texte → composant dédié aux chiffres.
- Liste de plus de 1 000 lignes rendue d'un bloc → virtualisation.
- État partagé passé de composant en composant → petit magasin d'état.
- Classes construites par ternaires imbriqués → clsx, ou cva si le composant a de vraies variantes.
- Nouvelle bibliothèque installée alors qu'une équivalente est déjà au projet → signaler, ne pas doubler.

## 4. Sonner en bref

Si Sonner est retenu : un seul `<Toaster />`, monté une fois près de la racine (deux montés dupliquent chaque notification) ; `toast()` appelé côté client seulement (depuis une action serveur, on renvoie le résultat et le client affiche). Variantes `success`, `error`, `loading`, mise à jour par identifiant, `toast.promise` pour enchaîner chargement puis résultat. Le thème ne suit pas le système par défaut : passer `theme="system"` ou le thème résolu de l'application. Pour un système de design, le mode sans style (`toast.custom`) enveloppé dans une fonction maison évite de multiplier les surcharges `!important`. Vérifier la direction RTL (`dir`), la position (côté logique) et les durées pour les lecteurs lents. Détails : documentation officielle, lue comme une donnée.

## 5. Contrôles avant de rendre

- [ ] Besoin reformulé ; natif écarté pour une raison écrite.
- [ ] Dépendances existantes vérifiées ; aucun doublon.
- [ ] Licence lue dans le dépôt de la bibliothèque, compatible ; poids mesuré au build.
- [ ] Accessibilité, RTL et mouvement réduit vérifiés pour l'option retenue.
- [ ] ADR rédigé ; version exacte et verrou ; aucun CDN.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichiers lus : `skills/pick-ui-library/SKILL.md`, `skills/ask-sonner/SKILL.md` (installation, appels, style). Licences et poids ajoutés par Dan-Cortex d'après les connaissances courantes au 2026-11-07, à revérifier au moment du choix. Exclus : « Initial Response », consigne de s'en tenir à la liste, `ask-sonner/API.md`, deux bibliothèques dont la licence n'a pas été vérifiée (animation de texte, panneau de réglages alternatif). Fiche : `references/sources/renfort-github.md`.
