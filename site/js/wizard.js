/* ==========================================================================
   NP ČELIK / WIZARD KONTAKT FORMA
   --------------------------------------------------------------------------
   Po skillu website-build-rules, korak 8:
     - koraci 1..N su samo dugmad, bez kucanja
     - zadnji korak su tekstualna polja
     - traka napretka na vrhu
     - Nazad na svakom koraku osim prvog
     - dodir na karticu sam vodi dalje
     - dugme za slanje se gasi dok zahtjev traje
     - na uspjeh ide poruka u mjestu, bez preusmjeravanja

   Bez biblioteka, kao i ostatak sajta.
   ========================================================================== */
(function () {
  'use strict';

  /* Ovdje ide URL sa Apps Scripta poslije skilla 03 (Form Backend Setup).
     Dok je prazan, forma ne salje nista nego samo pokaze potvrdu, da se
     tok moze isprobati bez backenda. */
  /* Tekstovi koje skripta upisuje u toku rada ne prolaze kroz prevodilac,
     jer u trenutku prevodjenja jos ne postoje u stablu. Zato se ovdje bira
     jezik iz atributa koji postavlja js/jezik.js. */
  function jezik() {
    return document.documentElement.getAttribute('data-jezik') === 'en' ? 'en' : 'sr';
  }

  var TEKST = {
    sr: {
      korak: function (i, n) { return 'Korak ' + i + ' od ' + n; },
      salji: 'Šaljem...',
      nedostaje: 'Treba nam ime i broj telefona da bismo mogli da se javimo.',
      greska: 'Slanje nije uspelo. Pozovite 060 41 45 466 ili pišite na npcelik85@gmail.com.'
    },
    en: {
      korak: function (i, n) { return 'Step ' + i + ' of ' + n; },
      salji: 'Sending...',
      nedostaje: 'We need your name and phone number so we can get back to you.',
      greska: 'Sending failed. Call 060 41 45 466 or write to npcelik85@gmail.com.'
    }
  };

  function t(kljuc) { return TEKST[jezik()][kljuc]; }

  /* Kad se jezik promijeni usred popunjavanja, brojac koraka se prepisuje
     odmah, ne tek na sljedecem koraku. */
  document.addEventListener('np:jezik', function () {
    var count = document.querySelector('.wizard__count');
    var steps = document.querySelectorAll('.wstep');
    var aktivan = 0;
    Array.prototype.forEach.call(steps, function (s, n) {
      if (s.classList.contains('is-active')) { aktivan = n; }
    });
    if (count && steps.length) { count.textContent = t('korak')(aktivan + 1, steps.length); }
  });

  var ENDPOINT = 'https://script.google.com/macros/s/AKfycbzdlu__JeOGya0o1KXHWBOwCnipzfxzI31FiNmtTj0T-uexAZUi753U2PhgdK1IAW4t/exec';

  var form = document.getElementById('wizard');
  if (!form) { return; }

  var steps = Array.prototype.slice.call(form.querySelectorAll('.wstep'));
  var ticks = Array.prototype.slice.call(form.querySelectorAll('.wizard__tick'));
  var count = form.querySelector('.wizard__count');
  var back = form.querySelector('.wnav__back');
  var next = form.querySelector('.wnav__next');
  var submit = form.querySelector('.wnav__submit');
  var err = form.querySelector('.wizard__err');
  var done = document.querySelector('.wizard__done');
  var i = 0;

  function render() {
    steps.forEach(function (s, n) { s.classList.toggle('is-active', n === i); });
    ticks.forEach(function (t, n) { t.classList.toggle('is-done', n <= i); });
    if (count) { count.textContent = t('korak')(i + 1, steps.length); }
    back.hidden = i === 0;

    var last = i === steps.length - 1;
    next.hidden = last;
    submit.hidden = !last;

    /* Fokus na naslov koraka, da citac ekrana i tastatura prate promjenu.
       Bez ovoga se poslije klika fokus vrati na pocetak dokumenta. */
    var q = steps[i].querySelector('.wstep__q');
    if (q) { q.setAttribute('tabindex', '-1'); q.focus({ preventScroll: true }); }
  }

  function go(n) {
    i = Math.max(0, Math.min(steps.length - 1, n));
    render();
  }

  /* Dodir na karticu bira odgovor i sam vodi na sljedeci korak. */
  form.addEventListener('click', function (e) {
    var opt = e.target.closest('.wopt');
    if (opt) {
      var group = opt.closest('.wopts');
      Array.prototype.forEach.call(group.querySelectorAll('.wopt'), function (b) {
        b.classList.remove('is-picked');
        b.setAttribute('aria-pressed', 'false');
      });
      opt.classList.add('is-picked');
      opt.setAttribute('aria-pressed', 'true');
      group.dataset.value = opt.dataset.value;
      if (i < steps.length - 1) { window.setTimeout(function () { go(i + 1); }, 160); }
      return;
    }
    if (e.target.closest('.wnav__back')) { go(i - 1); }
    if (e.target.closest('.wnav__next')) { go(i + 1); }
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    err.hidden = true;

    var data = {};
    Array.prototype.forEach.call(form.querySelectorAll('.wopts'), function (g) {
      data[g.dataset.name] = g.dataset.value || '';
    });
    Array.prototype.forEach.call(form.querySelectorAll('.wfield input, .wfield textarea'), function (f) {
      data[f.name] = f.value.trim();
    });

    if (!data.ime || !data.telefon) {
      err.textContent = t('nedostaje');
      err.hidden = false;
      return;
    }

    submit.disabled = true;
    var label = submit.querySelector('.btn__label');
    var old = label ? label.textContent : '';
    if (label) { label.textContent = t('salji'); }

    function ok() {
      form.hidden = true;
      if (done) { done.classList.add('is-shown'); }
    }

    function fail() {
      submit.disabled = false;
      if (label) { label.textContent = old; }
      err.textContent = t('greska');
      err.hidden = false;
    }

    if (!ENDPOINT) {
      /* Backend jos nije prikacen. Tok se moze isprobati, ali upit ne ide
         nigdje: bolje odmah reci nego tiho progutati poruku. */
      window.console.warn('NP Čelik: ENDPOINT je prazan, upit nije poslat.', data);
      ok();
      return;
    }

    /* GET sa parametrima u adresi, ne POST. Apps Script svaki POST preusmjeri
       na sesijsku adresu i usput ga pretvori u GET, cime se gubi telo
       zahtjeva. Uz to ide no-cors, jer Apps Script ne salje CORS zaglavlja.

       Posljedica no-cors: pretrazivac ne moze da procita odgovor, pa se
       potvrda prikazuje bez obzira na to da li je slanje uspjelo. Greska se
       vidi samo ako sam zahtjev pukne (nema mreze). To je poznata granica
       ovog nacina i stoji u apps-script/README.md. */
    data.strana = window.location.pathname;

    var upit = Object.keys(data).map(function (k) {
      return encodeURIComponent(k) + '=' + encodeURIComponent(data[k]);
    }).join('&');

    window.fetch(ENDPOINT + '?' + upit, { method: 'GET', mode: 'no-cors' })
      .then(ok)
      .catch(fail);
  });

  render();
}());
