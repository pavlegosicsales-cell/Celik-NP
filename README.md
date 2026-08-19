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

## Zna se, a nije rešeno

- **Rezolucija.** Svi izvori su Instagram eksporti, 1170 px široki. Hero na 1440 px ekranu radi
  interno zumiranje 1.5x pa je vidljivo mekan. Treba tražiti originale sa telefona.
- **`[DOPUNITI]` oznake** stoje u markupu na 5 mesta i vidljive su na sajtu dok se ne potvrde:
  broj završenih objekata, godina osnivanja, prosečan rok po tipu posla, rok garancije, koje ateste izdaje.
- **Tvrdnja „izlazak i procena su besplatni"** je pretpostavka iz context.md, stoji na dva mesta.
  Potvrditi sa klijentom pre lansiranja.
- **Godine na karticama u „Radovi"** su prenesene iz B-Steela i nisu proverene.
- **Nav ima stavku „Blog"** koja nikuda ne vodi, nasleđena iz B-Steela.
- **Sekcije Radovi, Pitanja, Kontakt i podnožje nisu vizuelno provereno** — headless Chrome ne
  skroluje, a sticky rig se rasteže na visinu prozora. Strukturno su čiste (svi resursi postoje,
  ARIA veze u FAQ-u se poklapaju, nema B-Steel tragova u tekstu), ali treba ih pogledati u browseru.
