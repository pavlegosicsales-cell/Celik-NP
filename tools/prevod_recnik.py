# -*- coding: utf-8 -*-
"""Srpski -> engleski, za prekidac jezika na sajtu.

Kljuc je DOSLOVAN srpski tekst kakav stoji u HTML-u. Provjera pokrivenosti
ide kroz tools/prevod.py, koji izvlaci sve vidljive stringove sa stranica i
javlja sta nije prevedeno i sta je visak.

Imena objekata i firmi (Mileva Koncept, Zeneva Lux, Caffe Porta...) se ne
prevode. Isto vazi za adresu, telefon i mejl.
"""

PREVOD = {
    # --- navigacija, zaglavlje, podnozje ---
    "Početna": "Home",
    "O nama": "About",
    "Usluge": "Services",
    "Galerija": "Gallery",
    "Kontakt": "Contact",
    "Pozovi": "Call",
    "Navigacija": "Navigation",
    "Mreže": "Social",
    "Telefon": "Phone",
    "Mejl": "Email",
    "Email": "Email",
    "Radionica": "Workshop",
    "Radno vreme": "Opening hours",
    "Pon–pet, 07–16h": "Mon to Fri, 07:00 to 16:00",
    "Ponedeljak do petak, 07 do 16h": "Monday to Friday, 07:00 to 16:00",
    "Avalska 11, Kragujevac": "Avalska 11, Kragujevac",
    "npcelik85@gmail.com": "npcelik85@gmail.com",
    "Kragujevac, Šumadija i centralna Srbija": "Kragujevac, Sumadija and central Serbia",
    "NP ČELIK © 2026. Sva prava zadržana.": "NP CELIK © 2026. All rights reserved.",
    "Preskoči na sadržaj": "Skip to content",
    "Instagram": "Instagram",
    "Facebook": "Facebook",
    "Pozovite 060 41 45 466": "Call 060 41 45 466",

    # --- naslovi stranica ---
    "Metalne konstrukcije i bravarija Kragujevac | NP Čelik":
        "Steel structures and metalwork in Kragujevac | NP Celik",
    "Usluge | NP Čelik Kragujevac": "Services | NP Celik Kragujevac",
    "Nosive metalne konstrukcije | NP Čelik Kragujevac":
        "Load bearing steel structures | NP Celik Kragujevac",
    "Kapije i ograde | NP Čelik Kragujevac": "Gates and fences | NP Celik Kragujevac",
    "Stepeništa i protivpožarna | NP Čelik Kragujevac":
        "Staircases and fire escapes | NP Celik Kragujevac",
    "Letnje i zatvorene bašte | NP Čelik Kragujevac":
        "Terraces and enclosed gardens | NP Celik Kragujevac",
    "Enterijer i završna obrada | NP Čelik Kragujevac":
        "Interiors and finishing | NP Celik Kragujevac",
    "Galerija radova | NP Čelik Kragujevac": "Project gallery | NP Celik Kragujevac",
    "O nama | NP Čelik Kragujevac": "About us | NP Celik Kragujevac",
    "Kontakt | NP Čelik Kragujevac": "Contact | NP Celik Kragujevac",

    # --- pocetna: hero i sekcije ---
    "Izrada i montaža": "Fabrication and installation",
    "Konstrukcije, kapije": "Structures, gates",
    "i bašte po meri.": "and gardens, made to measure.",
    "Izlazimo na teren, merimo, izrađujemo u sopstvenoj radionici i montiramo svojom ekipom. Jedan sagovornik od prvog poziva do skidanja zaštitne folije.":
        "We come out, measure, fabricate in our own workshop and install with our own crew. One person to talk to, from the first call to peeling off the protective film.",
    "Zatražite ponudu": "Request a quote",
    "Naši radovi": "Our work",
    "Radovi": "Work",
    "Šta radimo": "What we do",
    "Za koga radimo": "Who we work for",
    "Kako radimo": "How we work",
    "Reference": "References",
    "Rezultati": "Results",
    "Put": "The road",
    "Upit": "Enquiry",
    "Ponuda": "Quote",
    "Predaja": "Handover",
    "Odgovori": "Answers",
    "Radimo": "We build",
    "Šta sledi": "What happens next",
    "Realizacija": "Delivery",
    "Primopredaja": "Handover",
    "Izlazak i mera": "Site visit and measuring",
    "Raspisana ponuda": "Itemised quote",
    "Upit i procena": "Enquiry and estimate",
    "Čitamo upit": "We read your enquiry",
    "od poziva": "from your call",
    "do primopredaje.": "to handover.",
    "realizacija.": "delivery.",
    "Od mere na licu mesta,": "From measuring on site,",
    "do gotovog objekta": "to a finished job",
    ", sa poštovanjem dogovorenih rokova.": ", with the agreed deadlines kept.",
    "temeljno i precizno": "thoroughly and precisely",
    "Znate šta sledi,": "You know what comes next,",
    "Bez improvizacije, svaki korak je jasan unapred.":
        "No improvising. Every step is clear up front.",
    "Znate šta se dešava posle upita": "You know what happens after your enquiry",
    "Bravarska radionica na Avalskoj 11. Mera, izrada, antikorozivna zaštita i montaža su naša ekipa, pa nema situacije da bravar krivi farbara, a farbar montera.":
        "A metalwork shop at Avalska 11. Measuring, fabrication, anti corrosion protection and installation are all our own crew, so there is no blaming the painter or the fitter.",
    "NP Čelik radi na Avalskoj 11 u Kragujevcu od 2018. Mera, izrada, antikorozivna zaštita i montaža su naša ekipa, pa nema situacije da bravar krivi farbara, a farbar montera. Jedan sagovornik od prvog poziva do skidanja zaštitne folije.":
        "NP Celik has worked at Avalska 11 in Kragujevac since 2018. Measuring, fabrication, anti corrosion protection and installation are all our own crew, so there is no blaming the painter or the fitter. One person to talk to, from the first call to peeling off the protective film.",
    "Raspon usluga": "Range of work",
    "Mera → izrada → montaža": "Measure → fabricate → install",
    "Ceo posao pod jednim krovom. Jedna odgovornost i jedan sagovornik.":
        "The whole job under one roof. One responsibility, one person to talk to.",
    "Područje rada": "Where we work",
    "Kragujevac ·": "Kragujevac ·",
    "Šumadija i centralna Srbija": "Sumadija and central Serbia",
    "Izlazak na teren i procena su besplatni.": "Site visits and estimates are free.",
    "Tipovi objekata": "Types of property",
    "Ugostiteljstvo · firme · privatna lica": "Hospitality · companies · private clients",
    "Od maske za klima uređaj do noseće krovne konstrukcije i hale.":
        "From an air conditioning cover to a load bearing roof structure and a hall.",

    # --- usluge, kratki opisi ---
    "Nosive metalne konstrukcije": "Load bearing steel structures",
    "Kapije i ograde": "Gates and fences",
    "Stepeništa i protivpožarna stepeništa": "Staircases and fire escapes",
    "Letnje i zatvorene bašte": "Terraces and enclosed gardens",
    "Enterijer i završna obrada": "Interiors and finishing",
    "Modularni kontejneri": "Modular containers",
    "Modularni kontejner": "Modular container",
    "Krovne, međuspratne i platforme. Veliki otvoren prostor bez stubova nasred prostorije.":
        "Roof, intermediate floor and platform structures. Large open space with no columns in the middle of the room.",
    "Krovne, međuspratne i platforme. Veliki otvoren prostor bez stubova nasred prostorije, brža gradnja nego betonom i manje opterećenje na objekat.":
        "Roof, intermediate floor and platform structures. Large open space with no columns in the middle of the room, faster to build than concrete and less load on the building.",
    "Ulaz koji radi svaki dan bez zapinjanja i granica placa koja izgleda završeno.":
        "An entrance that works every day without sticking, and a boundary that looks finished.",
    "Ulaz koji radi svaki dan bez zapinjanja i granica placa koja izgleda završeno, a ne improvizovano. Klizne i krilne kapije, panelne, dvorišne i industrijske ograde.":
        "An entrance that works every day without sticking, and a boundary that looks finished rather than improvised. Sliding and swing gates, panel, yard and industrial fences.",
    "Bezbedan i miran hod. Protivpožarno stepenište je uslov za upotrebnu dozvolu.":
        "A safe, quiet climb. A fire escape is a condition for the occupancy permit.",
    "Bezbedan i miran hod, stepenište koje ne peva i ne klizi. Protivpožarno stepenište je uslov za pregled i upotrebnu dozvolu.":
        "A safe, quiet climb on a staircase that neither sings nor slips. A fire escape is a condition for inspection and the occupancy permit.",
    "Više stolova i gost koji sedi po kiši i zimi. Bašta se vraća kroz jednu sezonu.":
        "More tables and guests who stay seated in rain and in winter. A terrace pays for itself in one season.",
    "Više stolova i gost koji sedi po kiši i zimi. Bašta se vraća kroz jednu sezonu, ne kroz godine.":
        "More tables and guests who stay seated in rain and in winter. A terrace pays for itself in one season, not over years.",
    "Metal nosi ono što zid ne može": "Steel carries what a wall cannot",
    "Metal nosi, a drvo, staklo i kompakt ploče daju izgled. Lokal dobija prepoznatljiv karakter, sve po meri prostora, ne iz kataloga.":
        "Steel carries the load, while wood, glass and compact panels give the look. The place gets its own character, all made to fit the space, not picked from a catalogue.",
    "Modularni kontejneri: stambeni, magacinski, sanitarni":
        "Modular containers: living, storage, sanitary",
    "Gotov, useljiv prostor za nedelje umesto meseci. Kad se posao preseli, kontejner ide sa vama. Za razliku od svega ostalog što radimo po meri, ovo je proizvod: poznat rok, poznata izrada.":
        "A finished, usable space in weeks instead of months. When the job moves, the container moves with you. Unlike everything else we make to measure, this is a product: known lead time, known build.",

    # --- pod-stranice usluga ---
    "Pogledajte detaljno": "See the details",
    "Pitajte za kontejner": "Ask about containers",
    "Pogledajte usluge": "See our services",
    "Obim posla:": "Scope of work:",
    "Izrada po projektu": "Built to drawings",
    "Krovne konstrukcije": "Roof structures",
    "Krovne i međuspratne konstrukcije": "Roof and intermediate floor structures",
    "Međuspratne i platforme": "Intermediate floors and platforms",
    "Platforme i rešetkasti nosači": "Platforms and truss girders",
    "Hale i nadstrešnice": "Halls and canopies",
    "Antikorozivna zaštita": "Anti corrosion protection",
    "Antikorozivna zaštita pre isporuke": "Anti corrosion protection before delivery",
    "Montaža sopstvenom ekipom": "Installed by our own crew",
    "Klizne kapije": "Sliding gates",
    "Klizne i krilne kapije": "Sliding and swing gates",
    "Dekorativne kapije": "Decorative gates",
    "Dvorišne i industrijske ograde": "Yard and industrial fences",
    "3D panelne ograde": "3D panel fences",
    "Balkonski gelenderi i dekorativne ograde": "Balcony railings and decorative fences",
    "Oblaganje kompaktom": "Compact panel cladding",
    "Oblaganje kompakt pločama": "Compact panel cladding",
    "Pocinkovanje i plastifikacija": "Galvanising and powder coating",
    "Unutrašnja stepeništa": "Interior staircases",
    "Unutrašnja i spoljna stepeništa": "Interior and exterior staircases",
    "Spoljna stepeništa": "Exterior staircases",
    "Spoljno stepenište": "Exterior staircase",
    "Protivpožarna stepeništa": "Fire escapes",
    "Protivpožarno stepenište": "Fire escape",
    "Protivpožarna (evakuaciona) stepeništa": "Fire escape (evacuation) staircases",
    "Gazišta i gelenderi": "Treads and railings",
    "Zatvorene bašte": "Enclosed gardens",
    "Letnje bašte i pergole": "Terraces and pergolas",
    "Letnje bašte i kontejneri": "Terraces and containers",
    "Pergole, krov i zastakljenje": "Pergolas, roofing and glazing",
    "Staklene pregrade": "Glass partitions",
    "Drvena obloga i tavanica": "Timber cladding and ceiling",
    "Deking": "Decking",
    "Deking na metalnoj podkonstrukciji": "Decking on a steel substructure",
    "Šankovi i enterijerske konstrukcije": "Bars and interior structures",
    "Šankovi, stolovi i police": "Bars, tables and shelving",
    "Dekorativni metalni detalji": "Decorative steel details",
    "Maske za klima uređaje": "Air conditioning covers",
    "Ukrasne maske za klima uređaje": "Decorative air conditioning covers",
    "Stambeni": "Living",
    "Magacinski": "Storage",
    "Građevinski": "Site",
    "Sanitarni": "Sanitary",
    "Premeštanje na novu lokaciju": "Relocation to a new site",
    "Zaštita koja traje": "Protection that lasts",
    "Prateća dokumentacija": "Supporting documents",
    "Rad bez zatvaranja lokala": "Work without closing the venue",
    "Prostor koji radi dvanaest meseci": "A space that works twelve months a year",
    "Posao sa projektom i sa odgovornošću": "Work with drawings and with responsibility",
    "Prvi utisak o kući i o firmi": "The first impression of a house and of a company",
    "Detalj po kome se lokal pamti": "The detail a venue is remembered by",
    "Iz ponude profila.": "From the profile range.",
    "Radi se i kao samostalan posao.": "Also done as a standalone job.",
    "Radi se uz enterijerske konstrukcije.": "Done together with the interior structures.",
    "Dogovara se pre početka.": "Agreed before work starts.",
    "Garancija na zaštitu dve godine.": "Two year warranty on the protective coating.",
    "Kad prostor treba da ostane otvoren, konstrukcija ide u metal. Nema stubova nasred sale, raspon je veći, a objekat nosi manje težine nego sa betonskom pločom.":
        "When a space has to stay open, the structure goes in steel. No columns in the middle of the room, longer spans, and the building carries less weight than with a concrete slab.",
    "Kapija se otvara svaki dan, po kiši i po mrazu. Zato se razlika između dobre i loše ne vidi na montaži nego kroz dve zime, na vođici, šarki i na mestu gde je zaštita popustila.":
        "A gate is opened every day, in rain and in frost. That is why the difference between a good and a bad one shows not at installation but after two winters, on the track, the hinge and wherever the coating gave way.",
    "Stepenište je jedini deo objekta po kome svi hodaju svaki dan. Ako pod nogom radi ili gazište klizi, to se ne popravlja farbanjem.":
        "A staircase is the one part of a building everyone walks on every day. If it moves underfoot or the tread is slippery, paint will not fix it.",
    "Ugostitelju bašta nije ukras nego stolovi. Otvorena radi četiri meseca, zastakljena i pokrivena radi celu godinu, a razlika se vidi na prvom kišnom vikendu.":
        "For a restaurant a terrace is not decoration, it is tables. An open one works four months, a glazed and covered one works all year, and the difference shows on the first rainy weekend.",
    "Enterijer je jedini deo posla koji gost stvarno gleda izbliza. Šank, pregrada i polica po meri prostora rade ono što nameštaj iz kataloga ne može.":
        "The interior is the one part of the job a guest really looks at up close. A bar, a partition and shelving made to fit do what catalogue furniture cannot.",
    "Radimo po projektu, sa vašim projektantom ili sa saradnikom na koga vas uputimo. Izrada ide u radionici na Avalskoj, pa je vreme na objektu kratko.":
        "We work to drawings, with your designer or with a partner we point you to. Fabrication happens in the workshop on Avalska, so time on site is short.",
    "Radimo od tipske panelne ograde do kapije koja je sama po sebi znak firme. Merimo na licu mesta, jer se otvor i pad terena ne pogađaju iz kataloga.":
        "We build everything from a standard panel fence to a gate that is a company sign in itself. We measure on site, because an opening and a slope cannot be guessed from a catalogue.",
    "Rešetkasti nosači i krovni skelet za ugostiteljske i poslovne objekte.":
        "Truss girders and roof frames for hospitality and commercial buildings.",
    "Konstrukcija platforme sa gotovom podnom oblogom, kad je potrebno dobiti sprat u postojećoj visini.":
        "A platform structure with a finished floor, for when you need an extra level within the existing height.",
    "Pokriven prostor za robu, mašine ili vozila, brzo i bez klasične gradnje.":
        "Covered space for goods, machinery or vehicles, quickly and without conventional building work.",
    "Priprema površine, pocinkovanje ili plastifikacija i završni nanosi, pre nego što konstrukcija dođe na objekat.":
        "Surface preparation, galvanising or powder coating and the final coats, before the structure reaches the site.",
    "Za dvorišta i poslovne ulaze, sa vođicom i nosačima dimenzionisanim prema širini otvora i nagibu terena.":
        "For yards and commercial entrances, with the track and supports sized to the width of the opening and the slope of the ground.",
    "Puno lice sa izrađenim znakom, kad kapija treba da radi i kao obeležje objekta.":
        "A solid face with a fabricated emblem, for when the gate also has to mark the property.",
    "Panelne, dvorišne, industrijske i balkonske, sa oblaganjem kompakt pločama kad fasada to traži.":
        "Panel, yard, industrial and balcony fences, with compact panel cladding when the facade calls for it.",
    "Pocinkovano i farbano sa svim nanosima. Ograda bez pripreme i cinka počne da rđa kroz dve zime i onda se plaća dvaput.":
        "Galvanised and painted with every coat. A fence without preparation and zinc starts to rust within two winters and then gets paid for twice.",
    "Nosač, gazišta i gelender uklopljeni u enterijer, sa obradom koja ne odaje da je konstrukcija metalna.":
        "Stringer, treads and railing fitted into the interior, finished so the structure does not read as steel.",
    "Prilazi i pomoćni ulazi na stambenim i poslovnim objektima, sa zaštitom računatom na spoljne uslove.":
        "Approaches and secondary entrances on residential and commercial buildings, with coatings rated for outdoor conditions.",
    "Spoljna evakuaciona stepeništa sa podestima i gelenderima, po projektu i pod pregledom.":
        "External evacuation staircases with landings and railings, built to drawings and subject to inspection.",
    "Dorada i zamena na postojećim stepeništima, kad je nosač dobar a hod nije.":
        "Reworking and replacement on existing staircases, when the structure is sound but the climb is not.",
    "Konstrukcija, krov i drvena obloga za terase i ulične bašte.":
        "Structure, roof and timber cladding for terraces and street gardens.",
    "Metalna konstrukcija, zastakljenje i drvena tavanica, za rad tokom cele godine.":
        "Steel structure, glazing and a timber ceiling, for use all year round.",
    "Podela prostora bez zidanja, sa metalnim okvirom koji ostaje vidljiv kao deo enterijera.":
        "Dividing a space without masonry, with a steel frame left visible as part of the interior.",
    "Drvena terasa na metalnoj podkonstrukciji. Ostaje ravna i posle zima, ne uleže i ne krivi se kao na drvenoj podlozi.":
        "A timber deck on a steel substructure. It stays flat after winters, it does not sag or warp the way it does on a timber base.",
    "Nosive i vidljive konstrukcije za ugostiteljske lokale, izrađene prema merama prostora.":
        "Load bearing and exposed structures for hospitality venues, made to the dimensions of the space.",
    "Instalacije nestaju sa fasade i objekat izgleda dovršeno.":
        "The units disappear from the facade and the building looks finished.",
    "Završna obloga na ogradama i konstrukcijama, kad fasada traži ravnu površinu bez vidljivog profila.":
        "A finishing skin on fences and structures, when the facade calls for a flat surface with no visible profile.",
    "Retko radimo samo metal. Metal nosi, a drvo, staklo i kompakt daju izgled, i kombinacija je i jača i lepša od bilo čega samostalno.":
        "We rarely work in steel alone. Steel carries the load, while wood, glass and compact panels give the look, and the combination is both stronger and better looking than any of them on its own.",
    "Najveći deo posla ide u radionici na Avalskoj. Na objekat izlazimo sa gotovim elementima, pa je vreme kod vas kratko.":
        "Most of the work happens in the workshop on Avalska. We arrive on site with finished elements, so the time spent at your place is short.",
    "Nađite posao koji odgovara vašem objektu, roku i budžetu. Sve radimo istom ekipom: mera na licu mesta, izrada u radionici na Avalskoj, zaštita i montaža.":
        "Find the job that fits your building, your deadline and your budget. We do all of it with the same crew: measuring on site, fabrication in the workshop on Avalska, coating and installation.",

    # --- o nama ---
    "Radionica sa adresom,": "A workshop with an address,",
    "ekipa sa imenom.": "a crew with a name.",
    "Od maske za klimu do noseće konstrukcije":
        "From an air conditioning cover to a load bearing structure",
    "Radimo i tehnički zahtevne poslove sa projektom i odgovornošću, i sitne dorade u dvorištu.":
        "We take on technically demanding jobs with drawings and responsibility, and small fixes in the yard.",
    "Protivpožarna stepeništa, platforme i krovne konstrukcije su posao koji nas odvaja od radionica koje rade samo tipske ograde.":
        "Fire escapes, platforms and roof structures are the work that sets us apart from shops that only build standard fences.",
    "Ugostitelji, firme i ljudi iz komšiluka": "Restaurants, companies and neighbours",
    "Znamo šta znači „mora da bude gotovo pre sezone\" i planiramo posao oko tog datuma. Zato se bašte ugovaraju zimi.":
        "We know what \"it has to be done before the season\" means and we plan the job around that date. That is why terraces are agreed in winter.",
    "Isto tako izlazimo i za jednu masku za klima uređaj, jer je mala stvar danas često prvi posao od nekoliko.":
        "We will just as gladly come out for a single air conditioning cover, because a small job today is often the first of several.",
    "Pravila koja se vide posle pet godina": "Rules you can still see after five years",
    "Bez prebacivanja odgovornosti": "No passing the blame",
    "Ceo posao pod jednim krovom": "The whole job under one roof",
    "Mera, izrada, zaštita i montaža su naša ekipa. Nema prebacivanja odgovornosti između bravara, farbara i montera, jer su to isti ljudi.":
        "Measuring, fabrication, coating and installation are our own crew. There is no passing blame between the metalworker, the painter and the fitter, because they are the same people.",
    "Garancija dve godine": "Two year warranty",
    "Zaštita je deo posla, ne dodatak": "Protection is part of the job, not an extra",
    "Priprema površine, pocinkovanje ili plastifikacija i svi nanosi boje. Ograda bez pripreme i cinka počne da rđa kroz dve zime i onda se plaća dvaput.":
        "Surface preparation, galvanising or powder coating and every coat of paint. A fence without preparation and zinc starts to rust within two winters and then gets paid for twice.",
    "Ne dogovara se usput": "Not agreed along the way",
    "Rok stoji u ponudi": "The deadline is in the quote",
    "Ako nešto ne stižemo, kažemo unapred, jer je bolje čuti istinu na početku nego datum koji ne možemo da ispunimo.":
        "If we cannot make something, we say so up front, because hearing the truth at the start beats a date we cannot keep.",
    "Radionica na Avalskoj 11": "The workshop at Avalska 11",
    "Vraćamo se na svoj rad": "We come back to our own work",
    "Kad kroz godinu dana zapne kapija ili treba dorada, ne tražite firmu iz Beograda. Tu smo gde smo i bili.":
        "When a gate sticks a year later or needs adjusting, you are not looking for a company from Belgrade. We are where we have always been.",
    "Kako je radionica rasla": "How the workshop grew",
    "Osam godina, preko dvadeset objekata i sopstvena radionica na Avalskoj 11.":
        "Eight years, more than twenty completed jobs and our own workshop at Avalska 11.",
    "Radionica na Avalskoj": "The workshop on Avalska",
    "NP Čelik počinje sa radom u Kragujevcu. Bravarski radovi, kapije i ograde za dvorišta i firme u gradu.":
        "NP Celik starts work in Kragujevac. Metalwork, gates and fences for yards and companies in town.",
    "Prve letnje bašte": "The first terraces",
    "Rad na ugostiteljskim objektima u Kragujevcu i okolini. Kafana Paligorić, „Stara Srbija\", Caffe Porta.":
        "Work on hospitality venues in and around Kragujevac. Kafana Paligoric, \"Stara Srbija\", Caffe Porta.",
    "Serija NP Čelik kontejnera: stambeni, magacinski, građevinski i sanitarni. Za razliku od svega ostalog što radimo po meri, ovo je proizvod sa poznatim rokom.":
        "The NP Celik container line: living, storage, site and sanitary. Unlike everything else we make to measure, this is a product with a known lead time.",
    "Preko dvadeset objekata": "More than twenty completed jobs",
    "Sopstvena radionica i montaža. Protivpožarna stepeništa, zatvorene bašte i konstrukcije po projektu.":
        "Our own workshop and installation crew. Fire escapes, enclosed gardens and structures built to drawings.",
    "Radovi koje možete da obiđete": "Work you can go and see",
    "Fotografija": "Photo",
    "Recite šta vam treba,": "Tell us what you need,",
    "izlazimo i merimo.": "we come out and measure.",
    "Izlazak na teren i procena su besplatni. Posle mere dobijate raspisanu ponudu, sa rokom koji stoji u njoj.":
        "Site visits and estimates are free. After measuring you get an itemised quote, with the deadline written into it.",
    "Više o nama": "More about us",
    "Godina iskustva": "Years of experience",
    "Realizovanih projekata": "Completed projects",
    "Segmenta koja pokrivamo": "Segments we cover",
    "Od maske za klimu do zatvorene bašte i hale. Objekti završeni i predati.":
        "From an air conditioning cover to an enclosed garden and a hall. Jobs finished and handed over.",
    "Radionica na Avalskoj radi od 2018. Četvoro ljudi, oprema i sopstvena ekipa iza svakog posla.":
        "The workshop on Avalska has been running since 2018. Four people, the equipment and our own crew behind every job.",
    "Ugostiteljstvo, firme i privatna lica. Od dvorišne kapije do objekta sa projektom.":
        "Hospitality, companies and private clients. From a yard gate to a building with drawings.",
    "Nekoliko izdvojenih": "A few selected",
    "Pogledajte sve realizovane radove": "See all completed work",
    "Vidi još radova": "See more work",

    # --- galerija ---
    "Radovi NP Čelika u Kragujevcu i Šumadiji. Kliknite na fotografiju da je vidite u punoj veličini.":
        "NP Celik projects in Kragujevac and Sumadija. Click a photo to see it full size.",
    "Zatvorena bašta": "Enclosed garden",
    "Konstrukcija bašte": "Garden structure",
    "Pergola sa lamelama": "Louvred pergola",
    "Krovna konstrukcija": "Roof structure",
    "Zastakljena bašta": "Glazed garden",
    "Enterijer i šank": "Interior and bar",
    "Metalni detalji u lokalu": "Steel details in the venue",
    "Ograda i gelenderi": "Fence and railings",
    "Ograde i gelenderi": "Fences and railings",
    "Platforma": "Platform",
    "Klizna kapija": "Sliding gate",
    "Sopstveni proizvod": "Our own product",
    "Grivac": "Grivac",
    "Kragujevac": "Kragujevac",
    "Sušica": "Susica",
    "Kutlovo": "Kutlovo",
    "Aerodrom, Kragujevac": "Aerodrom, Kragujevac",
    "NP Čelik": "NP Celik",
    "Mileva Koncept": "Mileva Koncept",
    "Ženeva Lux": "Zeneva Lux",
    "Caffe Porta": "Caffe Porta",
    "Kafana Paligorić": "Kafana Paligoric",
    "Stara Srbija": "Stara Srbija",
    "Lokal Čudesa": "Cudesa venue",
    "Lokal „Čudesa\"": "\"Cudesa\" venue",
    "Blazeks MV": "Blazeks MV",
    "BLAŽEKS nameštaj": "BLAZEKS furniture",
    "MATIS New Point": "MATIS New Point",
    "Kapija „DOSTOJNA\"": "\"DOSTOJNA\" gate",
    "Kapija DOSTOJNA, Kutlovo": "DOSTOJNA gate, Kutlovo",
    "Ford salon": "Ford showroom",
    "Zatvorena bašta · Grivac": "Enclosed garden · Grivac",
    "Protivpožarna stepeništa · Kragujevac": "Fire escapes · Kragujevac",
    "Krovna konstrukcija · Kragujevac": "Roof structure · Kragujevac",
    "Letnja bašta · Kragujevac": "Terrace · Kragujevac",
    "Zastakljena bašta · Kragujevac": "Glazed garden · Kragujevac",
    "Enterijer i šank · Kragujevac": "Interior and bar · Kragujevac",
    "Ograda i gelenderi · Aerodrom": "Fence and railings · Aerodrom",
    "Stepenište · Sušica": "Staircase · Susica",
    "Platforma · Kragujevac": "Platform · Kragujevac",
    "Sa Simetra d.o.o. · Kutlovo": "With Simetra d.o.o. · Kutlovo",
    "Klizne kapije i 3D paneli": "Sliding gates and 3D panels",

    # --- kontakt i wizard ---
    "Recite šta, gde i za kada.": "Tell us what, where and by when.",
    "Ostalo je na nama.": "The rest is on us.",
    "Recite šta, gde i za kada. Ostalo je na nama.":
        "Tell us what, where and by when. The rest is on us.",
    "Recite šta, gde i za kada. Izlazimo na lokaciju i merimo na licu mesta.":
        "Tell us what, where and by when. We come to the site and measure in person.",
    "Čitamo svaki upit lično. Opišite posao, izlazimo na teren i merimo, pa dobijate raspisanu ponudu. Izlazak i procena su besplatni.":
        "We read every enquiry ourselves. Describe the job, we come out and measure, then you get an itemised quote. Site visits and estimates are free.",
    "Čitamo svaki upit lično. Opišite posao, izlazimo na teren i merimo na licu mesta, pa dobijate raspisanu ponudu. Izlazak i procena su besplatni.":
        "We read every enquiry ourselves. Describe the job, we come out and measure in person, then you get an itemised quote. Site visits and estimates are free.",
    "Korak 1 od 5": "Step 1 of 5",
    "Šta vam treba?": "What do you need?",
    "Kapija ili ograda": "A gate or a fence",
    "Letnja ili zatvorena bašta": "A terrace or an enclosed garden",
    "Stepenište ili PP stepenište": "A staircase or a fire escape",
    "Konstrukcija, hala, nadstrešnica": "A structure, hall or canopy",
    "Nešto drugo": "Something else",
    "Kakav je objekat?": "What kind of property is it?",
    "Ugostiteljski lokal": "A hospitality venue",
    "Poslovni objekat ili firma": "A commercial building or company",
    "Kuća ili dvorište": "A house or a yard",
    "Gradilište u toku": "An active construction site",
    "Gde je posao?": "Where is the job?",
    "Šumadija, van Kragujevca": "Sumadija, outside Kragujevac",
    "Centralna Srbija": "Central Serbia",
    "Drugde": "Somewhere else",
    "Za kada vam treba?": "When do you need it?",
    "Hitno": "Urgently",
    "U toku ovog meseca": "Within this month",
    "Pre sezone": "Before the season",
    "Još planiram": "Still planning",
    "Vaši podaci": "Your details",
    "Ime i prezime": "Full name",
    "Mejl, ako želite ponudu pismeno": "Email, if you want the quote in writing",
    "Dimenzije, rok, sve što znate o poslu": "Dimensions, deadline, anything you know about the job",
    "Javljamo se isti ili sledeći radni dan. Ako vam se žuri, pozovite 060 41 45 466.":
        "We get back to you the same or the next working day. If you are in a hurry, call 060 41 45 466.",
    "Dalje": "Next",
    "Nazad": "Back",
    "Pošaljite upit": "Send enquiry",
    "Upit je stigao": "Your enquiry arrived",
    "Upit stiže direktno nama, ne u zajednički sandučić. Javljamo se isti ili sledeći radni dan.":
        "The enquiry comes straight to us, not to a shared inbox. We get back to you the same or the next working day.",
    "Dolazimo na lokaciju, merimo na licu mesta i predlažemo rešenje. Izlazak i procena su besplatni.":
        "We come to the site, measure in person and propose a solution. Site visits and estimates are free.",
    "Dobijate ponudu stavku po stavku: materijal, zaštita, rok i cena. Rok stoji u ponudi, ne dogovara se usput.":
        "You get a quote item by item: material, coating, deadline and price. The deadline is in the quote, not agreed along the way.",
    "Ponuda je raspisana stavku po stavku: materijal, zaštita, rok i cena. Rok stoji u ponudi, ne dogovara se usput.":
        "The quote is itemised: material, coating, deadline and price. The deadline is in the quote, not agreed along the way.",
    "Montiramo, čistimo za sobom i predajemo posao. Kad kroz godinu dana zapne, vraćamo se na svoj rad.":
        "We install, clean up after ourselves and hand the job over. If something sticks a year later, we come back to our own work.",
    "Otvori mapu": "Open the map",
    "Uvećajte mapu": "Enlarge the map",
    "Uvećajte kartu lokacije": "Enlarge the location map",
    "44.0165° N, 20.9114° E": "44.0165° N, 20.9114° E",
    "Otvorite fotografiju": "Open the photo",

    # --- pitanja ---
    "Česta pitanja": "Common questions",
    "Koliko to košta?": "How much does it cost?",
    "Da vam ne bismo lupali cenu preko telefona, treba nam troje: šta, koje dimenzije i gde. Za orijentaciju odmah kažemo opseg po metru, a tačna cena ide posle izlaska na teren. Izlazak i procena su besplatni.":
        "Rather than guess a price over the phone, we need three things: what, what size and where. We will give you a range per metre straight away, and the exact price follows the site visit. Site visits and estimates are free.",
    "Koliko traje?": "How long does it take?",
    "Najveći deo se radi u radionici, pa je vreme na vašem objektu kratko. Rok zavisi od posla i njegovog obima, a upisujemo ga u ponudu, ne dogovaramo ga usput.":
        "Most of it is done in the workshop, so the time on your site is short. The deadline depends on the job and its scope, and we write it into the quote rather than agreeing it along the way.",
    "Da li će rđati?": "Will it rust?",
    "Zavisi isključivo od pripreme. Radimo čišćenje, osnovnu zaštitu, pocinkovanje ili plastifikaciju i završne nanose. Pogledajte radove od pre nekoliko godina, stoje. Na antikorozivnu zaštitu dajemo garanciju od dve godine.":
        "It depends entirely on the preparation. We clean, prime, galvanise or powder coat and apply the final coats. Look at work from a few years back, it is still standing. We give a two year warranty on the anti corrosion coating.",
    "Da li izlazite na teren i koje područje pokrivate?": "Do you come out, and what area do you cover?",
    "Radionica je na Avalskoj 11 u Kragujevcu. Baza nam je Kragujevac i Šumadija, a izlazimo na teren širom centralne Srbije: Grivac, Kutlovo, Sušica, Kosmaj.":
        "The workshop is at Avalska 11 in Kragujevac. Our base is Kragujevac and Sumadija, and we travel across central Serbia: Grivac, Kutlovo, Susica, Kosmaj.",
    "Da li mi treba projekat ili dozvola?": "Do I need drawings or a permit?",
    "Za konstrukcije, protivpožarna stepeništa i veće objekte radi se po projektu. Radimo sa vašim projektantom ili vas uputimo na saradnika. Naš deo je izrada i montaža. Po završenom poslu dobijate račun; atest i izjavu izvođača, ako ih objekat traži, pribavlja projektant.":
        "Structures, fire escapes and larger buildings are built to drawings. We work with your designer or point you to a partner. Our part is fabrication and installation. When the job is done you get an invoice; the certificate and contractor statement, if the building requires them, are obtained by the designer.",
    "Radite li male poslove?": "Do you take small jobs?",
    "Radimo, od maske za klima uređaj do hale. Mala stvar danas je često prvi posao od nekoliko.":
        "We do, from an air conditioning cover to a hall. A small job today is often the first of several.",
    "Radite li male poslove? ": "Do you take small jobs?",
    "Rad bez zatvaranja lokala ": "Work without closing the venue",
    "Većina posla se odradi u radionici. Na objekat izlazimo sa gotovim elementima, radimo van radnog vremena kad je moguće i za sobom čistimo.":
        "Most of the work is done in the workshop. We arrive with finished elements, work outside opening hours where possible and clean up after ourselves.",
    "pre nego što pitate.": "before you ask.",
    "Gotovo pre sezone": "Done before the season",
    "Znamo šta znači „mora da bude gotovo pre sezone\" i planiramo posao oko tog datuma. Zato se bašte ugovaraju zimi. Ako je kasno, reći ćemo iskreno šta stižemo, a šta ne.":
        "We know what \"it has to be done before the season\" means and we plan the job around that date. That is why terraces are agreed in winter. If it is late, we will tell you honestly what we can and cannot manage.",

    # --- alt tekstovi fotografija ---
    "Zatvorena bašta sa drvenom tavanicom, Mileva Koncept, Grivac":
        "Enclosed garden with a timber ceiling, Mileva Koncept, Grivac",
    "Metalna konstrukcija zatvorene bašte spolja, Mileva Koncept, Grivac":
        "Steel structure of the enclosed garden from outside, Mileva Koncept, Grivac",
    "Protivpožarno metalno stepenište, Ženeva Lux": "Steel fire escape, Zeneva Lux",
    "Protivpožarno metalno stepenište, Ženeva Lux, Kragujevac":
        "Steel fire escape, Zeneva Lux, Kragujevac",
    "Bela pergola sa lamelama i vertikalnim rešetkama, Ženeva Lux":
        "White louvred pergola with vertical screens, Zeneva Lux",
    "Krovne rešetke i noseća konstrukcija, Caffe Porta":
        "Roof trusses and load bearing structure, Caffe Porta",
    "Krovne rešetke i noseća metalna konstrukcija, Caffe Porta":
        "Roof trusses and load bearing steel structure, Caffe Porta",
    "Zastakljena letnja bašta, kafana Stara Srbija":
        "Glazed terrace, Stara Srbija tavern",
    "Metalni enterijer i šank, lokal Čudesa": "Steel interior and bar, Cudesa venue",
    "Metalni enterijer i šank, lokal Čudesa, Kragujevac":
        "Steel interior and bar, Cudesa venue, Kragujevac",
    "Metalni detalji i konstrukcija u lokalu Čudesa":
        "Steel details and structure in the Cudesa venue",
    "Ograda obložena kompaktom, Blazeks MV": "Fence clad in compact panels, Blazeks MV",
    "Ograda obložena kompaktom sa gelenderima, Blazeks MV":
        "Fence clad in compact panels with railings, Blazeks MV",
    "Spoljno metalno stepenište, BLAŽEKS nameštaj, Sušica":
        "External steel staircase, BLAZEKS furniture, Susica",
    "Spoljno metalno stepenište, NP Čelik": "External steel staircase, NP Celik",
    "Metalna konstrukcija platforme, MATIS New Point":
        "Steel platform structure, MATIS New Point",
    "Metalna konstrukcija platforme sa daskom 50 mm, MATIS New Point":
        "Steel platform structure with 50 mm boards, MATIS New Point",
    "Dekorativna klizna kapija DOSTOJNA, Kutlovo":
        "Decorative sliding gate DOSTOJNA, Kutlovo",
    "Modularni kontejner NP Čelika sa zastakljenom stranom":
        "NP Celik modular container with a glazed side",
    "Deking uz bazen i metalna konstrukcija nadstrešnice, u zalazak sunca":
        "Poolside decking and a steel canopy structure at sunset",
    "Metalna konstrukcija u izradi, radovi NP Čelika":
        "Steel structure under fabrication, NP Celik work",
    "Zatvorena bašta, Mileva Koncept": "Enclosed garden, Mileva Koncept",
    "Letnja bašta, Stara Srbija": "Terrace, Stara Srbija",
    "Ograda i gelenderi, Blazeks MV": "Fence and railings, Blazeks MV",
    "Zatvorena bašta, restoran Mileva Koncept, Grivac.":
        "Enclosed garden, Mileva Koncept restaurant, Grivac.",
    "Zatvorena bašta sa staklenim zidovima i metalnom konstrukcijom, restoran Mileva Koncept u Grivcu. Otvorite fotografiju.":
        "Enclosed garden with glass walls and a steel structure, Mileva Koncept restaurant in Grivac. Open the photo.",
    "Zastakljena letnja bašta na metalnoj konstrukciji, kafana Stara Srbija u Kragujevcu. Otvorite fotografiju.":
        "Glazed terrace on a steel structure, Stara Srbija tavern in Kragujevac. Open the photo.",
    "Pocinkovana i farbana ograda sa gelenderima, obložena kompakt pločama, objekat Blazeks MV na Aerodromu. Otvorite fotografiju.":
        "Galvanised and painted fence with railings, clad in compact panels, Blazeks MV on Aerodrom. Open the photo.",
    "Modularni kontejner NP Čelik, stambena izvedba sa prozorima i ulaznim vratima. Otvorite fotografiju.":
        "NP Celik modular container, living version with windows and an entrance door. Open the photo.",
    "Enterijer lokala Čudesa u Kragujevcu, šank i metalna konstrukcija po meri prostora. Otvorite fotografiju.":
        "Interior of the Cudesa venue in Kragujevac, bar and steel structure made to fit. Open the photo.",
    "Metalna PP stepeništa, objekat Ženeva Lux.": "Steel fire escapes, Zeneva Lux.",
    "Krovna konstrukcija Caffe Porta, Kragujevac.":
        "Roof structure, Caffe Porta, Kragujevac.",
    "Kafana Paligorić i „Stara Srbija\", Kragujevac.":
        "Kafana Paligoric and \"Stara Srbija\", Kragujevac.",
    "Lokal „Čudesa\", Kragujevac.": "\"Cudesa\" venue, Kragujevac.",
    "Ograda obložena kompaktom, Blazeks MV, Aerodrom.":
        "Fence clad in compact panels, Blazeks MV, Aerodrom.",
    "Stepenište za BLAŽEKS nameštaj, Sušica.": "Staircase for BLAZEKS furniture, Susica.",
    "Platforma sa daskom 50 mm i azmofonom, MATIS New Point.":
        "Platform with 50 mm boards and acoustic insulation, MATIS New Point.",
    "Kapija „DOSTOJNA\", Kutlovo, u saradnji sa Simetra d.o.o.":
        "\"DOSTOJNA\" gate, Kutlovo, in partnership with Simetra d.o.o.",
    "Klizne kapije i 3D paneli, Ford salon.":
        "Sliding gates and 3D panels, Ford showroom.",
    "Ukrasne maske, objekat „Orbita života\".":
        "Decorative covers, \"Orbita zivota\" building.",
    "Deking uz bazen, Kosmaj.": "Poolside decking, Kosmaj.",
    "Više objekata u Kragujevcu.": "Several buildings in Kragujevac.",
    "Stepeništa i PP stepeništa": "Staircases and fire escapes",
    "Ograda Blazeks MV, Aerodrom.": "Fence, Blazeks MV, Aerodrom.",
    "Protivpožarna stepeništa su zaseban posao: rade se po projektu, prolaze pregled i bez njih objekat ne dobija upotrebnu dozvolu. To nas odvaja od radionica koje rade samo tipske ograde.":
        "Fire escapes are a job of their own: built to drawings, subject to inspection, and without them a building does not get its occupancy permit. That is what sets us apart from shops that only build standard fences.",

    # --- aria-label i alt koje citac ekrana koristi ---
    "Putanja": "Breadcrumb",
    "Glavna navigacija": "Main navigation",
    "Glavna navigacija, mobilna": "Main navigation, mobile",
    "Navigacija u podnožju": "Footer navigation",
    "Otvorite meni": "Open the menu",
    "Zatvorite pregled": "Close the preview",
    "Pregled fotografije": "Photo preview",
    "Spisak usluga": "List of services",
    "Fotografije radova": "Photos of our work",
    "Šta radimo i za koga radimo": "What we do and who we do it for",
    "Sljedeći rad": "Next project",
    "Prethodni rad": "Previous project",
    "Sledeće pravilo": "Next rule",
    "Prethodno pravilo": "Previous rule",
    "NP Čelik na Facebooku": "NP Celik on Facebook",
    "NP Čelik na Instagramu": "NP Celik on Instagram",
    "NP Čelik, početna strana": "NP Celik, home page",
    "Pozovite nas na 060 41 45 466": "Call us on 060 41 45 466",
    "Spoljno metalno stepenište sa gelenderom na stambenom objektu":
        "External steel staircase with a railing on a residential building",
    "Drvena paluba uz bazen na Kosmaju, na metalnoj podkonstrukciji":
        "Timber poolside deck on Kosmaj, on a steel substructure",
    "Krovna metalna konstrukcija sa rešetkastim nosačima, Caffe Porta":
        "Steel roof structure with truss girders, Caffe Porta",
    "Spoljna protivpožarna metalna stepeništa na fasadi objekta Ženeva Lux":
        "External steel fire escapes on the facade of Zeneva Lux",
    "Dekorativna klizna kapija DOSTOJNA u Kutlovu, izrađena sa Simetra d.o.o.":
        "Decorative sliding gate DOSTOJNA in Kutlovo, built with Simetra d.o.o.",
    "Metalna konstrukcija platforme sa montiranom daskom 50 mm, MATIS New Point":
        "Steel platform structure with 50 mm boards fitted, MATIS New Point",
    "Modularni kontejner NP Čelik, stambena izvedba sa prozorima i ulaznim vratima":
        "NP Celik modular container, living version with windows and an entrance door",
    "Enterijer lokala Čudesa u Kragujevcu, šank i metalna konstrukcija po meri prostora":
        "Interior of the Cudesa venue in Kragujevac, bar and steel structure made to fit",
    "Zatvorena bašta sa drvenom tavanicom na metalnoj konstrukciji, Mileva Koncept, Grivac":
        "Enclosed garden with a timber ceiling on a steel structure, Mileva Koncept, Grivac",
    "Jezik": "Language",
}
