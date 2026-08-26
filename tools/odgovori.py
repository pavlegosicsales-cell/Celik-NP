# -*- coding: utf-8 -*-
"""Ubacuje odgovore klijenta (26.08.2026) i brise sve vidljive [DOPUNITI] oznake.

Odgovori:
  osnovan 2018   -> 8 godina (2026-2018)
  4 zaposlena
  preko 20 objekata
  garancija 2 godine
  dokumentacija: SAMO RACUN, bez atesta
  radno vreme 07-16h

Nije odgovoreno: avans i prosjecan rok. Klijent kaze da zavise od projekta,
pa se na sajtu ne pominju brojkom -- ni kao pretpostavka ni kao oznaka.
"""
import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')

R = pathlib.Path(__file__).resolve().parent.parent
p = R / 'site' / 'index.html'
s = p.read_text(encoding='utf-8')

REPL = [
# ---------- METRIKA: broj objekata ----------
('<span class="metric__value js-count" data-count-to="100">100+</span>',
 '<span class="metric__value js-count" data-count-to="20">20+</span>'),
('<p class="metric__desc">Od maske za klimu do zatvorene bašte i hale. [DOPUNITI: tačan broj završenih objekata]</p>',
 '<p class="metric__desc">Od maske za klimu do zatvorene bašte i hale. Objekti završeni i predati.</p>'),

# ---------- METRIKA: godine ----------
('<span class="metric__value js-count" data-count-to="6">6</span>',
 '<span class="metric__value js-count" data-count-to="8">8</span>'),
('<p class="metric__desc">Radionica, oprema i ekipa iza svakog posla. [DOPUNITI: godina osnivanja]</p>',
 '<p class="metric__desc">Radionica na Avalskoj radi od 2018. Četvoro ljudi, oprema i sopstvena ekipa iza svakog posla.</p>'),

# ---------- FAQ: rok ----------
# Klijent nije dao rok po tipu posla i kaze da zavisi od projekta.
# Brojka "jedan do tri dana" je bila pretpostavka iz context.md, izlazi.
('Najveći deo se radi u radionici, pa je montaža na objektu kratka, obično jedan do tri dana za standardne radove. Rok upisujemo u ponudu, ne dogovaramo ga usput. <span class="todo">[DOPUNITI: prosečan rok po tipu posla]</span>',
 'Najveći deo se radi u radionici, pa je vreme na vašem objektu kratko. Rok zavisi od posla i njegovog obima, a upisujemo ga u ponudu, ne dogovaramo ga usput.'),

# ---------- FAQ: rđa i garancija ----------
('Pogledajte radove od pre nekoliko godina, stoje. [DOPUNITI: rok garancije]',
 'Pogledajte radove od pre nekoliko godina, stoje. Na antikorozivnu zaštitu dajemo garanciju od dve godine.'),

# ---------- FAQ: projekat i dokumentacija ----------
# Klijent izdaje SAMO RACUN. Stara recenica je obecavala "pratecu dokumentaciju",
# sto bi kupac procitao kao atest ili izjavu izvodjaca.
('Naš deo, izradu, montažu i prateću dokumentaciju, dobijate uredno. [DOPUNITI: koje ateste izdajete]',
 'Naš deo je izrada i montaža. Po završenom poslu dobijate račun; atest i izjavu izvođača, ako ih objekat traži, pribavlja projektant.'),
]

miss = []
for a, b in REPL:
    if a not in s:
        miss.append(a[:80]); continue
    s = s.replace(a, b, 1)

p.write_text(s, encoding='utf-8')
print(f'{len(REPL)-len(miss)}/{len(REPL)} zamjena')
for m in miss:
    print('  NIJE NADJENO:', m)

# kontrola: nijedna vidljiva oznaka ne smije ostati
import re
vis = re.sub(r'<!--.*?-->', '', s, flags=re.S)
left = re.findall(r'\[DOPUNITI[^\]]*\]', vis)
print('vidljivih [DOPUNITI] ostalo:', left or 'nijedna')
