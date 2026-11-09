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
    titel: "Casus 1 · Over Heidezoom",
    html: `
<p><strong>Heidezoom Groep</strong> (fictief) is een vakantiebedrijf uit Apeldoorn. In 1968 begonnen Hendrik en Gerda Mulder een kleine camping op hun boerderij op de Veluwe. Nu werken er 910 vaste medewerkers en in de zomer nog eens 300 seizoenskrachten. Samen verhuren, schoonmaken en onderhouden ze bungalows, hotelkamers en tenten, en verzorgen ze activiteiten voor gasten. Heidezoom wil winst maken, maar ook over dertig jaar nog een gezond familiebedrijf zijn. Daarom koopt het dit jaar voor € 8 miljoen grond voor een nieuw park.</p>
<p>In Apeldoorn staat ook <strong>zwembad De Plons</strong>. Het zwembad is van de gemeente, verkoopt kaartjes en abonnementen aan bezoekers en vraagt precies zoveel entree dat de kosten gedekt zijn. Winst maken is niet de bedoeling. Daarnaast bestaat de <strong>Stichting Heidezoom Natuurfonds</strong>. Het fonds krijgt elk jaar een gift van Heidezoom en betaalt daarmee heideherstel en nestkasten. Het verkoopt niets.</p>
<p><strong>Housekeeping.</strong> Sinds 2010 werkt de schoonmaak in de parken met normtijden: een bungalow moet in 75 minuten wisselklaar zijn. Een teamleider meet met een app hoe lang elke schoonmaker per bungalow doet, en wie sneller is dan de norm krijgt een bonus per bungalow. Het werk is opgeknipt: de ene schoonmaker doet alleen badkamers, de ander alleen keukens, een derde alleen bedden. Vorig jaar was het verzuim 11%.</p>
<p>De nieuwe parkmanager in Ermelo deed een proef. Ze dronk elke ochtend koffie met de schoonmakers, vroeg naar hun ideeën en hing hun namen op bij de best beoordeelde bungalows. Binnen een maand ging de productiviteit omhoog en daalde het verzuim, terwijl de werkwijze verder hetzelfde bleef.</p>
<p>Algemeen directeur Peter Mulder wil een reorganisatie: "We maken een nieuw organogram met minder managers. Daarmee zijn we er."</p>`
  },
  strategie: {
    titel: "Casus 2 · Heidezoom op weg naar 2030",
    html: `
<p>Heidezoom Groep bestaat uit drie business units (BU's): <strong>Heidezoom Parken</strong> (zes bungalowparken), <strong>Heidezoom Hotels &amp; Congres</strong> (twee hotels met congrescentrum en wellness) en <strong>Heidezoom Glamping</strong> (luxe tenten en boomhutten, in 2021 overgenomen van oprichter Sanne de Wit).</p>
<p><strong>Drie uitspraken uit het jaarverslag.</strong><br>(A) "Wij geven gezinnen de ruimte om samen tot rust te komen in de natuur."<br>(B) "In 2032 is Heidezoom het meest gastvrije en natuurinclusieve vakantiebedrijf van Nederland."<br>(C) "Daarom investeren we de komende vijf jaar vooral in wellness en glamping en bouwen we het congreswerk af."</p>
<div class="tablewrap"><table>
<thead><tr><th>Productgroep</th><th>Marktgroei per jaar</th><th>Relatief marktaandeel*</th></tr></thead>
<tbody>
<tr><td>Bungalowvakanties</td><td>1%</td><td>1,6</td></tr>
<tr><td>Wellnessarrangementen</td><td>13%</td><td>1,2</td></tr>
<tr><td>Glamping</td><td>19%</td><td>0,4</td></tr>
<tr><td>Zakelijke congressen</td><td>−4%</td><td>0,6</td></tr>
</tbody></table></div>
<p class="footnote">* Eigen marktaandeel gedeeld door het marktaandeel van de grootste concurrent.</p>
<p><strong>Cijfers.</strong> In 2025 was de omzet € 128 miljoen. De familie als aandeelhouder wil in 2030 een omzet van € 150 miljoen. Bij ongewijzigd beleid verwacht Financiën voor 2030 € 133 miljoen.</p>
<p><strong>Plannen.</strong> Het managementteam bespreekt vier plannen:</p>
<ol>
<li>Met een spaarprogramma vaste gasten vaker per jaar laten boeken.</li>
<li>Een bouwbedrijf overnemen dat chalets en tiny houses maakt.</li>
<li>Voor de huidige gasten nieuwe arrangementen ontwikkelen, zoals e-bike-tochten met een boswachter en kookworkshops.</li>
<li>De bestaande bungalowvakanties via een Duitse website en Duitse reisbureaus verkopen aan Duitse gezinnen.</li>
</ol>
<p><strong>De drie BU's.</strong> Heidezoom Parken heeft zes vrijwel identieke bungalowtypes, koopt alles centraal in, laat gasten zelf inchecken met een code en is gemiddeld 15% goedkoper dan andere parken. Het richt zich op alle gezinnen in Nederland. Hotels &amp; Congres heeft een vaste groep zakelijke klanten; elke klant heeft een eigen accountmanager die elk congres volledig op maat maakt en de wensen van de klant al kent voordat die ze uitspreekt. Heidezoom Glamping brengt elk jaar als eerste een nieuw concept op de markt, zoals zwevende tenten en boomhutten met glazen dak.</p>
<p><strong>Concurrentie.</strong> In glamping is Glampr (fictief) de grootste, met een marktaandeel dat 2,5 keer zo groot is als dat van Heidezoom. Heidezoom Glamping valt Glampr openlijk aan met lagere prijzen en de campagne "Waarom meer betalen?". In het congreswerk volgt Hotels &amp; Congres de prijzen van de grote congrescentra en neemt het nieuwe arrangementen pas over als die bij anderen succesvol blijken.</p>
<p><strong>Omgeving.</strong> Nederland vergrijst en 55-plussers gaan vaker buiten de schoolvakanties op vakantie. Gemeenten op de Veluwe verhogen de toeristenbelasting. Door de stikstofregels mag Heidezoom op de Veluwe nauwelijks nog bijbouwen. Veel bedrijven vergaderen sinds de coronajaren online. Boekingsplatforms als Booking.com leveren 40% van de boekingen en vragen 18% commissie. Particulieren verhuren steeds vaker een tiny house in hun tuin via Airbnb. Vliegvakanties naar Zuid-Europa worden goedkoper.</p>
<p><strong>Twee ideeën.</strong> Hotels &amp; Congres wil, net als alle concurrenten, een subtropisch zwembad met glijbanen bouwen. Heidezoom Glamping wil een "stiltepark" openen: geen auto's, geen wifi, en gasten helpen een dagdeel mee met natuurbeheer. Geen enkel ander park biedt zoiets aan.</p>`
  },
  structure: {
    titel: "Casus 3 · Heidezoom Parken",
    html: `
<p>Heidezoom Parken is de grootste BU. Directeur is Ilse Brouwer. Onder haar staan zes parkmanagers, één per park: Epe, Ermelo, Nunspeet, Ede, Rheden en Hoog Soeren. Elk park heeft drie afdelingen: <strong>Receptie &amp; Recreatie</strong>, <strong>Housekeeping</strong> en <strong>Technische Dienst</strong>.</p>
<p>Op het hoofdkantoor zitten Marketing, HR, Financiën, Inkoop en de Reserveringscentrale. Zij ondersteunen en adviseren Ilse en de parkmanagers, maar geven geen opdrachten aan de parken. Eén uitzondering: de veiligheidscoördinator mag zelf een zwembad sluiten als de waterkwaliteit niet in orde is.</p>
<p><strong>Bevoegdheden.</strong> De parkmanagers beslissen zelf over de inzet van personeel, lokale activiteiten en uitgaven tot € 50.000. Alleen grote investeringen gaan naar Ilse.</p>
<p><strong>Housekeeping Ermelo.</strong> Teamleider Monique de Groot geeft leiding aan 34 schoonmakers. Zoals in casus 1 beschreven, doet nu elke schoonmaker maar één deel van de bungalow (badkamer, keuken of bedden). HR stelt twee maatregelen voor:</p>
<ol>
<li>Elke schoonmaker maakt voortaan een hele bungalow schoon: badkamer, keuken én bedden.</li>
<li>Vaste teams van vijf schoonmakers krijgen een eigen deel van het park. Het team maakt zelf de dagplanning, controleert zelf de kwaliteit en bestelt zelf schoonmaakmiddelen.</li>
</ol>
<p><strong>Hotels &amp; Congres.</strong> De afdeling Verkoop van Hotels &amp; Congres heeft drie teams: één voor particulieren, één voor bedrijven en één voor scholen en verenigingen. In het wellnesscentrum werken fysiotherapeuten, masseurs en huidtherapeuten. Zij werken zelfstandig volgens hun beroepsopleiding en de regels van hun beroepsvereniging; de manager bemoeit zich nauwelijks met hoe ze hun werk doen.</p>
<p><strong>Heidezoom Glamping</strong> heeft 40 medewerkers. Oprichter Sanne de Wit is nog steeds directeur. Er zijn nauwelijks regels of functieomschrijvingen: Sanne loopt elke dag rond en zegt iedereen wat er moet gebeuren.</p>`
  },
  systems: {
    titel: "Casus 4 · Een week in park Ermelo",
    html: `
<p>Een gast boekt online via de Reserveringscentrale en krijgt een code waarmee hij op vrijdag zelf incheckt. Tijdens het verblijf organiseert Recreatie activiteiten en is het zwembad open. Op maandag of vrijdag vertrekt de gast. Daarna maakt Housekeeping de bungalow schoon en verhelpt de Technische Dienst kleine gebreken. Schoon linnen komt van een externe wasserij; Inkoop regelt het contract. Afval wordt gescheiden opgehaald.</p>
<p><strong>Ondersteuning.</strong> HR, ICT, Financiën en de afdeling Facilitair Beheer (onder leiding van Daan Kuipers) ondersteunen de parken. Facilitair Beheer regelt onder meer energie, het wagenpark, de inkoop van schoonmaakmiddelen en het onderhoud van het hoofdkantoor. De salarisadministratie gebeurt op het hoofdkantoor.</p>
<p><strong>Reviews.</strong> Na hun verblijf geven gasten een cijfer voor onder meer de schoonmaak. Het gemiddelde cijfer voor schoonmaak daalde dit voorjaar van 8,4 naar 7,6. In de reviews klaagden gasten vooral over stof onder de bedden. Housekeeping heeft daarop de checklist aangepast.</p>
<p><strong>Besturing.</strong> Elk najaar stellen Ilse en de parkmanagers het jaarplan en het budget voor het volgende jaar vast.</p>
<p><strong>Energie.</strong> Facilitair Beheer heeft een dashboard laten bouwen dat van alle gebouwen, bungalows en installaties in het park alleen het energieverbruik laat zien. Ook maakt Daan een apart overzicht van de Technische Dienst: alle medewerkers, voertuigen en werkplaatsen, en hoe die samenwerken.</p>`
  },
  staffstyle: {
    titel: "Casus 5 · Werken bij Heidezoom",
    html: `
<p>Elk voorjaar heeft Heidezoom 300 seizoenskrachten nodig. HR-manager Fatima El Idrissi heeft vier maatregelen genomen:</p>
<ul>
<li>Een open dag voor mbo-studenten van toerisme en facilitaire dienstverlening.</li>
<li>Een leerlijn waarmee een schoonmaker in achttien maanden teamleider kan worden.</li>
<li>Begeleiding naar ander werk (outplacement) voor de medewerkers van het congrescentrum dat wordt gesloten.</li>
<li>Een bonus van € 750 voor seizoenskrachten die het hele seizoen blijven.</li>
</ul>
<p><strong>De rol van HR.</strong> Fatima leidt een HR-jaarplan af van de strategie: welke vaardigheden heeft Heidezoom in 2030 nodig voor wellness en glamping? Ook begeleidt ze de overgang naar zelfsturende schoonmaakteams, met workshops voor teamleiders en gesprekken met medewerkers die het niet zien zitten. De salarisadministratie en de contracten zijn sinds dit jaar uitbesteed aan een salarisbureau.</p>
<p><strong>Tevredenheid.</strong> In het medewerkersonderzoek klagen schoonmakers over het lage salaris, de krappe huisvesting voor seizoenskrachten en de oude schoonmaakkarren. Wat ze het meest waarderen, zijn complimenten van gasten en de keren dat ze zelf iets mochten beslissen.</p>
<p><strong>Leiderschap.</strong> Parkmanager Frank Wolters in Nunspeet gaat ervan uit dat medewerkers het minimale doen als niemand oplet. Hij heeft een prikklok ingevoerd, controleert elke dag zelf de bungalows en neemt alle beslissingen zelf, zonder overleg. Parkmanager Ellen Smit in Ede zorgt vooral dat iedereen het naar zijn zin heeft: elke week taart, veel uitjes en nooit een kritisch woord. De planning loopt bij haar vaak uit en de reviewcijfers dalen.</p>
<p><strong>Twee medewerkers.</strong> Teamleider Monique heeft er een halfjaar <strong>Yara</strong> bij. Yara kan al veel, maar maakt nog fouten en heeft na een zwaar seizoen haar enthousiasme verloren. <strong>Mehmet</strong> werkt er twaalf jaar, kent het werk door en door en komt zelf met verbeteringen. Monique vertelt Mehmet toch elke ochtend precies wat hij moet doen en hoe.</p>
<p><strong>Conflict.</strong> De parken Ede en Rheden delen één technisch team en ruziën over wie het team wanneer krijgt. Ilse besluit: elk park krijgt het team precies 2,5 dag per week.</p>
<p><strong>Twee seizoenskrachten.</strong> <strong>Kasia</strong> woont tijdelijk in een woonunit op het park. Haar contract loopt over zes weken af en ze weet niet waar ze daarna kan wonen. <strong>Gerrit</strong> heeft een vast contract en een eigen huis. Hij wil vooral nieuwe dingen leren en de leerlijn naar teamleider volgen.</p>`
  },
  skillssv: {
    titel: "Casus 6 · Kwaliteit en cultuur",
    html: `
<p><strong>Sleutelvaardigheid.</strong> Heidezoom Parken staat in de branche bekend om één ding: op zaterdag maakt het in vier uur 300 bungalows wisselklaar, zonder dat er een gast hoeft te wachten. Geen ander bedrijf haalt dat tempo.</p>
<p><strong>Cultuur in de parken.</strong> Alle medewerkers dragen een paars poloshirt met een heidetakje. Elke maandag om acht uur is er een briefing waarin de parkmanager de week doorneemt. Bij de receptie hangt een bord: "De gast komt altijd eerst". Voor elke functie is er een functieomschrijving en voor bijna elke taak een werkinstructie. Wie iets anders wil, moet een formulier invullen. Onder vaste medewerkers is het een ongeschreven waarheid dat seizoenskrachten toch weer weggaan, dus dat het geen zin heeft om ze goed in te werken.</p>
<p><strong>Heidezoom Lab.</strong> Voor nieuwe concepten werkt Heidezoom met projectteams van specialisten uit verschillende afdelingen. Per project stelt het team zelf de aanpak vast; wie de meeste kennis heeft, heeft het meeste te zeggen. Na het project gaat het team weer uit elkaar.</p>
<p><strong>Kwaliteit.</strong> Nu controleert een inspecteur na de schoonmaak één op de tien bungalows met een checklist. Is een bungalow niet goed, dan moet het team terug. Kwaliteitsmanager Ruben Hoekstra wil dat elke schoonmaker zelf zijn werk controleert, dat fouten worden geregistreerd en dat de teams elke week één verbetering bespreken. Om het schoonmaakcijfer weer omhoog te krijgen (zie casus 4) heeft hij deze acties gepland, maar nog niet in de goede volgorde:</p>
<ul>
<li>Na zes weken met een steekproef van 40 bungalows en de reviews kijken of het cijfer verbetert.</li>
<li>De nieuwe checklist en de stofzuigerroute worden de standaard in alle zes parken.</li>
<li>Doel vaststellen: binnen drie maanden is het gemiddelde schoonmaakcijfer weer minimaal 8,3.</li>
<li>De nieuwe checklist en een vaste stofzuigerroute vier weken uitproberen in park Ermelo.</li>
</ul>
<p><strong>Indicatoren.</strong> Ruben stelt voor het MT zes indicatoren op: (1) omzet per bungalow, (2) gemiddeld reviewcijfer van gasten, (3) gemiddelde schoontijd per bungalow, (4) percentage bungalows dat bij inspectie wordt afgekeurd, (5) winst per BU, (6) aantal nieuwe concepten van Heidezoom Lab per jaar.</p>
<p><strong>Facilitair Beheer.</strong> Daan Kuipers wil in alle bungalows sensoren plaatsen. Zijn voorstel aan het MT begint zo: "We installeren 1.200 sensoren van type Y die temperatuur, CO₂ en gebruik meten en koppelen die aan ons FMIS." Het MT stelde de beslissing uit.</p>
<p><strong>Denemarken.</strong> Heidezoom neemt een vakantiepark aan de Deense kust over. De Nederlandse parkmanager merkt dat Deense medewerkers hun leidinggevende gewoon met de voornaam aanspreken en het direct zeggen als ze het oneens zijn. Ze vinden een goede balans tussen werk en privé belangrijker dan carrière maken en zorgen goed voor elkaar.</p>
<p><strong>INK.</strong> Ruben wil verbeteracties ordenen met het INK-managementmodel. Op zijn lijst staan onder meer: een training coachend leidinggeven voor alle teamleiders, een nieuw reserveringssysteem, en een onderzoek naar wat de gemeente en omwonenden van de parken vinden.</p>`
  },
  recht: {
    titel: "Ondernemingsrecht · meerkeuze",
    html: `
<p>Net als bij de Waalhop-toets wordt ondernemingsrecht getoetst met <strong>meerkeuzevragen</strong>, en je mag de wettenbundel gebruiken. Elke vraag heeft een eigen korte casus uit de wereld van Heidezoom.</p>
<p>Stof volgens de dia's: les 1 (algemene aspecten en de eenmanszaak) en les 2 (vereniging, nv, bv en stichting).</p>`
  }
};

/* Open vragen: rubric = [beoordelingspunt, punten] */
const QUESTIONS = [
  /* ---------------- INLEIDING ---------------- */
  {
    id: "I1", topic: "inleiding", type: "open", pts: 3, model_naam: "Organisatie, bedrijf, onderneming",
    q: "Is zwembad De Plons een organisatie, een bedrijf of een onderneming? En de Stichting Heidezoom Natuurfonds? Licht beide antwoorden toe met de definities, en geef aan wat het verschil met Heidezoom Groep is.",
    model: `<ul>
<li><mark>Organisatie</mark>: een doelgericht samenwerkingsverband dat blijvend is.</li>
<li><mark>Bedrijf</mark>: een organisatie die goederen of diensten voortbrengt om die op een afzetmarkt te verkopen.</li>
<li><mark>Onderneming</mark>: een bedrijf dat gericht is op het maken van winst.</li></ul>
<p>De Plons is een organisatie én een bedrijf: het verkoopt kaartjes en abonnementen op een afzetmarkt. Het is geen onderneming, want het streeft geen winst na (alleen kostendekkend).</p>
<p>Het Natuurfonds is alleen een organisatie: doelgericht en blijvend, maar het verkoopt niets en maakt geen winst.</p>
<p>Heidezoom Groep is alle drie, want het verkoopt vakanties en wil winst maken.</p>`,
    rubric: [["De drie definities juist", 1], ["De Plons: bedrijf, geen onderneming, met uitleg", 1], ["Natuurfonds: alleen organisatie, en Heidezoom wel onderneming", 1]]
  },
  {
    id: "I2", topic: "inleiding", type: "open", pts: 4, model_naam: "Scientific Management en Human Relations",
    q: "Bij welke stroming in de organisatiekunde past de manier waarop housekeeping sinds 2010 werkt? Noem twee kenmerken uit de casus. Bij welke stroming past de proef van de parkmanager in Ermelo, en welk bekend onderzoek liet hetzelfde effect zien?",
    model: `<ul>
<li>Housekeeping past bij <mark>Scientific Management</mark> (Taylor): normtijden, tijdmeting per bungalow, ver doorgevoerde taakverdeling (alleen badkamers, alleen keukens) en een bonus per bungalow (prestatieloon).</li>
<li>De proef past bij de <mark>Human Relations-benadering</mark>: aandacht voor mensen, sociale contacten en erkenning verhogen de motivatie en productiviteit, ook als de werkwijze hetzelfde blijft.</li>
<li>Bekend onderzoek: de <mark>Hawthorne-experimenten</mark> (Mayo). Alleen al de aandacht voor de arbeiders verhoogde de productiviteit.</li></ul>`,
    rubric: [["Scientific Management", 1], ["Twee kenmerken uit de casus", 1], ["Human Relations-benadering", 1], ["Hawthorne-onderzoek (Mayo) met het effect van aandacht", 1]]
  },
  {
    id: "I3", topic: "inleiding", type: "open", pts: 4, model_naam: "7S-model: harde en zachte S'en",
    q: "Peter wil alleen een nieuw organogram. Leg met het 7S-model uit waarom dat niet genoeg is. Welke S'en zijn de harde en welke de zachte S'en? Geef twee zachte S'en die door de reorganisatie geraakt worden, met een voorbeeld voor Heidezoom.",
    model: `<p>Volgens het <mark>7S-model</mark> hangen alle zeven S'en samen. Een nieuw organogram verandert de structure, maar als de andere S'en niet meebewegen, sluit de organisatie niet meer op elkaar aan en presteert ze slechter.</p>
<ul>
<li><mark>Harde S'en</mark>: strategy, structure en systems. Die zijn relatief makkelijk te beschrijven en te veranderen.</li>
<li><mark>Zachte S'en</mark>: staff, style, skills en shared values. Die gaan over mensen en cultuur en veranderen langzaam.</li></ul>
<p>Voorbeelden (twee zijn genoeg):</p>
<ul>
<li>Style: met minder managers moeten leidinggevenden meer coachen en minder controleren.</li>
<li>Staff: teamleiders hebben andere vaardigheden nodig en er is begeleiding nodig voor wie zijn functie verliest.</li>
<li>Shared values: de gewoonte om alles aan de manager te vragen moet plaatsmaken voor eigen verantwoordelijkheid.</li>
<li>Skills: de organisatie moet leren werken met grotere teams en minder controle.</li></ul>`,
    rubric: [["Uitleg dat de S'en samenhangen, dus structuur alleen is niet genoeg", 1], ["Harde en zachte S'en juist ingedeeld", 1], ["Eerste zachte S met concreet voorbeeld", 1], ["Tweede zachte S met concreet voorbeeld", 1]]
  },

  /* ---------------- STRATEGIE ---------------- */
  {
    id: "S1", topic: "strategie", type: "open", pts: 4, model_naam: "BCG-matrix",
    q: "Plaats de vier productgroepen in het BCG-model. Licht per productgroep toe op basis van marktgroei en relatief marktaandeel.",
    model: `<ul>
<li>Bungalowvakanties: <mark>cash cow</mark>. Lage marktgroei (1%), hoog relatief marktaandeel (1,6 &gt; 1).</li>
<li>Wellnessarrangementen: <mark>star</mark>. Hoge marktgroei (13%), hoog relatief marktaandeel (1,2).</li>
<li>Glamping: <mark>question mark</mark>. Hoge marktgroei (19%), laag relatief marktaandeel (0,4).</li>
<li>Zakelijke congressen: <mark>dog</mark>. Krimpende markt (−4%), laag relatief marktaandeel (0,6).</li></ul>
<p>Noem bij twijfel welke grens je voor hoge groei hanteert; dat levert punten op.</p>`,
    rubric: [["Bungalowvakanties: cash cow, met beide assen", 1], ["Wellness: star, met beide assen", 1], ["Glamping: question mark, met beide assen", 1], ["Congressen: dog, met beide assen", 1]]
  },
  {
    id: "S2", topic: "strategie", type: "open", pts: 3, model_naam: "BCG: kasstromen en portfolio",
    q: "Welke productgroep moet volgens het BCG-model het geld opleveren, en waar moet dat geld naartoe? Past uitspraak C uit het jaarverslag bij het BCG-advies? Licht toe.",
    model: `<ul>
<li>De <mark>cash cow</mark> (bungalowvakanties) levert veel geld op en vraagt weinig investering. Die kasstroom gaat naar de <mark>star</mark> (wellness), om de leidende positie vast te houden, en naar de <mark>question mark</mark> (glamping), om het marktaandeel te vergroten.</li>
<li>Uitspraak C past hierbij: investeren in wellness (star) en glamping (question mark) en het congreswerk (dog) afbouwen.</li>
<li>Kanttekening voor een sterk antwoord: bij glamping is investeren alleen zinvol als Heidezoom een reële kans heeft om het aandeel te vergroten. Anders is het geld weggegooid.</li></ul>`,
    rubric: [["Cash cow levert de kasstroom", 1], ["Geld naar star en question mark, met reden", 1], ["Uitspraak C past: investeren in star/question mark, dog afbouwen", 1]]
  },
  {
    id: "S3", topic: "strategie", type: "open", pts: 3, model_naam: "Strategische kloof",
    q: "Bereken de strategische kloof voor 2030. Welke van de vier groeistrategieën van Ansoff is het meest riskant om de kloof te dichten, en waarom?",
    model: `<p>€ 150 miljoen − € 133 miljoen = <mark>€ 17 miljoen</mark>. Dat is het verschil tussen de gewenste prestatie (doelstelling) en de verwachte prestatie bij ongewijzigd beleid.</p>
<p>Het meest riskant is <mark>diversificatie</mark>: een nieuw product op een nieuwe markt. Heidezoom heeft dan geen ervaring met het product én niet met de klanten. Marktpenetratie is het minst riskant.</p>
<p class="valkuil">Valkuil: de omzet van 2025 (€ 128 miljoen) heb je voor de kloof niet nodig.</p>`,
    rubric: [["Juiste berekening: € 17 miljoen", 1], ["Diversificatie als meest riskant", 1], ["Uitleg: nieuw product én nieuwe markt, dus geen ervaring", 1]]
  },
  {
    id: "S4", topic: "strategie", type: "open", pts: 4, model_naam: "Groeistrategieën van Ansoff",
    q: "Benoem bij elk van de vier plannen de groeistrategie van Ansoff. Licht kort toe met de combinatie product–markt.",
    model: `<ol>
<li><mark>Marktpenetratie</mark>: bestaand product, bestaande markt; dezelfde gasten vaker laten boeken.</li>
<li><mark>Diversificatie</mark>: een nieuwe activiteit (bouwen) voor een nieuwe markt. Het is gerelateerde diversificatie, verticaal achterwaarts in de bedrijfskolom.</li>
<li><mark>Productontwikkeling</mark>: nieuwe arrangementen voor de bestaande gasten.</li>
<li><mark>Marktontwikkeling</mark>: bestaand product (bungalowvakanties) op een nieuwe markt (Duitse gezinnen).</li></ol>`,
    rubric: [["Plan 1: marktpenetratie", 1], ["Plan 2: diversificatie", 1], ["Plan 3: productontwikkeling", 1], ["Plan 4: marktontwikkeling", 1]]
  },
  {
    id: "S5", topic: "strategie", type: "open", pts: 4, model_naam: "Porter en Treacy & Wiersema",
    q: "a. Welke concurrentiestrategie van Porter volgt Heidezoom Parken?\nb. Welke waardestrategie van Treacy & Wiersema volgt Hotels & Congres, en welke Heidezoom Glamping?\nOnderbouw met de casus.",
    model: `<p>a. <mark>Kostenleiderschap</mark>: een breed publiek (alle gezinnen), gestandaardiseerde bungalows, centrale inkoop en zelf inchecken, waardoor Heidezoom Parken goedkoper kan zijn dan de concurrent.</p>
<p>b. Hotels &amp; Congres: <mark>customer intimacy</mark> (klantpartnerschap). Een eigen accountmanager per klant, maatwerk en de klant goed kennen.</p>
<p>Glamping: <mark>product leadership</mark>. Elk jaar als eerste een nieuw, innovatief concept.</p>`,
    rubric: [["a. Kostenleiderschap", 1], ["a. Onderbouwing: breed publiek en lage kosten door standaardisatie", 1], ["b. Hotels & Congres: customer intimacy, onderbouwd", 1], ["b. Glamping: product leadership, onderbouwd", 1]]
  },
  {
    id: "S6", topic: "strategie", type: "open", pts: 3, model_naam: "Marktposities van Kotler",
    q: "Welke marktpositie volgens Kotler heeft Heidezoom Glamping, en welke heeft Hotels & Congres in de congresmarkt? Onderbouw beide. Noem één risico van de strategie van Heidezoom Glamping.",
    model: `<ul>
<li>Glamping: <mark>marktuitdager</mark>. Niet de grootste, maar valt de marktleider openlijk aan om marktaandeel te winnen (lagere prijzen, campagne).</li>
<li>Hotels &amp; Congres: <mark>marktvolger</mark>. Volgt de prijzen en neemt arrangementen pas over als ze elders succesvol zijn; geen aanval op de leider.</li>
<li>Risico: de leider is groter en kan terugslaan, bijvoorbeeld met een prijzenoorlog die de kleinere uitdager meer pijn doet. Lage prijzen passen bovendien slecht bij een product-leadershipstrategie.</li></ul>`,
    rubric: [["Glamping: marktuitdager, onderbouwd", 1], ["Hotels & Congres: marktvolger, onderbouwd", 1], ["Een reëel risico van de aanval", 1]]
  },
  {
    id: "S7", topic: "strategie", type: "open", pts: 3, model_naam: "DESTEP (macro-omgeving)",
    q: "Noem drie ontwikkelingen uit de casus die bij de macro-omgeving horen. Geef per ontwikkeling de DESTEP-factor en geef aan of het voor Heidezoom een kans of een bedreiging is.",
    model: `<ul>
<li>Vergrijzing en 55-plussers buiten de schoolvakanties: <mark>demografisch</mark>. Een kans, bijvoorbeeld voor wellness en het voor- en naseizoen.</li>
<li>Hogere toeristenbelasting: <mark>politiek</mark> (met economisch gevolg). Een bedreiging, want de prijs voor gasten stijgt.</li>
<li>Stikstofregels: <mark>ecologisch</mark> (en politiek). Een bedreiging, want uitbreiden op de Veluwe kan nauwelijks.</li>
<li>Online vergaderen: <mark>sociaal-cultureel</mark> of <mark>technologisch</mark>. Een bedreiging voor het congreswerk.</li></ul>
<p class="valkuil">Valkuil: Booking.com, Airbnb-verhuurders, goedkope vliegvakanties en Glampr horen bij de meso-omgeving (vijfkrachtenmodel). Daarvoor krijg je hier geen punt.</p>`,
    rubric: [["Eerste macro-ontwikkeling met factor en kans/bedreiging", 1], ["Tweede macro-ontwikkeling met factor en kans/bedreiging", 1], ["Derde macro-ontwikkeling met factor en kans/bedreiging", 1]]
  },
  {
    id: "S8", topic: "strategie", type: "open", pts: 3, model_naam: "Vijfkrachtenmodel van Porter",
    q: "Analyseer de meso-omgeving van Heidezoom Parken met het vijfkrachtenmodel van Porter. Benoem drie krachten met een voorbeeld uit de casus en geef aan welke kracht volgens jou het sterkst is.",
    model: `<ul>
<li><mark>Onderhandelingsmacht van afnemers</mark> (via tussenpersonen): boekingsplatforms leveren 40% van de boekingen en dwingen 18% commissie af.</li>
<li><mark>Dreiging van nieuwe toetreders</mark>: particulieren die een tiny house verhuren via Airbnb.</li>
<li><mark>Dreiging van substituten</mark>: goedkopere vliegvakanties naar Zuid-Europa vervullen dezelfde behoefte.</li>
<li><mark>Concurrentie tussen bestaande aanbieders</mark>: andere parken op de Veluwe.</li></ul>
<p>Sterkste kracht, bijvoorbeeld de boekingsplatforms: Heidezoom is voor 40% van de boekingen van hen afhankelijk en kan de commissie nauwelijks beïnvloeden. Een andere keuze mag, als je die onderbouwt.</p>`,
    rubric: [["Twee krachten juist, met casusvoorbeeld", 1], ["Derde kracht juist, met casusvoorbeeld", 1], ["Sterkste kracht gekozen en onderbouwd", 1]]
  },
  {
    id: "S9", topic: "strategie", type: "open", pts: 3, model_naam: "Missie, visie en strategie",
    q: "Welke uitspraak (A, B of C) is de missie, welke de visie en welke de strategie? Leg het verschil tussen visie en strategie uit.",
    model: `<ul>
<li>A is de <mark>missie</mark>: waarom Heidezoom bestaat en wat het voor gasten wil betekenen.</li>
<li>B is de <mark>visie</mark>: het toekomstbeeld, waar Heidezoom in 2032 wil staan.</li>
<li>C is de <mark>strategie</mark>: de weg en de keuzes om daar te komen (investeren in wellness en glamping, congreswerk afbouwen).</li></ul>
<p>Verschil: de visie zegt wáár je naartoe wilt; de strategie zegt hóé je daar komt.</p>`,
    rubric: [["A, B en C juist benoemd", 2], ["Verschil visie en strategie uitgelegd", 1]]
  },
  {
    id: "S10", topic: "strategie", type: "open", pts: 2, model_naam: "Blauwe en rode oceaan",
    q: "Welk van de twee ideeën is een rode-oceaanstrategie en welk een blauwe-oceaanstrategie? Leg uit waarom een rode oceaan volgens Kim & Mauborgne op lange termijn onvoldoende is.",
    model: `<ul>
<li>Het subtropisch zwembad: <mark>rode oceaan</mark>. Hotels &amp; Congres doet hetzelfde als alle concurrenten en concurreert binnen de bestaande markt.</li>
<li>Het stiltepark: <mark>blauwe oceaan</mark>. Met een nieuw concept ontstaat een markt waarin nog geen concurrentie is.</li>
<li>In een rode oceaan vechten aanbieders om dezelfde klanten, met prijs en marketing. Dat drukt de marges en levert geen blijvend voordeel op.</li></ul>`,
    rubric: [["Zwembad rood en stiltepark blauw, met uitleg", 1], ["Waarom rode oceaan op lange termijn onvoldoende is", 1]]
  },

  /* ---------------- STRUCTURE ---------------- */
  {
    id: "ST1", topic: "structure", type: "open", pts: 4, model_naam: "Organogram, lijn en staf",
    q: "Beschrijf het organogram van Heidezoom Parken: wat staat in de lijn en wat is staf? Welk organisatiestelsel is dit, en welke bijzondere vorm van staf is de veiligheidscoördinator? Tip: teken het organogram eerst op papier.",
    model: `<ul>
<li><mark>Lijn</mark>: directeur Ilse → zes parkmanagers → per park de afdelingen Receptie &amp; Recreatie, Housekeeping en Technische Dienst → teamleiders en medewerkers.</li>
<li><mark>Staf</mark>: Marketing, HR, Financiën, Inkoop en de Reserveringscentrale, naast de lijn getekend. Ze adviseren en ondersteunen, maar geven geen opdrachten.</li>
<li>Stelsel: <mark>lijn-staforganisatie</mark>.</li>
<li>De veiligheidscoördinator is <mark>functionele staf</mark>: op zijn eigen vakgebied (veiligheid) mag hij de lijn iets opdragen, namelijk een zwembad sluiten.</li></ul>`,
    rubric: [["Lijn juist", 1], ["Staf juist", 1], ["Lijn-staforganisatie", 1], ["Veiligheidscoördinator = functionele staf, met uitleg", 1]]
  },
  {
    id: "ST2", topic: "structure", type: "open", pts: 3, model_naam: "Horizontale arbeidsverdeling (F/P/G/M)",
    q: "Op welk criterium (F, P, G of M) is de indeling gemaakt:\na. onder Ilse, in zes parken;\nb. binnen elk park, in drie afdelingen;\nc. bij Verkoop van Hotels & Congres, in drie teams?\nGeef bij elk aan of het horizontale specialisatie of horizontale differentiatie is.",
    model: `<ul>
<li>a. <mark>G-indeling</mark> (geografisch, per gebied/park): <mark>horizontale specialisatie</mark>.</li>
<li>b. <mark>F-indeling</mark> (naar soort werkzaamheid): <mark>horizontale differentiatie</mark>.</li>
<li>c. <mark>M-indeling</mark> (naar marktgroep: particulieren, bedrijven, scholen en verenigingen): <mark>horizontale specialisatie</mark>.</li></ul>
<p>Bij een P-, G- of M-indeling doet elke eenheid alle soorten werk voor een eigen product, gebied of klantgroep (specialisatie). Bij een F-indeling is het werk naar soort verdeeld (differentiatie).</p>`,
    rubric: [["a. G-indeling, specialisatie", 1], ["b. F-indeling, differentiatie", 1], ["c. M-indeling, specialisatie", 1]]
  },
  {
    id: "ST3", topic: "structure", type: "open", pts: 3, model_naam: "Verticale arbeidsverdeling",
    q: "Wat is de span of control van Monique? Is de besluitvorming bij Heidezoom Parken gecentraliseerd of gedecentraliseerd? Wat is een nadeel van een grote span of control in de housekeeping?",
    model: `<ul>
<li><mark>Span of control</mark> = 34: het aantal medewerkers dat rechtstreeks onder één leidinggevende valt.</li>
<li><mark>Gedecentraliseerd</mark>: parkmanagers beslissen zelf over personeel, activiteiten en uitgaven tot € 50.000; alleen grote investeringen gaan naar Ilse.</li>
<li>Nadeel: Monique heeft weinig tijd per medewerker voor begeleiding, controle en feedback. Dat kan alleen werken als het werk eenvoudig en gestandaardiseerd is, of als teams zelf veel regelen.</li></ul>`,
    rubric: [["Span of control = 34, met uitleg", 1], ["Gedecentraliseerd, onderbouwd", 1], ["Reëel nadeel van een grote span", 1]]
  },
  {
    id: "ST4", topic: "structure", type: "open", pts: 4, model_naam: "Werkstructurering",
    q: "Welke vorm van werkstructurering is maatregel 1, en welke maatregel 2? Leg het verschil uit. Welk motief voor arbeidsverdeling zat achter de oude werkwijze, en welk motief zit achter de nieuwe maatregelen?",
    model: `<ul>
<li>Maatregel 1: <mark>taakverbreding</mark>. Er komen taken van hetzelfde niveau bij (horizontaal): de hele bungalow in plaats van één onderdeel.</li>
<li>Maatregel 2: <mark>autonome (zelfsturende) taakgroep</mark>, een vorm van <mark>taakverrijking</mark>. Het team krijgt regelende en controlerende taken erbij: planning, kwaliteitscontrole en bestellen (verticaal).</li>
<li>Oude werkwijze: het <mark>economische motief</mark>, dus efficiëntie door specialisatie, korte inleertijd en snel werken.</li>
<li>Nieuwe maatregelen: het <mark>gedragskundige (sociale) motief</mark>: afwisseling, verantwoordelijkheid en motivatie, met minder verzuim.</li></ul>`,
    rubric: [["Maatregel 1: taakverbreding", 1], ["Maatregel 2: autonome taakgroep/taakverrijking", 1], ["Verschil horizontaal en verticaal uitgelegd", 1], ["Economisch motief oud, gedragskundig motief nieuw", 1]]
  },
  {
    id: "ST5", topic: "structure", type: "open", pts: 4, model_naam: "Configuraties van Mintzberg",
    q: "a. Welke configuratie van Mintzberg past bij Heidezoom Glamping? Noem het coördinatiemechanisme en het belangrijkste organisatiedeel.\nb. Welke configuratie past bij het wellnesscentrum? Noem ook hier het coördinatiemechanisme en het belangrijkste organisatiedeel.",
    model: `<p>a. <mark>Ondernemersorganisatie</mark> (eenvoudige structuur): een kleine organisatie zonder veel regels, waarin de oprichter alles zelf aanstuurt. Coördinatie via <mark>directe supervisie</mark>; het belangrijkste deel is de <mark>strategische top</mark>.</p>
<p>b. <mark>Professionele organisatie</mark> (professionele bureaucratie): goed opgeleide professionals werken zelfstandig volgens hun opleiding en beroepsregels. Coördinatie via <mark>standaardisatie van vaardigheden</mark>; het belangrijkste deel is de <mark>uitvoerende (operationele) kern</mark>.</p>`,
    rubric: [["a. Ondernemersorganisatie", 1], ["a. Directe supervisie en strategische top", 1], ["b. Professionele organisatie", 1], ["b. Standaardisatie van vaardigheden en uitvoerende kern", 1]]
  },

  /* ---------------- SYSTEMS ---------------- */
  {
    id: "SY1", topic: "systems", type: "open", pts: 4, model_naam: "ITO-model en feedback",
    q: "Beschrijf de afdeling Housekeeping van park Ermelo met het ITO-model: geef input, transformatie en output. Leg uit wat feedback is en geef een voorbeeld uit de casus.",
    model: `<ul>
<li><mark>Input</mark>: vuile bungalows na vertrek, schone was van de wasserij, schoonmaakmiddelen, schoonmakers en hun uren.</li>
<li><mark>Transformatie</mark>: schoonmaken, bedden opmaken en de bungalow wisselklaar maken.</li>
<li><mark>Output</mark>: schone, wisselklare bungalows (en ongewenste output, zoals vuile was en afval).</li>
<li><mark>Feedback</mark>: informatie over de output die wordt teruggekoppeld, zodat het proces kan worden bijgestuurd. Voorbeeld: gasten klagen in reviews over stof onder de bedden, waarna de checklist wordt aangepast.</li></ul>`,
    rubric: [["Input juist", 1], ["Transformatie juist", 1], ["Output juist", 1], ["Feedback uitgelegd met casusvoorbeeld", 1]]
  },
  {
    id: "SY2", topic: "systems", type: "open", pts: 4, model_naam: "Waardeketen van Porter",
    q: "Gebruik de waardeketen van Porter voor park Ermelo. Noem twee primaire en twee ondersteunende activiteiten uit de casus. Onder welke ondersteunende activiteit valt Facilitair Beheer? Is Housekeeping bij een vakantiepark primair of ondersteunend? Beargumenteer.",
    model: `<ul>
<li><mark>Primair</mark>: marketing en verkoop (online boeken via de Reserveringscentrale), operaties (het verblijf en de activiteiten van Recreatie), service (vragen en klachten van gasten). Ingaande logistiek, zoals het linnen dat binnenkomt, mag ook.</li>
<li><mark>Ondersteunend</mark>: inkoop (contract met de wasserij), HRM, technologieontwikkeling (ICT, het reserveringssysteem), infrastructuur.</li>
<li>Facilitair Beheer valt onder <mark>infrastructuur</mark> van de organisatie.</li>
<li>Housekeeping: bij een vakantiepark is een schone bungalow een deel van het product dat de gast koopt. Daarom is het goed te verdedigen als <mark>primair</mark> (operaties). Wie het als ondersteunend ziet, moet uitleggen waarom; de onderbouwing telt.</li></ul>`,
    rubric: [["Twee primaire activiteiten juist", 1], ["Twee ondersteunende activiteiten juist", 1], ["Facilitair Beheer = infrastructuur", 1], ["Housekeeping beargumenteerd vanuit het product van de gast", 1]]
  },
  {
    id: "SY3", topic: "systems", type: "open", pts: 3, model_naam: "Soorten processen",
    q: "Is het proces primair, secundair (ondersteunend) of besturend?\na. het verhuren van bungalows en het inchecken van gasten\nb. de salarisadministratie\nc. het vaststellen van het jaarplan en het budget\nZou je antwoord bij b anders zijn voor het salarisbureau waaraan Heidezoom de salarisadministratie heeft uitbesteed? Leg uit.",
    model: `<ul>
<li>a. <mark>Primair</mark>: draagt direct bij aan de dienst die Heidezoom verkoopt.</li>
<li>b. <mark>Secundair (ondersteunend)</mark>: maakt het primaire proces mogelijk.</li>
<li>c. <mark>Besturend</mark>: geeft richting en stuurt (planning &amp; control).</li>
<li>Voor het salarisbureau is salarisadministratie <mark>primair</mark>: dat is precies de dienst die het verkoopt. Of een proces primair is, hangt af van de organisatie.</li></ul>`,
    rubric: [["a en b juist", 1], ["c juist", 1], ["Salarisbureau: primair, met uitleg", 1]]
  },
  {
    id: "SY4", topic: "systems", type: "open", pts: 3, model_naam: "Subsysteem, aspectsysteem, open systeem",
    q: "Is het energiedashboard van Daan een subsysteem of een aspectsysteem? En zijn overzicht van de Technische Dienst? Leg het verschil uit. Waarom is park Ermelo een open systeem?",
    model: `<ul>
<li>Energiedashboard: <mark>aspectsysteem</mark>. Alle elementen (gebouwen, bungalows, installaties), maar slechts één soort relatie: energie.</li>
<li>Technische Dienst: <mark>subsysteem</mark>. Een deel van de elementen, met al hun onderlinge relaties.</li>
<li><mark>Open systeem</mark>: het park staat in wisselwerking met de omgeving. Gasten komen en gaan, linnen komt van de wasserij, afval wordt opgehaald en reviews van gasten sturen het werk bij.</li></ul>`,
    rubric: [["Dashboard = aspectsysteem, met uitleg", 1], ["Technische Dienst = subsysteem, met uitleg", 1], ["Open systeem met casusvoorbeeld", 1]]
  },

  /* ---------------- STAFF & STYLE ---------------- */
  {
    id: "SS1", topic: "staffstyle", type: "open", pts: 4, model_naam: "IDU-model en de drie B's",
    q: "Deel de eerste drie maatregelen van Fatima in volgens het IDU-model (instroom, doorstroom, uitstroom). Op welke van de drie B's (binden, boeien, behouden) is de seizoensbonus gericht? Leg uit.",
    model: `<ul>
<li>Open dag voor mbo-studenten: <mark>instroom</mark>.</li>
<li>Leerlijn van schoonmaker naar teamleider: <mark>doorstroom</mark>.</li>
<li>Outplacement bij sluiting van het congrescentrum: <mark>uitstroom</mark>.</li>
<li>Seizoensbonus: <mark>behouden</mark>. De bonus is bedoeld om medewerkers die er al zijn, tot het eind van het seizoen vast te houden.</li></ul>`,
    rubric: [["Open dag: instroom", 1], ["Leerlijn: doorstroom", 1], ["Outplacement: uitstroom", 1], ["Bonus: behouden, met uitleg", 1]]
  },
  {
    id: "SS2", topic: "staffstyle", type: "open", pts: 3, model_naam: "HRM-rollen van Ulrich",
    q: "Welke twee rollen uit het HRM-model van Ulrich vervult Fatima in de alinea 'De rol van HR'? Welke rol heeft Heidezoom grotendeels uitbesteed?",
    model: `<ul>
<li>Het HR-jaarplan afleiden van de strategie: <mark>strategische partner</mark>.</li>
<li>De overgang naar zelfsturende teams begeleiden, met aandacht voor weerstand: <mark>change agent</mark>.</li>
<li>Uitbesteed: een groot deel van de rol <mark>administratief expert</mark> (salarisadministratie en contracten).</li></ul>`,
    rubric: [["Strategische partner, met casus", 1], ["Change agent, met casus", 1], ["Administratief expert uitbesteed", 1]]
  },
  {
    id: "SS3", topic: "staffstyle", type: "open", pts: 2, model_naam: "Personeelsbeleid en personeelsbeheer",
    q: "Leg het verschil uit tussen personeelsbeleid en personeelsbeheer. Geef van beide een voorbeeld uit de casus.",
    model: `<ul>
<li><mark>Personeelsbeleid</mark>: de keuzes voor de lange termijn over personeel, afgeleid van de doelen en de strategie. Voorbeeld: het HR-jaarplan met de vaardigheden die nodig zijn voor wellness en glamping, of de leerlijn naar teamleider.</li>
<li><mark>Personeelsbeheer</mark>: de uitvoering en administratie rond personeel. Voorbeeld: salarisadministratie en contracten.</li></ul>`,
    rubric: [["Verschil juist uitgelegd", 1], ["Van beide een passend casusvoorbeeld", 1]]
  },
  {
    id: "SS4", topic: "staffstyle", type: "open", pts: 3, model_naam: "Tweefactorentheorie van Herzberg",
    q: "Deel de klachten en de waardering uit het medewerkersonderzoek in volgens de tweefactorentheorie van Herzberg. Wat bereikt Heidezoom als het alleen het salaris verhoogt?",
    model: `<ul>
<li><mark>Hygiënefactoren</mark> (dissatisfiers): salaris, huisvesting en de oude schoonmaakkarren (werkomstandigheden).</li>
<li><mark>Motivatoren</mark> (satisfiers): erkenning (complimenten van gasten) en verantwoordelijkheid (zelf beslissen).</li>
<li>Alleen het salaris verhogen haalt ontevredenheid weg, maar maakt medewerkers niet gemotiveerd. Voor motivatie zijn motivatoren nodig, zoals de zelfsturende teams.</li></ul>`,
    rubric: [["Hygiënefactoren juist", 1], ["Motivatoren juist", 1], ["Gevolg: minder ontevreden, niet meer gemotiveerd", 1]]
  },
  {
    id: "SS5", topic: "staffstyle", type: "open", pts: 3, model_naam: "Theorie X en Y van McGregor",
    q: "Van welke theorie van McGregor gaat Frank uit? Geef twee voorbeelden uit de casus en noem de klassieke leiderschapsstijl die erbij past.",
    model: `<ul>
<li><mark>Theorie X</mark>: een negatief mensbeeld; medewerkers zijn lui, vermijden verantwoordelijkheid en moeten gecontroleerd worden.</li>
<li>Voorbeelden: de prikklok, dagelijkse controle van de bungalows, alle beslissingen zelf nemen.</li>
<li>Stijl: <mark>autoritair (autocratisch) leiderschap</mark>.</li></ul>`,
    rubric: [["Theorie X, met uitleg", 1], ["Twee casusvoorbeelden", 1], ["Autoritaire stijl", 1]]
  },
  {
    id: "SS6", topic: "staffstyle", type: "open", pts: 4, model_naam: "Situationeel leiderschap (Hersey & Blanchard)",
    q: "Welke stijl volgens Hersey & Blanchard past het best bij Yara, en welke bij Mehmet? Onderbouw met competentie en motivatie. Welke stijl gebruikt Monique nu bij Mehmet, en wat is daarvan het gevolg?",
    model: `<ul>
<li>Yara: enige competentie, lage motivatie. Daarbij past <mark>S2 begeleiden</mark> (coachen): veel sturing én veel ondersteuning.</li>
<li>Mehmet: hoge competentie en hoge motivatie. Daarbij past <mark>S4 delegeren</mark>: weinig sturing en weinig ondersteuning; hij krijgt de verantwoordelijkheid.</li>
<li>Monique gebruikt bij Mehmet <mark>S1 instrueren</mark>.</li>
<li>Gevolg: Mehmet voelt zich niet serieus genomen en kan zijn motivatie verliezen; zijn kennis en verbeterideeën blijven onbenut.</li></ul>`,
    rubric: [["Yara: S2, onderbouwd", 1], ["Mehmet: S4, onderbouwd", 1], ["Monique gebruikt nu S1", 1], ["Gevolg van de verkeerde stijl", 1]]
  },
  {
    id: "SS7", topic: "staffstyle", type: "open", pts: 2, model_naam: "Managerial Grid (Blake & Mouton)",
    q: "Plaats Ellen in de Managerial Grid van Blake & Mouton. Onderbouw met beide dimensies. Welke stijl is volgens het model het meest effectief?",
    model: `<p>Ellen: <mark>1.9 country club management</mark>. Veel aandacht voor mensen (taart, uitjes, sfeer) en weinig aandacht voor productie en resultaat (planning loopt uit, cijfers dalen).</p>
<p>Meest effectief: <mark>9.9 teammanagement</mark>, met veel aandacht voor zowel mensen als resultaat.</p>`,
    rubric: [["1.9 country club, met beide dimensies", 1], ["9.9 teammanagement als meest effectief", 1]]
  },
  {
    id: "SS8", topic: "staffstyle", type: "open", pts: 3, model_naam: "Conflicthantering",
    q: "Welke stijl van conflicthantering gebruikt Ilse bij het conflict over het technische team? Leg uit met de dimensies eigen belang en belang van de ander. Wat is het nadeel ten opzichte van samenwerken?",
    model: `<ul>
<li>Ilse kiest een <mark>compromis</mark>: beide partijen leveren iets in en krijgen iets, met een gemiddelde aandacht voor het eigen belang en voor het belang van de ander.</li>
<li>Nadeel: niemand krijgt wat hij echt nodig heeft. Misschien heeft Ede het team vooral in het weekend nodig en Rheden doordeweeks. Bij <mark>samenwerken</mark> zoeken partijen samen naar een win-winoplossing die beide belangen volledig dient.</li></ul>`,
    rubric: [["Compromis herkend", 1], ["Uitleg met beide dimensies", 1], ["Nadeel tegenover samenwerken (win-win)", 1]]
  },
  {
    id: "SS9", topic: "staffstyle", type: "open", pts: 2, model_naam: "Behoeftepiramide van Maslow",
    q: "Op welk niveau van de behoeftepiramide van Maslow zit de behoefte van Kasia, en op welk niveau die van Gerrit? Waarom is de leerlijn voor Kasia nu waarschijnlijk geen goede motivator?",
    model: `<ul>
<li>Kasia: <mark>veiligheid</mark> (zekerheid over werk en huisvesting).</li>
<li>Gerrit: <mark>zelfontplooiing</mark> (nieuwe dingen leren, groeien).</li>
<li>Volgens Maslow komen hogere behoeften pas aan bod als de lagere vervuld zijn. Zolang Kasia's woonzekerheid niet geregeld is, zal een leerlijn haar weinig motiveren.</li></ul>`,
    rubric: [["Kasia veiligheid en Gerrit zelfontplooiing", 1], ["Uitleg met de volgorde van behoeften", 1]]
  },

  /* ---------------- SKILLS & SHARED VALUES ---------------- */
  {
    id: "SV1", topic: "skillssv", type: "open", pts: 3, model_naam: "Skills (sleutelvaardigheden)",
    q: "Wat is de sleutelvaardigheid van Heidezoom Parken? Leg uit waarom dit een skill van de organisatie is en niet van één medewerker. Wat is het verschil met de S van staff?",
    model: `<ul>
<li>Sleutelvaardigheid: op zaterdag in vier uur 300 bungalows wisselklaar maken, zonder wachtende gasten.</li>
<li>Het is een <mark>skill van de organisatie als geheel</mark>: het lukt alleen door de samenwerking van planning, housekeeping, technische dienst en receptie. Geen enkele medewerker kan dit alleen, en het onderscheidt Heidezoom van de concurrentie.</li>
<li><mark>Staff</mark> gaat over de medewerkers zelf: wie werken er, hoe worden ze geworven, ontwikkeld en beloond. Skills gaat over wat de organisatie als geheel goed kan.</li></ul>`,
    rubric: [["Sleutelvaardigheid juist uit de casus", 1], ["Uitleg: vaardigheid van de organisatie als geheel", 1], ["Verschil met staff", 1]]
  },
  {
    id: "SV2", topic: "skillssv", type: "open", pts: 3, model_naam: "Golden circle (Sinek) en toegevoegde waarde",
    q: "Het voorstel van Daan sloeg niet aan. Herschrijf de kern van zijn voorstel volgens de golden circle van Sinek (waarom, hoe, wat). Koppel het waarom aan een doel van Heidezoom en leg uit waarom de volgorde belangrijk is.",
    model: `<ul>
<li><mark>Waarom</mark>: gasten een comfortabele, gezonde bungalow bieden en tegelijk energie besparen. Dat past bij de visie (gastvrij en natuurinclusief) en verlaagt de kosten.</li>
<li><mark>Hoe</mark>: per bungalow meten wat er gebeurt, zodat verwarming en ventilatie automatisch kunnen worden bijgestuurd en schoonmaak kan worden ingepland op werkelijk gebruik.</li>
<li><mark>Wat</mark>: 1.200 sensoren voor temperatuur, CO₂ en gebruik, gekoppeld aan het FMIS.</li></ul>
<p>Volgorde: communiceer van binnen naar buiten. Het MT wil eerst weten welke toegevoegde waarde iets heeft voor de doelen van Heidezoom. Daan begon met het wat (techniek), en dan haakt een MT af.</p>`,
    rubric: [["Waarom, gekoppeld aan een doel van Heidezoom", 1], ["Hoe en wat juist ingevuld", 1], ["Uitleg van de volgorde", 1]]
  },
  {
    id: "SV3", topic: "skillssv", type: "open", pts: 3, model_naam: "Traditionele kwaliteitszorg en TQM",
    q: "Welke vorm van kwaliteitszorg past Heidezoom nu toe, en welke vorm wil Ruben invoeren? Noem drie verschillen tussen de twee vormen, met de casus als voorbeeld.",
    model: `<p>Nu: <mark>traditionele kwaliteitszorg</mark>. Ruben wil <mark>integrale kwaliteitszorg (TQM)</mark>.</p>
<ul>
<li>Achteraf controleren (de inspecteur na de schoonmaak) versus fouten voorkomen tijdens het werk (elke schoonmaker controleert zelf).</li>
<li>Kwaliteit is van een specialist (de inspecteur) versus kwaliteit is van iedereen.</li>
<li>Fouten herstellen (team moet terug) versus fouten registreren en continu verbeteren (wekelijks één verbetering).</li></ul>`,
    rubric: [["Traditioneel nu en TQM gewenst", 1], ["Twee verschillen met casus", 1], ["Derde verschil met casus", 1]]
  },
  {
    id: "SV4", topic: "skillssv", type: "open", pts: 4, model_naam: "PDCA-cyclus (Deming)",
    q: "Zet de vier acties van Ruben in de goede volgorde van de PDCA-cyclus en geef bij elke actie de fase. Wat moet Ruben doen als de steekproef laat zien dat het doel niet gehaald wordt?",
    model: `<ol>
<li><mark>Plan</mark>: doel vaststellen (binnen drie maanden minimaal 8,3), op basis van de oorzaak uit de reviews (stof onder de bedden).</li>
<li><mark>Do</mark>: de nieuwe checklist en stofzuigerroute vier weken uitproberen in Ermelo.</li>
<li><mark>Check</mark>: na zes weken met een steekproef en de reviews meten en vergelijken met het doel.</li>
<li><mark>Act</mark>: werkt het, dan wordt het de standaard in alle parken.</li></ol>
<p>Wordt het doel niet gehaald, dan stuurt Ruben in de Act-fase bij: hij zoekt opnieuw naar de oorzaak, past het plan aan en begint een nieuwe ronde van de cyclus.</p>`,
    rubric: [["Plan: het doel", 1], ["Do: proef in Ermelo", 1], ["Check: steekproef en Act: standaard in alle parken", 1], ["Bij niet halen: bijsturen en nieuwe cyclus", 1]]
  },
  {
    id: "SV5", topic: "skillssv", type: "open", pts: 4, model_naam: "Balanced scorecard",
    q: "Plaats de zes indicatoren van Ruben in de vier perspectieven van de balanced scorecard. Welk perspectief is het zwakst vertegenwoordigd, en waarom is dat een probleem?",
    model: `<ul>
<li><mark>Financieel</mark>: (1) omzet per bungalow en (5) winst per BU.</li>
<li><mark>Klant</mark>: (2) reviewcijfer van gasten.</li>
<li><mark>Interne processen</mark>: (3) schoontijd per bungalow en (4) percentage afgekeurde bungalows.</li>
<li><mark>Innovatie en leren</mark>: (6) nieuwe concepten van Heidezoom Lab.</li></ul>
<p>Zwakst: innovatie en leren (en eigenlijk ook klant), met maar één indicator. Er is geen indicator voor de ontwikkeling van medewerkers, terwijl Heidezoom juist moet leren werken met zelfsturende teams. Een BSC is bedoeld om in balans te sturen: niet alleen financieel en op korte termijn, maar ook op klanten, processen en de toekomst.</p>`,
    rubric: [["Financieel en klant juist", 1], ["Interne processen juist", 1], ["Innovatie en leren juist", 1], ["Zwakste perspectief met uitleg over balans", 1]]
  },
  {
    id: "SV6", topic: "skillssv", type: "open", pts: 3, model_naam: "Cultuurniveaus van Schein",
    q: "Geef bij elk van de drie cultuurniveaus van Schein een voorbeeld uit de casus van Heidezoom Parken.",
    model: `<ul>
<li><mark>Artefacten</mark> (zichtbaar): het paarse poloshirt met heidetakje, de maandagbriefing (ritueel), het bord bij de receptie.</li>
<li><mark>Beleden waarden</mark>: "De gast komt altijd eerst".</li>
<li><mark>Onderliggende basisveronderstellingen</mark> (onbewust, vanzelfsprekend): "seizoenskrachten gaan toch weer weg, dus inwerken heeft geen zin".</li></ul>`,
    rubric: [["Artefact juist", 1], ["Beleden waarde juist", 1], ["Basisveronderstelling juist", 1]]
  },
  {
    id: "SV7", topic: "skillssv", type: "open", pts: 4, model_naam: "Cultuurtypen van Handy",
    q: "Welke cultuur volgens Handy past bij de parken, en welke bij Heidezoom Lab? Geef bij beide twee kenmerken uit de casus. Met welke configuratie van Mintzberg gaat elke cultuur vaak samen?",
    model: `<ul>
<li>Parken: <mark>rolcultuur</mark>. Functieomschrijvingen, werkinstructies voor bijna elke taak, formulieren; de functie en de regels bepalen wat je doet.</li>
<li>Heidezoom Lab: <mark>taakcultuur</mark>. Projectteams van specialisten, de taak staat centraal en wie de meeste kennis heeft, heeft het meeste te zeggen.</li>
<li>Mintzberg: een rolcultuur past bij de <mark>machinebureaucratie</mark>, een taakcultuur bij de <mark>innovatieve organisatie (adhocratie)</mark>.</li></ul>
<p class="valkuil">Controleer in je reader hoe de assen van Handy getekend zijn. De conclusie volgt hier uit de kenmerken.</p>`,
    rubric: [["Parken: rolcultuur", 1], ["Lab: taakcultuur", 1], ["Kenmerken uit de casus bij beide", 1], ["Koppeling met Mintzberg", 1]]
  },
  {
    id: "SV8", topic: "skillssv", type: "open", pts: 2, model_naam: "Cultuurdimensies van Hofstede",
    q: "Welke twee cultuurdimensies van Hofstede herken je bij het Deense park? Licht toe met de casus.",
    model: `<ul>
<li><mark>Kleine machtsafstand</mark>: medewerkers spreken hun leidinggevende met de voornaam aan en zeggen het direct als ze het oneens zijn.</li>
<li><mark>Feminiene cultuur</mark>: balans tussen werk en privé en zorg voor elkaar zijn belangrijker dan carrière maken en presteren.</li></ul>`,
    rubric: [["Kleine machtsafstand, met casus", 1], ["Feminien, met casus", 1]]
  },
  {
    id: "SV9", topic: "skillssv", type: "open", pts: 3, model_naam: "INK-managementmodel",
    q: "Plaats de drie verbeteracties van Ruben in een aandachtsgebied van het INK-managementmodel. Geef bij elk aan of het een organisatiegebied of een resultaatgebied is.",
    model: `<ul>
<li>Training coachend leidinggeven: <mark>leiderschap</mark> (of management van medewerkers), een <mark>organisatiegebied</mark>.</li>
<li>Nieuw reserveringssysteem: <mark>management van middelen</mark> (of processen), een <mark>organisatiegebied</mark>.</li>
<li>Onderzoek onder gemeente en omwonenden: <mark>waardering door de maatschappij</mark>, een <mark>resultaatgebied</mark>.</li></ul>`,
    rubric: [["Training juist geplaatst", 1], ["Reserveringssysteem juist geplaatst", 1], ["Onderzoek omgeving: maatschappij, resultaatgebied", 1]]
  },

  /* ---------------- RECHT (meerkeuze) ---------------- */
  {
    id: "R1", topic: "recht", type: "mc", pts: 1,
    casus: "Joyce Bakker runt de snackbar op park Ermelo als eenmanszaak onder de naam 'Snackbar De Heide'. Ze sluit een huurcontract voor de keukenapparatuur.",
    q: "Wie is partij bij het huurcontract?",
    options: ["Snackbar De Heide, want die staat ingeschreven bij de KvK.", "Joyce zelf, want een eenmanszaak is geen rechtspersoon.", "Heidezoom Groep, want de snackbar staat op haar park.", "Snackbar De Heide en Joyce samen, ieder voor de helft."],
    correct: 1,
    uitleg: "Een eenmanszaak is geen rechtspersoon en kan dus zelf geen partij zijn. Joyce sluit het contract als natuurlijk persoon en is met haar hele vermogen aansprakelijk. Inschrijving bij de KvK maakt van een eenmanszaak geen rechtspersoon."
  },
  {
    id: "R2", topic: "recht", type: "mc", pts: 1,
    casus: "Een nieuwe ondernemer opent drie kilometer van Heidezoom een vakantiepark onder de naam 'Heidezoom Vakantiehuisjes'. Gasten raken in de war.",
    q: "Wat kan Heidezoom doen?",
    options: ["Niets, een handelsnaam is alleen beschermd als die ook als merk is geregistreerd.", "Optreden op grond van de Handelsnaamwet, omdat een naam die al door een ander werd gevoerd niet mag worden gebruikt als daardoor verwarring te duchten is.", "Alleen optreden als het nieuwe park ook in Apeldoorn zit.", "De KvK vragen de inschrijving van het nieuwe park te weigeren, want de KvK toetst handelsnamen vooraf."],
    correct: 1,
    uitleg: "De Handelsnaamwet verbiedt een handelsnaam die al eerder rechtmatig door een ander werd gevoerd, als daardoor bij het publiek verwarring te duchten is, gelet op de aard en de plaats van de ondernemingen (art. 5 Hnw). Merkregistratie is daarvoor niet nodig; de KvK toetst niet vooraf of er verwarring ontstaat."
  },
  {
    id: "R3", topic: "recht", type: "mc", pts: 1,
    casus: "Heidezoom Glamping heeft 40 werknemers. Een paar medewerkers willen een ondernemingsraad.",
    q: "Is Heidezoom Glamping verplicht een ondernemingsraad in te stellen?",
    options: ["Ja, vanaf 25 werknemers is een OR verplicht.", "Ja, elke onderneming moet een OR hebben.", "Nee, een OR is pas verplicht vanaf 50 werknemers.", "Nee, een OR is pas verplicht vanaf 100 werknemers."],
    correct: 2,
    uitleg: "De Wet op de ondernemingsraden verplicht een OR in een onderneming waarin in de regel minstens 50 personen werkzaam zijn (getalscriterium). Met 40 werknemers is dat bij Heidezoom Glamping niet het geval."
  },
  {
    id: "R4", topic: "recht", type: "mc", pts: 1,
    casus: "Heidezoom Parken heeft een ondernemingsraad. De directie wil een nieuwe regeling voor werktijden en roosters in de housekeeping invoeren.",
    q: "Welk recht heeft de ondernemingsraad?",
    options: ["Adviesrecht (art. 25 Wor).", "Geen, roosters zijn een zaak van de directie.", "Alleen het recht om geïnformeerd te worden.", "Instemmingsrecht (art. 27 Wor)."],
    correct: 3,
    uitleg: "Een regeling over arbeids- en rusttijden of werktijden is een regeling op sociaal gebied. Daarvoor heeft de OR instemmingsrecht (art. 27 Wor)."
  },
  {
    id: "R5", topic: "recht", type: "mc", pts: 1,
    casus: "Heidezoom Groep wil het congrescentrum verkopen aan een andere onderneming.",
    q: "Welk recht heeft de ondernemingsraad bij dit voorgenomen besluit?",
    options: ["Instemmingsrecht (art. 27 Wor).", "Geen, want het gaat om een verkoop van vastgoed.", "Adviesrecht (art. 25 Wor).", "Een vetorecht dat de verkoop altijd kan tegenhouden."],
    correct: 2,
    uitleg: "Het overdragen van (een deel van) de onderneming is een bedrijfsorganisatorisch en financieel-economisch besluit. Daarvoor heeft de OR adviesrecht (art. 25 Wor). Het advies moet op een moment komen dat het nog invloed kan hebben."
  },
  {
    id: "R6", topic: "recht", type: "mc", pts: 1,
    casus: "Sanne de Wit wil haar volgende onderneming als besloten vennootschap (bv) beginnen. Ze heeft € 1.000 eigen geld.",
    q: "Wat is juist?",
    options: ["Dat kan: voor een bv is een notariële akte met statuten nodig, maar geen minimumkapitaal.", "Dat kan niet, voor een bv is minimaal € 18.000 kapitaal nodig.", "Dat kan alleen met een tweede oprichter.", "Een bv ontstaat door inschrijving bij de KvK, zonder notaris."],
    correct: 0,
    uitleg: "Een bv wordt opgericht bij notariële akte, waarin de statuten zijn opgenomen. Sinds de flex-bv geldt er geen minimumkapitaal meer. Eén oprichter is genoeg. Inschrijving in het handelsregister is verplicht, maar de bv ontstaat door de akte."
  },
  {
    id: "R7", topic: "recht", type: "mc", pts: 1,
    casus: "Heidezoom Glamping BV heeft een onbetaalde rekening van € 12.000 bij een tentenleverancier. De leverancier stuurt de rekening naar directeur Sanne thuis.",
    q: "Moet Sanne de rekening uit haar privévermogen betalen?",
    options: ["Ja, een bestuurder is altijd hoofdelijk aansprakelijk naast de bv.", "Ja, omdat zij de enige directeur is.", "Nee, in beginsel is alleen de bv als rechtspersoon aansprakelijk; een bestuurder is pas persoonlijk aansprakelijk in bijzondere gevallen, zoals onbehoorlijk bestuur.", "Nee, want de leverancier had een bankgarantie moeten vragen."],
    correct: 2,
    uitleg: "De bv is een rechtspersoon met een eigen vermogen. Schuldeisers kunnen in beginsel alleen de bv aanspreken. Bestuurders zijn alleen in bijzondere gevallen persoonlijk aansprakelijk, bijvoorbeeld bij onbehoorlijk bestuur of als ze hebben gehandeld namens een bv in oprichting die de handeling niet bekrachtigt."
  },
  {
    id: "R8", topic: "recht", type: "mc", pts: 1,
    casus: "Medewerkers richten bij notariële akte de Personeelsvereniging Heidezoom op en laten haar inschrijven in het handelsregister. De vereniging heeft een schuld bij een busbedrijf.",
    q: "Wie kan het busbedrijf aanspreken?",
    options: ["Alleen de vereniging.", "De vereniging, en daarnaast alle bestuurders hoofdelijk.", "Alle leden, ieder voor een gelijk deel.", "Heidezoom Groep als werkgever."],
    correct: 0,
    uitleg: "Een vereniging die bij notariële akte is opgericht, heeft volledige rechtsbevoegdheid. Is ze ook ingeschreven, dan is in beginsel alleen de vereniging aansprakelijk. Bij een informele, niet-ingeschreven vereniging zijn de bestuurders hoofdelijk aansprakelijk naast de vereniging."
  },
  {
    id: "R9", topic: "recht", type: "mc", pts: 1,
    casus: "Het bestuur van de Stichting Heidezoom Natuurfonds wil leden werven die elk jaar meebeslissen over de projecten en stemrecht krijgen.",
    q: "Kan dat?",
    options: ["Ja, als de statuten worden aangepast.", "Ja, een stichting moet minstens drie leden hebben.", "Nee, een stichting heeft geen leden; het fonds kan wel donateurs werven.", "Nee, alleen een coöperatie mag leden hebben."],
    correct: 2,
    uitleg: "Een stichting is een rechtspersoon zonder leden, opgericht om met een daartoe bestemd vermogen een doel te verwezenlijken. Wie leden met stemrecht wil, kiest een vereniging. Donateurs of vrienden van het fonds mogen wel, maar zij zijn geen leden."
  },
  {
    id: "R10", topic: "recht", type: "mc", pts: 1,
    casus: "Een aandeelhouder van Heidezoom Glamping BV wil zijn aandelen verkopen aan een investeerder buiten de familie. In de statuten staat een blokkeringsregeling.",
    q: "Wat betekent dit?",
    options: ["Hij mag zijn aandelen nooit meer aan iemand verkopen, ook niet aan de familie.", "Hij mag de aandelen alleen via de beurs verkopen.", "De investeerder moet eerst een notariële verklaring van goed gedrag overleggen.", "Hij moet ze eerst aanbieden aan de andere aandeelhouders of goedkeuring krijgen."],
    correct: 3,
    uitleg: "Een blokkeringsregeling past bij het besloten karakter van de bv. Aandelen zijn niet vrij overdraagbaar: ze moeten eerst aan de mede-aandeelhouders worden aangeboden (aanbiedingsregeling) of de overdracht heeft goedkeuring nodig (goedkeuringsregeling). Bij een nv zijn aandelen vrij verhandelbaar, bijvoorbeeld via de beurs."
  }
];
