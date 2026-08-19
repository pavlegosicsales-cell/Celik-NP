# NP Čelik — paleta, 5 boja

Brend plava je **izmerena iz logo fajla**, nije procenjena sa oka: `Insta_Saver_celiknp_dp_HD (1).png`
prebačen u RGB i prebrojan po pikselu, najčešća vrednost je `#1B44D3`. Ostale četiri su neutrale
usklađene sa njom (svaka nosi trag plave, nijedna nije čista siva).

| # | Uloga | Hex | Gde se koristi |
|---|---|---|---|
| 1 | **Brend plava** | `#1B44D3` | Primarno dugme, puna strelica, sve što treba da nosi brend |
| 2 | **Mastilo** | `#0A0F1F` | Naslovi na svetlom, tekst na tamnom polju |
| 3 | **Hladno bela** | `#F4F6FB` | Nosiva svetla pozadina stranice |
| 4 | **Čelično plava** | `#5B6784` | Prigušen tekst, linije, ivice |
| 5 | **Čisto belo** | `#FFFFFF` | Tekst na plavoj, površine kartica |

Nijanse ovih pet (nisu nove boje): `#060A14` najtamnija podloga sekcija · `#A8BEFF` svetli akcenat i
traka „Kako radimo" · `#6E8CF5` sitni akcenti · `#2B3652` telo teksta · `#E8ECF7` naizmenična traka ·
`#D4DAE9` linije na svetlom · `#9AA6C2` prigušen tekst na tamnom.

Crvena za greške u formi ostaje crvena. To je funkcionalna boja, ne deo brenda.

## Kontrast, provereno računski

| Par | Odnos | Nivo |
|---|---|---|
| `#0A0F1F` na `#F4F6FB` | 17.6:1 | AAA |
| `#2B3652` na `#F4F6FB` | 11.1:1 | AAA |
| `#9AA6C2` na `#0A0F1F` | 7.8:1 | AAA |
| `#FFFFFF` na `#1B44D3` | 7.5:1 | AAA |
| `#1B44D3` na `#F4F6FB` | 6.9:1 | AA |
| `#5B6784` na `#F4F6FB` | 5.2:1 | AA |

Cela paleta prolazi AA, većina AAA.

## Gde su tokeni

Sve stoji u [site/css/tokens.css](site/css/tokens.css). Imena varijabli su zadržana iz B-Steel verzije
(`--sand-*`, `--cream-*`, `--stone-*`, `--brown-*`) da markup ne pukne, pa se **ne čitaju doslovno**:
`--sand-300` je sada svetla plava, `--cream-100` je hladno bela. Uloga svake piše u komentaru uz nju.

Jedini novi tokeni su `--brand-blue` i `--brand-blue-hover`. Njih sam morao da izdvojim jer je na
B-Steelu primarno dugme koristilo `--pure-black`, a `--pure-black` je istovremeno pozadina svih
tamnih sekcija na 18 mesta. Kad sam ga prvi put obojio u brend plavu, cela „O nama" sekcija je
postala kobalt plav zid.
