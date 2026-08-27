/* ==========================================================================
   PREKIDAC JEZIKA  /  srpski i engleski
   --------------------------------------------------------------------------
   Sajt je pisan na srpskom. Engleski se ne drzi u zasebnim fajlovima nego
   se tekst zamjenjuje u mjestu, po rjecniku iz js/prevod.js. Razlog: sve
   strane bi inace morale u dva primjerka, a index.html je pisan rucno.

   Sta se prevodi:
     tekstualni cvorovi        svuda osim u <script>, <style>, <svg>
     atributi                  alt, placeholder, title, aria-label
     <title> i meta description

   Original se pamti u mapi, pa povratak na srpski vraca tacno ono sto je
   bilo, bez ponovnog ucitavanja strane.

   Izbor jezika:
     1. ono sto je korisnik ranije izabrao (localStorage)
     2. ako izbora nema: jezik pretrazivaca, pa vremenska zona
        balkanski -> srpski, sve ostalo -> engleski
   ========================================================================== */
(function () {
  'use strict';

  var KLJUC = 'np-celik-jezik';

  /* Jezici i zone sa kojih se ocekuje srpski. Ovo je jedina lista koju
     treba dirati ako se opseg mijenja. */
  var BALKAN_JEZICI = ['sr', 'hr', 'bs', 'sh', 'me', 'mk', 'sl'];
  var BALKAN_ZONE = [
    'Europe/Belgrade', 'Europe/Zagreb', 'Europe/Sarajevo', 'Europe/Skopje',
    'Europe/Podgorica', 'Europe/Ljubljana', 'Europe/Banja_Luka'
  ];

  var ATRIBUTI = ['alt', 'placeholder', 'title', 'aria-label'];

  /* Elementi cije sadrzaje main.js prepisuje: natpisi dugmadi na slova,
     naslovi na rijeci, "pali se pri skrolu" na slova. Njihov izvorni tekst
     mora da se pokupi PRIJE nego sto main.js krene, pa se skupljanje radi
     odmah pri izvrsavanju ove skripte, ne na DOMContentLoaded.
     Redosled u HTML-u je zato obavezan: prevod.js, jezik.js, pa main.js. */
  var POSEBNI = [
    ['[data-roll]', 'roll'],
    ['[data-split-words]', 'words'],
    ['[data-scroll-fill]', 'fill']
  ];

  var PREVOD = window.NP_PREVOD || {};
  var originali = new Map();   // cvor ili [element, atribut] -> srpski tekst
  var atributi = [];           // [element, atribut, srpski]
  var tekstovi = [];           // [cvor, srpski]
  var posebni = [];            // [element, tip, srpski]
  var pripremljeno = false;

  /* Poziva se odmah, dok je tekst jos citav.
     Za naslove se pamti innerHTML, jer u njima ima <br> i obojenih
     span-ova koje rastavljac cuva; za ostalo je dovoljan obican tekst. */
  function pokupiPosebne() {
    POSEBNI.forEach(function (par) {
      Array.prototype.forEach.call(document.querySelectorAll(par[0]), function (el) {
        if (par[1] === 'words') {
          if (el.innerHTML.trim()) { posebni.push([el, 'words', el.innerHTML]); }
          return;
        }
        var sr = el.textContent.replace(/\s+/g, ' ').trim();
        if (sr) { posebni.push([el, par[1], sr]); }
      });
    });
  }

  /* Prevodi tekstualne cvorove unutar jednog elementa, cuvajuci markup. */
  function prevediUnutra(el, na_engleski) {
    var hod = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
    var n;
    while ((n = hod.nextNode())) {
      var k = n.nodeValue.replace(/\s+/g, ' ').trim();
      if (k && na_engleski && PREVOD[k]) { n.nodeValue = n.nodeValue.replace(k, PREVOD[k]); }
    }
  }

  function balkanski() {
    var jezici = navigator.languages || [navigator.language || ''];
    for (var i = 0; i < jezici.length; i++) {
      var kod = String(jezici[i]).toLowerCase().split('-')[0];
      if (BALKAN_JEZICI.indexOf(kod) !== -1) { return true; }
    }
    try {
      var zona = Intl.DateTimeFormat().resolvedOptions().timeZone;
      if (BALKAN_ZONE.indexOf(zona) !== -1) { return true; }
    } catch (e) { /* stari pretrazivac, ostaje na jeziku */ }
    return false;
  }

  function sacuvano() {
    try { return localStorage.getItem(KLJUC); } catch (e) { return null; }
  }

  function zapamti(jezik) {
    try { localStorage.setItem(KLJUC, jezik); } catch (e) { /* privatni rezim */ }
  }

  /* Skupljanje se radi jednom. Poslije toga je prebacivanje samo prolaz
     kroz dvije liste, bez ponovnog obilaska stabla. */
  function pripremi() {
    if (pripremljeno) { return; }
    pripremljeno = true;

    var hodac = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (cvor) {
        var r = cvor.parentNode;
        while (r) {
          var ime = r.nodeName;
          if (ime === 'SCRIPT' || ime === 'STYLE' || ime === 'svg' || ime === 'SVG' ||
              ime === 'NOSCRIPT') { return NodeFilter.FILTER_REJECT; }
          r = r.parentNode;
        }
        return cvor.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });

    var cvor;
    while ((cvor = hodac.nextNode())) {
      var kljuc = cvor.nodeValue.replace(/\s+/g, ' ').trim();
      if (PREVOD[kljuc]) { tekstovi.push([cvor, cvor.nodeValue, kljuc]); }
    }

    var svi = document.querySelectorAll('[alt], [placeholder], [title], [aria-label]');
    Array.prototype.forEach.call(svi, function (el) {
      ATRIBUTI.forEach(function (a) {
        var v = el.getAttribute(a);
        if (!v) { return; }
        var k = v.replace(/\s+/g, ' ').trim();
        if (PREVOD[k]) { atributi.push([el, a, v, k]); }
      });
    });
  }

  function postavi(jezik) {
    pripremi();
    var na_engleski = jezik === 'en';

    tekstovi.forEach(function (t) {
      t[0].nodeValue = na_engleski
        ? t[1].replace(t[2], PREVOD[t[2]])
        : t[1];
    });

    atributi.forEach(function (a) {
      a[0].setAttribute(a[1], na_engleski ? PREVOD[a[3]] : a[2]);
    });

    /* Rastavljeni elementi: novi tekst pa ponovo rastavljanje, da efekat
       ostane i na engleskom. Ako main.js jos nije stigao da izlozi kuku,
       upisuje se obican tekst. */
    posebni.forEach(function (x) {
      var el = x[0], tip = x[1], izvor = x[2];
      var kuka = window.NP_RESPLIT && window.NP_RESPLIT[tip];

      if (tip === 'words') {
        el.innerHTML = izvor;              // vrati <br> i obojene span-ove
        prevediUnutra(el, na_engleski);    // pa prevedi tekst u njima
        if (kuka) { kuka(el); }
        return;
      }

      var tekst = na_engleski && PREVOD[izvor] ? PREVOD[izvor] : izvor;
      if (kuka) { kuka(el, tekst); } else { el.textContent = tekst; }
    });

    // naslov strane i opis, zbog kartice u pretrazivacu
    var naslov = document.title.trim();
    if (!originali.has('title')) { originali.set('title', naslov); }
    var srNaslov = originali.get('title');
    document.title = na_engleski && PREVOD[srNaslov] ? PREVOD[srNaslov] : srNaslov;

    var opis = document.querySelector('meta[name="description"]');
    if (opis) {
      if (!originali.has('desc')) { originali.set('desc', opis.getAttribute('content')); }
      var srOpis = originali.get('desc');
      opis.setAttribute('content', na_engleski && PREVOD[srOpis] ? PREVOD[srOpis] : srOpis);
    }

    document.documentElement.setAttribute('lang', na_engleski ? 'en' : 'sr-Latn-RS');
    document.documentElement.setAttribute('data-jezik', na_engleski ? 'en' : 'sr');

    /* Skripte koje same upisuju tekst u toku rada (wizard) ne mogu da prodju
       kroz rjecnik, jer tog teksta u trenutku prevodjenja jos nema. Njima se
       javlja da je jezik promijenjen, pa se same osvjeze. */
    try {
      document.dispatchEvent(new CustomEvent('np:jezik', { detail: na_engleski ? 'en' : 'sr' }));
    } catch (e) { /* stari pretrazivac */ }

    Array.prototype.forEach.call(document.querySelectorAll('[data-jezik-prekidac]'), function (b) {
      var moj = b.getAttribute('data-jezik-prekidac');
      var aktivan = moj === (na_engleski ? 'en' : 'sr');
      b.classList.toggle('is-on', aktivan);
      b.setAttribute('aria-pressed', aktivan ? 'true' : 'false');
    });
  }

  /* ?lang=en u adresi ima prednost nad svim ostalim i pamti se. Sluzi za
     dijeljenje engleske verzije linkom i za provjeru na zivom sajtu. */
  function izAdrese() {
    var m = /[?&]lang=(sr|en)/.exec(window.location.search);
    return m ? m[1] : null;
  }

  function pokreni() {
    var izbor = izAdrese();
    if (izbor) { zapamti(izbor); }
    if (!izbor) { izbor = sacuvano(); }
    if (izbor !== 'sr' && izbor !== 'en') { izbor = balkanski() ? 'sr' : 'en'; }
    postavi(izbor);

    document.addEventListener('click', function (e) {
      var dugme = e.target.closest('[data-jezik-prekidac]');
      if (!dugme) { return; }
      e.preventDefault();
      var novi = dugme.getAttribute('data-jezik-prekidac');
      zapamti(novi);
      postavi(novi);
    });
  }

  /* Skupljanje ide odmah (defer znaci da je telo strane vec sparsirano),
     a primjena tek kad i main.js zavrsi svoje rastavljanje. */
  pokupiPosebne();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', pokreni);
  } else {
    window.setTimeout(pokreni, 0);
  }
})();
