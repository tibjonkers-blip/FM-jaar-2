"""Figuren en grafieken bij de samenvattingen van HRM voor de FM-professional.

Elke figuur herhaalt wat in de samenvatting van die les staat. Waar de samenvatting zegt dat iets de gangbare invulling is
(omdat de slide een afbeelding was), staat dat ook in de noot onder de figuur.
"""
from lib import *

SH = "­"  # zacht afbreekteken voor lange woorden in smalle kolommen

# ---- eigen svg: twee jaar verzuim op één lijn (2,6 px per week, week 0 op x=14). Labels op twee regels, zodat ze op een telefoon leesbaar blijven.
def _lab(x, y, week, tekst, eind=False):
    a = ' text-anchor="end"' if eind else ""
    return f'<text x="{x}" y="{y}"{a} class="bold">{week}</text><text x="{x}" y="{y + 14}"{a}>{tekst}</text>'

WVP = svg(
    '<rect class="f1" x="14" y="92" width="134.2" height="16" rx="3"/><rect class="f2" x="150.2" y="92" width="134.2" height="16" rx="3"/>'
    # boven de staaf: week 6, 42 en 91
    '<path class="ax" d="M29.6 92V30M123.2 92V58M250.6 92V86"/>'
    + _lab(29.6, 12, "week 6", "probleemanalyse") + _lab(123.2, 40, "week 42", "melding bij het UWV") + _lab(284.4, 68, "week 91", "verslag naar het UWV", eind=True)
    # onder de staaf: week 104, 52 en 8
    + '<path class="ax" d="M284.4 108V114M149.2 108V142M34.8 108V170"/>'
    + _lab(284.4, 126, "week 104", "einde wachttijd", eind=True) + _lab(149.2, 154, "week 52", "eerstejaarsevaluatie") + _lab(34.8, 182, "week 8", "plan van aanpak"),
    w=300, h=200, label="Tijdlijn van 104 weken ziekte. Week 6 probleemanalyse, week 8 plan van aanpak, week 42 melding bij het UWV, "
    "week 52 eerstejaarsevaluatie, week 91 re-integratieverslag naar het UWV, week 104 einde van de wachttijd.")

FIGUREN = [
    # ================================================================ overzicht
    F(0, "Overzicht", None, fig(
        "Lestijd per lijn: de workshops krijgen de meeste uren",
        bars([
            dict(label="Theoriecolleges HRM", sub="6 weken van 2 lesuren", segs=[(12, "c1")], val="12 lesuren"),
            dict(label="Theoriecolleges Arbeidsrecht", sub="6 weken van 2 lesuren", segs=[(12, "c1")], val="12 lesuren"),
            dict(label="Workshops Gespreksvoering", sub="7 weken van 3 lesuren", segs=[(21, "c1")], val="21 lesuren"),
        ], maxv=21, vw="6em", label="Lesuren per lijn"),
        noot="Uitgerekend uit de tabel hierboven. In het mondeling telt elke lijn even zwaar: 10 minuten per onderdeel."),
      after="Workshops Gespreksvoering"),

    # ================================================================ week 1 theorie
    F(1, "Theoriecollege", "Vier niveaus van HRM", fig(
        "Vier niveaus: van spelregels van buitenaf naar de dagelijkse aansturing",
        stairs([
            ("Institutioneel", "spelregels van buitenaf: vakbonden, overheid, SER, sectorafspraken"),
            ("Strategisch", "richting en continuïteit van de organisatie, gericht op de toekomst"),
            ("Tactisch of organisatorisch", "HR-beleid inrichten en maatregelen implementeren"),
            ("Operationeel", "dagelijkse aansturing door de direct leidinggevende: aannemen, begeleiden, beoordelen"),
        ]),
        noot="Als facility manager zit je vooral op de onderste trede, met invloed op het tactische niveau."),
      after="Soort regulering"),

    F(1, "Theoriecollege", "Michigan versus Harvard", fig(
        "Hard en zacht HRM naast elkaar",
        '<div class="lanes"><div class="lane"><h5>Michigan <small>hard HRM: prestatie, controle en organisatiebelang</small></h5>'
        + flow(["Selectie", "Prestatie", "Beoordeling", "Beloning en ontwikkeling"])
        + '</div><div class="lane"><h5>Harvard <small>soft HRM: stakeholders, betrokkenheid en welzijn</small></h5>'
        + cards([(None, "Werk" + SH + "systemen", None), (None, "Belonings" + SH + "systemen", None), (None, "Personeels" + SH + "stromen", None), (None, "Werknemers" + SH + "invloed", None)], cols=4)
        + "</div></div>",
        noot="Michigan is een cyclus van vier stappen, Harvard bestaat uit vier beleidsgebieden zonder volgorde. De vier stappen zijn de gangbare weergave van Fombrun; de slide toont ze als afbeelding."),
      after="FM-voorbeeld"),

    F(1, "Theoriecollege", "Werving en selectie", fig(
        "Werving en selectie in vijf fasen",
        flow([
            ("Voorbereiding", "functieprofiel en competentieprofiel"),
            ("Werving", "doelgroep en wervingsmix van kanalen"),
            ("Sollicitatie", "contact en informatie uitwisselen"),
            ("Selectie", "toekomstig werkgedrag voorspellen"),
            ("Onboarding", "inwerkplan, zelf begeleiden of een buddy"),
        ]),
        noot="Je rol is het grootst bij stap 4: daar ben je meestal beslissingsbevoegd. Bij stap 2 is je rol klein."),
      after="Rol facility manager"),

    F(1, "Theoriecollege", "Werving en selectie", fig(
        "STARR: vijf vragen over één echte situatie",
        flow([
            ("Situatie", "wat speelde er?"),
            ("Taak", "wat was jouw verantwoordelijkheid?"),
            ("Actie", "wat deed jij concreet?"),
            ("Resultaat", "wat leverde dat op?"),
            ("Reflectie", "wat heb je geleerd?"),
        ], numbered=False),
        noot="Gedrag uit het verleden is de beste voorspeller van toekomstig gedrag. De vragen per letter komen uit workshop 2."),
      after="STAR(R)-methode"),

    # ================================================================ week 1 arbeidsrecht
    F(1, "Arbeidsrecht", "Soorten recht in het arbeidsrecht", fig(
        "Hoe verder op de trap, hoe minder je mag afwijken",
        stairs([
            ("Aanvullend recht", "afwijken mag op iedere manier"),
            ("Semidwingend recht", "alleen bij schriftelijke overeenkomst"),
            ("5/8e dwingend recht", "alleen bij overeenkomst tussen werkgever en ondernemingsraad"),
            ("Driekwartdwingend recht", "alleen bij cao"),
            ("Dwingend recht", "nooit: een afwijkend beding is nietig"),
        ])),
      after="Herken je aan de wettekst"),

    F(1, "Arbeidsrecht", "De arbeidsovereenkomst: art. 7:610 BW", fig(
        "Vier elementen maken samen een arbeidsovereenkomst",
        som([
            ("Arbeid", "persoonlijk verricht"),
            ("Loon", "tegenprestatie van de werkgever"),
            ("Zekere tijd", "geen onderscheidend criterium"),
            ("Gezag", "meestal het beslissende element"),
        ], ("Arbeids" + SH + "overeenkomst", "art. 7:610 BW")),
        noot="Kijk naar alle omstandigheden van het geval en niet naar het etiket op het contract (Groen/Schoevers)."),
      after="In dienst van (gezag)"),

    F(1, "Arbeidsrecht", "Andere overeenkomsten waarbij arbeid wordt verricht", fig(
        "Wat geldt alleen bij een arbeidsovereenkomst?",
        cards([
            (None, "Dwingend recht", "vakantie, verlof, loon, loondoorbetaling bij ziekte en ontslag"),
            (None, "Werknemers" + SH + "verzekeringen", "ZW, WIA en WW"),
            (None, "Cao en pensioen", "de toepasselijke cao en pensioenregeling"),
        ]),
        noot="Bij opdracht (art. 7:400 BW) en aanneming van werk (art. 7:750 BW) ontbreekt het gezag, en daarmee ook deze bescherming.")),

    # ================================================================ week 1 workshop
    F(1, "Workshop", "Het communicatiemodel", fig(
        "Van zender naar ontvanger en weer terug",
        flow([
            ("Zender codeert", "zet de boodschap om in woorden en gebaren"),
            ("Boodschap", "verbaal of non-verbaal"),
            ("Ontvanger decodeert", "geeft betekenis vanuit het eigen referentiekader"),
        ], loop="daarna wisselen de rollen"),
        noot="In het voorbeeld uit de les ontstaat het misverstand bij stap 3. Doorvragen of samenvatten had het voorkomen.")),

    F(1, "Workshop", "Vragen stellen", fig(
        "Vijf ezelsbruggetjes voor het luisteren",
        cards([
            ("LSD", "Luisteren, Samenvatten, Doorvragen", None),
            ("OEN", "Open, Eerlijk, Nieuwsgierig", None),
            ("ANNA", "Altijd Navragen, Nooit Aannemen", None),
            ("NIVEA", "Niet Invullen Voor Een Ander", None),
            ("OMA", "Oordeel, Mening en Advies thuislaten", None),
        ], cols=5),
        noot="De slide noemt alleen de afkortingen; dit zijn de gangbare betekenissen.")),

    F(1, "Workshop", "Drie soorten gespreksvaardigheden", fig(
        "Een goed gesprek rust op drie soorten vaardigheden",
        pillars("Het gesprek met de acteur", [
            ("Luisteren", "actief luisteren, samenvatten, doorvragen, aandacht tonen"),
            ("Reguleren", "openen, richting geven, structuur bewaken, afronden"),
            ("Zenden", "duidelijk communiceren, informatie geven, uitleggen, feedback geven"),
        ], basis="In het tentamengesprek laat je alle drie zien"))),

    # ================================================================ week 2 theorie
    F(2, "Theoriecollege", "Beoordelen", fig(
        "De gesprekscyclus door het jaar",
        timeline([
            ("Begin", "Planningsgesprek", "prestatie- en ontwikkeldoelen voor de nieuwe periode afspreken"),
            ("Halverwege", "Functioneringsgesprek", "vooruitgang en obstakels bekijken"),
            ("Einde", "Beoordelingsgesprek", "prestaties beoordelen en nieuwe doelen bepalen"),
        ], breed="5.4em"),
        noot="Daarnaast noemt de slide het persoonlijk ontwikkelingsgesprek, vaak met een POP."),
      after="Planningsgesprek"),

    F(2, "Theoriecollege", "Beoordelen", fig(
        "Twee paren beoordelingsfouten die je makkelijk verwisselt",
        poles([
            ("Welk moment weegt te zwaar?", ("Primacy-effect", "de eerste indruk"), ("Recency-effect", "wat het laatst gebeurde")),
            ("Welke eigenschap kleurt het hele oordeel?", ("Halo-effect", "één positieve eigenschap"), ("Horn-effect", "één negatieve eigenschap")),
        ]),
        noot="De slide noemt alleen de namen; de uitleg is de gangbare betekenis. De andere zes fouten staan in de tabel."),
      after="Centrale tendentie"),

    F(2, "Theoriecollege", "Opleiden en ontwikkelen", fig(
        "Zes vormen van leren: je leert door te…",
        cards([
            ("doen", "Informeel leren op het werk", None),
            ("delen", "Leren via netwerken", None),
            ("vernieuwen", "Leren door innovaties en projecten", None),
            ("begeleiden", "Formeel opleiden op de werkplek", None),
            ("samenwerken", "Teamleren", None),
            ("studeren", "Cursussen en opleidingen", None),
        ], cols=3),
        noot="Meestal gebruik je een combinatie; de vormen versterken elkaar."),
      after="Vorm van leren"),

    F(2, "Theoriecollege", "Belonen", fig(
        "Vier grondslagen voor beloning",
        tree("Beloning", [
            ("Functie", "vast inkomen", ["basissalaris", "vakantiegeld", "dertiende maand"]),
            ("Prestatie", "variabel inkomen", ["prestatiebonus", "winstdeling", "sales incentive"]),
            ("Lidmaat" + SH + "schap", "secundaire arbeids" + SH + "voorwaarden"),
            ("Omstandig" + SH + "heden", "toeslagen", ["ORT", "consignatie", "overwerk"]),
        ], rootsub="contract, aantrekken en behouden, sturen"),
        noot="In de praktijk combineer je de grondslagen."),
      after="Grondslag"),

    # ================================================================ week 2 arbeidsrecht
    F(2, "Arbeidsrecht", "Flexibele arbeidsrelaties", fig(
        "De bescherming van een oproepkracht in de tijd",
        timeline([
            ("4 dagen vooraf", "Oproepen", "schriftelijk of elektronisch; dan moet de werknemer komen (art. 7:628a lid 2)"),
            ("Later ingetrokken", "Toch loon", "intrekken kan zonder loon tot uiterlijk vier dagen van tevoren (lid 3)"),
            ("Na 12 maanden", "Aanbod voor een vaste omvang", "binnen een maand, gelijk aan het gemiddelde van die 12 maanden; een maand bedenktijd (lid 5)"),
            ("Geen aanbod", "Recht op loon", "over de gemiddelde omvang (lid 8)"),
        ], breed="7.2em"),
        noot="Geldt alleen als de overeenkomst onder de definitie van art. 7:628a lid 9 BW valt. Bij cao mag de termijn van vier dagen korter."),
      after="7:628a lid 8"),

    F(2, "Arbeidsrecht", "Werving en selectie en gelijke behandeling", fig(
        "De Awgb als ladder: mag dit onderscheid?",
        ladder([
            ("Is het direct onderscheid?", "Iemand wordt rechtstreeks anders behandeld op grond van bijvoorbeeld godsdienst, ras of geslacht (art. 1 lid 1 sub b).", "Ja: verboden, tenzij een uitzondering uit stap 4 geldt"),
            ("Is het indirect onderscheid?", "Een neutrale regel treft in feite vooral een bepaalde groep (sub c).", "Nee: geen onderscheid in de zin van de Awgb"),
            ("Is er een objectieve rechtvaardiging?", "Een legitiem doel én een middel dat passend en noodzakelijk is (art. 2).", "Ja: het indirecte onderscheid is toegestaan"),
            ("Geldt een andere uitzondering?", "Art. 2 lid 2 sub a en b, art. 3 en art. 5 lid 2 Awgb.", "Ja: toegestaan"),
        ], slot="Geen rechtvaardiging en geen uitzondering: verboden onderscheid", stop=True),
        noot="Bij de Wgbl kan ook direct onderscheid naar leeftijd objectief gerechtvaardigd worden."),
      after="Andere uitzonderingen"),

    # ================================================================ week 2 workshop
    F(2, "Workshop", "Zes fasen van het sollicitatiegesprek", fig(
        "Een professionele opening in zes stappen",
        flow([
            "Verwelkom de kandidaat", "Stel de gespreks" + SH + "partners voor", "Noem doel en duur",
            "Leg de opbouw uit", "Vraag toestemming voor aantekeningen", "Begin met een open vraag",
        ], cols=3)),
      after="Een professionele opening"),

    # ================================================================ week 3 arbeidsrecht
    F(3, "Arbeidsrecht", "Bijzondere bedingen", fig(
        "Wanneer is een concurrentiebeding geldig?",
        som([
            ("Schriftelijk", None),
            ("Meerderjarige werknemer", None),
            ("Onbepaalde tijd", "bij bepaalde tijd alleen met een motivering van zwaarwegende bedrijfs- of dienstbelangen"),
        ], ("Geldig beding", "art. 7:653 lid 1 en 2 BW")),
        noot="Ook een geldig beding kan de rechter geheel of gedeeltelijk vernietigen (lid 3)."),
      after="de rechter kan een vergoeding toekennen"),

    F(3, "Arbeidsrecht", "Overgang van onderneming (OvO)", fig(
        "Kapitaal- of arbeidsintensief: waar kijk je naar?",
        poles([
            ("Wat moet zijn overgenomen?", ("Kapitaal" + SH + "intensief", "de belangrijke bedrijfsmiddelen, zoals bussen of keukens"), ("Arbeids" + SH + "intensief", "een wezenlijk deel van het personeel, zoals bij schoonmaak")),
        ]),
        noot="Dit is de gangbare lijn uit Liikenne, Sodexho en Clece; de uitwerking staat niet op de slide. De Spijkers-factoren weeg je altijd samen."),
      after="Handvat"),

    F(3, "Arbeidsrecht", "Overgang van onderneming (OvO)", fig(
        "Drie gevolgen van een overgang van onderneming",
        tree("Overgang van onderneming", [
            ("Rechten en plichten gaan over", "van rechtswege, art. 7:663 BW"),
            ("Oude werkgever blijft aansprakelijk", "nog één jaar, naast de nieuwe werkgever"),
            ("Opzegverbod", "wegens de overgang, art. 7:670 lid 8 BW"),
        ], rootsub="een economische eenheid die haar identiteit behoudt, art. 7:662 BW"),
        noot="Een OvO is er snel: ook bij een nieuwe aanbesteding, een nieuw schoonmaakbedrijf of een nieuwe cateraar."),
      after="Opzegverbod"),

    # ================================================================ week 3 workshop
    F(3, "Workshop", "Waarden en gewoontes", fig(
        "Waarde of gewoonte?",
        poles([
            ("Wat beschrijft het?", ("Waarde", "wat belangrijk is: respect, veiligheid, integriteit, gelijkwaardigheid"), ("Gewoonte", "hoe de organisatie dat nu doet: overleg om 9.00 uur, informele dresscode")),
            ("Kun je erover onderhandelen?", ("Minder", "de waarde erachter blijft staan"), ("Ja", "een gewoonte kun je anders afspreken")),
        ]))),

    F(3, "Workshop", "Van verschil naar werkbare afspraak (zeven stappen)", fig(
        "Eerst begrijpen, dan begrenzen of bijsturen",
        phases([
            ("Eerst begrijpen", ["Benoem feitelijk gedrag", "Onderzoek het perspectief", "Vat samen en controleer"], "t1"),
            ("Dan begrenzen of bijsturen", ["Benoem het organisatiebelang", "Verken mogelijkheden", "Maak een concrete afspraak", "Plan een evaluatiemoment"], "t2"),
        ]),
        noot="De zeven stappen en het motto komen van de slide; de verdeling in twee groepen is mijn eigen indeling."),
      after="Motto"),

    # ================================================================ week 4 theorie
    F(4, "Theoriecollege", "Motivatietheorieën", fig(
        "Zelfdeterminatietheorie: drie basisbehoeften dragen de motivatie",
        pillars("Gemotiveerde medewerker", [
            ("Autonomie", "controle over eigen keuzes"),
            ("Competentie", "vertrouwen in eigen kunnen"),
            ("Verbonden" + SH + "heid", "ergens bij horen"),
        ], basis="Ryan en Deci: alle drie de behoeften moeten vervuld zijn"))),

    F(4, "Theoriecollege", "Motivatietheorieën", fig(
        "Twee soorten factoren: de ene voorkomt ontevredenheid, de andere geeft tevredenheid",
        poles([
            ("Wat doet de factor?", ("Hygiëne" + SH + "factoren", "voorkomen ontevredenheid: salaris, arbeidsomstandigheden, beleid"), ("Motivatoren", "zorgen voor tevredenheid: erkenning, verantwoordelijkheid, groei, het werk zelf")),
        ]),
        noot="Vermoedelijk de twee-factorentheorie van Herzberg; de slide is een afbeelding. Dus eerst de basis op orde, dan erkenning en groei.")),

    F(4, "Theoriecollege", "Motivatietheorieën", fig(
        "Verwachtingstheorie: drie schakels tussen inspanning en motivatie",
        flow([
            ("Inspanning", "leidt dit tot een prestatie?"),
            ("Prestatie", "leidt die tot een beloning?"),
            ("Beloning", "vind ik die waardevol?"),
        ], numbered=False),
        noot="Iemand zet zich pas in als alle drie de antwoorden ja zijn. Vermoedelijk de theorie van Vroom; de slide noemt de naam niet.")),

    F(4, "Theoriecollege", "De interventiekaart", fig(
        "Drie termen die vaak door elkaar gaan",
        cards([
            (None, "Taakroulatie", "wisselen tussen taken"),
            (None, "Taakverbreding", "meer taken op hetzelfde niveau"),
            (None, "Taakverrijking", "meer verantwoordelijkheid en zeggenschap (verticaal)"),
        ]),
        noot="Dit is de gangbare betekenis; de slide noemt alleen de termen.")),

    F(4, "Theoriecollege", "Teams", fig(
        "De ontwikkelfasen van een team",
        flow([
            ("Forming", "kennismaken"),
            ("Storming", "strijd om rollen"),
            ("Norming", "afspraken en normen"),
            ("Performing", "presteren"),
            ("Adjourning", "afscheid"),
        ]),
        noot="Gangbare invulling volgens Tuckman; de slide is een afbeelding. Controleer de fasen in de les.")),

    F(4, "Theoriecollege", "Teams", fig(
        "Drie groepen succesfactoren voor een team",
        tree("Effectief team", [
            ("Context", None, ["middelen", "leiderschap", "vertrouwen", "beloning"]),
            ("Samenstelling", None, ["vaardigheden", "rollen", "omvang", "diversiteit"]),
            ("Proces", None, ["gemeenschappelijk doel", "specifieke doelen", "geloof in het team", "gezond conflictniveau"]),
        ]),
        noot="Gangbare invulling; ook deze slide is een afbeelding.")),

    F(4, "Theoriecollege", "Effectief leiderschap", fig(
        "Situationeel leiderschap: vier stijlen op twee assen",
        quad("Ondersteuning", "Sturing", [
            ("S3 Participeren of steunen", "weinig sturing, veel ondersteuning", "De medewerker kan het, maar twijfelt soms", "t3"),
            ("S2 Overtuigen of coachen", "veel sturing, veel ondersteuning", "Enige ervaring, de motivatie wisselt", "t2"),
            ("S4 Delegeren", "weinig sturing, weinig ondersteuning", "Ervaren en zelfstandig", "t0"),
            ("S1 Instrueren", "veel sturing, weinig ondersteuning", "Weinig ervaring, wel enthousiast", "t1"),
        ], ylaag="weinig", yhoog="veel", xlaag="weinig", xhoog="veel"),
        noot="Gangbare indeling van Hersey en Blanchard; de vier stijlen staan niet in de tekst van de slide. Groeit de medewerker, dan schuif je van S1 via S2 en S3 naar S4."),
      after="S4 Delegeren"),

    # ================================================================ week 4 arbeidsrecht
    F(4, "Arbeidsrecht", "Ziekte: art. 7:629 BW", fig(
        "Loonstaking of loonopschorting?",
        poles([
            ("Wat is er aan de hand?", ("Loonstaking", "een uitsluitingsgrond (lid 3): ziekte opzettelijk veroorzaakt, genezing belemmerd, passende arbeid geweigerd"), ("Loon" + SH + "opschorting", "een controlevoorschrift overtreden (lid 6): bijvoorbeeld niet naar de bedrijfsarts gaan")),
            ("Komt het loon er later alsnog?", ("Nee", "ook niet met terugwerkende kracht"), ("Ja", "met terugwerkende kracht zodra de werknemer zich er weer aan houdt")),
        ]),
        noot="In beide gevallen moet de werkgever eerst waarschuwen (lid 7)."),
      after="Wachtdagen"),

    F(4, "Arbeidsrecht", "Ziekte: art. 7:629 BW", fig(
        "Loondoorbetaling bij ziekte: 104 weken in twee helften",
        seg([
            (52, "c1", "Week 1 t/m 52: 70% van het loon", "maar minimaal het minimumloon"),
            (52, "c2", "Week 53 t/m 104: 70% van het loon", "ook als dat onder het minimumloon ligt"),
        ]),
        noot="Het maximum is 70% van het maximum dagloon. Heeft de werkgever te weinig aan re-integratie gedaan, dan kan het UWV de loondoorbetaling met maximaal een jaar verlengen."),
      after="Wachtdagen"),

    F(4, "Arbeidsrecht", "Vakantie", fig(
        "Wettelijke en bovenwettelijke vakantiedagen naast elkaar",
        pgrid(["Wettelijke dagen", "Bovenwettelijke dagen"], [
            ("Hoeveel?", [("4 keer de arbeidsduur per week", "bij 5 dagen per week dus 20 dagen, art. 7:634"), ("wat contract of cao daarbovenop geeft", None)]),
            ("Afkopen tijdens het dienstverband?", [("Nee", "art. 7:640"), ("Ja", None)]),
            ("Wanneer ben je ze kwijt?", [("Ze vervallen een half jaar na het opbouwjaar", "art. 7:640a"), ("Ze verjaren 5 jaar na het opbouwjaar", "art. 7:642")]),
            ("Ziektedagen als vakantie aanmerken?", [("Nee", "art. 7:637 en 7:638 lid 8"), ("Alleen met instemming of vooraf in het contract", None)]),
        ]),
        noot="Bij het einde van het dienstverband worden alle dagen uitbetaald (art. 7:641 lid 1)."),
      after="7:645"),

    F(4, "Arbeidsrecht", "Verlof (WAZO)", fig(
        "Vijf verloven vergeleken: hoe lang en wie betaalt?",
        legend([("c1", "loon van de werkgever"), ("c2", "uitkering via het UWV"), ("c3", "onbetaald")]) + bars([
            dict(label="Geboorteverlof", sub="binnen 4 weken, art. 4:2", segs=[(1, "c1")], val="1 keer"),
            dict(label="Kortdurend zorgverlof", sub="per 12 maanden, 70% loon, art. 5:1", segs=[(2, "c1")], val="2 keer"),
            dict(label="Aanvullend geboorteverlof", sub="binnen 6 maanden, art. 4:2a", segs=[(5, "c2")], val="5 keer"),
            dict(label="Langdurend zorgverlof", sub="per 12 maanden, art. 5:9", segs=[(6, "c3")], val="6 keer"),
            dict(label="Ouderschapsverlof", sub="per kind, tot het kind 8 is, art. 6:1", segs=[(9, "c2"), (17, "c3")], val="26 keer"),
        ], maxv=26, vw="4.6em", label="Duur van vijf soorten verlof in aantal keer de arbeidsduur per week"),
        noot="De lengte is steeds het aantal keer de arbeidsduur per week. Bij ouderschapsverlof is er voor 9 weken een uitkering als je ze opneemt voor het kind 1 jaar is. De andere verloven staan in de tabel."),
      after="Ouderschapsverlof"),

    F(4, "Arbeidsrecht", "Verlof (WAZO)", fig(
        "Zwangerschaps- en bevallingsverlof bij één kind",
        seg([
            (6, "c1", "Zwangerschapsverlof: 6 weken", "voor de vermoedelijke bevallingsdatum, uiterlijk 4 weken ervoor"),
            (10, "c2", "Bevallingsverlof: 10 weken", "plus de dagen die het zwangerschapsverlof korter was dan 6 weken"),
        ]),
        noot="Bij een meerling is het zwangerschapsverlof 10 weken, uiterlijk 8 weken voor de datum. De uitkering loopt via het UWV (art. 3:8 WAZO)."),
      after="Ouderschapsverlof"),

    # ================================================================ week 4 workshop
    F(4, "Workshop", "Drie soorten gesprekken", fig(
        "Drie gesprekken, drie kijkrichtingen",
        cards([
            ("terugkijken", "Beoordelings" + SH + "gesprek", "een oordeel over de afgelopen periode, van leidinggevende naar medewerker"),
            ("nu", "Functionerings" + SH + "gesprek", "hoe gaat het werk en wat heb je nodig; tweerichtingsverkeer"),
            ("vooruitkijken", "Ontwikkel" + SH + "gesprek", "talenten, ambities en loopbaan; tweerichtingsverkeer"),
        ]),
        noot="Gangbare uitleg; de slide geeft het antwoord niet. Alleen het beoordelingsgesprek kan gevolgen hebben voor beloning of contract."),
      after="Functioneringsgesprek"),

    F(4, "Workshop", "Gespreksstructuur", fig(
        "Het inhoudelijke deel van een ontwikkelgesprek",
        flow([
            ("Huidige situatie", "waar staat de medewerker nu?"),
            ("Ontwikkel" + SH + "mogelijkheden", "sterke punten en ontwikkelpunten"),
            ("Toekomst" + SH + "perspectief", "waar over drie tot vier jaar?"),
            ("Acties", "een SMART-afspraak en een datum om terug te kijken"),
        ]),
        noot="De vier stappen komen van de slide; de vragen erbij zijn uit de voorbereiding en de tip voor het tentamengesprek."),
      after="Acties"),

    # ================================================================ week 5 theorie
    F(5, "Theoriecollege", "Wat is diversiteit?", fig(
        "Diversiteit als ijsberg",
        iceberg("Leeftijd, geslacht, huidskleur of etniciteit, uiterlijk en kleding, taalaccent", [
            "waarden en overtuigingen", "werkstijl", "communicatiestijl", "houding tegenover autoriteit", "motivatie", "normen en verwachtingen over werk"],
            bovenkop="Boven water: surface-level", onderkop="Onder water: deep-level"),
        noot="De ijsberg is mijn eigen beeld bij de tabel. Deep-level verschillen worden pas later duidelijk en worden dan snel als onwil uitgelegd."),
      after="Surface-level diversity"),

    F(5, "Theoriecollege", "Waarom ontstaat wij-zij-denken?", fig(
        "Sociale identiteitstheorie in drie stappen",
        flow([
            ("Sociale categorisatie", "we delen mensen automatisch in groepen in"),
            ("Sociale identificatie", "je hoort bij een in-group en ontleent er eigenwaarde aan"),
            ("Sociale vergelijking", "je beoordeelt de eigen groep positiever dan de out-group"),
        ]),
        noot="Het gevaar na stap 3: wij-zij-denken en polarisatie.")),

    F(5, "Theoriecollege", "Wat doe je eraan?", fig(
        "Contact werkt alleen onder zes voorwaarden",
        chips(["gelijke status", "weerlegde stereotypen", "gemeenschappelijke doelen", "gelijkheidsbevorderende normen",
               "superieuren die de naleving bewaken", "daadwerkelijk contact"]),
        noot="Contacthypothese: door persoonlijk contact vallen de overeenkomsten tussen groepen meer op."),
      after="Contacthypothese"),

    F(5, "Theoriecollege", "Inclusief leiderschap", fig(
        "Zes kenmerken van inclusief leiderschap",
        cards([
            (None, "Zichtbare betrokkenheid", "authentieke toewijding"),
            (None, "Nederigheid", "fouten toegeven"),
            (None, "Bewustzijn van vooroordelen", "zicht op je eigen blinde vlek"),
            (None, "Nieuwsgierigheid", "luisteren zonder oordeel"),
            (None, "Culturele intelligentie", "aandacht voor andermans cultuur"),
            (None, "Effectieve samenwerking", "psychologische veiligheid en teamcohesie"),
        ], cols=3))),

    # ================================================================ week 5 arbeidsrecht
    F(5, "Arbeidsrecht", "De vier manieren", fig(
        "Vier manieren waarop een arbeidsovereenkomst eindigt",
        tree("Einde van de arbeids" + SH + "overeenkomst", [
            ("Van rechts" + SH + "wege", "het tijdelijke contract loopt af (7:667, 7:668a)"),
            ("Wederzijds goedvinden", "samen het einde afspreken (7:670b)"),
            ("Opzegging", "7:671 en verder", ["met instemming", "met toestemming UWV", "in de proeftijd", "op staande voet"]),
            ("Ontbinding", "door de kantonrechter (7:671b)"),
        ]))),

    F(5, "Arbeidsrecht", "1. Einde van rechtswege", fig(
        "De ketenregeling in drie getallen",
        cards([
            ("3 contracten", "Het 4e is voor onbepaalde tijd", "drie contracten voor bepaalde tijd mogen na elkaar"),
            ("3 jaar", "Daarna onbepaalde tijd", "als de keten langer dan drie jaar duurt"),
            ("6 maanden", "Tussenpoos telt mee", "bij een onderbreking van zes maanden of korter loopt de keten door"),
        ]),
        noot="Art. 7:668a BW. Eén contract van langer dan drie jaar mag nog eenmaal met 3 maanden worden verlengd (lid 3)."),
      after="Ketenregeling"),

    F(5, "Arbeidsrecht", "2. Wederzijds goedvinden: art. 7:670b BW", fig(
        "Bedenktijd: 14 dagen, of 3 weken als de werkgever er niet op wijst",
        bars([
            dict(label="Het recht staat in de overeenkomst", segs=[(14, "c1")], val="14 dagen"),
            dict(label="Het recht staat er niet in", segs=[(21, "c1")], val="3 weken"),
        ], maxv=21, vw="5em", label="Bedenktijd in dagen"),
        noot="Dezelfde termijnen gelden voor het herroepen van instemming met een opzegging (art. 7:671 lid 2).")),

    F(5, "Arbeidsrecht", "3. Opzegging", fig(
        "Ontslag op staande voet: drie voorwaarden tegelijk",
        som([
            ("Dringende reden", "objectief en subjectief"),
            ("Onverwijlde opzegging", "wel tijd voor onderzoek"),
            ("Onverwijlde mededeling van de reden", "wees compleet"),
        ], ("Geldig ontslag op staande voet", "art. 7:677 BW"))),
      after="onverwijlde mededeling van de reden"),

    F(5, "Arbeidsrecht", "3. Opzegging", fig(
        "Opzegtermijn: hoe langer in dienst, hoe langer de termijn van de werkgever",
        legend([("c1", "werkgever"), ("c2", "werknemer")]) + bars([
            dict(label="Korter dan 5 jaar in dienst", segs=[(1, "c1")], val="1 maand"),
            dict(label="5 tot 10 jaar", segs=[(2, "c1")], val="2 maanden"),
            dict(label="10 tot 15 jaar", segs=[(3, "c1")], val="3 maanden"),
            dict(label="15 jaar of langer", segs=[(4, "c1")], val="4 maanden"),
            dict(label="De werknemer zegt op", sub="altijd, lid 4", segs=[(1, "c2")], val="1 maand"),
        ], maxv=4, vw="5.6em", label="Opzegtermijn in maanden naar duur van het dienstverband"),
        noot="Art. 7:672 BW. Opzeggen gebeurt tegen het einde van de maand. De proceduretijd bij het UWV gaat eraf, maar er blijft minimaal een maand over."),
      after="Termijn werkgever"),

    F(5, "Arbeidsrecht", "4. Ontbinding door de kantonrechter", fig(
        "Welke ontslaggrond hoort bij welke route?",
        pgrid(["UWV (art. 7:671a)", "Kantonrechter (art. 7:671b)"], [
            ("a-grond: bedrijfseconomische redenen", [("Ja", "toestemming is 4 weken geldig"), ("Alleen als het UWV weigerde", None)]),
            ("b-grond: twee jaar ziekte", [("Ja", "het UWV kijkt ook naar de re-integratie"), ("Alleen als het UWV weigerde", None)]),
            ("c- tot en met i-grond", [None, ("Ja", "bijvoorbeeld disfunctioneren of een verstoorde arbeidsrelatie")]),
        ], hoek="Grond uit art. 7:669 lid 3"),
        noot="Voor bijna alle gronden geldt ook: er is een redelijke grond en herplaatsing binnen een redelijke termijn is niet mogelijk.")),

    F(5, "Arbeidsrecht", "Transitievergoeding en billijke vergoeding", fig(
        "Wanneer is de transitievergoeding verschuldigd?",
        tree("Transitievergoeding", [
            ("Wel", None, ["opzegging door de werkgever", "ontbinding op verzoek van de werkgever", "einde van rechtswege op initiatief van de werkgever",
                           "einde door de werknemer na ernstig verwijtbaar handelen van de werkgever"]),
            ("Niet", None, ["wederzijds goedvinden: dan is het onderdeel van de onderhandeling", "ernstig verwijtbaar handelen van de werknemer (lid 7)"]),
        ], rootsub="1/3 maandsalaris per dienstjaar, art. 7:673 BW"),
        noot="Het maximumbedrag op de slide is verouderd; zoek het bedrag voor 2026 op."),
      after="1/3 maandsalaris"),

    F(5, "Arbeidsrecht", "Transitievergoeding en billijke vergoeding", fig(
        "Rekenvoorbeeld Dirk: van opzegtermijn naar einddatum",
        bars([
            dict(label="Opzegtermijn bij 16 dienstjaren", segs=[(4, "c1")], val="4 maanden"),
            dict(label="Proceduretijd bij het UWV", start=3, segs=[(1, "c2")], val="− 1 maand", neg=True),
            dict(label="Blijft over", sub="minimaal 1 maand", segs=[(3, "c0")], val="3 maanden"),
        ], maxv=4, vw="5.6em", label="Opzegtermijn van vier maanden min een maand proceduretijd is drie maanden"),
        noot="Opgezegd op 15-3-2026 met drie maanden en tegen het einde van de maand: het dienstverband eindigt op 30-6-2026."),
      after="Dirk"),

    # ================================================================ week 5 workshop
    F(5, "Workshop", "Drie fasen in het gesprek", fig(
        "Het slechtnieuwsgesprek in drie fasen",
        flow([
            ("Breng de boodschap direct", "kernboodschap in de eerste zinnen, dan stoppen en ruimte geven"),
            ("Vang de reactie op", "stilte toelaten, parafraseren, gevoel reflecteren als hypothese"),
            ("Bespreek vervolgstappen", "pas als de ander eraan toe is"),
        ]),
        noot="De boodschap staat vast, de manier waarop je het gesprek voert niet."), pos="top"),

    F(5, "Workshop", "De drie oefencasussen", fig(
        "Scheid wat vaststaat van wat nog onzeker is",
        poles([
            ("Wat kun je in de reorganisatiecasus zeggen?", ("Vast staat", "de structuur verandert, meerdere functies vervallen, er komen enkele nieuwe functies, niet iedereen kan worden herplaatst"),
             ("Nog niet vast", "wie voor welke nieuwe positie in aanmerking komt, wie moet uitstromen, de uitkomst per persoon")),
        ]),
        noot="Zeg dus niet dat iemand wordt ontslagen als dat nog niet besloten is. Zeg wel dat de huidige functie vervalt."),
      after="Professionele grens"),

    # ================================================================ week 6 theorie
    F(6, "Theoriecollege", "Wat is ziekteverzuim?", fig(
        "Verzuim typeren: naar oorzaak en naar duur",
        '<div class="lanes"><div class="lane"><h5>Naar oorzaak</h5>'
        + cards([
            (None, "Wit verzuim", "aantoonbaar ziek, fysiek of psychisch"),
            (None, "Grijs verzuim", "onduidelijk ziektebeeld: iemand kan fysiek werken, maar is moe of niet gemotiveerd"),
            (None, "Zwart verzuim", "geen ziekte, toch ziek gemeld"),
        ])
        + '</div><div class="lane"><h5>Naar duur <small>in weken</small></h5>'
        + bars([
            dict(label="Kortdurend", segs=[(1, "c1")], val="maximaal 1 week"),
            dict(label="Middellang", start=1, segs=[(5, "c1")], val="1 tot 6 weken"),
            dict(label="Langdurend", start=6, segs=[(6, "c1")], val="langer dan 6 weken"),
        ], maxv=12, vw="9.5em", label="Verzuim naar duur in weken")
        + "</div></div>",
        noot="De staaf van langdurend verzuim heeft geen vast einde; bij ziekte loopt de loondoorbetaling tot 104 weken."),
      after="Langdurend"),

    F(6, "Theoriecollege", "De FM'er als gezondheidsregisseur", fig(
        "Drie domeinen voor verzuimpreventie",
        pillars("FM-interventiematrix verzuimpreventie", [
            ("Fysiek welzijn", None), ("Mentaal welzijn", None), ("Sociaal welzijn", None),
        ], basis="Direct invloed: werkplek, ergonomie, binnenklimaat, roosters, materiaal. Alleen indirect: leefstijl en privésituatie"),
        noot="Per domein bedacht je in de les vier interventies, een mix van harde en zachte.")),

    F(6, "Theoriecollege", "Wet verbetering poortwachter (Wvp)", fig(
        "Twee jaar verzuim op één lijn",
        legend([("c1", "eerste jaar: 70% loon, minimaal het minimumloon"), ("c2", "tweede jaar: 70% loon")]) + WVP,
        noot="Tussen week 8 en week 91 evalueren werkgever en werknemer elke 6 tot 8 weken. Week 91 is 13 weken voor het einde van de wachttijd."),
      after="Einde wachttijd"),

    F(6, "Theoriecollege", "Wet verbetering poortwachter (Wvp)", fig(
        "Spoor 1 en spoor 2",
        tree("Re-integratie", [
            ("Spoor 1", "bij de eigen werkgever", ["eigen werk", "aangepast werk", "ander werk"]),
            ("Spoor 2", "bij een andere werkgever, als terugkeer bij de eigen werkgever niet lukt"),
        ]),
        noot="Gangbare uitleg; de sporen staan als afbeelding op de slide.")),

    # ================================================================ week 6 workshop
    F(6, "Workshop", "Verzuimquiz: wat mag je vragen?", fig(
        "De medische grens: wat hoort bij wie?",
        poles([
            ("Bij wie hoort het onderwerp?", ("Leiding" + SH + "gevende", "werk, contact, advies van de bedrijfsarts, functionele mogelijkheden, werkaanpassingen, re-integratieafspraken"),
             ("Bedrijfsarts", "diagnose, behandeling, medicatie, medische geschiedenis, details van klachten")),
        ]),
        noot="Vertelt de medewerker toch iets medisch, dan leg je dat niet vast en ga je terug naar het werk en de afspraken.")),

    F(6, "Workshop", "De rode draad van alle zes workshops", fig(
        "De rode draad in zes stappen",
        flow(["Feitelijk openen", "Luisteren", "Perspectief onderzoeken", "Structuur bewaken", "Belangen verbinden", "Afspraken maken"], cols=3),
        noot="Dit is ook wat de beoordelaar in het tentamengesprek wil zien.")),

    # ================================================================ week 7
    F(7, "tentamen in het kort", None, fig(
        "Het mondeling: 30 minuten in drie gelijke delen",
        seg([
            (10, "c1", "Gesprek met een trainingsacteur: 10 min", "één casus: sollicitatie, diversiteit, slechtnieuws, ontwikkel of verzuim"),
            (10, "c2", "HRM-theorie: 10 min", "vier vragen over de theoriecolleges"),
            (10, "c3", "Arbeidsrecht: 10 min", "vier vragen over de hele periode"),
        ])),
      after="trainingsacteur"),
]
