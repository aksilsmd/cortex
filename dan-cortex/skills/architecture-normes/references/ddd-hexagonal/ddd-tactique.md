# DDD tactique : les briques du modèle

> Traduit et adapté de `ccheney/robust-skills`, `skills/clean-ddd-hexagonal/references/DDD-TACTICAL.md`, commit `0eea7b060d12`. © 2026 robust-skills contributors, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire pour modéliser ou relire un agrégat. Le code est un pseudo-code neutre : adapter constructeurs, génériques et gestion d'erreurs au langage retenu par l'ADR du projet. Exemple fil rouge : une commande Parapro (hypothèse d'illustration).

Sources d'origine : Eric Evans, *Domain-Driven Design* (2003) ; Vaughn Vernon, *Implementing Domain-Driven Design* (2013) et *Effective Aggregate Design* (2011) ; Martin Fowler, motif Repository (*PoEAA*).

## Sommaire
1. Entité
2. Objet-valeur
3. Agrégat
4. Dépôt
5. Événement de domaine
6. Service de domaine
7. Fabrique
8. Spécification
9. Contrôles avant de rendre

## 1. Entité

Objet doté d'une **identité** qui dure. Deux entités sont égales si elles ont la même identité, quelles que soient leurs valeurs. Elle a un identifiant unique, change d'attributs sans changer d'identité, et porte du comportement, pas seulement des données.

```
classe LigneCommande étend Entité<IdLigne> :
    idProduit : IdProduit ; quantité : Quantité ; prixUnitaire : Montant
    créer(idProduit, quantité, prix) -> nouvelle LigneCommande(IdLigne.générer(), ...)
    augmenterQuantité(n) : quantité = quantité.ajouter(n)
    sousTotal() -> prixUnitaire.multiplier(quantité.valeur)
```

## 2. Objet-valeur

Objet défini par ses **attributs**, sans identité : immuable, égalité par valeur, valide dès sa création, méthodes sans effet de bord.

| Objet-valeur | Attributs | Validation |
|---|---|---|
| Montant | valeur, devise | valeur ≥ 0 ; devise admise (DZD) |
| Courriel | adresse | format valide, normalisée en minuscules |
| Adresse | rue, commune, wilaya, pays | champs obligatoires |
| Période | début, fin | début ≤ fin |
| Quantité | valeur | valeur > 0 |

```
classe Montant :
    créer(valeur, devise) : garde valeur >= 0 ; garde devise admise
    ajouter(autre) : garde même devise -> Montant.créer(valeur + autre.valeur, devise)
    multiplier(facteur) -> Montant.créer(valeur * facteur, devise)
```

Un identifiant (`IdCommande`) est lui aussi un objet-valeur : `générer()` et `depuis(texte)` avec garde « non vide ».

## 3. Agrégat

Grappe d'entités et d'objets-valeurs modifiée comme un tout ; c'est une **frontière de cohérence**.

Règles :
1. Une seule racine, seul point d'entrée des modifications.
2. Les autres agrégats sont référencés **par identifiant**, jamais par objet.
3. Préférer un agrégat par transaction ; examiner les besoins explicites d'atomicité entre agrégats avant de choisir la cohérence à terme.
4. L'agrégat garantit ses propres invariants.
5. Petit plutôt que gros.

Dimensionner d'après les invariants et la contention constatée, pas d'après un seuil d'entités, de lignes ou de temps. Un gros agrégat mérite un examen, pas forcément un découpage ; un découpage doit préserver l'atomicité exigée. Questions : des parties peuvent-elles être cohérentes à terme ? (agrégats séparés) Tout change-t-il ensemble ? (même agrégat) Les cycles de vie sont-ils indépendants ? (séparés)

Bon : `Commande` (avec ses lignes) référence `Client` et `Produit` par identifiant. Mauvais : une « commande-dieu » qui embarque client, produits et adresse : trop de raisons de changer, conflits d'accès.

```
classe Commande étend RacineAgrégat<IdCommande> :
    idClient ; lignes ; statut ; adresseLivraison ; créeLe ; événements = [] ; version
    créer(idClient) : statut = BROUILLON ; ajouter événement CommandeCréée
    reconstituer(...)   # depuis la persistance, sans événement
    ajouterLigne(idProduit, quantité, prix) :
        garde statut hors {ANNULÉE, EXPÉDIÉE} ; garde quantité > 0
        fusionner avec la ligne du même produit, sinon créer ; événement LigneAjoutée
    confirmer() : garde statut = BROUILLON ; garde lignes non vides ; garde adresse présente
        statut = CONFIRMÉE ; événement CommandeConfirmée(total)
    expédier(suivi) : garde statut = CONFIRMÉE ; statut = EXPÉDIÉE ; événement CommandeExpédiée
    annuler(motif) : garde statut hors {EXPÉDIÉE, LIVRÉE} ; statut = ANNULÉE ; événement CommandeAnnulée
    total() -> somme des sousTotal()
```

Chaque garde correspond à une règle `RG-` de la spécification ; la citer en commentaire.

## 4. Dépôt

Accès de type collection aux agrégats ; masque la persistance.

1. Un dépôt par agrégat, pas par entité ni par table.
2. Interface dans le domaine, implémentation dans l'infrastructure.
3. Charge et enregistre l'agrégat entier.
4. Pas de logique de requête : les recherches complexes vont dans un modèle de lecture séparé.

```
interface DépôtCommandes : parId(id) ; enregistrer(commande) ; supprimer(commande) ; prochainId()
interface LectureCommandes : parStatut(s) ; parPériode(début, fin) ; compterParClient(id)   # renvoie des DTO
```

Erreurs fréquentes : un `DépôtLignesCommande` (dépôt par entité) ; des méthodes `parStatut`, `compterParClient` dans le dépôt d'écriture.

## 5. Événement de domaine

Trace un fait marquant du domaine : immuable, nommé au passé (`CommandeValidée`, pas `ValiderCommande`), porte les données utiles aux consommateurs, un identifiant et la date de survenue.

```
classe abstraite ÉvénementDomaine : idÉvénement = UUID ; survenuLe = maintenant ; type ; versCharge()
classe CommandeConfirmée : type = "commande.confirmée" ; idCommande ; total
```

## 6. Service de domaine

Opération sans état qui n'a sa place ni dans une entité ni dans un objet-valeur : elle met en jeu plusieurs agrégats, demande une information externe, ou porte une règle notable qui n'appartient à aucune entité.

```
interface Tarification : calculerRemise(commande, client) -> Montant
    # exemple : 5 % au-delà de 10 articles, 10 % client fidèle, plafond 20 % du total
interface FraisLivraison : calculer(lignes, destination) -> Montant
```

Les taux et barèmes viennent du paramétrage du projet, jamais codés en dur.

## 7. Fabrique

Encapsule une création complexe : invariants à faire respecter dès la création, graphe d'objets à construire.

```
FabriqueCommandes.depuisPanier(panier, client) :
    garde panier non vide
    commande = Commande.créer(client.id)
    pour chaque article : commande.ajouterLigne(...)
    si client.adresseParDéfaut : commande.fixerAdresse(...)
```

## 8. Spécification

Règle métier combinable, pour valider ou sélectionner : `estSatisfaitePar(candidat)`, `et`, `ou`, `non`.

```
livraisonOfferte = CommandeAuMoins(Montant.créer(seuil, "DZD")).et(CommandeNonVide())
si livraisonOfferte.estSatisfaitePar(commande) : appliquerLivraisonOfferte()
```

## 9. Contrôles avant de rendre

- Chaque agrégat a une racine, des références par identifiant et des invariants rattachés à des `RG-`.
- Aucun objet-valeur remplacé par un type primitif pour un montant, une quantité ou une adresse.
- Un dépôt par racine ; aucune requête de lecture dans le dépôt d'écriture.
- Les invariants modifiés sont couverts par des tests de domaine sans infrastructure.
