# FM jaar 2: studieplek periode 2

Statische studiesite voor Facility Management jaar 2, periode 2 (Inkoop en recht, HRM, Praktijkproject BM).
Netlify publiceert de map `site/` (zie `netlify.toml`); er is geen build op Netlify.

## Structuur

- `site/`: de gepubliceerde site (startpagina, oefenvragen per vak, later weektoetsen en samenvattingen).
- `scripts/vragen/`: vraagbanken voor de oefenvragen (`vragen_*.py` plus `*_w27.py`) en `template.html` voor de oefenpagina's.
- `scripts/toetsen/`: vraagbanken voor de weektoetsen (per vak per week).
- `scripts/build_site.py`: bouwt `site/` opnieuw uit de vraagbanken.

## Bijwerken

```
python3 scripts/build_site.py
git add -A && git commit -m "..." && git push
```

## Eigen notities per les

Onder elke les in de samenvattingen staat een notitieveld. Wat je daar typt, wordt alleen in je eigen browser bewaard (localStorage, sleutel `fm-notities-<vak>`) en komt nooit op de site of in deze repo. Onderaan elke samenvatting kun je alle notities van dat vak downloaden als `.md`-bestand en dat bestand later terugzetten, ook op een ander apparaat.

Een notitie hangt aan het id van haar les (`week-3-sourcing`). `scripts/samenvattingen/notitie-sleutels.json` houdt bij welke ids een notitieveld hebben gehad. Verandert de titel van een les, dan stopt `build_samenvattingen.py` met een melding: zet dan in `NOTITIE_ALIASSEN` het oude id op het nieuwe, zodat de notities meeverhuizen.
