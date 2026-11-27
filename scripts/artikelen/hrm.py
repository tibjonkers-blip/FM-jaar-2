# Wetsartikelen arbeidsrecht (HRM), lessen 1 t/m 6.
# Alleen artikelen die in de samenvattingen (scripts/samenvattingen/hrm/) of de slides van arbeidsrecht les 1-5 en het
# oefenmateriaal staan. De inhoud is een korte weergave in eigen woorden van wat daar staat; niets erbij verzonnen.
# let=... is een waarschuwing: verschil tussen slide, antwoordmodel en wet, of iets dat je zelf moet nalezen.
# WETTEN: (code, volledige naam, korte naam voor de inhoudsopgave).
# Velden: A(wet, nummer, titel, inhoud, weken, let=None). Weken = arbeidsrechtles (les N staat in week N).

TITEL = "Wetsartikelen arbeidsrecht"
LEAD = ("Alle wetsartikelen uit de arbeidsrechtlessen (les 1 t/m 6), per wet op volgorde, met in het kort wat erin staat. "
        "Gebaseerd op de samenvattingen, de slides en het oefenmateriaal met antwoorden. De wettenbundel blijft leidend.")

WETTEN = [
    ("BW7", "Burgerlijk Wetboek Boek 7, titel 10: de arbeidsovereenkomst", "Boek 7 BW"),
    ("BW", "Burgerlijk Wetboek, overige boeken", "Overig BW"),
    ("WAZO", "Wet arbeid en zorg (WAZO): verlof", "WAZO"),
    ("Awgb", "Algemene wet gelijke behandeling (Awgb)", "Awgb"),
    ("Gw", "Grondwet", "Grondwet"),
]

ARTIKELEN = []
def A(wet, nr, titel, inhoud, weken, let=None):
    ARTIKELEN.append(dict(wet=wet, nr=nr, titel=titel, inhoud=inhoud, weken=weken, let=let))

# ---------------------------------------------------------------- Boek 7 BW
A("BW7", "7:400", "Overeenkomst van opdracht",
  "Werkzaamheden verrichten anders dan op grond van een arbeidsovereenkomst, die niet bestaan uit een werk van stoffelijke aard maken "
  "(bijvoorbeeld een adviseur, advocaat of zzp'er). Verschil met 7:610: er is geen gezag.", [1])
A("BW7", "7:610", "Definitie arbeidsovereenkomst",
  "De werknemer verbindt zich in dienst van (gezag) de werkgever, tegen loon, gedurende zekere tijd arbeid te verrichten. "
  "Vier elementen: arbeid (persoonlijk), loon, gezag en zekere tijd. Dwingend recht: het etiket op het contract maakt niet uit "
  "(Groen/Schoevers, casus Davy).", [1, 2])
A("BW7", "7:610a", "Rechtsvermoeden: bestaan arbeidsovereenkomst",
  "Wie drie opeenvolgende maanden wekelijks of minstens 20 uur per maand arbeid verricht tegen beloning, wordt vermoed een "
  "arbeidsovereenkomst te hebben. De werkgever moet het tegendeel bewijzen.", [2])
A("BW7", "7:610b", "Rechtsvermoeden: omvang van de arbeid",
  "Heeft de arbeidsovereenkomst drie maanden geduurd, dan geldt de gemiddelde omvang van die drie maanden als de overeengekomen "
  "omvang, tenzij de werkgever aantoont dat de periode niet representatief is.", [2])
A("BW7", "7:613", "Wijzigingsbeding",
  "Schriftelijk beding waarmee de werkgever arbeidsvoorwaarden eenzijdig mag wijzigen, vooral bij collectieve wijzigingen. "
  "Alleen bij een zodanig zwaarwichtig belang van de werkgever dat het belang van de werknemer naar redelijkheid moet wijken. "
  "Zonder beding: via goed werkgever- en werknemerschap (dubbele redelijkheidstoets).", [3])
A("BW7", "7:617", "Vormen van loon",
  "Welke vormen van loon zijn toegestaan. Op de slide genoemd bij het element loon, met de vraag of het dwingend recht is.", [1])
A("BW7", "7:623", "Tijdstip van loonbetaling", "Wanneer het loon betaald moet worden. Alleen genoemd op de slide.", [1])
A("BW7", "7:625", "Te late loonbetaling", "Wat er geldt als het loon niet op tijd wordt betaald. Alleen genoemd op de slide.", [1])
A("BW7", "7:626", "Loonstrook", "De werkgever geeft een loonstrook. Alleen genoemd op de slide.", [1])
A("BW7", "7:628", "Geen arbeid, wel loon",
  "Uitgangspunt: de werkgever betaalt het loon door, tenzij het niet werken in redelijkheid voor rekening van de werknemer komt "
  "(bijvoorbeeld werkweigering). Voor rekening van de werkgever: schorsing of non-actiefstelling, een nietig ontslag als de "
  "werknemer bereid is te werken, bedrijfsrisico's en (soms) stakingen. Lid 5 is semidwingend, lid 7 driekwartdwingend "
  "(oefenmateriaal week 1).", [1, 4])
A("BW7", "7:628a", "Oproepkrachten",
  "Lid 1: minimumaanspraak van drie uur loon per oproep (onder voorwaarden). Lid 2: minstens vier dagen van tevoren schriftelijk of "
  "elektronisch oproepen, dan moet de werknemer komen. Lid 3: later dan vier dagen vooraf intrekken betekent toch loon. "
  "Lid 4: bij cao korter. Lid 5: na 12 maanden binnen een maand een vaste omvang aanbieden (gemiddelde van die 12 maanden), "
  "steeds opnieuw na elke 12 maanden. Lid 8: geen aanbod, dan loon over de gemiddelde omvang. Lid 9: definitie van de oproepovereenkomst.",
  [2], let="De slide noemt bij de referentiedagen \"7:628 lid 2\"; bedoeld is waarschijnlijk 7:628a lid 2.")
A("BW7", "7:628b", "Referentiedagen en -uren",
  "Vooraf schriftelijk vastleggen op welke dagen en uren de werkgever kan oproepen. Een oproep daarbuiten mag de werknemer altijd weigeren.", [2])
A("BW7", "7:629", "Loondoorbetaling bij ziekte",
  "Lid 1: 104 weken 70% van het loon, het eerste jaar minimaal het minimumloon; maximum 70% van het maximum dagloon. "
  "Lid 2: kortere periode voor bepaalde werknemers, zoals 6 weken na de AOW-leeftijd (sub b). Lid 3: uitsluitingsgronden "
  "(ziekte opzettelijk veroorzaakt, genezing belemmeren, passende arbeid weigeren): loonstaking. Lid 6: controlevoorschriften niet "
  "naleven: loonopschorting. Lid 7: eerst waarschuwen. Lid 9: maximaal twee wachtdagen, alleen als het in de arbeidsovereenkomst staat. "
  "Lid 10: wanneer ziekteperiodes worden samengeteld.", [4],
  let="De slide rekent met het maximum dagloon van 2021 (€225,57); zoek het actuele bedrag op.")
A("BW7", "7:634", "Omvang vakantie",
  "Lid 1: wettelijk minimum is vier keer de overeengekomen arbeidsduur per week (5 dagen per week = 20 dagen). Opbouw hangt aan het "
  "recht op loon, dus ook tijdens ziekte. Meer via contract of cao heet bovenwettelijk. Lid 1 is dwingend, lid 2 driekwartdwingend.", [1, 4, 5])
A("BW7", "7:635", "Geen loon, wel vakantieopbouw", "Gevallen waarin je geen loon krijgt maar wel vakantie opbouwt, bijvoorbeeld bij bepaalde soorten onbetaald verlof.", [4])
A("BW7", "7:637", "Ziektedagen als vakantie aanmerken",
  "Lid 1: alleen met instemming van de werknemer. Lid 2: of vooraf schriftelijk in de arbeidsovereenkomst afgesproken. "
  "In beide gevallen alleen voor bovenwettelijke dagen (casus Ad).", [4])
A("BW7", "7:638", "Vaststellen van vakantie",
  "Lid 1: de werkgever moet de werknemer in staat stellen vakantie op te nemen. Lid 2: periode volgens cao of contract, anders volgens de "
  "wensen van de werknemer, tenzij gewichtige redenen; reageert de werkgever niet binnen twee weken, dan staat de vakantie vast. "
  "Lid 5: na vaststelling alleen wijzigen bij gewichtige redenen, en de werkgever vergoedt de schade. Lid 8: ziek tijdens vakantie telt "
  "niet als vakantie, tenzij de werknemer instemt; vooraf afspreken kan alleen voor bovenwettelijke dagen (casus Dennis). "
  "Lid 8 bevat aanvullend én semidwingend recht.", [1, 4, 5])
A("BW7", "7:639", "Loon tijdens vakantie", "Tijdens vakantie heeft de werknemer recht op loon.", [4])
A("BW7", "7:640", "Geen afkoop", "Wettelijke vakantiedagen mag je tijdens het dienstverband niet afkopen; bovenwettelijke wel.", [4])
A("BW7", "7:640a", "Verval wettelijke vakantiedagen",
  "Wettelijke dagen vervallen een half jaar na het jaar waarin ze zijn opgebouwd (dagen uit 2026 vervallen op 1 juli 2027).", [4])
A("BW7", "7:641", "Vakantiedagen bij einde dienstverband",
  "Lid 1: alle resterende dagen uitbetalen. Lid 2: de werkgever geeft een verklaring met het saldo. Lid 3: de nieuwe werkgever hoeft "
  "voor die dagen geen loon te betalen.", [4])
A("BW7", "7:642", "Verjaring bovenwettelijke dagen", "Bovenwettelijke vakantiedagen verjaren vijf jaar na het jaar waarin ze zijn opgebouwd.", [4])
A("BW7", "7:645", "Vakantieregeling dwingend", "De vakantieregeling (afdeling 3) is dwingend recht, tenzij het artikel zelf iets anders zegt.", [1, 4])
A("BW7", "7:646", "Gelijke behandeling mannen en vrouwen",
  "Verbod op onderscheid tussen mannen en vrouwen. Lid 5: direct en indirect onderscheid. Lid 9: niet benadelen. Lid 10: objectieve "
  "rechtvaardiging van indirect onderscheid. Lid 12: bewijslast. Lid 14: opzegverbod. Dwingend recht (oefenmateriaal week 1).", [1, 2, 5])
A("BW7", "7:648", "Gelijke behandeling deeltijd en voltijd",
  "Geen onderscheid tussen deeltijders (ook oproepkrachten) en voltijders. Lid 4: opzegverbod.", [2, 5])
A("BW7", "7:649", "Gelijke behandeling bepaalde en onbepaalde tijd",
  "Geen onderscheid tussen werknemers met een tijdelijk en een vast contract. Lid 4: opzegverbod.", [2, 5])
A("BW7", "7:650", "Boetebeding",
  "Lid 1 en 2: schriftelijk, en duidelijk waarvoor en hoe hoog. Lid 3: de boete mag de werkgever niet bevoordelen (bestemming). "
  "Lid 4: valuta. Lid 5: maximaal een halve dag loon per week. Lid 6: verdient de werknemer meer dan het minimumloon, dan mag van "
  "lid 3 t/m 5 worden afgeweken (casus Dion).", [3, 4])
A("BW7", "7:651", "Boete of schadevergoeding", "De werkgever kan voor hetzelfde feit niet zowel een boete als schadevergoeding eisen.", [3])
A("BW7", "7:652", "Proeftijdbeding",
  "Lid 1: voor beide partijen gelijk. Lid 2: schriftelijk. Lid 3: onbepaalde tijd hoogstens 2 maanden. Lid 4: bepaalde tijd: geen proeftijd "
  "bij 6 maanden of korter, hoogstens 1 maand bij korter dan 2 jaar, hoogstens 2 maanden bij 2 jaar of langer. Lid 5: hoogstens 1 maand "
  "als het einde niet aan een kalenderdatum hangt. Lid 6: geen nieuwe proeftijd bij een opvolgend contract, tenzij de nieuwe functie "
  "duidelijk andere vaardigheden of verantwoordelijkheden vraagt (sub b, casus Laura). Lid 7: afwijken bij cao. Lid 8: wat nietig is.", [3])
A("BW7", "7:653", "Concurrentiebeding",
  "Raakt aan de vrije arbeidskeuze (art. 19 lid 3 Gw), daarom strenge eisen. Lid 1: alleen geldig als het schriftelijk is afgesproken met een meerderjarige werknemer met een contract voor onbepaalde tijd. "
  "Lid 2: bij bepaalde tijd alleen met een schriftelijke motivering van zwaarwegende bedrijfs- of dienstbelangen. Lid 3: de rechter kan het "
  "geheel of gedeeltelijk vernietigen. Lid 4: geen rechten als het contract eindigt door ernstig verwijtbaar handelen van de werkgever. "
  "Lid 5: de rechter kan een vergoeding toekennen als het beding de werknemer in belangrijke mate belemmert.", [3])
A("BW7", "7:653a", "Verbod op nevenwerkzaamheden",
  "Sinds augustus 2022 in de wet. Een verbod op werk voor anderen (ook als zelfstandige) mag alleen met een objectieve rechtvaardiging "
  "(passend, geschikt en noodzakelijk), bijvoorbeeld gezondheid, veiligheid of de Arbeidstijdenwet. Toestemming mag alleen met zo'n "
  "rechtvaardiging worden geweigerd. Lid 2: benadelingsverbod.", [3])
A("BW7", "7:662", "Overgang van onderneming: definitie",
  "Overgang van een economische eenheid die haar identiteit behoudt, door een overeenkomst, fusie, splitsing en dergelijke. "
  "Economische eenheid: een geheel van georganiseerde middelen om een activiteit uit te voeren. Beoordelen met de Spijkers-factoren. "
  "De regeling staat in art. 7:662 t/m 7:666a.", [3])
A("BW7", "7:663", "Overgang van onderneming: gevolgen",
  "De rechten en plichten uit de arbeidsovereenkomsten gaan van rechtswege over naar de nieuwe werkgever. De oude werkgever blijft nog "
  "een jaar naast de nieuwe aansprakelijk voor de naleving.", [3])
A("BW7", "7:667", "Einde van rechtswege",
  "Een contract voor bepaalde tijd eindigt zonder opzegging, tenzij anders afgesproken. Lid 3: tussentijds opzeggen kan alleen als dat "
  "schriftelijk is afgesproken (opzegbeding).", [5])
A("BW7", "7:668", "Aanzegplicht",
  "Werkt de werknemer na de einddatum gewoon door, dan is het contract verlengd onder dezelfde voorwaarden en voor dezelfde duur. "
  "Lid 1: de werkgever laat uiterlijk een maand voor het einde schriftelijk weten of het contract wordt voortgezet en onder welke voorwaarden. "
  "Lid 2: niet bij een einde zonder kalenderdatum of een contract korter dan 6 maanden. Lid 3: niet of te laat aangezegd: vergoeding.", [5])
A("BW7", "7:668a", "Ketenregeling",
  "Een contract voor onbepaalde tijd ontstaat bij het vierde tijdelijke contract of als de keten langer dan drie jaar duurt. Tussenpozen "
  "van zes maanden of korter tellen mee. Lid 2: draaideurconstructies. Lid 3: één contract van langer dan drie jaar mag nog eenmaal met "
  "drie maanden worden verlengd. Verdere leden: uitzonderingen.", [5])
A("BW7", "7:669", "Redelijke grond voor ontslag",
  "Lid 1: opzeggen kan alleen met een redelijke grond en als herplaatsing binnen een redelijke termijn niet mogelijk is. Lid 3 noemt de "
  "gronden: sub a bedrijfseconomische redenen (met anciënniteit en afspiegeling), sub b twee jaar ziekte, sub c t/m i de overige gronden, "
  "waaronder disfunctioneren (sub d). Voor a en b ga je naar het UWV, voor c t/m i naar de kantonrechter.", [5],
  let="Het antwoordmodel bij Peter noemt de gronden c t/m h; sinds 2020 is er ook de i-grond (combinatiegrond), zoals de slide zegt.")
A("BW7", "7:670", "Opzegverboden",
  "De werkgever mag niet opzeggen tijdens of wegens bijvoorbeeld ziekte, zwangerschap, dienstplicht, lidmaatschap van de OR of een "
  "vakbond, of weigeren op zondag te werken. Lid 8: opzegverbod wegens overgang van onderneming.", [3, 5])
A("BW7", "7:670a", "Uitzonderingen op de opzegverboden", "Wanneer een opzegverbod niet geldt. Alleen genoemd op de slide.", [5])
A("BW7", "7:670b", "Beëindigingsovereenkomst (wederzijds goedvinden)",
  "Schriftelijk. Er is geen wettelijke transitievergoeding; partijen onderhandelen over een vergoeding. Lid 2: de werknemer mag binnen 14 dagen zonder reden schriftelijk ontbinden (maar één keer per 6 maanden). Lid 3: staat dat "
  "recht niet in de overeenkomst, dan wordt het 3 weken.", [5])
A("BW7", "7:671", "Opzegging met instemming van de werknemer",
  "Lid 1: zonder instemming kan de werkgever alleen opzeggen in de gevallen van sub a t/m h (bijvoorbeeld met UWV-toestemming, in de proeftijd "
  "of op staande voet). Met instemming gelden de opzegtermijn en de transitievergoeding. Lid 2: de werknemer kan binnen 14 dagen herroepen, "
  "3 weken als de werkgever daar niet schriftelijk op wijst.", [5])
A("BW7", "7:671a", "Opzegging met toestemming van het UWV",
  "Alleen voor de a-grond (bedrijfseconomisch) en de b-grond (twee jaar ziekte) van art. 7:669 lid 3. Lid 6: de toestemming is 4 weken geldig; "
  "binnen die tijd opzeggen met inachtneming van de opzegtermijn.", [5])
A("BW7", "7:671b", "Ontbinding door de kantonrechter (verzoek werkgever)",
  "Voor de gronden c t/m i van art. 7:669 lid 3, voor a en b als het UWV de toestemming weigerde, en bij een tijdelijk contract zonder "
  "opzegbeding. De rechter houdt rekening met de opzegtermijn minus de proceduretijd.", [5])
A("BW7", "7:671c", "Ontbinding op verzoek van de werknemer", "Komt zelden voor; meestal om een extra billijke vergoeding te krijgen.", [5])
A("BW7", "7:672", "Opzegtermijnen",
  "Lid 1: opzeggen tegen het einde van de maand. Lid 2: werkgever 1 maand (korter dan 5 jaar in dienst), 2 maanden (5 tot 10), 3 maanden (10 tot 15), "
  "4 maanden (15 jaar of langer, sub d). Lid 3: 1 maand als de werknemer de AOW-leeftijd heeft. Lid 4: werknemer 1 maand. Lid 6: aftrek van de "
  "UWV-proceduretijd, met minimaal een maand over. Lid 7: bij cao korter. Lid 8: termijn werknemer schriftelijk verlengen tot hoogstens 6 maanden, "
  "die van de werkgever is dan het dubbele. Lid 9: bij cao gelijkstellen.", [5],
  let="Het antwoordmodel bij Dirk noemt lid 5 voor de aftrek van de proceduretijd; volgens de wettekst is het lid 6, zoals op de slide.")
A("BW7", "7:673", "Transitievergoeding",
  "Hoogte: 1/3 maandsalaris per dienstjaar, naar rato. Niet bij wederzijds goedvinden. Bij ontslag na twee jaar ziekte krijgt de werkgever "
  "compensatie van het UWV. Lid 1 sub a: bij opzegging door de werkgever, ontbinding op verzoek van de werkgever en een einde van rechtswege op initiatief van de werkgever. "
  "Sub b: bij een einde op initiatief van de werknemer door ernstig verwijtbaar handelen van de werkgever. "
  "Lid 7: niet verschuldigd bij ernstig verwijtbaar handelen van de werknemer.", [5],
  let="Het maximum op de slide (€84.000) is verouderd; in 2026 is het €102.000 of een jaarsalaris als dat hoger is.")
A("BW7", "7:674", "Overlijden van de werknemer",
  "Lid 1: de arbeidsovereenkomst eindigt door het overlijden. Lid 2: de werkgever betaalt vanaf de dag van overlijden tot een maand later het "
  "loon aan de nabestaanden. Lid 3: wie de nabestaanden zijn.", [4, 5])
A("BW7", "7:676", "Opzegging tijdens de proeftijd", "Geen opzegtermijn. Op verzoek geeft de opzeggende partij een schriftelijke toelichting.", [3, 5])
A("BW7", "7:677", "Ontslag op staande voet",
  "Drie voorwaarden: een dringende reden (objectief en subjectief), onverwijlde opzegging (wel tijd voor onderzoek) en onverwijlde, volledige "
  "mededeling van de reden.", [5])
A("BW7", "7:681", "Actie bij onjuiste opzegging",
  "Zegt de werkgever niet goed op (geen opzegtermijn, geen UWV-toestemming, geen dringende reden, in strijd met een opzegverbod), dan kan de "
  "werknemer hier in actie komen. Voor de werkgever kan dat veel schade opleveren.", [5])
A("BW7", "7:682", "Toestemming UWV aanvechten", "De werknemer kan de opzegging na UWV-toestemming aanvechten bij de kantonrechter.", [5])
A("BW7", "7:690", "Uitzendovereenkomst", "Ook een uitzendovereenkomst is een arbeidsovereenkomst.", [2])
A("BW7", "7:750", "Aanneming van werk",
  "Buiten dienstbetrekking een werk van stoffelijke aard tot stand brengen en opleveren tegen een prijs in geld (bijvoorbeeld een aannemer "
  "of loodgieter). Geen gezag, dus geen arbeidsovereenkomst.", [1])

# ---------------------------------------------------------------- overig BW
A("BW", "6:217", "Aanbod en aanvaarding", "Een overeenkomst, ook de arbeidsovereenkomst, komt tot stand door aanbod en aanvaarding.", [2])

# ---------------------------------------------------------------- WAZO
A("WAZO", "3:1", "Zwangerschaps- en bevallingsverlof",
  "Zwangerschapsverlof: vanaf 6 weken voor de vermoedelijke bevallingsdatum, uiterlijk vanaf 4 weken; bij een meerling 10 en uiterlijk 8 weken "
  "(lid 2, casus Marianne). Bevallingsverlof: 10 weken, plus de dagen die het zwangerschapsverlof korter was dan 6 (meerling 10) weken.", [4],
  let="In het antwoordmodel bij Marianne staat dat het \"zwangerschapsverlof\" ingaat op de dag na de bevalling; dat is het bevallingsverlof.")
A("WAZO", "3:2", "Adoptieverlof", "Verlof bij adoptie. Geen recht op loon, wel op een uitkering.", [4])
A("WAZO", "3:8", "Uitkering zwangerschaps- en bevallingsverlof", "De werknemer heeft recht op een uitkering; in de praktijk betaalt het UWV.", [4])
A("WAZO", "4:1", "Calamiteiten- en ander kort verzuimverlof",
  "Verlof met behoud van loon in de gevallen van lid 1 en lid 2, bijvoorbeeld voor de partner op de dag van de bevalling (lid 2 sub a, casus Robin).", [4])
A("WAZO", "4:2", "Geboorteverlof",
  "Voor de partner: één keer de arbeidsduur per week, op te nemen binnen 4 weken na de geboorte (lid 1). Met behoud van loon.", [4])
A("WAZO", "4:2a", "Aanvullend geboorteverlof",
  "Volgens het oefenmateriaal 5 keer de arbeidsduur per week, op te nemen binnen 6 maanden na de geboorte (lid 1 en 2). Zonder loon, wel met "
  "een uitkering (art. 4:2a jo. 4:2b).", [4])
A("WAZO", "4:2b", "Uitkering aanvullend geboorteverlof", "Samen met art. 4:2a de grondslag voor de uitkering tijdens het aanvullend geboorteverlof (antwoordmodel Robin).", [4])
A("WAZO", "4:6", "Afwijken van het geboorteverlof", "Afwijkingsmogelijkheden bij het geboorteverlof. Alleen genoemd op de slide.", [4])
A("WAZO", "4:7", "Afwijken van het geboorteverlof",
  "Afwijkingsmogelijkheden bij het geboorteverlof. Volgens het oefenmateriaal driekwartdwingend, en 5/8e dwingend als er geen cao is.", [1, 4])
A("WAZO", "5:1", "Kortdurend zorgverlof",
  "Voor noodzakelijke verzorging van een zieke (bijvoorbeeld partner, kind of bloedverwant in de eerste of tweede graad, lid 2). Per 12 maanden "
  "maximaal twee keer de arbeidsduur per week. De werkgever betaalt 70%, minimaal het minimumloon, maximaal 70% van het maximum dagloon.", [4])
A("WAZO", "5:9", "Langdurend zorgverlof", "Zelfde personen, langdurige zorg. Per 12 maanden maximaal 6 keer de arbeidsduur per week. Geen recht op loon.", [4])
A("WAZO", "5:16", "Afwijken bij zorgverlof",
  "In les 1 gebruikt als oefening: dit artikel bevat driekwart- én 5/8e dwingend recht. De inhoud zelf staat niet op de slide.", [1],
  let="Wat er precies in staat, is niet in de les behandeld. Lees het na in je bundel.")
A("WAZO", "6:1", "Ouderschapsverlof",
  "Recht op ouderschapsverlof voor elk kind. Onbetaald verlof (lid 1).", [4])
A("WAZO", "6:2", "Omvang ouderschapsverlof", "26 keer de arbeidsduur per week, per kind.", [4])
A("WAZO", "6:3", "Uitkering ouderschapsverlof",
  "Sinds augustus 2022 (met art. 6:3a): voor 9 keer de arbeidsduur per week een UWV-uitkering via de werkgever, als je het opneemt voordat het "
  "kind 1 jaar is. De rest blijft zonder loon of uitkering.", [4])
A("WAZO", "6:3a", "Uitkering ouderschapsverlof", "Hoort bij art. 6:3: de regeling van de gedeeltelijke uitkering sinds augustus 2022.", [4])
A("WAZO", "6:4", "Uiterste moment ouderschapsverlof", "Opnemen uiterlijk voordat het kind 8 jaar wordt.", [4])
A("WAZO", "6:5", "Melden ouderschapsverlof", "Het verlof ruim van tevoren bij de werkgever melden.", [4])

# ---------------------------------------------------------------- Awgb
A("Awgb", "1", "Direct en indirect onderscheid",
  "Onderscheid wegens zwangerschap is direct onderscheid op grond van geslacht (casus Dora). Lid 1 sub b: direct onderscheid, iemand wordt rechtstreeks anders behandeld op grond van bijvoorbeeld godsdienst, ras of geslacht. "
  "Lid 1 sub c: indirect onderscheid, een neutrale regel treft in feite vooral een bepaalde groep.", [2, 3])
A("Awgb", "2", "Uitzonderingen en objectieve rechtvaardiging",
  "Voor direct onderscheid op grond van godsdienst is geen rechtvaardiging (alleen de hoofddoek verbieden mag niet). "
  "Lid 1: indirect onderscheid mag bij een objectieve rechtvaardiging: een legitiem doel en een passend en noodzakelijk middel (taxibedrijf "
  "dat alle religieuze uitingen verbiedt). Lid 2 sub a: geslacht is bepalend (actrice voor een vrouwenrol). Lid 2 sub b: bescherming van de "
  "vrouw bij zwangerschap en moederschap (middagdutje voor zwangeren).", [2])
A("Awgb", "3", "Kerkgenootschappen en geestelijk ambt", "De wet geldt niet voor rechtsverhoudingen binnen kerkgenootschappen en het geestelijk ambt.", [2])
A("Awgb", "5", "Arbeid: instellingen op grondslag",
  "Lid 2: instellingen op godsdienstige, levensbeschouwelijke of politieke grondslag en het bijzonder onderwijs mogen eisen stellen als dat "
  "een wezenlijk, legitiem en gerechtvaardigd beroepsvereiste is gezien de grondslag.", [2])
A("Awgb", "8", "Opzegging na beroep op de wet",
  "Een opzegging in strijd met de wet, of als reactie op een beroep op de wet, is vernietigbaar.", [2])
A("Awgb", "8a", "Benadelingsverbod",
  "Het is verboden iemand te benadelen omdat hij zich op de Awgb heeft beroepen of een ander daarbij heeft bijgestaan.", [2])
A("Awgb", "10", "Bewijslast",
  "Voert iemand feiten aan waaruit onderscheid kan worden vermoed, dan moet de wederpartij bewijzen dat zij de wet niet heeft overtreden.", [2])

# ---------------------------------------------------------------- Grondwet
A("Gw", "1", "Gelijke behandeling", "Gelijke gevallen worden gelijk behandeld; discriminatie is verboden. Genoemd als kader bij werving en selectie.", [2])
A("Gw", "19 lid 3", "Vrije arbeidskeuze", "Het recht op vrije keuze van arbeid. Daarom stelt de wet strenge eisen aan het concurrentiebeding.", [3])
