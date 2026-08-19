# -*- coding: utf-8 -*-
"""Mapira NP Celik fotografije na B-Steel slotove slika.

Zadrzava TACAN odnos stranica svakog slota (da layout i CLS ostanu isti),
ali izlaznu velicinu ogranicava na ono sto izvor stvarno nosi -- izvori su
1170px sa Instagrama, pa se ne naduvavaju na 2400px.
Stvarne izlazne dimenzije se ispisuju da bi se width/height u markupu
azurirali na njih.
"""
from PIL import Image, ImageOps
import pathlib

R = pathlib.Path(__file__).resolve().parent.parent
SRC = R / 'images'
OUT = R / 'site' / 'assets' / 'img'

def f(frag):
    m = [p for p in SRC.iterdir() if frag.lower() in p.name.lower()]
    if len(m) != 1:
        raise SystemExit(f'! "{frag}" -> {len(m)} pogodaka: {[p.name for p in m]}')
    return m[0]

# slot -> (izvorni fragment, ciljna sirina, ciljna visina)
JOBS = [
    ('hero-radnici-zalazak.jpg',            'hero np celik',           1424, 1774),
    ('rad-01-celicna-hala.jpg',             '662530247',               1280,  961),
    ('rad-02-nadstresnica-odozdo.jpg',      'ugradnja dekinga',        1216, 1620),
    ('rad-05-montaza-na-terenu.jpg',        'MILEVA KONCEPTGrivac.jpg',1280, 1706),
    ('rad-04-detalj-spoja.jpg',             'Caffe Porta',              768, 1376),
    ('rad-06-nadstresnica-garaza.jpg',      'METALNIH STEPENI',        1424, 1898),
    ('proces-skelet-hale.jpg',              'MATIS',                   1272, 1506),
    ('zavarivanje-panorama.jpg',            'Napravili smo jos jednu', 2400,  829),
    ('rad-skelet-industrijske-hale.jpg',    'MILEVA KONCEPTGrivac (1)',1424, 1898),
    ('rad-nadstresnica-terasa.jpg',         'STARA SRBIJA',            1216, 1620),
    ('rad-nadstresnica-solarni-jesenice.jpg','ograde,pocinkovane',     1502, 1328),
    ('rad-hala-kopaonik.jpg',               'kontejneri',              1600, 1199),
    ('rad-poslovna-hala.jpg',               'lokal u nasem gradu⚒️“ČUDESA”.jpg',              1424, 1424),
    ('hero-celicna-konstrukcija.jpg',       'ČUDESA” (1)',              1600, 1067),
]

print(f'{"slot":42} {"trazeno":11} {"izlaz":11} izvor')
for slot, frag, tw, th in JOBS:
    p = f(frag)
    im = Image.open(p)
    im = ImageOps.exif_transpose(im).convert('RGB')
    sw, sh = im.size
    # najveca velicina u ciljnom odnosu koju izvor pokriva bez naduvavanja
    k = min(sw / tw, sh / th, 1.0)
    ow, oh = max(1, round(tw * k)), max(1, round(th * k))
    im = ImageOps.fit(im, (ow, oh), Image.LANCZOS, centering=(0.5, 0.42))
    im.save(OUT / slot, 'JPEG', quality=84, optimize=True, progressive=True)
    kb = (OUT / slot).stat().st_size // 1024
    print(f'{slot:42} {tw}x{th:<6} {ow}x{oh:<6} {kb:4} KB  <- {p.name[:44]}')

# logo badge: zadrzava alfa kanal
lp = f('celiknp_dp_HD (1).png')
lg = Image.open(lp).convert('RGBA')
lg.thumbnail((499, 400), Image.LANCZOS)
canvas = Image.new('RGBA', (499, 400), (0, 0, 0, 0))
canvas.paste(lg, ((499 - lg.width) // 2, (400 - lg.height) // 2), lg)
canvas.save(OUT / 'logo-badge.png', 'PNG', optimize=True)
print(f'{"logo-badge.png":42} 499x400     499x400     {(OUT/"logo-badge.png").stat().st_size//1024:4} KB  <- {lp.name}')
