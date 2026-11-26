# Werkafspraken voor Claude in deze repo

1. **Lees eerst `OVERZICHT.md`.** Daar staat hoe de site werkt, waar alles staat en welke afspraken gelden.
   Open alleen de bestanden die je voor de wijziging echt nodig hebt.
2. **Werk `OVERZICHT.md` bij in dezelfde commit of pull request** als je iets verandert aan de werking of de structuur:
   een bouwscript, `template.html`, `sitenav.py`, `figuren/lib.py`, `toetsen/lib.py`, de motor van de casustoetsen,
   `netlify.toml`, een nieuwe map, pagina of URL, een nieuwe `localStorage`-sleutel, of een nieuwe vaste afspraak.
   Pas ook de datum "Laatst bijgewerkt" aan. Alleen nieuwe vragen, uitleg, samenvattingstekst of figuren toevoegen
   hoeft niet, zolang de werkwijze gelijk blijft.
3. Klopt iets in `OVERZICHT.md` niet meer met de code, verbeter het dan meteen.
4. Bouw na elke wijziging in `scripts/` opnieuw (`python3 scripts/build_site.py`) en commit `site/` mee.
5. Houd `OVERZICHT.md` kort: het is een kaart van de code, geen handleiding per regel.

De controle in `.github/workflows/overzicht.yml` meldt bij een pull request of push wanneer code is veranderd
zonder dat `OVERZICHT.md` is bijgewerkt.
