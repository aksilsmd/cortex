# Dan-Cortex — point d'entrée des commandes du dépôt.
# Prérequis : Python 3.11 ou plus, bibliothèque standard uniquement.
# « verify » rejoue, dans l'ordre, les cinq étapes de .github/workflows/tests.yml.
# « build » rejoue la chaîne de régénération de CONTRIBUTING.md, section 4.

PYTHON ?= python3
PLUGIN := dan-cortex
CORTEX := $(PLUGIN)/skills/lancer-projet/scripts/cortex.py
ROBUSTESSE := $(PLUGIN)/skills/robustesse-agents/scripts/robustesse.py
REGLAGES := $(PLUGIN)/skills/robustesse-agents/assets/reglages-autonomes.json

.DEFAULT_GOAL := help
.PHONY: help verify controles test catalogues catalogues-verifier universel archive \
        archive-verifier build audit clean

help: ## Affiche cette aide
	@printf 'Cibles disponibles :\n\n'
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@printf '\nAprès toute modification : make build, puis make verify.\n'

verify: controles test catalogues-verifier archive-verifier audit ## Rejoue les cinq contrôles de la CI
	@printf '\nTout est vert.\n'

controles: ## Vérifie le format et le compte des 784 contrôles de couverture
	$(PYTHON) $(CORTEX) plugin verifier

test: ## Lance tous les tests
	$(PYTHON) -m unittest discover -s tests -v

catalogues-verifier: ## Vérifie que les catalogues et les cartes sont à jour
	$(PYTHON) scripts/generer_catalogues.py --verifier

archive-verifier: ## Vérifie que dist/dan-cortex.plugin est à jour
	$(PYTHON) scripts/construire_plugin.py --verifier

audit: ## Audite le gabarit de réglages du mode autonome
	$(PYTHON) -I $(ROBUSTESSE) audit-config --path $(REGLAGES)

catalogues: ## Régénère les catalogues et les cartes SVG
	$(PYTHON) scripts/generer_catalogues.py

universel: ## Régénère le paquet universel
	$(PYTHON) scripts/construire_universel.py

archive: ## Reconstruit dist/dan-cortex.plugin (fichiers suivis par Git)
	$(PYTHON) scripts/construire_plugin.py

build: catalogues universel ## Régénère tout ce qui est dérivé, puis l'archive
	@printf '\nL'"'"'archive se construit sur les fichiers suivis : git add -A avant.\n'
	git add -A
	$(PYTHON) scripts/construire_plugin.py

clean: ## Supprime les caches Python (jamais les fichiers générés et suivis)
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
