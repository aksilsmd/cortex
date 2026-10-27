# Inventaire des écrans et matrice d'interactions

But : qu'après lecture, personne n'ait à deviner ce qui se passe quand on clique. Le format des deux tableaux est
**imposé** : le script `cortex.py interactions verifier` les lit tels quels.

## Sommaire
1. L'inventaire des écrans
2. La matrice d'interactions
3. Ce que le script contrôle
4. Méthode pour ne rien oublier
5. Exemple complet : la connexion
6. Lien avec les tests

## 1. L'inventaire des écrans

Fichier unique : `03-conception/design/interactions/ecrans.md`. Une ligne par écran, modale, panneau ou étape
d'un assistant. Sept colonnes, dans cet ordre :

```markdown
| ID | Écran | Type | Rôles | Entrée | Terminal | États couverts |
|---|---|---|---|---|---|---|
| EC-001 | Connexion | page | visiteur | oui | non | chargement, erreur, succès |
```

| Colonne | Valeurs |
|---|---|
| ID | `EC-` suivi de trois chiffres, unique dans tout le projet |
| Écran | nom court et stable, celui des maquettes |
| Type | `page`, `modale`, `panneau`, `étape`, `e-mail`, `notification`, `statique`, `externe` |
| Rôles | qui peut y accéder : visiteur, utilisateur, administrateur… |
| Entrée | `oui` si l'on peut y arriver sans passer par un autre écran (adresse directe, lien d'e-mail, ouverture de l'application) |
| Terminal | `oui` si l'écran n'appelle aucune action (confirmation finale, page d'erreur définitive) |
| États couverts | parmi `chargement`, `vide`, `erreur`, `succès`, `partiel`, `hors-ligne`, `non autorisé` ; `n/a` pour un écran sans donnée |

Tout écran de type `page`, `panneau` ou `étape` qui affiche des données doit couvrir au moins `chargement` et
`erreur`, et `vide` s'il affiche une liste.

## 2. La matrice d'interactions

Un fichier par module : `03-conception/design/interactions/<module>.md`. Une ligne par élément interactif et par
action. Neuf colonnes, dans cet ordre :

```markdown
| ID | Élément | Type | Action | Conditions | Réaction du système | Destination | Erreurs et états | Workflow |
|---|---|---|---|---|---|---|---|---|
| EL-001-01 | Bouton « Se connecter » | bouton | clic | e-mail et mot de passe saisis | vérifie les identifiants, ouvre la session, journalise | EC-002 (succès) / EC-001 (échec) | message générique « identifiants incorrects » ; blocage temporaire après 5 échecs | WF-001 |
```

| Colonne | Contenu |
|---|---|
| ID | `EL-<numéro de l'écran>-<rang>` : `EL-001-03` est le troisième élément de l'écran `EC-001` |
| Élément | le libellé exact entre guillemets et sa nature : Bouton « Payer », Lien « Mot de passe oublié », Champ « E-mail », Ligne de tableau, Glisser vers la gauche |
| Type | `bouton`, `lien`, `champ`, `case`, `liste`, `onglet`, `menu`, `ligne`, `carte`, `geste`, `raccourci`, `automatique` (minuterie, arrivée d'une notification) |
| Action | `clic`, `double clic`, `saisie`, `validation`, `survol`, `appui long`, `glissement`, `touche Entrée`, `perte de focus`, `délai` |
| Conditions | état requis, rôle, validité des champs ; `-` si aucune. Dire aussi quand l'élément est masqué ou désactivé |
| Réaction du système | ce que fait le système, dans l'ordre : contrôle, appel, écriture, envoi, retour visuel. Jamais vide |
| Destination | `EC-xxx` ; plusieurs destinations séparées par ` / ` avec leur cas entre parenthèses ; `même écran` ; `retour` (écran précédent) ; `ferme` (ferme la modale) ; `externe : <description>` |
| Erreurs et états | messages d'erreur exacts, comportement hors-ligne, délai dépassé, double clic, droits insuffisants |
| Workflow | le ou les `WF-` auxquels l'interaction appartient |

Ne pas mettre de barre verticale dans une cellule. Un élément qui réagit à deux actions (clic et appui long) a
deux lignes.

## 3. Ce que le script contrôle

`python3 <skill lancer-projet>/scripts/cortex.py interactions verifier`

**Erreurs, à corriger avant le jalon J3 :**

- identifiant en double ;
- élément rattaché à un écran absent de l'inventaire ;
- réaction ou destination vide, `-`, `?` ou « à définir » ;
- destination vers un écran non défini ;
- **cul-de-sac** : écran non terminal sans aucun élément interactif ;
- **écran orphelin** : écran qui n'est pas une entrée et vers lequel rien ne mène ;
- écran inatteignable depuis les points d'entrée ;
- aucun point d'entrée.

**Alertes, à traiter ou justifier :** état `chargement` ou `erreur` non couvert ; élément sans workflow.

`cortex.py interactions graphe` écrit `navigation.md`, la carte de navigation en Mermaid, à joindre aux
maquettes.

## 4. Méthode pour ne rien oublier

Parcourir chaque écran avec cette liste, dans l'ordre :

1. **Ce qui se voit** : chaque bouton, lien, champ, onglet, menu, icône cliquable, ligne de liste, pagination,
   tri, filtre, recherche.
2. **Ce qui ne se voit pas** : touche Entrée et Échap, retour du navigateur ou du téléphone, glissements, appui
   long, raccourcis, clic en dehors d'une modale, rafraîchissement.
3. **Ce qui arrive tout seul** : expiration de session, minuterie, notification entrante, perte de connexion,
   mise à jour en temps réel.
4. **Ce qui est commun à tous les écrans** : en-tête, menu, pied de page, sélecteur de langue, bandeau de
   consentement. Le décrire une fois dans un module `commun.md` rattaché à un écran `EC-000 Gabarit commun`,
   déclaré de type `statique`, Entrée `oui`, États `n/a` : sans cela le script le signale comme orphelin.
5. **Chaque rôle** : ce qui est masqué, désactivé ou différent pour chaque rôle.
6. **Chaque état** : que peut-on faire sur l'écran vide, en erreur, en chargement ?
7. **Les sorties** : annuler, fermer, revenir, abandonner en cours de saisie (données conservées ou perdues ?).

Puis lancer le script. Tant qu'il signale une erreur, le module n'est pas fini.

## 5. Exemple complet : la connexion

Inventaire :

```markdown
| ID | Écran | Type | Rôles | Entrée | Terminal | États couverts |
|---|---|---|---|---|---|---|
| EC-001 | Connexion | page | visiteur | oui | non | chargement, erreur, succès |
| EC-002 | Tableau de bord | page | utilisateur | non | non | chargement, vide, erreur |
| EC-003 | Mot de passe oublié | page | visiteur | non | non | chargement, erreur, succès |
| EC-004 | Lien envoyé | page | visiteur | non | non | n/a |
| EC-005 | Création de compte | page | visiteur | oui | non | chargement, erreur, succès |
```

Matrice :

```markdown
| ID | Élément | Type | Action | Conditions | Réaction du système | Destination | Erreurs et états | Workflow |
|---|---|---|---|---|---|---|---|---|
| EL-001-01 | Champ « E-mail » | champ | perte de focus | - | contrôle le format | même écran | « Saisissez une adresse e-mail valide » sous le champ | WF-001 |
| EL-001-02 | Champ « Mot de passe » | champ | saisie | - | masque les caractères | même écran | - | WF-001 |
| EL-001-03 | Icône « Afficher le mot de passe » | bouton | clic | - | affiche ou masque le mot de passe ; l'état est annoncé aux lecteurs d'écran | même écran | - | WF-001 |
| EL-001-04 | Bouton « Se connecter » | bouton | clic | les deux champs remplis, sinon désactivé | vérifie les identifiants, ouvre la session, journalise la connexion | EC-002 (succès) / EC-001 (échec) | « Identifiants incorrects » sans dire lequel ; blocage 15 min après 5 échecs ; bouton inactif pendant l'appel ; « Connexion impossible, réessayez » si le service ne répond pas | WF-001 |
| EL-001-05 | Touche Entrée dans un champ | raccourci | touche Entrée | les deux champs remplis | même réaction que le bouton « Se connecter » | EC-002 (succès) / EC-001 (échec) | identiques à EL-001-04 | WF-001 |
| EL-001-06 | Lien « Mot de passe oublié » | lien | clic | - | ouvre le formulaire, reporte l'e-mail déjà saisi | EC-003 | - | WF-002 |
| EL-001-07 | Lien « Créer un compte » | lien | clic | - | ouvre la création de compte | EC-005 | - | WF-003 |
| EL-003-01 | Bouton « Envoyer le lien » | bouton | clic | e-mail au bon format | envoie un lien valable 30 minutes si le compte existe | EC-004 | même message que le compte existe ou non ; limite de 3 demandes par heure | WF-002 |
| EL-003-02 | Lien « Retour à la connexion » | lien | clic | - | revient sans rien enregistrer | EC-001 | - | WF-002 |
| EL-004-01 | Lien « Retour à la connexion » | lien | clic | - | revient à la connexion | EC-001 | - | WF-002 |
```

Les éléments des écrans `EC-002` et `EC-005` suivent dans leur propre module.

## 6. Lien avec les tests

La matrice est le modèle dont on dérive les tests de bout en bout :

- chaque ligne est une transition ; chaque transition doit être parcourue par au moins un cas de test ;
- chaque valeur de la colonne « Erreurs et états » donne un cas de test négatif ;
- le cahier de recette cite les `WF-` et, pour les cas ciblés, les `EL-` qu'il couvre.
  `cortex.py tracabilite verifier` signale les éléments dont ni l'identifiant ni le workflow n'apparaît dans un
  cas de test.
