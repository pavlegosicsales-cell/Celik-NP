# -*- coding: utf-8 -*-
"""Generise usluge.html i pod-stranice usluga."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from stranice import page, hero, cta, SITE
from usluge_sadrzaj import USLUGE

CHECK = '<svg aria-hidden="true" focusable="false"><use href="#i-check"></use></svg>'


def link_css(html):
    """Unutrasnje stranice nose i stranice.css."""
    return html.replace('<link rel="stylesheet" href="css/styles.css">',
                        '<link rel="stylesheet" href="css/styles.css">\n'
                        '<link rel="stylesheet" href="css/stranice.css">')


# ------------------------------------------------------------------ LISTA
def gradi_listu():
    stavke = []
    for i, u in enumerate(USLUGE, 1):
        scope = '\n'.join(
            f'            <li>{CHECK}<span>{x}</span></li>' for x in u['obim'])
        if u['stranica']:
            dugme = f'''
          <a class="btn btn--solid" href="usluga-{u['slug']}.html">
            <span class="btn__label" data-roll>Pogledajte detaljno</span>
            <span class="btn__icons" aria-hidden="true">
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
            </span>
          </a>'''
        else:
            # Kontejneri nemaju pod-stranicu: jedna fotografija nije dovoljna
            # da se napuni cijela stranica. Dugme vodi pravo na upit.
            dugme = '''
          <a class="btn btn--bare" href="index.html#kontakt">
            <span class="btn__label" data-roll>Pitajte za kontejner</span>
            <span class="btn__icons" aria-hidden="true">
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
            </span>
          </a>'''

        stavke.append(f'''
      <article class="sitem" data-reveal>
        <figure class="sitem__media">
          <img src="{u['slika']}" alt="{u['alt']}" width="1169" height="878" loading="lazy" decoding="async">
        </figure>
        <div class="sitem__body">
          <span class="sitem__num">{i:02d}</span>
          <h2 class="sitem__title">{u['naslov']}</h2>
          <p class="sitem__desc">{u['kratko']}</p>
          <p class="sitem__scope-title">Obim posla</p>
          <ul class="sitem__scope">
{scope}
          </ul>{dugme}
        </div>
      </article>''')

    body = (
        hero(eyebrow='Usluge',
             title_html='Šta radimo,<br>od kapije do hale',
             lede='Nađite posao koji odgovara vašem objektu, roku i budžetu. '
                  'Sve radimo istom ekipom: mera na licu mesta, izrada u '
                  'radionici na Avalskoj, zaštita i montaža.',
             img='assets/img/hero-radnici-zalazak.jpg',
             alt='Spoljna protivpožarna metalna stepeništa na fasadi objekta Ženeva Lux',
             crumbs=[('Početna', 'index.html'), ('Usluge', None)])
        + '\n  <section class="slist" aria-label="Spisak usluga">\n'
          '    <div class="slist__inner">'
        + '\n'.join(stavke)
        + '\n    </div>\n  </section>\n'
        + cta('Ne vidite svoj posao na spisku?',
              'Radimo od maske za klima uređaj do hale. Recite šta, gde i za '
              'kada, pa izlazimo na teren i merimo. Izlazak i procena su besplatni.'))

    html = link_css(page(
        title='Usluge | NP Čelik Kragujevac',
        desc='Metalne konstrukcije, kapije i ograde, stepeništa i protivpožarna '
             'stepeništa, letnje bašte, enterijer i modularni kontejneri. '
             'Izrada i montaža, Kragujevac i Šumadija.',
        ogimg='assets/img/hero-radnici-zalazak.jpg',
        body=body))
    (SITE / 'usluge.html').write_text(html, encoding='utf-8')
    return len(html)


# ------------------------------------------------------------------ DETALJ
def gradi_detalj(u):
    blokovi = '\n'.join(f'''
        <article class="sblock" data-reveal>
          <h3 class="sblock__title">{t}</h3>
          <p class="sblock__desc">{d}</p>
          <p class="sblock__note">{n}</p>
        </article>''' for t, d, n in u['blokovi'])

    uvod = '\n'.join(f'          <p class="sblocks__lead">{p}</p>' for p in u['uvod'])
    scope = '\n'.join(f'            <li>{CHECK}<span>{x}</span></li>' for x in u['obim'])

    body = (
        hero(eyebrow='Usluga',
             title_html=u['naslov_hero'],
             lede=u['kratko'],
             img=u['slika_hero'], alt=u['alt'],
             crumbs=[('Početna', 'index.html'), ('Usluge', 'usluge.html'),
                     (u['naslov'], None)])
        + f'''
  <section class="sblocks" aria-labelledby="uvod-naslov">
    <div class="sblocks__inner">
      <div class="sblocks__head" data-reveal>
        <h2 class="sblocks__title" id="uvod-naslov">{u['uvod_naslov']}</h2>
{uvod}
      </div>

      <div class="sblocks__grid">{blokovi}
      </div>
    </div>
  </section>

  <section class="slist" aria-labelledby="obim-naslov">
    <div class="slist__inner">
      <article class="sitem" data-reveal>
        <figure class="sitem__media">
          <img src="{u['slika']}" alt="{u['alt']}" width="1169" height="878" loading="lazy" decoding="async">
        </figure>
        <div class="sitem__body">
          <h2 class="sitem__title" id="obim-naslov">Obim posla</h2>
          <p class="sitem__desc">Šta ulazi u ponudu kad se dogovorimo. Tačan
            spisak i rok stoje u pisanoj ponudi, ne dogovaraju se usput.</p>
          <ul class="sitem__scope">
{scope}
          </ul>
          <a class="btn btn--solid" href="usluge.html">
            <span class="btn__label" data-roll>Sve usluge</span>
            <span class="btn__icons" aria-hidden="true">
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
              <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
            </span>
          </a>
        </div>
      </article>
    </div>
  </section>
'''
        + cta(f'Treba vam {u["naslov"].lower()}?',
              'Recite šta, gde i za kada. Izlazimo na teren, merimo na licu '
              'mesta i dobijate raspisanu ponudu. Izlazak i procena su besplatni.'))

    html = link_css(page(
        title=f'{u["naslov"]} | NP Čelik Kragujevac',
        desc=u['kratko'][:230],
        ogimg=u['slika_hero'],
        body=body))
    f = SITE / f'usluga-{u["slug"]}.html'
    f.write_text(html, encoding='utf-8')
    return f.name, len(html)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    n = gradi_listu()
    print(f'{"usluge.html":38} {n//1024:3} KB')
    for u in USLUGE:
        if u['stranica']:
            name, size = gradi_detalj(u)
            print(f'{name:38} {size//1024:3} KB')
