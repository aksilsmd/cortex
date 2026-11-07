# Architecture hexagonale : ports et adaptateurs en détail

> Traduit et adapté de `ccheney/robust-skills`, `skills/clean-ddd-hexagonal/references/HEXAGONAL.md`, commit `0eea7b060d12`. © 2026 robust-skills contributors, licence MIT (texte complet et liste des modifications : `NOTICE.md` de ce dossier).

À lire pour découper un service en ports et adaptateurs, ou pour relire ce découpage. Le résumé reste `../c4-ddd-hexagonal.md` §7. Sources d'origine : Alistair Cockburn, *Hexagonal Architecture* (2005) ; Cockburn et Garrido de Paz, *Hexagonal Architecture Explained* (2024).

## Sommaire
1. Principe
2. Ports
3. Adaptateurs
4. Asymétrie
5. Nommage
6. Arborescence
7. Changer d'adaptateur par configuration
8. Hexagonal fort ou faible
9. Bénéfices et contrôles

## 1. Principe

Une application doit pouvoir être pilotée indifféremment par des utilisateurs, des programmes, des tests automatiques ou des traitements par lots, et être développée et testée sans ses bases ni ses périphériques réels (idée de Cockburn).

- **Test de validation** : si toute l'application tourne depuis des jeux de tests, sans interface ni base réelle, les frontières sont justes. Les experts métier peuvent écrire des cas avant qu'un écran existe.
- **L'hexagone est symbolique** : la plupart des applications ont 2 à 4 ports, pas 6. La forme rappelle seulement que tout échange externe passe par un port.
- **Propriété** : l'application et le domaine définissent les abstractions dont ils ont besoin ; les adaptateurs techniques les implémentent de l'extérieur. Dans une organisation centrée DDD, l'interface de dépôt d'un agrégat vit à côté de lui dans `domaine/` ; dans une organisation centrée hexagonal, sous `application/ports/sortants/`.

## 2. Ports

Interfaces qui fixent comment l'application communique avec l'extérieur. Un port explicite se justifie par plusieurs adaptateurs, un besoin de test ou une frontière d'équipe ; dans une petite base, la méthode publique d'un cas d'usage suffit comme port entrant.

**Ports entrants (pilotants)** : comment le monde utilise l'application. Points d'entrée appelés par les adaptateurs ; un par cas d'usage.

```
PasserCommande.exécuter(commande : CommandePasserCommande) -> IdCommande
ConsulterCommande.exécuter(requête) -> CommandeDTO | rien
AnnulerCommande.exécuter(commande) -> rien
```

**Ports sortants (pilotés)** : comment l'application utilise les systèmes externes. Besoins de l'application, implémentés par les adaptateurs.

```
DépôtCommandes : parId(id) ; enregistrer(c) ; supprimer(c)
ÉmetteurÉvénements : publier(e) ; publierTous(liste)
PasserellePaiement : débiter(montant, moyen) -> RésultatPaiement ; rembourser(idPaiement, montant)
Notification : envoyerCourriel(à, gabarit) ; envoyerSMS(à, message)
```

## 3. Adaptateurs

**Entrants** : traduisent une entrée externe en appel de port. Un contrôleur HTTP lit la requête, construit `CommandePasserCommande` (identifiant client depuis la session, lignes depuis le corps), appelle le port, répond 201 avec l'identifiant ; 404 si la consultation ne trouve rien. Une commande en ligne, un service gRPC ou un consommateur de file font la même traduction vers le même port.

**Sortants** : implémentent un port avec une technologie.

```
DépôtCommandesSQL implémente DépôtCommandes :
    parId(id) : ligne = base.commandes.où(id) ; rien si absente ; sinon Correspondance.versDomaine(ligne)
    enregistrer(c) : base.commandes.insérerOuMettreÀJour(Correspondance.versPersistance(c))
DépôtCommandesMémoire implémente DépôtCommandes :    # pour les tests
    table en mémoire ; vider()
PasserellePaiementPrestataire implémente PasserellePaiement :
    débiter : appel du prestataire ; refus de carte -> RésultatPaiement.échec(message) ; sinon succès(idPaiement)
ÉmetteurÉvénementsFile implémente ÉmetteurÉvénements :
    publier(e) : envoyer {idÉvénement, type, survenuLe, charge} sur la file
```

Le prestataire de paiement réel et la passerelle SMS sont ceux retenus par l'ADR du projet ; l'adaptateur est le seul endroit qui connaît leur API.

## 4. Asymétrie

- Côté entrant, l'adaptateur **appelle** le port : l'application définit ce qu'elle **offre**.
- Côté sortant, l'adaptateur **implémente** le port : l'application définit ce dont elle **a besoin**.

## 5. Nommage

Proposition de Cockburn : ports en `Pour[Faire][Quelque chose]` (`PourPasserDesCommandes`, `PourStockerLesClients`, `PourNotifierLesAlertes`) ; adaptateurs nommés par leur technologie (`CommandeEnLignePourPasserDesCommandes`, `BaseSQLPourStockerLesClients`).

| Convention | Port | Adaptateur |
|---|---|---|
| Interface / implémentation | `DépôtCommandes` | `DépôtCommandesSQL` |
| Suffixe Port | `PortDépôtCommandes` | `AdaptateurCommandesSQL` |
| Préfixe « avec » | `StockageCommandes` | `StockageCommandesAvecSQL` |

Choisir une convention, l'écrire dans `../normes-developpement.md`, s'y tenir.

## 6. Arborescence

À utiliser pour grouper tous les ports par sens. En organisation DDD, garder les dépôts d'agrégat dans `domaine/<agrégat>/` et réserver `application/ports/sortants/` aux dépendances propres à l'application (paiement, notification, horloge, émetteur d'événements).

```
src/
├── application/
│   ├── ports/entrants/      # passer_commande, consulter_commande, annuler_commande
│   ├── ports/sortants/      # depot_commandes, emetteur_evenements, passerelle_paiement
│   └── cas_usage/           # un dossier par cas, implémente le port entrant
├── infrastructure/adaptateurs/
│   ├── entrants/            # http/, cli/, file/
│   └── sortants/            # sql/, file/, paiement/, memoire/ (tests)
└── domaine/
```

## 7. Changer d'adaptateur par configuration

L'intérêt de l'hexagonal : remplacer un adaptateur sans toucher au cœur. L'assemblage se fait au démarrage, une configuration par environnement :

| Port | Développement | Test | Production |
|---|---|---|---|
| DépôtCommandes | mémoire | mémoire | SQL |
| ÉmetteurÉvénements | mémoire | espion | file de messages |
| PasserellePaiement | factice | simulacre | prestataire réel |

Changer de base revient à lier un autre adaptateur au même port.

## 8. Hexagonal fort ou faible

- **Faible** : le port laisse passer la technologie, par exemple `chercherParRequête(sql, paramètres)`. Le domaine dépend alors de SQL.
- **Fort** : le port ne parle que le langage du domaine, par exemple `parId(id)`, `parClient(idClient)`, `enregistrer(commande)`.

## 9. Bénéfices et contrôles

Bénéfices : testabilité (doublures à la place des vrais adaptateurs) ; souplesse (changer de technologie sans toucher au cœur) ; indépendance (développer le cœur sans systèmes externes) ; frontières explicites ; travail parallèle sur des adaptateurs différents.

Contrôles avant de rendre :
- Aucun port ne mentionne SQL, HTTP, un SDK ni un format de fournisseur.
- Un adaptateur mémoire ou factice existe pour chaque port sortant utilisé en test.
- Chaque adaptateur sortant a un test d'intégration contre la vraie technologie (`../c4-ddd-hexagonal.md` §7).
- La règle « le domaine n'importe pas l'infrastructure » est contrôlée par un outil.
