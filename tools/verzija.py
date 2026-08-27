# -*- coding: utf-8 -*-
"""Upisuje ?v=<hash> na sve lokalne css i js linkove.

Zasto: Vercel servira staticke fajlove pod istim imenima. Kad se promijeni
js/main.js ili css/styles.css, pretrazivac koji je vec bio na sajtu i dalje
moze da vrti staru kopiju iz keša, pa nove stvari ne rade a da nista ne
puca. Hash u adresi pravi novu adresu za svaki izmijenjeni fajl, pa se stara
kopija ne moze upotrijebiti.

Hash je prvih osam znakova SHA-1 sadrzaja fajla, pa se mijenja samo kad se
fajl stvarno promijeni.

Pusta se iz korena projekta:  python tools/verzija.py
Ide automatski na kraju gradi_stranice.py.
"""
import hashlib
import pathlib
import re
import sys

R = pathlib.Path(__file__).resolve().parent.parent
SITE = R / 'site'

# href="css/..." ili src="js/...", sa ili bez postojeceg ?v=
VEZA = re.compile(r'((?:href|src)=")((?:css|js)/[A-Za-z0-9_.-]+\.(?:css|js))(\?v=[0-9a-f]+)?(")')


def hash_fajla(rel):
    p = SITE / rel
    if not p.exists():
        return None
    return hashlib.sha1(p.read_bytes()).hexdigest()[:8]


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    kes = {}
    ukupno = 0

    for f in sorted(SITE.glob('*.html')):
        s = f.read_text(encoding='utf-8')

        def zamijeni(m):
            rel = m.group(2)
            if rel not in kes:
                kes[rel] = hash_fajla(rel)
            h = kes[rel]
            if not h:
                return m.group(0)
            return m.group(1) + rel + '?v=' + h + m.group(4)

        novo, n = VEZA.subn(zamijeni, s)
        if novo != s:
            f.write_text(novo, encoding='utf-8')
        ukupno += n
        print(f'  {f.name:36s} {n} veza')

    print(f'\nverzionisano veza: {ukupno}')
    for rel, h in sorted(kes.items()):
        print(f'  {rel:22s} {h}')


if __name__ == '__main__':
    main()
