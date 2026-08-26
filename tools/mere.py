# -*- coding: utf-8 -*-
"""Vadi CSS pravila za imenovane Framer slojeve.

Framer daje svakom sloju klasu tipa framer-1abc23 i pise pravilo u
<style data-framer-css-ssr-minified>. Ovdje se spaja jedno s drugim:
ime sloja -> klasa -> pravilo, pa se mjere citaju iz izvora umjesto da se
procjenjuju sa snimka ekrana.
"""
import re, sys, pathlib

SRC = pathlib.Path(r'C:\Users\pavle\Downloads\Claude Code\B-Steel\research\konstra-source')


def load(path):
    h = path.read_text(encoding='utf-8', errors='replace')
    css = '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S))
    return h, css


def klase_za(h, ime):
    """Sve klase elemenata koji nose to ime sloja."""
    out = []
    for m in re.finditer(r'<[^>]*data-framer-name="' + re.escape(ime) + r'"[^>]*>', h):
        cm = re.search(r'class="([^"]*)"', m.group(0))
        if cm:
            out.append(cm.group(1).split())
    return out


def pravilo(css, cls):
    """Prvo pravilo koje cilja bas tu klasu."""
    for m in re.finditer(r'([^{}]+)\{([^{}]+)\}', css):
        sel, body = m.group(1), m.group(2)
        if re.search(r'\.' + re.escape(cls) + r'(?![\w-])', sel):
            return sel.strip()[:90], body.strip()
    return None, None


VAZNO = ('display|flex|grid|gap|padding|margin|width|height|max-width|min-height|'
         'aspect|object|position|inset|top|left|right|bottom|border|radius|'
         'background|overflow|align|justify|order|opacity|transform')


def prikazi(path, imena, dubina=2):
    h, css = load(path)
    print('=' * 76)
    print(path.name)
    print('=' * 76)
    for ime in imena:
        grupe = klase_za(h, ime)
        if not grupe:
            print(f'\n### {ime}  -> nema')
            continue
        print(f'\n### {ime}   ({len(grupe)} pojava)')
        vidjeno = set()
        for cls_list in grupe[:dubina]:
            for c in cls_list:
                if not c.startswith('framer-') or c in vidjeno:
                    continue
                vidjeno.add(c)
                sel, body = pravilo(css, c)
                if not body:
                    continue
                bits = [d.strip() for d in body.split(';')
                        if d.strip() and re.match(VAZNO, d.strip())]
                if bits:
                    print(f'  .{c}')
                    for b in bits:
                        print(f'      {b}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    f = sys.argv[1]
    imena = sys.argv[2].split(',')
    prikazi(SRC / f, imena)
