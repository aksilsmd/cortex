# Cadre juridique et éthique (forme générale)

Cette fiche pose des principes. Elle n'est pas un avis juridique. Le droit varie selon les pays (droit d'auteur, bases de données, concurrence déloyale, marques, contrats, accès aux systèmes) : tout cas réel est **à faire vérifier** par `${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md` et l'agent `juriste-numerique`. Les règles de l'Algérie, de la France et de l'Union européenne ne sont pas identiques ; ne rien supposer.

## Ce qu'on peut reprendre

- Les **fonctions** : ce que fait le produit (rechercher, trier, réserver, payer).
- Les **parcours** : l'enchaînement général des étapes pour atteindre un but.
- Les **idées et règles générales** : principes de fonctionnement, limites métier courantes.
- Les **conventions d'usage** répandues (un panier, une barre de recherche, un menu).

En général, les idées et les méthodes ne sont pas protégées en tant que telles, mais leur expression l'est, et certaines combinaisons ou pratiques peuvent tomber sous d'autres régimes. D'où la revue juridique.

## Ce qu'on ne reprend jamais

| élément | pourquoi | que faire à la place |
|---|---|---|
| code source (y compris code rendu lisible, scripts, feuilles de style) | droit d'auteur | écrire son propre code depuis la spécification |
| textes, slogans, descriptions | droit d'auteur | rédiger ses propres textes |
| images, illustrations, photos, icônes sous licence | droit d'auteur | contenus propres, libres de droits ou générés avec droits clairs |
| sons, musiques, voix | droit d'auteur et droits voisins | contenus propres |
| polices sous licence | licence | polices libres, licence vérifiée |
| marque, nom, logo | droit des marques | nom et identité propres |
| charte graphique reconnaissable (combinaison couleurs, formes, ambiance) | confusion, concurrence déloyale | charte propre, distincte |
| bases de données et contenus agrégés | droit des bases de données | données propres |

Règle pratique : si un visiteur peut confondre le résultat avec l'original, c'est trop proche.

## Limites de l'étude

- **Conditions d'utilisation** du site ou de l'application : les lire avant d'observer ; certaines interdisent l'extraction automatisée ou la rétro-conception. Si elles l'interdisent, ne pas étudier sans accord écrit du titulaire.
- **`robots.txt`** : le respecter pour toute exploration automatisée ; ne pas l'utiliser comme une autorisation générale, il ne remplace pas les conditions.
- **Protections** : aucun contournement d'identification, de gestion des droits numériques (DRM), d'anti-triche, de limitation de débit, de chiffrement. Une archive fermée reste fermée.
- **Données personnelles** : ne pas en collecter. Si une capture en contient par accident, la masquer ou la détruire, et appliquer `${CLAUDE_SKILL_DIR}/../confidentialite-traces/SKILL.md` ; consulter `delegue-protection-donnees` si un traitement est envisagé.
- **Zones authentifiées** : pas d'étude sans droit explicite (compte à soi, accord du titulaire). Les parties publiques seules par défaut.
- **Charge** : observer à un rythme raisonnable, sans nuire au service.
- **Analyse interne du code** (lecture des scripts, décompilation) : à réserver à un logiciel dont l'utilisateur est titulaire ou pour lequel il a un droit écrit. Sur un tiers, hors périmètre de ce skill.

## Si quelque chose est copié par erreur

1. Le retirer immédiatement de la sortie et de l'historique de versions si publié.
2. Le consigner dans le journal de provenance (quoi, où, quand, par qui, correction).
3. Chercher la cause dans le processus (spécification non neutre, séparation rompue) et la corriger.
4. Prévenir `juriste-numerique` si la sortie a déjà été diffusée.

## Éthique

- Dire à l'utilisateur ce qui est fait, avec quoi, et à quel coût, avant de le faire.
- Ne pas présenter un produit comme celui de la cible, ni suggérer un lien avec elle.
- Préférer la différenciation : la reconstruction sert à comprendre un besoin, pas à rejouer un concurrent.
- Toute étude d'une cible implique une personne responsable nommée dans la fiche cible.

## Étapes juridiques dans la méthode

| étape | contrôle juridique |
|---|---|
| fiche cible | droits, conditions d'utilisation, `robots.txt`, pays |
| observation | périmètre public, pas de contournement, pas de données personnelles |
| spécification | neutralité (aucune expression protégée) |
| construction | contenus et dépendances sous licences claires |
| vérification | plafond de ressemblance sur les contenus |
| publication | revue juridique complète, avis ou « à faire vérifier » |
