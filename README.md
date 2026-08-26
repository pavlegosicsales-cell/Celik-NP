# NP Čelik — sajt

Statični sajt u [site/](site/). **Kod je 1:1 prekopiran sa B-Steela** (koji je rađen po Konstra
Framer teardownu). Struktura, sve sekcije, sve animacije i ceo JS su nedirnuti. Promenjeno je
samo troje: **boje, tekst i slike.**

To je bila svesna odluka radi brzine, jer su i B-Steel i NP Čelik još probne početne strane.
Ako oba klijenta potpišu, sajtovi se razdvajaju.

## Šta je promenjeno

| | |
|---|---|
| **Boje** | Peščana paleta → plava iz logotipa. Vidi [PALETA.md](PALETA.md). 94 hex zamene + 10 `rgba()` koje prvi prolaz nije uhvatio. |
| **Tekst** | 102 + 9 zamena kroz [tools/tekst.py](tools/tekst.py) i [tools/tekst2.py](tools/tekst2.py). Copy je izveden iz [context.md](context.md), FAQ direktno iz liste prigovora. |
| **Slike** | 14 slotova mapirano na Instagram fotografije kroz [tools/slike.py](tools/slike.py). |
| **Cioda na karti** | Pomerena sa Kisača na Kragujevac, po istoj projekciji. |
| **Hero kadriranje** | `.hero__image img` ima `height:150%` — rig traži **uspravnu** sliku. Pejzažne se seku. |

## Mapa slika: ime fajla ≠ sadržaj

Imena fajlova su ostala B-Steelova da markup ne pukne. **Ne čitati ih doslovno:**

| Fajl | Šta je stvarno na slici | Gde se vidi |
|---|---|---|
| `hero-radnici-zalazak.jpg` | PP stepeništa, Ženeva Lux | hero |
| `rad-01-celicna-hala.jpg` | Kapija DOSTOJNA, Kutlovo | hero kartica 01 + usluga „Kapije i ograde" |
| `rad-02-nadstresnica-odozdo.jpg` | Deking uz bazen, Kosmaj | hero kartica 02 |
| `rad-04-detalj-spoja.jpg` | Krovne rešetke, Caffe Porta | usluga „Nosive konstrukcije" |
| `rad-05-montaza-na-terenu.jpg` | Zatvorena bašta, Mileva Koncept | hero kartica 03 + usluga „Letnje bašte" |
| `rad-06-nadstresnica-garaza.jpg` | Spoljno stepenište | usluga „Stepeništa i PP" |
| `proces-skelet-hale.jpg` | Platforma, MATIS New Point | sekcija „Kako radimo" |
| `zavarivanje-panorama.jpg` | Bašta sa dekingom u gradu | traka u „Rezultati" |
| `rad-skelet-industrijske-hale.jpg` | Mileva Koncept spolja | Radovi 01 |
| `rad-nadstresnica-terasa.jpg` | Stara Srbija | Radovi 02 |
| `rad-nadstresnica-solarni-jesenice.jpg` | Ograda, Blazeks MV | Radovi 03 |
| `rad-hala-kopaonik.jpg` | Modularni kontejner | Radovi 04 |
| `rad-poslovna-hala.jpg` | Lokal Čudesa | Radovi 05 |
| `hero-celicna-konstrukcija.jpg` | Čudesa, enterijer | samo `og:image` |

Izvori su u [images/](images/). Alati se puštaju iz korena projekta:
`python tools/slike.py` pa `python tools/dims.py`.

## Stranice

| Fajl | Šta je |
|---|---|
| `site/index.html` | Početna |
| `site/usluge.html` | Lista svih šest usluga |
| `site/usluga-metalne-konstrukcije.html` | Nosive konstrukcije |
| `site/usluga-kapije-i-ograde.html` | Kapije i ograde |
| `site/usluga-stepenista.html` | Stepeništa i PP stepeništa |
| `site/usluga-letnje-baste.html` | Letnje i zatvorene bašte |
| `site/usluga-deking-i-enterijer.html` | Enterijer i završna obrada |

Modularni kontejneri nemaju pod-stranicu: postoji samo jedna fotografija.
Stoje kao stavka u listi sa dugmetom pravo na upit.

Sve unutrašnje stranice se **generišu**, ne uređuju ručno. Zajednički delovi
(sprite, zaglavlje, mobilni meni, podnožje) se vade iz `index.html`, pa jedna
izmena u zaglavlju ostaje tačna svuda:

```
python tools/gradi_usluge.py
```

Copy živi u [tools/usluge_sadrzaj.py](tools/usluge_sadrzaj.py), a nove CSS
komponente u [site/css/stranice.css](site/css/stranice.css) — ništa u
`styles.css` nije dirano.

## Logo

Klijentov PDF je pravi vektor: 18 crteža, nula rastera, slova u krivama.
Varijante su izvučene u [brand_assets/](brand_assets/) kao SVG i PNG na 400dpi
([tools/logo_svg.py](tools/logo_svg.py)). Logo je **crn** u fajlu; na tamnom
zaglavlju ga CSS invertuje u belo. Plavi 3D logo sa Instagrama je bio samo
profilna slika, ne brend asset.

## Odgovori klijenta (26.08.2026)

Osnovan 2018 (8 godina) · četvoro zaposlenih · preko 20 objekata · garancija na
antikorozivnu zaštitu 2 godine · dokumentacija: **samo račun, bez atesta** ·
radno vreme 07–16h.

Avans i rok po tipu posla klijent nije dao i kaže da zavise od projekta, pa se
na sajtu ne pominju. Nema nijedne vidljive `[DOPUNITI]` oznake.

## Zna se, a nije rešeno

- **Rezolucija fotografija.** Instagram eksporti, 1170 px široki, osim hero slike
  koju je klijent poslao zasebno (1424 px). Hero rig radi interno zumiranje, pa su
  slike na velikim ekranima vidljivo mekane. Treba tražiti originale sa telefona.
- **Kontejneri imaju jednu jedinu fotografiju.** Zato nemaju pod-stranicu. Čim
  stigne još par, dodaje se `usluga-kontejneri.html` u `tools/usluge_sadrzaj.py`.
- **Tvrdnja „izlazak i procena su besplatni"** je pretpostavka iz `context.md`,
  stoji na više mesta. Nije potvrđena.
- **Godine na karticama u „Radovi"** prenesene su iz B-Steela i nisu proverene.
- **Nav ima „Blog" i „Galerija"** koji nikuda ne vode, nasleđeni iz B-Steela.
- **Sekcije Radovi, Pitanja, Kontakt i podnožje na početnoj** nisu vizuelno
  proverene: headless Chrome ne skroluje, a sticky rig se rasteže na visinu
  prozora. Strukturno su čiste. Stranice usluga jesu proverene.
