# -*- coding: utf-8 -*-
"""SEO pass po pravilima skilla website-build-rules (korak 6).

Sto radi:
  1. Prepisuje <title> i <meta name="description"> po specifikaciji
     (naslov ispod 60 znakova, opis 140-155 znakova, aktivan glas).
  2. Dodaje canonical, og:url, og:site_name, og:locale i twitter kartice.
     og:image postaje apsolutan, jer relativan Facebook i Twitter ne citaju.
  3. Ubacuje JSON-LD: LocalBusiness na pocetnoj, Service na svakoj
     pod-stranici usluge, BreadcrumbList gdje postoje mrvice.
  4. Pise sitemap.xml i upisuje Sitemap red u robots.txt.

Pusta se iz korena projekta:  python tools/seo.py
Provjera bez pisanja:         python tools/seo.py --provjeri
"""
import json
import re
import sys
import pathlib

R = pathlib.Path(__file__).resolve().parent.parent
SITE = R / 'site'

# Domen. Sajt jos nema svoj, pa stoji Vercel adresa. Kad stigne pravi domen
# mijenja se SAMO ova linija, pa se skripta pusti ponovo.
BASE = 'https://celik-np.vercel.app'

FIRMA = 'NP Čelik'
TELEFON = '+381604145466'
TELEFON_TEKST = '060 41 45 466'
MEJL = 'npcelik85@gmail.com'
ULICA = 'Avalska 11'
GRAD = 'Kragujevac'
PTT = '34000'

# ---------------------------------------------------------------- sadrzaj

STRANE = {
    'index.html': dict(
        slug='',
        title='Metalne konstrukcije i bravarija Kragujevac | NP Čelik',
        desc='Bravarska radionica u Kragujevcu od 2018. Radimo metalne konstrukcije, '
             'kapije, ograde, stepeništa i letnje bašte. Mera, izrada i montaža jednom ekipom.',
        ogimg='assets/img/hero-celicna-konstrukcija.jpg',
    ),
    'usluge.html': dict(
        slug='usluge.html',
        title='Usluge | NP Čelik Kragujevac',
        desc='Šest usluga NP Čelika u Kragujevcu: nosive konstrukcije, kapije i ograde, '
             'stepeništa, letnje bašte, enterijer i modularni kontejneri. Izlazak je besplatan.',
        ogimg='assets/img/hero-usluge.jpg',
    ),
    'usluga-metalne-konstrukcije.html': dict(
        slug='usluga-metalne-konstrukcije.html',
        title='Nosive metalne konstrukcije | NP Čelik Kragujevac',
        desc='Krovne i međuspratne konstrukcije i platforme po projektu, u Kragujevcu. '
             'Otvoren prostor bez stubova, brža gradnja nego betonom, manje opterećenje.',
        ogimg='assets/img/rad-04-detalj-spoja.jpg',
        usluga='Izrada i montaža nosivih metalnih konstrukcija',
        mrvica='Nosive konstrukcije',
    ),
    'usluga-kapije-i-ograde.html': dict(
        slug='usluga-kapije-i-ograde.html',
        title='Kapije i ograde | NP Čelik Kragujevac',
        desc='Klizne i krilne kapije, panelne i dvorišne ograde u Kragujevcu. Pocinkovano '
             'ili plastificirano, po meri placa. Izlazak na teren i procena su besplatni.',
        ogimg='assets/img/rad-01-celicna-hala.jpg',
        usluga='Izrada i montaža kapija i ograda',
        mrvica='Kapije i ograde',
    ),
    'usluga-stepenista.html': dict(
        slug='usluga-stepenista.html',
        title='Stepeništa i protivpožarna | NP Čelik Kragujevac',
        desc='Unutrašnja, spoljna i protivpožarna stepeništa u Kragujevcu. Miran hod bez '
             'škripe, gazišta po meri i zaštita koja izdrži zimu. Izlazimo i merimo besplatno.',
        ogimg='assets/img/rad-06-nadstresnica-garaza.jpg',
        usluga='Izrada i montaža stepeništa i protivpožarnih stepeništa',
        mrvica='Stepeništa',
    ),
    'usluga-letnje-baste.html': dict(
        slug='usluga-letnje-baste.html',
        title='Letnje i zatvorene bašte | NP Čelik Kragujevac',
        desc='Letnje i zatvorene bašte za kafiće i restorane u Kragujevcu. Više stolova i '
             'gost koji sedi po kiši i zimi. Bašte se ugovaraju zimi, pre same sezone.',
        ogimg='assets/img/rad-05-montaza-na-terenu.jpg',
        usluga='Izrada letnjih i zatvorenih bašti',
        mrvica='Letnje bašte',
    ),
    'usluga-deking-i-enterijer.html': dict(
        slug='usluga-deking-i-enterijer.html',
        title='Enterijer i završna obrada | NP Čelik Kragujevac',
        desc='Deking, drvena tavanica, staklo i kompakt ploče na metalnoj konstrukciji. '
             'Lokal u Kragujevcu dobija karakter, sve po meri prostora, a ne iz kataloga.',
        ogimg='assets/img/rad-poslovna-hala.jpg',
        usluga='Deking, enterijer i završna obrada',
        mrvica='Enterijer',
    ),
    'galerija.html': dict(
        slug='galerija.html',
        title='Galerija radova | NP Čelik Kragujevac',
        desc='Fotografije radova NP Čelika u Kragujevcu i Šumadiji: zatvorene bašte, '
             'stepeništa, kapije i ograde, platforme i modularni kontejneri.',
        ogimg='assets/img/rad-05-montaza-na-terenu.jpg',
    ),
    'o-nama.html': dict(
        slug='o-nama.html',
        title='O nama | NP Čelik Kragujevac',
        desc='NP Čelik radi na Avalskoj 11 u Kragujevcu od 2018. Preko dvadeset objekata, '
             'mera i izrada i montaža sopstvenom ekipom, garancija dve godine na zaštitu.',
        ogimg='assets/img/rad-05-montaza-na-terenu.jpg',
    ),
    'kontakt.html': dict(
        slug='kontakt.html',
        title='Kontakt | NP Čelik Kragujevac',
        desc='Pozovite 060 41 45 466 ili pošaljite upit kroz obrazac. Radionica je na '
             'Avalskoj 11 u Kragujevcu, radnim danima od 07 do 16h. Procena je besplatna.',
        ogimg='assets/img/rad-01-celicna-hala.jpg',
    ),
}


def lokal():
    """LocalBusiness za pocetnu. Samo potvrdjeni podaci iz context.md."""
    return {
        '@context': 'https://schema.org',
        '@type': 'HomeAndConstructionBusiness',
        '@id': BASE + '/#firma',
        'name': FIRMA,
        'url': BASE + '/',
        'telephone': TELEFON,
        'email': MEJL,
        'image': BASE + '/assets/img/hero-celicna-konstrukcija.jpg',
        'foundingDate': '2018',
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': ULICA,
            'addressLocality': GRAD,
            'postalCode': PTT,
            'addressCountry': 'RS',
        },
        'areaServed': [
            {'@type': 'City', 'name': 'Kragujevac'},
            {'@type': 'AdministrativeArea', 'name': 'Šumadijski okrug'},
            {'@type': 'AdministrativeArea', 'name': 'Centralna Srbija'},
        ],
        'openingHoursSpecification': [{
            '@type': 'OpeningHoursSpecification',
            'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'opens': '07:00',
            'closes': '16:00',
        }],
        'sameAs': [
            'https://www.instagram.com/celiknp/',
            'https://www.facebook.com/npcelikconstruction',
        ],
        'makesOffer': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': v['usluga']}}
            for v in STRANE.values() if v.get('usluga')
        ],
    }


def usluga_ld(p):
    return {
        '@context': 'https://schema.org',
        '@type': 'Service',
        'name': p['usluga'],
        'serviceType': p['mrvica'],
        'url': f"{BASE}/{p['slug']}",
        'areaServed': {'@type': 'City', 'name': 'Kragujevac'},
        'provider': {'@id': BASE + '/#firma'},
    }


def mrvice_ld(p):
    return {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Početna', 'item': BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Usluge', 'item': BASE + '/usluge.html'},
            {'@type': 'ListItem', 'position': 3, 'name': p['mrvica'],
             'item': f"{BASE}/{p['slug']}"},
        ],
    }


def blok(podaci):
    tekst = json.dumps(podaci, ensure_ascii=False, indent=2)
    return '<script type="application/ld+json">\n' + tekst + '\n</script>'


# ---------------------------------------------------------------- izmjene

MARKER = '<!-- SEO: canonical, drustvene mreze i strukturirani podaci -->'


def sredi(fajl, p, provjeri=False):
    put = SITE / fajl
    s = put.read_text(encoding='utf-8')

    kanon = BASE + '/' + p['slug']
    ogimg_abs = BASE + '/' + p['ogimg']

    # naslov i opis
    s = re.sub(r'<title>.*?</title>', '<title>' + p['title'] + '</title>', s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description" content=".*?">',
               '<meta name="description" content="' + p['desc'] + '">', s, count=1, flags=re.S)
    s = re.sub(r'<meta property="og:title" content=".*?">',
               '<meta property="og:title" content="' + p['title'] + '">', s, count=1, flags=re.S)
    s = re.sub(r'<meta property="og:description" content=".*?">',
               '<meta property="og:description" content="' + p['desc'] + '">', s, count=1, flags=re.S)
    s = re.sub(r'<meta property="og:image" content=".*?">',
               '<meta property="og:image" content="' + ogimg_abs + '">', s, count=1, flags=re.S)

    # stari blok napolje, pa novi umjesto njega
    s = re.sub(re.escape(MARKER) + r'.*?<!-- /SEO -->\n', '', s, flags=re.S)

    dodatak = [MARKER,
               '<link rel="canonical" href="' + kanon + '">',
               '<meta property="og:url" content="' + kanon + '">',
               '<meta property="og:site_name" content="' + FIRMA + '">',
               '<meta property="og:locale" content="sr_RS">',
               '<meta name="twitter:card" content="summary_large_image">',
               '<meta name="twitter:title" content="' + p['title'] + '">',
               '<meta name="twitter:description" content="' + p['desc'] + '">',
               '<meta name="twitter:image" content="' + ogimg_abs + '">']

    if fajl == 'index.html':
        dodatak.append(blok(lokal()))
    if p.get('usluga'):
        dodatak.append(blok(usluga_ld(p)))
        dodatak.append(blok(mrvice_ld(p)))
    dodatak.append('<!-- /SEO -->')

    s = s.replace('<link rel="icon"', '\n'.join(dodatak) + '\n<link rel="icon"', 1)

    if not provjeri:
        put.write_text(s, encoding='utf-8')
    return len(p['title']), len(p['desc'])


def sitemap():
    redovi = []
    for fajl, p in STRANE.items():
        redovi.append('  <url>\n    <loc>' + BASE + '/' + p['slug'] + '</loc>\n'
                      '    <changefreq>monthly</changefreq>\n'
                      '    <priority>' + ('1.0' if fajl == 'index.html' else '0.8') + '</priority>\n'
                      '  </url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">\n'.replace(
                'www.sitemap.org', 'www.sitemaps.org')
            + '\n'.join(redovi) + '\n</urlset>\n')


def main():
    provjeri = '--provjeri' in sys.argv
    sys.stdout.reconfigure(encoding='utf-8')
    print('naslov / opis (cilj: naslov < 60, opis 140-155)')
    for fajl, p in STRANE.items():
        nt, nd = sredi(fajl, p, provjeri)
        zn_t = 'ok' if nt < 60 else 'DUG'
        zn_d = 'ok' if 140 <= nd <= 155 else 'VAN OPSEGA'
        print(f'  {fajl:36s} naslov {nt:3d} {zn_t:3s}   opis {nd:3d} {zn_d}')

    if not provjeri:
        (SITE / 'sitemap.xml').write_text(sitemap(), encoding='utf-8')
        (SITE / 'robots.txt').write_text(
            'User-agent: *\nAllow: /\n\nSitemap: ' + BASE + '/sitemap.xml\n', encoding='utf-8')
        print('\nupisano: sitemap.xml, robots.txt')


if __name__ == '__main__':
    main()
