#!/usr/bin/env node
// Installe IT-Tools (CorentinTh/it-tools, GPL-3.0) en local, sans compte ni paiement.
// Télécharge la version construite officielle, vérifie son empreinte SHA-256, l'extrait et y ajoute le serveur local.
// Usage : node installer-it-tools.mjs [dossier-cible]   (défaut : ./outils/it-tools)
import { createHash } from 'node:crypto';
import { mkdirSync, writeFileSync, copyFileSync, existsSync, readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const VERSION = '2024.10.22-7ca5933';
const URL_ZIP = `https://github.com/CorentinTh/it-tools/releases/download/v${VERSION}/it-tools-${VERSION}.zip`;
const SHA256 = 'eef276d675db6053bdc65cd8482a566785561c70eed5035a0e05b0e627b0989d';
const cible = resolve(process.argv[2] ?? 'outils/it-tools'); mkdirSync(cible, { recursive: true });
const zip = join(cible, `it-tools-${VERSION}.zip`);
if (!existsSync(zip)) {
  // curl suit le proxy d'entreprise (HTTPS_PROXY) ; fetch de Node en secours.
  try { execFileSync('curl', ['-fsSL', '-o', zip, URL_ZIP], { stdio: 'inherit' }); }
  catch {
    try { const r = await fetch(URL_ZIP); if (!r.ok) throw new Error(String(r.status)); writeFileSync(zip, Buffer.from(await r.arrayBuffer())); }
    catch (e) { console.error(`Téléchargement impossible (${e.message}). Déposer à la main ${URL_ZIP} dans ${cible}, puis relancer.`); process.exit(2); }
  }
}
const h = createHash('sha256').update(readFileSync(zip)).digest('hex');
if (h !== SHA256) { console.error(`Empreinte inattendue ${h} : fichier refusé (ne pas l'exécuter).`); process.exit(3); }
try { execFileSync('unzip', ['-q', '-o', zip, '-d', cible]); }
catch { execFileSync('python3', ['-I', '-c', 'import sys,zipfile;zipfile.ZipFile(sys.argv[1]).extractall(sys.argv[2])', zip, cible]); }
const ici = dirname(fileURLToPath(import.meta.url));
copyFileSync(join(ici, 'serveur-it-tools.cjs'), join(cible, 'serveur.cjs'));
writeFileSync(join(cible, 'demarrer-it-tools.cmd'), '@echo off\r\ncd /d "%~dp0"\r\nstart "" http://127.0.0.1:3110/\r\nnode serveur.cjs\r\npause\r\n');
writeFileSync(join(cible, 'LISEZMOI.txt'), `IT-Tools ${VERSION} (https://github.com/CorentinTh/it-tools), licence GPL-3.0, outil séparé.\nDémarrer : node serveur.cjs (ou demarrer-it-tools.cmd sous Windows), puis http://127.0.0.1:3110/\nTout s'exécute dans le navigateur ; le serveur n'écoute que 127.0.0.1 et sa CSP interdit tout appel réseau sortant (aucun traceur).\nEmpreinte SHA-256 du zip officiel : ${SHA256}\n`);
console.log(`IT-Tools ${VERSION} installé dans ${cible} (empreinte vérifiée). Démarrer : node "${join(cible, 'serveur.cjs')}"`);
