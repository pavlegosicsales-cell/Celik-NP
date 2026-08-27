# -*- coding: utf-8 -*-
"""Sklapa usluge.html i pod-stranice usluga iz zajednickih dijelova index.html.

Zajednicko (sprite, zaglavlje, mobilni meni, podnozje, lightbox, skripta) se
NE prepisuje rucno nego se vadi iz index.html, pa jedna izmjena u zaglavlju
ostaje tacna na svim stranicama. Sadrzaj svake stranice dolazi iz SADRZAJ
rjecnika na dnu.

Sekcije prate Konstra semu:
  lista   -> hero sa mrvicama + usluge jedna ispod druge
  detalj  -> hero, uvodni blok, obim posla u podblokovima, proces, CTA
Testimonial iz Konstre je izostavljen: nemamo nijednu pravu izjavu klijenta,
a izmisljene se ne pisu.
"""
import re, sys, pathlib

R = pathlib.Path(__file__).resolve().parent.parent
SITE = R / 'site'
IDX = (SITE / 'index.html').read_text(encoding='utf-8')


def between(start_pat, end_pat, text=IDX, keep=True):
    a = re.search(start_pat, text)
    b = re.search(end_pat, text[a.start():])
    seg = text[a.start(): a.start() + b.end()]
    return seg if keep else seg


# ---- zajednicki dijelovi, izvuceni iz index.html ----
SPRITE = between(r'<!-- =+\s*\n\s+SVG SPRITE', r'</svg>\s*\n')
HEADER = between(r'<header class="header"', r'</header>')
SMENU = between(r'<div class="smenu" id="smenu"', r'\n</div>\s*\n')
FOOTER = between(r'<footer class="footer"', r'</footer>')
SKIP = '<a class="skip-link" href="#main">Preskoči na sadržaj</a>'

# zaglavlje i meni na pod-stranicama moraju voditi NAZAD na pocetnu,
# jer #o-nama i #kontakt ne postoje na ovoj stranici
def relink(html, prefix='index.html'):
    return re.sub(r'href="#(hero|o-nama|usluge|radovi|kontakt|proces|rezultati)"',
                  lambda m: f'href="{prefix}#{m.group(1)}"', html)


HEAD_TPL = '''<!DOCTYPE html>
<html lang="sr-Latn-RS">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="geo.placename" content="Kragujevac">
<meta property="og:type" content="website">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{ogimg}">
<link rel="icon" href="assets/img/favicon.ico" sizes="any">
<link rel="icon" href="assets/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="css/tokens.css">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
'''

TAIL = '''
<script src="js/prevod.js" defer></script>
<script src="js/jezik.js" defer></script>
<script src="js/main.js" defer></script>

</body>
</html>
'''


def page(title, desc, ogimg, body, ogtitle=None):
    return (HEAD_TPL.format(title=title, desc=desc, ogimg=ogimg,
                            ogtitle=ogtitle or title)
            + SKIP + '\n\n' + SPRITE + '\n'
            + relink(HEADER) + '\n\n' + relink(SMENU) + '\n\n'
            + '<main id="main">\n' + body + '\n</main>\n\n'
            + relink(FOOTER) + TAIL)


# ---------------------------------------------------------------- komponente

def hero(eyebrow, title_html, lede, img, alt, crumbs):
    kr = ''.join(
        f'<li class="crumbs__item"><a href="{h}">{t}</a></li>' if h
        else f'<li class="crumbs__item" aria-current="page">{t}</li>'
        for t, h in crumbs)
    return f'''
  <section class="phero" aria-labelledby="phero-naslov">
    <figure class="phero__image" data-appear="image">
      <img src="{img}" alt="{alt}" width="1424" height="1774" fetchpriority="high" decoding="async">
      <div class="phero__overlay" aria-hidden="true"></div>
    </figure>

    <div class="phero__inner">
      <nav class="crumbs" aria-label="Putanja">
        <ol class="crumbs__list">{kr}</ol>
      </nav>
      <p class="phero__eyebrow" data-appear="text"><span class="dot" aria-hidden="true"></span>{eyebrow}</p>
      <h1 class="phero__title" id="phero-naslov" data-appear="text">{title_html}</h1>
      <p class="phero__lead" data-appear="text">{lede}</p>
    </div>
  </section>
'''


def cta(title, lede):
    return f'''
  <section class="pcta" aria-labelledby="pcta-naslov">
    <div class="pcta__inner" data-reveal>
      <h2 class="pcta__title" id="pcta-naslov">{title}</h2>
      <p class="pcta__lead">{lede}</p>
      <div class="pcta__actions">
        <a class="btn btn--solid" href="index.html#kontakt">
          <span class="btn__label" data-roll>Zatražite ponudu</span>
          <span class="btn__icons" aria-hidden="true">
            <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
            <svg class="btn__icon"><use href="#i-arrow-right"></use></svg>
          </span>
        </a>
        <a class="btn btn--bare" href="tel:0604145466">
          <span class="btn__label" data-roll>060 41 45 466</span>
          <span class="btn__icons" aria-hidden="true">
            <svg class="btn__icon"><use href="#i-phone"></use></svg>
            <svg class="btn__icon"><use href="#i-phone"></use></svg>
          </span>
        </a>
      </div>
    </div>
  </section>
'''


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('SPRITE ', len(SPRITE), 'B')
    print('HEADER ', len(HEADER), 'B')
    print('SMENU  ', len(SMENU), 'B')
    print('FOOTER ', len(FOOTER), 'B')
