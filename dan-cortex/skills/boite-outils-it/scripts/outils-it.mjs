#!/usr/bin/env node
// Appels d'IT-Tools pour les agents Dan-Cortex.
// Deux familles :
//  1. Équivalents natifs Node (aucune dépendance) des outils IT-Tools les plus utiles, pour un résultat scriptable et reproductible.
//  2. Pilotage de l'interface IT-Tools servie en local (http://127.0.0.1:3110, voir serveur-it-tools.cjs) via Playwright,
//     quand le résultat est visuel (QR code, capture d'un outil).
// Usage : node outils-it.mjs <commande> [arguments]   —  node outils-it.mjs aide
import { createHash, createHmac, randomBytes, randomUUID, randomInt } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join } from 'node:path';
// Playwright : cherché à côté du script, puis depuis le dossier courant (projet), puis globalement.
const pw = async () => { try { return await import('playwright'); } catch { return createRequire(join(process.cwd(), 'x.js'))('playwright'); } };
const [cmd, ...a] = process.argv.slice(2);
const opt = (n, d) => { const i = a.indexOf(`--${n}`); return i >= 0 ? a[i + 1] : d; };
const entree = () => { const f = opt('fichier'); if (f) return readFileSync(f); const t = a.find((x, i) => !x.startsWith('--') && !(a[i - 1] ?? '').startsWith('--')); return Buffer.from(t ?? readFileSync(0)); };
const B32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
const b32dec = (s) => { let bits = '', out = []; for (const c of s.replace(/=+$/, '').toUpperCase()) bits += B32.indexOf(c).toString(2).padStart(5, '0'); for (let i = 0; i + 8 <= bits.length; i += 8) out.push(parseInt(bits.slice(i, i + 8), 2)); return Buffer.from(out); };
const b64u = (s) => Buffer.from(s.replace(/-/g, '+').replace(/_/g, '/'), 'base64').toString('utf8');
const BASE = process.env.IT_TOOLS_URL ?? 'http://127.0.0.1:3110';
const C = {
  aide: () => console.log(`Commandes (équivalents IT-Tools entre crochets) :
  hash <texte>|--fichier f [--algo sha256|sha1|sha512|md5]   [hash-text]  empreinte hexadécimale
  hmac <texte> --cle k [--algo sha256]                         [hmac-generator]
  jeton [--longueur 32] [--alphabet hex|base64url|alnum]       [token-generator]  secret aléatoire (crypto)
  uuid [--nombre 1]                                             [uuid-generator]  UUID v4
  base64 <texte> [--decoder]                                    [base64-string-converter]
  url <texte> [--decoder]                                       [url-encoder]
  jwt <jeton>                                                   [jwt-parser]  en-tête et charge utile, sans vérifier la signature
  totp --secret BASE32 [--decalage 0]                           [otp-generator]  code à 6 chiffres (tests de double authentification)
  entropie <mot-de-passe>|--fichier f                           [password-strength-analyser]  bits d'entropie estimés, n'affiche pas le secret
  qr <texte> --sortie fichier.png                               [qrcode-generator]  via l'interface IT-Tools locale (Playwright)
  capture <outil> --sortie f.png                                ouvre ${BASE}/<outil> et en fait une capture
  verifier                                                      vérifie que l'interface locale répond et n'appelle aucun hôte externe`),
  hash: () => console.log(createHash(opt('algo', 'sha256')).update(entree()).digest('hex')),
  hmac: () => console.log(createHmac(opt('algo', 'sha256'), opt('cle') ?? (() => { throw new Error('--cle requis'); })()).update(entree()).digest('hex')),
  jeton: () => { const n = Number(opt('longueur', 32)), al = opt('alphabet', 'base64url');
    if (al === 'alnum') { const s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'; console.log(Array.from({ length: n }, () => s[randomInt(s.length)]).join('')); }
    else console.log(randomBytes(Math.ceil(n * (al === 'hex' ? 0.5 : 0.75))).toString(al).slice(0, n)); },
  uuid: () => { for (let i = 0; i < Number(opt('nombre', 1)); i++) console.log(randomUUID()); },
  base64: () => console.log(a.includes('--decoder') ? Buffer.from(entree().toString(), 'base64').toString('utf8') : entree().toString('base64')),
  url: () => console.log(a.includes('--decoder') ? decodeURIComponent(entree().toString()) : encodeURIComponent(entree().toString())),
  jwt: () => { const [h, p] = entree().toString().trim().split('.'); console.log(JSON.stringify({ entete: JSON.parse(b64u(h)), charge: JSON.parse(b64u(p)), avertissement: 'signature non vérifiée' }, null, 2)); },
  totp: () => { const c = Buffer.alloc(8); c.writeBigUInt64BE(BigInt(Math.floor(Date.now() / 30000) + Number(opt('decalage', 0)))); const h = createHmac('sha1', b32dec(opt('secret'))).update(c).digest(); const o = h[19] & 15; console.log(String((h.readUInt32BE(o) & 0x7fffffff) % 1e6).padStart(6, '0')); },
  entropie: () => { const s = entree().toString().replace(/\n$/, ''); let n = 0; if (/[a-z]/.test(s)) n += 26; if (/[A-Z]/.test(s)) n += 26; if (/\d/.test(s)) n += 10; if (/[^a-zA-Z0-9]/.test(s)) n += 33;
    const bits = Math.round(s.length * Math.log2(Math.max(n, 1))); console.log(JSON.stringify({ longueur: s.length, alphabet: n, bits, niveau: bits < 50 ? 'faible' : bits < 80 ? 'moyen' : 'fort' })); },
  qr: async () => { const { chromium } = await pw(); const b = await chromium.launch(); const p = await b.newPage();
    await p.goto(`${BASE}/qrcode-generator`, { waitUntil: 'networkidle' }); await p.locator('textarea').first().fill(entree().toString()); await p.waitForTimeout(400);
    const src = await p.locator('img[src^="data:image/png"]').first().getAttribute('src'); writeFileSync(opt('sortie', 'qr.png'), Buffer.from(src.split(',')[1], 'base64')); await b.close(); console.log(opt('sortie', 'qr.png')); },
  capture: async () => { const { chromium } = await pw(); const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
    await p.goto(`${BASE}/${a[0] ?? ''}`, { waitUntil: 'networkidle' }); await p.screenshot({ path: opt('sortie', 'capture.png') }); await b.close(); console.log(opt('sortie', 'capture.png')); },
  verifier: async () => { const { chromium } = await pw(); const b = await chromium.launch(); const p = await b.newPage(); const ext = new Set();
    p.on('request', (r) => { const u = r.url(); if (!u.startsWith(BASE) && !/^(data|blob):/.test(u)) ext.add(u); });
    for (const o of ['', 'token-generator', 'hash-text', 'qrcode-generator', 'jwt-parser']) await p.goto(`${BASE}/${o}`, { waitUntil: 'networkidle' });
    await b.close(); console.log(JSON.stringify({ interface: 'ok', hotes_externes: [...ext] })); if (ext.size) process.exit(1); },
};
if (!C[cmd]) { C.aide(); process.exit(cmd ? 1 : 0); }
try { await C[cmd](); } catch (e) { console.error(`Erreur : ${e.message}`); process.exit(1); }
