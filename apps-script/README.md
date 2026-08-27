# Backend za upite — NP Čelik

Google Apps Script koji prima upite sa obrasca na sajtu, upisuje ih u Google
tabelu i šalje jedno obaveštenje mejlom.

Napravljeno skillom `form-backend-setup` (korak 3 od 3), 27.08.2026.

---

## Šta gde stoji

| Fajl | Šta radi |
|---|---|
| `Code.gs` | ceo backend: prijem, upis u tabelu, mejl |
| `site/js/wizard.js` | obrazac na sajtu, konstanta `ENDPOINT` na vrhu |
| `tools/pregled_mejla.js` | crta mejl u PNG bez deploya, za proveru izgleda |

## Polja koja obrazac šalje

`ime`, `telefon`, `mejl`, `posao`, `objekat`, `gde`, `kada`, `opis`, `strana`

Imena moraju da se poklapaju sa `readParams_` u `Code.gs`. Ako se obrazac
menja, menjaju se oba mesta.

---

## Postavljanje, korak po korak

1. **Napravi tabelu.** Google Drive > New > Google Sheets. Nazovi je npr.
   „NP Čelik — upiti". Zaglavlje se upisuje samo, na prvi upit.
2. **Otvori skriptu.** U toj tabeli: `Extensions > Apps Script`.
3. **Zameni kod.** Obriši sve iz `Code.gs` i nalepi ceo sadržaj ovog
   `Code.gs`.
4. **Proveri `NOTIFY_TO`.** Dok se testira, tu stoji tvoja adresa. Klijentova
   ide tek posle provere.
5. **Deploy.** `Deploy > New deployment > Web app`:
   - Execute as: **Me**
   - Who has access: **Anyone**
   - Prvi put traži dozvolu za slanje mejla, to je normalno.
6. **Kopiraj `/exec` adresu** i upiši je u `ENDPOINT` u `site/js/wizard.js`,
   pa pusti `python tools/verzija.py` da se osveži hash i push.
7. **Probaj obrazac** na sajtu i vidi da li mejl stiže i da li se red pojavio
   u tabeli.

## Puštanje uživo

Jedna linija u `Code.gs`:

```js
var NOTIFY_TO = 'npcelik85@gmail.com';
```

pa **obavezno**: `Deploy > Manage deployments > olovka > Version: New version >
Deploy`. Sama izmena koda ne menja ništa na živoj adresi. Ovo je greška koja
uhvati svakoga.

## Poznata ograničenja

- **Potvrda na sajtu nije dokaz da je mejl otišao.** Zahtev ide kroz `no-cors`,
  jer Apps Script ne šalje CORS zaglavlja, pa pretraživač ne može da pročita
  odgovor. Poruka „Upit je stigao" se prikazuje i kad slanje ne uspe. Zato se
  posle svake izmene proveri probnim upitom.
- **Kvota:** 100 primalaca dnevno na besplatnom Gmail nalogu. Za obrazac
  ovog obima je više nego dovoljno.
- **Upis u tabelu i mejl su razdvojeni.** Ako upis pukne, mejl svejedno ide.
  Gubitak upita zbog greške u tabeli je najgori mogući ishod, pa je namerno
  tako.

## Provera izgleda mejla bez deploya

```
node tools/pregled_mejla.js apps-script/Code.gs <izlazni-folder>
```

Crta pun upit, verziju za telefon i mrežu od šest graničnih slučajeva
(samo mejl, samo telefon, „n/a" u telefonu, bez opisa, prazan obrazac,
predugačke vrednosti). Pada uz poruku ako escape pukne.
