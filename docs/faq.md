# Questions fréquentes

## Usage

**Faut-il savoir programmer ?**
Non. `/dan-cortex:accueil-recueil` part d'une description en vrac, pose des questions à réponses suggérées et
accepte « Je ne sais pas, décide pour moi ». Les livrables sont rédigés pour être lus par un non-spécialiste.

**Quelle différence entre `accueil-recueil`, `recueil-besoin` et `lancer-projet` ?**
`accueil-recueil` est la porte d'entrée d'un débutant : il enchaîne exploration, entretien, livrables et étude
de réalisation. `recueil-besoin` est l'entretien seul, utilisable même hors du plugin. `lancer-projet` pilote un
projet déjà cadré, jalon par jalon.

**Puis-je n'utiliser qu'un seul skill ?**
Oui. Chaque skill s'appelle seul : `/dan-cortex:veille-marche` pour une étude de marché,
`/dan-cortex:audit-general` pour auditer un projet mené sans Dan-Cortex, etc.

**Combien de temps dure un projet ?**
Une étude d'opportunité en mode `eclair` tient dans une session. Un projet complet en dépasse plusieurs : le
dossier projet garde l'état et le chef d'orchestre reprend où il s'était arrêté.

**Dan-Cortex écrit-il le code ?**
Oui, par lots, avec le pôle `usine-logicielle` : plan, test rouge, développement, tests, contrôle visuel, revue
de sécurité, relecture indépendante, non-régression. Le code vit dans le dépôt du projet, pas dans le plugin.

## Coût

**Est-ce que ça consomme beaucoup ?**
Un système multi-agents coûte plus cher qu'une conversation simple. Dan-Cortex le limite : agents à contexte
réduit (environ 6 000 tokens au départ), modèle léger pour la collecte, comptes rendus de 150 mots, scripts pour
tout ce qui se compte, plafond de tokens avec alertes à 80 % et 100 %. Le coût permanent du plugin est d'environ
4 300 tokens par session ; désactive-le quand tu ne t'en sers pas.

**Quel mode choisir ?**
Commence par `eclair` ou `standard`. `integral` coûte environ deux à trois fois plus et se réserve aux grands
comptes et secteurs régulés.

## Autonomie et sécurité

**Peut-il agir sans moi ?**
En mode `autonome`, il enchaîne tout le périmètre après la qualification, dans les autorisations permanentes que
tu as écrites. Six limites dures demandent toujours ton accord : voir
[sécurité et robustesse](securite-et-robustesse.md#limites-dures).

**Peut-il pousser du code ou publier un site ?**
Seulement avec ton accord, ou dans une autorisation permanente écrite à J0 (par exemple « push sur la branche
`dev` de tel dépôt »). Jamais en dehors.

**Les scripts des skills copiés d'Anthropic sont-ils sûrs ?**
Ils viennent d'anthropics/skills, copiés sans modification au commit `2c5958e`, et s'exécutent sur ta machine.
Lis-les avant usage dans un environnement sensible ; tu peux retirer les dossiers dont tu n'as pas besoin.

## Droit et territoires

**Pour quels pays le droit est-il outillé ?**
France et Union européenne en détail. Royaume-Uni, États-Unis, Algérie, Maroc et Tunisie : repères et renvoi à un
avocat local. Les références sont à l'état d'octobre 2026.

**Les documents juridiques sont-ils utilisables tels quels ?**
Non. Ils sont marqués « à valider » : fais-les relire par un avocat ou un expert-comptable avant usage.

## Autres IA et contribution

**Fonctionne-t-il avec une autre IA que Claude ?**
Oui, en mode dégradé : [`AGENTS.md`](../AGENTS.md) pour les IA qui lisent un dépôt, le paquet universel
(`dan-cortex/universel/`) pour un simple chat. Sans sous-agents, l'IA joue les rôles l'un après l'autre avec les
mêmes portes de validation.

**Comment signaler une erreur de droit ou de norme ?**
Ouvre un ticket avec le modèle « Correction de droit ou de norme », en citant le texte officiel ou la source.

**Pourquoi le contenu est-il en français ?**
Le plugin est conçu pour des projets francophones et le droit français et européen d'abord. Le résumé anglais du
[README](../README.md#in-english) décrit le projet ; les contributions en anglais sont acceptées.
