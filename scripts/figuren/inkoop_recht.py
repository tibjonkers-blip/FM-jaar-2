"""Figuren en grafieken bij de samenvattingen van Inkoop en recht.

Elke figuur herhaalt wat in de samenvatting van die les staat. De getallen komen uit de rekenvoorbeelden en tabellen van de samenvatting.
"""
from lib import *

SH = "­"  # zacht afbreekteken voor lange woorden in smalle kolommen

# ---- eigen svg: vraag en aanbod
VRAAG_AANBOD = svg(
    '<path class="ax" d="M44 16V190H330"/>'
    '<text x="38" y="24" text-anchor="end" class="mut">prijs</text><text x="330" y="206" text-anchor="end" class="mut">hoeveelheid</text>'
    '<path class="dash" d="M44 105H177M177 105V190"/>'
    '<path class="ln l1" d="M64 40 290 170"/><path class="ln l2" d="M64 170 290 40"/>'
    '<circle class="f1 ring" cx="177" cy="105" r="5"/>'
    '<text x="296" y="174" class="bold">vraag</text><text x="296" y="44" class="bold">aanbod</text>'
    '<text x="50" y="99" class="bold">evenwichtsprijs</text>'
    '<text x="177" y="82" text-anchor="middle" class="mut">snijpunt</text>',
    w=350, h=212, label="Grafiek met een dalende vraaglijn en een stijgende aanbodlijn. Waar ze elkaar snijden ligt de evenwichtsprijs.")

FIGUREN = [
    # ================================================================ overzicht
    F(0, "Overzicht", None, fig(
        "Toetsmatrijs Inkoop: waar de punten zitten",
        legend([("c1", "kennis en begrip"), ("c2", "toepassen")]) + bars([
            dict(label="1. Basisprincipes van inkoop", sub="week 1", segs=[(5, "c1"), (5, "c2")], val="5 + 5"),
            dict(label="2. Contractmanagement", sub="week 5", segs=[(10, "c1"), (10, "c2")], val="10 + 10"),
            dict(label="3. Europees aanbesteden", sub="week 3 en 4", segs=[(10, "c1"), (10, "c2")], val="10 + 10"),
            dict(label="4. KPI's en TCO", sub="week 1 en 3", segs=[(10, "c1"), (10, "c2")], val="10 + 10"),
            dict(label="5. Sourcing", sub="week 2", segs=[(10, "c1"), (10, "c2")], val="10 + 10"),
            dict(label="6. Circulair inkopen, duurzaamheid en ethiek", sub="week 6", segs=[(5, "c1"), (5, "c2")], val="5 + 5"),
        ], maxv=20, vw="5em", label="Punten per leerdoel, verdeeld over kennis en begrip en toepassen"),
        noot="De getallen komen uit de toetsmatrijs hierboven. Bij elk leerdoel is de helft voor toepassen, en vier leerdoelen wegen twee keer zo zwaar als leerdoel 1 en 6."),
      after="Leerdoel"),

    # ================================================================ week 1 inkoop
    F(1, "Inkoop", "Het lineaire inkoopproces", fig(
        "Het inkoopproces in zes stappen",
        phases([
            ("Tactische inkoop", [("Specificeren", "wat heb je nodig?"), ("Selecteren", "welke leverancier?"), ("Contracteren", "afspraken vastleggen")], "t1"),
            ("Operationele inkoop", [("Bestellen", None), ("Bewaken", "komt het goed binnen?"), ("Nazorg", "afhandelen en evalueren")], "t2"),
        ]),
        noot="Stappen volgens Van Weele; op de slide stonden ze alleen als afbeelding, dus check ze in het boek. Een aanbesteding gaat over de eerste drie stappen (week 3).")),

    F(1, "Inkoop", "Kostenopbouw van een leverancier", fig(
        "Rekenvoorbeeld: waarom een bod van €80 toch kan",
        legend([("c1", "variabele kosten"), ("c2", "vaste kosten"), ("c3", "bijdrage aan de vaste kosten")]) + bars([
            dict(label="Kosten per stuk", segs=[(60, "c1"), (50, "c2")], val="€110"),
            dict(label="Bod van de klant", segs=[(60, "c1"), (20, "c3")], val="€80"),
        ], maxv=110, vw="3.5em", label="Kosten per stuk vergeleken met het bod van de klant"),
        noot="Het bod dekt de variabele kosten van €60 helemaal en levert €20 per stuk op voor de vaste kosten. Met onbenutte capaciteit kan de leverancier dus accepteren. Onder €60 moet de leverancier weigeren.")),

    F(1, "Inkoop", "Prijsvorming en marktvormen", fig(
        "Vraag en aanbod bepalen de evenwichtsprijs",
        legend([("c1", "vraag: hoe hoger de prijs, hoe minder er gevraagd wordt"), ("c2", "aanbod: hoe hoger de prijs, hoe meer er aangeboden wordt")]) + VRAAG_AANBOD,
        noot="De lijnen zijn een schets zonder echte getallen. Macht aan één kant van de markt (een monopolie of oligopolie) verstoort dit evenwicht."),
      after="evenwichtsprijs"),

    F(1, "Inkoop", "Methoden van prijsstelling", fig(
        "Kostprijsplus: zo is de verkoopprijs van €7,50 opgebouwd",
        seg([
            (2, "c2", "Vaste kosten €2,00", "€2.000.000 over 1.000.000 stuks"),
            (4, "c1", "Variabele kosten €4,00", "per stuk"),
            (1.5, "c3", "Marge €1,50", "20% van de verkoopprijs"),
        ]),
        noot="De kostprijs van €6,00 is 80% van de verkoopprijs. Wie 20% over de kostprijs rekent, komt op €7,20 en dat is hier fout.")),

    F(1, "Inkoop", "Total Cost of Ownership (TCO)", fig(
        "Rekenvoorbeeld TCO over vijf jaar",
        bars([
            dict(label="Eenmalige kosten", sub="machine, software, installatie", segs=[(420, "c1")], val="€420.000"),
            dict(label="Jaarlijkse kosten", sub="5 × €39.000", start=420, segs=[(195, "c1")], val="+ €195.000"),
            dict(label="Restwaarde", sub="na vijf jaar", start=515, segs=[(100, "c2")], val="− €100.000", neg=True),
            dict(label="TCO", sub="wat het echt kost", segs=[(515, "c0")], val="€515.000"),
        ], maxv=615, vw="7em", label="Opbouw van de TCO: eenmalige kosten plus jaarlijkse kosten min restwaarde"),
        noot="De aanschaf is maar een deel van het verhaal: de jaarlijkse kosten tellen op, de restwaarde gaat eraf."),
      after="Rekenvoorbeeld"),

    # ================================================================ week 1 recht
    F(1, "Recht", "Juridisch kader in drie lagen", fig(
        "Van wereld naar Nederland: elke laag werkt de laag erboven uit",
        nest([
            ("Wereld: WTO", "Government Procurement Agreement (GPA). Doel: vrije internationale handel."),
            ("Europa: EU", "Richtlijnen 2014/23, 2014/24 en 2014/25 en de arresten van het Hof van Justitie. Daaruit komen de algemene beginselen."),
            ("Nederland", "Aanbestedingswet 2012, Aanbestedingsbesluit, Gids proportionaliteit en ARW 2016."),
        ]))),

    F(1, "Recht", "De zeven algemene beginselen", fig(
        "Gelijkheid en transparantie in de drie fasen van een aanbesteding",
        pgrid(["Vóór de procedure", "Tijdens de procedure", "Na de procedure"], [
            ("Gelijkheid (art. 1.8 Aw)", [
                ("Gelijke kansen; alle offertes voldoen aan het bestek; niet onderhandelen", "Michaniki, SAG"),
                ("Criteria de hele procedure hetzelfde uitleggen; juistheid controleren", "Wienstrom, Manova"),
                ("Geen wezenlijke wijziging van de opdracht of het contract", "Pressetext")]),
            ("Transparantie (art. 1.9 Aw)", [
                ("Toegankelijke aankondiging, ook voor andere lidstaten", "TenderNed, art. 1.18 Aw"),
                ("Criteria, subcriteria en weging staan uitputtend in aankondiging en bestek", "niet tussentijds wijzigen"),
                ("Verduidelijken mag alleen om te concretiseren of een kenbare omissie te herstellen", "geen nieuwe inschrijving")]),
        ]))),

    F(1, "Recht", "Zo gebruik je dit in een casusantwoord", fig(
        "De vaste opbouw van een casusantwoord, met het voorbeeld van de omzeteis",
        flow([
            ("Beginsel en artikel", "evenredigheid, Gids proportionaliteit"),
            ("Wat het inhoudt", "eisen niet zwaarder dan nodig voor de opdracht"),
            ("Toepassing op de feiten", "omzeteis €20 miljoen bij een opdracht van €400.000 per jaar"),
            ("Conclusie", "de eis is disproportioneel"),
        ])), after="Gebruik de vaste opbouw"),

    # ================================================================ week 2 inkoop
    F(2, "Inkoop", "De drie keuzes in een sourcingstrategie", fig(
        "Aantal leveranciers: van één naar veel",
        cards([
            ("●", "Sole sourcing", "één leverancier, omdat die monopolist is: je hebt geen keus"),
            ("●", "Single sourcing", "bewust één leverancier"),
            ("●●", "Dual sourcing", "afspraken met twee leveranciers"),
            ("●●●●", "Multiple sourcing", "een veelvoud aan leveranciers"),
        ])), after="Aantal leveranciers"),

    F(2, "Inkoop", "De drie keuzes in een sourcingstrategie", fig(
        "De matrix van Kraljic met de strategie per kwadrant",
        quad("Financieel belang", "Leveringsrisico", [
            ("Hefboom", "hoog belang, laag risico, veel aanbieders", "Concurrentie benutten, vaak multiple sourcing", "t3"),
            ("Strategisch", "hoog belang, hoog risico", "Lange relatie, partnership, vaak single sourcing", "t1"),
            ("Routine", "laag belang, laag risico", "Efficiënt inkopen, bundelen, weinig tijd aan besteden", "t0"),
            ("Knelpunt", "laag belang, hoog risico", "Leveringszekerheid, vaak noodgedwongen sole sourcing; zoek alternatieven", "t4"),
        ]),
        noot="Onderbouw de plek van een product altijd met beide assen: financieel belang én leveringsrisico."),
      after="Kraljic-kwadrant"),

    F(2, "Inkoop", "Samenwerkingsvormen tussen organisaties", fig(
        "Horizontaal en verticaal samenwerken",
        '<div class="lanes"><div class="lane"><h5>Horizontaal <small>gelijke organisaties kopen samen in</small></h5>'
        + som(["Organisatie A", "Organisatie B", "Organisatie C"], ("Inkoopcombinatie", "bv. Intrakoop, VNG Realisatie, Aedes"))
        + '</div><div class="lane"><h5>Verticaal <small>schakels in de logistieke keten</small></h5>'
        + flow([("Leverancier", None), ("Inkopende organisatie", "koop je het eindproduct goed in, dan volgen onderdelen en diensten")], numbered=False)
        + "</div></div>")),

    F(2, "Inkoop", "Uitbesteden (outsourcing)", fig(
        "Drie keuzes bij uitbesteden",
        poles([
            ("Hoeveel gaat over?", ("Partial", "een deel van de activiteit"), ("Turnkey", "de hele activiteit")),
            ("Waar wordt het uitgevoerd?", ("On-site", "op jouw terrein, bv. schoonmaak of catering in je eigen pand"), ("Off-site", "buiten jouw terrein, bv. wasserij of archiefopslag")),
            ("Hoe ver weg zit de leverancier?", ("Nearshore", "korte reisafstand, dezelfde of een naburige tijdzone"), ("Offshore", "een ander, vaak ver, land")),
        ]))),

    F(2, "Inkoop", "Verborgen kosten bij goedkoop inkopen ver weg", fig(
        "De ijsberg van de goedkope gieter",
        iceberg("De lage aanschafprijs", [
            "transport", "invoerrechten en douane", "wisselkoersrisico", "langere levertijd, dus meer voorraad",
            "kwaliteitsrisico en extra controle", "communicatie", "kortere levensduur"],
            onderkop="Onder water: verborgen kosten"),
        noot="De duurdere lokale leverancier wint als deze kosten samen groter zijn dan het prijsverschil. Dat reken je uit met de TCO van week 1.")),

    # ================================================================ week 2 recht
    F(2, "Recht", "Wie is aanbestedingsplichtig? (H4)", fig(
        "Publiekrechtelijke instelling: alle drie de voorwaarden moeten kloppen",
        som([
            ("Algemeen belang", "opgericht voor behoeften van algemeen belang, niet industrieel of commercieel"),
            ("Rechtspersoonlijkheid", None),
            ("Overheidsinvloed", "hoofdzakelijk overheidsfinanciering, overheidstoezicht of bestuur voor meer dan de helft door de overheid benoemd"),
        ], ("Publiekrechtelijke instelling", "aanbestedingsplichtig, art. 1.1 Aw")),
        noot="Mist één voorwaarde, dan is het geen publiekrechtelijke instelling. Zo valt CZ af: die werkt op commerciële beginselen."),
      after="De overheidsinvloed bij categorie 2"),

    F(2, "Recht", "Uitzonderingen (afdeling 2.1.3 Aw)", fig(
        "Percelenregeling: hoeveel mag buiten de Europese aanbesteding blijven?",
        seg([
            (80, "c1", "Minstens 80% van de totale waarde", "Europees aanbesteden"),
            (20, "c2", "Hoogstens 20% van de totale waarde", "mag zonder Europese aanbesteding, in percelen van elk hoogstens €80.000 (leveringen en diensten) of €1.000.000 (werken)"),
        ])), after="Samen maximaal"),

    F(2, "Recht", "Uitzonderingen (afdeling 2.1.3 Aw)", fig(
        "(Quasi-)inbesteden: drie voorwaarden",
        som([
            ("Toezicht", "de dienst houdt toezicht als op een eigen dienst"),
            ("Meer dan 80%", "van de werkzaamheden is voor die dienst"),
            ("Geen particulier kapitaal", "geen directe participatie"),
        ], ("Inbesteden mag", "geen aanbesteding nodig, art. 2.24a Aw")))),

    F(2, "Recht", "Zo bouw je een casusantwoord op", fig(
        "Is de opdracht Europees aanbestedingsplichtig? De drie W's als ladder",
        ladder([
            ("Wie: is het een aanbestedende dienst?", "Overheid, publiekrechtelijke instelling of gesubsidieerde instelling. Toets elke voorwaarde en noem het artikel.", "Nee: niet aanbestedingsplichtig"),
            ("Wat: is het een overheidsopdracht?", "Schriftelijk, onder bezwarende titel, tussen ondernemer en aanbestedende dienst. Werk, levering of dienst; bij een combinatie het hoofdvoorwerp.", "Nee: geen overheidsopdracht"),
            ("Waarde: boven de drempel?", "Raam de totale waarde zonder btw, met opties en verlengingen (week 3).", "Nee: niet Europees aanbesteden. Bij een grensoverschrijdend belang gelden de beginselen wel."),
            ("Uitzondering van toepassing?", "Inbesteding, publiek-publieke samenwerking, percelenregeling of art. 2.23 en 2.24 Aw.", "Ja: geen Europese aanbesteding nodig"),
        ], slot="Europees aanbestedingsplichtig: sluit af met een conclusie in één zin"))),

    # ================================================================ week 3 inkoop
    F(3, "Inkoop", "Gunnen", fig(
        "Gunnen: één uitgangspunt, drie methoden",
        tree("EMVI", [
            ("Beste prijs-kwaliteitverhouding", "BPKV, de standaardmethode"),
            ("Laagste kosten", "op basis van kosteneffectiviteit, zoals TCO"),
            ("Laagste prijs", None),
        ], rootsub="economisch meest voordelige inschrijving"),
        noot="De aanbestedende dienst maakt vooraf gedetailleerd duidelijk hoe er gegund wordt.")),

    F(3, "Inkoop", "Meten van prestaties: KSF, KPI en norm", fig(
        "Van succesfactor naar meetbare afspraak",
        flow([
            ("KSF", "wat moet goed gaan om je doel te halen?"),
            ("KPI", "meetbare grootheid die laat zien hoe het met de KSF staat"),
            ("Norm", "het streefniveau voor de KPI"),
        ])), after="Norm"),

    F(3, "Inkoop", "Meten van prestaties: KSF, KPI en norm", fig(
        "Eén doel op drie niveaus: elk niveau draagt bij aan het niveau erboven",
        stairs([
            ("Strategisch", "medewerkers zijn tevreden over hun werkomgeving"),
            ("Tactisch", "tevredenheid over de schoonmaak minimaal 7,5"),
            ("Operationeel", "90% van de schoonmaakmeldingen binnen 4 uur opgelost"),
        ], van=58, numbered=False, midden=True),
        noot="Dit FM-voorbeeld zit niet in de opdracht van de les; het laat alleen het principe zien.")),

    # ================================================================ week 3 recht
    F(3, "Recht", "Drempelbedragen", fig(
        "Drempelbedragen per 1 januari 2026, zonder btw (volgens de slide)",
        bars([
            dict(label="Werken, en concessies", segs=[(5404, "c1")], val="€5.404.000"),
            dict(label="Sociale en andere specifieke diensten", segs=[(750, "c1")], val="€750.000"),
            dict(label="Leveringen en diensten, andere aanbestedende diensten", sub="gemeenten, provincies, waterschappen, publiekrechtelijke instellingen", segs=[(216, "c1")], val="€216.000"),
            dict(label="Leveringen en diensten, centrale overheid", sub="Rijk, ministeries", segs=[(140, "c1")], val="€140.000"),
        ], maxv=5404, vw="6.5em", label="Drempelbedragen per type opdracht"),
        noot="De drempel voor werken is 25 keer zo hoog als die van €216.000. Daarom maakt het bij een gemengde opdracht zoveel uit of het een werk of een dienst is."),
      after="Type opdracht"),

    F(3, "Recht", "De waarde ramen", fig(
        "Rekenvoorbeeld: opties en verlengingen tellen mee",
        legend([("c1", "vaste contractjaren, €90.000 per jaar"), ("c2", "optiejaren, €90.000 per jaar"), ("ref", "drempel €216.000")]) + bars([
            dict(label="Goed: 2 jaar plus 2 optiejaren", segs=[(90, "c1"), (90, "c1"), (90, "c2"), (90, "c2")], val="€360.000", ref=216),
            dict(label="Fout: alleen de eerste 2 jaar", segs=[(90, "c1"), (90, "c1")], val="€180.000", ref=216),
        ], maxv=360, vw="5.5em", label="Raming van een schoonmaakcontract vergeleken met de drempel"),
        noot="Wie alleen de eerste twee jaar telt, komt ten onrechte onder de drempel uit (art. 2.15 lid 2 Aw)."),
      after="Rekenvoorbeeld"),

    F(3, "Recht", "Beoordelingsinstrumenten in vaste volgorde", fig(
        "De vaste volgorde: eerst de ondernemer, dan de inschrijving",
        phases([
            ("Gaat over de ondernemer", [
                ("Uitsluitings" + SH + "gronden", "mag deze ondernemer meedoen?"),
                ("Geschiktheids" + SH + "eisen", "kan deze ondernemer de opdracht aan?"),
                ("Selectie" + SH + "criteria", "wie mag inschrijven? Alleen bij twee fasen")], "t2"),
            ("Gaat over de inschrijving", [
                ("Technische specificaties", "voldoet het aangebodene?"),
                ("Gunnings" + SH + "criteria", "welke inschrijving is de beste?")], "t1"),
        ])), after="Deze volgorde kwam ook terug"),

    # ================================================================ week 4 recht
    F(4, "Recht", "Openbare procedure", fig(
        "Openbare procedure: één fase",
        flow([
            ("Aankondiging", "verzenden"),
            ("Sluiting", "volgens de slide minimaal 45 dagen na verzending"),
            ("Beoordelen", "selectie en gunning in één keer"),
            ("Afwijzingen", None),
            ("Gunning en contract", None),
        ])), after="Eén fase"),

    F(4, "Recht", "Niet-openbare procedure", fig(
        "Niet-openbare procedure: twee fasen",
        phases([
            ("Selectiefase: wie mag inschrijven?", [
                ("Aankondiging", None), ("Sluiting", "30 dagen voor verzoeken tot deelneming"),
                ("Evaluatie", "minimaal 5 selecteren"), ("Afwijzen", None)], "t2"),
            ("Inschrijvingsfase: welke offerte wint?", [
                ("Offerte" + SH + "aanvraag", None), ("Sluiting", "40 dagen voor inschrijvingen"),
                ("Evaluatie", None), ("Afwijzen", None), ("Gunning en contract", None)], "t1"),
        ], stack=True)), after="Twee fasen"),

    F(4, "Recht", "Mededingingsprocedure met onderhandeling", fig(
        "Het verschil in volgorde: dialoog of onderhandeling",
        lanes([
            ("Concurrentiegerichte dialoog", "inschrijven na de dialoog", [
                ("Selectie", "minimaal 3"), ("Dialoogrondes", "programma van eisen en oplossing vaststellen"),
                ("Inschrijving", "één per partij, niet onderhandelen"), ("Gunning", "altijd beste prijs-kwaliteitverhouding")]),
            ("Mededingingsprocedure met onderhandeling", "eerst inschrijven, dan onderhandelen", [
                ("Selectie", "minimaal 3"), ("Inschrijving", None),
                ("Onderhandelen", "geen cherry picking"), ("Gunning", "laagste prijs mag ook")]),
        ])), after="Grootste verschil"),

    F(4, "Recht", "Mededingingsprocedure met onderhandeling", fig(
        "Minimumtermijnen per procedure in dagen (volgens de slides)",
        legend([("c2", "verzoeken tot deelneming"), ("c1", "inschrijvingen")]) + bars([
            dict(label="Openbare procedure", segs=[(45, "c1")], val="45"),
            dict(label="Niet-openbare procedure", segs=[(30, "c2"), (40, "c1")], val="30 + 40"),
            dict(label="Mededingingsprocedure met onderhandeling", segs=[(30, "c2"), (40, "c1")], val="30 + 40"),
            dict(label="Concurrentiegerichte dialoog", sub="voor dialoog en inschrijving geen wettelijk minimum", segs=[(30, "c2")], val="30"),
        ], maxv=70, vw="4.5em", label="Minimumtermijnen in dagen per procedure"),
        noot="Dit zijn de getallen van de slides (art. 2.71 Aw). Zoek ze op in je wettenbundel: verkorten en verlengen kan onder voorwaarden.")),

    F(4, "Recht", "Rechtsbescherming", fig(
        "De standstill (Alcatel-termijn) op een tijdlijn",
        timeline([
            ("Dag 0", "Afwijzing verzonden", "met de redenen, volgens de vormvoorschriften van art. 2.130 Aw"),
            ("Dag 1 t/m 20", "Standstill", "nog geen definitieve gunning en geen overeenkomst; een verliezer kan een kort geding starten"),
            ("Kort geding?", "De standstill loopt door tot de uitspraak", "ook als de 20 dagen dan al voorbij zijn"),
            ("Daarna", "Definitieve gunning en overeenkomst", "voor een verliezer rest alleen nog de bodemprocedure"),
        ], breed="6.6em"),
        noot="Boven de drempel is de termijn 20 dagen (art. 2.127 Aw). Onder de drempel of bij uitgezonderde opdrachten geldt 15 dagen."),
      after="Standstill (Alcatel-termijn)"),

    # ================================================================ week 5 inkoop
    F(5, "Inkoop", "Wat is contractmanagement?", fig(
        "Contractmanagement bestaat uit twee delen",
        tree("Contractmanagement", [
            ("Contractbeheer", "het administratieve proces: registreren, beheren, archiveren en mutaties verwerken"),
            ("Prestatiemanagement", "de prestaties van de leverancier en de eigen organisatie meten en sturen"),
        ], rootsub="afspraken wederzijds doen nakomen, voor maximale waarde"))),

    F(5, "Inkoop", "De vijf pijlers van succesvol contractmanagement (NEVI)", fig(
        "De vijf pijlers in één beeld",
        pillars("Succesvol contractmanagement", [
            ("Governance", "het raamwerk: beleid, rollen en toezicht"),
            ("Contract" + SH + "administratie", "inzicht in verplichtingen, afspraken en mijlpalen"),
            ("Prestatie" + SH + "management", "meten en sturen met KPI's en SLA's"),
            ("Relatie" + SH + "management", "sterke relaties met alle stakeholders"),
            ("Leveranciers" + SH + "management", "samenwerking starten, onderhouden en ontwikkelen"),
        ]),
        noot="Gebruik de pijlers als kapstok in een casus: loop ze één voor één langs en zeg wat al op orde is en wat aandacht nodig heeft."),
      pos="top"),

    # ================================================================ week 5 recht
    F(5, "Recht", "Afgebroken onderhandelingen", fig(
        "Wat kun je vorderen als onderhandelingen onrechtmatig zijn afgebroken?",
        tree("Onrechtmatig afgebroken", [
            ("Dooronderhandelen", "geen contractsdwang; weinig kans als de afbreker al met een ander heeft gecontracteerd"),
            ("Schadevergoeding", None, [
                ("Negatief contractsbelang:", "de gemaakte kosten. Dit is het uitgangspunt."),
                ("Positief contractsbelang:", "de gederfde winst. Alleen bij hoge uitzondering.")]),
        ], rootsub="grondslag: onrechtmatige daad, art. 6:162 BW")),
      after="Vordering tot dooronderhandelen"),

    F(5, "Recht", "Algemene voorwaarden (art. 6:231 e.v. BW)", fig(
        "Twee gronden om een beding in de AV te vernietigen",
        tree("Vernietigbaar beding", [
            ("Sub a: onredelijk bezwarend", "gelet op alle omstandigheden"),
            ("Sub b: geen redelijke mogelijkheid tot kennisneming", "de AV zijn niet uiterlijk bij het sluiten ter hand gesteld (art. 6:234 BW)"),
        ], rootsub="art. 6:233 BW")),
      after="Sub a: onredelijk bezwarend"),

    F(5, "Recht", "Algemene voorwaarden (art. 6:231 e.v. BW)", fig(
        "Hoe kleiner de wederpartij, hoe meer bescherming tegen AV",
        stairs([
            ("Grote onderneming (art. 6:235 BW)", "alleen de redelijkheid en billijkheid, art. 6:248 lid 2 BW"),
            ("Onderneming met minder dan 50 werknemers", "art. 6:233 sub a en b, en art. 6:234 BW"),
            ("Kleine onderneming, vergelijkbaar met een consument", "ook de reflexwerking van de zwarte en grijze lijst"),
            ("Consument", "art. 6:233 en 6:234 BW plus de zwarte lijst (6:236) en de grijze lijst (6:237)"),
        ], van=62)), after="Type wederpartij"),

    F(5, "Recht", "Algemene voorwaarden (art. 6:231 e.v. BW)", fig(
        "Battle of forms: wie het eerst verwijst, wint",
        flow([
            ("A verwijst als eerste naar de eigen AV", "meesturen hoeft niet"),
            ("B verwijst naar de eigen AV", "dat is niet genoeg om die van A af te wijzen"),
            ("De AV van A gelden", "first-shot rule, tenzij B ze uitdrukkelijk van de hand wijst"),
        ])), after="Battle of forms"),

    # ================================================================ week 6 inkoop
    F(6, "Inkoop", "Groen versus circulair inkopen", fig(
        "Circulair is vaak een onderdeel van groen, maar niet hetzelfde",
        nest([
            ("Duurzaam of groen inkopen", "de milieu-impact verminderen"),
            ("Circulair inkopen", "de waarde van grondstoffen en producten zo lang mogelijk behouden: afval bestaat niet"),
        ]),
        noot="Groen zonder circulair kan dus: een energiezuinige printer die na gebruik wordt weggegooid.")),

    F(6, "Inkoop", "Fasemodel duurzaam inkopen", fig(
        "De zes fasen als trap: let op het motief",
        stairs([
            ("Ontkenning", "laagste prijs telt; duurzaamheid heet duur en complex"),
            ("Windowdressing", "alleen communicatie en imago"),
            ("Naleving wet- en regelgeving", "aanleiding: een incident of de wet"),
            ("Kostenbesparingen", "duurzaamheid verlaagt kosten en voorkomt reputatieschade"),
            ("Innovatie", "leveranciers uitdagen en samen nieuwe oplossingen maken"),
            ("Maatschappelijke waarde", "geïntegreerd in organisatie en keten, ingericht volgens ISO 20400"),
        ], van=44)), after="Herkennen in een casus"),

    F(6, "Inkoop", "NEVI-gedragscode 2026 en ethiek", fig(
        "De drie principes van de NEVI-gedragscode",
        pillars("NEVI-gedragscode: zelfregulering door de beroepsgroep", [
            ("Maatschappelijke waarde", "meerwaarde voor organisatie en maatschappij, met een langetermijnvisie"),
            ("Integriteit en objectiviteit", "geen belangenverstrengeling, beslissen op objectieve criteria"),
            ("Deskundigheid en verantwoording", "keuzes uitleggen en verantwoorden, ook bij cybersecurity en AI"),
        ], basis="Wederkerigheid: ook leveranciers houden zich aan de gedragsregels"))),

    # ================================================================ week 6 recht
    F(6, "Recht", "De koopovereenkomst", fig(
        "Wanneer is het consumentenkoop?",
        som([
            ("Roerende zaak", None),
            ("Koper is particulier", "handelt niet in de uitoefening van een beroep of bedrijf"),
            ("Verkoper is professional", "handelt wel in de uitoefening van een beroep of bedrijf"),
        ], ("Consumentenkoop", "grotendeels dwingend recht, art. 7:5 en 7:6 BW")),
        noot="Mist één onderdeel, dan is het een gewone koop en is Titel 1 regelend recht. Een woning is geen roerende zaak, dus nooit consumentenkoop."),
      after="Consumentenkoop (art. 7:5 BW)"),

    F(6, "Recht", "Conformiteit (art. 7:17 BW)", fig(
        "De zaak is niet conform: wat kan de koper eisen?",
        tree("Niet conform", [
            ("Aflevering van het ontbrekende", None),
            ("Herstel", None),
            ("Vervanging", None),
        ], rootsub="de zaak voldoet niet aan de redelijke verwachtingen, art. 7:17 BW"),
        noot="Op kosten van de verkoper (art. 7:21 BW). Daarnaast gelden de rechten uit Boek 6, zoals ontbinding en schadevergoeding. Klaag wel binnen bekwame tijd (art. 7:23 BW)."),
      after="Rechten bij non-conformiteit"),

    F(6, "Recht", "Koop op afstand", fig(
        "De termijnen bij koop naast elkaar",
        bars([
            dict(label="Ontbinden bij koop op afstand", sub="art. 6:230o BW", segs=[(14 / 30.4, "c1")], val="14 dagen"),
            dict(label="Recht van reclame", sub="art. 7:39 BW: 6 weken na opeisbaarheid én 60 dagen na aflevering", segs=[(60 / 30.4, "c1")], val="60 dagen"),
            dict(label="Klagen na ontdekking van het gebrek, consument", sub="art. 7:23 BW", segs=[(2, "c1")], val="2 maanden"),
            dict(label="Bewijsvermoeden bij een gebrek, consument", sub="art. 7:18 lid 2 BW, termijn volgens de slide", segs=[(6, "c1")], val="6 maanden"),
            dict(label="Verjaring van de betaling, consumentenkoop", sub="art. 7:28 BW", segs=[(24, "c1")], val="2 jaar"),
        ], maxv=24, vw="5.5em", label="Lengte van de termijnen bij koop"),
        noot="De termijnen beginnen niet op hetzelfde moment: let per artikel op het startpunt (aflevering, ontdekking of opeisbaarheid). Is niet aan de informatieplicht voldaan, dan loopt de 14 dagen op tot 12 maanden.")),

    F(6, "Recht", "Eigendomsoverdracht", fig(
        "Drie voorwaarden voor eigendomsoverdracht",
        som([
            ("Geldige titel", "bv. een geldige koopovereenkomst"),
            ("Beschikkings" + SH + "bevoegdheid", "mag de vervreemder over de zaak beschikken?"),
            ("Levering", "roerend: art. 3:90 BW; onroerend: notariële akte en Kadaster, art. 3:89 BW"),
        ], ("Eigendom gaat over", "art. 3:84 BW; betaling is geen voorwaarde"))),
      after="Geldige titel"),

    F(6, "Recht", "Eigendomsoverdracht", fig(
        "Levering zonder feitelijke overdracht: bij wie is de zaak?",
        pgrid(["Verkoper", "Koper", "Derde"], [
            ("Constitutum possessorium", [("houdt de zaak zelf", "nu als houder voor de koper"), None, None]),
            ("Brevi manu", [None, ("had de zaak al", "was houder en wordt nu eigenaar"), None]),
            ("Longa manu", [None, None, ("houdt de zaak", "gaat nu voor de koper houden")]),
        ]),
        noot="In alle drie de gevallen verplaatst de zaak niet, maar gaat de eigendom wel over (art. 3:115 BW)."),
      after="Constitutum possessorium"),

    # ================================================================ week 7
    F(7, "Recht", "Antwoordmodellen", fig(
        "Welke week zit in welke vraag van de oefentoets?",
        bars([
            dict(label="Week 1: beginselen", sub="vraag 5", segs=[(1, "c1")], val="1 vraag"),
            dict(label="Week 2: wie, wat en raamovereenkomst", sub="vraag 1, 2 en 3", segs=[(3, "c1")], val="3 vragen"),
            dict(label="Week 3: waarde en beoordelingsinstrumenten", sub="vraag 1, 4 en 7", segs=[(3, "c1")], val="3 vragen"),
            dict(label="Week 4: procedures en rechtsbescherming", sub="vraag 3, 4, 6, 7, 8 en 9", segs=[(6, "c1")], val="6 vragen"),
            dict(label="Week 5: algemene voorwaarden", sub="vraag 12", segs=[(1, "c1")], val="1 vraag"),
            dict(label="Week 6: koop en eigendom", sub="vraag 10 en 11", segs=[(2, "c1")], val="2 vragen"),
        ], maxv=6, vw="5em", label="Aantal vragen van de oefentoets per week"),
        noot="Dit is mijn eigen indeling van de 12 vragen; sommige vragen raken twee weken en tellen dan twee keer mee. Het aanbestedingsrecht van week 2 tot en met 4 weegt in deze oefentoets het zwaarst."),
      pos="top"),
]
