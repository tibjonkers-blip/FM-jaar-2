# Eindtoets Praktijkproject BM: één organisatie door het hele verbetertraject (week 0 = versie E).
W = 0
P = "Verbeterproject"
PR = "Presentatie"

CASUS = ("Ziekenhuis Maaswaal (fictief) laat patiënten hun maaltijd kiezen op een papieren lijst. "
         "De verpleging vult die lijst 's ochtends om 9.00 uur in voor lunch en diner; om 10.30 uur haalt een "
         "voedingsassistent de lijsten op en typt een keukenmedewerker ze over in het keukensysteem. Wijzigingen "
         "(nieuwe opname, ontslag, nuchter voor een operatie) belt de verpleging door. Uit de metingen van periode 1: "
         "18% van de maaltijden komt ongeopend terug, patiënten klagen over lauwe maaltijden en de verpleging "
         "besteedt per afdeling ruim een uur per dag aan bestellijsten en telefoontjes.")

# ---------- MC ----------
mc("ppe-m01", W, P, "Ziekenhuis Maaswaal. Het team houdt een sessie met verpleging, keuken en twee patiënten en verzamelt 25 ideeën, zonder er al iets van af te schieten. In welke fase en werkwijze zit het team?",
   ["Analyze: oorzaken zoeken met 5x Waarom", "Generate: divergeren, eerst breed", "Generate: convergeren, kiezen en onderbouwen", "Improve: draagvlak bouwen met Kotter-light"], 1,
   "Week 1 is Generate, divergeren: zoveel mogelijk ideeën, nog niet oordelen. Te vroeg oordelen snoeit de beste ideeën weg. In week 2 kies je (convergeren).")
mc("ppe-m02", W, P, "Ziekenhuis Maaswaal. Patiënten die een warme maaltijd krijgen die bij hun wens past, eten beter en herstellen sneller. Bij welke facilitaire toegevoegde waarde past dit het best?",
   ["Flexibiliteit", "Healing environment", "Waardestijging", "Innovatie"], 1,
   "Healing environment is een van de 11 facilitaire toegevoegde waarden. Daarnaast spelen hier duurzaamheid (minder verspilling) en kosten mee: meervoudige toegevoegde waarde.")
mc("ppe-m03", W, P, "Ziekenhuis Maaswaal. Een idee is dat de keuken pas kookt en portioneert op basis van de definitieve bestellingen van die dag. Bij welk Lean-principe past dit?",
   ["Jidoka: stop de lijn bij een fout", "Pull: start werk pas op een signaal", "Heijunka: spreid de werkdruk", "5S: orde en netheid"], 1,
   "Pull (pijler Just in Time): je produceert wat nodig is, op het juiste moment, op een signaal van de klant. Dat pakt de overproductie aan.")
mc("ppe-m04", W, P, "Ziekenhuis Maaswaal. Op de bestel-tablet kan een maaltijd pas worden verstuurd als er een dieetcode is gekozen. Hoe heet dit principe?",
   ["Poka-Yoke", "Heijunka", "Kanban", "Gemba"], 0,
   "Poka-Yoke: ontwerp het proces zo dat de fout niet gemaakt kán worden. Het hoort bij de pijler kwaliteit (Jidoka).")
mc("ppe-m05", W, P, "Ziekenhuis Maaswaal. Hoe classificeer je de stap 'keukenmedewerker typt de papieren lijsten over in het keukensysteem'?",
   ["VA: de patiënt heeft er direct baat bij", "BNVA: geen klantwaarde, wel noodzakelijk", "NVA: pure verspilling, elimineren", "VA, mits de medewerker zorgvuldig typt"], 2,
   "Overtypen voegt niets toe voor de patiënt en is niet nodig als de bestelling digitaal binnenkomt. NVA elimineer je. Een dieetcontrole door de diëtist zou BNVA zijn: geen klantwaarde, wel noodzakelijk.")
mc("ppe-m06", W, P, "Ziekenhuis Maaswaal, PUGH-matrix. Criteria en gewicht: verspilling 5, werkdruk verpleging 4, invoeringskosten 3, patiënttevredenheid 4. Optie A (bestellen aan bed met tablet) scoort +2, +1, −2, +2. Wat is het gewogen totaal van optie A?",
   ["10", "16", "22", "28"], 1,
   "(2 × 5) + (1 × 4) + (−2 × 3) + (2 × 4) = 10 + 4 − 6 + 8 = 16. De baseline (huidige situatie) staat op 0.")
mc("ppe-m07", W, P, "Ziekenhuis Maaswaal. Het keukensysteem kan niet koppelen met tablets, en op de afdelingen is het gewoonte om alles op papier te doen. Op welke dimensie scoort de tabletoplossing dan zwak?",
   ["Haalbaarheid via de 80/20-regel", "Impact volgens de KKT-driehoek", "Aansluiting op de context", "Geen, dit zijn uitvoeringsdetails"], 2,
   "Aansluiting op de context: past het bij cultuur, systemen en de bedoeling van de organisatie? Volgens de notities de toets die studenten het vaakst vergeten.")
mc("ppe-m08", W, P, "Ziekenhuis Maaswaal. De cliëntenraad heeft veel belang bij de maaltijdservice, maar weinig formele invloed op de keuze. Wat is de strategie volgens de belang-invloed-grid?",
   ["Monitoren", "Informeren", "Tevreden houden", "Nauw betrekken"], 1,
   "Veel belang, weinig invloed: informeren. Veel belang en veel invloed (bijvoorbeeld het hoofd voedingsdienst): nauw betrekken.")
mc("ppe-m09", W, P, "Ziekenhuis Maaswaal. Verpleegkundigen zeggen: 'Bestellen aan bed kost ons de eerste weken juist meer tijd.' Welke aanpak van weerstand past hierbij?",
   ["Ruimte geven", "Tijd vrijmaken", "Waardering voor het verleden", "Een duidelijke visie geven"], 1,
   "Oorzaak 'het kost (eerst) meer werk' koppel je aan de aanpak 'tijd vrijmaken'. Weerstand is geen onwil, maar een voorspelbare reactie.")
mc("ppe-m10", W, P, "Ziekenhuis Maaswaal, FMEA-light. Risico: 'verkeerde dieetcode gekozen, patiënt krijgt een maaltijd met een allergeen'. Ernst 5, Kans 2, Detectie 4. Wat is het RPN?",
   ["11", "20", "40", "50"], 2,
   "5 × 2 × 4 = 40. Een zeldzame maar ernstige fout die moeilijk te ontdekken is, kan hoger eindigen dan een fout die vaak voorkomt maar direct opvalt.")
mc("ppe-m11", W, P, "Ziekenhuis Maaswaal. De leverancier wil alle twaalf afdelingen in één weekend omzetten. Hoe heet die strategie en wat is het grootste bezwaar?",
   ["Gefaseerd; de uitrol duurt dan te lang",
        "Big-bang; het hoogste risico voor de zorg",
        "Schaduwdraaien; het levert dubbel werk op",
        "Pilot; je verzamelt te weinig data"], 1,
   "Big-bang is snel, maar heeft het hoogste risico. In een ziekenhuis weegt het risico voor de operationele dienstverlening zwaar; een pilot op één afdeling en daarna gefaseerd ligt meer voor de hand.")
mc("ppe-m12", W, P, "Ziekenhuis Maaswaal. Wie is na het vertrek van het studentteam het meest logisch de proceseigenaar van de maaltijdbestelling?",
   ["De manager zorg, die als sponsor middelen vrijmaakte", "Het hoofd voedingsdienst, verantwoordelijk voor het proces", "De diëtist, die de dieetcodes heeft bepaald", "De docent, die het project heeft begeleid"], 1,
   "De proceseigenaar is de lijnmanager die verantwoordelijk is voor het proces en het mandaat heeft (Lean Back). De sponsor maakt mensen en middelen vrij, maar draagt het proces niet dagelijks.")

# ---------- open ----------
op("ppe-o1", W, P, CASUS + " Kies uit deze situatie één quick win en één structurele verbetering. Leg met de Impact/Effort-matrix uit waarom je allebei kiest.",
   "Quick win (hoge impact, lage moeite): bijvoorbeeld een vaste afmeldregel bij ontslag of nuchter via één telefoonnummer of een korte checklist, of de bestellijst later op de ochtend laten invullen zodat er minder wijzigingen zijn. Structureel (hoge impact, hoge moeite): digitaal bestellen aan bed dat direct in het keukensysteem landt, met koken op bestelling (pull). Quick wins geven momentum en draagvlak, maar lossen vaak alleen een symptoom op; de structurele verbetering pakt de oorzaak aan (overtypen, te vroeg bestellen) maar kost meer tijd en geld. Een advies met alleen symptoombestrijding is zwak.",
   ["Passende quick win", "Passende structurele verbetering", "Uitleg: momentum en draagvlak versus oorzaak aanpakken"])
op("ppe-o2", W, P, "Ziekenhuis Maaswaal. Het team kiest voor bestellen aan bed met een tablet. Onderbouw de waarde van deze oplossing voor de drie perspectieven uit week 2, en laat zien dat er sprake is van meervoudige (financiële én niet-financiële) toegevoegde waarde.",
   "Opdrachtgever: minder verspilling (18% retour) betekent lagere kosten en past bij duurzaamheidsdoelen en imago; draagt bij aan KPI's. Gebruiker (patiënt): kiest dichter bij het moment zelf, krijgt wat hij of zij wil, warmer en beter passend bij het dieet, wat het herstel ondersteunt (healing environment). Proces: geen overtypen (NVA weg), minder telefoontjes, minder wijzigingen, kortere doorlooptijd en minder werkdruk voor de verpleging. Meervoudig: financieel (minder weggegooid voedsel, minder uren) én niet-financieel (tevredenheid, duurzaamheid, healing environment). Geen eenzijdige focus op kosten.",
   ["Opdrachtgever-perspectief concreet", "Gebruiker- en procesperspectief concreet", "Financiële én niet-financiële waarde benoemd"])
op("ppe-o3", W, P, "Ziekenhuis Maaswaal. Van de verpleegkundigen is ongeveer een vijfde enthousiast, een vijfde fel tegen en de rest twijfelt. Stel met de 20-60-20-verdeling en Kotter-light een aanpak op om draagvlak te bouwen.",
   "20-60-20: stop niet al je energie in de tegenstanders; laat de voorstanders zichtbaar succes boeken, dan kiest de middengroep (60%) de kant van de sterkste groep. Kotter-light: 1 Urgentie: laat de eigen cijfers zien (18% retour, ruim een uur per dag per afdeling aan lijsten). 2 Coalitie: een zichtbare sponsor (manager zorg) plus enkele invloedrijke verpleegkundigen als ambassadeurs. 3 Communicatie: vaak, consistent en in twee richtingen, zorgen serieus nemen (bijvoorbeeld de extra tijd in het begin). 4 Betrokkenheid: verpleegkundigen een rol geven in het testen en vier een zichtbare quick win op de pilotafdeling.",
   ["20-60-20 juist toegepast", "Minstens drie Kotter-light-stappen concreet", "Alle vier de stappen concreet voor deze casus"])
op("ppe-o4", W, PR, "Ziekenhuis Maaswaal. Je presenteert je advies aan de raad van bestuur. Zet de kern van je presentatie in de PROA-structuur, en benoem per blok de projectfase(n) en wat je laat zien.",
   "Probleem (Define en Measure): maaltijdbestelling via papieren lijsten leidt tot verspilling en ontevredenheid. Risico (Measure): de omvang, 18% van de maaltijden ongeopend retour, lauwe maaltijden, ruim een uur verpleegtijd per afdeling per dag; eventueel in euro's. Oorzaak (Analyze): te vroeg bestellen, overtypen en wijzigingen per telefoon, dus geen directe koppeling tussen vraag en productie. Advies (Generate, Improve, Control): mogelijkheden en keuze (PUGH, bestellen aan bed met pull), implementatie (pilot op één afdeling, daarna gefaseerd, RACI, FMEA-maatregelen) en grip op resultaten (KPI verspilling met norm en ingrijpgrens, proceseigenaar hoofd voedingsdienst). Visueel: één boodschap per slide, het proces tekenen in plaats van vertellen, en denken vanuit wat de raad nodig heeft om ja te zeggen.",
   ["Probleem en Risico juist gescheiden met cijfers", "Oorzaak bij Analyze", "Advies met keuze, implementatie én borging", "Afgestemd op de beslisser of visueel uitgewerkt"])

# ---------- casus ----------
cs("ppe-c1", W, P, "Ziekenhuis Maaswaal, deel 1: van analyse naar keuze en pilot", CASUS + " Het team wil van de analyse naar een gekozen ontwerp en een pilot op de afdeling Orthopedie.",
   [("Deel de volgende stappen in als VA, BNVA of NVA en zeg wat je ermee doet in de future state: (a) lijsten ophalen bij de afdeling, (b) dieetcontrole door de diëtist, (c) de maaltijd bereiden, (d) wijzigingen telefonisch doorgeven en noteren.",
     "(a) NVA: transport van informatie, elimineren door digitaal bestellen. (b) BNVA: geen directe klantwaarde, wel noodzakelijk voor veiligheid, minimaliseren (bijvoorbeeld automatische controle op dieetcode, de diëtist alleen bij afwijkingen). (c) VA: hier wil de patiënt voor betalen, behouden en versterken. (d) NVA: herstelwerk door te vroeg bestellen, elimineren door later en digitaal te bestellen.",
     ["Minstens drie stappen juist ingedeeld", "Alle vier juist met de bijbehorende ontwerpregel"]),
    ("Het team scoorde de opties eerst en bepaalde daarna de gewichten, 'zodat de beste optie er goed uitkomt'. Wat is hier mis, en hoe hoort het volgens de vijf stappen van de PUGH-matrix?",
     "De gewichten moet je vóór het scoren afspreken, anders stuurt de weging stiekem het antwoord en is de keuze niet navolgbaar. Volgens de vijf stappen: representatieve groep (team plus stakeholders zoals verpleging en keuken), maximaal zes vitale criteria met gewicht, baseline is de huidige situatie met score 0, alternatieven scoren van −2 tot +2 ten opzichte van de baseline, score maal gewicht optellen. De matrix is een hulpmiddel, geen rechter; de waarde zit in de transparantie en het gesprek.",
     ["Fout benoemd: weging na scoren stuurt de uitkomst", "Minstens vier van de vijf stappen juist"]),
    ("Formuleer twee SMART-succescriteria voor de pilot en noem drie randvoorwaarden voor een goede pilot op Orthopedie.",
     "Succescriteria, bijvoorbeeld: 'Binnen zes weken na de start van de pilot op Orthopedie komt maximaal 8% van de maaltijden ongeopend terug (nu 18%).' 'Na zes weken besteedt de verpleging op Orthopedie gemiddeld maximaal 20 minuten per dag aan maaltijdbestellingen.' Randvoorwaarden: een plan (doel, duur, betrokkenen), een datacollectieplan (wie meet retouren en tijd, hoe), communicatie naar verpleging en patiënten, training van verpleging en voedingsassistenten, uitvoering volgens plan en evaluatie tegen de doelen vóór verdere uitrol.",
     ["Twee criteria die echt SMART zijn", "Drie passende randvoorwaarden"])])
cs("ppe-c2", W, P, "Ziekenhuis Maaswaal, deel 2: van invoering naar overdracht",
   "De pilot op Orthopedie is geslaagd: het retourpercentage daalde van 18% naar 7%. Het ziekenhuis wil gefaseerd uitrollen naar de andere elf afdelingen. Het hoofd voedingsdienst wordt proceseigenaar. Uit de FMEA-light kwamen twee toprisico's: (1) de wifi op sommige afdelingen valt weg, zodat bestellingen niet aankomen (E4, K3, D4); (2) een tablet is leeg bij de bestelronde (E2, K4, D1). Het studentteam vertrekt over drie weken; de aanschaf van extra tablets is nog niet goedgekeurd.",
   [("Bereken het RPN van beide risico's en bedenk voor het hoogste risico een beheersmaatregel met een verantwoordelijke. Welke score daalt door je maatregel?",
     "Risico 1: 4 × 3 × 4 = 48. Risico 2: 2 × 4 × 1 = 8. Risico 1 heeft prioriteit. Maatregel: een automatische ontvangstbevestiging en een melding aan de keuken als een afdeling op een vast tijdstip nog niets heeft besteld; de detectiescore daalt. Of: de wifi op die afdelingen laten verbeteren door ICT, dan daalt de kans. Plus een OCAP: bij uitval valt de afdeling terug op de papieren lijst. Verantwoordelijke: bijvoorbeeld de applicatiebeheerder of ICT.",
     ["Beide RPN's juist", "Maatregel met verantwoordelijke", "Juist aangegeven welke score daalt"]),
    ("Vul de borgingskaart in voor deze verbetering: afbakening, proceseigenaar, twee KPI's met norm, hoe geborgd, losse eindjes.",
     "Afbakening: van de keuze van de patiënt op de tablet tot de geleverde maaltijd; leverancier en klant zijn patiënt en afdeling, de keuken levert. Proceseigenaar: hoofd voedingsdienst, die het weet en mandaat heeft. KPI 1: percentage ongeopend geretourneerde maaltijden, norm maximaal 8%, ingrijpen boven 10%. KPI 2: percentage bestellingen dat vóór de deadline binnen is, norm minstens 95%. Hoe geborgd: SOP of één-punt-les voor verpleging en voedingsassistenten, KPI's maandelijks in het overleg van de voedingsdienst en op een visueel bord. Losse eindjes: goedkeuring en aanschaf van extra tablets, wifi op de afdelingen.",
     ["Afbakening en proceseigenaar juist", "Twee KPI's met concreet getal en norm", "Borging zichtbaar gemaakt", "Losse eindjes benoemd"]),
    ("Het team stelt voor om in de laatste week het dossier te mailen en meteen afscheid te nemen. Wat adviseer je op basis van de gouden regel en de Tollgate, en welke concrete les zou dit team kunnen vastleggen?",
     "Niet doen: draag pas over als de proceseigenaar het echt kan dragen, en daarna pas ontbind je het team. Plan een Tollgate met de manager zorg (sponsor), het hoofd voedingsdienst, een vertegenwoordiger van de verpleging en de keuken: storyboard, wat ging goed en fout, toetsen aan de succescriteria (7% retour), formeel overdragen, losse eindjes (tablets) expliciet benoemen. Daarna verankeren en archiveren. Concrete les, bijvoorbeeld: 'Test de wifi op elke afdeling vóórdat de afdeling overgaat, en neem ICT vanaf de pilot op in de RACI.'",
     ["Mailen afgewezen met de gouden regel", "Tollgate met deelnemers en agenda", "Concrete les ('wat doe je voortaan')"])])
