"""Bouwt de statische site in site/ uit de vraagbanken, de weektoetsen en de template.

Gebruik:
  python3 scripts/build_site.py                 bouwt site/<vak>/ (index.html, vragen.json, toetsen.json),
                                                site/samenvattingen/<vak>/, de casustoetsen site/bedrijfskunde/<toets>/
                                                en de startpagina site/index.html
  python3 scripts/build_site.py --artifact DIR  bouwt daarnaast de Claude-artifactversie in DIR/<vak>/
"""
import os, subprocess, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
VRAGEN = os.path.join(SCRIPTS, "vragen")
SITE = os.path.join(ROOT, "site")

HEAD = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
</head>
<body>
"""
TAIL = "\n</body>\n</html>\n"

VAKKEN = {
    "inkoop-recht": dict(gen="vragen_inkoop.py", toets="ir", artifact="inkoop",
        TITLE="Oefenen Inkoop en recht", HEADING="Inkoop en recht",
        CODE="IR", ACCENT="#0b6f82", ACCENT_SOFT="#dff0f3", ACCENT_DARK="#63cfe2", ACCENT_SOFT_DARK="#123447", BAND="#0b6f82", BAND_DARK="#0d5e6e",
        CLAUDE_DOC="https://claude.ai/artifact/VHXx8mhoAqU8B2DEmeEpsg", LS_KEY="fm-quiz-inkoop-recht",
        EXAM_LINE="Schriftelijk casustentamen in ANS: Inkoop 50%, Recht 50%. De helft van de inkooppunten is voor toepassen, dus oefen de open casusvragen echt uitgeschreven."),
    "hrm": dict(gen="vragen_hrm.py", toets="hrm", artifact="hrm",
        TITLE="Oefenen HRM", HEADING="HRM voor de FM-professional",
        CODE="HRM", ACCENT="#9a2d6c", ACCENT_SOFT="#f6e4ef", ACCENT_DARK="#f095c9", ACCENT_SOFT_DARK="#3a1a3a", BAND="#8f2a65", BAND_DARK="#7a2457",
        CLAUDE_DOC="https://claude.ai/artifact/F5i831ZTxpUePeyVdzXz8C", LS_KEY="fm-quiz-hrm",
        EXAM_LINE="Mondeling tentamen van 30 minuten: een gesprek met een acteur, vier HRM-vragen en vier arbeidsrechtvragen over de hele periode. Zeg je antwoorden bij open vragen ook hardop."),
    "praktijkproject": dict(gen="vragen_pp.py", toets="pp", artifact=None,
        TITLE="Oefenen Business management", HEADING="Praktijkproject Business Management",
        CODE="BM", ACCENT="#9a520a", ACCENT_SOFT="#fbecd8", ACCENT_DARK="#f5b65e", ACCENT_SOFT_DARK="#3a2b1c", BAND="#9a520a", BAND_DARK="#8a4a0a",
        CLAUDE_DOC="https://claude.ai/artifact/MNHrxykYerRjrc76rQu4Qg", LS_KEY="fm-quiz-praktijkproject",
        EXAM_LINE="Geen schriftelijk tentamen: je cijfer komt uit de adviespresentatie (30 minuten plus 15 minuten vragen) en je portfolio moet voldoende zijn. Oefen hier de modellen die je in je advies moet kunnen uitleggen en toepassen."),
}

def render(tpl, c, target, slug):
    vals = {k: v for k, v in c.items() if k.isupper() and k != "CLAUDE_DOC"}
    if target == "site":
        vals.update(HOME='<a class="home" href="../">← Studieplek</a>',
                    DOC_URL=f"../samenvattingen/{slug}/", DOC_CLASS="", DOC_TARGET="")
    else:
        vals.update(HOME="", DOC_URL=c["CLAUDE_DOC"], DOC_CLASS="ext", DOC_TARGET='target="_blank" rel="noopener"')
    html = tpl
    for k, v in vals.items():
        html = html.replace(f"__{k}__", v)
    rest = html.replace("__proto__", "")
    assert "__" not in rest, (slug, rest[rest.index("__") - 40: rest.index("__") + 40])
    return html

def main():
    art = None
    if "--artifact" in sys.argv:
        art = sys.argv[sys.argv.index("--artifact") + 1]
    tpl = open(os.path.join(VRAGEN, "template.html"), encoding="utf-8").read()
    for slug, c in VAKKEN.items():
        out = os.path.join(SITE, slug)
        os.makedirs(out, exist_ok=True)
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(HEAD + render(tpl, c, "site", slug) + TAIL)
        subprocess.run([sys.executable, os.path.join(VRAGEN, c["gen"]), os.path.join(out, "vragen.json")], check=True)
        subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_toetsen.py"), c["toets"], os.path.join(out, "toetsen.json")], check=True)
        subprocess.run([sys.executable, os.path.join(SCRIPTS, "add_toelichting.py"), slug, out], check=True)
        if art and c["artifact"]:
            ad = os.path.join(art, c["artifact"])
            os.makedirs(ad, exist_ok=True)
            open(os.path.join(ad, "index.html"), "w", encoding="utf-8").write(render(tpl, c, "artifact", slug))
            for f in ("vragen.json", "toetsen.json"):
                shutil.copy(os.path.join(out, f), os.path.join(ad, f))
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_bedrijfskunde.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_samenvattingen.py")], check=True)
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_home.py")], check=True)
    print("site gebouwd in", SITE, "| artifacts in", art or "-")

if __name__ == "__main__":
    main()
