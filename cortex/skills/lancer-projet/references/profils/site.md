# Profil — site web de très grande entreprise (type `site`)

Lu par le chef d'orchestre à J0 pour poser les bonnes questions et composer l'équipe. État : octobre 2026.

## Ce qui distingue ce type de projet

- La difficulté est organisationnelle avant d'être technique : plusieurs sites, domaines, langues, marchés et propriétaires.
- Le marché des plateformes d'expérience numérique (DXP) se recompose : repositionnement « IA et gouvernance » chez plusieurs éditeurs, aucun Magic Quadrant Gartner DXP depuis environ 20 mois. Comparer par essai chiffré, pas par quadrant.
- La migration (URL, SEO, contenus) est le risque technique central.
- Core Web Vitals, mesurés au 75e centile sur données terrain, mobile et ordinateur séparés : LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.

## Étiquettes à poser

`b2b` (souvent), `grand-compte`, `multilingue`, `international` si plusieurs pays, `rtl` si arabe ou hébreu, `donnees-perso` (formulaires, cookies, mesure d'audience), `migration` s'il existe un site, `integrations` (CRM, recherche, personnalisation), `progiciel` si DXP du marché, `code` si développement sur mesure, `secteur-public` selon le client.

## Acheter, configurer ou construire

| Option | À retenir si | Point de vigilance |
|---|---|---|
| Suite DXP (Adobe, Optimizely, Sitecore, Acquia) | beaucoup de sites, personnalisation, équipes marketing nombreuses | dépendance éditeur, licences par site |
| CMS headless (Contentful, Contentstack, Builder.io, Pimcore) | équipe front solide, multi-canaux | la charge se déplace vers le front, la prévisualisation, la personnalisation |
| CMS open source (Drupal, WordPress) | maîtrise du code, budget licence réduit | maintenance et sécurité à charge ; fin de vie de la version : à vérifier |

Critères : TCO sur 5 ans, licences par site, délai de publication, SLA éditeur, qualité du workflow de traduction, intégrabilité. Faire un essai chiffré (PoC) avant sélection. Non documentés : AEM, Sitecore XM Cloud, Strapi ni les tarifs : **à vérifier**.

## Prérequis propres à ce type

1. Inventaire des sites, domaines, langues et propriétaires, avec RACI par marché.
2. Modèle de contenu et design system partagés, validés **avant** le choix de l'outil.
3. Audit et nettoyage des contenus et médias avant reprise.
4. Budget de performance fixé dès le cadrage.

## Agents à renforcer et livrables spécifiques

- `redacteur-contenu-localisation` : workflow de traduction et validation par langue, rôles éditoriaux.
- `expert-accessibilite` : obligation légale probable (RGAA, EAA : à valider par le juriste).
- `analyste-concurrence` et `stratege-produit` : positionnement et périmètre ; `analyste-contexte` si plusieurs pays.
- `architecte-solution` et `integrateur` : choix DXP, intégrations ; `ingenieur-devops` : bascule et retour arrière.
- `expert-acquisition` : table de redirections, SEO de migration, plan de marquage.
- Livrables spécifiques : table de redirections URL, modèle de contenu, budget de performance, plan de gel de contenu.

## Exigences des plateformes et des tiers

- Migration : redirections serveur permanentes (301 ou 308) une à une selon une table d'URL ; contrôler `rel=canonical` et `noindex` après bascule ; erreur fréquente : rediriger vers des URL inexistantes ; vérifier avec Search Console et un crawler (Google Search Central).
- Accessibilité et consentement : hors périmètre, **à valider** par le juriste.

## Pièges et causes d'échec fréquentes

- Migrer sans table de redirections ni contrôle canonical et noindex.
- Choisir l'outil avant le modèle de contenu.
- Sous-estimer la gouvernance et la traduction : à 20 sites ou plus, modèle partagé, workflow de traduction et RACI par marché forment le chemin critique (déduction).
- Ne mesurer les Web Vitals qu'en laboratoire.
- Recherche interne et personnalisation non cadrées (outil, données, consentement, cas d'usage mesurable).
- Oublier le gel de contenu, le retour arrière et le support éditeur le jour J.

## Planning type

Aucune durée type n'est établie. Séquence : inventaire et modèle de contenu → essai chiffré et choix → conception et design system → reprise et traduction des contenus (en parallèle du développement) → recette, performance, redirections → gel, bascule, suivi SEO plusieurs semaines. Chemin critique probable : modèle de contenu, puis traduction et validation éditoriale (hypothèse).

## Sources

- Gartner MQ DXP 2025, via CX Today ; CMSWire, septembre 2026 (repositionnement des éditeurs).
- web.dev, seuils des Core Web Vitals.
- Google Search Central, « site move with URL changes ».
