"""Figuren en grafieken bij de samenvattingen van Praktijkproject Business Management.

Elke figuur herhaalt wat in de samenvatting van die les staat. Getallen komen uit de rekenvoorbeelden en praktijkvoorbeelden van de samenvatting.
De Impact/Effort-matrix van week 1 staat al in de samenvatting zelf en wordt hier niet herhaald.
"""
import math

from lib import *

SH = "­"  # zacht afbreekteken voor lange woorden in smalle kolommen

# ---- eigen svg: eerst breed, dan smal
DIAMANT = svg(
    '<path class="f1" opacity=".22" d="M12 82 150 28V136Z"/><path class="f2" opacity=".22" d="M288 82 150 28V136Z"/>'
    '<path class="dash" d="M150 22V142"/>'
    '<text x="150" y="13" text-anchor="middle">longlist van minimaal 10 ideeën</text>'
    '<text x="98" y="79" text-anchor="middle" class="bold">Divergeren</text><text x="98" y="94" text-anchor="middle" class="mut">week 1</text>'
    '<text x="202" y="79" text-anchor="middle" class="bold">Convergeren</text><text x="202" y="94" text-anchor="middle" class="mut">week 2</text>'
    '<text x="12" y="158">knelpunt</text><text x="288" y="158" text-anchor="end">één voorkeursoplossing</text>',
    w=300, h=164, label="Een ruit: van één knelpunt waaiert het uit naar een longlist van minimaal tien ideeën (divergeren, week 1) "
    "en daarna loopt het weer toe naar één voorkeursoplossing (convergeren, week 2).")

# ---- eigen svg: de KKT-driehoek
KKT = svg(
    '<path class="ln l1" d="M130 30 44 142H216Z"/>'
    '<circle class="f1 ring" cx="130" cy="30" r="5"/><circle class="f1 ring" cx="44" cy="142" r="5"/><circle class="f1 ring" cx="216" cy="142" r="5"/>'
    '<text x="130" y="17" text-anchor="middle" class="bold">Kwaliteit</text>'
    '<text x="44" y="162" text-anchor="middle" class="bold">Kosten</text><text x="216" y="162" text-anchor="middle" class="bold">Tijd</text>'
    '<text x="130" y="104" text-anchor="middle" class="mut">zelden alle drie</text><text x="130" y="118" text-anchor="middle" class="mut">tegelijk beter</text>',
    w=260, h=170, label="Driehoek met op de hoeken kwaliteit, kosten en tijd. Je kunt ze zelden alle drie tegelijk verbeteren.")


# ---- eigen svg: de zeester van de retrospective
def _zeester():
    cx, cy, ro, ri = 150, 104, 56, 23
    pts = []
    for k in range(5):
        a, b = math.radians(-90 + 72 * k), math.radians(-54 + 72 * k)
        pts += [f"{cx + ro * math.cos(a):.1f} {cy + ro * math.sin(a):.1f}", f"{cx + ri * math.cos(b):.1f} {cy + ri * math.sin(b):.1f}"]
    out = [f'<path class="f1" opacity=".24" d="M{"L".join(pts)}Z"/><path class="ln l1" d="M{"L".join(pts)}Z"/>']
    labels = ["blijven doen", "meer van", "minder van", "stoppen", "starten"]
    for k, t in enumerate(labels):
        a = math.radians(-90 + 72 * k)
        x, y = cx + (ro + 12) * math.cos(a), cy + (ro + 12) * math.sin(a)
        anchor = "middle" if k == 0 else ("start" if k in (1, 2) else "end")
        dy = -2 if k == 0 else (4 if k in (1, 4) else 10)
        out.append(f'<text x="{x:.1f}" y="{y + dy:.1f}" text-anchor="{anchor}" class="bold">{t}</text>')
    return svg("".join(out), w=300, h=190, label="Zeester met vijf armen: blijven doen, meer van, minder van, stoppen en starten.")


ZEESTER = _zeester()

FIGUREN = [
    # ================================================================ overzicht
    F(0, "Overzicht", None, fig(
        "De adviespresentatie: 45 minuten en een vaste opbouw",
        '<div class="lanes"><div class="lane"><h5>Tijd</h5>'
        + seg([(30, "c1", "Presenteren: 30 minuten", "lever de presentatie vooraf in via Handin"), (15, "c2", "Vragen: 15 minuten", None)])
        + '</div><div class="lane"><h5>Opbouw</h5>'
        + flow([("Probleem", "en de gevolgen"), ("Oorzaak", None), ("Advies", "wat, hoe tot stand gekomen, implementatie, monitoring en meervoudige toegevoegde waarde")], numbered=False)
        + "</div></div>",
        noot="De presentatie bepaalt 100% van je cijfer."),
      after="Adviespresentatie (100% van het cijfer)"),

    F(0, "Overzicht", None, fig(
        "Vijf criteria die elk even zwaar wegen",
        cards([
            ("20%", "Theorie en modellen", "in de analyse"),
            ("20%", "Concreet advies", "samenhangend, met prioritering en fasering"),
            ("20%", "Presenteren", "overtuigend en afgestemd op de stakeholders"),
            ("20%", "Stake" + SH + "holders", "belangen, weerstand en draagvlak"),
            ("20%", "Toege" + SH + "voegde waarde", "financieel én niet-financieel"),
        ], cols=5)),
      after="Criterium (elk 20%)"),

    F(0, "Overzicht", None, fig(
        "Het portfolio: twee helften",
        seg([(50, "c1", "Reflectie met feedback: 50%", "meerdere feedbackbronnen voor boven niveau"), (50, "c2", "Actieve deelname: 50%", None)]),
        noot="Het portfolio moet voldoende zijn (V/NV) en telt niet mee in het cijfer."),
      after="De beoordeling weegt 50%"),

    # ================================================================ week 1
    F(1, "terugblik", "DMAGIC: waar sta je?", fig(
        "DMAGIC: zes fasen over twee periodes",
        phases([
            ("Periode 1: begrijpen", [("Define", "opdracht afbakenen, KSF's en KPI's"), ("Measure", "huidige situatie meten"), ("Analyze", "oorzaken vinden")], "t2"),
            ("Periode 2: verbeteren", [("Generate", "week 1 tot 3: verbeterrichtingen bedenken en kiezen"), ("Improve", "week 3 en 4: veranderaanpak, implementatie en risico's"), ("Control", "week 5 en 6: borging en eigenaarschap")], "t1"),
        ]),
        noot="Generate is bewust toegevoegd aan het klassieke DMAIC-model: wie te snel naar de eerste oplossing springt, mist vaak de beste."),
      after="Define"),

    F(1, "terugblik", "Eerst breed, dan smal", fig(
        "Eerst breed, dan smal",
        DIAMANT,
        noot="De valkuil in week 1: te vroeg oordelen snoeit de beste ideeën weg.")),

    F(1, "terugblik", "Omdenken vanuit klantwaarde", fig(
        "Klantwaarde is meer dan snelheid",
        chips(["snelheid", "betrouwbaarheid", "responsiviteit", "deskundigheid", "beleving"]),
        noot="Koppeling met SERVQUAL uit de notities. Verbeteren kan dus ook betekenen: betrouwbaarder, veiliger, gastvrijer of duurzamer.")),

    F(1, "terugblik", "Verbeteren met richting", fig(
        "Toets elke verbeterrichting twee keer",
        '<div class="lanes"><div class="lane"><h5>Past het bij de richting van de organisatie?</h5>'
        + cards([
            ("waarom", "Missie", "waarom bestaat de organisatie?"),
            ("waarheen", "Visie", "waar wil ze naartoe?"),
            ("hoe", "Strategie", "hoe komt ze daar?"),
        ])
        + '</div><div class="lane"><h5>Welke van de 11 facilitaire toegevoegde waarden levert het op?</h5>'
        + chips(["productiviteit", "kosten verlagen", "risico's beheren", "waardestijging", "flexibiliteit", "cultuur", "imago", "innovatie",
                 "tevredenheid", "duurzaamheid", "healing environment"])
        + "</div></div>",
        noot="Let op de waarschuwing van de docent: een eenzijdige focus op kosten verlagen kan elders schade aanrichten.")),

    F(1, "terugblik", "Inspiratie uit Lean: twee pijlers", fig(
        "De twee pijlers van het Toyota Production System",
        pillars("Toyota Production System", [
            ("Just in Time", "snelheid, laat het werk stromen: flow, pull en kanban, heijunka, de bottleneck eerst"),
            ("Jidoka", "kwaliteit, bouw het goed in bij de bron: stop de lijn, poka-yoke, standaardisatie, 5S"),
        ]),
        noot="Het gaat niet om templates invullen, maar om de gedachte erachter als inspiratie."),
      after="Just in Time"),

    F(1, "terugblik", "Uitgewerkt voorbeeld: de facilitaire servicedesk", fig(
        "De servicedesk: doorlooptijd tegenover de verwachting",
        legend([("c1", "doorlooptijd nu"), ("ref", "verwachting van gebruikers: reactie binnen 2 dagen")]) + bars([
            dict(label="Doorlooptijd van een melding", segs=[(6.5, "c1")], val="6,5 dag", ref=2),
        ], maxv=6.5, vw="4.6em", label="Doorlooptijd van 6,5 dag tegenover een verwachting van 2 dagen"),
        noot="De meldingen blijven liggen bij één coördinator: dat is de bottleneck."),
      after="Probleem"),

    # ================================================================ week 2
    F(2, "gekozen ontwerp", "Future state: ontwerp vanuit het ideaal", fig(
        "De vaste volgorde in Lean",
        flow([
            ("Current state", "de huidige situatie beschrijven, gedaan in periode 1"),
            ("Verspilling analyseren", None),
            ("Future state", "het ideale proces ontwerpen: alleen stappen die waarde toevoegen"),
            ("Terug" + SH + "redeneren", "naar wat haalbaar is"),
        ])),
      after="Lean kent een vaste volgorde"),

    F(2, "gekozen ontwerp", "Future state: ontwerp vanuit het ideaal", fig(
        "De storingsmelding: waar zit de tijd?",
        legend([("c2", "het herstel zelf: een uur"), ("c0", "wachten en overdragen"), ("c1", "future state")]) + bars([
            dict(label="Nu", segs=[(0.125, "c2"), (4.875, "c0")], val="5 dagen"),
            dict(label="Future state", segs=[(1, "c1")], val="minder dan 1 dag"),
        ], maxv=5, vw="8em", label="Doorlooptijd van een storingsmelding: nu vijf dagen, in de future state minder dan een dag"),
        noot="De winst zit in het wegnemen van wachten en overdragen, niet in harder werken. Het uur herstel is getekend op werkdagen van acht uur; dat is mijn aanname.")),

    F(2, "gekozen ontwerp", "Wat voegt waarde toe? VA, BNVA en NVA", fig(
        "Drie soorten processtappen, drie ontwerpregels",
        cards([
            ("behouden", "VA", "value added: de klant wil ervoor betalen"),
            ("minimaliseren", "BNVA", "business non-value added: geen klantwaarde, wel noodzakelijk"),
            ("elimineren", "NVA", "non-value added: pure verspilling"),
        ])),
      after="Ontwerpregel"),

    F(2, "gekozen ontwerp", "Vergelijk je richtingen op vier dimensies", fig(
        "Twee denkhulpen bij haalbaarheid en impact",
        '<div class="lanes"><div class="lane"><h5>Haalbaarheid <small>de wet van de concentratie (80/20)</small></h5>'
        + legend([("c1", "de vitale 20% en wat die veroorzaakt"), ("c0", "de rest")]) + bars([
            dict(label="Activiteiten", segs=[(20, "c1"), (80, "c0")], val="20% vitaal"),
            dict(label="Problemen", segs=[(80, "c1"), (20, "c0")], val="80% daaruit"),
        ], maxv=100, vw="6.4em", label="Twintig procent van de activiteiten veroorzaakt vaak tachtig procent van de problemen")
        + '</div><div class="lane"><h5>Impact <small>de KKT- of duivelsdriehoek</small></h5>' + KKT + "</div></div>",
        noot="De andere twee dimensies zijn risico (eenvoud is bijna altijd een deugd) en aansluiting op de context. Die laatste vergeten studenten het vaakst.")),

    F(2, "gekozen ontwerp", "De PUGH-matrix in 5 stappen", fig(
        "De scoreschaal: elk alternatief tegenover de huidige situatie",
        cards([
            ("−2", "veel slechter", None), ("−1", "slechter", None), ("0", "gelijk aan de baseline", None), ("+1", "beter", None), ("+2", "veel beter", None),
        ], cols=5),
        noot="Vermenigvuldig elke score met het gewicht van het criterium en tel op. Spreek de gewichten af voordat je gaat scoren.")),

    F(2, "gekozen ontwerp", "Rekenvoorbeeld: PUGH op het storingsproces", fig(
        "De gewogen totalen uit het rekenvoorbeeld",
        legend([("c1", "beter dan nu"), ("c2", "slechter dan nu"), ("ref", "nul: de huidige situatie")]) + bars([
            dict(label="Optie A", sub="(2×5) + (−1×3) + (2×4) + (−1×2)", start=1, segs=[(13, "c1")], val="13", ref=1),
            dict(label="Optie B", sub="5 + 0 + 4 + 0", start=1, segs=[(9, "c1")], val="9", ref=1),
            dict(label="Baseline", sub="de huidige situatie", start=1, segs=[(0, "c0")], val="0", ref=1),
            dict(label="Optie C", sub="0 − 3 + 4 − 2", segs=[(1, "c2")], val="−1", neg=True, ref=1),
        ], maxv=14, vw="3em", label="Gewogen totaalscores: optie A 13, optie B 9, baseline 0, optie C min 1"),
        noot="Optie A wint. Optie C scoort slechter dan de huidige situatie; in de slidetabel lijkt dat 0, maar nagerekend is het −1."),
      after="Optie A: (2×5)"),

    F(2, "gekozen ontwerp", "Onderbouwen: waarde voor drie perspectieven", fig(
        "Een sterke onderbouwing verbindt drie perspectieven",
        pillars("Jouw voorkeursoplossing", [
            ("Opdracht" + SH + "gever", "missie, KSF's en KPI's: kosten, betrouwbaarheid, imago, naleving"),
            ("Gebruiker", "meer klantwaarde en betere beleving: sneller, duidelijker, prettiger"),
            ("Proces", "minder verspilling, kortere doorlooptijd, betere flow"),
        ], basis="De oplossing dient geen deelbelang, maar het geheel"),
        noot="Redeneer klantwaarde vanuit de gebruiker, niet vanuit de organisatie.")),

    F(2, "gekozen ontwerp", "Risico afdekken: pilot, simulatie of gefaseerd", fig(
        "Drie manieren om het risico te beheersen",
        cards([
            (None, "Pilot", "op kleine schaal testen in de echte omgeving, daarna evalueren en verfijnen"),
            (None, "Simulatie", "de werkelijkheid veilig nabootsen als een echte test te ingrijpend is"),
            (None, "Gefaseerd", "stap voor stap uitrollen bij grote veranderingen"),
        ]),
        noot="Voorbeeld uit de les: eerst vier weken een pilot op één afdeling met duidelijke meetafspraken."),
      after="Gefaseerd"),

    # ================================================================ week 3
    F(3, "veranderaanpak", "Ratio en gevoel", fig(
        "Verandering loopt langs twee sporen",
        poles([
            ("Waar gaat het over?", ("Ratio", "feiten, cijfers, analyse"), ("Gevoel", "vertrouwen, betrokkenheid, motivatie")),
            ("Wat levert het op?", ("Inzicht", "brengt de noodzaak in beeld, maar motiveert zelden tot nieuw gedrag"), ("Beweging", "hier komen mensen daadwerkelijk in beweging")),
        ]),
        noot="Je advies moet tegelijk kloppen en mensen raken (Kotter).")),

    F(3, "veranderaanpak", "Stap 1: wie heeft hier belang bij?", fig(
        "De belang-invloed-grid: wat doe je met welke stakeholder?",
        quad("Invloed", "Belang", [
            ("Tevreden houden", "veel invloed, weinig belang", None, "t3"),
            ("Nauw betrekken", "veel invloed, veel belang", None, "t1"),
            ("Monitoren", "weinig invloed, weinig belang", None, "t0"),
            ("Informeren", "weinig invloed, veel belang", None, "t2"),
        ], ylaag="weinig", yhoog="veel", xlaag="weinig", xhoog="veel"),
        noot="Let op het rimpeleffect: een verandering raakt vaak ook afdelingen die dachten er niets mee te maken te hebben."),
      after="Tevreden houden"),

    F(3, "veranderaanpak", "Stap 2: weerstand is normaal", fig(
        "De fasen van Carnall",
        flow(["Ontkenning", "Verdediging", "Verwerking", "Aanpassing", "Internali" + SH + "satie"]),
        noot="Optioneel genoemd door de docent. Weerstand is geen onwil, maar een voorspelbare reactie.")),

    F(3, "veranderaanpak", "Stap 3: voorstanders, twijfelaars, tegenstanders (20-60-20)", fig(
        "20-60-20: de middengroep geeft de doorslag",
        seg([
            (20, "c1", "Voorstanders: 20%", "laat ze zichtbaar succes boeken met een quick win"),
            (60, "c0", "Middenmoot: 60%", "nog onbeslist; kiest de kant van de sterkste groep"),
            (20, "c2", "Tegenstanders: 20%", "stop hier niet al je energie in"),
        ]))),

    F(3, "veranderaanpak", "Stap 4: draagvlak bouwen met Kotter-light", fig(
        "Kotter-light in vier stappen",
        flow([
            ("Urgentie", "laat de noodzaak voelen met je eigen cijfers"),
            ("Coalitie", "een zichtbare sponsor plus ambassadeurs"),
            ("Communi" + SH + "catie", "vaak, consistent en in twee richtingen"),
            ("Betrokken" + SH + "heid", "geef mensen een rol en vier quick wins"),
        ]),
        noot="Het oorspronkelijke model van Kotter heeft acht stappen. Stap 8, borg in de cultuur, komt terug in week 5."),
      after="Urgentie"),

    F(3, "veranderaanpak", "RACI: vier rollen per activiteit", fig(
        "Consulted is niet hetzelfde als Informed",
        poles([
            ("Wanneer?", ("Consulted", "vooraf om advies gevraagd"), ("Informed", "achteraf op de hoogte gebracht")),
            ("In welke richting?", ("Dialoog", "tweerichtingsverkeer"), ("Mededeling", "eenrichtingsverkeer")),
        ]),
        noot="Verwar je ze, dan krijg je onnodige vertraging of mensen die zich gepasseerd voelen. Controleer daarnaast elke rij van je RACI: precies één A en minstens één R.")),

    # ================================================================ week 4
    F(4, "implementatie ontwerpen", "Succescriteria SMART maken", fig(
        "Van zwak naar sterk succescriterium",
        poles([
            ("Hoe meetbaar is het?", ("Zwak", "medewerkers gebruiken het portaal beter"), ("Sterk", "binnen 8 weken wordt 80% van de meldingen via het nieuwe portaal ingediend")),
        ]),
        noot="Zonder vooraf afgesproken succescriteria wordt elke evaluatie een kwestie van gevoel.")),

    F(4, "implementatie ontwerpen", "Casus: digitaal meldproces voor storingen", fig(
        "De mijlpalen in de casus",
        flow(["Testomgeving gereed", "Pilot gestart", "Go/no-go", "Organisatie" + SH + "breed live"], numbered=False),
        noot="Mijlpalen zijn controleerbare ijkmomenten in de planning."),
      after="Mijlpalen"),

    F(4, "implementatie ontwerpen", "Risico's scoren: Ernst × Kans × Detectie", fig(
        "Het risicogetal: drie scores met elkaar vermenigvuldigd",
        som([
            ("Ernst", "hoe erg zijn de gevolgen? 1 tot 5"),
            ("Kans", "hoe vaak treedt het op? 1 tot 5"),
            ("Detectie", "hoe moeilijk is het te ontdekken? 1 tot 5"),
        ], ("RPN", "het hoogste getal krijgt de hoogste prioriteit; maximaal 125"), op="×"),
        noot="Detectie werkt omgekeerd: een lage score betekent dat de fout makkelijk wordt opgemerkt, een hoge score dat hij ongezien schade aanricht."),
      after="RPN (Risk Priority Number)"),

    F(4, "implementatie ontwerpen", "Voorbeeld: FMEA-light op het meldproces", fig(
        "De drie risico's op volgorde van RPN",
        bars([
            dict(label="FMIS-koppeling valt uit", sub="ernst 5 × kans 2 × detectie 5", segs=[(50, "c1")], val="50"),
            dict(label="Verkeerde categorie", sub="ernst 4 × kans 3 × detectie 4", segs=[(48, "c1")], val="48"),
            dict(label="Gebruiker blijft bellen", sub="ernst 3 × kans 5 × detectie 2", segs=[(30, "c1")], val="30"),
        ], maxv=50, vw="3em", label="Risk Priority Number per risico"),
        noot="Niet de fout die het vaakst voorkomt krijgt prioriteit, maar de combinatie van ernst, kans en detectie."),
      after="FMIS-koppeling valt uit"),

    F(4, "implementatie ontwerpen", "Hoe ga je live? Vier invoeringsstrategieën", fig(
        "Vier manieren om live te gaan",
        cards([
            ("laagste risico", "Pilot", "klein testen in de echte omgeving en verfijnen"),
            (" ", "Gefaseerd", "stap voor stap, afdeling per afdeling"),
            (" ", "Schaduw" + SH + "draaien", "oud en nieuw tijdelijk naast elkaar"),
            ("hoogste risico", "Big-bang", "in één keer over; snel"),
        ], cols=4),
        noot="Kies bewust, samen met de operationele organisatie. De slide geeft alleen bij pilot en big-bang het risico aan."),
      after="Big-bang"),

    F(4, "implementatie ontwerpen", "Retrospective en eerste stap richting stage (tweede les)", fig(
        "De zeester van de retrospective",
        ZEESTER,
        noot="Eindig met maximaal twee concrete teamacties en maak een foto van de zeester voor je portfolio."),
      after="Groepsproces met de zeester"),

    # ================================================================ week 5
    F(5, "borging", "Het borgingsplan: 6 bouwstenen", fig(
        "Zes bouwstenen en wat elk doet",
        cards([
            ("hoe het hoort", "Standaardisatie", "de werkwijze vastleggen"),
            ("bewaakt", "KPI-opvolging", "blijven meten"),
            ("draagt", "Eigenaarschap", "een vaste verantwoordelijke"),
            ("houdt levend", "Evaluatie" + SH + "momenten", "de PDCA-cyclus draaiend houden"),
            ("maakt overdraagbaar", "Overdracht", "bundelen en actief overdragen"),
            ("borgt de kennis", "Lessons learned", "de geleerde lessen vastleggen"),
        ], cols=3),
        noot="Kernvraag van de Control-fase: wat moet blijven bestaan als het studentteam weg is?"),
      after="Rol in het geheel"),

    F(5, "borging", "Bouwsteen 1: standaardisatie", fig(
        "De vier onderdelen van een SOP",
        flow(["Afbakening", "KPI's en voorschriften", "Volgorde van stappen", "Vastleggen"]),
        noot="Zonder vastgelegde werkwijze ontstaat variatie (mura)."),
      after="SOP"),

    F(5, "borging", "Bouwsteen 4: evaluatiemomenten en de PDCA-cyclus", fig(
        "De PDCA-cyclus bij borging",
        cycle([
            ("Plan", "verbetering en norm"),
            ("Do", "uitvoeren"),
            ("Check", "meten of het proces nog presteert zoals afgesproken"),
            ("Act", "goed: standaard bijwerken; onvoldoende: nieuwe verbeterronde"),
        ], "PDCA-cyclus"),
        noot="Bij borging draait het vooral om Check en Act."),
      after="Betekenis bij borging"),

    F(5, "borging", "Praktijkvoorbeeld: storingsmeldingen bij een zorginstelling", fig(
        "De zorginstelling: doorlooptijd voor en na de pilot",
        legend([("c0", "voor de verbetering"), ("c1", "na de pilot"), ("ref", "norm in het borgingsplan: maximaal 4 dagen")]) + bars([
            dict(label="Voor de verbetering", sub="meldingen via vijf kanalen", segs=[(11, "c0")], val="11 dagen", ref=4),
            dict(label="Na de pilot", sub="één centraal digitaal meldpunt", segs=[(3, "c1")], val="3 dagen", ref=4),
        ], maxv=11, vw="5em", label="Gemiddelde doorlooptijd: 11 dagen voor de verbetering, 3 dagen na de pilot, norm maximaal 4 dagen"),
        noot="Zonder borging is de afdeling binnen enkele maanden terug bij de gele briefjes."),
      after="Pilot: doorlooptijd daalt"),

    F(5, "Training", "Structuur: inleiding, kern, slot, en de kern volgens PROA", fig(
        "PROA: de kern van je adviespresentatie",
        flow([
            ("Probleem", "wat is het probleem?"),
            ("Risico", "wat is de omvang?"),
            ("Oorzaak", "wat is de oorzaak?"),
            ("Advies", "mogelijkheden, implementatie en grip op de resultaten"),
        ], numbered=False),
        noot="Probleem en risico komen uit Define en Measure, oorzaak uit Analyze, advies uit Generate, Improve en Control."),
      after="Fase in je project"),

    # ================================================================ week 6
    F(6, "overdracht en lessons", "Wie neemt het over? De proceseigenaar", fig(
        "Lean Back: wie doet wat?",
        poles([
            ("Welke rol heb je?", ("Studentteam", "stuurt en faciliteert; de rol is tijdelijk"), ("Proces" + SH + "eigenaar", "heeft het mandaat en is verantwoordelijk voor de uitvoering")),
        ]),
        noot="Eigenaarschap ontstaat niet vanzelf op het overdrachtsmoment: betrek de eigenaar nu al.")),

    F(6, "overdracht en lessons", "Het overdrachtsdossier: alles op één plek", fig(
        "Wat zit er in het overdrachtsdossier?",
        tree("Overdrachts" + SH + "dossier", [
            ("Werk" + SH + "standaard", "de SOP of EPL"),
            ("Borgings" + SH + "plan", "KPI's, normen, evaluatieritme"),
            ("Eigenaar" + SH + "schap", "wie, met welke afspraken"),
            ("Project" + SH + "documentatie", "analyse, current en future state"),
            ("Losse eindjes", "open acties en lessons learned"),
        ]),
        noot="Vuistregel: zo compleet dat iemand zonder jullie ermee verder kan."),
      after="Losse eindjes"),

    F(6, "overdracht en lessons", "De overdracht maak je formeel: de Tollgate", fig(
        "Van Tollgate tot afgesloten project",
        flow([
            ("Tollgate", "samenvatten, terugkijken, toetsen aan de succescriteria en formeel overdragen"),
            ("Verankeren", "processen, procedures en administratieve organisatie bijwerken"),
            ("Archiveren", "de documenten toegankelijk bewaren"),
            ("Team ontbinden", "pas als de proceseigenaar het echt kan dragen"),
        ]),
        noot="Gouden regel: draag pas over als de proceseigenaar het echt kan dragen.")),

    F(6, "overdracht en lessons", "Deel 2: lessons learned vastleggen", fig(
        "Zo leert de hele organisatie",
        flow(["Observeren", "Verbeteren", "Vastleggen"], loop="elke les komt in de bijgewerkte standaard"),
        noot="Beslissingen gelden alleen voor de toekomst: het rendement is er voor het volgende team en de opdrachtgever.")),

    # ================================================================ week 7
    F(7, "afronding", "Stap 1: Control betekent je verbetering laten standhouden", fig(
        "Wat Control oplevert",
        cards([
            (None, "Minder variatie", "het proces loopt elke keer hetzelfde"),
            (None, "Voorspelbaar resultaat", "afwijkingen vallen direct op"),
            (None, "Snel bijsturen", "actie zodra je van de norm afwijkt"),
        ]),
        noot="Eén keer goed werken is geen verbetering, dat is toeval.")),

    F(7, "afronding", "Stap 2: afronden is de Act in de PDCA-cyclus", fig(
        "Afronden is de Act-stap",
        cycle([
            ("Plan", "bepaal wat je verandert"),
            ("Do", "test op kleine schaal"),
            ("Check", "meet of het werkt"),
            ("Act", "borg en maak het standaard"),
        ], "PDCA-cyclus"),
        noot="Daarna begint de cyclus opnieuw, bij een organisatie die zelf blijft verbeteren (Kaizen)."),
      after="Bepaal wat je verandert"),

    F(7, "afronding", "Stap 7: retrospective op het teamproces", fig(
        "Lessons learned of retrospective?",
        poles([
            ("Waar gaat het over?", ("Lessons learned", "de aanpak: wat werkte bijzonder goed en wat juist niet"), ("Retro" + SH + "spective", "jullie samenwerking: wat behouden, wat anders, wat nemen we mee")),
        ]),
        noot="De uitkomsten van de retrospective voeden je individuele portfolio."), pos="top"),

    F(7, "afronding", "De opdracht in de les: je overdrachtspakket (60 min)", fig(
        "Het overdrachtspakket in 60 minuten",
        seg([
            (15, "c1", "Deel A: einddossier-check, 15 min", "ingevulde checklist plus actielijst"),
            (25, "c2", "Deel B: borgingskaart, 25 min", "je verbeterde proces op één pagina"),
            (20, "c3", "Deel C: overdrachtsplan en lessons, 20 min", "3 lessons learned en 3 retro-uitkomsten"),
        ])),
      after="Deel C"),
]
