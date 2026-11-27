"""Begrippen Praktijkproject Business Management, per les. Alles komt uit scripts/samenvattingen/praktijkproject/
(slides en sprekersnotities). Zie inkoop_recht.py voor de velden.
"""
from begrip import b

G = " (Gangbare invulling: de slides leggen het niet uit.)"

B = [
    # ---------------- Week 1: terugblik en verbeterrichtingen
    b("pp-w1", "DMAGIC", "Verbetermodel met de fasen Define, Measure, Analyze, Generate, Improve en Control; de Generate-fase is bewust toegevoegd aan DMAIC."),
    b("pp-w1", "Generate-fase", "De fase waarin je verbeterrichtingen bedenkt en kiest, zodat je niet te snel naar de eerste oplossing springt.", ook=("generate",)),
    b("pp-w1", "Kaizen", "Continu verbeteren als gewoonte, in kleine stappen, door iedereen."),
    b("pp-w1", "Gemba", "De werkvloer: de plek waar het werk echt gebeurt en waar je de kansen ziet."),
    b("pp-w1", "Divergeren", "Zoveel mogelijk ideeën verzamelen zonder te oordelen (week 1)."),
    b("pp-w1", "Convergeren", "Kiezen en onderbouwen van één voorkeursoplossing (week 2)."),
    b("pp-w1", "Klantwaarde", "Een activiteit is pas waardevol als de klant er echt iets aan heeft; Lean begint bij het specificeren van waarde vanuit de klant."),
    b("pp-w1", "11 facilitaire toegevoegde waarden", "Toets voor elke verbeterrichting: productiviteit, kosten, risico's, waardestijging, flexibiliteit, cultuur, imago, innovatie, tevredenheid, duurzaamheid en healing environment.", ook=("facilitaire toegevoegde waarden", "toegevoegde waarden")),
    b("pp-w1", "Just in Time", "Lean-principe (pijler snelheid): precies wat nodig is, op het juiste moment.", ook=("JIT",)),
    b("pp-w1", "Jidoka", "Lean-pijler kwaliteit: bouw het goed in bij de bron en geef geen fout door naar de volgende stap."),
    b("pp-w1", "Kanban", "Pull-principe: start werk pas op een signaal, bijvoorbeeld een bord met nieuw, opgepakt en opgelost.", ook=("pull",)),
    b("pp-w1", "Heijunka", "Lean-principe dat werkdruk en pieken spreidt."),
    b("pp-w1", "Theory of Constraints", "Verbeter de zwakste schakel (bottleneck), want die bepaalt de output.", ook=("TOC", "bottleneck")),
    b("pp-w1", "Poka-Yoke", "Ontwerp het zo dat de fout niet gemaakt kán worden, zoals verplichte velden op een meldformulier.", ook=("poka yoke",)),
    b("pp-w1", "5S", "Orde en netheid die fouten en variatie voorkomen; de vijfde S (Standhouden) vraagt discipline om de afspraak te blijven volgen."),
    b("pp-w1", "Impact/Effort-matrix", "Matrix waarin je elk idee op impact en moeite zet, om bewust minstens één quick win en één structurele verbetering te kiezen.", ook=("impact effort matrix",)),
    b("pp-w1", "Quick win", "Verbetering met veel impact en weinig moeite; geeft momentum en draagvlak, maar lost vaak alleen een symptoom op."),

    # ---------------- Week 2: van verbeterrichtingen naar gekozen ontwerp
    b("pp-w2", "Future state", "Het beeld van het ideale proces met alleen waardetoevoegende stappen; je ontwerpt eerst de droom en redeneert terug naar wat haalbaar is.", ook=("toekomstbeeld",)),
    b("pp-w2", "Current state", "De beschrijving van de huidige situatie van het proces, gemaakt in periode 1."),
    b("pp-w2", "VA", "Value added: een stap waarvoor de klant wil betalen. Ontwerpregel: behouden en versterken.", ook=("value added",)),
    b("pp-w2", "BNVA", "Business non-value added: geen klantwaarde, maar wel noodzakelijk, zoals registratie of regelgeving. Ontwerpregel: minimaliseren.", ook=("business non-value added",)),
    b("pp-w2", "NVA", "Non-value added: pure verspilling, zoals drie keer overtypen. Ontwerpregel: elimineren.", ook=("non-value added",)),
    b("pp-w2", "Muda", "Lean-term voor verspilling."),
    b("pp-w2", "Mura", "Lean-term voor onnodige variatie; ontstaat als een werkwijze niet is vastgelegd."),
    b("pp-w2", "Muri", "Lean-term voor overbelasting."),
    b("pp-w2", "Service blueprint", "Vorm om het toekomstbeeld vast te leggen die scheidt wat de gebruiker ziet (frontstage) van het werk erachter (backstage)."),
    b("pp-w2", "Future-state map", "De volledige waardestroom van begin tot eind na verbetering, met tijden en informatiestromen; de meest complete vorm."),
    b("pp-w2", "One Piece Flow", "Stuk voor stuk door het proces in plaats van in batches." + G),
    b("pp-w2", "Takttijd", "De beschikbare tijd gedeeld door de klantvraag: het tempo waarin de klant vraagt." + G),
    b("pp-w2", "FIFO", "First in, first out: oppakken in volgorde van binnenkomst." + G, ook=("first in first out",)),
    b("pp-w2", "Wet van de concentratie", "Vaak veroorzaakt 20% van de activiteiten 80% van de problemen; pak die vitale 20% aan.", ook=("80/20-regel", "Pareto")),
    b("pp-w2", "Duivelsdriehoek", "Kwaliteit, kosten en tijd: je kunt zelden alles tegelijk verbeteren.", ook=("KKT-driehoek",)),
    b("pp-w2", "PUGH-matrix", "Oplossingenmatrix (Stuart Pugh) waarin je alternatieven met gewogen criteria van −2 tot +2 scoort ten opzichte van de baseline; de hoogste totaalscore wint.", ook=("PUGH", "oplossingenmatrix")),
    b("pp-w2", "Baseline", "In de PUGH-matrix de huidige situatie, die op elk criterium score 0 krijgt."),
    b("pp-w2", "Pilot", "Test op kleine schaal in de echte omgeving, met vooraf een plan, meetafspraken en getrainde medewerkers; de invoeringsstrategie met het laagste risico."),

    # ---------------- Week 3: veranderaanpak en draagvlak
    b("pp-w3", "Stakeholder", "Iedereen die invloed heeft op je verbetering óf er gevolgen van ondervindt."),
    b("pp-w3", "Rimpeleffect", "Een verandering raakt vaak ook afdelingen die dachten er niets mee te maken te hebben."),
    b("pp-w3", "Sponsor", "Stakeholderrol: maakt mensen en middelen vrij en heeft mandaat."),
    b("pp-w3", "Proceseigenaar", "De lijnmanager met mandaat die verantwoordelijk is voor het proces en het na de overdracht voortzet en verder verbetert."),
    b("pp-w3", "Belang-invloed-grid", "Indeling van stakeholders op belang en invloed: nauw betrekken, tevreden houden, informeren of monitoren.", ook=("belang-invloedmatrix", "stakeholdermatrix")),
    b("pp-w3", "Weerstand", "Geen onwil maar een voorspelbare reactie op opgelegde verandering, bijvoorbeeld door verlies aan controle of onzekerheid."),
    b("pp-w3", "20-60-20-regel", "Bij een verandering is grofweg 20% voorstander, 60% onbeslist en 20% tegenstander; de middengroep kiest de kant van de sterkste groep.", ook=("20-60-20",)),
    b("pp-w3", "Kotter-light", "Vereenvoudigde versie van Kotters acht stappen met vier stappen: urgentie, coalitie, communicatie en betrokkenheid."),
    b("pp-w3", "Fasen van Carnall", "Fasen die mensen bij verandering doorlopen: ontkenning, verdediging, verwerking, aanpassing en internalisatie.", ook=("Carnall",)),
    b("pp-w3", "RACI", "Methode die per activiteit de rollen vastlegt: Responsible, Accountable (precies één), Consulted en Informed."),
    b("pp-w3", "Accountable", "RACI-rol die goedkeurt en eindverantwoordelijk is; altijd precies één per activiteit."),
    b("pp-w3", "Consulted", "RACI-rol die vooraf om advies wordt gevraagd: tweerichtingsverkeer."),
    b("pp-w3", "Informed", "RACI-rol die achteraf op de hoogte wordt gebracht: eenrichtingsverkeer."),
    b("pp-w3", "TBV's", "Taken, bevoegdheden en verantwoordelijkheden die je per activiteit vastlegt.", ook=("TBV", "taken bevoegdheden verantwoordelijkheden")),
    b("pp-w3", "RASCI", "Uitbreiding van RACI met S voor Support (ondersteunt actief).", ook=("CAIRO",)),

    # ---------------- Week 4: implementatie en risico's
    b("pp-w4", "Implementeren", "Het invoeren van de gekozen oplossing in het proces; in het implementatieplan staan alle activiteiten en wie wat wanneer doet.", ook=("implementatie",)),
    b("pp-w4", "Mijlpaal", "Controleerbaar ijkmoment in de planning, zoals 'training afgerond' of 'go/no-go'.", ook=("mijlpalen",)),
    b("pp-w4", "Randvoorwaarden", "Wat moet kloppen vóór je start, zoals een werkende systeemkoppeling, budget of toegang."),
    b("pp-w4", "Succescriteria", "SMART geformuleerde maatstaven waaraan je meet of de implementatie gelukt is, gekoppeld aan KPI's en klantwaarde.", ook=("succescriterium",)),
    b("pp-w4", "Catchball", "De oplossing met mensen invoeren door hen om feedback te vragen, zodat ze mede-eigenaar worden."),
    b("pp-w4", "FMEA", "Failure Mode and Effect Analysis: gestructureerd potentiële fouten in een proces opsporen en aanpakken vóórdat ze optreden (oorspronkelijk van de NASA).", ook=("Failure Mode and Effect Analysis", "FMEA-light")),
    b("pp-w4", "Failure mode", "De faalmogelijkheid in een processtap: wat zou hier fout kunnen gaan?", ook=("faalmogelijkheid",)),
    b("pp-w4", "RPN", "Risk Priority Number: Ernst × Kans × Detectie; het hoogste getal krijgt de hoogste prioriteit (maximaal 125 op een schaal van 1-5).", ook=("Risk Priority Number", "risicoprioriteitsgetal")),
    b("pp-w4", "Detectiescore", "FMEA-factor: een lage score betekent dat een fout makkelijk wordt opgemerkt, een hoge dat hij ongezien schade aanricht.", ook=("detectie",)),
    b("pp-w4", "Schaduwdraaien", "Invoeringsstrategie waarbij oud en nieuw tijdelijk naast elkaar draaien."),
    b("pp-w4", "Big-bang", "Invoeringsstrategie waarbij je in één keer overgaat; snel, maar met het hoogste risico.", ook=("big bang",)),
    b("pp-w4", "Gefaseerd invoeren", "Invoeringsstrategie waarbij je stap voor stap uitrolt, afdeling per afdeling.", ook=("gefaseerd",)),
    b("pp-w4", "OCAP", "Out of Control Action Plan: een vooraf klaarliggend noodplan met triggers en acties voor als het toch misgaat.", ook=("Out of Control Action Plan",)),
    b("pp-w4", "Zeester", "Retrospective-werkvorm met vijf vakken: blijven doen, meer van, minder van, stoppen en starten."),

    # ---------------- Week 5: borging en eigenaarschap
    b("pp-w5", "Borgen", "De verbetering loskoppelen van de aanwezigheid van het studentteam, zodat ze blijft werken. Kernvraag: wat moet blijven bestaan als het team weg is?", ook=("borging",)),
    b("pp-w5", "Control-fase", "De laatste DMAGIC-fase: zorgen dat het verbeterde proces betrouwbaar, voorspelbaar en herhaalbaar blijft en het probleem niet terugkomt.", ook=("control",)),
    b("pp-w5", "Borgingsplan", "Plan met zes bouwstenen: standaardisatie, KPI-opvolging, eigenaarschap, evaluatiemomenten, overdracht en lessons learned."),
    b("pp-w5", "Standaardwerk", "De afgesproken, vastgelegde manier van werken; volgens Lean de basis van verbetering.", ook=("standaardisatie",)),
    b("pp-w5", "SOP", "Standard Operating Procedure: werkinstructie met afbakening, KPI's en voorschriften, volgorde van stappen en vastleggen.", ook=("Standard Operating Procedure", "werkinstructie")),
    b("pp-w5", "Visueel management", "Zichtbaar maken of er volgens de standaard wordt gewerkt, bijvoorbeeld een SOP of KPI-bord bij de servicedesk.", ook=("visual control",)),
    b("pp-w5", "Ingrijpgrens", "Vooraf bepaalde waarde van een KPI waarbij je ingrijpt, zodat je 'out of control' ziet aankomen."),
    b("pp-w5", "PDCA-cyclus", "Plan, Do, Check, Act (Shewhart en Deming): de motor van continu verbeteren. Bij borging draait het vooral om Check en Act.", ook=("PDCA", "Deming-cirkel")),
    b("pp-w5", "Respect voor mensen", "Lean-waarde: betrek medewerkers, neem hun zorgen serieus en vier successen, zodat hún verbetering het vertrek van het team overleeft."),
    b("pp-w5", "Overdrachtsdossier", "Bundel van SOP's, KPI-definities, eigenaarschap en evaluatieafspraken die je actief overdraagt, zo compleet dat iemand zonder jullie verder kan."),
    b("pp-w5", "Lessons learned", "Vastgelegde lessen over wat goed ging, wat stroef liep en welke aannames niet klopten; borgt niet het proces maar de kennis."),

    # ---------------- Training 3: de adviespresentatie
    b("pr-w5", "PROA", "Structuur van de kern van een adviespresentatie: Probleem, Risico (omvang), Oorzaak en Advies."),
    b("pr-w5", "Show, don't tell", "Visualiseringstip: laat zien in plaats van vertellen, bijvoorbeeld een getekend proces met gemarkeerde knelpunten."),
    b("pr-w5", "Visuele ruis", "Alles op een slide wat niet bijdraagt aan de boodschap en daardoor afleidt."),

    # ---------------- Week 6: overdracht en lessons learned
    b("pp-w6", "Lean Back", "Het studentteam stuurt en faciliteert, de proceseigenaar heeft het mandaat en is verantwoordelijk voor de uitvoering."),
    b("pp-w6", "EPL", "Visuele werkinstructie van één A4; in Lean meestal 'één-punt-les'.", ook=("één-punt-les", "een-punt-les")),
    b("pp-w6", "Tollgate", "Formeel overdrachtsgesprek (projectafsluiting) met de belanghebbenden, waarop je toetst aan de succescriteria en de verantwoordelijkheid overdraagt."),
    b("pp-w6", "Storyboard", "Korte samenvatting van het project, vaak op één pagina, die de rode draad toegankelijk maakt."),
    b("pp-w6", "Best practice", "Een geleerde les die zo sterk is dat ze herbruikbaar is in vergelijkbare projecten."),

    # ---------------- Week 7: afronding
    b("pp-w7", "Einddossier", "Alle tussenproducten samengebracht tot één definitief adviespakket, getoetst op volledig, consistent en toegankelijk."),
    b("pp-w7", "Borgingskaart", "Mini-SOP van één pagina met proces en afbakening, proceseigenaar, twee KPI's met norm, hoe het geborgd is en de losse eindjes."),
    b("pp-w7", "SIPOC", "Supplier, Input, Process, Output, Customer; helpt bij de afbakening van een proces." + G),
    b("pp-w7", "Retrospective", "Terugblik op de samenwerking in het team: wat ging goed, wat kon beter en wat nemen we mee. (Lessons learned gaan over de aanpak.)", ook=("retro",)),
    b("pp-w7", "Losse eindjes", "Wat de organisatie na de overdracht nog moet regelen, zoals een aankoop, training of besluit; benoem ze expliciet in het dossier."),
]
