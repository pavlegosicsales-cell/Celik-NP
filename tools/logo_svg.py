# -*- coding: utf-8 -*-
"""Izvlaci varijante logotipa NP Celik iz np celik logo.pdf u ciste SVG fajlove.

PDF je pravi vektor: 18 crteza, nula rasterskih slika, nula teksta (slova su
konvertovana u krive). fitz-ov get_svg_image() uvijek serijalizuje cijelu
stranu, pa se putanje ovdje crtaju rucno, samo one koje padaju u trazenu zonu.

Boja u izvoru je #1A1A18. Izlaz koristi currentColor, pa se logo boji iz CSS-a.
"""
import sys, pathlib
import pymupdf as fz

R = pathlib.Path(__file__).resolve().parent.parent
SRC = R / 'np celik logo.pdf'
OUT = R / 'brand_assets'
OUT.mkdir(exist_ok=True)

# zone izmjerene iz get_drawings() klastera, u tackama
VAR = {
    'lockup-horizontalni': (625, 626, 982, 811),   # NP celik + KRAGUJEVAC/AVALSKA/TEL
    'lockup-kartica':      (1437, 151, 1933, 859), # uspravna varijanta sa okvirom
    'mark-np-celik':       (696, 429, 734, 449),   # sam znak, bez podnaslova
    'lockup-mali':         (829, 425, 891, 511),   # znak + KRAGUJEVAC + adresa
}
PAD = 3


def d_from_items(items, ox, oy, closed):
    """PDF crtezi -> SVG path d.

    Segmenti u fitz-u dolaze redom i cine kontinuiranu putanju. Prva verzija
    je svakom segmentu davala svoj M, cime su se konture raspadale i fill je
    davao fragmente umjesto slova. Ovdje se M pise samo kad kraj prethodnog
    segmenta nije pocetak sljedeceg, dakle na pravom prekidu subputanje.
    """
    out, cur = [], None
    def P(p):
        return f'{p.x - ox:.2f},{p.y - oy:.2f}'
    def near(a, b):
        return a is not None and abs(a.x - b.x) < 0.01 and abs(a.y - b.y) < 0.01
    for it in items:
        op = it[0]
        if op == 'l':
            if not near(cur, it[1]):
                if cur is not None and closed:
                    out.append('Z')
                out.append(f'M{P(it[1])}')
            out.append(f'L{P(it[2])}')
            cur = it[2]
        elif op == 'c':
            if not near(cur, it[1]):
                if cur is not None and closed:
                    out.append('Z')
                out.append(f'M{P(it[1])}')
            out.append(f'C{P(it[2])} {P(it[3])} {P(it[4])}')
            cur = it[4]
        elif op == 're':
            r = it[1]
            out.append(f'M{r.x0-ox:.2f},{r.y0-oy:.2f} H{r.x1-ox:.2f} '
                       f'V{r.y1-oy:.2f} H{r.x0-ox:.2f} Z')
            cur = None
        elif op == 'qu':
            q = it[1]
            out.append(f'M{P(q.ul)} L{P(q.ur)} L{P(q.lr)} L{P(q.ll)} Z')
            cur = None
    if cur is not None and closed:
        out.append('Z')
    return ' '.join(out)


def main():
    doc = fz.open(SRC)
    page = doc[0]
    drawings = page.get_drawings()

    for name, (x0, y0, x1, y1) in VAR.items():
        clip = fz.Rect(x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD)
        w, h = clip.width, clip.height

        body = []
        for dr in drawings:
            r = fz.Rect(dr['rect'])
            # samo putanje koje zona zaista sadrzi; intersects je hvatao
            # i susjedne varijante koje je clip samo okrznuo
            if not (clip.contains(r) or (r & clip).get_area() > 0.6 * r.get_area()):
                continue
            d = d_from_items(dr['items'], clip.x0, clip.y0, dr.get('closePath', True))
            if not d:
                continue
            # izvorna boja #1A1A18 ide u currentColor da se logo boji iz CSS-a
            fill = 'currentColor' if dr.get('fill') else 'none'
            stroke = 'currentColor' if dr.get('color') else 'none'
            attrs = f'fill="{fill}" stroke="{stroke}"'
            if dr.get('color'):
                attrs += f' stroke-width="{dr.get("width", 1):.2f}"'
            if dr.get('even_odd'):
                attrs += ' fill-rule="evenodd"'
            body.append(f'  <path {attrs} d="{d}"/>')

        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
               f'width="{w:.0f}" height="{h:.0f}" role="img" '
               f'aria-label="NP Čelik">\n' + '\n'.join(body) + '\n</svg>\n')
        (OUT / f'{name}.svg').write_text(svg, encoding='utf-8')
        print(f'{name:22} {len(svg)//1024:3} KB  {w:.0f}x{h:.0f}  putanja: {len(body)}')

        # prateci PNG sa alfom, za mjesta gdje SVG ne moze
        pix = page.get_pixmap(clip=clip, dpi=600, alpha=True)
        pix.save(OUT / f'{name}.png')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
