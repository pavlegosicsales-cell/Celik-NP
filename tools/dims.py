# -*- coding: utf-8 -*-
"""Sinhronizuje width/height u markupu sa stvarnim dimenzijama fajlova."""
import re, pathlib
from PIL import Image

R = pathlib.Path(__file__).resolve().parent.parent
html = R / 'site' / 'index.html'
imgdir = R / 'site' / 'assets' / 'img'

real = {}
for p in imgdir.iterdir():
    if p.suffix.lower() in ('.jpg', '.png'):
        with Image.open(p) as im:
            real[p.name] = im.size

s = html.read_text(encoding='utf-8')
tag = re.compile(r'<img\b[^>]*>', re.S)

n = 0
def fix(m):
    global n
    t = m.group(0)
    f = re.search(r'assets/img/([^"\']+)', t)
    if not f or f.group(1) not in real:
        return t
    w, h = real[f.group(1)]
    new = re.sub(r'width="\d+"', f'width="{w}"', t)
    new = re.sub(r'height="\d+"', f'height="{h}"', new)
    if new != t:
        n += 1
        print(f'  {f.group(1):40} -> {w}x{h}')
    return new

s = tag.sub(fix, s)
html.write_text(s, encoding='utf-8')
print(f'{n} <img> tagova azurirano')
