/**
 * NP Čelik — backend za upite sa sajta
 * ------------------------------------
 * Upisuje svaki upit u Google tabelu i šalje jedno obaveštenje mejlom.
 *
 * Sajt šalje GET sa parametrima u adresi. Apps Script svaki POST preusmeri
 * na sesijsku adresu i pretvori ga u GET, čime se gubi e.postData, pa je GET
 * jedini pouzdan put. doPost je ostavljen za slučaj da se front promeni.
 *
 * Polja koja obrazac šalje (js/wizard.js):
 *   ime, telefon, mejl, posao, objekat, gde, kada, opis, strana
 */

/* ================= PODEŠAVANJA ================= */

// Dok se testira, obaveštenja idu na tvoju adresu. Tek kad vidiš da mejl
// stiže i izgleda kako treba, ovde ide npcelik85@gmail.com i pusti se
// Deploy > Manage deployments > New version.
var NOTIFY_TO   = 'pavlegosic9@gmail.com';
var SENDER_NAME = 'NP Čelik sajt';
var BRAND       = 'NP Čelik';
// Tabela sa upitima, link stoji u podnožju svakog mejla. Prazno ga sakriva.
var SHEET_URL   = '';
// Prazno kad je skripta vezana za tabelu. Popuniti samo ako je samostalna.
var SHEET_ID    = '';

/* ================= PALETA =================
   Boje su iz site/css/tokens.css, ne izmišljene:
     brend plava  #1B44D3   (--brand-blue)
     mastilo      #0A0F1F   (--ink-900)
     telo teksta  #2B3652   (--brown-800)
     prigušeno    #5B6784   (--stone-600)
     hladno bela  #F4F6FB   (--cream-100)
     linije       #D4DAE9

   Brend plava je dovoljno tamna da beo tekst na njoj prolazi kontrast
   (7.4:1), pa brand i brandDark mogu da budu ista boja. */

var C = {
  page:      '#F4F6FB',
  card:      '#FFFFFF',
  panel:     '#EEF1F9',
  line:      '#D4DAE9',
  brand:     '#1B44D3',
  brandDark: '#1B44D3',
  ink:       '#0A0F1F',
  body:      '#2B3652',
  muted:     '#5B6784',
  onBrand:   '#FFFFFF'
};

// Zaobljenja. Outlook na Windowsu ih poravna, ništa nosivo ne visi o njima.
var RADIUS = '16px';
var RPILL  = '8px';

// Jedno pismo. Veb fontovi se u mejlu ne učitavaju.
var SANS = 'Helvetica,Arial,sans-serif';

/* ================= ULAZ ================= */

function doGet(e) {
  var d = readParams_(e);
  if (!d.ime && !d.mejl && !d.telefon && !d.opis) {
    return json_({ ok: true, service: BRAND + ' endpoint za upite' });
  }
  return handle_(d);
}

function doPost(e) {
  var d = readParams_(e);
  if (e && e.postData && e.postData.contents) {
    try {
      var body = JSON.parse(e.postData.contents);
      for (var k in body) if (body[k]) d[k] = body[k];
    } catch (err) { /* nije JSON, parametri su već pročitani */ }
  }
  return handle_(d);
}

function handle_(d) {
  var sheetErr = '';
  // Namerno razdvojeno: neuspeo upis u tabelu ne sme da košta upit.
  try { saveRow_(d); } catch (err) { sheetErr = String(err); }
  try {
    sendEmail_(d);
  } catch (err) {
    return json_({ ok: false, error: String(err), sheetError: sheetErr });
  }
  return json_({ ok: true, sheetError: sheetErr });
}

function readParams_(e) {
  var p = (e && e.parameter) ? e.parameter : {};
  return {
    ime:     p.ime     || '',
    telefon: p.telefon || '',
    mejl:    p.mejl    || '',
    posao:   p.posao   || '',
    objekat: p.objekat || '',
    gde:     p.gde     || '',
    kada:    p.kada    || '',
    opis:    p.opis    || '',
    strana:  p.strana  || ''
  };
}

/* ================= TABELA ================= */

function saveRow_(d) {
  var ss = SHEET_ID
    ? SpreadsheetApp.openById(SHEET_ID)
    : SpreadsheetApp.getActiveSpreadsheet();
  if (!ss) throw new Error('Nema tabele: veži skriptu za tabelu ili postavi SHEET_ID.');
  var sheet = ss.getSheets()[0];

  if (sheet.getLastRow() === 0) {
    sheet.appendRow(['Stiglo', 'Ime', 'Telefon', 'Mejl', 'Posao', 'Objekat',
                     'Lokacija', 'Rok', 'Opis', 'Strana']);
    sheet.getRange(1, 1, 1, 10).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }

  sheet.appendRow([
    new Date(),
    d.ime || '', d.telefon || '', d.mejl || '', d.posao || '', d.objekat || '',
    d.gde || '', d.kada || '', d.opis || '', d.strana || ''
  ]);
}

/* ================= MEJL ================= */

function sendEmail_(d) {
  MailApp.sendEmail(NOTIFY_TO, buildSubject_(d), buildPlain_(d), {
    name: SENDER_NAME,
    htmlBody: buildHtml_(d),
    replyTo: d.mejl || undefined   // odgovor ide pravo podnosiocu upita
  });
}

function buildSubject_(d) {
  var ko = d.ime || 'Novi kontakt';
  var rep = d.posao ? ' (' + d.posao + ')' : '';
  return 'Novi upit sa sajta: ' + ko + rep;
}

function buildPlain_(d) {
  return [
    'NOVI UPIT SA SAJTA NP ČELIK',
    '',
    'Ime:       ' + (d.ime || ''),
    'Telefon:   ' + (d.telefon || ''),
    'Mejl:      ' + (d.mejl || ''),
    'Posao:     ' + (d.posao || ''),
    'Objekat:   ' + (d.objekat || ''),
    'Lokacija:  ' + (d.gde || ''),
    'Rok:       ' + (d.kada || ''),
    '',
    'OPIS POSLA',
    (d.opis || '(nije upisan)'),
    '',
    'Stiglo sa obrasca na sajtu' + (d.strana ? ' (' + d.strana + ')' : '') + '.'
  ].join('\n');
}

/**
 * Pravila su namerna, vidi reference/gotchas.md uz skill:
 *  - samo tabele i inline stilovi, bez flex/grid, bez veb fontova, bez slika
 *  - !important na svakoj boji i bgcolor na svakom bloku, da Gmail i
 *    Outlook.com u tamnom režimu ne preboje mejl
 *  - color-scheme meta sprečava Apple Mail da sam invertuje
 *  - dugmad su tabelarne ćelije sa razmakom, ne stilizovani linkovi
 */
function buildHtml_(d) {
  var ime = d.ime || 'Neko';

  // Dugme se pojavljuje samo kad je vrednost upotrebljiva.
  var cifre = String(d.telefon || '').replace(/[^\d+]/g, '');
  var zove = cifre.replace(/\D/g, '').length >= 6;
  var tel = 'tel:' + cifre;
  var pise = /.+@.+\..+/.test(String(d.mejl || ''));

  var rows = [
    ['Ime',      d.ime],
    ['Telefon',  d.telefon, zove ? tel : ''],
    ['Mejl',     d.mejl, pise ? 'mailto:' + esc_(d.mejl) : ''],
    ['Posao',    d.posao],
    ['Objekat',  d.objekat],
    ['Lokacija', d.gde],
    ['Rok',      d.kada]
  ].filter(function (r) { return r[1]; }).map(function (r, i, all) {
    var border = (i === all.length - 1) ? '' : 'border-bottom:1px solid ' + C.line + ';';
    var value = r[2]
      ? '<a href="' + r[2] + '" style="color:' + C.ink + ' !important;text-decoration:none;' +
        'border-bottom:1px solid ' + C.line + ';">' + esc_(r[1]) + '</a>'
      : esc_(r[1]);
    return '<tr>' +
      '<td bgcolor="' + C.card + '" width="120" style="background-color:' + C.card + ' !important;' + border +
        'padding:15px 16px 15px 0;color:' + C.muted + ' !important;font:700 11px/1.35 ' + SANS + ';' +
        'letter-spacing:.13em;text-transform:uppercase;vertical-align:top;">' + r[0] + '</td>' +
      '<td bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;' + border +
        'padding:13px 0;color:' + C.ink + ' !important;font:400 17px/1.45 ' + SANS + ';">' + value + '</td>' +
    '</tr>';
  }).join('');

  var panel =
    '<tr><td bgcolor="' + C.panel + '" style="background-color:' + C.panel + ' !important;' +
      'border-left:3px solid ' + C.brand + ';border-radius:' + RPILL + ';padding:20px 22px;">' +
      '<div style="color:' + C.muted + ' !important;font:700 11px/1.2 ' + SANS + ';letter-spacing:.13em;' +
        'text-transform:uppercase;padding-bottom:10px;">Opis posla</div>' +
      '<div style="color:' + C.body + ' !important;font:400 16px/1.65 ' + SANS + ';white-space:pre-wrap;">' +
        esc_(d.opis || 'Opis nije upisan.') + '</div>' +
    '</td></tr>';

  var solid = function (href, label) {
    return '<td bgcolor="' + C.brandDark + '" style="background-color:' + C.brandDark + ' !important;' +
      'border-radius:' + RPILL + ';padding:15px 30px;">' +
      '<a href="' + href + '" style="color:' + C.onBrand + ' !important;text-decoration:none;' +
      'font:700 13px/1 ' + SANS + ';letter-spacing:.1em;text-transform:uppercase;">' + label + '</a></td>';
  };
  var ghost = function (href, label) {
    return '<td bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;' +
      'border:1px solid ' + C.line + ';border-radius:' + RPILL + ';padding:14px 28px;">' +
      '<a href="' + href + '" style="color:' + C.ink + ' !important;text-decoration:none;' +
      'font:700 13px/1 ' + SANS + ';letter-spacing:.1em;text-transform:uppercase;">' + label + '</a></td>';
  };
  var mailHref = 'mailto:' + esc_(d.mejl) + '?subject=' +
    encodeURIComponent('Odgovor na vaš upit — NP Čelik');

  /* Natpisi bez imena. Srpski trazi akuzativ ("pozovi Marka", ne "Marko"),
     a promjena po padezima za proizvoljno ime nije pouzdana, pa ime ostaje
     u zaglavlju mejla gdje stoji u nominativu. */
  var buttons = '';
  if (zove && pise) {
    buttons = solid(tel, 'Pozovi') +
      '<td width="10" style="width:10px;">&nbsp;</td>' + ghost(mailHref, 'Odgovori mejlom');
  } else if (zove) {
    buttons = solid(tel, 'Pozovi');
  } else if (pise) {
    buttons = solid(mailHref, 'Odgovori mejlom');
  }

  // Bez upotrebljivog kontakta red se izostavlja, da ne stoji prazna traka.
  var actions = buttons
    ? '<tr><td class="pad" bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;padding:28px 40px 38px;">' +
      '<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>' + buttons + '</tr></table>' +
      '</td></tr>'
    : '<tr><td bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;height:34px;font-size:0;line-height:0;">&nbsp;</td></tr>';

  return '' +
'<!DOCTYPE html><html><head><meta charset="utf-8">' +
'<meta name="viewport" content="width=device-width,initial-scale=1">' +
'<meta name="color-scheme" content="light dark">' +
'<meta name="supported-color-schemes" content="light dark">' +
'<style>:root{color-scheme:light dark;supported-color-schemes:light dark;}' +
'@media (max-width:600px){.pad{padding-left:24px !important;padding-right:24px !important;}' +
'.hd{font-size:26px !important;}}</style></head>' +
'<body style="margin:0;padding:0;background-color:' + C.page + ' !important;" bgcolor="' + C.page + '">' +
'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" ' +
  'bgcolor="' + C.page + '" style="background-color:' + C.page + ' !important;">' +
'<tr><td align="center" style="padding:32px 12px 44px;">' +

  '<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->' +
  '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" ' +
    'style="width:100%;max-width:600px;">' +

  '<tr><td style="padding:0;">' +
  '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" ' +
    'bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;' +
    'border:1px solid ' + C.line + ';border-radius:' + RADIUS + ';">' +

    '<tr><td class="pad" bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;' +
      'border-top:4px solid ' + C.brand + ';border-radius:' + RADIUS + ' ' + RADIUS + ' 0 0;padding:34px 40px 28px;">' +
      '<div style="color:' + C.brand + ' !important;font:700 11px/1.2 ' + SANS + ';letter-spacing:.2em;' +
        'text-transform:uppercase;">' + esc_(BRAND) + '</div>' +
      '<div class="hd" style="color:' + C.ink + ' !important;font:700 32px/1.15 ' + SANS + ';' +
        'letter-spacing:-.01em;padding-top:14px;">Novi upit</div>' +
      '<div style="color:' + C.muted + ' !important;font:400 15px/1.5 ' + SANS + ';padding-top:10px;">' +
        esc_(ime) + (d.posao ? ' &middot; ' + esc_(d.posao) : '') + '</div>' +
    '</td></tr>' +

    (rows ? '<tr><td class="pad" bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;padding:0 40px;">' +
      '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" ' +
        'bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;' +
        'border-top:1px solid ' + C.line + ';">' + rows + '</table>' +
    '</td></tr>' : '') +

    '<tr><td class="pad" bgcolor="' + C.card + '" style="background-color:' + C.card + ' !important;padding:26px 40px 0;">' +
      '<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">' + panel + '</table>' +
    '</td></tr>' +

    actions +

  '</table></td></tr>' +

    '<tr><td class="pad" bgcolor="' + C.page + '" style="background-color:' + C.page + ' !important;padding:20px 40px 0;">' +
      '<div style="color:' + C.muted + ' !important;font:700 11px/1.7 ' + SANS + ';letter-spacing:.12em;' +
        'text-transform:uppercase;">Obrazac na sajtu' +
        (d.strana ? ' &nbsp;&middot;&nbsp; ' + esc_(d.strana) : '') + '</div>' +
      (SHEET_URL ? '<div style="padding-top:8px;"><a href="' + SHEET_URL + '" ' +
        'style="color:' + C.muted + ' !important;font:400 12px/1.7 ' + SANS + ';' +
        'text-decoration:underline;">Otvori tabelu sa svim upitima</a></div>' : '') +
    '</td></tr>' +

  '</table>' +
  '<!--[if mso]></td></tr></table><![endif]-->' +
'</td></tr></table></body></html>';
}

/* ================= POMOĆNE ================= */

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function esc_(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
