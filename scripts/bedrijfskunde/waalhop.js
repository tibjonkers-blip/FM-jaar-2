const TOPICS = [
  { id: "inleiding", label: "Inleiding & 7S", kort: "Inleiding" },
  { id: "strategie", label: "Strategy", kort: "Strategy" },
  { id: "structure", label: "Structure", kort: "Structure" },
  { id: "systems", label: "Systems", kort: "Systems" },
  { id: "staffstyle", label: "Staff & Style", kort: "Staff & Style" },
  { id: "skillssv", label: "Skills & Shared values", kort: "Skills & SV" },
  { id: "recht", label: "Ondernemingsrecht", kort: "Recht" }
];

const CASES = {
  inleiding: {
    titel: "Casus 1 · Over Waalhop",
    html: `
<p><strong>Waalhop Groep</strong> (fictief) is een brouwerijconcern uit Nijmegen. In 1952 begon brouwer Gerrit Waal een kleine brouwerij als eenmanszaak achter zijn café aan de Waalkade. Inmiddels werken er 640 mensen samen in het brouwen, bottelen, verkopen en vervoeren van bier en frisdrank. Waalhop wil winstgevend groeien en investeert dit jaar € 12 miljoen in een nieuwe, energiezuinige bottellijn, zodat het bedrijf ook over twintig jaar nog bestaat.</p>
<p>Naast de groep bestaat de <strong>Stichting Waalhop Cultuurfonds</strong>. Het fonds krijgt elk jaar een bijdrage van Waalhop en sponsort daarmee lokale muziekfestivals en buurtfeesten. Het fonds verkoopt niets, maakt geen winst en heeft twee vrijwillige bestuurders.</p>
<p>In de bottelarij is het werk sinds de jaren zestig tot op de seconde uitgemeten. Voor elke handeling geldt een normtijd, vastgesteld met tijdstudies. Operators doen de hele dienst dezelfde handeling. De nieuwe HR-manager merkt dat het verzuim in de bottelarij hoog is en dat operators klagen over saai werk en weinig contact met collega's.</p>
<p>Marketingdirecteur Ramon de Bruin wil de komende jaren vol inzetten op alcoholvrij bier. "We passen gewoon onze strategie aan, verder hoeft er niets te veranderen," zegt hij in het managementteam.</p>`
  },
  strategie: {
    titel: "Casus 2 · Koers 2030",
    html: `
<p>Waalhop Groep bestaat uit drie business units (BU's): <strong>Brouwerij Nijmegen</strong> (pils en alcoholvrij bier), <strong>Brouwerij De Linge</strong> (speciaalbier) en <strong>Waalhop Dranken</strong> (frisdrank). CEO is Marloes Verbeek.</p>
<p><strong>Missie en visie.</strong> Op de website staan twee uitspraken:<br>(A) "Wij brengen mensen samen rond eerlijk gebrouwen bier uit onze regio."<br>(B) "In 2035 is Waalhop dé duurzame brouwer van Oost-Nederland."</p>
<div class="tablewrap"><table>
<thead><tr><th>Productgroep</th><th>Marktgroei per jaar</th><th>Relatief marktaandeel*</th></tr></thead>
<tbody>
<tr><td>Pils</td><td>1%</td><td>1,8</td></tr>
<tr><td>Alcoholvrij bier</td><td>14%</td><td>1,3</td></tr>
<tr><td>Speciaalbier</td><td>11%</td><td>0,5</td></tr>
<tr><td>Frisdrank</td><td>−2%</td><td>0,4</td></tr>
</tbody></table></div>
<p class="footnote">* Eigen marktaandeel gedeeld door het marktaandeel van de grootste concurrent.</p>
<p><strong>Cijfers.</strong> In 2025 was de omzet € 182 miljoen. De raad van bestuur wil in 2030 minimaal € 210 miljoen omzet halen. Bij ongewijzigd beleid verwacht de afdeling Financiën voor 2030 een omzet van € 176 miljoen.</p>
<p><strong>Plannen.</strong> Voor 2030 liggen vier plannen op tafel:</p>
<ol>
<li>De bestaande pils gaan verkopen via een Duitse supermarktketen.</li>
<li>Een nieuw alcoholvrij IPA ontwikkelen voor de huidige klanten in Nederland.</li>
<li>Eigen brouwcafés openen in vijf Gelderse steden.</li>
<li>Met 'drie halen, twee betalen'-acties bestaande klanten meer pils laten kopen.</li>
</ol>
<p><strong>Concurrentie.</strong> De Linge brouwt kleine series speciaalbier voor liefhebbers en speciaalbiercafés. Het bier is duur, maar heeft een unieke smaak en wint regelmatig prijzen. Waalhop Dranken maakt frisdrank vooral als huismerk voor supermarkten. Deze BU richt al haar processen in op een zo laag mogelijke kostprijs per liter en levert foutloos en op tijd. In alcoholvrij bier is Waalhop de grootste van Nederland.</p>
<p><strong>Omgeving.</strong> Het kabinet verhoogt de accijns op bier. Jongeren drinken steeds minder alcohol. Door droge zomers wordt brouwgerst duurder. Elk jaar openen er tientallen nieuwe ambachtelijke brouwerijen. Drie grote supermarktketens nemen samen 70% van Waalhops pils af en eisen elk jaar lagere inkoopprijzen. Ook kombucha en alcoholvrije mocktails winnen terrein.</p>
<p><strong>Nieuw idee.</strong> De directeur van De Linge wil een app laten bouwen waarmee klanten zelf een bier samenstellen: smaak, kleur en alcoholpercentage. De Linge brouwt het op bestelling en bezorgt het thuis. Geen andere brouwer in Nederland biedt dit aan.</p>`
  },
  structure: {
    titel: "Casus 3 · Brouwerij Nijmegen",
    html: `
<p>Brouwerij Nijmegen is de grootste BU van Waalhop Groep. Directeur is Joost Hendriks. Onder hem staan drie afdelingshoofden: <strong>Brouwen</strong>, <strong>Bottelen</strong> en <strong>Logistiek</strong>. Daarnaast zijn er de afdelingen Planning, HRM, Financiën, Facility Management en het Kwaliteitslab. Die afdelingen adviseren en ondersteunen de directeur en de afdelingshoofden, maar hebben zelf geen zeggenschap over de productie. Eén uitzondering: als het Kwaliteitslab een besmetting vindt, mag het lab zelf een bottellijn stilleggen.</p>
<p>De afdeling Planning legt per week tot op het kwartier vast wat elke lijn produceert. Alle afdelingen werken volgens vaste procedures en werkinstructies. Het werk is routinematig: elke week worden dezelfde soorten bier gebrouwen en gebotteld. Alle beslissingen over productievolumes, investeringen en werktijden neemt Joost zelf.</p>
<p><strong>Bottelen.</strong> De bottelarij heeft vier lijnen. Op elke lijn werken drie ploegen: ploeg 1 reinigt de flessen, ploeg 2 vult en dopt, ploeg 3 etiketteert en verpakt. Ploegleider Bas van Dijk geeft leiding aan 22 operators. Tussen Joost en een operator zitten twee lagen: het afdelingshoofd en de ploegleider.</p>
<p><strong>Werkdruk.</strong> Operators klagen over eentonig werk. HRM stelt twee maatregelen voor:</p>
<ol>
<li>Operators wisselen elke twee uur van taak tussen vullen, etiketteren en verpakken.</li>
<li>Elke ploeg wordt ook verantwoordelijk voor het eigen kleine onderhoud, de kwaliteitscontrole en het maken van het ploegrooster.</li>
</ol>
<p><strong>De groep.</strong> Waalhop Groep bestaat uit drie BU's, elk met een eigen directie. De BU's bepalen zelf welke producten ze maken en hoe. De holding stuurt de BU's aan op omzet- en winstdoelen.</p>`
  },
  systems: {
    titel: "Casus 4 · Van gerst tot krat",
    html: `
<p>Bij Brouwerij Nijmegen begint alles bij Inkoop, die mout, hop en flessen inkoopt. Vrachtwagens lossen de grondstoffen bij de silo's en in het magazijn. In het brouwhuis worden mout, water en hop gebrouwen tot bier; daarna rijpt het bier zes weken in lagertanks. De bottelarij vult het bier in flessen en fusten. Logistiek levert de kratten met eigen vrachtwagens aan supermarkten en cafés. Marketing &amp; Verkoop onderhoudt de contacten met afnemers en de klantenservice behandelt klachten.</p>
<p><strong>Ondersteuning.</strong> HRM, ICT, Financiën en Facility Management ondersteunen het primaire proces. FM, onder leiding van Wouter Arts, beheert het gebouw, de stoominstallatie, de koelinstallatie van de lagertanks, de schoonmaak en het bedrijfsrestaurant. Valt de koeling uit, dan moet een hele tank bier worden weggegooid.</p>
<p><strong>Klachten.</strong> Afgelopen maand meldden cafés via de klantenservice dat het bier troebel uit de tap kwam. Het Kwaliteitslab ontdekte dat het filter in de bottelarij verkeerd was afgesteld. De instelling is aangepast.</p>
<p><strong>Doelen.</strong> Het managementteam stelt elk jaar het budget en de strategische doelen vast. Dit jaar is een van de doelen: het waterverbruik omlaag van 4 naar 3 liter water per liter bier. FM brengt daarom alle energie- en waterstromen in de brouwerij in kaart.</p>`
  },
  staffstyle: {
    titel: "Casus 5 · Mensen van Waalhop",
    html: `
<p>De arbeidsmarkt voor brouwers en operators is krap. HR-manager Esra Yıldız heeft daarom vier maatregelen genomen:</p>
<ul>
<li>Medewerkers die een nieuwe collega aandragen, krijgen € 500 als die collega wordt aangenomen.</li>
<li>Nieuwe medewerkers krijgen de eerste drie maanden een buddy en een inwerkprogramma.</li>
<li>Elke medewerker heeft jaarlijks een ontwikkelgesprek en kan cursussen volgen bij de Waalhop Brouwacademie.</li>
<li>Met elke vertrekkende medewerker voert HRM een exitgesprek.</li>
</ul>
<p>Esra besteedt nu het grootste deel van haar tijd aan salarisadministratie, contracten en verlofregistratie. De directie wil dat zij vanaf volgend jaar aan tafel zit bij het managementteam om mee te denken over de koers van Waalhop.</p>
<p><strong>Arbeidsvoorwaarden.</strong> Een operator verdient € 2.950 bruto per maand. Via de cao bouwt iedere medewerker pensioen op. Accountmanagers in de buitendienst krijgen een leaseauto.</p>
<p><strong>Leiderschap.</strong> Directeur Joost Hendriks is ervan overtuigd dat medewerkers graag verantwoordelijkheid nemen en zelf met verbeteringen komen. Hij laat ploegen zelf hun doelen voorstellen en neemt besluiten samen met zijn afdelingshoofden.</p>
<p>Ploegleider Bas heeft twee nieuwe situaties. <strong>Lotte</strong> is twee weken in dienst als operator. Ze is enthousiast, maar heeft nog nooit een vullijn bediend; Bas laat haar "lekker zelf uitzoeken hoe het werkt". <strong>Henk</strong> werkt al 25 jaar aan de lijn en kent elke machine, maar sinds de reorganisatie twijfelt hij of zijn werk nog gewaardeerd wordt en doet hij het minimale.</p>
<p><strong>Petra</strong>, hoofd Logistiek, zegt: "Mensen zijn er om het werk te doen. Hoe ze zich voelen, is niet mijn probleem." Ze stuurt alleen op levertijden en kilometers.</p>
<p><strong>Conflict.</strong> Bottelen en Logistiek ruziën over de planning van lege kratten: Bottelen wil ze 's ochtends, Logistiek 's middags. Joost hakt zonder overleg de knoop door: Logistiek moet zich aanpassen.</p>
<p>Na een maand vertelt Lotte aan Bas: "Het werk is prima, maar ik ken nog bijna niemand. Ik wil vooral bij de ploeg horen."</p>`
  },
  skillssv: {
    titel: "Casus 6 · Kwaliteit en cultuur bij De Linge",
    html: `
<p>Brouwerij De Linge in Leerdam heeft 85 medewerkers. Oprichter en directeur Gijs van Asperen bepaalt sinds 1998 alles zelf, van de recepten tot de kleur van de etiketten. Medewerkers werken graag samen en helpen elkaar, maar waaraan gewerkt wordt, beslist Gijs.</p>
<p><strong>Cultuur.</strong> De brouwers dragen zwarte schorten met het oude logo. Elke vrijdag om vier uur proeft het hele bedrijf samen de nieuwe batch. In de hal hangt een muur met medailles. Op de website staat de kernwaarde "Ambacht boven alles". Nieuwe medewerkers merken al snel dat iedereen ervan uitgaat dat "machines het bier verpesten": voorstellen om te automatiseren worden steeds weer afgewezen.</p>
<p><strong>Sleutelvaardigheid.</strong> De Linge staat erom bekend dat ze elk jaar nieuwe, prijswinnende recepten ontwikkelt in kleine series.</p>
<p><strong>Kwaliteit.</strong> Tot nu toe test het lab aan het eind van elke batch een paar flessen; een slechte batch wordt afgekeurd. Vorige maand ging het mis: door te veel koolzuur sprongen flessen kapot in de koelkast van een café. Kwaliteitsmanager Noor Bakker wil dat kwaliteit voortaan "van iedereen" is: elke brouwer meet zelf in elke stap, fouten worden geregistreerd en er wordt continu verbeterd. Ze wil ook een zelfevaluatie doen met het INK-managementmodel.</p>
<p>Noor stelt voor het MT vier prestatie-indicatoren op:</p>
<ol>
<li>omzet uit speciaalbier;</li>
<li>klanttevredenheid bij speciaalbiercafés;</li>
<li>percentage afgekeurde batches;</li>
<li>aantal opleidingsuren per brouwer.</li>
</ol>
<p><strong>Facility management.</strong> Facility manager Wouter Arts wil een nieuwe, beter regelbare koelcel. Zijn voorstel aan Gijs begon met: "We kopen een koelcel van 40 m³ met digitale temperatuurregeling van merk X." Gijs las het niet eens uit.</p>
<p><strong>Overname.</strong> Waalhop Dranken neemt een frisdrankfabriek in Polen over. De Nederlandse managers merken dat de Poolse medewerkers duidelijke instructies van hun leidinggevende verwachten en hun baas niet snel tegenspreken. Ook willen zij graag vaste regels en procedures.</p>`
  },
  recht: {
    titel: "Ondernemingsrecht · meerkeuze",
    html: `
<p>Volgens de laatste dia van de rechtlessen wordt ondernemingsrecht op de toets met <strong>meerkeuzevragen</strong> getoetst. Je mag daarbij de wettenbundel gebruiken. Elke vraag heeft een eigen korte casus uit de wereld van Waalhop.</p>
<p>Stof volgens de dia's: hoofdstuk 16 en 17 (algemene aspecten en eenmanszaak), hoofdstuk 20 (§ 1 t/m 5), hoofdstuk 22 (§ 1 t/m 4 en 7 t/m 8) en hoofdstuk 23 (§ 1 t/m 4).</p>`
  }
};

/* Open vragen: rubric = [beoordelingspunt, punten] */
const QUESTIONS = [
  /* ---------------- INLEIDING ---------------- */
  {
    id: "I1", topic: "inleiding", type: "open", pts: 3, model_naam: "Kenmerken van een organisatie",
    q: "Noem de drie kenmerken van een organisatie en geef bij elk kenmerk een voorbeeld uit de casus.",
    model: `<ul>
<li><mark>Samenwerkingsverband</mark>: 640 medewerkers werken samen aan brouwen, bottelen, verkopen en vervoeren. Samen bereiken ze meer dan ieder afzonderlijk (synergie).</li>
<li><mark>Doelgerichtheid</mark>: Waalhop wil winstgevend groeien.</li>
<li><mark>Continuïteit</mark>: Waalhop investeert € 12 miljoen in een nieuwe bottellijn, zodat het bedrijf over twintig jaar nog bestaat.</li></ul>`,
    rubric: [["Samenwerkingsverband met passend casusvoorbeeld", 1], ["Doelgerichtheid met passend casusvoorbeeld", 1], ["Continuïteit met passend casusvoorbeeld", 1]]
  },
  {
    id: "I2", topic: "inleiding", type: "open", pts: 3, model_naam: "Organisatie, bedrijf, onderneming",
    q: "Is Waalhop Groep een organisatie, een bedrijf of een onderneming? En de Stichting Waalhop Cultuurfonds? Licht beide antwoorden toe met de definities.",
    model: `<ul>
<li><mark>Organisatie</mark>: een doelgericht samenwerkingsverband dat blijvend is.</li>
<li><mark>Bedrijf</mark>: een organisatie die goederen of diensten voortbrengt om die op een afzetmarkt te verkopen.</li>
<li><mark>Onderneming</mark>: een bedrijf dat gericht is op het maken van winst.</li></ul>
<p>Waalhop Groep is alle drie: een blijvend, doelgericht samenwerkingsverband dat bier en frisdrank verkoopt en winstgevend wil groeien.</p>
<p>Het Cultuurfonds is wel een organisatie (doelgericht en blijvend), maar geen bedrijf, want het verkoopt niets op een afzetmarkt. Het is ook geen onderneming, want het maakt geen winst.</p>`,
    rubric: [["De drie definities juist", 1], ["Waalhop: alle drie, met uitleg", 1], ["Cultuurfonds: wel organisatie, geen bedrijf en geen onderneming, met uitleg", 1]]
  },
  {
    id: "I3", topic: "inleiding", type: "open", pts: 3, model_naam: "Stromingen in de organisatiekunde",
    q: "Bij welke organisatiekundige stroming past de werkwijze in de bottelarij? Bij welke stroming passen de klachten van de operators? Wat was de kern van de kritiek van die tweede stroming op de eerste?",
    model: `<ul>
<li>De werkwijze past bij <mark>Scientific Management</mark> (1900–1935, Taylor, Ford): tijdstudies, normtijden, taakverdeling en standaardisatie, gericht op maximale efficiëntie.</li>
<li>De klachten passen bij de <mark>Human Relations-benadering</mark> (1935–1955): aandacht voor motivatie, samenwerking en sociale relaties.</li>
<li>Kritiek: Scientific Management benaderde mensen te mechanisch, als onderdeel van het proces. Het werk werd daardoor onaantrekkelijk en dat leidde tot demotivatie.</li></ul>`,
    rubric: [["Scientific Management met kenmerk uit de casus", 1], ["Human Relations-benadering herkend", 1], ["Kritiek: mens te mechanisch benaderd, demotivatie", 1]]
  },
  {
    id: "I4", topic: "inleiding", type: "open", pts: 4, model_naam: "7S-model van McKinsey",
    q: "Ramon zegt dat er naast de strategie niets hoeft te veranderen. Leg met het 7S-model uit waarom dit niet klopt. Noem twee andere S'en die door de nieuwe strategie veranderen en geef bij elke S een concreet voorbeeld voor Waalhop.",
    model: `<p>Volgens het <mark>7S-model</mark> hangen de zeven S'en (strategy, structure, systems, staff, style, skills en shared values) met elkaar samen. Verandert één S, dan heeft dat gevolgen voor de andere. Een organisatie presteert pas goed als de S'en op elkaar aansluiten.</p>
<p>Voorbeelden (twee zijn genoeg):</p>
<ul>
<li>Skills: Waalhop moet kennis opbouwen van het ontalcoholiseren van bier.</li>
<li>Systems: er is een nieuw productieproces en een nieuwe installatie nodig.</li>
<li>Staff: specialisten werven of brouwers omscholen.</li>
<li>Structure: een aparte afdeling of BU voor alcoholvrij bier.</li>
<li>Shared values: een brouwerscultuur waarin "echt bier alcohol heeft" moet veranderen.</li></ul>`,
    rubric: [["Uitleg dat de S'en samenhangen", 1], ["Gevolg: een verandering in één S raakt de andere S'en", 1], ["Eerste S met concreet voorbeeld", 1], ["Tweede S met concreet voorbeeld", 1]]
  },

  /* ---------------- STRATEGIE ---------------- */
  {
    id: "S1", topic: "strategie", type: "open", pts: 4, model_naam: "BCG-matrix",
    q: "Plaats de vier productgroepen in het BCG-model. Licht per productgroep toe op basis van marktgroei en relatief marktaandeel.",
    model: `<ul>
<li>Pils: <mark>cash cow</mark>. Lage marktgroei (1%), hoog relatief marktaandeel (1,8 &gt; 1).</li>
<li>Alcoholvrij bier: <mark>star</mark>. Hoge marktgroei (14%), hoog relatief marktaandeel (1,3).</li>
<li>Speciaalbier: <mark>question mark</mark>. Hoge marktgroei (11%), laag relatief marktaandeel (0,5).</li>
<li>Frisdrank: <mark>dog</mark>. Krimpende markt (−2%), laag relatief marktaandeel (0,4).</li></ul>
<p>Een relatief marktaandeel boven 1 betekent dat Waalhop groter is dan de grootste concurrent.</p>`,
    rubric: [["Pils: cash cow, met beide assen", 1], ["Alcoholvrij: star, met beide assen", 1], ["Speciaalbier: question mark, met beide assen", 1], ["Frisdrank: dog, met beide assen", 1]]
  },
  {
    id: "S2", topic: "strategie", type: "open", pts: 4, model_naam: "BCG-advies",
    q: "Geef per productgroep een advies: investeren, behouden (melken) of afstoten. Onderbouw elk advies.",
    model: `<ul>
<li>Alcoholvrij (star): <mark>investeren</mark> om de leidende positie in een snelgroeiende markt vast te houden. Later wordt het een cash cow.</li>
<li>Pils (cash cow): <mark>behouden en melken</mark>. Weinig investeren en de kasstroom gebruiken om alcoholvrij en speciaalbier te financieren.</li>
<li>Speciaalbier (question mark): <mark>selectief investeren</mark> als er een reële kans is om het marktaandeel te vergroten (bijvoorbeeld met de app), anders afstoten.</li>
<li>Frisdrank (dog): <mark>afstoten of afbouwen</mark>. Een nuance mag: de huismerkcontracten kunnen capaciteit benutten, maar kies uiteindelijk duidelijk.</li></ul>`,
    rubric: [["Alcoholvrij: investeren, onderbouwd", 1], ["Pils: behouden/melken, onderbouwd", 1], ["Speciaalbier: selectief investeren of afstoten, onderbouwd", 1], ["Frisdrank: afstoten/afbouwen, onderbouwd", 1]]
  },
  {
    id: "S3", topic: "strategie", type: "open", pts: 3, model_naam: "Strategische kloof",
    q: "Bereken de strategische kloof voor 2030 en leg uit wat dit begrip betekent. Wat moet Waalhop met deze uitkomst?",
    model: `<p>€ 210 miljoen − € 176 miljoen = <mark>€ 34 miljoen</mark>.</p>
<p>De <mark>strategische kloof</mark> is het verschil tussen de gewenste prestatie (de doelstelling) en de verwachte prestatie bij ongewijzigd beleid (de prognose).</p>
<p>Waalhop moet nieuw beleid ontwikkelen om de kloof te dichten, bijvoorbeeld met groeistrategieën van Ansoff.</p>
<p class="valkuil">Valkuil: de omzet van 2025 (€ 182 miljoen) heb je voor de berekening niet nodig.</p>`,
    rubric: [["Juiste berekening: € 34 miljoen", 1], ["Definitie: gewenst versus verwacht bij ongewijzigd beleid", 1], ["Gevolg: nieuwe strategie nodig om de kloof te dichten", 1]]
  },
  {
    id: "S4", topic: "strategie", type: "open", pts: 4, model_naam: "Groeistrategieën van Ansoff",
    q: "Benoem bij elk van de vier plannen de groeistrategie van Ansoff. Licht kort toe met de combinatie product–markt.",
    model: `<ol>
<li><mark>Marktontwikkeling</mark>: bestaand product (pils), nieuwe markt (Duitsland).</li>
<li><mark>Productontwikkeling</mark>: nieuw product (alcoholvrij IPA), bestaande markt.</li>
<li><mark>Diversificatie</mark>: nieuwe activiteit (horeca) op een nieuwe markt. Het gaat om gerelateerde diversificatie, verticaal voorwaarts in de bedrijfskolom.</li>
<li><mark>Marktpenetratie</mark>: bestaand product, bestaande markt, meer verkopen aan dezelfde klanten.</li></ol>`,
    rubric: [["Plan 1: marktontwikkeling", 1], ["Plan 2: productontwikkeling", 1], ["Plan 3: diversificatie", 1], ["Plan 4: marktpenetratie", 1]]
  },
  {
    id: "S5", topic: "strategie", type: "open", pts: 4, model_naam: "Porter en Treacy & Wiersema",
    q: "a. Welke concurrentiestrategie van Porter volgt De Linge?\nb. Welke waardestrategie van Treacy & Wiersema volgt Waalhop Dranken?\nOnderbouw beide antwoorden met de casus.",
    model: `<p>a. <mark>Focusstrategie</mark> (gericht op differentiatie): De Linge richt zich op een kleine doelgroep, namelijk liefhebbers en speciaalbiercafés. Ze onderscheidt zich door een unieke smaak en prijswinnende kwaliteit en vraagt daarvoor een hoge prijs.</p>
<p>b. <mark>Operational excellence</mark>: alle processen zijn gericht op de laagste kostprijs per liter en op foutloos en tijdig leveren.</p>`,
    rubric: [["a. Focusstrategie", 1], ["a. Onderbouwing: smalle doelgroep en onderscheidend", 1], ["b. Operational excellence", 1], ["b. Onderbouwing: lage kosten, efficiënte processen", 1]]
  },
  {
    id: "S6", topic: "strategie", type: "open", pts: 3, model_naam: "Marktposities van Kotler",
    q: "Welke marktpositie volgens Kotler heeft Waalhop in alcoholvrij bier? Noem twee strategieën die bij deze positie passen en werk elke strategie uit met een concrete maatregel voor Waalhop.",
    model: `<p>Waalhop is <mark>marktleider</mark>: de grootste van Nederland, met een relatief marktaandeel van 1,3.</p>
<ul>
<li><mark>Marktvergroting</mark>: een nieuwe doelgroep of toepassing zoeken, bijvoorbeeld alcoholvrij bier in sportkantines.</li>
<li><mark>Marktaandeel verdedigen</mark>: blijven innoveren en scherp prijzen tegenover de nieuwe ambachtelijke brouwers.</li>
<li><mark>Marktaandeel uitbreiden</mark>: nieuwe markten betreden of een kleine alcoholvrije brouwer overnemen.</li></ul>`,
    rubric: [["Marktleider, onderbouwd", 1], ["Eerste strategie met concrete maatregel", 1], ["Tweede strategie met concrete maatregel", 1]]
  },
  {
    id: "S7", topic: "strategie", type: "open", pts: 3, model_naam: "DESTEP (macro-omgeving)",
    q: "Noem drie ontwikkelingen uit de casus die bij de macro-omgeving horen. Geef per ontwikkeling de DESTEP-factor en geef aan of het voor Waalhop een kans of een bedreiging is.",
    model: `<ul>
<li>Hogere accijns op bier: <mark>politiek</mark> (ook economisch). Een bedreiging voor pils.</li>
<li>Jongeren drinken minder alcohol: <mark>sociaal-cultureel</mark> (of demografisch). Een kans voor alcoholvrij bier en een bedreiging voor pils.</li>
<li>Droge zomers maken gerst duurder: <mark>ecologisch</mark> (met economisch gevolg). Een bedreiging, want de kosten stijgen.</li></ul>
<p class="valkuil">Valkuil: nieuwe brouwerijen, de macht van supermarkten en kombucha horen bij de meso-omgeving (vijfkrachtenmodel). Daarvoor krijg je hier geen punt.</p>`,
    rubric: [["Eerste macro-ontwikkeling met factor en kans/bedreiging", 1], ["Tweede macro-ontwikkeling met factor en kans/bedreiging", 1], ["Derde macro-ontwikkeling met factor en kans/bedreiging", 1]]
  },
  {
    id: "S8", topic: "strategie", type: "open", pts: 3, model_naam: "Vijfkrachtenmodel van Porter",
    q: "Analyseer de meso-omgeving van Waalhop met het vijfkrachtenmodel van Porter. Benoem drie krachten met een voorbeeld uit de casus en geef aan welke kracht volgens jou het sterkst is.",
    model: `<ul>
<li><mark>Onderhandelingsmacht van afnemers</mark>: drie supermarktketens nemen 70% van de pils af en eisen lagere inkoopprijzen.</li>
<li><mark>Dreiging van nieuwe toetreders</mark>: elk jaar tientallen nieuwe ambachtelijke brouwerijen.</li>
<li><mark>Dreiging van substituten</mark>: kombucha en alcoholvrije mocktails.</li>
<li><mark>Onderhandelingsmacht van leveranciers</mark>: brouwgerst wordt duurder.</li></ul>
<p>De sterkste kracht is de macht van afnemers: Waalhop is voor 70% van de pilsafzet afhankelijk van drie klanten.</p>`,
    rubric: [["Twee krachten juist, met casusvoorbeeld", 1], ["Derde kracht juist, met casusvoorbeeld", 1], ["Sterkste kracht gekozen en onderbouwd", 1]]
  },
  {
    id: "S9", topic: "strategie", type: "open", pts: 2, model_naam: "Missie en visie",
    q: "Welke uitspraak (A of B) is de missie en welke de visie? Leg het verschil tussen beide begrippen uit.",
    model: `<p>A is de <mark>missie</mark>: waarom bestaat Waalhop? Het brede doel, de waarden en de plaats in de wereld.</p>
<p>B is de <mark>visie</mark>: een toekomstbeeld op lange termijn (2035) van waar Waalhop wil staan.</p>`,
    rubric: [["A = missie, B = visie", 1], ["Verschil juist uitgelegd", 1]]
  },
  {
    id: "S10", topic: "strategie", type: "open", pts: 2, model_naam: "Blauwe en rode oceaan",
    q: "Leg uit waarom de app van De Linge als een blauwe-oceaanstrategie gezien kan worden. Wat is het verschil met een rode oceaan?",
    model: `<p><mark>Blauwe oceaan</mark>: met innovatie een nieuwe markt creëren waar nog geen concurrentie is. Geen andere brouwer biedt bier op bestelling aan, dus concurrentie is (nog) niet relevant.</p>
<p><mark>Rode oceaan</mark>: concurreren in een bestaande markt, binnen dezelfde grenzen als de concurrenten (prijs, marketing). Volgens Kim &amp; Mauborgne is dat onvoldoende voor langdurig succes.</p>`,
    rubric: [["Blauwe oceaan uitgelegd en gekoppeld aan de app", 1], ["Rode oceaan juist uitgelegd", 1]]
  },

  /* ---------------- STRUCTURE ---------------- */
  {
    id: "ST1", topic: "structure", type: "open", pts: 4, model_naam: "Organogram, lijn en staf",
    q: "Beschrijf het organogram van Brouwerij Nijmegen: welke afdelingen staan in de lijn en welke zijn staf? Welk organisatiestelsel heeft Brouwerij Nijmegen, en welke bijzondere vorm van staf is het Kwaliteitslab? Tip: teken het organogram eerst op papier.",
    model: `<ul>
<li><mark>Lijn</mark>: directeur → afdelingshoofden Brouwen, Bottelen en Logistiek → ploegleiders → operators. Het primaire proces wordt in de lijn uitgevoerd.</li>
<li><mark>Staf</mark>: Planning, HRM, Financiën, Facility Management en Kwaliteitslab, getekend naast de lijn. Ze adviseren en ondersteunen, maar hebben geen zeggenschap.</li>
<li>Stelsel: <mark>lijn-staforganisatie</mark>.</li>
<li>Het Kwaliteitslab is <mark>functionele staf</mark>: op het eigen vakgebied (kwaliteit) mag het de lijn aansturen, bijvoorbeeld een bottellijn stilleggen.</li></ul>`,
    rubric: [["Lijnafdelingen juist", 1], ["Stafafdelingen juist", 1], ["Lijn-staforganisatie", 1], ["Kwaliteitslab = functionele staf, met uitleg", 1]]
  },
  {
    id: "ST2", topic: "structure", type: "open", pts: 4, model_naam: "Horizontale arbeidsverdeling (F/P/G/M)",
    q: "Op welk criterium zijn de BU's van Waalhop Groep ingedeeld, en op welk criterium de drie ploegen per bottellijn? Is er telkens sprake van horizontale specialisatie of van horizontale differentiatie? Licht toe.",
    model: `<ul>
<li>BU's: ingedeeld naar product (pils/alcoholvrij, speciaalbier, frisdrank). Dat is een <mark>P-indeling</mark>, dus <mark>horizontale specialisatie</mark>: elke BU voert alle functies uit voor een eigen product.</li>
<li>Ploegen: ingedeeld naar soort werkzaamheid (reinigen, vullen en doppen, etiketteren en verpakken). Dat is een <mark>F-indeling</mark>, dus <mark>horizontale differentiatie</mark>.</li></ul>`,
    rubric: [["BU's: P-indeling", 1], ["BU's: horizontale specialisatie", 1], ["Ploegen: F-indeling", 1], ["Ploegen: horizontale differentiatie", 1]]
  },
  {
    id: "ST3", topic: "structure", type: "open", pts: 3, model_naam: "Verticale arbeidsverdeling",
    q: "Wat is de span of control van Bas? Is de besluitvorming in Brouwerij Nijmegen gecentraliseerd of gedecentraliseerd? Gaat het bij deze begrippen om verticale of horizontale arbeidsverdeling? Onderbouw met de casus.",
    model: `<ul>
<li><mark>Span of control</mark> (spanwijdte) = 22: het aantal medewerkers dat rechtstreeks onder één leidinggevende valt.</li>
<li><mark>Gecentraliseerd</mark>: Joost neemt zelf alle beslissingen over volumes, investeringen en werktijden.</li>
<li>Beide begrippen horen bij <mark>verticale arbeidsverdeling</mark>: de verdeling van bevoegdheden en hiërarchie van boven naar beneden.</li></ul>`,
    rubric: [["Span of control = 22, met uitleg", 1], ["Gecentraliseerd, met onderbouwing", 1], ["Verticale arbeidsverdeling", 1]]
  },
  {
    id: "ST4", topic: "structure", type: "open", pts: 4, model_naam: "Werkstructurering",
    q: "Welke vorm van werkstructurering is maatregel 1 en welke maatregel 2? Leg uit wat beide vormen inhouden en wat het verschil is. Welk motief voor arbeidsverdeling ligt aan deze maatregelen ten grondslag?",
    model: `<ul>
<li>Maatregel 1: <mark>taakroulatie</mark>, waarbij medewerkers op vaste momenten van taak wisselen op hetzelfde niveau.</li>
<li>Maatregel 2: <mark>taakverrijking</mark>, waarbij taken van een hoger niveau worden toegevoegd: plannen, controleren en onderhoud. Dit gaat richting een (semi-)autonome taakgroep.</li>
<li>Verschil: roulatie en taakverbreding blijven op hetzelfde niveau (horizontaal); verrijking voegt regelende en controlerende taken toe (verticaal).</li>
<li>Motief: het <mark>gedragskundige (sociale) motief</mark>, zodat het werk aantrekkelijk blijft en medewerkers zich kunnen ontplooien en gemotiveerd blijven (Herzberg).</li></ul>`,
    rubric: [["Maatregel 1: taakroulatie, uitgelegd", 1], ["Maatregel 2: taakverrijking (niet taakverbreding), uitgelegd", 1], ["Verschil horizontaal/verticaal benoemd", 1], ["Gedragskundig/sociaal motief", 1]]
  },
  {
    id: "ST5", topic: "structure", type: "open", pts: 4, model_naam: "Configuraties van Mintzberg",
    q: "a. Welke configuratie van Mintzberg past bij Brouwerij Nijmegen? Noem het belangrijkste coördinatiemechanisme en het belangrijkste organisatiedeel.\nb. Welke configuratie past bij Waalhop Groep als geheel? Onderbouw.",
    model: `<p>a. <mark>Machinebureaucratie</mark>: routinematig werk, vaste procedures en centralisatie. Het coördinatiemechanisme is <mark>standaardisatie van werkprocessen</mark>. Het belangrijkste deel is de <mark>technostructuur</mark> (Planning), die het werk standaardiseert.</p>
<p>b. <mark>Gedivisionaliseerde organisatie</mark> (divisiestructuur): zelfstandige BU's met een eigen directie, die zelf bepalen wat en hoe ze produceren. De holding stuurt op output (omzet- en winstdoelen): standaardisatie van output. Het middenkader (de BU-directies) is het belangrijkste deel.</p>`,
    rubric: [["a. Machinebureaucratie, onderbouwd", 1], ["a. Standaardisatie van werkprocessen en technostructuur", 1], ["b. Gedivisionaliseerde organisatie", 1], ["b. Onderbouwing: autonome BU's, sturing op output", 1]]
  },

  /* ---------------- SYSTEMS ---------------- */
  {
    id: "SY1", topic: "systems", type: "open", pts: 4, model_naam: "ITO-model en feedback",
    q: "Beschrijf Brouwerij Nijmegen met het ITO-model: geef een voorbeeld van input, transformatie en output. Leg uit wat feedback is en geef een voorbeeld uit de casus.",
    model: `<ul>
<li><mark>Input</mark>: mout, hop, water, flessen, energie, personeel.</li>
<li><mark>Transformatie</mark>: brouwen, rijpen en bottelen.</li>
<li><mark>Output</mark>: kratten bier en fusten voor supermarkten en cafés (ook ongewenste output, zoals afvalwater).</li>
<li><mark>Feedback</mark>: informatie over de output die wordt teruggekoppeld naar de input of de transformatie, zodat het proces kan worden bijgestuurd. Voorbeeld: cafés melden troebel bier, waarna het filter in de bottelarij opnieuw wordt afgesteld.</li></ul>`,
    rubric: [["Input juist", 1], ["Transformatie juist", 1], ["Output juist", 1], ["Feedback uitgelegd met casusvoorbeeld", 1]]
  },
  {
    id: "SY2", topic: "systems", type: "open", pts: 4, model_naam: "Waardeketen van Porter",
    q: "Gebruik de waardeketen van Porter. Noem twee primaire en twee ondersteunende activiteiten uit de casus. Onder welke ondersteunende activiteit valt FM, en hoe beïnvloedt FM bij Brouwerij Nijmegen een primaire activiteit?",
    model: `<ul>
<li><mark>Primair</mark>: ingaande logistiek (lossen bij silo's en magazijn), operaties (brouwen, rijpen, bottelen), uitgaande logistiek (kratten leveren), marketing &amp; verkoop, service (klantenservice).</li>
<li><mark>Ondersteunend</mark>: inkoop, HRM, technologieontwikkeling (bijvoorbeeld ICT of het Kwaliteitslab), infrastructuur.</li>
<li>FM valt onder <mark>infrastructuur</mark> van de organisatie.</li>
<li>Invloed: als de koelinstallatie van de lagertanks uitvalt, moet een hele tank bier worden weggegooid. Dat raakt de operaties direct. FM is formeel ondersteunend, maar werkt in de praktijk als een "systeemversneller".</li></ul>`,
    rubric: [["Twee primaire activiteiten juist", 1], ["Twee ondersteunende activiteiten juist", 1], ["FM = infrastructuur", 1], ["Invloed van FM op een primaire activiteit, met voorbeeld", 1]]
  },
  {
    id: "SY3", topic: "systems", type: "open", pts: 3, model_naam: "Soorten processen",
    q: "Is het proces primair, secundair (ondersteunend) of besturend?\na. het brouwen van bier\nb. het onderhouden van de koelinstallatie\nc. het vaststellen van het jaarbudget en de strategische doelen\nZou je antwoord bij b anders zijn voor een installatiebedrijf dat koelinstallaties onderhoudt? Leg uit.",
    model: `<ul>
<li>a. <mark>Primair</mark>: draagt direct bij aan het product.</li>
<li>b. <mark>Secundair (ondersteunend)</mark>: maakt het primaire proces mogelijk.</li>
<li>c. <mark>Besturend</mark>: geeft richting, stuurt en controleert (planning &amp; control).</li>
<li>Bij een installatiebedrijf is onderhoud <mark>primair</mark>: dat is precies de dienst die het bedrijf levert. Of een proces primair is, hangt af van de organisatie.</li></ul>`,
    rubric: [["a en b juist", 1], ["c juist", 1], ["Installatiebedrijf: primair, met uitleg", 1]]
  },
  {
    id: "SY4", topic: "systems", type: "open", pts: 3, model_naam: "Subsysteem, aspectsysteem, open systeem",
    q: "Is een systeem met alleen de afdeling Logistiek een subsysteem of een aspectsysteem? En het overzicht van alle energie- en waterstromen dat FM maakt? Leg het verschil uit. Waarom is Brouwerij Nijmegen een open systeem?",
    model: `<ul>
<li>Logistiek: <mark>subsysteem</mark>, een deel van de elementen met al hun relaties.</li>
<li>Energie- en waterstromen: <mark>aspectsysteem</mark>, alle elementen maar slechts één soort relatie (één aspect).</li>
<li><mark>Open systeem</mark>: de brouwerij staat in wisselwerking met de omgeving. Ze haalt input bij leveranciers, levert output aan supermarkten en cafés, krijgt feedback van cafés en reageert op maatschappelijke eisen zoals minder waterverbruik.</li></ul>`,
    rubric: [["Logistiek = subsysteem, met uitleg", 1], ["Energiestromen = aspectsysteem, met uitleg", 1], ["Open systeem met casusvoorbeeld", 1]]
  },

  /* ---------------- STAFF & STYLE ---------------- */
  {
    id: "SS1", topic: "staffstyle", type: "open", pts: 4, model_naam: "IDU-model en de drie B's",
    q: "Deel de vier maatregelen van Esra in volgens het IDU-model (instroom, doorstroom, uitstroom). Geef bij elke maatregel ook aan op welke van de drie B's (binden, boeien, behouden) die vooral gericht is.",
    model: `<ul>
<li>€ 500 voor het aandragen van een collega: <mark>instroom</mark>, <mark>binden</mark> (medewerkers aantrekken).</li>
<li>Buddy en inwerkprogramma: <mark>instroom</mark> (onboarding), <mark>binden</mark> (eerste verbondenheid). "Behouden" is ook goed te verdedigen.</li>
<li>Ontwikkelgesprek en Brouwacademie: <mark>doorstroom</mark>, <mark>boeien</mark> (ontwikkelen en motiveren).</li>
<li>Exitgesprek: <mark>uitstroom</mark>, <mark>behouden</mark> (leren van vertrekredenen om verloop te voorkomen).</li></ul>`,
    rubric: [["Aandraagpremie: instroom + binden", 1], ["Buddy/inwerken: instroom + binden (of behouden)", 1], ["Ontwikkelgesprek/academie: doorstroom + boeien", 1], ["Exitgesprek: uitstroom + behouden", 1]]
  },
  {
    id: "SS2", topic: "staffstyle", type: "open", pts: 3, model_naam: "HRM-rollen van Ulrich",
    q: "Welke rol volgens het HRM-model van Ulrich vervult Esra nu, en naar welke rol wil de directie haar laten groeien? Noem een derde rol uit het model en geef een voorbeeld van hoe Esra die rol bij Waalhop kan invullen.",
    model: `<ul>
<li>Nu: <mark>administratief expert</mark> (salaris, contracten, verlof).</li>
<li>Gewenst: <mark>strategische partner</mark>, die meedenkt over de koers en de strategie helpt realiseren.</li>
<li>Derde rol, bijvoorbeeld <mark>change agent</mark> (de overstap naar alcoholvrij bier of naar zelfsturende ploegen begeleiden) of <mark>employee champion</mark> (opkomen voor het welzijn van medewerkers, zoals het hoge verzuim in de bottelarij aanpakken).</li></ul>`,
    rubric: [["Nu: administratief expert", 1], ["Gewenst: strategische partner", 1], ["Derde rol met concreet voorbeeld", 1]]
  },
  {
    id: "SS3", topic: "staffstyle", type: "open", pts: 3, model_naam: "Arbeidsvoorwaarden",
    q: "Deel de drie arbeidsvoorwaarden uit de casus in als primair, secundair of tertiair. Gebruik de indeling uit de les en licht toe.",
    model: `<ul>
<li>€ 2.950 bruto per maand: <mark>primair</mark> (basisloon).</li>
<li>Pensioen via de cao: <mark>secundair</mark> (voorziening die per onderneming of cao is vastgesteld).</li>
<li>Leaseauto voor accountmanagers: <mark>tertiair</mark> (voorziening voor een speciale categorie personeel, zoals "een auto van de zaak" in de les).</li></ul>
<p class="valkuil">Let op: sommige bronnen rekenen een leaseauto tot de secundaire arbeidsvoorwaarden. Volg op het tentamen de indeling van je docent en onderbouw je keuze.</p>`,
    rubric: [["Brutoloon: primair", 1], ["Pensioen via cao: secundair", 1], ["Leaseauto: tertiair, met uitleg", 1]]
  },
  {
    id: "SS4", topic: "staffstyle", type: "open", pts: 3, model_naam: "Theorie X en Y van McGregor",
    q: "Van welke theorie van McGregor gaat Joost uit? Geef een voorbeeld uit de casus en noem de klassieke leiderschapsstijl die daarbij past.",
    model: `<ul>
<li><mark>Theorie Y</mark>: een positief mensbeeld; medewerkers willen verantwoordelijkheid nemen en zijn van nature gemotiveerd en creatief.</li>
<li>Voorbeeld: Joost laat ploegen zelf doelen voorstellen en neemt besluiten samen met zijn afdelingshoofden.</li>
<li>Stijl: <mark>democratisch (participatief) leiderschap</mark>, met gezamenlijke besluitvorming.</li></ul>`,
    rubric: [["Theorie Y, met uitleg", 1], ["Casusvoorbeeld", 1], ["Democratische stijl", 1]]
  },
  {
    id: "SS5", topic: "staffstyle", type: "open", pts: 4, model_naam: "Situationeel leiderschap (Hersey & Blanchard)",
    q: "Welke stijl volgens Hersey & Blanchard past het best bij Lotte, en welke bij Henk? Onderbouw met het ontwikkelingsniveau (competentie en motivatie). Welke stijl gebruikt Bas nu bij Lotte, en waarom werkt die niet?",
    model: `<ul>
<li>Lotte: lage competentie, hoge motivatie. Daarbij past <mark>S1 instrueren</mark>: veel sturing, weinig ondersteuning.</li>
<li>Henk: hoge competentie, maar wisselende of lage motivatie. Daarbij past <mark>S3 ondersteunen</mark>: weinig sturing, veel ondersteuning en waardering.</li>
<li>Bas gebruikt bij Lotte nu <mark>S4 delegeren</mark>.</li>
<li>Dat werkt niet: delegeren past alleen bij een competente én gemotiveerde medewerker. Lotte kan de lijn nog niet bedienen, dus het risico op fouten en onzekerheid is groot.</li></ul>`,
    rubric: [["Lotte: S1, onderbouwd", 1], ["Henk: S3, onderbouwd", 1], ["Bas gebruikt nu S4", 1], ["Uitleg waarom S4 niet past", 1]]
  },
  {
    id: "SS6", topic: "staffstyle", type: "open", pts: 2, model_naam: "Managerial Grid (Blake & Mouton)",
    q: "Plaats Petra in de Managerial Grid van Blake & Mouton. Onderbouw met beide dimensies.",
    model: `<p><mark>9.1 Autoritair management</mark>: maximale aandacht voor productie en resultaat (levertijden, kilometers) en minimale aandacht voor mensen ("hoe ze zich voelen, is niet mijn probleem").</p>`,
    rubric: [["9.1 autoritair (taakgericht) management", 1], ["Onderbouwing met beide dimensies", 1]]
  },
  {
    id: "SS7", topic: "staffstyle", type: "open", pts: 3, model_naam: "Conflicthantering",
    q: "Welke stijl van conflicthantering gebruikt Joost bij het conflict over de kratten? Welke stijl raad je aan, en waarom? Gebruik de dimensies eigen belang en belang van de ander.",
    model: `<ul>
<li>Joost <mark>domineert (forceert)</mark>: veel nadruk op het eigen belang (zijn oplossing) en weinig op het belang van de ander. Logistiek moet zich zonder overleg aanpassen.</li>
<li>Advies: <mark>samenwerken</mark>, met veel aandacht voor het belang van beide afdelingen. Samen zoeken ze een win-winoplossing, bijvoorbeeld een buffervoorraad lege kratten. Dat is de meest effectieve en duurzame stijl.</li></ul>`,
    rubric: [["Domineren/forceren herkend", 1], ["Samenwerken geadviseerd", 1], ["Onderbouwing met beide dimensies en win-win", 1]]
  },
  {
    id: "SS8", topic: "staffstyle", type: "open", pts: 2, model_naam: "Behoeftepiramide van Maslow",
    q: "Op welk niveau van de behoeftepiramide van Maslow zit de behoefte van Lotte? Wat zegt de piramide over de volgorde waarin behoeften worden vervuld?",
    model: `<p>Lotte heeft een <mark>sociale behoefte</mark>: erbij horen.</p>
<p>Volgens Maslow vervullen mensen eerst de lagere behoeften (fysiologisch, veiligheid). Pas daarna richten ze zich op hogere behoeften (sociaal, waardering, zelfontplooiing).</p>`,
    rubric: [["Sociale behoefte", 1], ["Volgorde: eerst lagere, dan hogere behoeften", 1]]
  },

  /* ---------------- SKILLS & SHARED VALUES ---------------- */
  {
    id: "SV1", topic: "skillssv", type: "open", pts: 3, model_naam: "Skills (sleutelvaardigheden)",
    q: "Wat wordt in het 7S-model bedoeld met skills? Wat is de sleutelvaardigheid van De Linge, en waarom verschilt die van de sleutelvaardigheid die Waalhop Dranken nodig heeft?",
    model: `<ul>
<li><mark>Skills</mark>: de sleutelvaardigheden van de organisatie als geheel, niet die van één medewerker. Hiermee levert de organisatie toegevoegde waarde en onderscheidt ze zich.</li>
<li>De Linge: elk jaar nieuwe, prijswinnende recepten ontwikkelen in kleine series.</li>
<li>Waalhop Dranken heeft een andere strategie (operational excellence) en heeft dus andere skills nodig: efficiënt, goedkoop en foutloos produceren. De strategie bepaalt welke skills nodig zijn.</li></ul>`,
    rubric: [["Definitie: vaardigheid van de organisatie als geheel", 1], ["Sleutelvaardigheid De Linge", 1], ["Verschil gekoppeld aan de strategie", 1]]
  },
  {
    id: "SV2", topic: "skillssv", type: "open", pts: 3, model_naam: "Golden circle (Sinek) en toegevoegde waarde",
    q: "Het voorstel van Wouter sloeg niet aan. Herschrijf de kern van zijn voorstel volgens de golden circle van Sinek (waarom, hoe, wat). Leg uit waarom de volgorde belangrijk is.",
    model: `<ul>
<li><mark>Waarom</mark>: elke batch krijgt een constante kwaliteit, met minder afgekeurde batches en geen kapotte flessen meer. Dat sluit aan bij "Ambacht boven alles".</li>
<li><mark>Hoe</mark>: de temperatuur tijdens rijping en opslag nauwkeurig regelen.</li>
<li><mark>Wat</mark>: een koelcel van 40 m³ met digitale temperatuurregeling.</li></ul>
<p>Volgorde: communiceer van binnen naar buiten. Een opdrachtgever is vooral geïnteresseerd in het waarom, oftewel de toegevoegde waarde voor zijn doelen. Wouter begon met het wat, en daarop haakte Gijs af.</p>`,
    rubric: [["Waarom, gekoppeld aan een doel van De Linge", 1], ["Hoe en wat juist ingevuld", 1], ["Uitleg van de volgorde (van binnen naar buiten)", 1]]
  },
  {
    id: "SV3", topic: "skillssv", type: "open", pts: 4, model_naam: "Traditionele kwaliteitszorg en TQM",
    q: "Welke vorm van kwaliteitszorg past De Linge nu toe, en welke vorm wil Noor invoeren? Geef van beide vormen twee kenmerken die je in de casus terugziet.",
    model: `<ul>
<li>Nu: <mark>traditionele kwaliteitszorg</mark>. Er wordt achteraf gecontroleerd (aan het eind van de batch), een aparte afdeling (het lab) is verantwoordelijk, en slechte batches worden afgekeurd in plaats van voorkomen.</li>
<li>Noor: <mark>integrale kwaliteitszorg (TQM)</mark>. Kwaliteit is van iedereen, er wordt in elke stap gemeten (voorkomen), fouten worden geregistreerd en er wordt continu verbeterd.</li></ul>`,
    rubric: [["Nu: traditionele kwaliteitszorg", 1], ["Twee kenmerken van traditioneel uit de casus", 1], ["Noor: TQM/integrale kwaliteitszorg", 1], ["Twee kenmerken van TQM uit de casus", 1]]
  },
  {
    id: "SV4", topic: "skillssv", type: "open", pts: 4, model_naam: "PDCA-cyclus (Deming)",
    q: "Werk de PDCA-cyclus uit voor het koolzuurprobleem. Beschrijf per fase wat De Linge concreet doet.",
    model: `<ul>
<li><mark>Plan</mark>: de oorzaak analyseren (bijvoorbeeld te veel koolzuur bij de nagisting) en een SMART-doel stellen, zoals "binnen drie maanden geen enkele batch meer boven de koolzuurnorm". Het plan: koolzuur meten na elke stap.</li>
<li><mark>Do</mark>: het plan uitvoeren, eerst als pilot op één brouwlijn.</li>
<li><mark>Check</mark>: de resultaten meten en vergelijken met het doel.</li>
<li><mark>Act</mark>: werkt het, dan wordt de nieuwe werkwijze de standaard (werkinstructie). Werkt het niet, dan wordt het plan bijgesteld en begint de cyclus opnieuw.</li></ul>`,
    rubric: [["Plan concreet, met doel", 1], ["Do concreet", 1], ["Check concreet", 1], ["Act concreet: standaardiseren of bijsturen", 1]]
  },
  {
    id: "SV5", topic: "skillssv", type: "open", pts: 5, model_naam: "Balanced scorecard",
    q: "Noor wil de vier indicatoren gebruiken in een balanced scorecard. Plaats elke indicator in het juiste perspectief van de BSC en leg uit waarom een gebalanceerde set belangrijk is.",
    model: `<ol>
<li>Omzet uit speciaalbier: <mark>financieel perspectief</mark>.</li>
<li>Klanttevredenheid bij cafés: <mark>klantperspectief</mark>.</li>
<li>Percentage afgekeurde batches: <mark>intern (proces)perspectief</mark>.</li>
<li>Opleidingsuren per brouwer: <mark>innovatie- en leerperspectief</mark>.</li></ol>
<p>Gebalanceerd: een organisatie stuurt dan niet alleen op financiën, maar zowel intern als extern en op korte én lange termijn. Volgens onderzoek presteren organisaties met een evenwichtige set doelen op lange termijn beter. Zonder balans wordt innovatie vaak het onderschoven kindje.</p>`,
    rubric: [["Omzet: financieel", 1], ["Klanttevredenheid: klant", 1], ["Afgekeurde batches: interne processen", 1], ["Opleidingsuren: innovatie en leren", 1], ["Uitleg van het belang van balans", 1]]
  },
  {
    id: "SV6", topic: "skillssv", type: "open", pts: 3, model_naam: "Cultuurniveaus van Schein",
    q: "Geef bij elk van de drie cultuurniveaus van Schein een voorbeeld uit de casus.",
    model: `<ul>
<li><mark>Artefacten</mark> (zichtbaar): de zwarte schorten met het oude logo, de vrijdagse proeverij (ritueel), de muur met medailles.</li>
<li><mark>Beleden waarden</mark>: "Ambacht boven alles".</li>
<li><mark>Onderliggende basisveronderstellingen</mark> (onbewust, vanzelfsprekend): "machines verpesten het bier", waardoor automatiseren steeds wordt afgewezen.</li></ul>`,
    rubric: [["Artefact juist", 1], ["Beleden waarde juist", 1], ["Basisveronderstelling juist", 1]]
  },
  {
    id: "SV7", topic: "skillssv", type: "open", pts: 4, model_naam: "Cultuurtypen van Handy",
    q: "Welke cultuur volgens Handy heeft De Linge? Onderbouw met de twee dimensies van Handy. Met welke configuratie van Mintzberg gaat deze cultuur vaak samen?",
    model: `<ul>
<li><mark>Machtscultuur</mark>.</li>
<li><mark>Machtsspreiding laag</mark>: de macht ligt centraal bij Gijs, die alles bepaalt.</li>
<li><mark>Samenwerkingsgraad hoog</mark>: medewerkers werken graag samen, maar de top bepaalt waaraan.</li>
<li>Mintzberg: de <mark>ondernemersorganisatie</mark> (eenvoudige structuur), met directe supervisie vanuit de strategische top.</li></ul>
<p class="valkuil">Controleer in je reader hoe de assen van Handy getekend zijn. De conclusie "machtscultuur" staat vast door de centrale rol van de oprichter.</p>`,
    rubric: [["Machtscultuur", 1], ["Machtsspreiding laag, onderbouwd", 1], ["Samenwerkingsgraad hoog, onderbouwd", 1], ["Ondernemersorganisatie", 1]]
  },
  {
    id: "SV8", topic: "skillssv", type: "open", pts: 2, model_naam: "Cultuurdimensies van Hofstede",
    q: "Welke twee cultuurdimensies van Hofstede herken je bij de Poolse fabriek? Licht toe met de casus.",
    model: `<ul>
<li><mark>Grote machtsafstand</mark>: medewerkers verwachten duidelijke instructies en spreken hun baas niet snel tegen.</li>
<li><mark>Sterke onzekerheidsvermijding</mark>: medewerkers willen graag vaste regels en procedures.</li></ul>`,
    rubric: [["Machtsafstand, met casus", 1], ["Onzekerheidsvermijding, met casus", 1]]
  },
  {
    id: "SV9", topic: "skillssv", type: "open", pts: 2, model_naam: "INK-managementmodel",
    q: "Noor wil een zelfevaluatie doen met het INK-managementmodel. Uit welke soorten aandachtsgebieden bestaat het model, en wat verbindt ze?",
    model: `<ul>
<li>Vijf <mark>organisatiegebieden</mark> (wat de organisatie doet: leiderschap, strategie en beleid, management van medewerkers, middelen en processen) en vier <mark>resultaatgebieden</mark> (wat dat oplevert voor klanten, medewerkers, maatschappij en bestuur/financiers).</li>
<li>Het aandachtsgebied <mark>verbeteren en vernieuwen</mark> verbindt resultaten met de organisatie: leren en veranderen. Het model is integraal en "Rijnlands": het zoekt balans tussen alle belanghebbenden.</li></ul>`,
    rubric: [["Organisatiegebieden en resultaatgebieden", 1], ["Verbeteren en vernieuwen als verbindend gebied", 1]]
  },

  /* ---------------- RECHT (meerkeuze) ---------------- */
  {
    id: "R1", topic: "recht", type: "mc", pts: 1,
    casus: "Ruud Jansen exploiteert café Het Waalhuis als eenmanszaak. Het café heeft een schuld van € 80.000 bij Waalhop. Op de zakelijke rekening staat nog € 20.000.",
    q: "Wat kan Waalhop?",
    options: ["Alleen de € 20.000 van het café opeisen, want de eenmanszaak is zelf aansprakelijk.", "Het hele bedrag opeisen, want Ruud is met zijn gehele vermogen aansprakelijk, ook privé.", "Het hele bedrag opeisen, maar alleen als Ruud getrouwd is.", "Niets, want een eenmanszaak is een rechtspersoon."],
    correct: 1,
    uitleg: "Een eenmanszaak is geen rechtspersoon. De eigenaar is met zijn gehele vermogen, dus ook privé, aansprakelijk voor de schulden van de zaak. Gaat de eigenaar failliet, dan gaat ook de zaak failliet, en omgekeerd."
  },
  {
    id: "R2", topic: "recht", type: "mc", pts: 1,
    casus: "Ruud wil alleen de naam 'Het Waalhuis' verkopen aan een collega in Arnhem. Het café zelf houdt hij.",
    q: "Wat is juist?",
    options: ["Dat mag: een handelsnaam is vrij verhandelbaar.", "Dat mag niet: een handelsnaam kan alleen samen met de onderneming worden overgedragen (art. 2 Handelsnaamwet).", "Dat mag alleen nadat de naam bij de KvK als merk is geregistreerd.", "Dat mag, als de koper de naam binnen een jaar inschrijft."],
    correct: 1,
    uitleg: "Volgens art. 2 Hnw kan een handelsnaam alleen worden overgedragen samen met de onderneming die de naam voert. Een uitzondering is franchising (zoals Bakker Bart of Albert Heijn). Merken vallen onder het BVIE, niet onder de Handelsnaamwet."
  },
  {
    id: "R3", topic: "recht", type: "mc", pts: 1,
    casus: "Brouwerij De Linge heeft 85 werknemers. Directeur Gijs wil een bottellijn sluiten en het bottelen uitbesteden aan een ander bedrijf.",
    q: "Welk recht heeft de ondernemingsraad bij dit besluit?",
    options: ["Geen, want De Linge hoeft geen ondernemingsraad te hebben.", "Instemmingsrecht (art. 27 Wor).", "Adviesrecht (art. 25 Wor), want het gaat om een bedrijfsorganisatorisch besluit.", "Vetorecht op grond van de Wet op de economische delicten."],
    correct: 2,
    uitleg: "Vanaf 50 werknemers is een OR verplicht (getalscriterium). Bij bedrijfsorganisatorische en financieel-economische besluiten, zoals sluiting of uitbesteding, heeft de OR adviesrecht (art. 25 Wor). Dat advies is niet vrijblijvend."
  },
  {
    id: "R4", topic: "recht", type: "mc", pts: 1,
    casus: "De directie van De Linge wil een nieuwe regeling voor beoordelingsgesprekken invoeren.",
    q: "Welk recht heeft de ondernemingsraad hierbij?",
    options: ["Adviesrecht (art. 25 Wor).", "Instemmingsrecht (art. 27 Wor).", "Geen, personeelsbeleid is aan de directie.", "Alleen het recht om geïnformeerd te worden."],
    correct: 1,
    uitleg: "Regelingen op sociaal gebied, zoals een regeling voor personeelsbeoordeling, vallen onder het instemmingsrecht van art. 27 Wor. Zonder instemming van de OR kan de ondernemer zo'n regeling niet zomaar invoeren."
  },
  {
    id: "R5", topic: "recht", type: "mc", pts: 1,
    casus: "De Stichting Waalhop Cultuurfonds is op 1 maart bij de notaris opgericht, maar is nog niet ingeschreven in het handelsregister. Op 15 maart sluit het bestuur een contract met een podiumbouwer.",
    q: "Wat is juist?",
    options: ["De stichting bestaat nog niet, want inschrijving is een oprichtingseis.", "De stichting bestaat. Inschrijving is geen oprichtingseis, maar zolang de stichting niet is ingeschreven, zijn de bestuurders naast de stichting hoofdelijk aansprakelijk.", "De stichting bestaat en alleen de stichting is aansprakelijk.", "De stichting bestaat niet, want een stichting moet leden hebben."],
    correct: 1,
    uitleg: "Een stichting ontstaat door een notariële akte met statuten. Inschrijving in het handelsregister is geen oprichtingseis, maar wel verplicht: niet inschrijven is een economisch delict (WED), en zolang er niet is ingeschreven zijn alle bestuurders hoofdelijk aansprakelijk."
  },
  {
    id: "R6", topic: "recht", type: "mc", pts: 1,
    casus: "Twaalf liefhebbers richten mondeling de supportersclub 'Vrienden van De Linge' op. Er is geen notariële akte en de club staat niet ingeschreven in het handelsregister. De club heeft een openstaande rekening bij een drukkerij.",
    q: "Wie kan de drukkerij aanspreken?",
    options: ["Alleen de vereniging.", "De vereniging, en daarnaast alle bestuurders hoofdelijk.", "Alle twaalf leden, ieder voor een gelijk deel.", "Niemand, want een vereniging zonder notariële akte bestaat niet."],
    correct: 1,
    uitleg: "Een vereniging kan mondeling worden opgericht; dan is het een informele vereniging (zonder volledige rechtsbevoegdheid). Is die niet ingeschreven, dan is het hele bestuur hoofdelijk aansprakelijk naast de vereniging. Is ze wel ingeschreven, dan zijn bestuurders alleen aansprakelijk als de vereniging niet kan betalen."
  },
  {
    id: "R7", topic: "recht", type: "mc", pts: 1,
    casus: "Waalhop Dranken BV heeft twee bestuurders. In de statuten staat dat elke bestuurder zelfstandig bevoegd is tot € 25.000. Bestuurder Sem koopt in zijn eentje een etiketteermachine van € 40.000. Medebestuurder Lisa is het er niet mee eens.",
    q: "Wie moet de leverancier betalen?",
    options: ["De BV, voor het volledige bedrag: een grensbedrag in de statuten beperkt de vertegenwoordigingsbevoegdheid niet tegenover derden.", "Sem persoonlijk, voor het volledige bedrag.", "De BV tot € 25.000 en Sem voor het restant.", "Niemand: de koop is ongeldig."],
    correct: 0,
    uitleg: "Bij de NV en BV is elke bestuurder in beginsel individueel bevoegd. Dat kan in de statuten alleen worden beperkt met een twee- of meerhandtekeningenclausule, niet met een grensbedrag. Tegenover de leverancier is de BV dus gebonden. Intern kan de BV Sem wel aanspreken, bijvoorbeeld wegens onbehoorlijk bestuur."
  },
  {
    id: "R8", topic: "recht", type: "mc", pts: 1,
    casus: "Marloes tekent namens 'Waalhop Horeca BV i.o.' een huurcontract voor een pand. Twee maanden later wordt de BV opgericht, maar de BV bekrachtigt het huurcontract niet.",
    q: "Wie is aansprakelijk voor de huur?",
    options: ["De BV.", "Marloes, als handelend bestuurder.", "Waalhop Groep, als moedermaatschappij.", "De notaris die de BV heeft opgericht."],
    correct: 1,
    uitleg: "Wie handelt namens een BV in oprichting (i.o.), is zelf aansprakelijk. Na de oprichting kan de BV de handeling bekrachtigen; dan wordt de BV gebonden. Hier gebeurt dat niet, dus blijft Marloes als handelend bestuurder aansprakelijk."
  },
  {
    id: "R9", topic: "recht", type: "mc", pts: 1,
    casus: "Waalhop Groep wil geld ophalen door aandelen via de beurs te verkopen.",
    q: "Welke rechtsvorm past hierbij, en welk startkapitaal is volgens de les verplicht?",
    options: ["BV, zonder minimumkapitaal.", "NV, met een startkapitaal van € 45.000.", "Stichting, met een startkapitaal van € 45.000.", "Coöperatie, zonder minimumkapitaal."],
    correct: 1,
    uitleg: "De NV heeft een openbaar karakter: aandelen zijn vrij verhandelbaar, onder meer via de beurs. Er geldt meer dwingend recht en een startkapitaal van € 45.000. De BV heeft een besloten karakter, vaak met een blokkeringsregeling, en geen startkapitaal."
  },
  {
    id: "R10", topic: "recht", type: "mc", pts: 1,
    casus: "Het Cultuurfonds (een stichting) houdt dit jaar € 30.000 over.",
    q: "Wat mag het bestuur met dit geld doen?",
    options: ["Het als bonus aan de twee bestuurders uitkeren.", "Het teruggeven aan Waalhop Groep als oprichter.", "Het schenken aan een muziekschool voor kinderen in Nijmegen.", "Het verdelen onder de leden van de stichting."],
    correct: 2,
    uitleg: "Voor een stichting geldt een uitkeringsverbod: geen uitkeringen aan oprichters of bestuurders, en geen winstuitkeringen. Uitkeringen met een sociale of ideële strekking mogen wel. Een stichting heeft bovendien geen leden."
  }
];
