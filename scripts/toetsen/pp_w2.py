W = 2
P = "Verbeterproject"

# ---------- MC ----------
mc("pp2-m01", W, P, "Wat is een future state in Lean?",
   ["Een geordende lijst met alle verbeterideeën die uit de brainstorm zijn gekomen",
        "Een samenhangend beeld van het ideale proces, met alleen waardetoevoegende stappen",
        "De huidige situatie van het proces, maar dan met actuele meetgegevens erbij",
        "Het implementatieplan met mijlpalen, middelen en verantwoordelijken per stap"], 1,
   "De future state is het beeld van het ideale proces zonder verspilling. Het is geen losse verzameling verbeteringen, maar een samenhangend beeld van hoe een melding of aanvraag straks doorstroomt.")
mc("pp2-m02", W, P, "Waarom ontwerp je de future state eerst vanuit het ideaal en redeneer je pas daarna terug naar wat haalbaar is?",
   ["Omdat de opdrachtgever bij een verbeterproject meestal de meest ambitieuze oplossing wil zien",
        "Om niet te blijven hangen in kleine aanpassingen aan een proces dat in de kern niet deugt",
        "Omdat haalbaarheid in Lean pas meetelt als de pilot is afgerond en geëvalueerd",
        "Omdat je anders de criteria en de weging van de PUGH-matrix niet kunt invullen"], 1,
   "Wie begint bij het bestaande proces, schaaft vaak alleen wat bij. Door eerst de 'droom' te ontwerpen, zie je wat er in de kern anders kan.")
mc("pp2-m03", W, P, "Een storingsmelding is vijf dagen onderweg, terwijl het herstel een uur kost. Waar zit volgens de les de winst in de future state?",
   ["In harder werken van de monteurs",
    "In het wegnemen van wachten en overdragen",
    "In het aannemen van extra monteurs",
    "In een duurder FMIS"], 1,
   "Het herstel zelf kost maar een uur; de rest is wachten en overdragen. Die verspilling haal je weg.")
mc("pp2-m04", W, P, "Een stap voegt volgens de notities pas echt waarde toe als aan drie voorwaarden is voldaan. Welke van deze vier is géén van die voorwaarden?",
   ["De klant wil ervoor betalen", "De stap verandert het product of de dienst volgens de wens van de klant", "Het gaat in één keer goed", "De stap is wettelijk verplicht"], 3,
   "Een wettelijk verplichte stap zonder klantwaarde is BNVA: noodzakelijk, maar niet waardetoevoegend. Die minimaliseer je.")
mc("pp2-m05", W, P, "Op maandag komen bij de servicedesk 40 meldingen binnen, op vrijdag maar 5. Welke vorm van verspilling is dit?",
   ["Muda", "Mura", "Muri", "Poka-Yoke"], 1,
   "Mura is onnodige variatie of ongelijkmatigheid. Muri is overbelasting; dat kan een gevolg zijn van de maandagpiek.")
mc("pp2-m06", W, P, "Eén technicus moet alle spoedklussen in het weekend oppakken en raakt uitgeput. Welke vorm van verspilling is dit?",
   ["Mura", "Muri", "NVA", "BNVA"], 1,
   "Muri is overbelasting van mensen of middelen. Let er in je ontwerp op dat je die niet vergroot.")
mc("pp2-m07", W, P, "Welke vorm van een toekomstbeeld laat de volledige waardestroom zien van begin tot eind, met tijden en informatiestromen?",
   ["Future-state map", "Service blueprint", "Verbeterde flow", "Impact/Effort-matrix"], 0,
   "De future-state map is de meest complete vorm. De service blueprint scheidt frontstage en backstage; de verbeterde flow is pragmatisch.")
mc("pp2-m08", W, P, "Je wilt de opdrachtgever snel laten zien welke stappen in de swimlane zijn geschrapt, samengevoegd of verplaatst. Welke vorm past?",
   ["Service blueprint", "Verbeterde flow", "Future-state map", "RACI"], 1,
   "De verbeterde flow is een aangepaste flowchart of swimlane. Pragmatisch, en goed om te tonen wat er is veranderd.")
mc("pp2-m09", W, P, "Een servicedesk is 480 minuten per dag open en krijgt gemiddeld 60 meldingen per dag. Wat is de takttijd (gangbare definitie)?",
   ["4 minuten", "8 minuten", "60 minuten", "480 minuten"], 1,
   "Takttijd = beschikbare tijd / klantvraag = 480 / 60 = 8 minuten. Elke 8 minuten vraagt de klant om een nieuwe melding. Let op: de slide noemt takttijd zonder uitleg; dit is de gangbare invulling.")
mc("pp2-m10", W, P, "Wat betekent FIFO in de future state van het storingsproces?",
   ["Eerst de makkelijkste meldingen oppakken",
    "Meldingen oppakken in volgorde van binnenkomst",
    "De meldingen van de directie eerst",
    "Alle meldingen van één dag in één keer afhandelen"], 1,
   "FIFO is first in, first out. Zo blijft geen melding eindeloos liggen.")
mc("pp2-m11", W, P, "De wet van de concentratie (80/20) helpt bij de dimensie haalbaarheid. Wat betekent dat voor je keuze?",
   ["Je verbetert 80% van alle processtappen en laat de rest voorlopig zoals het is",
        "Je pakt de vitale 20% aan die vaak 80% van de problemen veroorzaakt",
        "Je besteedt 80% van het projectbudget aan de pilot en 20% aan de uitrol",
        "Je kiest de oplossing waar minstens 80% van de medewerkers voor stemt"], 1,
   "Vaak veroorzaakt 20% van de activiteiten 80% van de problemen. Door je daarop te richten, blijft je oplossing haalbaar binnen tijd en middelen.")
mc("pp2-m12", W, P, "Wat leert de KKT- of duivelsdriehoek je bij de dimensie impact?",
   ["Dat kwaliteit in FM altijd voorgaat op kosten en tijd",
        "Dat je zelden kwaliteit, kosten en tijd tegelijk verbetert",
        "Dat kosten de enige harde maatstaf zijn voor impact",
        "Dat tijd in FM-processen nauwelijks meetelt bij impact"], 1,
   "Kwaliteit, kosten en tijd beïnvloeden elkaar. Verbeter je de een, dan kost dat vaak iets bij een ander.")
mc("pp2-m13", W, P, "Waarom is binnen Lean een matrix nodig om tussen oplossingen te kiezen, in plaats van op gevoel?",
   ["Omdat een matrix objectief altijd de goedkoopste en snelste oplossing naar boven haalt",
        "Omdat consensus een kernwaarde is: de keuze moet gedragen en navolgbaar zijn",
        "Omdat de docent de keuze anders niet kan beoordelen in het portfolio",
        "Omdat gevoel en ervaring in een Lean-verbeterproject geen enkele rol mogen spelen"], 1,
   "Kies je op gevoel of op de hardste stem, dan volgt discussie en verlies je draagvlak. De waarde zit in de transparantie en het gesprek.")
mc("pp2-m14", W, P, "Hoeveel criteria gebruik je maximaal in de PUGH-matrix?",
   ["Drie", "Vier", "Zes", "Tien"], 2,
   "Maximaal zes vitale criteria, waarbij je de zwaarste een hoger gewicht geeft.")
mc("pp2-m15", W, P, "Optie D scoort: doorlooptijd +1 (weging 4), kosten +2 (weging 3), gebruiksgemak −1 (weging 5). Wat is het gewogen totaal?",
   ["+2", "+5", "+15", "+17"], 1,
   "(1 × 4) + (2 × 3) + (−1 × 5) = 4 + 6 − 5 = 5.")
mc("pp2-m16", W, P, "Een optie krijgt in de PUGH-matrix een gewogen totaal van −1. Wat betekent dat?",
   ["De optie is ongeveer even goed als de beste optie",
    "De optie scoort slechter dan de huidige situatie",
    "Er is een rekenfout, want totalen kunnen niet negatief zijn",
    "De optie moet eerst als pilot worden getest"], 1,
   "De baseline (huidige situatie) staat op 0. Een negatief totaal betekent slechter dan nu. Dat zag je ook bij optie C in het voorbeeld uit de les.")
mc("pp2-m17", W, P, "Tijdens de werkdag vullen jullie de PUGH-matrix in met medewerkers. Jullie team komt uiteindelijk tot een andere keuze dan de medewerkers. Wat zegt de les daarover?",
   ["Dat mag niet: de keuze van de medewerkers is bindend",
    "Dat mag, het is jullie advies, maar je moet het onderbouwen",
    "Dan moet de opdrachtgever een nieuwe matrix laten invullen",
    "Dan stem je opnieuw tot er een meerderheid is"], 1,
   "Uiteindelijk is het jullie advies. Afwijken mag, maar onderbouw waarom.")
mc("pp2-m18", W, P, "Een technisch briljant ontwerp vraagt dat alle medewerkers voortaan met tablets werken, terwijl de organisatie nauwelijks digitaal werkt. Op welke dimensie scoort het ontwerp zwak?",
   ["Impact", "Aansluiting op de context", "Haalbaarheid volgens 80/20", "Takttijd"], 1,
   "Aansluiting op de context: past het bij cultuur, systemen en de bedoeling van de organisatie? Dit is de toets die studenten het vaakst vergeten.")

# ---------- open ----------
op("pp2-o1", W, P, "Een bezoeker meldt zich bij de receptie van een kantoor. Deel deze vier stappen in als VA, BNVA of NVA en geef bij elk de ontwerpregel: (1) wachten tot de receptionist klaar is met een telefoontje, (2) een identiteitsbewijs laten zien voor de toegangsregistratie, (3) de gastheer wordt gebeld en haalt de bezoeker op, (4) de receptionist typt de gegevens over van de papieren lijst in het systeem.",
   "(1) NVA, wachten is pure verspilling: elimineren. (2) BNVA, nodig voor veiligheid maar geen klantwaarde: minimaliseren, bijvoorbeeld vooraf digitaal aanmelden. (3) VA, de bezoeker komt hiervoor: behouden en versterken. (4) NVA, overtypen: elimineren, bijvoorbeeld direct digitaal registreren.",
   ["Stap 1 en 4 als NVA met elimineren", "Stap 2 als BNVA met minimaliseren", "Stap 3 als VA met behouden/versterken"])
op("pp2-o2", W, P, "Noem de drie manieren om een toekomstbeeld vast te leggen. Welke kies je voor het verbeteren van de catering bij vergaderingen, als de opdrachtgever vooral wil weten wat de gast merkt van de veranderingen? Onderbouw.",
   "Future-state map (complete waardestroom met tijden en informatiestromen), service blueprint (scheidt frontstage, wat de gebruiker ziet, van backstage) en verbeterde flow (aangepaste flowchart of swimlane). Hier past de service blueprint: catering is dienstverlening en de opdrachtgever wil zien wat de gast ervaart. Je laat zien welke backstage-verbeteringen er zijn zonder verlies van frontstage-kwaliteit.",
   ["Drie vormen juist genoemd", "Service blueprint gekozen", "Onderbouwing met frontstage/backstage en beleving"])
op("pp2-o3", W, P, "Een team twijfelt tussen twee richtingen voor het schoonmaakproces: (A) schoonmaken op basis van gebruik met sensoren, (B) vaste schoonmaakrondes met een betere checklist. Vergelijk A en B op de vier dimensies uit de les.",
   "Haalbaarheid: B is binnen tijd en middelen goed haalbaar; A vraagt sensoren, koppeling en budget. Impact: A kan meer impact hebben (minder onnodig schoonmaken, meer waar het nodig is), B verbetert vooral de kwaliteit; volgens de KKT-driehoek kun je zelden alles tegelijk verbeteren. Risico: A heeft meer risico (techniek, data, acceptatie); eenvoud is bijna altijd een deugd. Context: past A bij de systemen en de cultuur van de organisatie en het schoonmaakbedrijf? Conclusie bijvoorbeeld: B als basis en A eerst als pilot.",
   ["Haalbaarheid vergeleken", "Impact vergeleken, met KKT of 80/20", "Risico vergeleken", "Context vergeleken"])
op("pp2-o4", W, P, "Beschrijf de vijf stappen van de PUGH-matrix. Welke valkuil noemt de docent bij de weging, en hoe voorkom je die?",
   "1. Representatieve groep samenstellen: team plus stakeholders van wie je het oordeel vertrouwt. 2. Maximaal zes vitale criteria bepalen en de zwaarste een hoger gewicht geven. 3. De baseline (huidige situatie) krijgt op elk criterium 0. 4. Elk alternatief scoren ten opzichte van de baseline, van −2 tot +2. 5. Score × gewicht, optellen per alternatief; de hoogste totaalscore wint. Valkuil: als je de gewichten pas na het scoren afspreekt, stuurt de weging stiekem het antwoord. Voorkomen: gewichten vooraf afspreken en de cijfers samen bespreken.",
   ["Stap 1 en 2 juist", "Stap 3 en 4 juist (baseline 0, −2 tot +2)", "Stap 5 juist", "Valkuil weging en oplossing: gewichten vooraf afspreken"])
op("pp2-o5", W, P, "Leg het verschil uit tussen een pilot, een simulatie en een gefaseerde invoering. Geef bij elk een FM-situatie waarin je die vorm kiest.",
   "Pilot: op kleine schaal testen in de echte omgeving, met plan, meetafspraken en getrainde medewerkers; daarna evalueren en verfijnen. Bijvoorbeeld een nieuw meldproces vier weken op één afdeling. Simulatie: de werkelijkheid veilig nabootsen als een echte test te ingrijpend is, bijvoorbeeld een ontruimingsprocedure of een nieuwe looproute op een OK-complex. Gefaseerd: stap voor stap uitrollen bij grote veranderingen, bijvoorbeeld een nieuw FMIS per gebouw invoeren.",
   ["Pilot juist met passend voorbeeld", "Simulatie juist met passend voorbeeld", "Gefaseerd juist met passend voorbeeld"])
op("pp2-o6", W, P, "De voorkeursoplossing voor de catering bij vergaderingen is een online bestelformulier dat direct bij de keuken binnenkomt, met een vaste besteldeadline. Onderbouw de waarde voor de opdrachtgever, de gebruiker en het proces.",
   "Opdrachtgever: minder weggegooid eten en minder spoedbestellingen (kosten, duurzaamheid), betrouwbaarder dienstverlening en beter imago bij bezoekers. Gebruiker: bestellen kost minder moeite, de bestelling klopt en staat op tijd klaar (beleving, betrouwbaarheid). Proces: minder verspilling (geen mails die worden overgetypt), kortere doorlooptijd en minder variatie voor de keuken. Een sterk antwoord laat zien dat de oplossing het geheel dient.",
   ["Opdrachtgever: koppeling aan doelen of KPI's in zijn taal", "Gebruiker: klantwaarde vanuit de vergaderaar", "Proces: minder verspilling, kortere doorlooptijd of minder variatie"])

# ---------- casus ----------
cs("pp2-c1", W, P, "Aanvraag van een toegangspas",
   "Bij een gemeentehuis vraagt een nieuwe medewerker een toegangspas aan. Huidige situatie: (1) de leidinggevende mailt een formulier naar de receptie; (2) de mail ligt gemiddeld 2 dagen in een gedeelde mailbox; (3) de receptie print het formulier en laat het tekenen door het hoofd beveiliging; (4) het getekende formulier gaat per interne post naar de afdeling ICT (1 dag); (5) ICT typt de gegevens over in het toegangssysteem; (6) de pas wordt gemaakt (10 minuten); (7) de medewerker haalt de pas op bij de receptie. De doorlooptijd is gemiddeld 6 werkdagen; nieuwe medewerkers lopen hun eerste week met een dagpas.",
   [("Deel de zeven stappen in als VA, BNVA of NVA.",
     "VA: 6 (de pas maken) en eventueel 7 (de medewerker krijgt de pas). BNVA: 1 (de aanvraag moet er zijn) en 3 (een controle door beveiliging is nodig, maar kan eenvoudiger). NVA: 2 (wachten in de mailbox), 4 (interne post, transport en wachten) en 5 (overtypen).",
     ["NVA-stappen juist (2, 4, 5)", "BNVA-stappen juist (1, 3)", "VA-stap(pen) juist (6, eventueel 7)"]),
    ("Ontwerp de future state. Beschrijf hoe het proces straks loopt en wat je doet met elk soort stap.",
     "Bijvoorbeeld: de leidinggevende vult één digitaal formulier in dat direct in het toegangssysteem landt (overtypen en interne post geëlimineerd); het hoofd beveiliging keurt digitaal goed, of standaardaanvragen worden zonder akkoordstap goedgekeurd (BNVA geminimaliseerd); aanvragen worden op FIFO-basis opgepakt; de pas ligt op dag 1 klaar. Doorlooptijd van 6 dagen naar 1 dag. Regels: NVA elimineren, BNVA minimaliseren, VA behouden.",
     ["NVA geëlimineerd met concrete maatregel", "BNVA geminimaliseerd met concrete maatregel", "Samenhangend beeld met nieuwe doorlooptijd of flow (FIFO)"]),
    ("Welke vorm kies je om dit toekomstbeeld aan de opdrachtgever te laten zien? Onderbouw.",
     "Verbeterde flow (swimlane) is pragmatisch: je laat zien welke stappen geschrapt en samengevoegd zijn tussen leidinggevende, receptie, beveiliging en ICT. Een future-state map kan ook, als je de tijden en informatiestromen volledig wilt tonen. Een service blueprint is minder logisch, omdat het hier vooral om backstage gaat.",
     ["Passende vorm gekozen", "Onderbouwing gekoppeld aan wat de vorm laat zien"])])
cs("pp2-c2", W, P, "PUGH-matrix voor het afvalproces",
   "Een team wil het afvalproces van een kantoorgebouw verbeteren. Er zijn drie opties naast de huidige situatie (baseline): (A) centrale afvalstations per verdieping, (B) persoonlijke prullenbakken weghalen en scheiden bij de bron, (C) een externe partij die het afval na ophalen sorteert. Criteria en wegingen: scheidingspercentage (5), kosten (3), gebruiksgemak (4), invoeringsrisico (2). Scores: A: +2, −1, +1, 0. B: +2, +1, −1, −1. C: +1, −2, +2, +1.",
   [("Bereken het gewogen totaal van A, B en C en geef aan welke optie wint.",
     "A: (2×5) + (−1×3) + (1×4) + (0×2) = 10 − 3 + 4 + 0 = 11. B: 10 + 3 − 4 − 2 = 7. C: 5 − 6 + 8 + 2 = 9. Optie A wint met 11.",
     ["A = 11 juist", "B = 7 en C = 9 juist", "A als winnaar"]),
    ("Het team ontdekt dat het gewicht van kosten pas na het scoren van 4 naar 3 is verlaagd. Wat is daar mis mee, en wat zou je doen?",
     "Gewichten spreek je af vóór het scoren; anders stuurt de weging stiekem het antwoord. Met kosten op 4 wordt het A: 11 − 1 = 10, B: 7 + 1 = 8, C: 9 − 2 = 7; A wint nog steeds, maar dat moet je laten zien. Doe het transparant: leg vast waarom het gewicht zou moeten veranderen, bespreek het met de groep en reken beide varianten door. De matrix is een hulpmiddel, geen rechter.",
     ["Benoemt dat gewichten vooraf moeten worden vastgesteld", "Rekent de variant door of laat zien dat de uitkomst gelijk blijft", "Transparante aanpak: bespreken en vastleggen"]),
    ("Benoem één risico van de winnende optie en doe een voorstel om dat risico te beheersen.",
     "Risico bij A: medewerkers blijven hun afval toch op de werkplek weggooien of lopen niet naar het station, waardoor het scheidingspercentage tegenvalt. Voorstel: eerst een pilot van vier weken op één verdieping, met vooraf een meetafspraak (scheidingspercentage per week), communicatie en uitleg aan medewerkers, en daarna evalueren en verfijnen voordat het gebouwbreed wordt ingevoerd.",
     ["Reëel risico van optie A", "Pilot (of simulatie/gefaseerd) passend gekozen", "Met meetafspraken of evaluatie"])])
cs("pp2-c3", W, P, "Vergaderzalen bij een zorgverzekeraar",
   "Bij een zorgverzekeraar staan vergaderzalen vaak niet klaar: de opstelling klopt niet, de beamer werkt niet of de koffie ontbreekt. Reserveren gaat via Outlook, opstelling via een mail aan de facilitaire dienst en catering via een apart formulier. De organisatie wil de komende jaren vooral kosten besparen en heeft een cultuur waarin alles via de leidinggevende moet. Het team overweegt twee richtingen: (1) één reserveringsformat waarin zaal, opstelling en catering samen worden aangevraagd, plus een gereedmaak-checklist; (2) een volledig zelfbedieningsconcept waarin medewerkers zelf de zaal inrichten en koffie halen.",
   [("Vergelijk de twee richtingen op haalbaarheid, risico en aansluiting op de context.",
     "Haalbaarheid: richting 1 is met bestaande middelen snel in te voeren; richting 2 vraagt herinrichting van zalen en voorzieningen. Risico: bij 2 is de kans groter dat zalen rommelig achterblijven en dat externe gasten een slechte indruk krijgen; eenvoud is een deugd, dus 1 is risicoarmer. Context: in een cultuur waarin alles via de leidinggevende gaat, past volledige zelfbediening slecht; richting 1 sluit beter aan, al kan 2 wel bij het besparingsdoel passen.",
     ["Haalbaarheid juist vergeleken", "Risico juist vergeleken", "Context: cultuur van de organisatie meegenomen"]),
    ("Welke richting adviseer je? Onderbouw de waarde voor opdrachtgever, gebruiker en proces.",
     "Bijvoorbeeld richting 1. Opdrachtgever: minder verspilde zaaltijd en spoedwerk, past bij kosten besparen en een betrouwbare uitstraling naar externe gasten. Gebruiker: één aanvraag in plaats van drie, en de zaal staat klaar zoals afgesproken. Proces: minder overdrachten en dubbele registratie, kortere doorlooptijd en minder variatie door de checklist. Een andere keuze kan ook goed zijn als ze met de drie perspectieven wordt onderbouwd.",
     ["Keuze gemaakt en logisch na de vergelijking", "Waarde voor opdrachtgever en gebruiker", "Waarde voor het proces"])])
