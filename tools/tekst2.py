# -*- coding: utf-8 -*-
"""Ostatak copy-ja: naslovi prelomljeni <br>-om i FAQ sa <span class="todo">."""
import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')

R = pathlib.Path(__file__).resolve().parent.parent
p = R / 'site' / 'index.html'
s = p.read_text(encoding='utf-8')

REPL = [
# hero naslov (data-split-words: prelom <br> je namjeran, cuva se)
('>Metalne konstrukcije<br>po meri.</h1>',
 '>Konstrukcije, kapije<br>i bašte po meri.</h1>'),

# naslov sekcije Usluge
('>Od ideje do čelika,<br><span class="svcs__title-accent">na jednom mestu</span></h2>',
 '>Od mere na licu mesta,<br><span class="svcs__title-accent">do gotovog objekta</span></h2>'),

# naslov sekcije Kako radimo
('>Znate šta sledi,<br><span class="proces__title-accent">od upita<br>do primopredaje.</span></h2>',
 '>Znate šta sledi,<br><span class="proces__title-accent">od poziva<br>do primopredaje.</span></h2>'),

# naslov sekcije Radovi
('>Nekoliko izdvojenih <span class="works__title-accent">realizacija.</span></h2>',
 '>Nekoliko izdvojenih <span class="works__title-accent">realizacija.</span></h2>'),

# naslov sekcije Kontakt
('>Recite nam šta vam treba.<br><span class="contact__title-accent">Ostalo je na nama.</span></h2>',
 '>Recite šta, gde i za kada.<br><span class="contact__title-accent">Ostalo je na nama.</span></h2>'),

# fact: podrucje rada
('<p class="fact__value">Kisač ·<br>Novi Sad i okolina</p>',
 '<p class="fact__value">Kragujevac ·<br>Šumadija i centralna Srbija</p>'),

# geo meta
('<meta name="geo.placename" content="Kisač, Novi Sad">',
 '<meta name="geo.placename" content="Kragujevac">'),

# FAQ: rok
('Poštovanje dogovorenih rokova nam je jedno od osnovnih načela. Rok dogovaramo unapred i držimo ga se. <span class="todo">[DOPUNITI: prosječan rok isporuke po tipu objekta]</span>',
 'Najveći deo se radi u radionici, pa je montaža na objektu kratka, obično jedan do tri dana za standardne radove. Rok upisujemo u ponudu, ne dogovaramo ga usput. <span class="todo">[DOPUNITI: prosečan rok po tipu posla]</span>'),

# FAQ: podrucje
('Sedište nam je u Kisaču, radimo Novi Sad i okolinu. <span class="todo">[DOPUNITI: šira teritorija ako radite izvan tog područja]</span>',
 'Radionica je na Avalskoj 11 u Kragujevcu. Baza nam je Kragujevac i Šumadija, a izlazimo na teren širom centralne Srbije: Grivac, Kutlovo, Sušica, Kosmaj.'),
]

miss = []
for a, b in REPL:
    if a not in s:
        miss.append(a)
        continue
    s = s.replace(a, b)

p.write_text(s, encoding='utf-8')
print(f'{len(REPL)-len(miss)}/{len(REPL)} zamjena primijenjeno')
for m in miss:
    print('  NIJE NADJENO:', m[:100])
