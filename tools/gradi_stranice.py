# -*- coding: utf-8 -*-
"""Generise usluge.html, kontakt.html i o-nama.html po Konstrinoj semi.

Struktura i mjere: research/konstra-stranice-teardown.md
Zajednicki dijelovi se vade iz index.html preko tools/stranice.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from stranice import page, SITE
from usluge_sadrzaj import USLUGE
from galerija_sadrzaj import PROJEKTI

CHECK = '<svg aria-hidden="true" focusable="false"><use href="#i-check"></use></svg>'
ARROW = ('<span class="btn__icons" aria-hidden="true">'
         '<svg class="btn__icon"><use href="#i-arrow-right"></use></svg>'
         '<svg class="btn__icon"><use href="#i-arrow-right"></use></svg></span>')


def css(html):
    return html.replace('<link rel="stylesheet" href="css/styles.css">',
                        '<link rel="stylesheet" href="css/styles.css">\n'
                        '<link rel="stylesheet" href="css/stranice.css">')


def svijetlo(html):
    """Stranice sa tamnim heroom nose bijelo zaglavlje.

    Konstra bira izmedju "Desktop White" i "Desktop Black" po stranici.
    Ovo je do sada bio rucni korak poslije gradnje, pa se gubio na svakoj
    ponovnoj gradnji. Sada ide automatski.
    """
    return html.replace('<header class="header" id="header">',
                        '<header class="header header--light" id="header">')


def hero(title, lede, img, alt, crumbs):
    """Konstra Service Hero: 100vh, tamni overlay, mrvice iznad naslova."""
    kr = ''.join(
        f'<li class="crumbs__item"><a href="{h}">{t}</a></li>' if h
        else f'<li class="crumbs__item" aria-current="page">{t}</li>'
        for t, h in crumbs)
    return f'''
  <section class="phero" aria-labelledby="phero-naslov">
    <figure class="phero__image">
      <img src="{img}" alt="{alt}" fetchpriority="high" decoding="async">
    </figure>
    <div class="phero__overlay" aria-hidden="true"></div>

    <div class="phero__inner">
      <nav class="crumbs" aria-label="Putanja">
        <ol class="crumbs__list">{kr}</ol>
      </nav>
      <div class="phero__heading">
        <h1 class="phero__title" id="phero-naslov">{title}</h1>
        <p class="phero__lead">{lede}</p>
      </div>
    </div>
  </section>
'''


# ====================================================================== USLUGE
def gradi_usluge():
    """Spisak usluga koristi ISTI sticky rig kao pocetna (.svcs / .svc).

    Konstra na /service ima obicnu listu bez preklapanja. Ovdje se namjerno
    odstupa, na zahtjev: kartice se lijepe i preklapaju kao u sekciji Usluge
    na pocetnoj, da dvije stranice ne izgledaju kao dva razlicita sajta.
    Markup i klase su doslovno iste kao u index.html, mijenja se samo broj
    kartica: sest umjesto cetiri.
    """
    NL = chr(10)
    kartice = []

    for n, u in enumerate(USLUGE, 1):
        stavke = []
        for x in u['obim']:
            stavke.append(
                '                  <li class="scope__item">' + NL
                + '                    <span class="scope__icon" aria-hidden="true">'
                  '<svg><use href="#i-check"></use></svg></span>' + NL
                + '                    <span>' + x + '</span>' + NL
                + '                  </li>')
        scope = NL.join(stavke)

        if u['stranica']:
            cta = ('<a class="btn btn--outline-light svc__cta" href="usluga-'
                   + u['slug'] + '.html">'
                   '<span class="btn__label" data-roll>Pogledajte detaljno</span>'
                   + ARROW + '</a>')
        else:
            cta = ('<a class="btn btn--outline-light svc__cta" href="kontakt.html">'
                   '<span class="btn__label" data-roll>Pitajte za kontejner</span>'
                   + ARROW + '</a>')

        kartice.append(f'''
        <article class="svc" data-reveal style="--z: {n}">

          <div class="svc__media">
            <img src="{u['slika']}" alt="{u['alt']}" width="1169" height="878" loading="lazy" decoding="async">
          </div>

          <div class="svc__content">
            <div class="svc__info">
              <h2 class="svc__title">{u['naslov']}</h2>
              <p class="svc__desc">{u['kratko']}</p>
            </div>

            <div class="svc__foot">
              <div class="scope">
                <p class="scope__label">Obim posla:</p>
                <ul class="scope__list">
{scope}
                </ul>
              </div>
              {cta}
            </div>
          </div>

        </article>''')

    body = (hero('Usluge',
                 'Nađite posao koji odgovara vašem objektu, roku i budžetu. Sve radimo '
                 'istom ekipom: mera na licu mesta, izrada u radionici na Avalskoj, '
                 'zaštita i montaža.',
                 'assets/img/hero-usluge.jpg',
                 'Metalna konstrukcija u izradi, radovi NP Čelika',
                 [('Početna', 'index.html'), ('Usluge', None)])
            + NL + '  <section class="svcs svcs--lista" aria-label="Spisak usluga">'
            + NL.join(kartice)
            + NL + '  </section>' + NL)

    html = svijetlo(css(page(title='Usluge | NP Čelik Kragujevac',
                    desc='Metalne konstrukcije, kapije i ograde, stepeništa i protivpožarna '
                         'stepeništa, letnje bašte, enterijer i modularni kontejneri u Kragujevcu.',
                    ogimg='assets/img/hero-usluge.jpg', body=body)))
    (SITE / 'usluge.html').write_text(html, encoding='utf-8')
    return len(html)


def gradi_detalj(u):
    scope = '\n'.join(f'              <li>{CHECK}<span>{x}</span></li>' for x in u['obim'])
    blokovi = '\n'.join(f'''
      <article class="sitem" data-reveal>
        <div class="sitem__body">
          <h2 class="sitem__title">{t}</h2>
          <p class="sitem__desc">{d}</p>
          <p class="sitem__scope-title">{n}</p>
        </div>
      </article>''' for t, d, n in u['blokovi'])

    uvod = '\n'.join(f'          <p class="sitem__desc">{p}</p>' for p in u['uvod'])

    body = (hero(u['naslov'], u['kratko'], u['slika_hero'], u['alt'],
                 [('Početna', 'index.html'), ('Usluge', 'usluge.html'), (u['naslov'], None)])
            + f'''
  <section class="sindex" aria-labelledby="uvod-naslov">
    <div class="sindex__inner">

      <article class="sitem" data-reveal>
        <figure class="sitem__media">
          <img src="{u['slika']}" alt="{u['alt']}" width="1169" height="878" loading="lazy" decoding="async">
        </figure>
        <div class="sitem__body">
          <h2 class="sitem__title" id="uvod-naslov">{u['uvod_naslov']}</h2>
{uvod}
          <p class="sitem__scope-title">Obim posla:</p>
          <ul class="sitem__scope">
{scope}
          </ul>
          <a class="btn btn--solid" href="kontakt.html"><span class="btn__label" data-roll>Zatražite ponudu</span>{ARROW}</a>
        </div>
      </article>
{blokovi}

    </div>
  </section>
''')

    html = svijetlo(css(page(title=f'{u["naslov"]} | NP Čelik Kragujevac',
                    desc=u['kratko'][:230], ogimg=u['slika_hero'], body=body)))
    f = SITE / f'usluga-{u["slug"]}.html'
    f.write_text(html, encoding='utf-8')
    return f.name, len(html)


# ===================================================================== KONTAKT
KORACI = [
    ('posao', 'Šta vam treba?', [
        ('Kapija ili ograda', 'i-warehouse'), ('Letnja ili zatvorena bašta', 'i-flame'),
        ('Stepenište ili PP stepenište', 'i-hardhat'), ('Konstrukcija, hala, nadstrešnica', 'i-factory'),
        ('Modularni kontejner', 'i-warehouse'), ('Nešto drugo', 'i-cog')]),
    ('objekat', 'Kakav je objekat?', [
        ('Ugostiteljski lokal', 'i-flame'), ('Poslovni objekat ili firma', 'i-factory'),
        ('Kuća ili dvorište', 'i-hardhat'), ('Gradilište u toku', 'i-cog')]),
    ('gde', 'Gde je posao?', [
        ('Kragujevac', 'i-pin'), ('Šumadija, van Kragujevca', 'i-pin'),
        ('Centralna Srbija', 'i-pin'), ('Drugde', 'i-pin')]),
    ('kada', 'Za kada vam treba?', [
        ('Hitno', 'i-clock'), ('U toku ovog meseca', 'i-clock'),
        ('Pre sezone', 'i-calendar-check'), ('Još planiram', 'i-calendar-check')]),
]


def gradi_kontakt():
    koraci = []
    for n, (name, q, opts) in enumerate(KORACI):
        cards = '\n'.join(
            f'''            <button class="wopt" type="button" data-value="{o}" aria-pressed="false">
              <svg aria-hidden="true" focusable="false"><use href="#{ic}"></use></svg>
              <span>{o}</span>
            </button>''' for o, ic in opts)
        koraci.append(f'''
        <fieldset class="wstep{' is-active' if n == 0 else ''}">
          <legend class="wstep__q">{q}</legend>
          <div class="wopts" data-name="{name}">
{cards}
          </div>
        </fieldset>''')

    ticks = '\n'.join('          <span class="wizard__tick"></span>' for _ in range(len(KORACI) + 1))

    body = f'''
  <section class="kontakt" aria-labelledby="kontakt-naslov">
    <div class="kontakt__inner">

      <div class="kontakt__head">
        <p class="slabel"><span class="dot" aria-hidden="true"></span>Kontakt</p>
        <h1 class="kontakt__title" id="kontakt-naslov">Recite šta, gde i za kada. Ostalo je na nama.</h1>
        <p class="kontakt__lead">Čitamo svaki upit lično. Opišite posao, izlazimo na teren
          i merimo na licu mesta, pa dobijate raspisanu ponudu. Izlazak i procena su besplatni.</p>
      </div>

      <div class="kontakt__form">
        <form class="wizard" id="wizard" novalidate>
          <div class="wizard__bar" aria-hidden="true">
{ticks}
          </div>
          <p class="wizard__count" role="status">Korak 1 od {len(KORACI) + 1}</p>
{''.join(koraci)}

          <fieldset class="wstep">
            <legend class="wstep__q">Vaši podaci</legend>
            <div class="wfields">
              <div class="wfield">
                <label for="w-ime">Ime i prezime</label>
                <input id="w-ime" name="ime" type="text" autocomplete="name" required>
              </div>
              <div class="wfield">
                <label for="w-tel">Telefon</label>
                <input id="w-tel" name="telefon" type="tel" autocomplete="tel" required>
              </div>
              <div class="wfield wfield--full">
                <label for="w-mejl">Mejl, ako želite ponudu pismeno</label>
                <input id="w-mejl" name="mejl" type="email" autocomplete="email">
              </div>
              <div class="wfield wfield--full">
                <label for="w-opis">Dimenzije, rok, sve što znate o poslu</label>
                <textarea id="w-opis" name="opis" rows="4"></textarea>
              </div>
            </div>
            <p class="wizard__note">Javljamo se isti ili sledeći radni dan. Ako vam se žuri, pozovite 060 41 45 466.</p>
          </fieldset>

          <p class="wizard__err" role="alert" hidden></p>

          <div class="wnav">
            <button class="wnav__back" type="button" hidden>Nazad</button>
            <button class="btn btn--solid wnav__next" type="button"><span class="btn__label">Dalje</span>{ARROW}</button>
            <button class="btn btn--solid wnav__submit" type="submit" hidden><span class="btn__label">Pošaljite upit</span>{ARROW}</button>
          </div>
        </form>

        <div class="wizard__done" role="status">
          <h2>Upit je stigao</h2>
          <p>Javljamo se isti ili sledeći radni dan. Ako vam se žuri, pozovite 060 41 45 466.</p>
        </div>
      </div>

      <aside class="kontakt__intro">
        <div class="kontakt__details">
          <div class="kdetail">
            <span class="kdetail__label"><svg aria-hidden="true" focusable="false"><use href="#i-phone"></use></svg>Telefon</span>
            <a class="kdetail__value" href="tel:0604145466">060 41 45 466</a>
          </div>
          <div class="kdetail">
            <span class="kdetail__label"><svg aria-hidden="true" focusable="false"><use href="#i-mail"></use></svg>Mejl</span>
            <a class="kdetail__value" href="mailto:npcelik85@gmail.com">npcelik85@gmail.com</a>
          </div>
          <div class="kdetail">
            <span class="kdetail__label"><svg aria-hidden="true" focusable="false"><use href="#i-pin"></use></svg>Radionica</span>
            <a class="kdetail__value" href="https://www.google.com/maps/search/?api=1&amp;query=Avalska%2011%2C%20Kragujevac" target="_blank" rel="noopener noreferrer">Avalska 11, Kragujevac</a>
          </div>
          <div class="kdetail">
            <span class="kdetail__label"><svg aria-hidden="true" focusable="false"><use href="#i-clock"></use></svg>Radno vreme</span>
            <span class="kdetail__value">Pon–pet, 07–16h</span>
          </div>
        </div>
      </aside>

    </div>
  </section>

  <section class="next" aria-labelledby="sledi-naslov">
    <div class="next__inner">
      <div>
        <p class="slabel slabel--dark"><span class="dot" aria-hidden="true"></span>Šta sledi</p>
        <h2 class="next__title" id="sledi-naslov">Znate šta se dešava posle upita</h2>
      </div>
      <div class="next__grid">
        <article class="nstep" data-reveal>
          <span class="nstep__num">01</span>
          <h3 class="nstep__title">Čitamo upit</h3>
          <p>Upit stiže direktno nama, ne u zajednički sandučić. Javljamo se isti ili sledeći radni dan.</p>
        </article>
        <article class="nstep" data-reveal>
          <span class="nstep__num">02</span>
          <h3 class="nstep__title">Izlazak i mera</h3>
          <p>Dolazimo na lokaciju, merimo na licu mesta i predlažemo rešenje. Izlazak i procena su besplatni.</p>
        </article>
        <article class="nstep" data-reveal>
          <span class="nstep__num">03</span>
          <h3 class="nstep__title">Raspisana ponuda</h3>
          <p>Dobijate ponudu stavku po stavku: materijal, zaštita, rok i cena. Rok stoji u ponudi, ne dogovara se usput.</p>
        </article>
      </div>
    </div>
  </section>
'''

    html = css(page(title='Kontakt | NP Čelik Kragujevac',
                    desc='Pozovite 060 41 45 466 ili pošaljite upit. Bravarska radionica na '
                         'Avalskoj 11 u Kragujevcu. Izlazak na teren i procena su besplatni.',
                    ogimg='assets/img/rad-01-celicna-hala.jpg', body=body))
    html = html.replace('<script src="js/main.js" defer></script>',
                        '<script src="js/main.js" defer></script>\n'
                        '<script src="js/wizard.js" defer></script>')
    (SITE / 'kontakt.html').write_text(html, encoding='utf-8')
    return len(html)


LIGHTBOX = '''<!-- Pregled fotografije referenci. Isti markup i ista skripta kao na pocetnoj. -->
<div class="lightbox" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Pregled fotografije">
  <button class="lightbox__close" type="button" aria-label="Zatvorite pregled">
    <svg aria-hidden="true" focusable="false"><use href="#i-close"></use></svg>
  </button>
  <img class="lightbox__img" alt="">
</div>

<script src="js/main.js" defer></script>'''


# ==================================================================== GALERIJA
def gradi_galeriju():
    """Po Konstrinoj /project: hero preko cijelog ekrana pa mreza kartica.

    Mjere iz izvora (konstra-project-lista.html):
      Hero      100vh, padding 216px 72px 64px, veo #00000080
      Sekcija   #FFF7E5, padding 112px 72px, kontejner 1320
      Kartica   632 sirine, padding 32, overflow hidden, slika preko cijele
                povrsine, veo preko nje, podaci na dnu
      Tacka     7px, razdvaja tip posla od mjesta

    Kartica otvara fotografiju u lightboxu, isto kao Radovi na pocetnoj.
    """
    NL = chr(10)
    kartice = []
    for p in PROJEKTI:
        kartice.append(f'''
        <a class="gcard" href="assets/img/{p["slika"]}" data-lightbox data-reveal>
          <span class="gcard__media">
            <img src="assets/img/{p["slika"]}" alt="" width="{p["w"]}" height="{p["h"]}" loading="lazy" decoding="async">
          </span>
          <span class="gcard__veil" aria-hidden="true"></span>
          <span class="gcard__body">
            <span class="gcard__meta">
              <span>{p["tip"]}</span>
              <span class="gcard__dot" aria-hidden="true"></span>
              <span>{p["mjesto"]}</span>
            </span>
            <span class="gcard__name">{p["naziv"]}</span>
          </span>
          <span class="visually-hidden">{p["alt"]}</span>
        </a>''')

    body = (hero('Galerija',
                 'Radovi NP Čelika u Kragujevcu i Šumadiji. Kliknite na fotografiju '
                 'da je vidite u punoj veličini.',
                 'assets/img/deking-bazen-zalazak.jpg',
                 'Deking uz bazen i metalna konstrukcija nadstrešnice, u zalazak sunca',
                 [('Početna', 'index.html'), ('Galerija', None)])
            + NL + '  <section class="gal" aria-label="Fotografije radova">'
            + NL + '    <div class="gal__grid">'
            + NL.join(kartice)
            + NL + '    </div>'
            + NL + '  </section>' + NL)

    html = svijetlo(css(page(title='Galerija radova | NP Čelik Kragujevac',
                    desc='Fotografije radova NP Čelika u Kragujevcu i Šumadiji: bašte, '
                         'stepeništa, kapije, ograde, platforme i modularni kontejneri.',
                    ogimg='assets/img/rad-05-montaza-na-terenu.jpg', body=body)))
    html = html.replace('<script src="js/main.js" defer></script>', LIGHTBOX)
    (SITE / 'galerija.html').write_text(html, encoding='utf-8')
    return len(html)


# ====================================================================== O NAMA
def gradi_o_nama():
    body = f'''
  <section class="ahero" aria-labelledby="onama-naslov">
    <div class="ahero__inner">
      <p class="slabel"><span class="dot" aria-hidden="true"></span>O nama</p>
      <h1 class="ahero__title" id="onama-naslov">Radionica sa adresom,<br>ekipa sa imenom.</h1>
      <p class="ahero__lead">NP Čelik radi na Avalskoj 11 u Kragujevcu od 2018. Mera, izrada,
        antikorozivna zaštita i montaža su naša ekipa, pa nema situacije da bravar krivi
        farbara, a farbar montera. Jedan sagovornik od prvog poziva do skidanja zaštitne folije.</p>
      <div class="ahero__actions">
        <a class="btn btn--solid" href="kontakt.html"><span class="btn__label" data-roll>Zatražite ponudu</span>{ARROW}</a>
        <a class="btn btn--bare" href="usluge.html"><span class="btn__label" data-roll>Pogledajte usluge</span>{ARROW}</a>
      </div>
    </div>

    <!-- ====================================================================
         Po Konstrinoj /about sekciji "Mission". Mjere su citane iz izvora
         (B-Steel/research/konstra-source/konstra-about.html), ne procijenjene:

           Bg Image   position: sticky, top 0, sirina 100%, odnos 1.49817
                      (961px visine na ekranu od 1440), will-change: filter
           Kartica    886 x auto, padding 32, radius 12, unutrasnji razmak 40,
                      apsolutno centrirana preko slike, meka visestruka sjenka
           Slika u kartici  266 x 315
           Tekst      naslov + dva pasusa, razmak 20

         Original ima ukupnu visinu 2439 pri slici od 961, dakle 1478px
         skrola. Toliko je i ovdje: .msn__rail. Kroz taj skrol se pozadina
         zamucuje, a prva kartica smjenjuje drugom.
         ==================================================================== -->
    <section class="msn" aria-label="Šta radimo i za koga radimo">
      <div class="msn__stage">
        <div class="msn__bg">
          <!-- Bela pergola sa lamelama, Ženeva Lux. Fotografija je kvadratna,
               a rig je 3:2, pa object-fit: cover sece gore i dole. -->
          <img src="assets/img/pergola-zeneva-lux.jpg" alt="" width="1424" height="1424" loading="lazy" decoding="async">
        </div>

        <article class="msn__card" data-msn-card>
          <div class="msn__media">
            <img src="assets/img/proces-skelet-hale.jpg" alt="Metalna konstrukcija platforme sa daskom 50 mm, MATIS New Point" width="988" height="1170" loading="lazy" decoding="async">
          </div>
          <div class="msn__body">
            <p class="slabel"><span class="dot" aria-hidden="true"></span>Šta radimo</p>
            <h2 class="msn__title">Od maske za klimu do noseće konstrukcije</h2>
            <p>Radimo i tehnički zahtevne poslove sa projektom i odgovornošću,
              i sitne dorade u dvorištu.</p>
            <p>Protivpožarna stepeništa, platforme i krovne konstrukcije su posao
              koji nas odvaja od radionica koje rade samo tipske ograde.</p>
          </div>
        </article>

        <article class="msn__card" data-msn-card>
          <div class="msn__media">
            <img src="assets/img/rad-05-montaza-na-terenu.jpg" alt="Zatvorena bašta sa drvenom tavanicom, Mileva Koncept, Grivac" width="1169" height="1558" loading="lazy" decoding="async">
          </div>
          <div class="msn__body">
            <p class="slabel"><span class="dot" aria-hidden="true"></span>Za koga radimo</p>
            <h2 class="msn__title">Ugostitelji, firme i ljudi iz komšiluka</h2>
            <p>Znamo šta znači „mora da bude gotovo pre sezone" i planiramo posao
              oko tog datuma. Zato se bašte ugovaraju zimi.</p>
            <p>Isto tako izlazimo i za jednu masku za klima uređaj, jer je mala
              stvar danas često prvi posao od nekoliko.</p>
          </div>
        </article>
      </div>

      <!-- Duzina skrola kroz koju traje smjena. Na telefonu se gasi. -->
      <div class="msn__rail" aria-hidden="true"></div>
    </section>
  </section>

  <!-- ==========================================================================
       Po Konstrinoj /about sekciji "Core Value". Mjere iz izvora:

         Sekcija  padding 112px 72px, razmak 72px
         Sticky   position sticky, top 0, visina 100vh, min-height 820px
         Kolona   300px, cetiri u redu sa razmakom 32 (1296 ukupno)
         Lenjir   14px sirok, 254px visok, dvije tacke od 12px na krajevima,
                  linija 2px na sredini. Pri skrolu se skuplja na 133px i
                  tekst ispod se podigne.
         Plocica  padding 4px 12px, radius 4px
         Razmaci  broj->lenjir 16, plocica->tekst 40, naslov->opis 12
         Skrol    cetiri odsjecka po 496px, jedan po koloni
       ========================================================================== -->
  <section class="cvals" aria-labelledby="pravila-naslov">
    <div class="cvals__sticky">
      <div class="cvals__head">
        <p class="slabel"><span class="dot" aria-hidden="true"></span>Kako radimo</p>
        <h2 class="cvals__title" id="pravila-naslov" data-scroll-fill>Pravila koja se vide posle pet godina</h2>
      </div>

      <div class="cvals__row">
        <article class="cval" data-cval>
          <div class="cval__mark">
            <span class="cval__num">01</span>
            <span class="cval__rule" aria-hidden="true"></span>
          </div>
          <div class="cval__body">
            <p class="cval__tag">Bez prebacivanja odgovornosti</p>
            <div class="cval__text">
              <h3 class="cval__title">Ceo posao pod jednim krovom</h3>
              <p>Mera, izrada, zaštita i montaža su naša ekipa. Nema prebacivanja odgovornosti
                između bravara, farbara i montera, jer su to isti ljudi.</p>
            </div>
          </div>
        </article>
        <article class="cval" data-cval>
          <div class="cval__mark">
            <span class="cval__num">02</span>
            <span class="cval__rule" aria-hidden="true"></span>
          </div>
          <div class="cval__body">
            <p class="cval__tag">Garancija dve godine</p>
            <div class="cval__text">
              <h3 class="cval__title">Zaštita je deo posla, ne dodatak</h3>
              <p>Priprema površine, pocinkovanje ili plastifikacija i svi nanosi boje. Ograda bez
                pripreme i cinka počne da rđa kroz dve zime i onda se plaća dvaput.</p>
            </div>
          </div>
        </article>
        <article class="cval" data-cval>
          <div class="cval__mark">
            <span class="cval__num">03</span>
            <span class="cval__rule" aria-hidden="true"></span>
          </div>
          <div class="cval__body">
            <p class="cval__tag">Ne dogovara se usput</p>
            <div class="cval__text">
              <h3 class="cval__title">Rok stoji u ponudi</h3>
              <p>Ako nešto ne stižemo, kažemo unapred, jer je bolje čuti istinu na početku nego
                datum koji ne možemo da ispunimo.</p>
            </div>
          </div>
        </article>
        <article class="cval" data-cval>
          <div class="cval__mark">
            <span class="cval__num">04</span>
            <span class="cval__rule" aria-hidden="true"></span>
          </div>
          <div class="cval__body">
            <p class="cval__tag">Radionica na Avalskoj 11</p>
            <div class="cval__text">
              <h3 class="cval__title">Vraćamo se na svoj rad</h3>
              <p>Kad kroz godinu dana zapne kapija ili treba dorada, ne tražite firmu iz Beograda.
                Tu smo gde smo i bili.</p>
            </div>
          </div>
        </article>
      </div>

      <div class="cvals__nav" aria-hidden="true">
        <button class="cvals__arrow" type="button" data-cvals-prev aria-label="Prethodno pravilo">
          <svg aria-hidden="true" focusable="false"><use href="#i-arrow-right"></use></svg>
        </button>
        <button class="cvals__arrow cvals__arrow--on" type="button" data-cvals-next aria-label="Sledeće pravilo">
          <svg aria-hidden="true" focusable="false"><use href="#i-arrow-right"></use></svg>
        </button>
      </div>
    </div>

    <div class="cvals__rail" aria-hidden="true"></div>
    <div class="cvals__rail" aria-hidden="true"></div>
    <div class="cvals__rail" aria-hidden="true"></div>
    <div class="cvals__rail" aria-hidden="true"></div>
  </section>

  <!-- ==========================================================================
       Po Konstrinoj "Build Stages" sa pocetne. Mjere iz izvora:
         Sekcija   padding 112px 72px, razmak 72
         Zaglavlje red, naslov lijevo, podnaslov desno, poravnati po dnu
         Sadrzaj   red, razmak 64, koraci lijevo, slika desno
         Korak     red, razmak 24, padding 32px 0 0; broj 56px, radius 50px,
                   padding 12px 16px; tijelo padding 8px 0 32px sa linijom
         Slika     sticky top 80, max-width 50%, odnos 0.8556, radius 12
       ========================================================================== -->
  <section class="hist" aria-labelledby="istorija-naslov">
    <div class="hist__inner">
      <div class="hist__head">
        <div class="hist__title-wrap">
          <p class="slabel"><span class="dot" aria-hidden="true"></span>Put</p>
          <h2 class="hist__title" id="istorija-naslov">Kako je radionica rasla</h2>
        </div>
        <p class="hist__lead">Osam godina, preko dvadeset objekata i sopstvena radionica
          na Avalskoj 11.</p>
      </div>

      <div class="hist__body">
        <ol class="hist__steps">
          <li class="hstep">
            <span class="hstep__num">01</span>
            <div class="hstep__body">
              <div class="hstep__head">
                <h3 class="hstep__title">Radionica na Avalskoj</h3>
                <span class="hstep__year">2018</span>
              </div>
              <p>NP Čelik počinje sa radom u Kragujevcu. Bravarski radovi, kapije i ograde
              za dvorišta i firme u gradu.</p>
            </div>
          </li>
          <li class="hstep">
            <span class="hstep__num">02</span>
            <div class="hstep__body">
              <div class="hstep__head">
                <h3 class="hstep__title">Prve letnje bašte</h3>
                <span class="hstep__year">2021</span>
              </div>
              <p>Rad na ugostiteljskim objektima u Kragujevcu i okolini. Kafana Paligorić,
              „Stara Srbija", Caffe Porta.</p>
            </div>
          </li>
          <li class="hstep">
            <span class="hstep__num">03</span>
            <div class="hstep__body">
              <div class="hstep__head">
                <h3 class="hstep__title">Modularni kontejneri</h3>
                <span class="hstep__year">2023</span>
              </div>
              <p>Serija NP Čelik kontejnera: stambeni, magacinski, građevinski i sanitarni.
              Za razliku od svega ostalog što radimo po meri, ovo je proizvod sa poznatim rokom.</p>
            </div>
          </li>
          <li class="hstep">
            <span class="hstep__num">04</span>
            <div class="hstep__body">
              <div class="hstep__head">
                <h3 class="hstep__title">Preko dvadeset objekata</h3>
                <span class="hstep__year">2026</span>
              </div>
              <p>Sopstvena radionica i montaža. Protivpožarna stepeništa, zatvorene bašte
              i konstrukcije po projektu.</p>
            </div>
          </li>
        </ol>

        <div class="hist__media">
          <!-- [SLIKA: privremena] Spoljno metalno stepeniste. Zamijeniti kad
               klijent posalje fotografiju koja bolje stoji uz "Put". -->
          <img src="assets/img/rad-06-nadstresnica-garaza.jpg" alt="Spoljno metalno stepenište, NP Čelik" width="1169" height="1558" loading="lazy" decoding="async">
        </div>
      </div>
    </div>
  </section>


  <section class="arefs" aria-labelledby="reference-naslov">
    <div class="arefs__inner">
      <p class="slabel"><span class="dot" aria-hidden="true"></span>Reference</p>
      <h2 class="arefs__title" id="reference-naslov">Radovi koje možete da obiđete</h2>

      <a class="rrow rrow--foto" href="assets/img/rad-05-montaza-na-terenu.jpg" data-lightbox><span class="rrow__num">01</span><span class="rrow__name">Mileva Koncept</span><span class="rrow__meta">Zatvorena bašta · Grivac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Zatvorena bašta sa drvenom tavanicom, Mileva Koncept, Grivac</span></a>
      <a class="rrow rrow--foto" href="assets/img/hero-radnici-zalazak.jpg" data-lightbox><span class="rrow__num">02</span><span class="rrow__name">Ženeva Lux</span><span class="rrow__meta">Protivpožarna stepeništa · Kragujevac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Protivpožarno metalno stepenište, Ženeva Lux</span></a>
      <a class="rrow rrow--foto" href="assets/img/rad-04-detalj-spoja.jpg" data-lightbox><span class="rrow__num">03</span><span class="rrow__name">Caffe Porta</span><span class="rrow__meta">Krovna konstrukcija · Kragujevac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Krovne rešetke i noseća konstrukcija, Caffe Porta</span></a>
      <div class="rrow"><span class="rrow__num">04</span><span class="rrow__name">Kafana Paligorić</span><span class="rrow__meta">Letnja bašta · Kragujevac</span></div>
      <a class="rrow rrow--foto" href="assets/img/rad-nadstresnica-terasa.jpg" data-lightbox><span class="rrow__num">05</span><span class="rrow__name">Stara Srbija</span><span class="rrow__meta">Zastakljena bašta · Kragujevac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Zastakljena letnja bašta, kafana Stara Srbija</span></a>
      <a class="rrow rrow--foto" href="assets/img/hero-celicna-konstrukcija.jpg" data-lightbox><span class="rrow__num">06</span><span class="rrow__name">Lokal „Čudesa"</span><span class="rrow__meta">Enterijer i šank · Kragujevac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Metalni enterijer i šank, lokal Čudesa</span></a>
      <a class="rrow rrow--foto" href="assets/img/rad-nadstresnica-solarni-jesenice.jpg" data-lightbox><span class="rrow__num">07</span><span class="rrow__name">Blazeks MV</span><span class="rrow__meta">Ograda i gelenderi · Aerodrom</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Ograda obložena kompaktom, Blazeks MV</span></a>
      <a class="rrow rrow--foto" href="assets/img/rad-06-nadstresnica-garaza.jpg" data-lightbox><span class="rrow__num">08</span><span class="rrow__name">BLAŽEKS nameštaj</span><span class="rrow__meta">Stepenište · Sušica</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Spoljno metalno stepenište, BLAŽEKS nameštaj, Sušica</span></a>
      <a class="rrow rrow--foto" href="assets/img/proces-skelet-hale.jpg" data-lightbox><span class="rrow__num">09</span><span class="rrow__name">MATIS New Point</span><span class="rrow__meta">Platforma · Kragujevac</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Metalna konstrukcija platforme, MATIS New Point</span></a>
      <a class="rrow rrow--foto" href="assets/img/rad-01-celicna-hala.jpg" data-lightbox><span class="rrow__num">10</span><span class="rrow__name">Kapija „DOSTOJNA"</span><span class="rrow__meta">Sa Simetra d.o.o. · Kutlovo</span><span class="rrow__see" aria-hidden="true">Fotografija<svg><use href="#i-arrow-right"></use></svg></span><span class="visually-hidden">Dekorativna klizna kapija DOSTOJNA, Kutlovo</span></a>
      <div class="rrow"><span class="rrow__num">11</span><span class="rrow__name">Ford salon</span><span class="rrow__meta">Klizne kapije i 3D paneli</span></div>
    </div>
  </section>

  <!-- ==========================================================================
       Zavrsna traka po Konstrinoj CTA sekciji: fotografija preko cijele
       sirine, tamni veo, tekst lijevo dolje, jedno puno dugme.
       Fotografija: modularni kontejner NP Čelika, snimljen protiv sunca.
       ========================================================================== -->
  <section class="ocean" aria-labelledby="ocean-naslov">
    <div class="ocean__media">
      <img src="assets/img/modularni-kontejner-zora.jpg" alt="" width="1456" height="1456" loading="lazy" decoding="async">
    </div>
    <div class="ocean__inner">
      <h2 class="ocean__title" id="ocean-naslov">Recite šta vam treba,<br>izlazimo i merimo.</h2>
      <p class="ocean__lead">Izlazak na teren i procena su besplatni. Posle mere dobijate
        raspisanu ponudu, sa rokom koji stoji u njoj.</p>
      <div class="ocean__actions">
        <a class="btn btn--solid" href="kontakt.html"><span class="btn__label" data-roll>Zatražite ponudu</span><span class="btn__icons" aria-hidden="true"><svg class="btn__icon"><use href="#i-arrow-right"></use></svg><svg class="btn__icon"><use href="#i-arrow-right"></use></svg></span></a>
        <a class="btn btn--outline btn--on-dark-outline" href="tel:0604145466"><span class="btn__label" data-roll>060 41 45 466</span><span class="btn__icons" aria-hidden="true"><svg class="btn__icon"><use href="#i-phone"></use></svg><svg class="btn__icon"><use href="#i-phone"></use></svg></span></a>
      </div>
    </div>
  </section>
'''

    html = css(page(title='O nama | NP Čelik Kragujevac',
                    desc='Bravarska radionica na Avalskoj 11 u Kragujevcu od 2018. Četvoro ljudi, '
                         'preko dvadeset objekata, mera i izrada i montaža sopstvenom ekipom.',
                    ogimg='assets/img/rad-05-montaza-na-terenu.jpg', body=body))
    # Reference se otvaraju u lightboxu, pa stranici treba isti okvir kao pocetnoj.
    html = html.replace('<script src="js/main.js" defer></script>', LIGHTBOX)
    (SITE / 'o-nama.html').write_text(html, encoding='utf-8')
    return len(html)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(f'{"usluge.html":36} {gradi_usluge()//1024:3} KB')
    for u in USLUGE:
        if u['stranica']:
            n, s = gradi_detalj(u)
            print(f'{n:36} {s//1024:3} KB')
    print(f'{"kontakt.html":36} {gradi_kontakt()//1024:3} KB')
    print(f'{"o-nama.html":36} {gradi_o_nama()//1024:3} KB')
    print(f'{"galerija.html":36} {gradi_galeriju()//1024:3} KB')

    # Generisane strane nose samo osnovni <head>. Canonical, twitter kartice
    # i JSON-LD upisuje seo.py, pa se pusta odmah poslije gradnje.
    print()
    import seo
    seo.main()

    # Hash u adresi css i js fajlova, da pretrazivac ne vrti staru kopiju.
    print()
    import verzija
    verzija.main()
