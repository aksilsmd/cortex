# Production et publication

## Formats
- **EPUB** — standard de l'ebook, texte qui se recompose (*reflowable*) ; EPUB 3 = HTML/CSS + métadonnées (fichier OPF). Format cible par défaut.
- **PDF** — mise en page fixe, imprimable ; pour l'impression pro : format (*trim size*), marges, fonds perdus, dos selon l'épaisseur.
- **MOBI/KF8/AZW** — Kindle, en voie de remplacement par l'EPUB (Amazon via KPF).
- **Source unique → multi-sortie** : écrire en Markdown et générer tous les formats avec pandoc (voir `outils-ecriture.md`).

## Auto-édition vs maison d'édition
- **Maison** : avance éventuelle, travail éditorial/diffusion/distribution pris en charge ; mais cession de droits, délais longs, sélectivité.
- **Auto-édition** : contrôle total, royalties plus élevées (KDP, Kobo, agrégateur Draft2Digital) ; mais édition, couverture et promotion à la charge de l'auteur.
- **Hybride** possible.

## Métadonnées (découvrabilité)
Titre et sous-titre, auteur, description, **catégories BISAC**, mots-clés, langue, date, prix, série. Portées par l'EPUB (OPF) et les fiches des plateformes. Déterminantes pour être trouvé.

## Couverture
Doit se lire en vignette et signaler le genre ; titre lisible. Pour l'imprimé : dos (épaisseur selon pages/papier), 4ᵉ de couverture, fonds perdus.

## ISBN (notions)
Identifiant à 13 chiffres, **un par format** (EPUB, broché…). Attribué par l'agence nationale : en France **AFNIL** (gratuit), aux USA Bowker (payant). Facultatif sur certaines plateformes (Amazon fournit un ASIN) mais recommandé pour la distribution large et le dépôt légal. Ne pas confondre avec le code-barres EAN.

Sources : spécification EPUB 3 (w3.org), kdp.amazon.com, draft2digital.com, afnil.org, bisg.org (BISAC).
