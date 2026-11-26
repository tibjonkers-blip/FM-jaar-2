# Overzicht: hoe de studiesite werkt

Lees dit bestand voordat je iets aanpast. Het legt in het kort uit waar alles staat en hoe het samenhangt,
zodat je niet de hele code hoeft door te lezen. Werk het bij in dezelfde wijziging als je de werking,
de structuur of een afspraak verandert (zie `CLAUDE.md`).

Laatst bijgewerkt: 26-11-2026

## In één alinea

Statische studiesite voor Facility Management jaar 2, periode 2, met drie vakken: Inkoop en recht (IR),
HRM en Praktijkproject Business Management (BM), plus twee casustoetsen Facilitaire Bedrijfskunde uit periode 1.
Alle inhoud staat als Python-data en Markdown in `scripts/`. Python-bouwscripts maken daar kant-en-klare
HTML- en JSON-bestanden van in `site/`. Die map staat in de repo en Netlify publiceert hem zoals hij is:
er draait geen build op Netlify. Elke push naar `main` gaat automatisch live. Er is geen server, database
of login: voortgang, cijfers en notities staan alleen in de browser van de gebruiker (`localStorage`).

## Bouwen en publiceren

```
python3 scripts/build_site.py      # bouwt alles opnieuw in site/
git add -A && git commit -m "..." && git push
```

- Alleen Python 3 uit de standaardbibliotheek, geen pakketten.
- Bouw altijd opnieuw na een wijziging in `scripts/` en commit `site/` mee, anders verandert de live site niet.
- `build_site.py --artifact DIR` maakt daarnaast een versie van de oefenpagina's IR en HRM voor de Claude-artifacts (zonder sitebalk).
- `netlify.toml`: `publish = "site"`, geen build-commando, plus de beveiligingsheaders (zie Beveiliging).

## Mappen

| Pad | Wat |
|---|---|
| `site/` | Gebouwde site. Niet met de hand aanpassen, alles komt uit `scripts/`. |
| `scripts/build_*.py` | Bouwscripts (zie hieronder). |
| `scripts/sitenav.py` | Gedeelde navigatie: vaste balk bovenaan, tabbladen per vak, CSS en JS daarvan. |
| `scripts/vragen/` | Oefenvragen per vak plus `template.html`, de oefenpagina (vragen én weektoetsen). |
| `scripts/toetsen/` | Weektoetsen en eindtoetsen per vak per week (`ir_w1.py`, `hrm_eind.py`, ...), helpers in `lib.py`. |
| `scripts/toelichting/` | Uitleg "Waarom dit klopt" bij open vragen en casusdeelvragen, één bestand per vak. |
| `scripts/samenvattingen/<vak>/` | Samenvattingen als Markdown (`overzicht.md`, `week-1.md` t/m `week-7.md`), export van de Claude-documenten. |
| `scripts/figuren/` | Figuren in de samenvattingen: componenten in `lib.py`, per vak een lijst `FIGUREN`. |
| `scripts/bedrijfskunde/` | Casustoetsen Waalhop en Heidezoom: gedeelde motor (`app.js`, `markup.html`, `style.css`) en per toets een databestand (`waalhop.js`, `heidezoom.js`). |

## Pagina's en URL's

| URL | Gemaakt door | Bron |
|---|---|---|
| `/` | `build_home.py` | aantallen uit de gebouwde `vragen.json`/`toetsen.json`; maakt ook `favicon.svg` |
| `/<vak>/` (`inkoop-recht`, `hrm`, `praktijkproject`) | `build_site.py` | `scripts/vragen/template.html` + `vragen.json` + `toetsen.json` |
| `/samenvattingen/<vak>/` | `build_samenvattingen.py` | `scripts/samenvattingen/<vak>/*.md` + `scripts/figuren/<vak>.py` |
| `/bedrijfskunde/<toets>/` | `build_bedrijfskunde.py` | `scripts/bedrijfskunde/` |

Deeplinks: `/<vak>/#oefenen-wN`, `/<vak>/#toetsen-wN`, `/samenvattingen/<vak>/#week-N`.
BM heet in de code `praktijkproject` (map, slug) en `pp` (toetsen).

## Bouwvolgorde (`build_site.py`)

Per vak (instellingen in `VAKKEN` bovenin `build_site.py`: kleuren, titels, `LS_KEY`, tentamenregel):
1. `template.html` invullen (alle `__NAAM__`-plekken; de bouw stopt als er een overblijft) → `site/<vak>/index.html`.
2. Vraaggenerator draaien (`vragen_inkoop.py`, `vragen_hrm.py`, `vragen_pp.py`) → `site/<vak>/vragen.json`.
3. `build_toetsen.py <ir|hrm|pp>` → `site/<vak>/toetsen.json`.
4. `add_toelichting.py` zet de uitleg uit `scripts/toelichting/` in beide JSON-bestanden.

Daarna: `build_bedrijfskunde.py`, `build_samenvattingen.py` (leest de gebouwde JSON voor de knoppen onder elke week),
en als laatste `build_home.py`.

## Inhoud toevoegen

**Oefenvragen** (`scripts/vragen/`). Elke generator heeft een lijst `lessen` (id, week, onderdeel, titel) en `V` met vragen
via `mc(id, les, tag, vraag, opties, juist, uitleg)` en `open_(id, les, tag, vraag, model, punten)`. Extra bestanden worden
met `exec` ingelezen en vullen dezelfde lijsten aan: IR `inkoop_w27.py` + `inkoop_extra*.py`, HRM `hrm_w27.py` + `hrm_extra*.py`,
BM `pp_oefen_*.py`. Ids moeten uniek zijn (assert).

**Weektoetsen** (`scripts/toetsen/<vak>_wN.py`). Helpers `mc()`, `op()` (open) en `cs()` (casus met deelvragen) uit `lib.py`.
Per week drie keer de samenstelling uit `CONFIG` in `build_toetsen.py`; het script verdeelt alles over vaste versies A, B en C.
Eindtoetsen staan in `<vak>_eind.py`, `<vak>_eind2.py`, ...: altijd `week=0`, versie E/E2/..., nooit gemengd in weektoetsen.
`check()` controleert dubbele ids, 4 opties per MC en punten bij open vragen.

**Uitleg "Waarom dit klopt"** (`scripts/toelichting/<vak>.py`, dict `T`). Sleutel = vraag-id, of `<casus-id>-s<n>` voor deelvraag n (vanaf 0).
Elke nieuwe open vraag en casusdeelvraag hoort er een te krijgen. Ontbrekende vinden:
`python3 scripts/add_toelichting.py <vak> site/<vak> --missing`.

**Samenvattingen** (`scripts/samenvattingen/<vak>/`). Markdown uit de Claude-documenten. `clean_source()` haalt Claude-specifieke
regels weg, lege "Na de les aangevuld"-blokken verdwijnen. Een `##`-kop is een les, `###`/`####` zijn deelkoppen.
Het BM-tabblad "Logboek portfolio" komt bewust niet op de site (persoonlijk, de site is openbaar).

**Figuren** (`scripts/figuren/<vak>.py`). `F(week, les, kop, fig(...), pos/after)`; de figuur komt onder de kop waarvan de tekst
precies gelijk is aan `kop`. Komt die kop niet precies één keer voor, dan stopt de bouw. Componenten: `flow`, `phases`, `lanes`,
`ladder`, `timeline`, `cycle`, `quad`, `nest`, `tree`, `som`, `poles`, `cards`, `stairs`, `pillars`, `iceberg`, `pgrid`, `chips`,
`legend`, `bars`, `seg`, `svg`.

**Casustoetsen bedrijfskunde**: een nieuwe toets = nieuw databestand met `TOPICS`, `CASES`, `QUESTIONS` en een regel in `TOETSEN`
in `build_bedrijfskunde.py` (plus `CASUS` in `sitenav.py`).

## Gedrag in de browser

- **Oefenpagina** (`template.html`): tabbladen Oefenen en Weektoetsen, keuze per week en onderdeel, MC-opties worden bij het tonen
  geschud (verwijs in teksten dus nooit naar "optie A" of een positie). Voortgang en toetscijfers in `localStorage`
  (`LS_KEY` per vak, lezen via `lsGet`). Draait de pagina als Claude-artifact, dan gebruikt hij ook `window.claude` (db voor
  voortgang, Claude kijkt open antwoorden na); op de site is dat er niet en kijkt de gebruiker zelf na met het modelantwoord.
- **Casustoetsen**: `app.js` bewaart antwoorden in `localStorage` (sleutel per toets in `TOETSEN`), zelf nakijken met rubric.
- **Navigatie**: elke pagina krijgt de balk en tabs uit `sitenav.py`, met `root` als relatief pad naar de startpagina.
- **`localStorage` lezen**: `lsGet` in `template.html` en de lader in `bedrijfskunde/app.js` controleren het type van een bewaarde
  waarde en vallen terug op de standaardwaarde. Houd dat patroon aan bij nieuwe sleutels.

## Beveiliging

`netlify.toml` stuurt voor elke pagina een Content-Security-Policy mee: alleen eigen bestanden en Google Fonts, inline scripts
toegestaan, geen iframes, formulieren of andere domeinen. Daarnaast X-Frame-Options, nosniff, Referrer-Policy, Permissions-Policy
en HSTS. Gevolg: **elke nieuwe externe bron (script, lettertype, afbeelding, API) moet eerst in de CSP**, anders blokkeert de
browser hem. De samenvattingen laten alleen http(s)-, mail- en interne links door (`inline()` in `build_samenvattingen.py`).

## Vormgeving

"Bewegwijzering": per vak een zone met kleurband, wit codebordje (IR/HRM/BM) en tabbladen. Kleuren IR `#0b6f82`/`#63cfe2`,
HRM `#9a2d6c`/`#f095c9`, BM `#9a520a`/`#f5b65e`, startpagina navy `#1d2b4f`, donkere achtergrond `#121b2b`.
Eén lettertype: Archivo via Google Fonts. Geen monospace en geen hoofdletterlabels. Licht en donker thema.
Test elke gewijzigde pagina op 1280, 380 en 320 px breed, licht en donker.

## Vaste afspraken voor inhoud

- Alles gebaseerd op de samenvattingen, inclusief de sprekersnotities van de slides. Geen verzonnen bronnen.
- Nooit de naam van een docent; schrijf "de docent". Namen in casussen zijn verzonnen.
- Geen hij/zij voor verzonnen personen.
- Bij MC is het juiste antwoord niet duidelijk het langste, en geen dubbele vragen.

## Lopend werk (nog niet op `main`)

Controleer of deze pull requests inmiddels gemerged zijn en verplaats de beschrijving dan naar de juiste sectie hierboven.

- **PR #2, eigen notities per les**: onder elke les in de samenvattingen een notitieveld (`NOTES_CSS`/`NOTES_JS` in
  `build_samenvattingen.py`). Opslag in `localStorage`, sleutel `fm-notities-<vak>`, nooit op de site of in de repo. Onderaan elke
  samenvatting: alle notities downloaden als `.md` en terugzetten (samenvoegen, niets overschrijven), knop "Meescrollen", en de
  zoekbalk doorzoekt ook de notities. Een notitie hangt aan het les-id (`week-N-<titel>`); `scripts/samenvattingen/notitie-sleutels.json`
  houdt alle ids bij en de bouw stopt als er een verdwijnt. Lestitel veranderd? Zet het oude id op het nieuwe in `NOTITIE_ALIASSEN`.
  Synchroniseren tussen apparaten wordt nog gebouwd.
