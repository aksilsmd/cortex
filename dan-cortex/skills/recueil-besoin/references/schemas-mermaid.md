# Schémas en Mermaid (texte rendu ensuite)

Mermaid (MIT) écrit des diagrammes en texte, versionnables, rendus en image. On produit le texte ; le rendu se fait avec `mmdc` (déjà présent dans l'environnement) ou un aperçu. Pour des schémas plus riches à éditer à la main : draw.io (Apache-2.0) ; pour des wireframes peu intimidants : Excalidraw (MIT) ; pour des maquettes fidèles : Penpot (MPL-2.0).

## Parcours utilisateur (flowchart)
```mermaid
flowchart TD
  A[Arrivée] --> B{Connecté ?}
  B -- non --> C[Connexion / inscription]
  B -- oui --> D[Accueil]
  C --> D
  D --> E[Action principale]
  E --> F[Confirmation]
```

## Modèle de données (entité-association)
```mermaid
erDiagram
  CLIENT ||--o{ COMMANDE : passe
  COMMANDE ||--|{ LIGNE : contient
  PRODUIT ||--o{ LIGNE : figure_dans
  CLIENT {
    string nom
    string email
    string role
  }
  COMMANDE {
    date date
    string statut
  }
```

## Enchaînement des écrans
```mermaid
flowchart LR
  Accueil --> Liste --> Fiche --> Panier --> Paiement --> Confirmation
```

## Architecture (blocs)
```mermaid
flowchart TB
  U[Navigateur / mobile] --> S[Application]
  S --> BD[(Base de données)]
  S --> X[Services externes]
```

Règles : un schéma répond à une question (parcours, données, écrans, architecture) ; on le montre à la personne et on le fait valider ; on garde le texte source dans le dossier pour pouvoir le modifier.
