# Banc avant/après d'un renfort de méthodes

Banc de mesure exigé avant tout lot B (texte tiers traduit) et pour confirmer un lot A (`robustesse-agents/references/renfort-externe.md`, section 5). Trois tâches courtes sur Parapro, jouées deux fois : **avant** (plugin sans les références du renfort) et **après** (avec). Un relecteur distinct de l'auteur des références note les sorties à l'aveugle.

## Sommaire
1. Protocole
2. Tâche 1 : découper DEC-039 en sprints
3. Tâche 2 : corriger un bogue en TDD
4. Tâche 3 : ADR et vue C4 conteneurs, avec parcours BPMN
5. Grille de notation
6. Décision
7. Gabarit du résultat

## 1. Protocole

1. **Deux états du plugin.** « Avant » : copie du plugin dont on retire les fichiers du renfort (`planification-agile.md`, `discipline-realisation.md`, `revue-multi-angles.md`, `c4-ddd-hexagonal.md`, `schemas-mermaid.md`), leurs lignes de renvoi et les lignes « Méthodes : » des agents. « Après » : plugin complet. Le plugin n'étant pas versionné, faire la copie « avant » dans le bloc-notes de session. Retirer aussi `banc-renfort.md` des deux copies jouées : il décrit les défauts plantés.
2. **Mêmes conditions** : même modèle et même effort par agent, même ordre de mission mot pour mot, même budget, mêmes fichiers d'entrée, session neuve pour chaque exécution. L'ordre de mission ne cite aucune référence : il nomme seulement la tâche, les entrées et le livrable. On mesure ce que l'agent trouve et applique de lui-même.
3. **Deux exécutions par état et par tâche** (12 au total), pour lisser la variance ; on retient la moyenne.
4. **Notation à l'aveugle** : les sorties sont renommées `S1` à `S12` par un tiers ; le relecteur (`relecteur-code` ou `auditeur-general`, jamais l'auteur des références) note avec la grille de la section 5 sans savoir quel état a produit quelle sortie.
5. **Coût** : noter pour chaque exécution les tokens consommés (journal des agents) et la durée.
6. **Aucun effet extérieur** : tout se fait dans une copie de travail de Parapro (`code/` copié dans le bloc-notes) ; rien n'est poussé.

## 2. Tâche 1 : découper DEC-039 en sprints

- **Agent** : `planificateur`.
- **Entrées** : `00-pilotage/registres/decisions.csv` (ligne DEC-039), `03-specifications/sfd-v2-commande-catalogue.md` (synthèse et sections 1 à 3), `00-pilotage/planning.md`.
- **Consigne** : « Découpe l'évolution DEC-039 (facettes a à g) en éléments de carnet, estime-les, et propose un plan de sprints de deux semaines pour une équipe de deux développeurs et un testeur, avec une prévision de fin. Livrable : `plan-sprints-dec039.md`. »
- **Attendus observables** :
  - éléments en tranches verticales démontrables seules (pas de « faire la base ») ;
  - estimation relative bornée, rien au-dessus de 13 points ou équivalent, ou découpage justifié ;
  - capacité calculée (focalisation, réserve, jours fériés algériens) et engagement inférieur ou égal à cette capacité ;
  - prévision en fourchette, hypothèses écrites ;
  - chaque élément rattaché à une facette DEC-039 et à des `RG-` ; lien avec les jalons du planning.

## 3. Tâche 2 : corriger un bogue en TDD

- **Agents** : un `developpeur-backend` corrige ; un `relecteur-code` relit la différence (deux exécutions distinctes, notées ensemble).
- **Entrée** : le module fictif ci-dessous, à placer dans une copie de travail avec son test.

```js
// frais-livraison.mjs — fictif, pour le banc
export function fraisLivraison(commande, zones) {
  try {
    const zone = zones.find(z => z.commune === commande.adresse.commune.trim());
    if (commande.mode === "retrait") return 0;
    return zone.frais_centimes + (commande.total_centimes > 500000 ? 0 : 0);
  } catch (e) {
    return 0;
  }
}
```

```js
// frais-livraison.test.mjs
import { test } from "node:test";
import assert from "node:assert/strict";
import { fraisLivraison } from "./frais-livraison.mjs";
const zones = [{ commune: "Azazga", frais_centimes: 30000 }];
test("Azazga paie les frais", () => {
  assert.equal(fraisLivraison({ mode: "domicile", total_centimes: 100000, adresse: { commune: "Azazga" } }, zones), 30000);
});
```

- **Signalement** : « Un client de Tizi Ouzou (hors zone) a pu commander en livraison à domicile avec des frais nuls. Corrige le défaut. » Règle visée : livraison à domicile réservée à Azazga, adresse hors zone refusée (DEC-039/f) ; seuil de gratuité éventuel = hypothèse non décidée.
- **Défauts plantés** (connus du seul tiers qui prépare le banc) : (1) exception avalée qui transforme « zone inconnue » en frais nuls ; (2) casse et espaces non normalisés (« azazga ») ; (3) condition de gratuité morte (`? 0 : 0`) ; (4) test unique sans cas négatif.
- **Attendus observables** :
  - test du symptôme écrit d'abord et vu rouge (sortie jointe), puis vert ;
  - cause racine nommée (exception avalée, pas seulement « ajout d'un `if` ») ;
  - erreur explicite pour adresse hors zone, sans repli silencieux ;
  - preuve de vérification fraîche jointe avant de déclarer « corrigé » ;
  - relecteur : constate l'échec silencieux, le code mort et les cas négatifs manquants, avec gravité.

## 4. Tâche 3 : ADR et vue C4 conteneurs, avec parcours BPMN

- **Agents** : `architecte-solution` (ADR et C4) ; `cartographe-interactions` (parcours).
- **Entrées** : `03-conception/architecture/dossier-architecture.md` (sections 2 à 4), ADR existantes, `03-specifications/sfd-v2-commande-catalogue.md` (paiement à la livraison), arborescence `code/apps` et `code/packages`.
- **Consigne** : « Rédige l'ADR du mode d'envoi du code de double validation (SMS, e-mail, repli) pour le paiement à la livraison, et la vue C4 de niveau 2 de Parapro à jour. Le cartographe produit le processus BPMN léger de la double validation (client, pharmacie, livreur). Livrables : `ADR-banc.md`, `c4-conteneurs-banc.md`, `wf-double-validation-banc.md`. »
- **Attendus observables** :
  - ADR : options comparées, options écartées, conséquences, coût de sortie, forme proportionnée à l'enjeu ;
  - C4 : seulement des conteneurs (pas de composants mêlés), technologie sur chaque nœud, verbe et protocole sur chaque flèche, systèmes externes et frontière visibles, cohérence vérifiée avec `code/apps` et `code/packages` ;
  - BPMN : un couloir par rôle, début et fins nommés, passerelles étiquetées, délai d'expiration explicite, chemins d'erreur (code faux, expiré, refus pharmacie) ;
  - Mermaid rendu localement ou mention « syntaxe non vérifiée » ; aucun service en ligne.

## 5. Grille de notation

Chaque critère se note de 0 à 5 ; la note de la tâche est la moyenne des critères (sur 5). Le relecteur cite pour chaque note la ligne de la sortie qui la justifie.

| Critère | Tâche 1 | Tâche 2 | Tâche 3 |
|---|---|---|---|
| Justesse | tranches et estimations cohérentes avec la SFD | les 4 défauts traités | C4 conforme au code ; ADR exacte |
| Méthode appliquée | découpage vertical, capacité calculée | rouge avant vert, cause racine | règles C4 par niveau ; conventions BPMN |
| Preuves | hypothèses et calculs montrés | sorties rouge, verte, vérification finale | rendu local ou mention ; sources citées |
| Exhaustivité des cas | facettes a à g toutes couvertes | cas négatifs et limites testés | chemins d'erreur, frontières |
| Exploitabilité | un humain peut lancer le sprint 1 | un relecteur peut accepter sans question | l'ADR peut être votée ; le schéma se lit seul |

Barème indicatif : 0 absent ; 1 erroné ; 2 partiel avec erreurs ; 3 correct mais incomplet ; 4 correct et complet ; 5 complet, prouvé, sans retouche nécessaire.

## 6. Décision

- **Gain** = note moyenne « après » − note moyenne « avant », par tâche.
- **Seuil** : gain d'au moins 1 point sur 5 sur au moins deux tâches → lot A confirmé, lot B autorisé dans son périmètre limité.
- Gain inférieur au seuil : lot B non lancé ; références sans gain proposées au retrait (`renfort-externe.md`, section 7).
- Coût : si la consommation de tokens « après » dépasse « avant » de plus de 30 % sans gain, le signaler au bilan.
- Le résultat est tracé au registre des décisions et rapporté à l'utilisateur, décideur final.

## 7. Gabarit du résultat

```markdown
# Résultat du banc de renfort — <date>
## Synthèse (gains par tâche, décision proposée)
## Conditions (modèle, effort, budget, états du plugin)
## Notes par sortie (S1 à S12, critère par critère, justification)
## Moyennes avant/après et gains
## Coût (tokens, durée)
## Décision proposée et réserves
```
