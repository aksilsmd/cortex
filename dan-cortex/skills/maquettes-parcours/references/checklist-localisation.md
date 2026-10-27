# Contrôles — contenu, localisation, culture, éthique d'interface

Un contrôle par ligne. Colonnes imposées ; voir `lancer-projet/references/dossier-projet.md` pour les étiquettes.

| ID | Jalon | Criticité | Types | Conditions | Contrôle | Preuve attendue | Référence |
|---|---|---|---|---|---|---|---|
| LOC-001 | J3 | majeur | tous | - | La voix, le ton et le lexique du produit sont documentés, avec un exemple de formulation à suivre et à éviter | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-002 | J3 | majeur | tous | multilingue | Toutes les chaînes de l'interface sont externalisées avec une clé, un contexte pour le traducteur et aucune concaténation | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-003 | J3 | majeur | tous | multilingue | Un format de messages unique (ICU MessageFormat ou MessageFormat 2) est choisi, et les pluriels suivent les règles CLDR de chaque langue | 03-conception/design/contenu-localisation.md | CLDR 47 |
| LOC-004 | J3 | majeur | tous | multilingue | Dates, nombres, monnaies, téléphones et adresses sont formatés selon la locale par CLDR ou Intl, jamais codés en dur | 03-conception/design/contenu-localisation.md | CLDR 47 |
| LOC-005 | J3 | majeur | tous | multilingue | L'extension des textes traduits est prévue dans les maquettes et vérifiée par pseudo-localisation en recette | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-006 | J3 | bloquant | tous | multilingue | Les langues et les marchés de la première version sont décidés et consignés au registre des décisions | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-007 | J3 | majeur | tous | rtl | Les écrans clés existent en variante de droite à gauche, avec dir, propriétés CSS logiques et seules les icônes directionnelles reflétées | 03-conception/design/maquettes/cahier-maquettes.md | bonne pratique |
| LOC-008 | J5 | majeur | tous | rtl | Les écrans en écriture de droite à gauche sont relus par un locuteur natif, nombres, URL et noms latins isolés compris | 05-validation/pv-recette.md | bonne pratique |
| LOC-009 | J3 | majeur | tous | international | Les hypothèses culturelles par marché sont validées auprès d'au moins cinq utilisateurs locaux avant de figer la direction artistique | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-010 | J3 | majeur | tous | paiement+international | Les moyens de paiement de chaque marché reposent sur des données locales vérifiées et datées, puis sont testés auprès de ce marché | 03-conception/design/contenu-localisation.md | bonne pratique |
| LOC-011 | J3 | bloquant | tous | b2c | Chaque écran a été passé en revue selon les six catégories d'interfaces trompeuses de l'EDPB, et le résultat est consigné | 03-conception/design/contenu-localisation.md | EDPB 03/2022 v2.0 ; DSA art. 25 |
| LOC-012 | J3 | bloquant | tous | abonnement,donnees-perso | Refuser est aussi simple qu'accepter, se désabonner aussi court que s'abonner, et aucune case n'est précochée | 03-conception/design/contenu-localisation.md | EDPB 03/2022 v2.0 ; DSA art. 25 |
| LOC-013 | J3 | majeur | tous | mineurs | Une analyse de risque et une assurance de l'âge conforme aux lignes directrices de la Commission précèdent les réglages protecteurs par défaut | 03-conception/design/contenu-localisation.md | Lignes directrices Commission art. 28 DSA, 14 juillet 2025 |
| LOC-014 | J3 | majeur | ecommerce | b2c | Aucun compte à rebours ni stock fictif n'est affiché, et le prix toutes taxes comprises figure dès la liste de produits | 03-conception/design/contenu-localisation.md | EDPB 03/2022 v2.0 ; bonne pratique |
| LOC-015 | J3 | mineur | tous | - | Les critères UX/UI du RGESN 2024 sont auto-évalués : ni lecture automatique ni défilement infini, poids de page annoncé | 03-conception/design/contenu-localisation.md | RGESN 2024 |
| LOC-016 | J5 | majeur | tous | multilingue | Chaque langue livrée a été relue par un locuteur natif, et les textes juridiques par le juriste, avant la mise en production | 05-validation/pv-recette.md | bonne pratique |
