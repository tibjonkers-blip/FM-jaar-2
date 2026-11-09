W = 4
I, R = "Inkoop", "Recht"

# ---------- Inkoop MC (aanbestedingsdocumenten beoordelen) ----------
mc("ir4-i01", W, I, "Je beoordeelt een aanbesteding met de vraag 'kan een normaal bedrijf aan deze eisen voldoen?'. Welk beginsel toets je vooral?",
   ["Proportionaliteit", "Wederzijdse erkenning", "Objectiviteit", "Non-discriminatie op nationaliteit"], 0,
   "Of eisen haalbaar en in verhouding tot de opdracht zijn, is de kern van proportionaliteit. De Gids Proportionaliteit is daarbij het verplichte richtsnoer.")
mc("ir4-i02", W, I, "In een aankondiging staat bij de gunning alleen: 'Wij kiezen de inschrijving die het beste bij ons past.' Wat is het probleem?",
   ["Er is geen probleem, de dienst mag zelf kiezen", "Gunningscriteria en wegingen zijn niet vooraf duidelijk, in strijd met transparantie en objectiviteit", "Het is in strijd met het clusterverbod", "Het mag alleen bij de openbare procedure"], 1,
   "Inschrijvers moeten vooraf weten waarop en met welk gewicht ze worden beoordeeld (art. 2.115 lid 4 Aw). Een open norm als 'wat het beste past' maakt willekeur mogelijk.")
mc("ir4-i03", W, I, "Welke aanwijzing in de aanbestedingsdocumenten maakt een opdracht juist toegankelijker voor kleine bedrijven?",
   ["Eén groot perceel voor alle locaties", "Verdeling in percelen per regio met proportionele omzeteisen", "Een omzeteis van tien keer de opdrachtwaarde", "Referenties van minstens vijf vergelijkbare landelijke opdrachten"], 1,
   "Percelen en eisen die in verhouding staan tot (het perceel van) de opdracht verlagen de drempel voor het mkb. Dat sluit aan bij art. 1.5 Aw.")
mc("ir4-i04", W, I, "Een gemeente gunt de catering met prijs 70% en kwaliteit 30%. Wat zegt dat over haar prioriteiten?",
   ["Kwaliteit weegt zwaarder", "Prijs weegt zwaarder; de kans is groot dat de goedkoopste inschrijver wint", "Er wordt op laagste prijs gegund", "Dit mag niet, kwaliteit moet altijd zwaarder wegen"], 1,
   "Bij 70% prijs is het nog steeds BPKV, maar de prijs is dominant. Een weging is toegestaan, als die maar vooraf bekend is.")
mc("ir4-i05", W, I, "Een aanbesteding is juridisch correct, maar voelt voor kleine bedrijven toch oneerlijk. Welke verklaring past het best?",
   ["Juridisch correct betekent altijd eerlijk", "Eisen die net binnen de wet blijven (zoals hoge referentie-eisen of één groot perceel) kunnen kleine bedrijven feitelijk uitsluiten", "Kleine bedrijven mogen nooit meedoen aan Europese aanbestedingen", "Eerlijkheid speelt in het aanbestedingsrecht geen rol"], 1,
   "Dit is de derde stelling van de aanbestedingsrechtbank. Iets kan rechtmatig zijn en toch in de praktijk drempels opwerpen, bijvoorbeeld door zware referentie-eisen, korte termijnen of grote clusters.")
mc("ir4-i06", W, I, "Je wilt nagaan of bedrijven begrijpen wat ze moeten aanbieden en hoe ze worden beoordeeld. Waar kijk je vooral naar?",
   ["De omzet van de opdrachtgever", "Het programma van eisen, de beoordelingssystematiek en de nota van inlichtingen", "Het aantal inschrijvers bij de vorige aanbesteding", "De kleur van de huisstijl"], 1,
   "Duidelijkheid zie je terug in een helder programma van eisen, een uitgewerkte beoordelingssystematiek (wat scoort hoe) en de antwoorden in de nota van inlichtingen.")
mc("ir4-i07", W, I, "Wat is een nota van inlichtingen?",
   ["Het contract met de winnaar", "Een document waarin de aanbestedende dienst vragen van alle (potentiële) inschrijvers beantwoordt, gelijk voor iedereen", "Een geheim verslag van de beoordelingscommissie", "Het afwijzingsbericht aan de verliezers"], 1,
   "Via de nota van inlichtingen krijgen alle inschrijvers dezelfde antwoorden. Dat dient gelijkheid en transparantie.")
mc("ir4-i08", W, I, "Een ziekenhuis eist voor de schoonmaak 'minstens vijf referenties van ziekenhuizen met meer dan 1.000 bedden in de afgelopen drie jaar'. Hoe beoordeel je dat?",
   ["Prima, hoe zwaarder de eis hoe beter", "Waarschijnlijk disproportioneel: weinig bedrijven kunnen dit, terwijl ervaring in de zorg ook met minder of kleinere referenties aan te tonen is", "Verplicht volgens de Gids Proportionaliteit", "Alleen een probleem bij leveringen"], 1,
   "Referentie-eisen moeten in verhouding staan tot de opdracht. De Gids Proportionaliteit raadt aan het aantal referenties te beperken en te vragen naar relevante, niet per se identieke ervaring.")
mc("ir4-i09", W, I, "Welke vraag hoort NIET bij een eerste analyse van een gepubliceerde aanbesteding?",
   ["Wat wordt er ingekocht?", "Wie is de opdrachtgever?", "Hoe wordt de winnaar gekozen?", "Welke inschrijver gaat waarschijnlijk winnen?"], 3,
   "Het werkblad van de les vraagt wat er wordt ingekocht, wie de opdrachtgever is, welke eisen er zijn en hoe wordt gegund. Wie gaat winnen kun je uit de documenten niet afleiden.")
mc("ir4-i10", W, I, "Een gemeente kondigt een complexe facilitaire aanbesteding aan met een inschrijftermijn die net aan het wettelijke minimum voldoet, midden in de zomervakantie. Welk punt kun je als 'oneerlijk' aanmerken?",
   ["De korte termijn in de vakantie benadeelt kleinere inschrijvers zonder grote tenderafdeling", "Het is verboden in de zomer aan te besteden", "De gemeente moet altijd minstens een jaar de tijd geven", "Niets, termijnen spelen geen rol"], 0,
   "Wettelijk kan het kloppen, maar de dienst moet bij het bepalen van termijnen ook rekening houden met de complexiteit van de opdracht. Een krappe termijn in de vakantie benadeelt partijen zonder grote tenderteams.")
mc("ir4-i11", W, I, "Wat is het belangrijkste verschil tussen een eis en een gunningscriterium in een aanbestedingsdocument?",
   ["Er is geen verschil", "Een eis is knock-out (wel of niet voldoen), op een gunningscriterium kun je meer of minder scoren", "Gunningscriteria zijn altijd knock-out", "Eisen gaan alleen over de prijs"], 1,
   "Eisen (zoals geschiktheidseisen of minimumeisen in het PvE) leiden bij niet-voldoen tot uitsluiting. Gunningscriteria bepalen de rangorde tussen inschrijvingen die aan de eisen voldoen.")
mc("ir4-i12", W, I, "De opdrachtgever wil vooral innovatie in de werkplekdienstverlening, maar gunt op laagste prijs. Wat is de kritiek?",
   ["Geen kritiek, laagste prijs stimuleert innovatie", "De gunningsmethode past niet bij het doel: op laagste prijs heeft een leverancier geen prikkel om met innovatie te scoren", "Laagste prijs is verboden", "Innovatie mag geen doel zijn bij publieke inkoop"], 1,
   "Als kwaliteit of innovatie het doel is, moet dat terugkomen in de gunningscriteria, bijvoorbeeld via BPKV of Best Value. Anders wint gewoon de goedkoopste.")

# ---------- Recht MC ----------
mc("ir4-r01", W, R, "Wat is het kenmerkende verschil tussen de openbare en de niet-openbare procedure?",
   ["De openbare procedure kent twee fasen, de niet-openbare één", "Bij de openbare procedure dien je kwalificatiegegevens en inschrijving in één keer in; de niet-openbare kent een selectiefase en een inschrijvingsfase", "De niet-openbare procedure mag alleen onder de drempel", "Bij de openbare procedure wordt niet gepubliceerd"], 1,
   "De openbare procedure (art. 2.26 Aw) bestaat uit één fase. De niet-openbare (art. 2.27 Aw) selecteert eerst gegadigden, die daarna als inschrijvers een offerte mogen doen.")
mc("ir4-r02", W, R, "Hoeveel gegadigden moet een aanbestedende dienst minimaal selecteren bij de niet-openbare procedure (als er genoeg geschikte zijn)?",
   ["2", "3", "5", "10"], 2,
   "Minimaal 5 (art. 2.99 lid 3 Aw). Bij de concurrentiegerichte dialoog en de mededingingsprocedure met onderhandeling is dat 3. Volgens Nord-Pas-de-Calais mag je niet bij voorbaat beperken tot precies 5.")
mc("ir4-r03", W, R, "Er zijn zeer veel potentiële inschrijvers voor een levering van computers. Welke procedure adviseer je volgens het oefenmateriaal?",
   ["Openbare procedure, dan krijg je de meeste concurrentie", "Niet-openbare procedure, omdat je het aantal inschrijvers in de selectiefase kunt beperken", "Concurrentiegerichte dialoog", "Onderhandelingsprocedure zonder aankondiging"], 1,
   "Met de niet-openbare procedure houd je het beheersbaar: je selecteert minimaal 5 gegadigden (art. 2.27 jo. 2.99 lid 3 Aw). Bij de openbare procedure weet je vooraf niet hoeveel inschrijvingen je moet beoordelen.")
mc("ir4-r04", W, R, "Mag een gemeente in het bestek eisen dat de laptops 'van het merk HP' zijn?",
   ["Ja, als de medewerkers tevreden zijn over HP", "Nee, behalve als een nauwkeurige omschrijving zonder merk niet mogelijk is en er 'of gelijkwaardig' bij staat (art. 2.76 lid 3 en 4 Aw)", "Ja, bij leveringen mag dat altijd", "Nee, ook niet met 'of gelijkwaardig'"], 1,
   "Een merk eisen is in principe verboden. Alleen als het onderwerp anders niet nauwkeurig te beschrijven is, mag het met de toevoeging 'of gelijkwaardig'. Laptops kun je prima functioneel omschrijven.")
mc("ir4-r05", W, R, "Welk arrest bepaalt dat je in de selectiefase geen gunningscriteria mag gebruiken?",
   ["Commissie/Italië (C-362/90)", "Pressetext", "Vestergaard", "Telaustria"], 0,
   "Selectie gaat over de ondernemer, gunning over de inschrijving. Die mogen niet door elkaar lopen (Commissie/Italië, en eerder al Beentjes voor de openbare procedure).")
mc("ir4-r06", W, R, "Voor welke situatie is de concurrentiegerichte dialoog bedoeld?",
   ["Voor eenvoudige standaardleveringen", "Voor zeer complexe opdrachten waarbij het objectief onmogelijk is vooraf te bepalen welke middelen of oplossingen nodig zijn", "Voor alle opdrachten onder de drempel", "Voor dwingende spoed"], 1,
   "De dialoog (art. 2.28 Aw) is voor complexe trajecten, zoals grote infrastructuur of computernetwerken. De dienst stelt samen met marktpartijen oplossingen vast, daarna doet elke inschrijver één aanbieding waarover niet meer wordt onderhandeld.")
mc("ir4-r07", W, R, "Wat betekent 'geen cherry picking' bij de dialoog en de mededingingsprocedure met onderhandeling?",
   ["Je mag niet de goedkoopste kiezen", "Je mag ideeën of oplossingen van de ene inschrijver niet aan een andere inschrijver geven", "Je mag maar één inschrijver uitnodigen", "Je mag de procedure niet afbreken"], 1,
   "Vertrouwelijkheid: oplossingen van de ene deelnemer mag je niet doorspelen aan een andere. Dat zou het gelijkheidsbeginsel en het bedrijfsgeheim schenden.")
mc("ir4-r08", W, R, "Een dijk breekt door en er moet direct worden gerepareerd. Welke procedure mag het waterschap gebruiken?",
   ["Alleen de openbare procedure", "Onderhandelingsprocedure zonder voorafgaande bekendmaking wegens dwingende spoed (art. 2.32 lid 1 sub c Aw)", "Concurrentiegerichte dialoog", "Een prijsvraag"], 1,
   "Dwingende spoed: niet te voorzien, niet aan de dienst zelf te wijten, en de wettelijke termijnen zijn niet haalbaar. De latere dijkverhoging is geen dwingende spoed meer.")
mc("ir4-r09", W, R, "Een gemeente wijst de verliezers af en sluit de volgende dag het contract met de winnaar. Wat is er mis?",
   ["Niets", "De standstill- of Alcatel-termijn van 20 dagen (art. 2.127 lid 3 Aw) is niet in acht genomen", "De gemeente had eerst de ACM moeten inlichten", "De winnaar had eerst een kort geding moeten aanspannen"], 1,
   "Na de gunningsbeslissing moet de dienst 20 dagen wachten, zodat verliezers naar de kortgedingrechter kunnen. Daarna is alleen nog een bodemprocedure mogelijk.")
mc("ir4-r10", W, R, "Wat kan een afgewezen inschrijver vorderen als het contract al in strijd met de standstill is gesloten?",
   ["Alleen een excuus", "In een bodemprocedure onder meer vernietiging of ongedaanmaking van de overeenkomst (art. 4.15 e.v. Aw) en schadevergoeding (art. 6:162 BW)", "Alleen een herbeoordeling door de ACM", "Niets, een gesloten contract is definitief"], 1,
   "De rechter kan een overeenkomst vernietigen als die in strijd met de standstill of zonder verplichte aankondiging is gesloten. Daarnaast kan schadevergoeding uit onrechtmatige daad worden gevorderd.")
mc("ir4-r11", W, R, "Wat kan de ACM doen als de rechter een onrechtmatig gesloten overeenkomst niet vernietigt?",
   ["Niets", "Een boete opleggen van maximaal 15% van de waarde van de opdracht (art. 4.21 Aw)", "De gemeente opheffen", "De winnaar uitsluiten van toekomstige opdrachten"], 1,
   "Art. 4.21 Aw geeft de ACM de bevoegdheid tot een boete van maximaal 15% van de opdrachtwaarde.")
mc("ir4-r12", W, R, "Welke rechtsbescherming geldt bij een opdracht onder de Europese drempel?",
   ["Geen enkele", "Analoge toepassing van de rechtsbeschermingsregels via de ABBB en het fair-playbeginsel, met onder meer een Alcatel-termijn van 15 dagen", "Precies dezelfde als boven de drempel, met 20 dagen", "Alleen een klacht bij de Europese Commissie"], 1,
   "Volgens de slides worden de regels naar analogie toegepast bij opdrachten onder de drempel en uitgezonderde opdrachten, met een Alcatel-termijn van 15 dagen.")

# ---------- Open vragen ----------
op("ir4-io1", W, I, "Je beoordeelt een gepubliceerde Europese aanbesteding op de vraag 'is deze eerlijk en toegankelijk voor bedrijven?'. Noem vier concrete punten waar je in de documenten naar kijkt en waarom.",
   "1. De geschiktheidseisen (omzet, referenties, certificaten): zijn ze proportioneel of sluiten ze kleine bedrijven onnodig uit? 2. De gunningscriteria en wegingen: zijn ze vooraf duidelijk en objectief? 3. De opdeling in percelen: kan het mkb meedoen? 4. De duidelijkheid van het programma van eisen en de beoordelingssystematiek: begrijpen inschrijvers wat ze moeten aanbieden? Ook goed: de inschrijftermijn, de verhouding prijs/kwaliteit en de nota van inlichtingen.",
   ["Vier relevante punten uit de documenten", "Bij elk punt een uitleg gekoppeld aan eerlijkheid of toegankelijkheid", "Koppeling met een beginsel (proportionaliteit, transparantie, gelijkheid)"])
op("ir4-io2", W, I, "Reageer onderbouwd op de stelling 'Europese aanbestedingen bevoordelen grote bedrijven'. Geef een argument voor, een argument tegen en je eigen conclusie.",
   "Voor: grote bedrijven hebben tenderafdelingen, kunnen aan hoge omzet- en referentie-eisen voldoen en kunnen grote clusters aan. Tegen: de wet beschermt het mkb met het clusterverbod en de percelenregeling (art. 1.5 Aw), de Gids Proportionaliteit en de beperking van administratieve lasten (art. 1.6 Aw). Conclusie: de regels zijn bedoeld om toegang te geven, maar het hangt van de keuzes van de aanbestedende dienst af of dat in de praktijk lukt.",
   ["Argument voor", "Argument tegen met verwijzing naar regels voor mkb", "Eigen onderbouwde conclusie"])
op("ir4-io3", W, I, "Je stelt zelf een aanbesteding op voor de catering van een hogeschool. Noem drie keuzes die je maakt om die eerlijk en toegankelijk te houden, en licht toe.",
   "Bijvoorbeeld: (1) percelen per locatie of per soort dienst (restaurant, vending, evenementen), zodat ook kleinere cateraars kunnen meedoen; (2) proportionele geschiktheidseisen volgens de Gids Proportionaliteit, bijvoorbeeld een omzeteis van hooguit drie keer de perceelwaarde en een beperkt aantal referenties; (3) heldere gunningscriteria met wegingen en een beoordelingssystematiek die vooraf bekend zijn, met kwaliteit zwaar gewogen; (4) een ruime termijn en een marktconsultatie vooraf.",
   ["Drie concrete keuzes", "Elke keuze onderbouwd met eerlijkheid of toegankelijkheid"])
op("ir4-ro1", W, R, "Geef twee voordelen en twee nadelen van de openbare procedure ten opzichte van de niet-openbare procedure.",
   "Voordelen: kortere doorlooptijd, minder bewerkelijk omdat je maar één keer evalueert, lagere aanbestedingskosten, en lagere juridische risico's omdat je maar één keer afwijst. Nadelen: het aantal inschrijvingen is ongewis en het proces is daardoor minder beheersbaar, je kunt het aantal inschrijvers niet vooraf inperken, je kunt pas beginnen als alle documenten klaar zijn, en iedereen die erom vraagt krijgt de documenten.",
   ["Twee juiste voordelen", "Twee juiste nadelen"])
op("ir4-ro2", W, R, "Wanneer mag een aanbestedende dienst de onderhandelingsprocedure zonder voorafgaande bekendmaking gebruiken? Noem drie gronden en leg dwingende spoed uit met een voorbeeld.",
   "Art. 2.32 Aw: (1) er kwamen geen of geen geschikte inschrijvingen bij een openbare of niet-openbare procedure; (2) de opdracht kan om technische of artistieke redenen of door uitsluitende rechten maar door één ondernemer worden uitgevoerd; (3) dwingende spoed. Dwingende spoed vereist een gebeurtenis die de dienst niet kon voorzien, die niet aan de dienst zelf te wijten is, en waardoor de wettelijke termijnen niet haalbaar zijn. Voorbeeld: een dijkdoorbraak waarbij direct levensreddend werk nodig is. Een latere dijkverhoging is geen dwingende spoed.",
   ["Drie juiste gronden", "Drie voorwaarden van dwingende spoed", "Passend voorbeeld met grens (doorbraak ja, verhoging nee)"])
op("ir4-ro3", W, R, "Leg uit wat een afgewezen inschrijver in kort geding en in een bodemprocedure kan vorderen, en waarom de Alcatel-termijn belangrijk is.",
   "Kort geding: een bevel of verbod, zoals een verbod om te gunnen, een bevel tot staking van de procedure, een (marginaal getoetste) herbeoordeling of heraanbesteding, of een voorschot op schadevergoeding. Bodemprocedure: vernietiging of nietigverklaring van een beslissing, een verklaring voor recht, een bevel of verbod op straffe van een dwangsom, schadevergoeding (art. 6:162 BW) en ongedaanmaking of vernietiging van een overeenkomst (art. 4.15 e.v. en 4.18 Aw). De Alcatel-termijn van 20 dagen (art. 2.127 Aw) geeft verliezers de tijd een kort geding te starten voordat het contract wordt gesloten. Daarna rest alleen de bodemprocedure.",
   ["Vorderingen in kort geding", "Vorderingen in de bodemprocedure", "Functie van de Alcatel-termijn"])

# ---------- Casussen ----------
cs("ir4-ic1", W, I, "De aanbestedingsrechtbank: beveiliging Gemeente Zwolle",
   "Uit een (fictieve) aankondiging op TenderNed:\n'De Gemeente Zwolle besteedt de beveiliging van al haar 14 locaties aan in één perceel, looptijd 4 jaar, geraamde waarde €2,4 miljoen. Geschiktheidseisen: minimale gemiddelde jaaromzet €15 miljoen over de laatste drie jaar; vijf referenties van gemeenten met meer dan 100.000 inwoners; ISO 9001-certificaat. Gunning: laagste prijs. Inschrijftermijn: 35 dagen, van 10 juli tot 14 augustus.'",
   [("Wat wordt er ingekocht, door wie, en hoe wordt de winnaar gekozen?",
     "Beveiliging van 14 locaties voor 4 jaar door de Gemeente Zwolle (een aanbestedende dienst, categorie 1), voor €2,4 miljoen. Gunning op laagste prijs: alleen de prijs bepaalt wie wint.",
     ["Wat en wie juist", "Gunning op laagste prijs benoemd"]),
    ("Beoordeel of deze aanbesteding eerlijk en toegankelijk is. Gebruik minstens drie concrete voorbeelden uit de tekst.",
     "Niet erg toegankelijk. (1) Eén perceel voor 14 locaties sluit regionale beveiligers uit; percelen per regio zouden beter passen (art. 1.5 Aw). (2) Een omzeteis van €15 miljoen is ruim 25 keer de jaarwaarde (€600.000) en dus disproportioneel; de Gids Proportionaliteit gaat uit van veel minder. (3) Vijf referenties van grote gemeenten is zwaar en beperkt het aantal bedrijven dat kan meedoen. (4) De termijn valt in de zomervakantie. (5) Laagste prijs zegt weinig over de kwaliteit van beveiliging, terwijl die cruciaal is.",
     ["Minstens drie concrete voorbeelden uit de tekst", "Gekoppeld aan proportionaliteit, clusterverbod of toegankelijkheid voor het mkb", "Duidelijk eindoordeel"]),
    ("Wat zou je als adviseur anders doen? Noem twee verbeteringen.",
     "Bijvoorbeeld: opdelen in percelen per regio; proportionele omzeteis (bijvoorbeeld maximaal drie keer de perceelwaarde) en minder of algemenere referenties; gunnen op BPKV met kwaliteitscriteria zoals opleiding van beveiligers, reactietijden en een plan van aanpak; een langere termijn buiten de vakantie.",
     ["Twee concrete, onderbouwde verbeteringen"])])
cs("ir4-rc1", W, R, "Laptops voor de gemeente Nijmegen",
   "De gemeente Nijmegen wil nieuwe computers en laptops voor haar medewerkers. Totale waarde €280.000 ex btw: €260.000 voor de levering en €20.000 voor training van medewerkers. Uit een marktverkenning blijkt dat er zeer veel potentiële inschrijvers zijn. De medewerkers waren erg tevreden over HP en willen opnieuw HP.",
   [("Is dit een aanbestedingsplichtige opdracht, en is het een levering of een dienst? Gebruik de drie W's.",
     "Wie: de gemeente is een territoriaal lichaam (art. 1.1 Aw). Wat: een combinatie van levering en dienst; daarbij beslist de hoogste waarde (art. 2.12a lid 2 Aw), dus een levering. Waarde: €280.000 in totaal (art. 2.15 lid 2 Aw), boven de €216.000. Conclusie: Europees aanbestedingsplichtig.",
     ["Wie juist", "Wat: levering op basis van de hoogste waarde", "Waarde boven de drempel, conclusie"]),
    ("Welke procedure adviseer je, en mag de gemeente HP eisen?",
     "De niet-openbare procedure, omdat je bij zeer veel gegadigden in de selectiefase kunt beperken tot minimaal 5 (art. 2.27 jo. 2.99 lid 3 Aw). Een merk eisen mag in principe niet (art. 2.76 lid 3 Aw). Het mag alleen als een nauwkeurige omschrijving zonder merk niet mogelijk is én met 'of gelijkwaardig' (lid 4). Laptops zijn functioneel te omschrijven, dus HP eisen mag niet (vgl. Vestergaard).",
     ["Niet-openbare procedure met reden en artikel", "Merkeis niet toegestaan, art. 2.76 lid 3 en 4"]),
    ("De gemeente wil na de afwijzing van de verliezers meteen het contract tekenen. Wat adviseer je en wat zijn de risico's?",
     "Niet doen. Eerst de standstilltermijn van 20 dagen afwachten (art. 2.127 lid 3 Aw), met een gemotiveerde afwijzing (art. 2.130 Aw). Anders kan een afgewezen inschrijver in een bodemprocedure vernietiging van de overeenkomst vorderen (art. 4.15 Aw) en schadevergoeding eisen. Vernietigt de rechter niet, dan kan de ACM een boete opleggen van maximaal 15% van de opdrachtwaarde (art. 4.21 Aw).",
     ["Standstill 20 dagen", "Risico vernietiging/schadevergoeding", "Risico ACM-boete max 15%"])])
cs("ir4-rc2", W, R, "Nieuw campusconcept voor een universiteit",
   "Een universiteit wil een volledig nieuw 'campus-as-a-service'-concept: werkplekken, catering, schoonmaak, beveiliging en energie in één slim, flexibel model met een innovatieve financieringsconstructie. De universiteit weet nog niet welke technische oplossingen en juridische constructie het beste zijn. Ze wil marktpartijen laten meedenken, maar is bang dat de beste ideeën van één partij bij een andere terechtkomen.",
   [("Welke procedure past het best? Onderbouw met de kenmerken uit de wet.",
     "De concurrentiegerichte dialoog (art. 2.28 Aw). De opdracht is zeer complex en het is objectief niet mogelijk vooraf te bepalen welke middelen en oplossingen nodig zijn, ook financieel en juridisch. In de dialoog stelt de universiteit samen met marktpartijen het programma van eisen en de oplossingen vast. Een verdedigbaar alternatief is de mededingingsprocedure met onderhandeling (art. 2.30 Aw), waarbij eerst wordt ingeschreven en dan onderhandeld.",
     ["Concurrentiegerichte dialoog gekozen", "Onderbouwd met complexiteit en het niet vooraf kunnen bepalen van de oplossing"]),
    ("Hoe wordt de zorg van de universiteit over de ideeën van marktpartijen geregeld?",
     "Geen cherry picking: de dienst mag oplossingen of vertrouwelijke informatie van de ene deelnemer niet aan andere deelnemers doorgeven. Vertrouwelijkheid is een uitdrukkelijk aandachtspunt van de dialoog.",
     ["Verbod op cherry picking / vertrouwelijkheid juist uitgelegd"]),
    ("Hoeveel gegadigden moet de universiteit minimaal uitnodigen, en wat gebeurt er na de dialoogfase?",
     "Minimaal 3 (art. 2.99 lid 3 Aw), tegenover 5 bij de niet-openbare procedure. Na de dialoog doet elke deelnemer één definitieve inschrijving waarover niet meer mag worden onderhandeld. Er wordt gegund op de economisch meest voordelige inschrijving op basis van de beste prijs-kwaliteitverhouding.",
     ["Minimaal 3", "Eén definitieve inschrijving zonder onderhandeling", "Gunning op BPKV/EMVI"])])
