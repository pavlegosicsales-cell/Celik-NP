#!/usr/bin/env node
/**
 * Render an Apps Script notification email to PNGs, without deploying anything.
 *
 *   node preview.js <path-to-Code.gs> <output-dir> [--mobile]
 *
 * Evals the .gs (the HTML builder is plain JS, the Google globals are never
 * touched by buildHtml_), renders a full submission plus five awkward ones,
 * screenshots each with headless Chrome and builds a comparison grid.
 *
 * Writes:
 *   main.png       the full submission, desktop width
 *   mobile.png     the full submission at 375px
 *   edge-grid.png  the five degraded cases side by side
 *   case-*.html    every rendered case, openable in a browser
 */

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

const CHROME = process.env.CHROME ||
  'C:/Program Files/Google/Chrome/Application/chrome.exe';

const gsPath = process.argv[2];
const outDir = process.argv[3];
if (!gsPath || !outDir) {
  console.error('usage: preview.js <path-to-Code.gs> <output-dir>');
  process.exit(1);
}
fs.mkdirSync(outDir, { recursive: true });

// Stub the Google globals so a stray reference at load time cannot throw.
const SpreadsheetApp = {}, MailApp = {}, ContentService = {}, Utilities = {};
eval(fs.readFileSync(gsPath, 'utf8'));

if (typeof buildHtml_ !== 'function') {
  console.error('No buildHtml_ found in ' + gsPath);
  process.exit(1);
}

// Generic samples. Field names not present in the script are simply ignored,
// so this works for any form shape.
const full = {
  ime: 'Marko Petrović', telefon: '060 123 4567', mejl: 'marko@primer.rs',
  posao: 'Letnja ili zatvorena bašta', objekat: 'Ugostiteljski lokal',
  gde: 'Kragujevac', kada: 'Pre sezone',
  opis: 'Bašta oko 40 m2, uz postojeću terasu. Treba zastakljenje i krov.\n\nMožete li da izađete na teren sledeće nedelje?',
  strana: '/kontakt.html'
};

const cases = {
  full,
  'samo-mejl': { ime: 'Ana', mejl: 'ana@primer.rs', posao: 'Kapija ili ograda', strana: '/index.html' },
  'samo-telefon': { ime: 'Boban Ilić', telefon: '064 555 111', opis: 'Zovite me posle 16h.' },
  'los-telefon': { ime: 'Kika', mejl: 'k@primer.rs', telefon: 'n/a', opis: 'Kratko pitanje o ceni.' },
  'bez-opisa': { ime: 'Petar Rakić', mejl: 'p@primer.rs', telefon: '0601234567', posao: 'Stepenište ili PP stepenište', objekat: 'Poslovni objekat ili firma', gde: 'Šumadija, van Kragujevca', kada: 'Hitno' },
  'prazan': {},
  'napad': {
    ime: '"><script>alert(1)</script> & sin', posao: 'Ograda & <b>kapija</b>',
    mejl: 'x"y@z.com', telefon: '++381 (60) 897-4986 lok 2',
    opis: '<img src=x onerror=alert(1)> & "navodnici"'
  },
  'predugacko': {
    ime: 'Aleksandar Konstantinović-Milovanović Treći',
    mejl: 'aleksandar.konstantinovic.milovanovic@jedan-veoma-dugacak-domen-primer.rs',
    telefon: '+381 60 000 000', posao: 'Konstrukcija, hala, nadstrešnica',
    objekat: 'Gradilište u toku', gde: 'Centralna Srbija', kada: 'U toku ovog meseca',
    opis: 'Lorem ipsum dolor sit amet. '.repeat(45)
  }
};

let failures = 0;
const written = {};

for (const key of Object.keys(cases)) {
  let html;
  try {
    html = buildHtml_(cases[key]);
  } catch (err) {
    console.log('FAIL  ' + key + ' threw: ' + err.message);
    failures++;
    continue;
  }

  // Safety checks that have caught real bugs.
  if (/<script[\s>]/i.test(html)) {
    console.log('FAIL  ' + key + ': raw <script> tag in output, escaping is broken');
    failures++;
  }
  if (/style="[^"]*"[A-Za-z]/.test(html)) {
    console.log('FAIL  ' + key + ': a style attribute is closing early, check for double quotes in a font stack');
    failures++;
  }
  if (/href="[^"]*"[A-Za-z]/.test(html)) {
    console.log('FAIL  ' + key + ': an href is closing early, escape the URL');
    failures++;
  }

  const file = path.join(outDir, 'case-' + key + '.html');
  fs.writeFileSync(file, html);
  written[key] = file;
  console.log('ok    ' + key.padEnd(12) + (html.length / 1024).toFixed(1) + 'kb');
}

function shoot(url, out, w, h, scale) {
  execFileSync(CHROME, [
    '--headless', '--disable-gpu', '--hide-scrollbars',
    '--force-device-scale-factor=' + (scale || 1.5),
    '--window-size=' + w + ',' + h,
    '--screenshot=' + out, url
  ], { stdio: 'ignore' });
}

if (written.full) {
  shoot('file://' + written.full, path.join(outDir, 'main.png'), 680, 980);
  // Headless Chrome refuses to make a window narrower than 500px, so a
  // --window-size=375 shot is a 500px layout cropped to 375 and every mobile
  // media query lies. Render inside a 375px iframe instead: the iframe is its
  // own viewport, so the query fires for real.
  const phone = path.join(outDir, 'phone.html');
  fs.writeFileSync(phone,
    '<body style="margin:0;background:#999">' +
    '<iframe src="case-full.html" style="width:375px;height:1000px;border:0;display:block"></iframe>' +
    '</body>');
  shoot('file://' + phone, path.join(outDir, 'mobile.png'), 375, 1000, 2);
}

const edge = ['samo-mejl', 'samo-telefon', 'los-telefon', 'bez-opisa', 'prazan', 'predugacko']
  .filter(k => written[k]);
if (edge.length) {
  const grid = path.join(outDir, 'grid.html');
  fs.writeFileSync(grid,
    '<body style="margin:0;background:#888;display:flex;flex-wrap:wrap">' +
    edge.map(k => '<iframe src="case-' + k + '.html" style="width:50%;height:660px;border:0"></iframe>').join('') +
    '</body>');
  shoot('file://' + grid, path.join(outDir, 'edge-grid.png'), 1360, 1990, 1);
}

console.log('');
console.log(failures ? failures + ' check(s) failed' : 'all checks passed');
console.log('screenshots in ' + outDir);
process.exit(failures ? 1 : 0);
