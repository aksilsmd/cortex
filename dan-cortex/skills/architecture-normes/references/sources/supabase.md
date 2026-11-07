# Collecte — Supabase

Pages consultées le 2026-11-03 (outils : WebSearch, WebFetch). Résumés et reformulations ; aucune copie de page.

| URL | Titre | Apport |
|---|---|---|
| https://supabase.com/docs/guides/api/api-keys.md | Supabase – API keys | Clés `sb_publishable_` (client, soumise à RLS) et `sb_secret_` (serveur, contourne RLS) ; `anon`/`service_role` JWT dépréciées d'ici fin 2026, à désactiver manuellement ; rôles Postgres anon/authenticated/service_role ; grants vérifiés avant RLS ; clé secrète refusée depuis un navigateur (401) ; SDK `@supabase/server` pour Edge Functions. |
| https://www.jetadmin.io/blog/supabase-review/ | Supabase Review 2026 (30 sept. 2026, prix relevés le 26 sept.) | Free : 50 000 MAU, 500 Mo de base, 1 Go de fichiers, 5 Go d'egress, 2 projets, pause après une semaine d'inactivité ; Pro dès 25 USD/mois (8 Go base, 100 Go fichiers, 250 Go egress, 100 000 MAU, 10 USD de crédit compute, sauvegardes 7 j) ; Team dès 599 USD (SOC 2, ISO 27001, SSO, sauvegardes 14 j) ; paliers compute ; plafond de dépenses incomplet (compute, réplicas, PITR exclus). |
| https://supabase.com/kb/faqs/platform/database-only-cost | Supabase KB – coût d'un projet base seule | Page officielle de FAQ sur le coût (non récupérée en détail). |
| https://computingforgeeks.com/self-host-supabase-docker-compose/ | Self-host Supabase with Docker Compose (source secondaire) | Auto-hébergement par Docker Compose officiel (dossier `docker` du dépôt) : Postgres, GoTrue (Auth), PostgREST, Realtime, Storage, Kong, Studio ; secrets et clés à régénérer. |
| https://supabase.com/docs/guides/database/postgres/row-level-security | Supabase – Row Level Security | Référence RLS (politiques par rôle, `auth.uid()`, performances : index et `(select auth.uid())`) — pratiques connues, à recouper. |
