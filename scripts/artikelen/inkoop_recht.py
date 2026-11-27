# Wetsartikelen recht (Inkoop en recht), recht week 1 t/m 7: aanbestedingsrecht en vervolg verbintenissenrecht.
# Alleen artikelen die in de samenvattingen (scripts/samenvattingen/inkoop-recht/, de delen "Recht week N") of de slides
# "Week N Recht" en het oefenmateriaal staan. De inhoud is een korte weergave van wat daar staat; niets erbij verzonnen.
# let=... is een waarschuwing: verschil tussen slide, antwoordmodel en wet, of iets dat je zelf moet nalezen.
# WETTEN: (code, volledige naam, korte naam voor de inhoudsopgave).
# Velden: A(wet, nummer, titel, inhoud, weken, let=None). Weken = recht week N.

TITEL = "Wetsartikelen recht"
LEAD = ("Alle wetsartikelen uit de rechtlessen (week 1 t/m 7): eerst de Aanbestedingswet, daarna het Burgerlijk Wetboek en de Europese "
        "regels, per wet op volgorde en met in het kort wat erin staat. Gebaseerd op de samenvattingen, de slides en het oefenmateriaal. "
        "De wettenbundel blijft leidend.")

WETTEN = [
    ("Aw1", "Aanbestedingswet 2012, deel 1: definities en beginselen", "Aw deel 1"),
    ("Aw2", "Aanbestedingswet 2012, deel 2: overheidsopdrachten boven de drempel", "Aw deel 2"),
    ("Aw2A", "Aanbestedingswet 2012, deel 2A: concessies", "Aw deel 2A"),
    ("Aw4", "Aanbestedingswet 2012, deel 4: rechtsbescherming en toezicht", "Aw deel 4"),
    ("BW", "Burgerlijk Wetboek: overeenkomsten, algemene voorwaarden, koop en eigendom", "BW"),
    ("EU", "Europese en internationale regels", "Europees"),
]

ARTIKELEN = []
def A(wet, nr, titel, inhoud, weken, let=None):
    ARTIKELEN.append(dict(wet=wet, nr=nr, titel=titel, inhoud=inhoud, weken=weken, let=let))

# ---------------------------------------------------------------- Aw deel 1
A("Aw1", "1.1", "Definities",
  "Wie aanbestedingsplichtig is: overheden (de Staat, territoriale lichamen, samenwerkingsverbanden), publiekrechtelijke instellingen "
  "(cumulatief: algemeen belang niet van industriële of commerciële aard, rechtspersoonlijkheid en overheidsinvloed via financiering (a), "
  "toezicht (b) of benoeming van meer dan de helft van het bestuur (c)) en aankoopcentrales. Ook de definities van overheidsopdracht "
  "(schriftelijk, onder bezwarende titel, tussen ondernemer en aanbestedende dienst), ondernemer, werk, levering, dienst en concessie "
  "(exploitatie voor eigen risico).", [2, 3, 4, 7])
A("Aw1", "1.4", "Objectiviteit en maatschappelijke waarde",
  "Lid 1: de dienst kiest de procedure en de toegelaten ondernemers op basis van objectieve criteria. Lid 2: streven naar maatschappelijke "
  "waarde. Lid 3: de keuze voor een procedure op verzoek motiveren.", [1, 4, 7])
A("Aw1", "1.5", "Clusterverbod en percelen",
  "Lid 1: opdrachten niet onnodig samenvoegen (clusterverbod). Lid 3: percelen (op de slide \"percelenregeling, wordt later behandeld\").", [1])
A("Aw1", "1.6", "Administratieve lasten", "Beperking van de administratieve lasten voor ondernemers.", [1])
A("Aw1", "1.8", "Gelijkheid en non-discriminatie",
  "Ondernemers op gelijke wijze behandelen, en geen onderscheid naar nationaliteit (direct of indirect). Bijvoorbeeld: met één inschrijver "
  "over de prijs onderhandelen is in strijd met gelijkheid (oefentoets vraag 5a).", [1, 7])
A("Aw1", "1.9", "Transparantie",
  "Passende openbaarheid vooraf, duidelijke criteria tijdens en motivering van de gunning achteraf. Doel: controleren of gelijkheid en "
  "non-discriminatie worden nageleefd.", [1])
A("Aw1", "1.10", "Evenredigheid (proportionaliteit)",
  "Lid 1: eisen, voorwaarden en criteria staan in een redelijke verhouding tot het voorwerp van de opdracht. Lid 3 en 4: de Gids "
  "proportionaliteit (pas toe of leg uit). Bijvoorbeeld: ondernemingen met een onderlinge afhankelijkheidsrelatie per definitie uitsluiten "
  "(oefentoets vraag 5b).", [1, 7])
A("Aw1", "1.18", "Aankondigen via TenderNed", "Een aanbestedingsplichtige opdracht wordt aangekondigd via TenderNed.", [1, 2])

# ---------------------------------------------------------------- Aw deel 2
A("Aw2", "2.1", "Drempel werken", "Drempel voor werken: €5.404.000 (per 1 januari 2026). De Aw verwijst naar art. 4 van richtlijn 2014/24.", [3])
A("Aw2", "2.2", "Drempel centrale overheid", "Leveringen en diensten door de staat (centrale overheid): €140.000.", [3])
A("Aw2", "2.3", "Drempel andere aanbestedende diensten",
  "Leveringen en diensten door andere aanbestedende diensten (gemeenten, provincies, waterschappen, publiekrechtelijke instellingen): €216.000.", [3, 4, 7])
A("Aw2", "2.6a", "Drempel sociale en specifieke diensten", "Sociale en andere specifieke diensten: €750.000.", [3])
A("Aw2", "2.7", "Nieuwe drempels", "Een nieuwe drempel geldt vanaf het besluit van de Europese Commissie (die stelt ze elke twee jaar opnieuw vast).", [3])
A("Aw2", "2.8", "Gesubsidieerde instellingen",
  "Meer dan 50% subsidie van een aanbestedende dienst voor een werk (of een dienst die daarmee verband houdt) boven de drempel: dan moet "
  "worden aanbesteed. Niet voor leveringen. De subsidieverlener ziet toe op de naleving.", [2, 3])
A("Aw2", "2.12a", "Gemengde opdrachten",
  "Lid 1: een gemengde opdracht volgt de regels van het hoofdvoorwerp (wat is essentieel, wat bijkomstig). Lid 2: bij diensten + sociale "
  "diensten en bij leveringen + diensten beslist de hoogste geraamde waarde.", [2, 4, 7])
A("Aw2", "2.13 t/m 2.22", "Raming van de waarde", "De regels voor het ramen van de waarde van een opdracht.", [3])
A("Aw2", "2.14", "Splitsingsverbod", "Een opdracht niet opsplitsen om onder de drempel te blijven.", [3])
A("Aw2", "2.15", "Totale waarde",
  "Lid 2: het totale bedrag excl. btw, inclusief opties en verlengingen. Lid 3: bij een raamovereenkomst de waarde van alle opdrachten die je "
  "voor de hele looptijd verwacht.", [3, 4, 7])
A("Aw2", "2.17", "Waarde van diensten",
  "Sub d: looptijd van 48 maanden of korter: de totale waarde voor de hele looptijd. Sub e: zonder totale prijs, met onbepaalde duur of langer "
  "dan 48 maanden: het maandbedrag × 48.", [3],
  let="De slide vat sub e samen als \"overeenkomst van 4 jaar of langer: berekening op basis van 4 jaar\". De wet is preciezer, zie de inhoud.")
A("Aw2", "2.18", "Percelen",
  "Bij percelen tel je de waarde van alle percelen samen. Percelenregeling: werken ≤ €1.000.000 per perceel en leveringen en diensten "
  "≤ €80.000 per perceel mogen zonder Europese aanbesteding, samen maximaal 20% van de totale waarde.", [2, 3])
A("Aw2", "2.19", "Percelenregeling", "Hoort bij art. 2.18: de percelenregeling voor leveringen en diensten.", [2])
A("Aw2", "2.23", "Uitgezonderde opdrachten",
  "Onder meer leveringen onder art. 346 VWEU, echte defensieopdrachten (niet wat ook civiel bruikbaar is) en geheime opdrachten.", [2])
A("Aw2", "2.24", "Andere uitzonderingen",
  "Onder meer alleenrecht voor diensten, verwerven of huren van onroerende zaken, arbitrage en bemiddeling, onderzoeksopdrachten en "
  "arbeidsovereenkomsten.", [2])
A("Aw2", "2.24a", "(Quasi-)inbesteden",
  "Opdracht aan een eigen rechtspersoon mag zonder aanbesteding als de dienst er toezicht op houdt als op een eigen dienst, meer dan 80% van de "
  "werkzaamheden voor die dienst is en er geen directe participatie van particulier kapitaal is.", [2])
A("Aw2", "2.24b", "Publiek-publieke samenwerking met rechtspersoon",
  "Via een gezamenlijke rechtspersoon: gezamenlijk toezicht, de 80%-eis en geen particulier kapitaal.", [2])
A("Aw2", "2.24c", "Publiek-publieke samenwerking zonder rechtsvorm",
  "Samenwerking voor verplichte openbare diensten in het openbaar belang, waarbij de diensten maximaal 20% van die activiteiten op de open "
  "markt verrichten (Stadtreinigung Hamburg; casus Lansingerland).", [2])
A("Aw2", "2.25", "Openbare of niet-openbare procedure", "Het wettelijk kader: de dienst kiest de openbare of de niet-openbare procedure.", [4])
A("Aw2", "2.26", "Stappen openbare procedure",
  "(a) aankondiging, (b) uitsluitingsgronden, (c) geschiktheidseisen, (d) technische specificaties, (e) beoordelen op het gunningscriterium, "
  "(f) proces-verbaal, (g) gunningsbeslissing meedelen, (h) overeenkomst sluiten, (i) aankondiging van de gegunde opdracht. Selectiecriteria "
  "staan er niet in.", [4, 7])
A("Aw2", "2.27", "Stappen niet-openbare procedure", "Twee fasen: eerst selectie (minimaal 5 gegadigden), dan inschrijving.", [4])
A("Aw2", "2.28", "Concurrentiegerichte dialoog",
  "Lid 1 sub a en b: alleen in strikt omschreven gevallen, voor zeer complexe opdrachten. Lid 3 en 4: ook na onregelmatige (afgestemd, niet aan "
  "de essentiële voorwaarden) of onaanvaardbare (ver boven budget, niet geschikt) inschrijvingen, zonder de opdracht fundamenteel te wijzigen.", [4])
A("Aw2", "2.29", "Verloop concurrentiegerichte dialoog", "Sub i: gunnen op beste prijs-kwaliteitverhouding (antwoordmodel oefentoets).", [4, 7])
A("Aw2", "2.30", "Mededingingsprocedure met onderhandeling",
  "Lid 1: in dezelfde gevallen als de concurrentiegerichte dialoog (art. 2.28 lid 1 sub a en b). Eerst inschrijven, dan onderhandelen. "
  "Gunnen op laagste prijs mag hier wel.", [4, 7])
A("Aw2", "2.31a", "Innovatiepartnerschap", "Procedure van het innovatiepartnerschap. Alleen genoemd op de slide.", [4])
A("Aw2", "2.32", "Onderhandelingsprocedure zonder aankondiging",
  "Lid 1 sub a: geen (geschikte) inschrijvingen bij een openbare of niet-openbare procedure. Sub b: maar één ondernemer kan het (technische of "
  "artistieke redenen, uitsluitende rechten). Sub c: dwingende spoed door een onvoorzienbare gebeurtenis die niet aan de dienst te wijten is "
  "(dijkdoorbraak wel, dijkverhoging daarna niet).", [4])
A("Aw2", "2.33 t/m 2.36", "Overige gronden", "Overige gronden voor de onderhandelingsprocedure zonder aankondiging.", [4])
A("Aw2", "2.37", "Procedure zonder aankondiging",
  "Onderhandelen, proces-verbaal, gunningsbeslissing meedelen, overeenkomst sluiten en de gegunde opdracht aankondigen met de reden voor deze procedure.", [4])
A("Aw2", "2.38", "Sociale en specifieke diensten",
  "Boven €750.000 een licht regime: aankondiging, technische specificaties, toetsing inschrijvers, proces-verbaal, overeenkomst sluiten en "
  "de gegunde opdracht publiceren.", [2])
A("Aw2", "2.39", "Sociale en specifieke diensten", "Hoort bij art. 2.38: het lichte regime.", [2])
A("Aw2", "2.42", "Prijsvraag", "De prijsvraag. Alleen genoemd op de slide.", [4])
A("Aw2", "2.44", "Raamovereenkomst",
  "Legt voor een periode de voorwaarden vast voor later te gunnen opdrachten (prijs, hoeveelheid). Te plaatsen via de openbare en niet-openbare "
  "procedure, de concurrentiegerichte dialoog, de mededingingsprocedure met onderhandeling, de onderhandelingsprocedure zonder aankondiging, het "
  "innovatiepartnerschap en de procedure voor sociale en specifieke diensten (oefentoets vraag 3).", [2, 4, 7])
A("Aw2", "2.48", "Dynamisch aankoopsysteem", "Het dynamisch aankoopsysteem; wordt in Nederland zelden gebruikt.", [4])
A("Aw2", "2.66", "Stukken elektronisch beschikbaar", "Voorbeeld van een grond om de termijn te verlengen (volgens de slide +5 dagen).", [4])
A("Aw2", "2.71", "Minimumtermijnen",
  "Lid 1: openbare procedure 45 dagen. Lid 2: verzoeken tot deelneming 30 dagen. Lid 3: concurrentiegerichte dialoog 30 dagen. Lid 4: "
  "inschrijvingen na selectie 40 dagen. Lid 5: met een vooraankondiging verkorten tot 29 dagen, nooit minder dan 22 (voorwaarden in lid 6).", [4, 7])
A("Aw2", "2.72", "Verlengen van termijnen", "Onder voorwaarden verlengen (samen met art. 2.73).", [4])
A("Aw2", "2.73", "Verlengen van termijnen", "Hoort bij art. 2.72.", [4])
A("Aw2", "2.74", "Verkorten bij urgentie",
  "Bij een naar behoren onderbouwde urgente situatie, niet te wijten aan de dienst zelf: 15 dagen voor inschrijvingen (openbaar), 15 dagen voor "
  "verzoeken tot deelneming en 10 dagen voor inschrijvingen (niet-openbaar en mededingingsprocedure). Bijvoorbeeld als de leverancier failliet gaat.", [4, 7])
A("Aw2", "2.74b", "Elektronisch inschrijven", "Termijn 5 dagen korter als elektronisch inschrijven mogelijk is.", [4])
A("Aw2", "2.75", "Technische specificaties", "Vanaf art. 2.75 de regels voor technische specificaties (met 2.76 en 2.77 ook wederzijdse erkenning).", [1, 3])
A("Aw2", "2.76", "Geen merk eisen",
  "Lid 3: geen merk, oorsprong of procedé eisen. Lid 4: alleen als een nauwkeurige omschrijving anders niet kan, en dan met \"of gelijkwaardig\" "
  "(casus HP-laptops). Lid 4 sub b ook genoemd bij wederzijdse erkenning.", [1, 3, 4])
A("Aw2", "2.77", "Gelijkwaardigheid", "Genoemd bij wederzijdse erkenning, samen met art. 2.75 en 2.76.", [1])
A("Aw2", "2.78a", "Keurmerken", "Lid 3 genoemd bij wederzijdse erkenning: gelijkwaardige keurmerken accepteren.", [1],
  let="De slide noemt alleen \"2.78a lid 3\" zonder uitleg; dat het om keurmerken gaat, staat niet op de slide. Lees het na.")
A("Aw2", "2.82", "Voorbehouden opdrachten",
  "Wel aanbesteden, maar alleen sociale werkplaatsen mogen inschrijven (minimaal 30% personeel met een beperking of kansarm).", [2])
A("Aw2", "2.84", "Beroepsbevoegdheid", "Bevoegdheid om het beroep uit te oefenen (handelsregister, vergunning), met een eigen verklaring.", [3])
A("Aw2", "2.86", "Dwingende uitsluitingsgronden", "Gronden waarop de dienst een ondernemer moet uitsluiten (bijvoorbeeld veroordeeld voor fraude of omkoping). Samen met 2.86a.", [3])
A("Aw2", "2.86a", "Dwingende uitsluitingsgronden", "Hoort bij art. 2.86 (\"moet\").", [3])
A("Aw2", "2.87", "Facultatieve uitsluitingsgronden",
  "Gronden waarop de dienst mag uitsluiten (\"mag\"). Lid 1 sub g: eerdere slechte prestaties; volgens de slide van week 1 het artikel bij "
  "objectiviteit (ervaringen uit het verleden).", [1, 3, 7])
A("Aw2", "2.88", "Afwijken van uitsluitingsgronden", "De dienst \"kan\" afwijken van art. 2.86 en 2.87.", [3])
A("Aw2", "2.89", "Bewijsstukken", "Bewijsstukken en verklaringen, ook voor buitenlandse inschrijvers.", [3])
A("Aw2", "2.90", "Geschiktheidseisen",
  "Financiële en economische draagkracht, technische bekwaamheid en beroepsbevoegdheid. Lid 3: een omzeteis alleen met zwaarwegende motivering. "
  "Lid 5 sub a: maximaal drie keer de geraamde waarde.", [1, 3, 7])
A("Aw2", "2.96", "Kwaliteitsnormen", "Eisen over kwaliteitsnormen.", [3])
A("Aw2", "2.97", "Milieunormen", "Eisen over milieunormen.", [3])
A("Aw2", "2.98", "Beroepsbevoegdheid", "Eisen over beroepsbevoegdheid.", [3])
A("Aw2", "2.99", "Selectie",
  "Lid 1: selectiecriteria en het beperken van het aantal gegadigden alleen bij twee-fasenprocedures (niet-openbaar, concurrentiegerichte dialoog, "
  "mededingingsprocedure met onderhandeling, innovatiepartnerschap). Lid 2: het aantal in de aankondiging. Lid 3: minimaal 5 bij niet-openbaar, "
  "3 bij de dialoog en de mededingingsprocedure.", [3, 4, 7])
A("Aw2", "2.110", "Gunning bij de concurrentiegerichte dialoog",
  "Lid 1: altijd op beste prijs-kwaliteitverhouding. Lid 6: gelijke behandeling tijdens de dialoog. Lid 7: geen cherry picking (oplossingen niet "
  "zonder instemming aan anderen doorgeven).", [4, 7])
A("Aw2", "2.114", "Gunningscriterium (EMVI)",
  "Lid 1: standaard de economisch meest voordelige inschrijving. Lid 2: op basis van beste prijs-kwaliteitverhouding (sub a), laagste kosten "
  "(sub b) of laagste prijs (sub c). Lid 3: uitgangspunt is beste prijs-kwaliteit. Lid 4: kies je laagste kosten of prijs, dan motiveer je dat.", [3, 4, 7])
A("Aw2", "2.115", "Gunningscriteria", "Lid 4: het relatieve gewicht van de gunningscriteria vermelden.", [3, 4])
A("Aw2", "2.116", "Abnormaal lage inschrijvingen", "Regels voor abnormaal lage inschrijvingen.", [3])
A("Aw2", "2.117", "Elektronische veiling", "Geen eigen procedure, maar onderdeel van een andere procedure.", [4])
A("Aw2", "2.127", "Opschortende termijn (Alcatel)",
  "Onder de drempel volgens de slide naar analogie 15 dagen. Lid 1: geen definitieve gunning en geen overeenkomst tijdens de termijn. Lid 2: te rekenen vanaf de dag na verzending van de mededeling. "
  "Lid 3: ten minste 20 kalenderdagen. Lid 4: uitzonderingen.", [3, 4, 7],
  let="Dat de standstill doorloopt tot de uitspraak in een kort geding (oefentoets vraag 8), staat niet in art. 2.127. Vraag de docent waarop dit is gebaseerd.")
A("Aw2", "2.130", "Mededeling gunningsbeslissing",
  "De relevante redenen (kenmerken en voordelen van de winnende inschrijving, naam van de winnaar) en een nauwkeurige omschrijving van de opschortende termijn.", [4])
A("Aw2", "2.132", "Proces-verbaal", "De inhoud van het proces-verbaal van de opdrachtverlening.", [7])
A("Aw2", "2.134", "Aankondiging gegunde opdracht", "Lid 1: binnen 30 dagen na de gunning via TenderNed.", [7])
A("Aw2", "2.140", "Looptijd raamovereenkomst",
  "Lid 3: maximaal vier jaar, behalve in deugdelijk gemotiveerde uitzonderingsgevallen. Lid 2: geen wezenlijke wijzigingen bij opdrachten op basis "
  "van een raamovereenkomst.", [2, 7],
  let="Het antwoordmodel van de oefentoets (vraag 2) noemt lid 2 voor de looptijd; volgens de wettekst is het lid 3, zoals op de slide.")
A("Aw2", "2.143", "Raamovereenkomst met meerdere ondernemers", "Lid 1: de uitvoering als er meer dan één ondernemer partij is.", [2])

# ---------------------------------------------------------------- Aw deel 2A
A("Aw2A", "2a.10", "Waarde van een concessie", "Lid 2: de waarde is de verwachte omzet excl. btw. Drempel €5.404.000.", [2])
A("Aw2A", "2a.13 t/m 2a.26", "Uitgezonderde concessies", "Concessies die niet onder de regels vallen, veelal gelijk aan de uitzonderingen bij gewone opdrachten.", [2])
A("Aw2A", "2a.27", "Looptijd concessie", "Maximaal vijf jaar, tenzij langer nodig om investeringen terug te verdienen.", [2])
A("Aw2A", "2a.30", "Procedure concessie",
  "Vormvrij, mits je de organisatie van de procedure beschrijft en de stappen documenteert. Onderhandelen mag zolang de criteria gelijk blijven.", [2])
A("Aw2A", "2a.33", "Aankondiging concessie", "Aankondigen via TenderNed (samen met art. 1.18).", [2])

# ---------------------------------------------------------------- Aw deel 4
A("Aw4", "4.15", "Vernietiging van de overeenkomst",
  "Lid 1: de rechter vernietigt een overeenkomst in strijd met het aanbestedingsrecht, onder meer zonder vereiste aankondiging (sub a) of zonder "
  "de opschortende termijn in acht te nemen (sub b).", [4])
A("Aw4", "4.18", "Afzien van vernietiging", "Lid 1: om dwingende redenen van algemeen belang kan de rechter van vernietiging afzien.", [4])
A("Aw4", "4.21", "Boete ACM", "Lid 1 en 4: vernietigt de rechter niet (art. 4.18), dan kan de ACM een boete opleggen van maximaal 15% van de geraamde waarde.", [4])

# ---------------------------------------------------------------- BW
A("BW", "2:3", "Stichting is een rechtspersoon", "Genoemd bij de HAN: een stichting heeft rechtspersoonlijkheid (voorwaarde publiekrechtelijke instelling).", [2])
A("BW", "2:360", "Openbare jaarrekening", "Rechtspersonen die hun jaarrekening openbaar maken; genoemd bij art. 6:235 lid 1 sub a.", [5])
A("BW", "3:33", "Wil en verklaring", "Een rechtshandeling vereist een op een rechtsgevolg gerichte wil die zich door een verklaring heeft geopenbaard.", [5])
A("BW", "3:35", "Vertrouwensbeginsel", "Wie een verklaring redelijkerwijs zo mocht opvatten, wordt beschermd als dat vertrouwen gerechtvaardigd is.", [5])
A("BW", "3:37", "Vormvrijheid", "Lid 1: verklaringen kunnen in iedere vorm worden gedaan, tenzij anders bepaald.", [5])
A("BW", "3:40", "Goede zeden en openbare orde", "Lid 1: een rechtshandeling in strijd met de goede zeden of de openbare orde is nietig (maatschappelijke aanvaardbaarheid).", [5])
A("BW", "3:84", "Eigendomsoverdracht",
  "Lid 1: drie voorwaarden: een geldige titel, beschikkingsbevoegdheid en levering. Betaling is geen voorwaarde.", [6, 7])
A("BW", "3:89", "Levering onroerende zaak", "Notariële akte en inschrijving in de openbare registers (Kadaster). Sleutels geven is niet genoeg (casus Draaier).", [6])
A("BW", "3:90", "Levering roerende zaak", "Levering van een roerende zaak door verschaffing van het bezit.", [6])
A("BW", "3:92", "Eigendomsvoorbehoud", "De verkoper blijft eigenaar tot er betaald is. Belangrijk bij faillissement; houd de zaken identificeerbaar.", [5, 6])
A("BW", "3:93", "Levering recht aan toonder", "Levering van een recht aan toonder. Alleen genoemd op de slide.", [6])
A("BW", "3:115", "Levering zonder feitelijke overdracht",
  "Sub a: constitutum possessorium (verkoper houdt de zaak voor de koper). Sub b: brevi manu (koper had de zaak al). Sub c: longa manu (een derde "
  "houdt de zaak voor de koper; pas na erkenning door de derde).", [6])
A("BW", "3:306", "Verjaring", "Hoofdregel 20 jaar; voor de meeste vorderingen is het anders bepaald (art. 3:306 e.v.), meestal 5 jaar.", [6])
A("BW", "6:3", "Natuurlijke verbintenis", "Na verjaring of verval is een recht niet meer afdwingbaar: een natuurlijke verbintenis.", [6])
A("BW", "6:38", "Tijd van nakoming", "Zonder afspraak moet direct (terstond) worden nagekomen.", [6])
A("BW", "6:41", "Plaats van nakoming", "Aflevering op het adres van de verkoper (samen met art. 7:9).", [6])
A("BW", "6:74", "Tekortkoming", "Niet nakomen is een tekortkoming (wanprestatie); vereist een overeenkomst. Pacta sunt servanda.", [5])
A("BW", "6:75", "Overmacht", "Geen toerekenbare tekortkoming bij overmacht. Regelend recht: AV breiden het eigen overmachtsbegrip vaak uit.", [5])
A("BW", "6:119", "Wettelijke rente", "Schadevergoeding bij te late betaling van een geldsom: de wettelijke rente.", [6])
A("BW", "6:162", "Onrechtmatige daad",
  "Grondslag voor schadevergoeding bij onrechtmatig afgebroken onderhandelingen (er is nog geen overeenkomst) en in de bodemprocedure bij aanbesteden.", [4, 5])
A("BW", "6:185", "Productaansprakelijkheid", "De producent is aansprakelijk voor schade door een gebrekkig product (ook verkopen aan een wederverkoper is in het verkeer brengen).", [6])
A("BW", "6:213", "Overeenkomst", "Definitie van de overeenkomst; bij afgebroken onderhandelingen is er nog geen overeenkomst.", [5])
A("BW", "6:217", "Aanbod en aanvaarding", "Lid 1: een overeenkomst komt tot stand door aanbod en aanvaarding (contractvrijheid).", [5])
A("BW", "6:225", "Battle of forms", "Lid 3: verwijzen beide partijen naar hun eigen AV, dan gelden die van wie het eerst verwijst, tenzij de ander ze uitdrukkelijk van de hand wijst.", [5])
A("BW", "6:227", "Bepaalbaarheid", "De verbintenissen moeten bepaalbaar zijn (vergelijk art. 7:4 voor de prijs).", [6])
A("BW", "6:230g", "Overeenkomst op afstand", "Definitie: consumentenkoop met alleen communicatie op afstand (samen met art. 6:230m).", [6])
A("BW", "6:230m", "Informatieplicht", "De verkoper op afstand moet de consument informeren.", [6])
A("BW", "6:230o", "Ontbindingsrecht koop op afstand", "14 dagen bedenktijd; tot 12 maanden als niet aan de informatieplicht is voldaan.", [6])
A("BW", "6:231", "Begrippen algemene voorwaarden",
  "Sub a: AV zijn schriftelijke bedingen voor meerdere overeenkomsten, behalve kernbedingen. Sub b: gebruiker. Sub c: wederpartij.", [5])
A("BW", "6:232", "Gebondenheid", "De wederpartij is gebonden, ook als zij de AV niet kende; de gebruiker verklaart ze voor of bij het sluiten van toepassing.", [5])
A("BW", "6:233", "Vernietigingsgronden",
  "Sub a: onredelijk bezwarend, gelet op alle omstandigheden. Sub b: geen redelijke mogelijkheid tot kennisneming gegeven.", [5, 7])
A("BW", "6:234", "Kennisneming",
  "De AV ter hand stellen uiterlijk bij het sluiten. Alleen als dat redelijkerwijs niet kan: verwijzen naar AV bij de KvK of de griffie. Eigen regeling voor elektronische overeenkomsten.", [5, 7])
A("BW", "6:235", "Wie geen beroep op 6:233 kan doen",
  "Lid 1 sub a: rechtspersonen die hun jaarrekening openbaar maken. Sub b: partijen met 50 of meer werkzame personen bij het sluiten van de "
  "overeenkomst. Zij kunnen alleen een beroep doen op art. 6:248 lid 2.", [5, 7],
  let="Het antwoordmodel van de oefentoets (vraag 12) schrijft \"6:235 sub b\"; bedoeld is lid 1 sub b.")
A("BW", "6:236", "Zwarte lijst", "Bedingen die bij een consument als onredelijk bezwarend gelden, zonder tegenbewijs (bijvoorbeeld uitsluiten van ontbinding, sub b).", [5])
A("BW", "6:237", "Grijze lijst", "Bedingen die bij een consument vermoed worden onredelijk bezwarend te zijn; tegenbewijs mag (bijvoorbeeld een wezenlijk andere prestatie, sub c).", [5])
A("BW", "6:244", "Beklemde detaillist", "Een detaillist mag niet vastzitten tussen ruimere aansprakelijkheid tegenover zijn klant en een exoneratie van zijn leverancier.", [5])
A("BW", "6:247", "Internationale aspecten AV",
  "Lid 1: twee zakelijke partijen in Nederland: de regeling geldt dwingend. Lid 2: een van beide niet in Nederland: niet dwingend. Lid 4: "
  "Nederlandse consument en buitenlandse gebruiker: dwingend.", [5])
A("BW", "6:248", "Redelijkheid en billijkheid", "Lid 1: aanvullende werking. Lid 2: beperkende werking (onaanvaardbaar); rechters nemen dat niet snel aan. Ook de toets voor exoneratieclausules.", [5, 7])
A("BW", "6:265", "Ontbinding", "De voorwaarden voor ontbinding; vereist voor het recht van reclame.", [6])
A("BW", "7:1", "Koop", "Wederkerige overeenkomst: een plicht tot leveren tegenover een plicht tot betalen.", [6])
A("BW", "7:2", "Koop van een woning", "Schriftelijk; de particuliere koper heeft drie dagen bedenktijd (lid 2). Geldt niet voor een zakelijke koper van een kantoorpand.", [6])
A("BW", "7:4", "Geen prijs afgesproken", "Dan is een redelijke prijs verschuldigd.", [6])
A("BW", "7:5", "Consumentenkoop", "Koop van een roerende zaak door een koper die niet handelt in beroep of bedrijf, van een verkoper die dat wel doet.", [6, 7])
A("BW", "7:6", "Dwingend recht bij consumentenkoop", "Lid 1: de regeling is bij consumentenkoop grotendeels dwingend. Lid 2: uitzonderingen. Bij andere koop regelend recht.", [6, 7])
A("BW", "7:6a", "Garantie bij consumentenkoop", "Naast een garantie houdt de consument al zijn wettelijke rechten; een negatieve garantie werkt niet.", [6])
A("BW", "7:7", "Ongevraagde toezending", "Regels voor ongevraagd toegezonden zaken. Alleen genoemd op de slide.", [6])
A("BW", "7:9", "Aflevering", "Lid 4: de termijn van dertig dagen geldt alleen bij consumentenkoop. Aflevering op het adres van de verkoper (jo. art. 6:41).", [6])
A("BW", "7:12", "Kosten van aflevering", "Lid 1: de kosten van aflevering zijn voor de verkoper.", [6])
A("BW", "7:17", "Conformiteit",
  "De zaak moet aan de overeenkomst beantwoorden en voldoen aan de redelijke verwachtingen van de koper, gelet op de aard en de mededelingen van de "
  "verkoper, ook voor normaal gebruik.", [6, 7])
A("BW", "7:18", "Mededelingen eerdere schakels",
  "Publieke mededelingen van eerdere schakels in de keten (zoals de producent) tellen mee (huidige wet: lid 2 sub d).", [6],
  let="De slide noemt dit lid 1, en het bewijsvermoeden lid 2 met 6 maanden. In de huidige wet: 7:18 lid 2 sub d en 7:18a lid 2 (één jaar).")
A("BW", "7:18a", "Bewijsvermoeden consumentenkoop",
  "Lid 2: openbaart een gebrek zich binnen één jaar na aflevering, dan wordt vermoed dat de zaak nooit conform was.", [6],
  let="De slide en het antwoordmodel noemen art. 7:18 lid 2 en 6 maanden. Vraag de docent welke versie op het tentamen telt.")
A("BW", "7:21", "Rechten bij non-conformiteit",
  "Lid 1: aflevering van het ontbrekende (sub a), herstel (sub b) of vervanging (sub c). Lid 2: op kosten van de verkoper. Daarnaast de rechten "
  "uit Boek 6 (ontbinding, schadevergoeding).", [6, 7])
A("BW", "7:22", "Ontbinding en prijsvermindering (consument)",
  "Lid 1 sub a ontbinding, sub b prijsvermindering. Lid 2: pas als herstel en vervanging onmogelijk zijn of niet gevergd kunnen worden.", [6])
A("BW", "7:23", "Klachtplicht", "Lid 1: binnen bekwame tijd klagen nadat je het gebrek ontdekte of had moeten ontdekken; bij een consument is binnen twee maanden in ieder geval op tijd.", [6])
A("BW", "7:24", "Productaansprakelijkheid verkoper (consument)",
  "Lid 2: de verkoper is toch aansprakelijk als hij het gebrek kende of behoorde te kennen, de afwezigheid ervan toezegde, of bij zaakschade onder de €500.", [6])
A("BW", "7:26", "Betaling", "Lid 2: betalen op het moment en de plaats van aflevering.", [6])
A("BW", "7:28", "Verjaring betaling consumentenkoop", "De vordering tot betaling verjaart na twee jaar.", [6])
A("BW", "7:39", "Recht van reclame", "Lid 1: de verkoper kan de zaak terugvorderen als niet betaald is en aan de voorwaarden voor ontbinding is voldaan. Alleen roerende zaken die geen registergoed zijn.", [6])
A("BW", "7:41", "Reclame: zelfde staat", "Alleen als de zaak nog in dezelfde staat is als bij aflevering.", [6])
A("BW", "7:44", "Reclame: vervaltermijn", "Het recht vervalt als zowel 6 weken na opeisbaarheid van de betaling als 60 dagen na aflevering voorbij zijn.", [6])

# ---------------------------------------------------------------- EU en internationaal
A("EU", "18 VWEU", "Non-discriminatie", "Verbod op discriminatie naar nationaliteit; achtergrond van het non-discriminatiebeginsel.", [1])
A("EU", "101 en 102 VWEU", "Mededingingsregels", "Europese mededingingsregels voor ondernemingen. Alleen genoemd op de slide.", [1])
A("EU", "346 VWEU", "Defensie", "Uitzondering voor leveringen die de wezenlijke veiligheidsbelangen raken; genoemd bij art. 2.23 Aw.", [2])
A("EU", "Richtlijn 2014/24", "Klassieke overheid",
  "Richtlijn voor overheidsopdrachten van de klassieke overheid; art. 4 bevat de drempels. 2014/25 gaat over de nutssectoren, 2014/23 over concessies.", [1, 3],
  let="De slide van week 1 verwisselt de drie richtlijnen; de juiste indeling staat hier.")
A("EU", "GPA art. II, III, V, XVII", "Government Procurement Agreement (WTO)",
  "Art. II waardering van de opdracht, art. III non-discriminatie, art. V speciale regelingen voor ontwikkelingslanden, art. XVII transparantie.", [1])
