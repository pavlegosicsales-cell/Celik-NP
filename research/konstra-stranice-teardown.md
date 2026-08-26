# Konstra teardown: /service, /contact, /about

Metod: Framer u eksportu zadržava imena slojeva iz editora u `data-framer-name`.
Struktura je čitana odatle, mere iz `<style data-framer-css-ssr-minified>`.
Ništa nije procenjeno sa snimka ekrana. Alati: [tools/teardown.py](../tools/teardown.py),
[tools/mere.py](../tools/mere.py).

Izvor: `B-Steel/research/konstra-source/konstra-{service,contact,about}.html`.

Framer renderuje **tri kopije** svake sekcije (Desktop / Tablet / Phone) i skriva
dve preko `.hidden-*` klasa. Zato se u sekvenci imena sve ponavlja po tri puta.

---

## 1. `/service` — samo DVE sekcije

```
Main
 ├─ Service Hero      Hero Image · Overlay · Container(Heading · Breadcrumbs)
 └─ Service Index     6 × [ Service image | Service Info ]
```

**Nema CTA na kraju.** Posle poslednje usluge ide pravo podnožje.

### Service Hero
| | |
|---|---|
| visina | `100vh` |
| padding | `216px 72px 64px` |
| raspored | flex column, `align-items: center` |
| Hero Image | `position: absolute; inset: 0` |
| **Overlay** | `background: #1a1711b3` — **tamna providna, ne svetli preliv** |
| Heading | flex column, `gap: 20px`, `max-width: 556px`, align flex-start |
| Breadcrumbs | flex row, iznad naslova |

Overlay je taman pa je **tekst u herou beo**. Ovo je najveća razlika u odnosu
na hero početne stranice, koji ide na svetli peščani preliv i taman tekst.

### Service Index
| | |
|---|---|
| pozadina | `#FFF7E5` (cream-50) |
| padding | `112px 72px` |
| stavka | flex **row**, `gap: 48px`, `width: 1296px`, `padding: 16px 32px 16px 16px` |
| Service image | `flex: 1 0 0` |
| Service Info | flex column, `gap: 20px`, `width: 100%` |
| Scope List Wrapper | flex row, `align-items: flex-end` |
| List Inner | flex column, `gap: 16px`, `max-width: 344px` |
| Project scope | flex row, `gap: 8px`, ikona + tekst |

**Slika je uvek levo.** Nema naizmeničnog rasporeda. Naslov usluge, opis,
`Project scope:` pa pet stavki, pa dugme `View details`.

---

## 2. `/contact` — tri sekcije

```
Main
 ├─ Contact             Intro text · Contact details · forma
 ├─ What happens next   3 numerisana koraka
 └─ FAQ                 6 pitanja
```

### Contact
| | |
|---|---|
| pozadina | `#FFF7E5` |
| padding | `200px 72px 112px` |
| Intro text container | flex column, `gap: 20px` |
| Contact details container | flex column, `gap: 32px`, `max-width: 236px` |
| Email container | flex column, `gap: 8px` (naslovčić iznad vrednosti) |

Tri detalja: `Email address`, `Phone number`, `Location`.
Forma je klasična: First name, Last name, Email, Phone, Project type (select),
Project details (textarea). Ispod stoji „We respond within 24 hours personally,
not automatically."

> Kod nas ovu formu **zamenjuje wizard** iz skilla `website-build-rules`.

### What happens next
| | |
|---|---|
| pozadina | `#030000` (crna) — jedina crna sekcija na stranici |
| padding | `112px 72px` |
| Number | flex column, `padding: 12px 14px`, `gap: 10px` |

Tri koraka: `Your enquiry is reviewed` · `Discovery call scheduled` ·
`Written project summary`.

---

## 3. `/about` — sedam sekcija

```
Main
 ├─ Hero          naslov · opis · 2 dugmeta
 ├─ Mission       2 bloka naizmenično: Image Stack (2 slike) + Text Stack
 ├─ Core Value    sticky, 4 numerisane vrednosti
 ├─ History       timeline, 5 godina, Progress traka
 ├─ Team Member   6 članova
 ├─ Awards        lista priznanja
 └─ CTA           BG slika + Overlay + dugme
```

| sekcija | pozadina | padding | gap |
|---|---|---|---|
| Hero | `#FFF7E5` | `216px 0 0` | 72px |
| Mission | — | `0` | 0 |
| Core Value | `#FFF7E5` | `112px 72px` | 72px |
| History | `#FAE1A6` (peščana) | `112px 72px` | 72px |
| Team Member | `#030000` | `78px 72px` | 72px |
| Awards | `#FFF7E5` | `112px 72px` | 0 |

Ritam je namerno naizmeničan: svetlo, slika preko pune širine, svetlo,
**peščano**, **crno**, svetlo. History i Team Member su jedine dve sekcije
koje prekidaju svetlu podlogu.

`Core Value` koristi `position: sticky` na naslovu dok četiri vrednosti
prolaze pored njega.

`History` ima `Progress Container` sa trakom koja se puni po godini.

---

## Šta iz ovoga NE prenosimo doslovno

- **Awards** — NP Čelik nema sertifikate ni nagrade. Ista forma liste se
  koristi za **reference** (Paligorić, Stara Srbija, Caffe Porta, Mileva
  Koncept, Čudesa, Ženeva Lux), sa lokacijom umesto godine.
- **Team Member, 6 članova** — klijent je rekao da ih je četvoro. Nema
  fotografija ni imena, pa sekcija stoji sa oznakama dok ne stignu.
- **History, 5 godina** — koriste se samo potvrđene: 2018 osnivanje,
  2021 prvi ugostiteljski objekti, 2023 kontejneri kao proizvod, 2026 danas.
  Nijedna prekretnica nije izmišljena.
