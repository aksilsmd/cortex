# Collecte — types de tests

Pages consultées le 2026-11-03 (outils : Firecrawl search/scrape/query, WebSearch). Résumés et reformulations ; aucune copie de page.

| URL | Titre | Apport |
|---|---|---|
| https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/ | ISTQB CTFL v4.0 Overview | Syllabus en vigueur : CTFL v4.0.1 (téléchargeable) ; chapitres niveaux et types de test, maintenance, test statique. |
| https://www.istqb.com/certifications/ctfl/ | CTFL v4.0 guide | Cinq niveaux (composant, intégration de composants, système, intégration système, acceptation) et quatre types (fonctionnel, non fonctionnel, boîte noire, boîte blanche). |
| https://www.gasq.org/files/content/gasq/downloads/certification/ISTQB/Foundation%20Level/ISTQB_CTFL_Syllabus-v4.0%20.pdf | ISTQB CTFL Syllabus v4.0 (PDF, 74 p.) | 7 principes ; confirmation vs régression ; déclencheurs du test de maintenance ; critères d'entrée/sortie (exemples), DoR/DoD ; risque = probabilité × impact, risques produit/projet ; pyramide ; quadrants Q1–Q4 ; partitions, valeurs limites à 2 et 3 valeurs, tables de décision, transitions d'états ; couverture instructions/branches ; exploratoire en sessions avec charte ; shift-left. |
| https://astqb.org/2-2-test-levels-and-test-types/ | ASTQB 2.2 Test Levels and Test Types | Niveau = instance du processus de test ; en cycle séquentiel, critères de sortie d'un niveau = critères d'entrée du suivant ; types applicables à tous les niveaux. |
| https://istqb.org/certifications/ | ISTQB certifications | CT-AT (Agile Tester) annoncé en retrait ; nouvelle spécialité Finance Testing (2026). |
| https://martinfowler.com/articles/practical-test-pyramid.html | The Practical Test Pyramid (H. Vocke, 2018) | Beaucoup d'unitaires, moins d'intégration, très peu d'E2E ; contrats consumer-driven ; ne pas dupliquer entre couches ; pousser le test au plus bas niveau capable de détecter le défaut. |
| https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications | The Testing Trophy and Testing Classifications (K. C. Dodds) | Couches statique, unitaire, intégration, E2E ; critère : confiance obtenue par temps investi ; les tests qui ressemblent à l'usage réel donnent plus de confiance. |
| https://grafana.com/docs/k6/latest/testing-guides/test-types/ | k6 – Load test types | Fumée, charge moyenne (5–60 min), stress, endurance (heures), pic, point de rupture : but, charge et durée de chacun. |
| https://principlesofchaos.org/ | Principles of Chaos Engineering | État stable mesurable, hypothèse, variables du monde réel, expérimentation en production, automatisation, rayon d'impact minimal. |
| https://owasp.org/www-project-web-security-testing-guide/ | OWASP WSTG | Version stable 4.2 ; 5.0 en développement. |
| https://asvs.owasp.org/ | OWASP ASVS | Version 5.0.0 publiée le 30 mai 2025 ; exigences de sécurité pour concevoir et tester les applications web. |
| https://mas.owasp.org/MASVS/ | OWASP MASVS | Groupes STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY ; MASTG et MASWE pour vérifier. |
| https://quality.arc42.org/articles/iso-25010-update-2023 | ISO 25010 update 2023 | Modèle de qualité produit révisé en 2023 : 9 caractéristiques, dont sûreté (safety) ajoutée, utilisabilité renommée capacité d'interaction, portabilité renommée flexibilité. |
| https://www.w3.org/TR/WCAG22/ | WCAG 2.2 | Référentiel des tests d'accessibilité (niveau AA visé). |
| https://docs.pact.io/ | Pact docs | Non récupérée (hors liste autorisée) ; le principe du contrat consumer-driven est repris de l'article de M. Fowler / H. Vocke. |
