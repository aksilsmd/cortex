# Swift moderne : écrire du Swift comme le langage le veut

Repères pour écrire, relire ou migrer du Swift (iOS, iPadOS, macOS). Lecture à la demande : `developpeur-mobile` sur un projet natif Apple, `relecteur-code` en revue.

**Versions** : selon la source, Swift 6.3 est publié (août 2026), 6.4 ne l'est pas. Lire la chaîne d'outils du projet avant toute nouveauté.

## 1. Fil conducteur

Swift se dévoile progressivement : on commence par le plus simple, le plus statique, le plus mono-fil, et l'on n'achète de la dynamique (concurrence, références partagées, existentiels, pointeurs) que pour une raison nommée. Échelle des défauts : données en `struct`/`enum` ; type concret avant abstraction ; `some` avant `any` ; acteur principal synchrone avant `async`, puis `@concurrent`, puis `actor` ; `Array`/`String` avant stockage en ligne ; API sûre avant `Unsafe*`.

## 2. Données : types valeur d'abord

- `struct`/`enum` par défaut ; `class` pour identité, état partagé, héritage ou ressource. `let` par défaut.
- Une structure portant une référence modifiable n'est ni valeur ni référence : garder l'objet immuable, ou le cacher derrière une **copie à l'écriture** (unicité vérifiée avant modification).
- Plusieurs booléens et optionnels exclusifs deviennent un `enum` : états impossibles inexprimables, changement atomique.
- Types **non copiables** (`~Copyable`) pour une propriété unique (descripteur, virement) ; méthode finale `consuming` ; paramètres `borrowing`, `consuming`, `inout`.

## 3. Erreurs et optionnels

Récupérable → `throw` ; erreur de programmation → `precondition`. Erreurs en `enum` à valeurs associées. `guard` pour sortir, `if let` sinon. Erreurs typées pour le code interne ou contraint, `throws` simple en API publique. Déballage forcé seulement avec invariant énoncé.

## 4. Concurrence : rester sur un seul fil tant que la mesure ne dit pas autre chose

Progression sans saut : 1) tout sur l'acteur principal ; 2) `async`/`await` pour masquer une latence (réseau, disque) ; 3) `@concurrent` pour déplacer **son propre** calcul lourd, après qu'Instruments a montré un blocage ; 4) `actor` pour sortir de l'**état** de l'acteur principal quand les allers-retours deviennent trop nombreux.

- Réglages : « Approachable Concurrency » partout ; isolation par défaut sur l'acteur principal pour les modules d'application et d'interface ; **pas** pour une bibliothèque générique, dont les API restent `nonisolated`.
- Depuis Swift 6.2, **`async` ne déplace pas** une fonction hors de l'acteur appelant. `@concurrent` bascule toujours vers le réservoir parallèle ; `nonisolated` s'exécute là où on l'appelle (bon défaut d'une bibliothèque).
- Chaque `await` est un point de suspension qui rompt l'atomicité : revérifier ses hypothèses après, ne jamais garder un verrou ni s'appuyer sur un stockage local au fil à travers.
- **Réentrance des acteurs** : exclusion mutuelle, pas transaction. État modifié dans des méthodes synchrones, cohérent à chaque `await` ; revérifier un cache après l'attente ou dédoublonner. Les acteurs ne sont pas FIFO.

## 5. `Sendable` et partage

- Types valeur `Sendable` si leur stockage l'est (inféré pour les types non publics ; à écrire pour les publics, c'est une promesse). Acteurs et classes de l'acteur principal le sont implicitement.
- Classes de modèle ni `@MainActor` ni `Sendable`, volontairement ; un objet non `Sendable` peut être transmis si l'émetteur cesse de l'utiliser.
- `@unchecked Sendable` et `nonisolated(unsafe)` : seulement avec une vraie synchronisation interne, jamais pour faire taire un avertissement.
- Face à une erreur de concurrence : 1) ne pas partager (copie locale par tâche, la solution la plus fréquente) ; 2) type valeur `Sendable` ; 3) isoler sur un acteur ; 4) seulement ensuite `Mutex`/`Atomic`. Variables globales : `let`, puis acteur principal, puis `Mutex`.

## 6. Concurrence structurée

- `async let` pour un nombre fixe d'enfants ; groupe de tâches pour un nombre variable (groupe « sans résultat » quand les enfants ne rendent rien) ; `Task {}` seulement quand la durée de vie ne tient pas dans une portée (rappel, appui) ; `Task.detached` presque jamais.
- Annulation coopérative : vérifier avant tout travail coûteux ; le gestionnaire d'annulation s'exécute en parallèle du corps.
- **Borner** le parallélisme : N enfants, un nouveau à chaque fin.
- Continuations : reprendre **exactement une fois** sur chaque chemin.

## 7. SwiftUI

- Les vues et leur état sont sur l'acteur principal : annotations superflues avec l'isolation par défaut.
- Certaines fermetures (effets visuels, géométrie, mise en page) s'exécutent hors du fil principal : y copier la seule valeur utile plutôt que capturer `self`.
- Les rappels d'action sont synchrones à dessein : l'animation déclenchée par un geste part dans la même image ; la `Task` ne porte que le travail long qui suit. Mouvement : `mouvement-interface/references/mouvement-fluide-apple.md`.

## 8. Protocoles et génériques

- Ni classe ni protocole d'emblée : types concrets, puis code répété, puis protocole, puis générique.
- Protocole sans personnalisation : extension contrainte à la place. Préférer « possède » à « est ». Composition plutôt qu'héritage. Un transtypage forcé signale une relation de types perdue.
- Une exigence de protocole est un point de personnalisation (répartition dynamique) ; une méthode seulement en extension est statique et se fait masquer.
- `some P` par défaut ; `any P` pour stocker des types hétérogènes, avec son coût (types associés effacés, optimiseur aveugle). Méthode à type associé inappelable sur `any P` : passer l'existentiel à une fonction `some P`. Types associés primaires sur ses protocoles pour ce que l'appelant fournit.

## 9. Conception d'API

Clarté au point d'usage : pas de préfixe de type ni de `get` en tête ; accès explicite aux frontières ; états illégaux inexprimables ; macros seulement pour le code que le compilateur pourrait écrire.

## 10. Performance

Algorithme d'abord : `remove(at:)` en boucle est quadratique, `removeAll(where:)` linéaire ; les chaînes `map`/`filter` allouent un tableau par étape. Puis mesure (Time Profiler et Allocations d'Instruments lancés sur un test) : `memmove` = copies accidentelles ; millions d'allocations = tableaux intermédiaires ; `swift_beginAccess` = contrôles d'exclusivité ; `retain`/`release` = trafic de comptage. Leviers : `final` et optimisation du module entier ; grosses structures à copie à l'écriture ; `[Modèle]` homogène plutôt que `[any Modèle]` ; `InlineArray` et `Span` (6.2) à la place des tampons non sûrs ; pas d'`async` sans attente ; regrouper les passages par l'acteur principal.

## 11. Cycle de vie et ARC

La durée de vie garantie finit au dernier usage : rien ne dépend du moment d'un `deinit` (pas d'effet de bord, `defer` au site d'appel). `weak`/`unowned` seulement pour casser un cycle ; mieux, ne pas le créer.

## 12. Tests, macros, journaux

- **Swift Testing** par défaut ; XCTest seulement pour l'automatisation d'interface, les mesures de performance et l'Objective-C. `#expect` sur des expressions ordinaires ; `try #require` pour arrêter et déballer ; suites en `struct` (instance neuve par test) ; tests paramétrés plutôt que boucles ; traits pour conditions, anomalies suivies, étiquettes, durée ; problème connu plutôt que test désactivé. Exécution parallèle et ordre aléatoire : corriger les dépendances cachées. Rattacher aux identifiants `CT-` de la recette.
- **Macros** : testées comme transformations d'arbre, avec diagnostics explicites.
- **Journaux** : `Logger` d'`os`, pas `print` ; valeurs non numériques masquées par défaut, `public` seulement pour ce qui n'est pas personnel, empreinte pour corréler (cohérent avec `confidentialite-traces`) ; niveaux choisis selon la persistance ; identifiant de corrélation.

## 13. Code non sûr, syntaxe récente, migration

- « Non sûr » veut dire comportement indéfini si la précondition est violée. `Span` plutôt que pointeurs ; sinon région minimale, pointeurs de tampon, pas d'échappement, Address Sanitizer ; sécurité mémoire stricte dans les modules sensibles.
- Formes récentes : `if`/`switch` en expression, paquets de paramètres, `@Observable`, Swift Regex avec analyseurs de Foundation et locale explicite.
- Migration vers Swift 6, dans l'ordre : compiler avec le nouveau compilateur ; par cible, contrôles complets en avertissement, couche d'interface d'abord ; corriger les causes racines les moins chères ; passer la cible en mode Swift 6 ; cible suivante ; refactoriser **ensuite**, séparément.

## 14. Accessibilité et RTL

- Mouvement : lire la préférence de mouvement réduit de l'environnement SwiftUI et remplacer glissements et ressorts par des fondus.
- Texte dynamique : polices de style, mises en page qui suivent les grandes tailles.
- VoiceOver : libellés, valeurs et actions d'accessibilité sur les commandes personnalisées et les gestes.
- RTL : `leading`/`trailing` plutôt que gauche/droite, icônes directionnelles inversées, vérifier la direction de mise en page en arabe.

## 15. Contrôles avant de rendre

- [ ] Version de la chaîne d'outils vérifiée ; aucune fonction 6.4 sur une cible 6.3.
- [ ] Types valeur par défaut ; chaque classe, `any`, `actor` ou `Unsafe` justifié.
- [ ] Concurrence introduite seulement après mesure ; aucun `@unchecked Sendable` de complaisance.
- [ ] Tâches structurées et bornées ; continuations reprises une fois.
- [ ] Tests en Swift Testing rattachés aux `CT-` ; journaux sans donnée personnelle en clair.
- [ ] Mouvement réduit, texte dynamique, VoiceOver, RTL.

## Origine

Méthode reformulée en français (forme A, `robustesse-agents/references/renfort-externe.md`), sans texte copié ni exemple de code repris, d'après https://github.com/emilkowalski/skills (licence MIT, © 2026 Emil Kowalski), commit `c8a7962`. Fichier lu : `skills/write-swift/SKILL.md`. Exclus : « Initial Response », code, tableau de référence rapide ; section 14 ajoutée par Dan-Cortex. Fiche : `references/sources/renfort-github.md`.
