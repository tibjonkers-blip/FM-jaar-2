W = 1
I, R = "Inkoop", "Recht"

# ---------- Inkoop MC ----------
mc("ir1-i01", W, I, "Een leverancier verwacht volgend jaar 200.000 stuks te maken. De vaste kosten zijn €600.000 en de variabele kosten €5 per stuk. In de branche is 25% marge op de verkoopprijs gebruikelijk. Wat is de richtprijs volgens de kostprijsplusmethode?",
   ["€8,00", "€10,00", "€10,67", "€11,00"], 2,
   "Vaste kosten per stuk: €600.000 / 200.000 = €3. Kostprijs: €3 + €5 = €8. De marge is 25% van de verkoopprijs, dus 75% van de prijs dekt de kostprijs: (100 / 75) × €8 = €10,67. €10,00 krijg je als je ten onrechte 25% opslag op de kostprijs rekent.")
mc("ir1-i02", W, I, "De vaste kosten van een leverancier zijn €30 per stuk en de variabele kosten €45 per stuk. Jij biedt €50 per stuk. De leverancier heeft machines die stilstaan en is niet afhankelijk van jou. Wat is de meest waarschijnlijke reactie?",
   ["Hij weigert, want de totale kosten (€75) zijn hoger dan €50", "Hij kan accepteren: €50 dekt de variabele kosten en levert €5 per stuk op voor de vaste kosten", "Hij moet accepteren, want elke order is beter dan geen order", "Hij accepteert alleen als jij ook de vaste kosten vergoedt"], 1,
   "Bij onbenutte capaciteit kan een order onder de integrale kostprijs toch aantrekkelijk zijn, zolang de prijs boven de variabele kosten ligt. Het verschil (€5) draagt bij aan de vaste kosten die hij toch al heeft. Pas als de prijs onder de variabele kosten komt, moet hij weigeren.")
mc("ir1-i03", W, I, "Je koopt een vaatwasstraat voor het bedrijfsrestaurant: aanschaf €80.000, installatie €10.000, jaarlijks €12.000 aan onderhoud en energie. Na 4 jaar is de restwaarde €20.000. Wat is de TCO over 4 jaar?",
   ["€98.000", "€118.000", "€138.000", "€158.000"], 1,
   "Eenmalig €90.000 + 4 × €12.000 = €138.000, min de restwaarde van €20.000 = €118.000. €138.000 is de TCO zonder restwaarde.")
mc("ir1-i04", W, I, "Defensie is in Nederland de enige afnemer van een bepaald type gevechtsuitrusting. Welke marktvorm is dit aan de vraagzijde?",
   ["Monopolie", "Oligopolie", "Polypolie", "Volledige mededinging"], 0,
   "Eén vrager op de markt is een monopolie aan de vraagzijde. Die vrager heeft veel invloed op prijs en voorwaarden.")
mc("ir1-i05", W, I, "Een hogeschool koopt pennen en printpapier, net als duizenden andere organisaties. Wat past het best bij de positie van de inkoper?",
   ["De inkoper kan de marktprijs sturen omdat de hogeschool groot is", "De inkoper heeft weinig invloed op de prijs en volgt de marktontwikkelingen", "De inkoper moet een monopolist zoeken", "De inkoper kan de prijs het best via openboekcalculatie bepalen"], 1,
   "Dit is een polypolie aan de vraagzijde: heel veel vragers, geen enkele kan de prijs bepalen. Je volgt de markt en let vooral op het proces, bundeling en voorwaarden.")
mc("ir1-i06", W, I, "Een leverancier van werkplekadvies zegt: 'Onze prijs baseren we op wat het voor de klant waard is dat zijn medewerkers minder uitvallen.' Welke methode van prijsstelling is dit?",
   ["Kostprijsplusmethode", "Concurrentiegeoriënteerde prijsstelling", "Klantgeoriënteerde prijsstelling", "Dumping"], 2,
   "Klantgeoriënteerde prijsstelling neemt de waardeperceptie van de klant als leidraad, niet de eigen kosten of de prijzen van concurrenten.")
mc("ir1-i07", W, I, "Je bouwt zelf de kostprijs van een schoonmaakdienst na met cao-lonen, normtijden en branchegegevens, om te zien wat de prijs zou moeten zijn. Hoe heet dit?",
   ["Benchmarken", "Should cost analyse", "Openboekcalculatie", "Inkoopmarktonderzoek"], 1,
   "Bij een should cost analyse construeert de inkoper zelf de kostenopbouw op basis van industrie- en leveranciersgegevens. Bij openboekcalculatie geeft de leverancier zelf inzicht.")
mc("ir1-i08", W, I, "De cateraar laat op jouw verzoek zien hoe zijn prijs is opgebouwd uit personeelskosten, inkoop, overhead en marge. Welke techniek gebruik je dan?",
   ["Openboekcalculatie", "Benchmarken", "Should cost analyse", "Capaciteitsbenutting"], 0,
   "Bij openboekcalculatie geeft de leverancier inzicht in de opbouw van zijn kosten. Daarmee kun je gericht onderhandelen over de onderdelen.")
mc("ir1-i09", W, I, "Wat is dumping?",
   ["Een leverancier verkoopt onder de variabele kosten om een concurrent uit de markt te drukken", "Een leverancier hanteert voor de buitenlandse markt een lagere prijs dan voor de binnenlandse", "Een inkoper koopt grote partijen in om korting te krijgen", "Een leverancier verkoopt restvoorraad met verlies"], 1,
   "Dumping is een lagere prijs op de buitenlandse markt. Vaak zijn de vaste kosten al gedekt via de binnenlandse markt, zodat alleen de variabele kosten nog meetellen.")
mc("ir1-i10", W, I, "Een beveiligingsbedrijf moet de meldkamer ook betalen als er bij jouw klant die nacht niets gebeurt. Wat voor kosten zijn dat voor de leverancier?",
   ["Directe kosten", "Indirecte kosten (overhead)", "Variabele kosten", "Verborgen kosten voor de inkoper"], 1,
   "Indirecte kosten worden gemaakt voor alle opdrachten samen, zonder duidelijke relatie met één product of dienst. Het voorbeeld van de slides is de receptionist die ook betaald wordt als er geen gast komt.")
mc("ir1-i11", W, I, "Facilitaire inkoop (schoonmaak, catering, kantoorartikelen) valt meestal onder:",
   ["Primaire of directe inkoop (product related)", "Indirecte inkoop (non product related)", "Make-inkoop", "Publieke inkoop"], 1,
   "Facilitaire goederen en diensten gaan niet in het eindproduct zitten maar ondersteunen de bedrijfsvoering: indirecte of non product related inkoop.")
mc("ir1-i12", W, I, "Welk kenmerk hoort typisch bij publieke inkoop en niet bij private inkoop?",
   ["Vooral focus op prijs en ad hoc beslissen", "Vrij onderhandelen met de leverancier van je keuze", "Gebonden aan aanbestedingswetgeving en gericht op maatschappelijke doelstellingen", "Leveringsrisico's uitsluiten"], 2,
   "Publieke inkoop heeft maatschappelijke doelen, aanbestedingswetgeving, politieke sensitiviteit en een focus op prijs-kwaliteitverhouding. Vrij onderhandelen en ad hoc kiezen horen bij private inkoop.")

# ---------- Recht MC ----------
mc("ir1-r01", W, R, "Wat is het belangrijkste doel van het aanbestedingsrecht?",
   ["Lokale ondernemers beschermen tegen buitenlandse concurrentie", "Mededinging op de markt voor overheidsopdrachten, zodat de overheid 'best value for taxpayers money' krijgt", "De overheid verplichten altijd de laagste prijs te kiezen", "Onderhandse gunning makkelijker maken"], 1,
   "Het aanbestedingsrecht reguleert markten voor overheidsopdrachten via gelijkheid en transparantie, bevordert mededinging op de EU-markt en voorkomt vriendjespolitiek. Het is juist het tegenovergestelde van onderhandse gunning.")
mc("ir1-r02", W, R, "Een gemeente eist dat inschrijvers 'een vestiging in de eigen provincie' hebben. Welk beginsel komt hiermee het eerst in gevaar?",
   ["Non-discriminatie (en gelijkheid), art. 1.8 Aw", "Wederzijdse erkenning", "Beperking van administratieve lasten, art. 1.6 Aw", "Clusterverbod, art. 1.5 Aw"], 0,
   "Een vestigingseis benadeelt buitenlandse en verder weg gevestigde bedrijven: een verkapte of indirecte vorm van discriminatie. Die is verboden tenzij er een objectieve rechtvaardiging is.")
mc("ir1-r03", W, R, "Na het openen van de inschrijvingen vraagt de aanbestedende dienst één inschrijver zijn prijs 'te verduidelijken', waarna die een lagere prijs noemt. Is dat toegestaan?",
   ["Ja, verduidelijken mag altijd", "Ja, als de dienst daarna alle inschrijvers dezelfde kans geeft", "Nee, een verduidelijking mag niet leiden tot een nieuwe of aangepaste inschrijving (gelijkheid)", "Nee, want na de inschrijving mag helemaal geen contact meer zijn"], 2,
   "Verduidelijken mag alleen ter concretisering of herstel van een kenbare omissie, en mag niet leiden tot een nieuwe inschrijving. Een lagere prijs is een inhoudelijke wijziging en schendt het gelijkheidsbeginsel. Er mag wel om duidelijkheid gevraagd worden, dus 'nooit contact' klopt niet.")
mc("ir1-r04", W, R, "Na de gunning wil een ministerie de looptijd van het contract verdubbelen zonder nieuwe aanbesteding. Welk arrest is hier het bekendst?",
   ["Michaniki", "Pressetext", "Telaustria", "Vestergaard"], 1,
   "Pressetext (C-454/06) gaat over wezenlijke wijzigingen na de gunning. Een wezenlijke wijziging staat gelijk aan een nieuwe opdracht en raakt het gelijkheidsbeginsel na de procedure.")
mc("ir1-r05", W, R, "Waar moet een aanbestedingsplichtige opdracht in Nederland worden aangekondigd?",
   ["Op de eigen website van de aanbestedende dienst", "In een landelijke krant", "Op TenderNed (art. 1.18 Aw)", "Dat mag de aanbestedende dienst vrij kiezen"], 2,
   "Het medium is in principe een discretionaire bevoegdheid, tenzij er een voorschrift is. Voor aanbestedingsplichtige opdrachten is dat TenderNed.")
mc("ir1-r06", W, R, "Voor een schoonmaakopdracht van €150.000 per jaar eist een gemeente een jaaromzet van minstens €10 miljoen. Welk beginsel staat hier onder druk?",
   ["Proportionaliteit", "Objectiviteit", "Wederzijdse erkenning", "Transparantie achteraf"], 0,
   "Eisen mogen niet zwaarder zijn dan nodig voor de opdracht. Een omzeteis van ruim 60 keer de jaarwaarde is buitensporig en sluit mkb-bedrijven onnodig uit.")
mc("ir1-r07", W, R, "Een Duitse inschrijver levert een Duits veiligheidscertificaat in plaats van het gevraagde Nederlandse VCA-certificaat. Het Duitse certificaat is gelijkwaardig. Wat moet de aanbestedende dienst doen?",
   ["Uitsluiten, want het gevraagde certificaat ontbreekt", "Accepteren op grond van wederzijdse erkenning", "Alleen accepteren als de inschrijver een Nederlandse vestiging heeft", "De inschrijver een nieuwe inschrijving laten doen"], 1,
   "Wederzijdse erkenning: gelijkwaardige technische specificaties, certificaten en kwalificaties uit andere lidstaten moeten worden geaccepteerd (art. 2.75 tot en met 2.77 Aw; Vestergaard).")
mc("ir1-r08", W, R, "Een beoordelaar geeft een inschrijver extra punten omdat 'we al jaren prettig met ze samenwerken', terwijl dat geen gunningscriterium is. Welk beginsel wordt geschonden?",
   ["Objectiviteit", "Proportionaliteit", "Wederzijdse erkenning", "Beperking van administratieve lasten"], 0,
   "Subjectieve voorkeuren mogen geen rol spelen: gunningscriteria moeten objectief en uniform worden toegepast. Ervaringen uit het verleden mogen alleen op een objectieve manier meetellen (vgl. art. 2.87 lid 1 sub g Aw).")
mc("ir1-r09", W, R, "Gelden de algemene beginselen ook voor een opdracht onder de Europese drempel?",
   ["Nee, onder de drempel is alles vrij", "Ja, als er een duidelijk grensoverschrijdend belang is", "Alleen voor werken", "Alleen als de opdracht op TenderNed staat"], 1,
   "Bij een grensoverschrijdend belang gelden de algemene beginselen, met name de drie belangrijkste, ook bij niet-aanbestedingsplichtige opdrachten. Gezichtspunten: ligging dichtbij de grens, de omvang van het bedrag en de aard van de opdracht.")
mc("ir1-r10", W, R, "Een provincie voegt schoonmaak, catering, beveiliging en groenonderhoud samen in één opdracht, zonder goede reden. Wat is het probleem?",
   ["Strijd met het clusterverbod (art. 1.5 lid 1 Aw)", "Strijd met de non-discriminatie (art. 1.8 Aw)", "Strijd met de wederzijdse erkenning", "Geen probleem, samenvoegen verlaagt altijd de kosten"], 0,
   "Het clusterverbod verbiedt het onnodig samenvoegen van opdrachten, omdat dat kleinere ondernemingen uitsluit. Samenvoegen mag alleen met een goede motivering.")
mc("ir1-r11", W, R, "Welke Europese richtlijn regelt de aanbesteding door de 'klassieke' overheid (gemeenten, ministeries, provincies)?",
   ["Richtlijn 2014/23/EU", "Richtlijn 2014/24/EU", "Richtlijn 2014/25/EU", "Richtlijn 2004/18/EG"], 1,
   "Richtlijn 2014/24 is de klassieke richtlijn, 2014/25 gaat over de speciale sectoren (nutssectoren) en 2014/23 over concessies. Kritische noot: op slide 9 van week 1 staan de nummers door elkaar (2014/23 als klassieke overheid). Check bij de docent welke nummering op het tentamen telt.")
mc("ir1-r12", W, R, "Welke uitspraak over de Gids Proportionaliteit klopt?",
   ["Het is een vrijblijvend advies", "Het is via het Aanbestedingsbesluit aangewezen en daardoor verplicht", "Het geldt alleen voor werken boven de drempel", "Het vervangt de Aanbestedingswet 2012"], 1,
   "De Gids Proportionaliteit is aangewezen door het Aanbestedingsbesluit (een AMvB) en is daardoor verplicht. Afwijken mag alleen gemotiveerd ('pas toe of leg uit').")

# ---------- Open vragen ----------
op("ir1-io1", W, I, "Een facilitair manager kiest koffieautomaten alleen op aanschafprijs. Leg uit wat TCO is, waarom alleen de aanschafprijs een slechte basis is, en noem drie verborgen kosten die bij koffieautomaten kunnen spelen.",
   "TCO (Total Cost of Ownership) zijn alle kosten en opbrengsten gedurende de hele periode dat je eigenaar bent: aanschaf plus installatie, gebruik, onderhoud en afvoer, min de restwaarde. Alleen de aanschafprijs vergelijken is misleidend, omdat een goedkope machine duur kan uitvallen in gebruik. Verborgen kosten bij koffieautomaten zijn bijvoorbeeld onderhoud en storingen, energieverbruik, ingrediënten die je alleen bij die leverancier mag kopen, schoonmaak en ontkalken, en de afvoer aan het eind.",
   ["Definitie TCO: alle kosten (en opbrengsten) over de hele levensduur/bezitsperiode", "Uitleg waarom alleen aanschafprijs een vertekend beeld geeft", "Drie concrete verborgen kosten die passen bij koffieautomaten"])
op("ir1-io2", W, I, "Je onderhandelt over een schoonmaakcontract. Beoordeel per kostensoort (loonkosten, materiaal, overhead, reiskosten) hoeveel onderhandelingsruimte er is en waarom.",
   "Loonkosten: beperkt, omdat schoonmakers onder de cao vallen en het grootste deel van de prijs arbeid is; je kunt wel praten over normtijden en frequenties. Materiaal: ja, onderhandelbaar via volume, alternatieve middelen of eigen inkoop. Overhead: soms, afhankelijk van de opbouw; via openboek kun je zien of de opslag redelijk is. Reiskosten: ja, bijvoorbeeld door roosters slim te plannen of locaties te combineren.",
   ["Loonkosten beperkt, met reden (cao, groot aandeel arbeid)", "Materiaal onderhandelbaar, met reden", "Overhead soms, met reden", "Reiskosten onderhandelbaar, met reden"])
op("ir1-io3", W, I, "Leg uit wat een make-or-buybeslissing is en noem voor de catering van een hogeschool twee argumenten om het zelf te doen en twee argumenten om het uit te besteden.",
   "Bij make-or-buy kiest een organisatie of ze een activiteit zelf uitvoert of extern inkoopt. Zelf doen: meer controle over kwaliteit en uitstraling, en flexibiliteit bij veranderingen of eigen personeel dat de organisatie kent. Uitbesteden: specialistische kennis en schaalvoordelen van een cateraar, minder risico en zorg voor personeel, variabele in plaats van vaste kosten, en focus op de kerntaak onderwijs.",
   ["Juiste uitleg van make-or-buy", "Twee passende argumenten voor zelf doen", "Twee passende argumenten voor uitbesteden"])
op("ir1-ro1", W, R, "Het gelijkheidsbeginsel werkt vóór, tijdens en na de aanbestedingsprocedure. Leg voor elke fase uit wat het betekent en noem bij minstens twee fasen een passend arrest.",
   "Vóór de procedure: alle inschrijvers gelijke kansen bij de voorbereiding en beoordeling van hun inschrijving (Michaniki). Alle inschrijvingen moeten aan de eisen voldoen en er wordt niet onderhandeld (SAG). Tijdens: de dienst controleert de juistheid (Wienstrom), legt gunningscriteria de hele procedure op dezelfde manier uit, en vraagt niet om precisering van een onjuiste of onnauwkeurige inschrijving (Manova). Na: wezenlijke wijzigingen in de opdracht of het contract na gunning zijn in strijd met gelijkheid (Pressetext).",
   ["Fase vóór juist uitgelegd", "Fase tijdens juist uitgelegd", "Fase na (wezenlijke wijziging) juist uitgelegd", "Minstens twee arresten aan de juiste fase gekoppeld"])
op("ir1-ro2", W, R, "Wat houdt het transparantiebeginsel (art. 1.9 Aw) in? Bespreek transparantie vooraf, tijdens en na de procedure en leg uit waarom transparantie nodig is.",
   "Vooraf: een passende mate van openbaarheid, met een toegankelijke aankondiging (voor aanbestedingsplichtige opdrachten op TenderNed) en voldoende informatie voor potentiële inschrijvers (Telaustria, Coname). Tijdens: criteria duidelijk, precies en ondubbelzinnig; gunningscriteria met subcriteria en wegingsfactoren uitputtend vooraf bekend, en geen tussentijdse wijziging. Na: de gunning wordt gemotiveerd, en verduidelijking mag alleen ter concretisering en niet tot een nieuwe inschrijving leiden. Transparantie is nodig om te kunnen controleren of gelijkheid en non-discriminatie zijn nageleefd.",
   ["Transparantie vooraf (aankondiging, openbaarheid)", "Transparantie tijdens (heldere criteria, wegingen vooraf, niet wijzigen)", "Transparantie na (motivering gunning)", "Doel: controle op gelijkheid en non-discriminatie"])
op("ir1-ro3", W, R, "Noem drie Nederlandse uitgangspunten uit de Aanbestedingswet met het artikel, en leg bij elk in één zin uit wat het betekent voor een facilitaire aanbesteding.",
   "Creatie van maatschappelijke waarde (art. 1.4 lid 2 Aw): bij de inkoop rekening houden met maatschappelijke effecten, zoals duurzaamheid of social return. Clusterverbod (art. 1.5 lid 1 Aw): facilitaire diensten niet onnodig samenvoegen tot één grote opdracht. Percelenregeling (art. 1.5 lid 3 Aw): een opdracht in principe in percelen verdelen of motiveren waarom niet. Beperking van administratieve lasten (art. 1.6 Aw): niet meer bewijsstukken vragen dan nodig.",
   ["Drie juiste uitgangspunten", "Juiste artikelen erbij", "Per uitgangspunt een toepassing op facilitaire inkoop"])

# ---------- Casussen ----------
cs("ir1-ic1", W, I, "Koffieautomaten voor de hogeschool",
   "Je bent inkoper bij een hogeschool en vergelijkt twee aanbiedingen voor tien koffieautomaten voor vijf jaar.\n\nAanbieding A (koop): €4.000 per automaat, onderhoudscontract €3.000 per jaar voor alle automaten, energie €1.500 per jaar. Restwaarde na vijf jaar in totaal €5.000.\n\nAanbieding B (huur, all-in): €11.000 per jaar inclusief onderhoud en vervanging bij defect. Energiezuinige automaten: energie €1.200 per jaar. Geen restwaarde.\n\nDe accountmanager van B zegt: 'Onze prijs is gebaseerd op wat ongestoorde koffievoorziening voor uw studenten en medewerkers waard is.'",
   [("Bereken de TCO over vijf jaar van aanbieding A en van aanbieding B. Laat je berekening zien.",
     "A: aanschaf 10 × €4.000 = €40.000; jaarlijks €3.000 + €1.500 = €4.500, over vijf jaar €22.500; min restwaarde €5.000. TCO A = €40.000 + €22.500 − €5.000 = €57.500. B: (€11.000 + €1.200) × 5 = €61.000. TCO B = €61.000.",
     ["TCO A juist (€57.500) met berekening", "TCO B juist (€61.000) met berekening"]),
    ("Welke aanbieding adviseer je? Betrek naast de TCO minstens twee andere overwegingen.",
     "Op TCO is A €3.500 goedkoper. Maar bij B ligt het risico van storingen en vervanging bij de leverancier, je hebt geen kapitaalbeslag van €40.000 vooraf, en je bent flexibeler als het gebruik verandert. Bij A ben je eigenaar en loop je het risico dat de restwaarde lager uitvalt. Een goed advies weegt het kleine prijsverschil af tegen risico en flexibiliteit en kiest onderbouwd.",
     ["Advies sluit aan op de berekening", "Minstens twee relevante andere overwegingen (risico, kapitaalbeslag, flexibiliteit, service)", "Duidelijke keuze met onderbouwing"]),
    ("Welke methode van prijsstelling gebruikt leverancier B en welke techniek kun je inzetten om te controleren of zijn prijs redelijk is?",
     "B gebruikt klantgeoriënteerde prijsstelling: de waardeperceptie van de klant is leidraad. Controleren kan met benchmarken (prijzen van andere leveranciers of eerdere aankopen), een should cost analyse, of door te vragen om een openboekcalculatie.",
     ["Klantgeoriënteerde prijsstelling herkend", "Passende controletechniek genoemd en uitgelegd"])])
cs("ir1-rc1", W, R, "Schoonmaak gemeentehuis Kerkrade",
   "De gemeente Kerkrade (direct aan de Duitse grens) wil de schoonmaak van het gemeentehuis voor twee jaar uitbesteden. De geraamde waarde ligt onder de Europese drempel. De gemeente wil:\n1. alleen bedrijven toelaten die in Limburg gevestigd zijn, 'zodat het geld in de regio blijft';\n2. een minimale jaaromzet eisen van €5 miljoen;\n3. alleen het Nederlandse VCA-certificaat accepteren.\nEen Duits schoonmaakbedrijf uit Aken met een gelijkwaardig Duits certificaat en een jaaromzet van €2 miljoen wil meedoen.",
   [("Gelden de algemene beginselen van het aanbestedingsrecht hier, ook al ligt de opdracht onder de drempel? Motiveer.",
     "Ja, waarschijnlijk wel. Bij een duidelijk grensoverschrijdend belang gelden de algemene beginselen ook onder de drempel. De gezichtspunten zijn de ligging dichtbij de grens (Kerkrade ligt aan de grens met Aken), het bedrag en de aard van de opdracht. Dat een Duits bedrijf belangstelling heeft, ondersteunt dat.",
     ["Juiste regel: beginselen gelden bij grensoverschrijdend belang", "Toepassing met de gezichtspunten op Kerkrade"]),
    ("Beoordeel de drie wensen van de gemeente aan de hand van de beginselen.",
     "1. De vestigingseis is een verkapte of indirecte discriminatie naar nationaliteit en strijdig met gelijkheid en non-discriminatie (art. 1.8 Aw). 2. Een omzeteis van €5 miljoen voor deze opdracht is waarschijnlijk disproportioneel; eisen mogen niet zwaarder zijn dan nodig. 3. Alleen VCA accepteren is in strijd met wederzijdse erkenning: een gelijkwaardig certificaat uit een andere lidstaat moet worden geaccepteerd.",
     ["Wens 1 gekoppeld aan non-discriminatie/gelijkheid", "Wens 2 gekoppeld aan proportionaliteit", "Wens 3 gekoppeld aan wederzijdse erkenning"]),
    ("Welk advies geef je de gemeente in één of twee zinnen?",
     "Laat de vestigingseis vallen, stel een omzeteis die in verhouding staat tot de opdrachtwaarde (of laat die weg), en accepteer gelijkwaardige certificaten. Zo voorkomt de gemeente klachten en procedures van uitgesloten bedrijven.",
     ["Concreet en uitvoerbaar advies dat de drie knelpunten oplost"])])
cs("ir1-rc2", W, R, "Facilitaire dienstverlening Provincie Gelderland",
   "De Provincie Gelderland heeft facilitaire dienstverlening Europees aanbesteed. In de aankondiging staat: prijs 40% en kwaliteit 60%. Na het openen van de inschrijvingen gebeurt het volgende:\n- De provincie besluit dat prijs toch belangrijker is en rekent met 60% prijs en 40% kwaliteit.\n- Inschrijver X heeft een onduidelijke prijs voor de schoonmaak opgegeven. De provincie vraagt alleen X om een 'verduidelijking'. X stuurt een nieuwe, lagere prijs.\n- Na de gunning aan X spreken provincie en X af dat de looptijd van 4 naar 8 jaar gaat, zonder nieuwe aanbesteding.",
   [("Mocht de provincie de weging van prijs en kwaliteit wijzigen? Gebruik het juiste beginsel.",
     "Nee. Volgens het transparantiebeginsel (art. 1.9 Aw) moeten de gunningscriteria met subcriteria en wegingsfactoren uitputtend vooraf bekend zijn en mogen ze tussentijds niet worden gewijzigd. Inschrijvers hebben hun inschrijving op de oude weging gebaseerd; wijzigen achteraf maakt willekeur mogelijk en schendt ook de gelijkheid.",
     ["Nee, met transparantie (criteria en wegingen vooraf vast, niet wijzigen)", "Uitleg waarom: inschrijvers gingen uit van de bekendgemaakte weging"]),
    ("Beoordeel de 'verduidelijking' bij inschrijver X.",
     "Niet toegestaan. Een verduidelijking mag alleen ter concretisering of herstel van een kenbare omissie en mag niet leiden tot een nieuwe inschrijving. Een nieuwe, lagere prijs verandert de inschrijving inhoudelijk. Bovendien krijgt alleen X die kans, in strijd met het gelijkheidsbeginsel (SAG, Manova).",
     ["Niet toegestaan, verduidelijking mag geen nieuwe inschrijving worden", "Gelijkheidsbeginsel (alleen X krijgt de kans), eventueel met arrest"]),
    ("Mag de looptijd na de gunning van 4 naar 8 jaar? Noem het relevante arrest.",
     "Nee. Een verdubbeling van de looptijd is een wezenlijke wijziging: andere inschrijvers hadden misschien anders ingeschreven of meegedaan. Volgens Pressetext (C-454/06) staat een wezenlijke wijziging na gunning gelijk aan een nieuwe opdracht, die opnieuw moet worden aanbesteed.",
     ["Nee, wezenlijke wijziging", "Pressetext genoemd en toegepast"])])
