# -*- coding: utf-8 -*-
"""Sadrzaj stranice Galerija.

Svaki unos ima samo ono sto je potvrdjeno: naziv objekta, tip posla i
lokaciju iz spiska referenci u context.md, plus fotografiju iz mape u
README.md.

GODINE NAMJERNO NEMA. Klijentov Instagram (instagram.com/celiknp) se ne da
procitati automatski, a godine koje stoje na karticama "Radovi" na pocetnoj
su prenesene iz B-Steela i nisu provjerene, pa se ne prepisuju ovdje.
Kad klijent posalje godine, dodaje se polje 'godina' i ispisuje se u
.gcard__meta iza tipa posla.
"""

PROJEKTI = [
    dict(naziv='Mileva Koncept', tip='Zatvorena bašta', mjesto='Grivac',
         slika='rad-05-montaza-na-terenu.jpg',
         alt='Zatvorena bašta sa drvenom tavanicom, Mileva Koncept, Grivac',
         w=1169, h=1558),
    dict(naziv='Mileva Koncept', tip='Konstrukcija bašte', mjesto='Grivac',
         slika='rad-skelet-industrijske-hale.jpg',
         alt='Metalna konstrukcija zatvorene bašte spolja, Mileva Koncept, Grivac',
         w=1169, h=1558),
    dict(naziv='Ženeva Lux', tip='Protivpožarno stepenište', mjesto='Kragujevac',
         slika='hero-radnici-zalazak.jpg',
         alt='Protivpožarno metalno stepenište, Ženeva Lux, Kragujevac',
         w=1424, h=1774),
    dict(naziv='Ženeva Lux', tip='Pergola sa lamelama', mjesto='Kragujevac',
         slika='pergola-zeneva-lux.jpg',
         alt='Bela pergola sa lamelama i vertikalnim rešetkama, Ženeva Lux',
         w=1424, h=1424),
    dict(naziv='Caffe Porta', tip='Krovna konstrukcija', mjesto='Kragujevac',
         slika='rad-04-detalj-spoja.jpg',
         alt='Krovne rešetke i noseća metalna konstrukcija, Caffe Porta',
         w=768, h=1376),
    dict(naziv='Stara Srbija', tip='Zastakljena bašta', mjesto='Kragujevac',
         slika='rad-nadstresnica-terasa.jpg',
         alt='Zastakljena letnja bašta, kafana Stara Srbija',
         w=1098, h=1463),
    dict(naziv='Lokal „Čudesa"', tip='Enterijer i šank', mjesto='Kragujevac',
         slika='hero-celicna-konstrukcija.jpg',
         alt='Metalni enterijer i šank, lokal Čudesa, Kragujevac',
         w=1170, h=780),
    dict(naziv='Lokal „Čudesa"', tip='Metalni detalji u lokalu', mjesto='Kragujevac',
         slika='rad-poslovna-hala.jpg',
         alt='Metalni detalji i konstrukcija u lokalu Čudesa',
         w=1170, h=1170),
    dict(naziv='Blazeks MV', tip='Ograda i gelenderi', mjesto='Aerodrom, Kragujevac',
         slika='rad-nadstresnica-solarni-jesenice.jpg',
         alt='Ograda obložena kompaktom sa gelenderima, Blazeks MV',
         w=993, h=878),
    dict(naziv='BLAŽEKS nameštaj', tip='Spoljno stepenište', mjesto='Sušica',
         slika='rad-06-nadstresnica-garaza.jpg',
         alt='Spoljno metalno stepenište, BLAŽEKS nameštaj, Sušica',
         w=1169, h=1558),
    dict(naziv='MATIS New Point', tip='Platforma', mjesto='Kragujevac',
         slika='proces-skelet-hale.jpg',
         alt='Metalna konstrukcija platforme sa daskom 50 mm, MATIS New Point',
         w=988, h=1170),
    dict(naziv='Kapija „DOSTOJNA"', tip='Klizna kapija', mjesto='Kutlovo',
         slika='rad-01-celicna-hala.jpg',
         alt='Dekorativna klizna kapija DOSTOJNA, Kutlovo',
         w=1169, h=878),
    dict(naziv='Modularni kontejner', tip='Sopstveni proizvod', mjesto='NP Čelik',
         slika='modularni-kontejner-zora.jpg',
         alt='Modularni kontejner NP Čelika sa zastakljenom stranom',
         w=1456, h=1456),
]
