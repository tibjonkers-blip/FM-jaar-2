W = 4
P = "Verbeterproject"

# ---------- MC ----------
mc("pp4-m01", W, P, "Wat is implementeren volgens de les?",
   ["Het kiezen van de beste oplossing met de PUGH-matrix en de opdrachtgever",
        "Het invoeren van de gekozen oplossing, met alle activiteiten en wie wat wanneer doet",
        "Het meten van de huidige situatie met een nulmeting en procesanalyse",
        "Het overdragen van het project aan de proceseigenaar bij de Tollgate"], 1,
   "In een implementatieplan beschrijf je álle activiteiten en wie, wat en wanneer in actie komt. Het Lean-boek benadrukt discipline.")
mc("pp4-m02", W, P, "Welke van deze vier is een mijlpaal in een implementatieplan?",
   ["Een budget van € 5.000 voor training", "Training afgerond", "80% van de meldingen via het portaal", "Een werkende koppeling met het FMIS vóór de start"], 1,
   "Een mijlpaal is een controleerbaar ijkmoment in de planning. Het budget is een middel, 80% via het portaal is een succescriterium, en de werkende koppeling is een randvoorwaarde.")
mc("pp4-m03", W, P, "Wat is volgens de les belangrijk bij de bouwsteen middelen?",
   ["Alle middelen bij de opdrachtgever neerleggen", "Kritieke resources op naam zetten", "Middelen pas na de pilot bepalen", "Alleen het budget noemen"], 1,
   "Middelen zijn mensen, budget, systemen en tijd. Zet de kritieke resources op naam, zodat duidelijk is wie of wat je echt nodig hebt.")
mc("pp4-m04", W, P, "Je rekent terug vanaf de gewenste invoerdatum en ziet dat de planning niet past. Wat raadt de les aan?",
   ["De invoerdatum altijd verschuiven",
    "Activiteiten inkorten of parallel uitvoeren",
    "De training schrappen, want die kost de meeste tijd",
    "De mijlpalen weglaten"], 1,
   "Reken terug vanaf de wensdatum. Te laat? Kort in of voer activiteiten parallel uit, met oog voor de afhankelijkheden.")
mc("pp4-m05", W, P, "'De training kan pas starten als de werkinstructie klaar is.' Waar moet je in de planning dus op letten?",
   ["Op de afhankelijkheden tussen activiteiten",
        "Op de RPN-score van de training in de FMEA",
        "Op de span of control van de trainer",
        "Op de takttijd van het nieuwe proces"], 0,
   "Bewaak afhankelijkheden: activiteit 2 kan pas starten als activiteit 1 klaar is.")
mc("pp4-m06", W, P, "Waarom geef je per resultaat maar één persoon de eindverantwoordelijkheid?",
   ["Omdat gedeelde eindverantwoordelijkheid in de praktijk van niemand is",
        "Omdat de opdrachtgever in het implementatieplan maar één naam wil zien",
        "Omdat de anderen dan als Informed op de hoogte gehouden kunnen worden",
        "Omdat de FMEA per risico precies één verantwoordelijke voorschrijft"], 0,
   "Met meerdere A's geeft niemand de doorslag en voelt niemand zich echt eigenaar.")
mc("pp4-m07", W, P, "Wat is het doel van FMEA?",
   ["Achteraf onderzoeken waarom een project mislukte",
    "Potentiële fouten in een proces opsporen en aanpakken voordat ze optreden",
    "De beste oplossing kiezen uit een aantal alternatieven",
    "Bepalen wie welke rol heeft in het project"], 1,
   "FMEA (Failure Mode and Effect Analysis) stelt bij elke processtap de vraag: wat zou hier fout kunnen gaan? De methode komt van de NASA.")
mc("pp4-m08", W, P, "Wat is het hoogst mogelijke RPN in de FMEA-light uit de les?",
   ["15", "25", "100", "125"], 3,
   "Elke factor loopt van 1 tot 5, dus het maximum is 5 × 5 × 5 = 125.")
mc("pp4-m09", W, P, "Een risico scoort Ernst 3, Kans 4 en Detectie 3. Wat is het RPN?",
   ["10", "12", "36", "48"], 2,
   "3 × 4 × 3 = 36.")
mc("pp4-m10", W, P, "Welk risico krijgt de hoogste prioriteit? (1) E5, K1, D4. (2) E2, K5, D3. (3) E4, K3, D2.",
   ["Risico 1, want de ernst is het hoogst", "Risico 2, met RPN 30", "Risico 3, met RPN 24", "Risico 1, met RPN 20"], 1,
   "RPN 1 = 20, RPN 2 = 30, RPN 3 = 24. Niet de hoogste ernst bepaalt de prioriteit, maar de combinatie.")
mc("pp4-m11", W, P, "Na de maatregel 'monitoring en automatische alert bij uitval van de koppeling' scoor je het risico opnieuw. Welke score daalt vooral?",
   ["Ernst", "Kans", "Detectie", "Geen enkele"], 2,
   "Met monitoring en een alert ontdek je de fout sneller, dus de detectiescore daalt. De koppeling valt niet minder vaak uit, en de ernst blijft meestal gelijk.")
mc("pp4-m12", W, P, "Na de maatregel 'minder en duidelijkere categorieën in het portaal' scoor je het risico 'melding in de verkeerde categorie' opnieuw. Welke score daalt vooral?",
   ["Ernst", "Kans", "Detectie", "Alle drie evenveel"], 1,
   "Met minder, heldere categorieën kiezen melders minder vaak de verkeerde: de kans daalt.")
mc("pp4-m13", W, P, "Welke techniek gebruik je volgens de notities binnen FMEA om de kernoorzaak van een faalmogelijkheid te vinden?",
   ["5x Waarom", "PUGH-matrix", "RACI", "Belang-invloed-grid"], 0,
   "Met 5x Waarom vraag je door tot de kernoorzaak. Zo richt je je maatregel op de oorzaak in plaats van op het symptoom.")
mc("pp4-m14", W, P, "Welke invoeringsstrategie heeft volgens de les het laagste risico?",
   ["Big-bang", "Schaduwdraaien", "Gefaseerd", "Pilot"], 3,
   "Pilot heeft het laagste risico, big-bang het hoogste. Gefaseerd en schaduwdraaien zitten daartussen.")
mc("pp4-m15", W, P, "Welke van deze vier is géén leidend criterium bij de keuze van een invoeringsstrategie?",
   ["Het risico voor de operationele dienstverlening",
    "De mogelijkheid tot schaduwdraaien",
    "De technische mogelijkheid om te faseren",
    "De voorkeur van het studententeam voor een snelle afronding"], 3,
   "De drie leidende criteria uit de notities zijn operationeel risico, schaduwdraaien en faseren. Kies samen met de operationele organisatie en laat de managers accorderen.")
mc("pp4-m16", W, P, "Bij welke randvoorwaarde voor een goede pilot leg je vast welke data je verzamelt, door wie en wanneer?",
   ["Plan", "Datacollectieplan", "Communicatie", "Evaluatie"], 1,
   "Het datacollectieplan. Zonder data kun je bij de evaluatie niet vaststellen of de pilot de doelen haalt.")
mc("pp4-m17", W, P, "Welk van deze vier hoort níet bij de vijf vakken van de zeester in de retrospective?",
   ["Blijven doen", "Meer van", "Stoppen", "Meer budget"], 3,
   "De zeester heeft vijf vakken: blijven doen, meer van, minder van, stoppen en starten.")
mc("pp4-m18", W, P, "Hoe eindigt het teamdeel van de retrospective volgens de les?",
   ["Met een cijfer voor elk teamlid",
    "Met maximaal twee concrete teamacties",
    "Met een nieuwe PUGH-matrix",
    "Met een lijst van alle verbeterpunten zonder keuze"], 1,
   "Eindig met maximaal twee concrete teamacties. Leg als team een foto van de zeester, een korte samenvatting en de twee actiepunten vast.")

# ---------- open ----------
op("pp4-o1", W, P, "Noem de zes bouwstenen van een implementatieplan en geef bij elke bouwsteen in één zin wat je vastlegt.",
   "1. Activiteiten: hoofd- en subacties, inclusief opleiding en instructies. 2. Mijlpalen: controleerbare ijkmomenten, zoals 'pilot gestart' of 'go/no-go'. 3. Verantwoordelijkheden: wie doet wat, belegd met RACI, één Accountable per resultaat. 4. Middelen: mensen, budget, systemen en tijd, kritieke resources op naam. 5. Randvoorwaarden: wat moet kloppen vóór de start, zoals een werkende koppeling. 6. Succescriteria: SMART en gekoppeld aan KPI's en klantwaarde.",
   ["Twee bouwstenen juist met uitleg", "Nog twee bouwstenen juist met uitleg", "Laatste twee bouwstenen juist met uitleg"])
op("pp4-o2", W, P, "Een team schrijft als succescriteria: 'de schoonmaak wordt beter' en 'gebruikers zijn tevredener'. Herschrijf beide SMART en leg uit waarom dat nodig is.",
   "Bijvoorbeeld: 'Binnen 10 weken is het percentage afgekeurde ruimtes bij de kwaliteitsmeting gedaald van 15% naar maximaal 5%' en 'In de gebruikersenquête van maart scoort de schoonmaak gemiddeld minstens een 7,5 (nu 6,4)'. Nodig omdat zonder vooraf afgesproken criteria elke evaluatie een kwestie van gevoel wordt; met criteria voer je het gesprek met de opdrachtgever op basis van feiten.",
   ["Eerste criterium SMART (meetbaar, met termijn)", "Tweede criterium SMART", "Uitleg: zonder criteria wordt evaluatie een kwestie van gevoel"])
op("pp4-o3", W, P, "Leg de detectielogica in de FMEA uit. Waarom krijgt de meest voorkomende fout niet automatisch de hoogste prioriteit?",
   "Detectie gaat over hoe moeilijk een fout te ontdekken is. Een lage score betekent dat de fout makkelijk wordt opgemerkt, een hoge score dat hij ongezien schade aanricht. Slechte detecteerbaarheid verhoogt dus het RPN. Prioriteit volgt uit RPN = E × K × D: een fout die vaak voorkomt maar weinig ernstig en goed zichtbaar is (zoals 'gebruiker blijft bellen', RPN 30) kan lager eindigen dan een zeldzame fout die ernstig is en lang onopgemerkt blijft (zoals 'FMIS-koppeling valt uit', RPN 50).",
   ["Hoge detectiescore = moeilijk te ontdekken, verhoogt RPN", "RPN als combinatie van ernst, kans en detectie", "Voorbeeld of uitleg waarom frequentie alleen niet beslist"])
op("pp4-o4", W, P, "Beschrijf de zes stappen van de FMEA-light. Wat betekent het dat FMEA iteratief is?",
   "1. Kies de belangrijkste processtappen. 2. Benoem per stap de faalmogelijkheid. 3. Beschrijf het effect op klant en proces. 4. Scoor ernst, kans en detectie (1-5). 5. Bereken het RPN en sorteer van hoog naar laag. 6. Bepaal per toprisico een beheersmaatregel en een verantwoordelijke. Iteratief: na de maatregelen scoor je opnieuw op kans en detectie om te zien of het risico echt daalt; de ernst blijft meestal gelijk.",
   ["Stap 1 t/m 3 juist", "Stap 4 en 5 juist", "Stap 6 met maatregel én verantwoordelijke", "Iteratief: opnieuw scoren, ernst blijft meestal gelijk"])
op("pp4-o5", W, P, "Leg uit wat een OCAP is en wat catchball is. Geef bij beide een voorbeeld bij de invoering van een nieuw meldportaal.",
   "OCAP (Out of Control Action Plan): een vooraf klaarliggend noodplan met triggers en acties voor als het toch misgaat. Voorbeeld: als het portaal langer dan een uur niet werkt (trigger), schakelt de servicedesk over op de fallback-mailbox en meldt ICT het binnen 15 minuten (actie). Catchball: de oplossing met mensen invoeren door hen om feedback te vragen, zodat ze eigenaar worden. Voorbeeld: baliemedewerkers bepalen mee welke meldcategorieën er komen.",
   ["OCAP juist uitgelegd", "OCAP-voorbeeld met trigger en actie", "Catchball juist uitgelegd met voorbeeld"])
op("pp4-o6", W, P, "Na de retrospective leg je individueel een aantal dingen vast voor je portfolio. Welke vier vragen beantwoord je volgens de les, en waarom is het belangrijk om ook terug te kijken op de afspraken van de vorige keer?",
   "Welke feedback kreeg ik? Wat zegt dit over mijn gedrag in de groep? Wat ga ik bewust uitproberen? Waar wil ik opnieuw feedback op? Terugkijken op vorige afspraken is belangrijk omdat elke retrospective anders een losse evaluatie wordt; zo zie je je ontwikkeling over meerdere sprints, en kun je checken of je actie nog bij je leerdoel past (een leerdoel bijstellen hoort bij ontwikkeling).",
   ["Minstens drie van de vier vragen juist", "Alle vier de vragen juist", "Reden: ontwikkeling over meerdere sprints zichtbaar, geen losse evaluatie"])

# ---------- casus ----------
cs("pp4-c1", W, P, "Digitale bezoekersregistratie bij een ministerie",
   "Een ministerie wil de papieren bezoekerslijst bij de receptie vervangen door digitale vooraanmelding: de gastheer meldt de bezoeker vooraf aan en de bezoeker krijgt een QR-code. Het concept-implementatieplan van het team bestaat uit: (1) software selecteren, (2) koppeling met het toegangssysteem maken, (3) systeem live zetten op 1 maart. Verantwoordelijk: 'de facilitaire dienst'. Succescriterium: 'de receptie wordt minder druk'.",
   [("Wat ontbreekt er aan de activiteiten? Noem minstens drie ontbrekende activiteiten en leg uit waarom de les dit de klassieke beginnersfout noemt.",
     "Ontbrekend: training van receptionisten en beveiliging, werkinstructie voor de receptie, communicatie naar alle medewerkers die gasten ontvangen (gastheren), procesbeschrijving, begeleiding in de eerste weken, een terugvaloptie. De beginnersfout is alleen de zichtbare verandering plannen ('systeem aanzetten') en training, instructies en begeleiding vergeten; daar zit het echte werk.",
     ["Drie relevante ontbrekende activiteiten", "Uitleg beginnersfout: alleen zichtbare verandering gepland"]),
    ("Verbeter de bouwstenen verantwoordelijkheden en succescriteria.",
     "Verantwoordelijkheden: niet 'de facilitaire dienst', maar per activiteit een RACI met één Accountable, bijvoorbeeld hoofd facilitaire dienst A voor de invoering, ICT R voor de koppeling, teamleider receptie R voor de training, beveiliging C. Succescriteria SMART, bijvoorbeeld: 'binnen 6 weken na livegang is 90% van de bezoekers vooraf aangemeld' en 'de gemiddelde wachttijd bij de receptie is binnen 2 maanden onder 2 minuten'.",
     ["RACI met één Accountable per resultaat", "Minstens één SMART succescriterium", "Tweede SMART criterium of koppeling aan klantwaarde"]),
    ("Noem drie mijlpalen en één randvoorwaarde voor dit plan.",
     "Mijlpalen: software gekozen, testomgeving gereed, training afgerond, pilot gestart, go/no-go, organisatiebreed live. Randvoorwaarde: de koppeling met het toegangssysteem werkt en voldoet aan de beveiligingseisen, of het budget is goedgekeurd, of alle gastheren hebben toegang tot het aanmeldsysteem.",
     ["Drie controleerbare mijlpalen", "Eén randvoorwaarde die vóór de start moet kloppen"])])
cs("pp4-c2", W, P, "FMEA-light voor het nieuwe cateringbestelsysteem",
   "Een team maakt een FMEA-light voor een nieuw online bestelsysteem voor vergadercatering. Risico's met scores (E, K, D): (A) besteller vergeet het aantal personen aan te passen: 2, 4, 3. (B) bestelling komt niet bij de keuken aan door een storing: 5, 2, 4. (C) dieetwensen worden niet doorgegeven: 4, 3, 4. (D) besteller bestelt na de deadline: 2, 5, 1.",
   [("Bereken de RPN van alle vier de risico's en zet ze in volgorde van prioriteit.",
     "A: 2 × 4 × 3 = 24. B: 5 × 2 × 4 = 40. C: 4 × 3 × 4 = 48. D: 2 × 5 × 1 = 10. Volgorde: C (48), B (40), A (24), D (10).",
     ["RPN A en D juist", "RPN B en C juist", "Juiste volgorde"]),
    ("Bepaal voor de twee hoogste risico's een beheersmaatregel en een verantwoordelijke. Geef aan welke score door je maatregel daalt.",
     "C (dieetwensen): verplicht veld 'dieetwensen' in het formulier (Poka-Yoke), verlaagt de kans; en de keuken controleert dieetbestellingen met een checklist, verlaagt de detectiescore. Verantwoordelijke: bijvoorbeeld de teamleider catering. B (storing): automatische bevestiging aan de keuken en een melding als een bestelling niet binnenkomt, verlaagt de detectiescore; een fallback per mail verkleint de gevolgen. Verantwoordelijke: bijvoorbeeld de applicatiebeheerder.",
     ["Maatregel voor C met verantwoordelijke", "Maatregel voor B met verantwoordelijke", "Juist aangegeven welke score daalt (kans of detectie)"]),
    ("Risico D komt het vaakst voor. Waarom krijgt het toch de laagste prioriteit?",
     "De prioriteit volgt uit de combinatie van ernst, kans en detectie. D komt vaak voor, maar de gevolgen zijn klein (ernst 2) en het wordt direct opgemerkt (detectie 1), dus RPN 10. Niet de meest voorkomende fout krijgt prioriteit, maar de combinatie.",
     ["Uitleg met lage ernst en goede detectie", "Principe: combinatie bepaalt de prioriteit"])])
cs("pp4-c3", W, P, "Nieuw toegangssysteem in het Rivierenland Ziekenhuis",
   "Het Rivierenland Ziekenhuis (fictief) vervangt de sleutels van alle 1.200 deuren door een pas-systeem. Het oude sleutelsysteem kan tijdelijk blijven werken. De leverancier biedt aan om in één nacht alle deuren om te bouwen ('dan is het in één keer klaar'). Op de afdelingen spoedeisende hulp en de OK moeten medewerkers altijd direct overal bij kunnen.",
   [("Welke invoeringsstrategie adviseer je? Onderbouw met de criteria uit de les en zeg waarom je het aanbod van de leverancier wel of niet volgt.",
     "Het aanbod is een big-bang: snel, maar met het hoogste risico. Het risico voor de operationele dienstverlening is hier groot (SEH en OK). Het oude systeem kan blijven werken, dus schaduwdraaien is mogelijk, en faseren per afdeling is technisch mogelijk. Advies: start met een pilot op een minder kritische afdeling (bijvoorbeeld kantoren), daarna gefaseerd per afdeling, en houd op SEH en OK tijdelijk de sleutels als schaduwsysteem. Kies dit samen met de operationele organisatie en laat het door de managers accorderen.",
     ["Big-bang afgewezen vanwege hoogste risico", "Criteria gebruikt: operationeel risico, schaduwdraaien, faseren", "Concreet advies met pilot, gefaseerd of schaduwdraaien"]),
    ("Noem vier van de zes randvoorwaarden voor een goede pilot en werk ze uit voor dit ziekenhuis.",
     "Plan: pilot van drie weken op de kantoorvleugel, met doel en betrokkenen. Datacollectieplan: aantal mislukte toegangspogingen en storingsmeldingen per dag, bijgehouden door beveiliging. Communicatie: medewerkers weten wanneer hun deur omgaat en wat ze moeten doen bij problemen. Training: beveiliging en receptie kunnen passen aanmaken en blokkeren. Uitvoering volgens plan inclusief dataverzameling. Evaluatie: resultaten tegen de doelen, voordat de volgende fase start.",
     ["Twee randvoorwaarden concreet voor het ziekenhuis", "Nog twee randvoorwaarden concreet", "Evaluatie tegen doelen of datacollectie genoemd"])])
