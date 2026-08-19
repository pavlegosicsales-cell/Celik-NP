# -*- coding: utf-8 -*-
"""NP Celik recolor: B-Steel pjescana paleta -> NP Celik plava iz logotipa.

Brend plava #1B44D3 je izvucena iz logotipa (najcesci piksel, PIL Counter).
Sve ostalo su nijanse te plave ili neutralne izvedene iz nje.
Crvena za greske ostaje: funkcionalna boja, nije dio brenda.
"""
import io, re, sys, pathlib

MAP = {
    # --- akcenat / brend ---
    '#030000': '#1B44D3',   # pure-black -> BREND PLAVA (punjenje primarnog dugmeta)
    '#FAE1A6': '#A8BEFF',   # sand-300   -> svijetla plava (akcenat na tamnom, punjenje)
    '#F9DC8B': '#8FA9FA',   # sand-400   -> jaci svijetli akcenat
    '#D9C390': '#B9C6E8',   # sand-500   -> podloga trake
    '#FF7478': '#6E8CF5',   # coral-400  -> plavi kvadratic uz oznaku sekcije

    # --- svijetlo polje ---
    '#FCF6E9': '#F4F6FB',   # cream-100  -> nosiva svijetla pozadina
    '#FFF7E5': '#FFFFFF',   # cream-50   -> naslovi na tamnom / cisto bijelo
    '#F9F0DA': '#E8ECF7',   # cream-200  -> naizmjenicna traka

    # --- linije i prigusen tekst ---
    '#D2CCBC': '#D4DAE9',   # stone-300
    '#C7C0AF': '#C3CBDF',   # stone-400
    '#BAB3A2': '#9AA6C2',   # stone-500  (prigusen na tamnom, 7.8:1)
    '#7B725E': '#5B6784',   # stone-600  (5.2:1 na bg)
    '#897F6C': '#6B7794',   # stone-700
    '#CFD3D7': '#C3CBDF',   # ivica polja na hover
    '#9AA1A9': '#5B6784',   # placeholder

    # --- tamno polje ---
    '#504732': '#2B3652',   # brown-800  -> tijelo teksta (11.1:1)
    '#1B1915': '#0A0F1F',   # ink-900    -> nosiva tamna (17.6:1)
    '#271E07': '#101833',   # ink-950
    '#3A362F': '#16224A',   # steel-600  -> srednja kartica u Rezultatima

    # --- hero gradijent preko slike ---
    '#FBD077': '#8FA9FA',
    '#FFBC24': '#6E8CF5',
    '#ECA910': '#4A6BE0',
    '#FFCA30': '#A8BEFF',
}

FILES = ['site/css/tokens.css', 'site/css/styles.css', 'site/index.html']
root = pathlib.Path(__file__).resolve().parent.parent

pat = re.compile('|'.join(re.escape(k) for k in MAP), re.IGNORECASE)
up = {k.upper(): v for k, v in MAP.items()}

total = 0
for rel in FILES:
    p = root / rel
    src = p.read_text(encoding='utf-8')
    n = len(pat.findall(src))
    out = pat.sub(lambda m: up[m.group(0).upper()], src)
    p.write_text(out, encoding='utf-8')
    total += n
    print(f'{rel:24} {n:4} zamjena')
print(f'{"UKUPNO":24} {total:4}')
