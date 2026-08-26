# -*- coding: utf-8 -*-
"""Teardown Konstra stranica: vadi stablo sekcija iz data-framer-name atributa.

Framer u eksportu zadrzava imena slojeva iz editora. To je najbrzi i najtacniji
put do strukture: ne pogadja se iz snimka ekrana nego se cita ono sto je
dizajner stvarno nazvao.

Framer renderuje TRI kopije svake sekcije (Desktop / Tablet / Phone) i skriva
dvije preko .hidden-* klasa. Zato se duplikati sazimaju.
"""
import re, sys, pathlib, html as htmllib

SRC = pathlib.Path(r'C:\Users\pavle\Downloads\Claude Code\B-Steel\research\konstra-source')

TAG = re.compile(r'<(/?)(\w+)([^>]*?)(/?)>', re.S)
NAME = re.compile(r'data-framer-name="([^"]+)"')


def tree(path, max_depth=3, skip_chrome=True):
    """Stablo imenovanih slojeva do zadate dubine."""
    h = path.read_text(encoding='utf-8', errors='replace')
    out, depth, stack = [], 0, []
    for m in TAG.finditer(h):
        closing, tag, attrs, selfclose = m.groups()
        if tag in ('br', 'img', 'meta', 'link', 'input', 'path', 'use', 'source'):
            continue
        if closing:
            if stack and stack[-1][1] == depth:
                stack.pop()
            depth = max(0, depth - 1)
            continue
        if selfclose:
            continue
        nm = NAME.search(attrs)
        if nm:
            lvl = len(stack)
            if lvl < max_depth:
                out.append((lvl, nm.group(1).strip()))
            stack.append((nm.group(1), depth))
        depth += 1
    return out


def sazmi(rows):
    """Framer daje Desktop/Tablet/Phone kopije. Zadrzi prvu pojavu u nizu."""
    res, prev = [], None
    for lvl, nm in rows:
        if (lvl, nm) == prev:
            continue
        res.append((lvl, nm))
        prev = (lvl, nm)
    return res


CHROME = {'Desktop Black', 'Desktop White', 'Tablet Black', 'Tablet White',
          'Phone Black Default', 'Phone White Default', 'Logo Wrapper', 'Logo',
          'Menu', 'Nav ( Black) 01', 'Nav ( White) 01', 'Dot', 'Subtitle',
          'Icon Wrapper', 'Open', 'Title', 'Container', 'Button- 07',
          'Button - 04', 'Footer'}


def tekst_sekcije(path, ime):
    """Vidljiv tekst unutar prve sekcije sa datim imenom."""
    h = path.read_text(encoding='utf-8', errors='replace')
    i = h.find(f'data-framer-name="{ime}"')
    if i < 0:
        return ''
    seg = h[i:i + 60000]
    seg = re.sub(r'<(script|style|svg)\b.*?</\1>', '', seg, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', '\n', seg)
    lines, out = [' '.join(x.split()) for x in t.split('\n')], []
    for l in lines:
        l = htmllib.unescape(l)
        if l and len(l) > 2 and (not out or out[-1] != l):
            out.append(l)
    return ' | '.join(out[:40])


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    which = sys.argv[1] if len(sys.argv) > 1 else 'konstra-service.html'
    rows = sazmi(tree(SRC / which, max_depth=2))
    print('=' * 74)
    print(which)
    print('=' * 74)
    for lvl, nm in rows:
        if nm in CHROME and lvl == 0:
            continue
        print('  ' * lvl + ('· ' if lvl else '# ') + nm)
