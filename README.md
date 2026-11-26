# FM jaar 2: studieplek periode 2

Statische studiesite voor Facility Management jaar 2, periode 2 (Inkoop en recht, HRM, Praktijkproject BM).
Netlify publiceert de map `site/` (zie `netlify.toml`); er is geen build op Netlify.

Hoe alles werkt en waar het staat: zie [OVERZICHT.md](OVERZICHT.md).

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

Onder elke les in de samenvattingen staat een notitieveld. Wat je typt, wordt in je browser bewaard en nooit op de site of in deze repo gezet. Onderaan elke samenvatting kun je alle notities van dat vak downloaden als `.md`-bestand en dat bestand later terugzetten.

### Synchroniseren tussen je apparaten instellen (eenmalig)

1. Netlify: open de site, ga naar **Site configuration > Environment variables** en voeg de variabele `NOTITIES_WACHTWOORD` toe. Kies een lang wachtwoord (minstens 12 tekens, bijvoorbeeld vier losse woorden) dat je nergens anders gebruikt.
2. Publiceer de site opnieuw (**Deploys > Trigger deploy > Deploy site**), of merge daarna pas de pull request: een functie ziet een nieuwe variabele pas na een nieuwe deploy.
3. Open een samenvatting, scroll naar **Je eigen notities** en vul onder "Synchroniseren tussen je apparaten" het wachtwoord in. Doe dat één keer per apparaat (laptop, telefoon); het geldt meteen voor alle drie de vakken.

De notities staan dan ook in Netlify Blobs (store `notities`) van jouw Netlify-account. Hoe het technisch werkt: zie "Eigen notities" in [OVERZICHT.md](OVERZICHT.md).
