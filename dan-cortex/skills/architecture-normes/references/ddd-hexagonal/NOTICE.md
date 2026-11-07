# NOTICE — références DDD et hexagonal (lot B, forme B limitée)

Dossier vendorisé dans Dan-Cortex le 2026-11-03, décision « renfort GitHub » (projet Parapro, DEC-042, PV du 2026-11-03, lot 5), après banc favorable (`banc-resultats.md`). Propriétaire : architecte-solution. Mise à jour : `robustesse-agents/references/renfort-externe.md` §6.

| Champ | Valeur |
|---|---|
| Dépôt amont | https://github.com/ccheney/robust-skills |
| Titulaire | © 2026 robust-skills contributors |
| Licence | MIT (fichier `LICENSE` du dépôt, reproduit ci-dessous) |
| Commit source | `0eea7b060d12e3520556a73b15fbfa79480987d1` (2026-09-12) |

## Fichiers repris (arrêtés à la relecture du 2026-11-03)

| Fichier amont | Fichier Dan-Cortex |
|---|---|
| `skills/clean-ddd-hexagonal/SKILL.md` | `vue-ensemble.md` |
| `skills/clean-ddd-hexagonal/references/DDD-TACTICAL.md` | `ddd-tactique.md` |
| `skills/clean-ddd-hexagonal/references/HEXAGONAL.md` | `hexagonal.md` |
| `skills/clean-ddd-hexagonal/references/CQRS-EVENTS.md` | `cqrs-evenements.md` |

Non repris : `DDD-STRATEGIC.md`, `LAYERS.md`, `TESTING.md` (déjà couverts en forme A par `../c4-ddd-hexagonal.md` §5 à §7) et `CHEATSHEET.md` (redondant, gabarits TypeScript) ; aucun fichier de `scripts/`, `evals/` ni `docs/` du dépôt.

## Modifications

- Traduction en français et adaptation au format Dan-Cortex : sommaire, contrôles avant de rendre, renvois vers `../c4-ddd-hexagonal.md`, `../normes-developpement.md`, `../donnees-schema.md`, rattachement des gardes aux règles `RG-`, exemple fil rouge Parapro (devise DZD, wilaya).
- Code TypeScript (Express, gRPC, commander, conteneur d'injection) réécrit en pseudo-code court et neutre ; noms de fournisseurs (Stripe, RabbitMQ, Postgres, MongoDB) remplacés par des rôles (prestataire de paiement, file, base SQL).
- **Supprimés** : schémas Mermaid d'illustration ; toutes les URL (sources citées par auteur et titre) ; exemple de schéma JSON pointant vers un domaine tiers ; la phrase sur la priorité des consignes de l'utilisateur, remplacée par la priorité de l'ordre de mission et des ADR (aucune consigne concurrente du chef d'orchestre).
- **Ajoutés** : renvoi vers les ADR pour CQRS, saga et sourçage d'événements ; paramétrage des barèmes au lieu de valeurs codées en dur ; contrôles avant de rendre.

## Texte de la licence

```text
MIT License

Copyright (c) 2026 robust-skills contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
