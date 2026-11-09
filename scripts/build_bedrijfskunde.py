"""Bouwt de casus-proeftoetsen Facilitaire Bedrijfskunde (periode 1) voor de site.

Eén gedeelde motor (scripts/bedrijfskunde/style.css, markup.html, app.js) en per toets een databestand
met TOPICS, CASES en QUESTIONS. Uitvoer: site/bedrijfskunde/<slug>/index.html.
Nakijken door Claude werkt alleen als de pagina in Claude draait; op de site is zelf nakijken beschikbaar.
"""
import os, json

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "bedrijfskunde")
SITE = os.path.join(os.path.dirname(HERE), "site", "bedrijfskunde")

TOETSEN = [
    dict(slug="waalhop", data="waalhop.js", titel="Proeftoets Waalhop", key="waalhop-proeftoets-v1",
         lead="Brouwerijconcern Waalhop. Casusvragen over alle S'en en meerkeuzevragen over ondernemingsrecht.",
         fictie="Waalhop Groep is een verzonnen organisatie.",
         hint="Alle vragen samen: reken op ongeveer 3 uur. Per onderwerp: 20 tot 40 minuten."),
    dict(slug="heidezoom", data="heidezoom.js", titel="Proeftoets Heidezoom", key="heidezoom-proeftoets-v1",
         lead="Vakantiebedrijf Heidezoom. Dezelfde opzet als Waalhop, met nieuwe casussen en vragen over alle S'en en ondernemingsrecht.",
         fictie="Heidezoom Groep is een verzonnen organisatie.",
         hint="Alle vragen samen: reken op ongeveer 3 uur. Per onderwerp: 20 tot 40 minuten."),
]

FONTS = "https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,400;7..72,600&family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap"

PAGE = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITLE__</title>
<meta name="description" content="__LEAD__">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="__FONTS__">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0}img{max-width:100%}
__CSS__
</style>
</head>
<body>
__MARKUP__
<script>
__DATA__

__APP__
</script>
</body>
</html>
"""

def read(name):
    return open(os.path.join(SRC, name), encoding="utf-8").read()

def build():
    css, markup, app = read("style.css"), read("markup.html"), read("app.js")
    for t in TOETSEN:
        others = [o for o in TOETSEN if o is not t]
        other = " ".join(f'Ook beschikbaar: <a href="../{o["slug"]}/">{o["titel"]}</a>.' for o in others)
        m = (markup.replace("__H1__", t["titel"]).replace("__LEAD__", t["lead"]).replace("__OTHER__", other)
                   .replace("__HINT__", t["hint"]).replace("__FICTIE__", t["fictie"]))
        a = app.replace("__KEY__", t["key"]).replace("__HINT__", t["hint"])
        html = (PAGE.replace("__TITLE__", t["titel"]).replace("__LEAD__", t["lead"]).replace("__FONTS__", FONTS)
                    .replace("__CSS__", css).replace("__MARKUP__", m).replace("__DATA__", read(t["data"])).replace("__APP__", a))
        assert "__" not in html.replace("__proto__", ""), [l for l in html.splitlines() if "__" in l][:3]
        out = os.path.join(SITE, t["slug"])
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html)
        print(f"bedrijfskunde/{t['slug']}: {len(html)//1024} kB")

def counts():
    """Aantal vragen en punten per toets, voor de startpagina."""
    import re
    res = {}
    for t in TOETSEN:
        d = read(t["data"])
        n_open = len(re.findall(r'type: "open"', d)); n_mc = len(re.findall(r'type: "mc"', d))
        pts = sum(int(x) for x in re.findall(r'pts: (\d+)', d))
        res[t["slug"]] = dict(titel=t["titel"], open=n_open, mc=n_mc, punten=pts)
    return res

if __name__ == "__main__":
    build()
    print(json.dumps(counts(), ensure_ascii=False))
