# Cadre : connexion, coût, droits, données, modération, registre

Faits tirés de la bibliothèque Scenario (commit en `sources.md`). Ce qui n'y figure pas est marqué « à revérifier ».

## 1. Connexion et authentification

- Point d'accès : `https://mcp.scenario.com/mcp` (HTTP en flux). Préférer l'authentification OAuth : on se connecte avec son compte Scenario dans le navigateur, aucun secret ne traverse la conversation.
- Claude Code, sans connecteur existant : la commande `claude mcp add --transport http scenario https://mcp.scenario.com/mcp` ajoute le serveur ; c'est l'utilisateur qui la lance. Sur une offre d'équipe, l'ajout revient à un propriétaire de l'organisation ; chaque membre se connecte ensuite avec son propre compte.
- Test gratuit : demander la liste des équipes (`teams_list`). Connexion qui échoue après avoir fonctionné : refaire l'authentification avant de déboguer ; `diagnostics_run` nomme la couche (`auth`, `tenant-scope`, `api-unreachable`, `healthy`).
- Clé d'API : réservée aux exécutions sans humain. La clé se crée dans le portail Scenario et se branche à la main, selon le guide officiel. L'agent ne demande jamais de clé, n'en place aucune dans une commande, un fichier ou un message, et ne répète pas celle qui apparaîtrait dans son contexte. Ne pas mettre de clé en en-tête fixe d'un connecteur d'organisation : tous les membres hériteraient de ses droits.
- Administration d'équipe : authentification par utilisateur, clés d'API refusées.

## 2. Coût

- Unité : le crédit « Creative Unit » (CU). La valeur monétaire d'un CU et le détail des offres ne figurent pas dans la bibliothèque : à revérifier sur le site de Scenario avant tout chiffrage en euros.
- Estimation avant génération : **elle existe.** `model_run` avec `dry_run: true` renvoie le coût de cette charge exacte (`creativeUnitsCost`) sans créer de tâche ; `dry_run` se place au premier niveau de l'appel, pas dans `parameters` (sinon la tâche est lancée et facturée). Les champs du schéma marqués `cost_impact` font varier le prix. L'estimation de `recommend` suppose les valeurs par défaut. Pour une étape qui dépend d'un résultat précédent, chiffrer d'abord depuis `recommend`, puis refaire le `dry_run` sur le vrai fichier. `workflow_run` accepte aussi `dry_run`. Entraînement : action `configure` avec `dry_run`.
- Solde et consommation : `consumption_limit_get` (reste disponible, fin de période) ; `usage` (consommation passée, `project_id` requis, chiffres par défaut sur la durée de vie du projet : borner les dates).
- Ordres de grandeur relevés à la rédaction de la bibliothèque, à revérifier : un maillage 3D par modèle à base de LLM, 1 300 CU au réglage par défaut contre 45 pour un générateur monoimage ; une analyse du Quality Gate, 1 CU ; une détection de propriété intellectuelle, 1 CU par génération et 1 CU par image fournie.
- Plan gratuit : plafond de 50 CU par jour. Un 429 sur quota ou solde arrête le lot ; ne pas renvoyer la même charge. Une fois les crédits de l'offre épuisés, un « mode relax » impose des attentes qui s'allongent ; proposer recharge, offre supérieure, charge moins chère ou report, jamais modifier soi-même la facturation ou les membres.
- Tâches échouées : remboursées, sauf celles des modèles xAI stoppées par modération. Une vidéo rejetée après rendu a déjà été calculée : vérifier le coût sur la ligne de la tâche.
- Économies : itérer à la résolution et à la durée les plus basses, puis agrandir l'exemplaire retenu ; chercher un modèle personnalisé public avant d'en entraîner un.
- Budget : total reporté dans `budget-finance`, plafond accordé jamais dépassé.

## 3. Modèles tiers accessibles

Familles citées par la bibliothèque (la disponibilité dépend de l'équipe et de l'offre, le catalogue change : redécouvrir à chaque session, ne figer aucun identifiant) :
- image : GPT Image, MAI Image, Seedream, Gemini image (Nano Banana), Reve, Ideogram, Grok Imagine, Luma Uni-1 ;
- vidéo : Kling, Veo, Seedance, Gemini Omni, Luma Ray, Runway, Grok Imagine, Wan, MiniMax Hailuo, Vidu ;
- audio : ElevenLabs, ACE-Step, MiniMax, Sonilo ;
- 3D : Meshy, Rodin, Sparc3D, Tripo, Hunyuan 3D, Trellis, ainsi que des modèles 3D de Scenario à base de LLM.

Un modèle signalé comme exigeant une autre offre échoue en 403 : ne pas réessayer, relayer la marche à suivre et ne changer de modèle qu'avec l'accord de l'utilisateur. Le Quality Gate est une option de l'offre Enterprise.

## 4. Droits sur les contenus générés et usage commercial

La bibliothèque **ne documente pas** la propriété des contenus générés ni les conditions d'usage commercial, et chaque modèle tiers a ses propres conditions. Conduite :
- ne jamais écrire « libre de droits » ni « utilisable commercialement » ;
- renvoyer à l'agent `juriste-numerique`, à `${CLAUDE_SKILL_DIR}/../juridique-conformite/SKILL.md` et aux conditions générales d'utilisation de Scenario et du fournisseur du modèle (à revérifier à la date de publication) ;
- un avertissement de droit d'auteur attaché à une sortie terminée est informatif : la relecture avant usage commercial incombe à l'utilisateur ;
- entraînement vidéo sur un modèle MiniMax H3 : la licence interdit d'utiliser les sorties pour entraîner d'autres IA et d'imiter une personne réelle ; l'annoncer à l'utilisateur avant l'accord sur le devis ;
- le droit sur des visuels de marque, la musique d'une chanson existante ou une ressemblance reste à clarifier par l'utilisateur avant diffusion.

## 5. Données envoyées à un tiers

Chaque prompt, image, audio ou vidéo fournis partent chez Scenario, puis chez le fournisseur du modèle choisi (les filtres de contenu s'exécutent côté fournisseur). Donc :
- jamais de donnée personnelle, de visage de personne réelle sans consentement écrit, de secret, de document client ou interne ; en cas de doute, consulter l'agent `delegue-protection-donnees` et `${CLAUDE_SKILL_DIR}/../confidentialite-traces/SKILL.md` ;
- les préférences enregistrées côté Scenario (`memory_set`) restent chez le tiers : n'y mettre ni donnée personnelle ni secret ;
- les rapports d'anomalie publics (`scenario-report`) se font sans clé, sans lien signé, sans donnée personnelle, et sans identifiant d'équipe sans accord ;

## 6. Modération

Trois barrières possibles : filtre du fournisseur, détection de propriété intellectuelle de l'équipe (option Enterprise, règle de l'administrateur), restrictions d'offre ou liste bloquée. Lire l'erreur d'abord. Si un filtre de fournisseur bloque un contenu légitime : essayer le même prompt sur un modèle d'un autre fournisseur, puis une reformulation honnête (proportions plutôt qu'intensité, description du dessin plutôt qu'un nom protégé). Si tout refuse, s'arrêter et le dire : insister jusqu'à passer est du contournement. On ne s'en sert pas pour produire un contenu qu'un fournisseur interdit, ni pour reproduire une marque ou une personne réelle.

## 7. Registre de traçabilité

Une ligne par média livré, dans le registre du projet (jamais de secret ni de donnée personnelle dedans) :

| Champ | Contenu |
|---|---|
| Identifiant interne | numéro du livrable |
| Date | jour de génération |
| Besoin et usage | à quoi il sert, où il sera publié |
| Skill et modèle | dossier de la bibliothèque, famille et identifiant relevé ce jour |
| Prompt | texte complet et références utilisées (identifiants d'assets, sans fichiers personnels) |
| Paramètres | taille, durée, qualité, éventuelle graine |
| Coût | estimation validée et coût réel en CU |
| Accord | qui a validé le devis, quand |
| Contrôle | critères, verdict, relecteur |
| Droits | état : à vérifier, vérifié par qui |
| Fichier livré | nom et emplacement |
