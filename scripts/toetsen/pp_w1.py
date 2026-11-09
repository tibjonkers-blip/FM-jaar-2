W = 1
P = "Verbeterproject"

# ---------- MC ----------
mc("pp1-m01", W, P, "In welke DMAGIC-fase heb je in periode 1 KSF's en KPI's afgeleid uit klantwaarde?",
   ["Define", "Measure", "Analyze", "Generate"], 0,
   "In Define baken je de opdracht af vanuit missie, visie en strategie en leid je KSF's en KPI's af uit klantwaarde. In Measure meet je de huidige situatie, in Analyze zoek je oorzaken.")
mc("pp1-m02", W, P, "Hoe is het project in periode 2 georganiseerd?",
   ["Als watervalproject met één grote oplevering aan het eind van week 7, zonder tussentijdse review",
        "In Scrum-light: twee sprints (week 1-3 en 4-6), met review bij de opdrachtgever en retrospective",
        "Als Kanban-project zonder sprints, met een doorlopend bord en alleen een eindpresentatie",
        "Met een stuurgroep van docent en opdrachtgever die elke week de voortgang formeel goedkeurt"], 1,
   "Je werkt in Scrum-light: twee sprints, een review bij de opdrachtgever (go/no-go in week 4) en een retrospective in de tweede les.")
mc("pp1-m03", W, P, "Wat is Kaizen?",
   ["Een eenmalige grote verbetering, bedacht door externe experts",
    "Continu verbeteren als gewoonte, in kleine stappen, door iedereen",
    "Het vastleggen van de beste werkwijze in een werkinstructie",
    "Het stilleggen van het proces zodra er een fout optreedt"], 1,
   "Kaizen is continu verbeteren in kleine stappen, door iedereen. Vastleggen is standaardisatie, stilleggen is 'stop de lijn'.")
mc("pp1-m04", W, P, "'Verspil nooit het creatieve potentieel van mensen.' Bij welk van de drie menselijke principes uit de les hoort deze uitspraak?",
   ["Kaizen", "Gemba", "Mensen", "Jidoka"], 2,
   "De drie menselijke principes zijn Kaizen, Gemba en Mensen. Bij 'mensen' gaat het erom dat medewerkers zich veilig voelen om problemen te benoemen en zelf met ideeën komen.")
mc("pp1-m05", W, P, "Een team begint een brainstorm over de schoonmaak zonder klantfeedback, KPI's of ergernissen van medewerkers. Welke brainstormstap slaat het team over?",
   ["Stap 1: een diverse blik, mensen van verschillende afdelingen",
    "Stap 2: de sessie voeden met klantfeedback, KPI's en ergernissen",
    "Stap 3: geen idee te gek, eerst kwantiteit",
    "Het convergeren met de PUGH-matrix"], 1,
   "De sessie moet gevoed worden met informatie, anders blijven ideeën los van het echte probleem. Convergeren hoort pas bij week 2.")
mc("pp1-m06", W, P, "Volgens de notities zit klantwaarde niet alleen in snelheid. Welk model koppelt de docent hieraan?",
   ["De KKT-driehoek", "SERVQUAL", "De belang-invloed-grid", "De PUGH-matrix"], 1,
   "Via SERVQUAL: klantwaarde zit ook in betrouwbaarheid, responsiviteit, deskundigheid en beleving. Verbeteren kan dus ook betrouwbaarder, veiliger of gastvrijer betekenen.")
mc("pp1-m07", W, P, "Waarom toets je een verbeterrichting aan de strategie van de opdrachtgever?",
   ["Omdat een voorstel dat de strategie ondersteunt draagvlak krijgt; wat ertegenin gaat haalt het zelden",
        "Omdat de strategie van de opdrachtgever bepaalt hoeveel budget er voor het project beschikbaar is",
        "Omdat de docent die toets als vast onderdeel van het portfolio en de eindbeoordeling vraagt",
        "Omdat je alleen met de strategie de criteria en weging van de PUGH-matrix kunt invullen"], 0,
   "Toets elke richting aan missie, visie en strategie. Een voorstel dat haaks op de strategie staat, haalt het zelden.")
mc("pp1-m08", W, P, "De cateraar maakt broodjes pas klaar als een vergadering definitief is bevestigd, en dan precies voor het aantal deelnemers. Welk Lean-principe is dit?",
   ["Just in Time", "Heijunka", "Poka-Yoke", "5S"], 0,
   "Just in Time: precies wat nodig is, op het juiste moment. Zo voorkom je overproductie en weggegooide broodjes.")
mc("pp1-m09", W, P, "Bij de receptie ligt elke ochtend een stapel post te wachten tot de interne bode om 14.00 uur langskomt. Welk principe wordt hier geschonden?",
   ["Flow: geen ophopingen tussen stappen", "Jidoka: geen fout doorgeven", "Standaardisatie: beste werkwijze vastleggen", "Gemba: naar de werkvloer gaan"], 0,
   "Flow betekent dat het werk doorstroomt zonder ophopingen. De stapel post is een wachtrij tussen twee stappen.")
mc("pp1-m10", W, P, "Na de eerste klacht over verkeerd geprinte bezoekersbadges stopt de receptie met uitgeven en zoekt eerst de oorzaak. Welk principe past hierbij?",
   ["Heijunka", "Stop de lijn", "Pull/Kanban", "Just in Time"], 1,
   "Stop de lijn: bij een probleem direct stilleggen en oplossen, zodat de fout niet verder wordt doorgegeven. Het hoort bij de kwaliteitspijler (Jidoka).")
mc("pp1-m11", W, P, "De technische dienst hangt in de werkplaats een schaduwbord op, labelt alle kasten en ruimt elke vrijdag op. Wat wil het team hiermee vooral voorkomen?",
   ["Fouten en variatie (mura)", "Overbelasting van de coördinator (muri)", "Te hoge inkoopprijzen", "Te weinig meldingen"], 0,
   "Dit is 5S: orde en netheid voorkomen fouten en variatie (mura). Iedereen vindt het gereedschap op dezelfde plek.")
mc("pp1-m12", W, P, "Bij welke pijler van het Toyota Production System hoort standaardisatie?",
   ["Snelheid (Just in Time)", "Kwaliteit (Jidoka)", "Mensen (respect)", "Kaizen (verbeteren)"], 1,
   "De kwaliteitspijler bevat Jidoka, stop de lijn, Poka-Yoke, standaardisatie en 5S. De snelheidspijler bevat JIT, flow, pull, Heijunka en TOC.")
mc("pp1-m13", W, P, "Een teamlid wil in elke ruimte een sensor ophangen, 'want dat is innovatief'. Wat is volgens de les de juiste toets voor zo'n FM Tech-idee?",
   ["Of de sensoren goedkoper en nieuwer zijn dan wat concurrenten in hun gebouwen gebruiken",
        "Of het klantwaarde toevoegt en bij de strategie past; technologie is een middel",
        "Of de ICT-afdeling er dit kwartaal tijd en budget voor heeft om het te installeren",
        "Of het idee in de Impact/Effort-matrix rechtsboven valt, bij hoge impact en hoge effort"], 1,
   "FM Tech komt bewust kort aan bod: technologie is een middel. Toets steeds of het klantwaarde toevoegt en bij de strategie past.")
mc("pp1-m14", W, P, "In het servicedeskvoorbeeld is de doorlooptijd 6,5 dag. Wat is daar de quick win?",
   ["Automatische routering van meldingen naar het juiste team",
        "Een digitaal meldingenbord voor het hele servicedeskteam",
        "Verplichte velden en een automatische ontvangstbevestiging",
        "Een tweede coördinator aannemen voor de piekmomenten"], 2,
   "Verplichte velden en een ontvangstbevestiging zijn snel geregeld en hebben direct effect. Routering en een meldingenbord zijn de structurele verbetering.")
mc("pp1-m15", W, P, "Een idee kost veel tijd en geld, maar heeft weinig effect op het probleem. In welk kwadrant van de Impact/Effort-matrix valt het?",
   ["Quick win", "Structurele verbetering", "Fill-in", "Niet doen"], 3,
   "Weinig impact en veel moeite: niet doen. Fill-ins zijn weinig impact en weinig moeite.")
mc("pp1-m16", W, P, "Waarom moet je de brainstorm met medewerkers en klanten tijdens de werkdag goed voorbereiden?",
   ["Omdat de opdrachtgever de vragen vooraf moet goedkeuren",
    "Omdat je maar één kans hebt om het juiste op te halen",
    "Omdat je de uitkomst meteen in de PUGH-matrix moet zetten",
    "Omdat de brainstorm meetelt voor je cijfer"], 1,
   "Medewerkers en klanten maken één keer tijd voor je. Bereid dus goed voor wat je wilt ophalen, zodat je longlist echte input bevat.")
mc("pp1-m17", W, P, "Waarom waarschuwt de docent voor een eenzijdige focus op kostenreductie bij het kiezen van verbeterrichtingen?",
   ["Omdat kosten in facilitair management bij het kiezen van verbeterrichtingen niet meetellen",
        "Omdat het elders schade kan doen, zoals aan tevredenheid, imago of productiviteit",
        "Omdat een opdrachtgever in FM liever investeert in groei dan dat er bespaard wordt",
        "Omdat kostenreductie niet bij de elf vormen van toegevoegde waarde hoort"], 1,
   "Kosten verlagen is één van de 11 toegevoegde waarden, maar wie alleen daarop stuurt, kan andere waarden beschadigen. Het criterium meervoudige toegevoegde waarde (20%) vraagt financiële én niet-financiële waarde.")
mc("pp1-m18", W, P, "Wat doe je in de Generate-fase in week 1, en wat pas in week 2?",
   ["Week 1 de beste oplossing kiezen, week 2 daar ideeën en varianten bij verzamelen",
        "Week 1 ideeën verzamelen zonder oordeel, week 2 kiezen en onderbouwen",
        "Week 1 de current state meten, week 2 met 5x Waarom de oorzaken zoeken",
        "Week 1 de implementatie plannen, week 2 met een FMEA de risico's scoren"], 1,
   "Eerst breed (divergeren), dan smal (convergeren). Zo voorkom je dat je te vroeg oordeelt.")

# ---------- open ----------
op("pp1-o1", W, P, "Leg uit wat divergeren en convergeren zijn, en waarom ze in het project bewust over twee weken zijn verdeeld.",
   "Divergeren is zoveel mogelijk ideeën verzamelen zonder te oordelen (week 1, longlist). Convergeren is kiezen en onderbouwen van één voorkeursoplossing (week 2, PUGH-matrix). Ze zijn gescheiden omdat te vroeg oordelen ('dat kan toch niet') de beste ideeën wegsnoeit. Wie meteen kiest, mist vaak de oplossing die echt waarde toevoegt; daarom is de Generate-fase ook aan DMAIC toegevoegd.",
   ["Divergeren juist uitgelegd", "Convergeren juist uitgelegd", "Reden van scheiden: te vroeg oordelen snoeit goede ideeën weg"])
op("pp1-o2", W, P, "Bezoekers van een gemeentehuis wachten soms twintig minuten bij de receptie om zich te registreren. Formuleer één interne vraag en één vraag vanuit klantwaarde over dit knelpunt. Noem daarnaast twee aspecten van klantwaarde (SERVQUAL) die hier naast snelheid een rol spelen.",
   "Intern: 'Hoe registreren wij bezoekers sneller?' Vanuit klantwaarde: 'Wat heeft een bezoeker eigenlijk nodig als hij binnenkomt?' (bijvoorbeeld weten waar hij moet zijn en zich welkom voelen). Andere aspecten: betrouwbaarheid (de afspraak staat klaar), responsiviteit (snel geholpen), deskundigheid (de receptionist weet de weg) en beleving (gastvrij ontvangen).",
   ["Interne vraag juist geformuleerd", "Klantwaardevraag juist geformuleerd vanuit de bezoeker", "Twee SERVQUAL-aspecten passend bij de situatie"])
op("pp1-o3", W, P, "Leg de twee pijlers van het Toyota Production System uit. Noem bij elke pijler twee principes en geef bij elke pijler een FM-voorbeeld.",
   "Snelheid (Just in Time): laat het werk stromen. Principes: Just in Time, flow, pull/Kanban, Heijunka, bottleneck/TOC. FM-voorbeeld: vergaderzalen gespreid klaarzetten of de drukste servicebalie eerst aanpakken. Kwaliteit (Jidoka): bouw kwaliteit in bij de bron, geef geen fout door. Principes: Jidoka, stop de lijn, Poka-Yoke, standaardisatie, 5S. FM-voorbeeld: verplichte velden op een meldformulier.",
   ["Pijler snelheid juist uitgelegd met twee principes", "FM-voorbeeld bij snelheid", "Pijler kwaliteit juist uitgelegd met twee principes", "FM-voorbeeld bij kwaliteit"])
op("pp1-o4", W, P, "Een team stelt voor om storingsmeldingen voortaan via één digitaal formulier te laten lopen. Laat met drie van de 11 facilitaire toegevoegde waarden zien wat dit oplevert, waarvan minstens twee niet-financieel.",
   "Voorbeelden: productiviteit (medewerkers verliezen minder tijd door storingen die lang blijven liggen), tevredenheid (melders weten dat hun melding is opgepakt), risico's beheren (geen meldingen meer kwijt, bijvoorbeeld bij veiligheidsgebreken), kosten verlagen (minder dubbel werk, overtypen), imago (een organisatie die snel reageert). Een sterk antwoord maakt de impact concreet en weegt financieel en niet-financieel tegen elkaar af.",
   ["Eerste toegevoegde waarde juist en concreet", "Tweede toegevoegde waarde juist en concreet", "Derde toegevoegde waarde juist, met minstens twee niet-financieel"])
op("pp1-o5", W, P, "Waarom gaat een verbeterteam naar de Gemba? Leg uit wat het oplevert voor je analyse én voor het draagvlak van je advies.",
   "De Gemba is de werkvloer, waar het werk echt gebeurt. Daar zie je de kansen, en de mensen die het werk doen weten vaak precies wat er misgaat (vraag de receptionist, schoonmaker of technicus naar hun grootste ergernis). Voor het draagvlak: mensen die gehoord worden en hun ideeën terugzien, staan eerder achter de verandering. Volgens de notities hangt het al dan niet landen van een advies af van cultuur, weerstand en draagvlak, niet alleen van hoe slim de oplossing is.",
   ["Gemba juist uitgelegd", "Opbrengst voor de analyse", "Opbrengst voor draagvlak, met koppeling aan cultuur of betrokkenheid"])
op("pp1-o6", W, P, "Je organiseert een brainstorm over het afvalscheidingsproces op een hogeschool. Werk de drie stappen van een goede brainstorm uit voor deze situatie.",
   "Stap 1, diverse blik: schoonmakers, iemand van de kantine, een student, een docent en de facilitair coördinator. Stap 2, de sessie voeden: cijfers over restafval en scheidingspercentage, klachten of opmerkingen van gebruikers, ergernissen van schoonmakers (bijvoorbeeld volle bakken op vaste plekken). Stap 3, geen idee te gek: eerst zoveel mogelijk ideeën, voortbouwen op elkaar en nog niet oordelen; het doel is een longlist van minstens tien ideeën.",
   ["Stap 1 concreet ingevuld", "Stap 2 concreet ingevuld met data of ergernissen", "Stap 3: kwantiteit, niet oordelen, voortbouwen"])

# ---------- casus ----------
cs("pp1-c1", W, P, "Servicedesk Hogeschool Rijnstad",
   "Bij de facilitaire servicedesk van Hogeschool Rijnstad (fictief) komen meldingen binnen via mail, telefoon en de balie. Alle meldingen gaan langs één coördinator, die ze verdeelt over de technici. De gemiddelde doorlooptijd is 5 werkdagen; studenten en docenten verwachten binnen één dag te horen dat hun melding is opgepakt. Een derde van de meldingen is onvolledig ('lamp kapot'), zodat de technicus eerst moet uitzoeken waar het om gaat. Technici pakken meldingen op in de volgorde die de coördinator die ochtend kiest.",
   [("Welke drie Lean-principes kun je inzetten om dit proces te verbeteren? Koppel elk principe aan een concreet knelpunt uit de casus.",
     "Bottleneck/TOC: de coördinator is de zwakste schakel en bepaalt de output; die eerst ontlasten, bijvoorbeeld met automatische routering. Poka-Yoke: verplichte velden (locatie, ruimte, soort storing) tegen onvolledige meldingen. Pull/Kanban: technici pakken zelf de volgende melding van een bord met nieuw, opgepakt, opgelost, in plaats van wachten op de verdeling. Flow of FIFO zijn ook goed als ze aan een knelpunt gekoppeld zijn.",
     ["Eerste principe juist en gekoppeld aan een knelpunt", "Tweede principe juist en gekoppeld", "Derde principe juist en gekoppeld"]),
    ("Plaats vier verbeterideeën voor deze servicedesk in de Impact/Effort-matrix en kies welke quick win en welke structurele verbetering je adviseert. Waarom allebei?",
     "Bijvoorbeeld: verplichte velden en een automatische ontvangstbevestiging (quick win: veel impact, weinig moeite), automatische routering naar technici via het FMIS (structureel: veel impact, meer moeite), een poster bij de balie over hoe je meldt (fill-in), een eigen app laten bouwen (niet doen: veel moeite, weinig extra impact). Allebei: de quick win geeft momentum en draagvlak, maar bestrijdt vooral het symptoom; de structurele verbetering pakt de oorzaak (de bottleneck) aan.",
     ["Vier ideeën logisch in de kwadranten geplaatst", "Quick win en structurele verbetering gekozen", "Uitleg: momentum/draagvlak tegenover oorzaak aanpakken"])])
cs("pp1-c2", W, P, "Patiëntmaaltijden in het Maasziekenhuis",
   "In het Maasziekenhuis (fictief) bereidt de keuken alle patiëntmaaltijden tussen 11.00 en 12.00 uur, omdat alle afdelingen om 12.00 uur willen eten. Op dat uur is de keuken overbelast en gaan er vaak fouten in de dieetmaaltijden. Er wordt elke dag zo'n 15% van de maaltijden weggegooid, omdat de keuken vooraf een vast aantal maakt. Het hoofd voeding wil de verspilling aanpakken en stelt voor 'gewoon 15% minder te koken en het menu te versoberen'.",
   [("Beoordeel het voorstel van het hoofd voeding met de 11 facilitaire toegevoegde waarden. Noem minstens twee waarden die onder druk komen.",
     "Het voorstel kijkt vooral naar kosten verlagen. Onder druk komen bijvoorbeeld healing environment (eten draagt bij aan herstel), tevredenheid (patiënten), risico's beheren (te weinig maaltijden of verkeerde dieetmaaltijden) en imago. De docent waarschuwt voor een eenzijdige focus op kostenreductie. Beter is de oorzaak van de verspilling aanpakken (vast aantal vooraf, piekbelasting) dan alleen minder koken.",
     ["Herkent eenzijdige focus op kostenreductie", "Twee andere toegevoegde waarden die onder druk komen, met uitleg", "Alternatief: oorzaak van verspilling aanpakken"]),
    ("Welke twee Lean-principes uit de snelheidspijler passen bij dit probleem? Werk beide uit voor de keuken.",
     "Heijunka: de werkdruk spreiden, bijvoorbeeld afdelingen in twee of drie tijdsloten laten eten, zodat de piek tussen 11.00 en 12.00 verdwijnt en er minder fouten zijn. Just in Time / Pull: niet een vast aantal vooraf maken, maar koken op basis van de bestellingen van patiënten op de dag zelf (signaal), zodat er minder wordt weggegooid.",
     ["Heijunka juist toegepast op de piek", "JIT of pull juist toegepast op de verspilling", "Koppeling aan de gevolgen (minder fouten, minder weggooien)"])])
cs("pp1-c3", W, P, "Flexplekken bij Waterschap Veluwerand",
   "Waterschap Veluwerand (fictief) werkt met flexplekken. Medewerkers klagen dat ze 's ochtends lang zoeken naar een vrije werkplek en dat sommige plekken de hele dag 'bezet' zijn door een jas. Missie: 'Wij zorgen voor schoon en veilig water voor iedereen in de regio.' Strategie voor de komende jaren: duurzaam werken en kosten van huisvesting omlaag. Een teamlid stelt voor om 400 bezettingssensoren met een app aan te schaffen.",
   [("Toets het sensorvoorstel aan de les over FM Tech en aan missie, visie en strategie. Wat zou je het team adviseren voordat het dit idee in de longlist hoger zet?",
     "Technologie is een middel, geen doel. Eerst bepalen welke klantwaarde het oplevert: weten waar een vrije plek is en minder zoeken. Het past bij de strategie als het ook bezettingsdata oplevert om vierkante meters af te stoten (kosten huisvesting omlaag, duurzaamheid). Advies: eerst klantwaarde en strategische bijdrage expliciet maken en goedkopere alternatieven meenemen (bijvoorbeeld een clean-desk-afspraak tegen 'jassenclaims'), en het idee daarna eerlijk in de Impact/Effort-matrix zetten.",
     ["Technologie als middel, geen doel", "Koppeling aan strategie (huisvestingskosten, duurzaamheid) of missie", "Concreet advies, bijvoorbeeld klantwaarde eerst of alternatieven meenemen"]),
    ("Formuleer drie ontwerpeisen waaraan elke oplossing voor dit probleem moet voldoen. Leid ze af van klantwaarde en strategie.",
     "Voorbeelden: (1) een medewerker vindt binnen 5 minuten een vrije werkplek (klantwaarde, snelheid); (2) de oplossing verhoogt het aantal benodigde werkplekken niet (strategie: kosten huisvesting); (3) de oplossing kost geen extra energie of materiaal, of draagt bij aan duurzaam werken (strategie); (4) de oplossing is eenvoudig te gebruiken zonder training. Goede ontwerpeisen zijn concreet en toetsbaar.",
     ["Drie ontwerpeisen geformuleerd", "Afgeleid van klantwaarde én strategie", "Concreet en toetsbaar geformuleerd"])])
