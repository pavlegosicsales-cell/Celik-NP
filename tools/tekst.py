# -*- coding: utf-8 -*-
"""B-Steel copy -> NP Celik copy. Struktura, klase i markup se ne diraju."""
import sys, pathlib
sys.stdout.reconfigure(encoding='utf-8')

R = pathlib.Path(__file__).resolve().parent.parent
p = R / 'site' / 'index.html'
s = p.read_text(encoding='utf-8')

REPL = [
# ---------- META ----------
('B-steel | Metalne konstrukcije, nadstrešnice i hale | Kisač, Novi Sad',
 'NP Čelik | Metalne konstrukcije, kapije, ograde i letnje bašte | Kragujevac'),
('Projektovanje, izrada i montaža kvalitetnih metalnih konstrukcija za stambene, poslovne i industrijske objekte. Kisač, Novi Sad i okolina. Zatražite ponudu.',
 'Bravarska radionica u Kragujevcu. Izrada i montaža metalnih konstrukcija, kapija, ograda, stepeništa, letnjih bašti i modularnih kontejnera. Mera, izrada i montaža sopstvenom ekipom.'),
('B-steel | Metalne konstrukcije', 'NP Čelik | Metalne konstrukcije i bravarija'),
('Projektovanje, izrada i montaža kvalitetnih metalnih konstrukcija za stambene, poslovne i industrijske objekte.',
 'Od mere na licu mesta do montaže. Konstrukcije, kapije, ograde, stepeništa, letnje bašte i kontejneri za Kragujevac i Šumadiju.'),

# ---------- KONTAKT ----------
('060 7600 664', '060 41 45 466'),
('0607600664', '0604145466'),
('montaznehale24@gmail.com', 'npcelik85@gmail.com'),
('Železnička 36, Kisač', 'Avalska 11, Kragujevac'),
('%C5%BDelezni%C4%8Dka%2036%2C%20Kisa%C4%8D', 'Avalska%2011%2C%20Kragujevac'),
('45.3306° N, 19.7203° E', '44.0165° N, 20.9114° E'),
('Kisač · Novi Sad i okolina', 'Kragujevac · Šumadija'),
('Kisač, Novi Sad i okolina', 'Kragujevac, Šumadija i centralna Srbija'),
('Sedište nam je u Kisaču, radimo Novi Sad i okolinu. [DOPUNITI: šira teritorija ako radite izvan tog područja]',
 'Radionica je na Avalskoj 11 u Kragujevcu. Baza nam je Kragujevac i Šumadija, a izlazimo na teren širom centralne Srbije: Grivac, Kutlovo, Sušica, Kosmaj.'),
('Izlazimo na teren za procenu i montažu. [DOPUNITI: šira teritorija]',
 'Izlazak na teren i procena su besplatni.'),
('https://www.instagram.com/izdrada_metalnih_konstrukcija/', 'https://www.instagram.com/celiknp/'),
('https://www.facebook.com/profile.php?id=61566103301816', 'https://www.facebook.com/npcelikconstruction'),
('B-steel na Instagramu', 'NP Čelik na Instagramu'),
('B-steel na Facebooku', 'NP Čelik na Facebooku'),

# ---------- HERO ----------
('Siluete radnika na čeličnoj skeli protiv neba u zalazak sunca',
 'Drvena paluba na metalnoj podkonstrukciji uz bazen na Kosmaju, u zalazak sunca'),
('Metalne konstrukcije po meri.', 'Konstrukcije, kapije i bašte po meri.'),
('Bavimo se projektovanjem, izradom i montažom kvalitetnih metalnih konstrukcija za stambene, poslovne i industrijske objekte.',
 'Izlazimo na teren, merimo, izrađujemo u sopstvenoj radionici i montiramo svojom ekipom. Jedan sagovornik od prvog poziva do skidanja zaštitne folije.'),

# ---------- O NAMA ----------
('Pretvaramo vašu ideju u gotovu čeličnu konstrukciju, sa jasnim rokovima, preciznom izradom i montažom na terenu, od prvog upita do primopredaje.',
 'Bravarska radionica na Avalskoj 11. Mera, izrada, antikorozivna zaštita i montaža su naša ekipa, pa nema situacije da bravar krivi farbara, a farbar montera.'),
('Projekat → izrada → montaža', 'Mera → izrada → montaža'),
('Kompletna usluga na jednom mestu, bez koordinacije više izvođača.',
 'Ceo posao pod jednim krovom. Jedna odgovornost i jedan sagovornik.'),
('Stambeni · poslovni · industrijski', 'Ugostiteljstvo · firme · privatna lica'),
('Od nadstrešnice i kućne konstrukcije do industrijske hale i skladišta.',
 'Od maske za klima uređaj do noseće krovne konstrukcije i hale.'),

# ---------- USLUGE ----------
('Od ideje do čelika, na jednom mestu', 'Od mere na licu mesta do gotovog objekta'),

('Izrada metalnih konstrukcija', 'Nosive metalne konstrukcije'),
('Proizvodnja čeličnih konstrukcija po meri i projektu.',
 'Krovne, međuspratne i platforme. Veliki otvoren prostor bez stubova nasred prostorije.'),
('Izrada prema projektu i meri objekta', 'Krovne i međuspratne konstrukcije'),
('Stubovi, binderi i rožnjače', 'Platforme i rešetkasti nosači'),
('Ukrute i spojni elementi', 'Hale i nadstrešnice'),
('Priprema i obrada materijala', 'Izrada po projektu'),
('Kontrola kvaliteta pre isporuke', 'Antikorozivna zaštita pre isporuke'),

('Montaža konstrukcija', 'Kapije i ograde'),
('Stručna i sigurna montaža na terenu.',
 'Ulaz koji radi svaki dan bez zapinjanja i granica placa koja izgleda završeno.'),
('Izlazak i priprema terena', 'Klizne i krilne kapije'),
('Sigurna montaža nosivih elemenata', '3D panelne ograde'),
('Sklapanje prema projektu', 'Dvorišne i industrijske ograde'),
('Rad prema propisima i standardima', 'Balkonski gelenderi i dekorativne ograde'),
('Primopredaja gotove konstrukcije', 'Pocinkovanje i plastifikacija'),

('Zavarivanje metala', 'Stepeništa i PP stepeništa'),
('Profesionalno zavarivanje različitih vrsta metalnih elemenata.',
 'Bezbedan i miran hod. Protivpožarno stepenište je uslov za upotrebnu dozvolu.'),
('Zavarivanje čeličnih i metalnih elemenata', 'Unutrašnja i spoljna stepeništa'),
('Spojevi nosivih konstrukcija', 'Protivpožarna (evakuaciona) stepeništa'),
('Izrada po projektu i specifikaciji', 'Gazišta i gelenderi'),
('Čist i precizan zavar', 'Izrada po projektu'),
('Obrada i dorada spojeva', 'Prateća dokumentacija'),

('Nadstrešnice i hale', 'Letnje bašte i kontejneri'),
('Izrada čeličnih nadstrešnica, skladišta i industrijskih hala.',
 'Više stolova i gost koji sedi po kiši i zimi. Bašta se vraća kroz jednu sezonu.'),
('Nadstrešnice za vozila i terase', 'Letnje i zatvorene bašte'),
('Čelične hale i skladišta', 'Pergole, krov i zastakljenje'),
('Industrijski i poslovni objekti', 'Deking na metalnoj podkonstrukciji'),
('Kompletno: projekat → izrada → montaža', 'Modularni kontejneri: stambeni, magacinski, sanitarni'),
('Sklapanje na šrafove', 'Gotovo pre sezone'),

# ---------- KAKO RADIMO ----------
('Znate šta sledi, od upita do primopredaje.', 'Znate šta sledi, od poziva do primopredaje.'),
('Javite se sa opisom objekta. Po potrebi izlazimo na teren da sve vidimo na licu mesta.',
 'Recite šta, gde i za kada. Izlazimo na lokaciju i merimo na licu mesta.'),
('Dobijate jasnu ponudu unapred, bez skrivenih troškova i naknadnih iznenađenja.',
 'Ponuda je raspisana stavku po stavku: materijal, zaštita, rok i cena. Rok stoji u ponudi, ne dogovara se usput.'),
('Projektujemo, izrađujemo i montiramo: stručno, precizno i po dogovorenom planu.',
 'Najveći deo posla ide u radionici na Avalskoj. Na objekat izlazimo sa gotovim elementima, pa je vreme kod vas kratko.'),
('Predajemo završen objekat u dogovorenom roku, spreman za upotrebu.',
 'Montiramo, čistimo za sobom i predajemo posao. Kad kroz godinu dana zapne, vraćamo se na svoj rad.'),
('Čelični skelet hale u fazi montaže, pogled odozdo ka krovnim rešetkama',
 'Metalna konstrukcija platforme sa montiranom daskom 50 mm, MATIS New Point'),

# ---------- REZULTATI ----------
('Od privatnih nadstrešnica do industrijskih hala. Objekti završeni i predati.',
 'Od maske za klimu do zatvorene bašte i hale. [DOPUNITI: tačan broj završenih objekata]'),
('Stručan tim i savremena oprema iza svake konstrukcije.',
 'Radionica, oprema i ekipa iza svakog posla. [DOPUNITI: godina osnivanja]'),
('Stambeni, poslovni i industrijski objekti, projekti svih veličina.',
 'Ugostiteljstvo, firme i privatna lica. Od dvorišne kapije do objekta sa projektom.'),

# ---------- RADOVI ----------
('Nekoliko izdvojenih realizacija.', 'Nekoliko izdvojenih realizacija. Većinu možete i da obiđete.'),

('Skelet industrijske hale', 'Zatvorena bašta, Mileva Koncept'),
('Čelični skelet industrijske hale u montaži, dvije zglobne platforme i kamion sa dizalicom. Otvorite fotografiju.',
 'Zatvorena bašta sa staklenim zidovima i metalnom konstrukcijom, restoran Mileva Koncept u Grivcu. Otvorite fotografiju.'),

('Nadstrešnica nad terasom', 'Letnja bašta, Stara Srbija'),
('Čelična nadstrešnica nad terasom, pogled odozdo na rešetkastu konstrukciju. Otvorite fotografiju.',
 'Zastakljena letnja bašta na metalnoj konstrukciji, kafana Stara Srbija u Kragujevcu. Otvorite fotografiju.'),

('Nadstrešnica sa solarnim panelima, Jesenice', 'Ograda i gelenderi, Blazeks MV'),
('Velika čelična nadstrešnica nad parkingom sa solarnim panelima na krovu, snimak iz vazduha. Otvorite fotografiju.',
 'Pocinkovana i farbana ograda sa gelenderima, obložena kompakt pločama, objekat Blazeks MV na Aerodromu. Otvorite fotografiju.'),

('Hala na Kopaoniku', 'Modularni kontejneri'),
('Čelična hala obložena plavim trapeznim limom, radnici na merdevinama tokom oblađivanja. Otvorite fotografiju.',
 'Modularni kontejner NP Čelik, stambena izvedba sa prozorima i ulaznim vratima. Otvorite fotografiju.'),

('Poslovna hala', 'Lokal Čudesa'),
('Završena poslovna hala obložena sivim i bijelim sendvič panelima. Otvorite fotografiju.',
 'Enterijer lokala Čudesa u Kragujevcu, šank i metalna konstrukcija po meri prostora. Otvorite fotografiju.'),

# alt tekstovi hero galerije i kartica usluga
('Čelična konstrukcija hale sa krovnim rešetkama na vedrom nebu',
 'Dekorativna klizna kapija DOSTOJNA u Kutlovu, izrađena sa Simetra d.o.o.'),
('alt="Čelična konstrukcija hale"', 'alt="Dekorativna kapija DOSTOJNA, Kutlovo"'),
('Čelična nadstrešnica, pogled odozdo', 'Zatvorena bašta sa staklenim krovom, Mileva Koncept, Grivac'),
('alt="Montaža konstrukcije na terenu"', 'alt="Spoljna protivpožarna stepeništa, objekat Ženeva Lux"'),
('Montaža čelične konstrukcije na terenu', 'Spoljna protivpožarna metalna stepeništa na objektu Ženeva Lux'),
('Detalj zavarenog spoja stuba i rešetke', 'Krovna metalna konstrukcija sa rešetkastim nosačima, Caffe Porta'),
('Čelična nadstrešnica za vozila', 'Spoljno metalno stepenište sa gelenderom na stambenom objektu'),

# ---------- FAQ ----------
('Kako znam da ćete završiti na vreme?', 'Koliko traje?'),
('Poštovanje dogovorenih rokova nam je jedno od osnovnih načela. Rok dogovaramo unapred i držimo ga se. [DOPUNITI: prosječan rok isporuke po tipu objekta]',
 'Najveći deo se radi u radionici, pa je montaža na objektu kratka, obično jedan do tri dana za standardne radove. Rok upisujemo u ponudu, ne dogovaramo ga usput. [DOPUNITI: prosečan rok po tipu posla]'),

('Radite li i projekat i montažu, ili samo dio?', 'Da li će rđati?'),
('Radimo kompletno: projektovanje, izradu i montažu. Ne morate da koordinirate više izvođača, sve je na jednom mestu.',
 'Zavisi isključivo od pripreme. Radimo čišćenje, osnovnu zaštitu, pocinkovanje ili plastifikaciju i završne nanose. Pogledajte radove od pre nekoliko godina, stoje. [DOPUNITI: rok garancije]'),

('Kako se dobija ponuda i ima li skrivenih troškova?', 'Koliko to košta?'),
('Ponudu dajemo unapred, jasno i bez skrivenih troškova. Javite se sa opisom objekta, po potrebi izlazimo na teren, i dobijate konkretnu ponudu.',
 'Da vam ne bismo lupali cenu preko telefona, treba nam troje: šta, koje dimenzije i gde. Za orijentaciju odmah kažemo opseg po metru, a tačna cena ide posle izlaska na teren. Izlazak i procena su besplatni.'),

('Radite li za privatne investitore ili samo za firme?', 'Radite li male poslove?'),
('Radimo za sve: stambene (privatne) objekte, poslovne i industrijske. Od nadstrešnice za kuću do industrijske hale.',
 'Radimo, od maske za klima uređaj do hale. Mala stvar danas je često prvi posao od nekoliko.'),

('Kojim tipovima objekata se bavite?', 'Da li mi treba projekat ili dozvola?'),
('Metalne konstrukcije po meri: noseće i krovne konstrukcije, nadstrešnice, čelične hale, skladišta i industrijski objekti, projekti svih veličina.',
 'Za konstrukcije, protivpožarna stepeništa i veće objekte radi se po projektu. Radimo sa vašim projektantom ili vas uputimo na saradnika. Naš deo, izradu, montažu i prateću dokumentaciju, dobijate uredno. [DOPUNITI: koje ateste izdajete]'),

# ---------- KONTAKT ----------
('Recite nam šta vam treba. Ostalo je na nama.', 'Recite šta, gde i za kada. Ostalo je na nama.'),
('Čitamo svaki upit lično. Javite se sa opisom objekta, po potrebi izlazimo na teren, i dobijate konkretnu ponudu bez skrivenih troškova.',
 'Čitamo svaki upit lično. Opišite posao, izlazimo na teren i merimo, pa dobijate raspisanu ponudu. Izlazak i procena su besplatni.'),
('Šta gradite?', 'Šta vam treba?'),
('>Nadstrešnica<', '>Kapija ili ograda<'),
('>Čelična hala ili skladište<', '>Letnja bašta<'),
('>Noseća konstrukcija<', '>Stepenište<'),
('>Zavarivanje<', '>Konstrukcija, hala ili nadstrešnica<'),

# ---------- BREND ----------
('B-STEEL', 'NP ČELIK'),
('B-steel', 'NP Čelik'),
('B-Steel', 'NP Čelik'),
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
    print('  NIJE NADJENO:', m[:95])
