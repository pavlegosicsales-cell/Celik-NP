# -*- coding: utf-8 -*-
"""Pise site/js/prevod.js iz rjecnika i provjerava pokrivenost.

Pusta se iz korena projekta:
    python tools/prevod.py            upisuje js/prevod.js
    python tools/prevod.py --provjeri samo javlja sta nije prevedeno

Provjera prolazi kroz sve strane u site/ i vadi:
  - vidljive tekstualne cvorove (bez script, style, svg)
  - atribute alt, placeholder, title, aria-label
  - <title> i meta description
Sve sto nije u rjecniku se ispisuje, pa se rjecnik dopuni.
"""
import json
import re
import sys
import glob
import pathlib
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from prevod_recnik import PREVOD

R = pathlib.Path(__file__).resolve().parent.parent
SITE = R / 'site'

PRESKOCI = {'script', 'style', 'svg'}
ATRIBUTI = ('alt', 'placeholder', 'title', 'aria-label')


class Citac(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dubina = 0
        self.tekst = []
        self.attr = []

    def handle_starttag(self, tag, attrs):
        if tag in PRESKOCI:
            self.dubina += 1
        for k, v in attrs:
            if k in ATRIBUTI and v and v.strip():
                self.attr.append(' '.join(v.split()))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag in PRESKOCI:
            self.dubina -= 1

    def handle_endtag(self, tag):
        if tag in PRESKOCI and self.dubina:
            self.dubina -= 1

    def handle_data(self, data):
        if self.dubina:
            return
        d = ' '.join(data.split())
        if d and len(d) > 1:
            self.tekst.append(d)


def bez_prevoda(s):
    """Brojevi, tacke i sami znaci se ne prevode."""
    if re.fullmatch(r'[\d\s+.,·/%–—-]+', s):
        return True
    # Oznake na samom prekidacu jezika ostaju iste u oba jezika.
    return s in {'NP ČELIK', '·', '→', 'SR', 'EN'}


def skupi():
    svi = {}
    for f in sorted(glob.glob(str(SITE / '*.html'))):
        c = Citac()
        c.feed(pathlib.Path(f).read_text(encoding='utf-8'))
        for x in c.tekst + c.attr:
            if not bez_prevoda(x):
                svi.setdefault(x, set()).add(pathlib.Path(f).name)
    return svi


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    svi = skupi()
    nedostaje = sorted([k for k in svi if k not in PREVOD], key=len)

    print(f'stringova na sajtu: {len(svi)}')
    print(f'u rjecniku:         {len(PREVOD)}')
    print(f'nedostaje:          {len(nedostaje)}')
    for k in nedostaje:
        print('   -', k, ' ->', sorted(svi[k]))

    if '--provjeri' in sys.argv:
        return

    tijelo = json.dumps(PREVOD, ensure_ascii=False, indent=2, sort_keys=True)
    js = ('/* Generisano iz tools/prevod_recnik.py. Ne mijenjati rucno:\n'
          '   izmjena ide u rjecnik, pa se pusti  python tools/prevod.py  */\n'
          'window.NP_PREVOD = ' + tijelo + ';\n')
    (SITE / 'js' / 'prevod.js').write_text(js, encoding='utf-8')
    print('\nupisano: site/js/prevod.js')


if __name__ == '__main__':
    main()
