# Contribuer

1. Ouvre un ticket qui décrit le manque (contrôle oublié, faille de robustesse, erreur de droit ou de norme) avec un
   exemple reproductible et sa source.
2. Un contrôle s'ajoute par une ligne dans le fichier `checklist-*.md` du pôle, au format des autres, puis
   `python3 dan-cortex/skills/lancer-projet/scripts/cortex.py plugin verifier`.
3. Les essais restent locaux par défaut ; tout essai qui appelle un modèle est facultatif et documenté.
4. N'ajoute ni vrai secret, ni invite privée, ni donnée personnelle, ni charge utile visant un système tiers.
5. Le mode autonome ne s'élargit pas en retirant une limite dure : une nouvelle délégation passe par les
   autorisations permanentes écrites à J0.
6. Toute modification de `dan-cortex/` se termine par `python3 scripts/construire_plugin.py`, qui reconstruit
   `dist/dan-cortex.plugin` de façon reproductible à partir des fichiers suivis par Git. La CI vérifie que
   l'archive est à jour (`--verifier`).
7. Ne relance pas un ancien paquet de mise à jour (`dan-cortex-update-1.3.0`) : son script réécrit la version.
8. Avant une pull request : `python3 -m unittest discover -s tests -v` et le vérificateur de checklists ci-dessus.
