# Sources

## Dépôt étudié

- Projet : Craft Anything (`storytold/craft-anything`), application Rust en alpha précoce.
- Licence : double licence MIT ou Apache-2.0, au choix. Le nom, le mot-symbole et les logos ArtCraft ne sont pas couverts (fichier de licence de marque du dépôt) ; rien de tel n'est repris ici.
- Commit : `e64d7cb73d7f39323b7040a984e0f9b3f7981146`.
- Forme : **B allégée** (licence permissive) : méthode réécrite avec nos mots ; seuls des noms de commandes et d'options, qui sont des faits, sont cités. Aucun code ni long texte recopié.
- Crédit : projet Craft Anything, copyright 2026 ArtCraft Team et contributeurs, selon son fichier de licence.

## Fichiers lus

- `README.md`, `README.fr.md` : modes, étapes, usage responsable, installation, statut.
- `docs/STATUS.md`, `docs/claude-code.md` : état d'avancement, intégration de l'agent de codage, permissions et approbations.
- `docs/pitfalls.md`, `SECURITY.md`, `CLAUDE.md` : consultés pour le contexte du projet.
- Modules de reconstruction (`crates/ai/src/rebuild/` : `mod.rs`, `study.rs`, `brief.rs`, `check.rs`, `kinds/website.rs`, `kinds/app.rs`, `kinds/game.rs`, `kinds/self_test.rs`, `kinds/mechanics.rs`) : déroulement, règles données au constructeur, mesures de ressemblance, valeurs par défaut des réglages (`crates/engine/src/settings.rs`).

## Ce qui a été retenu

- Le cycle étudier, construire, vérifier, affiner ; le plan par étapes ; les approbations avant exécution ; les questions à l'utilisateur ; les inconnues consignées.
- La distinction des deux modes de l'outil et ses limites.
- Les types de cibles et leurs vérifications ; les réglages par défaut.
- L'avertissement sur l'exécution de code lors de l'installation de dépendances.

## Ce qui n'a pas été retenu

- Les centaines d'outils de rétro-conception (binaires, microprogrammes, bases de données), hors périmètre.
- Les règles d'intégration du dépôt (contribution, publication, traduction).
- L'identité visuelle et les marques du projet.

## Ajouts propres à ce skill

Cadre juridique, séparation des rôles, spécification neutre, journal de provenance et revue juridique ne viennent pas du dépôt : ils sont notre contribution, à faire valider par `juriste-numerique`. Le droit varie selon les pays : à faire vérifier.

## À revérifier

- Toute commande ou option, avant usage réel, sur la version installée.
- Le statut alpha, qui évolue.
- La disponibilité et les signatures des installateurs publiés.
