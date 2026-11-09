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
