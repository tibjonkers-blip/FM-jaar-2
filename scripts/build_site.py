"""Bouwt de statische site in site/ uit de vraagbanken en de template.

Gebruik: python3 scripts/build_site.py
"""
import os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VRAGEN = os.path.join(ROOT, "scripts", "vragen")
SITE = os.path.join(ROOT, "site")

HEAD = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
</head>
<body>
"""
TAIL = "\n</body>\n</html>\n"

VAKKEN = {
    "inkoop-recht": dict(gen="vragen_inkoop.py", TITLE="Oefenen Inkoop en recht", HEADING="Oefenen: Inkoop en recht",
        ACCENT="#0b6a7d", ACCENT_SOFT="#e0eff2", ACCENT_DARK="#62c4d7", ACCENT_SOFT_DARK="#13313a",
        DOC_URL="https://claude.ai/artifact/VHXx8mhoAqU8B2DEmeEpsg", LS_KEY="fm-quiz-inkoop-recht",
        EXAM_LINE="Schriftelijk casustentamen in ANS: Inkoop 50%, Recht 50%. De helft van de inkooppunten is voor toepassen, dus oefen de open casusvragen echt uitgeschreven."),
    "hrm": dict(gen="vragen_hrm.py", TITLE="Oefenen HRM", HEADING="Oefenen: HRM voor de FM-professional",
        ACCENT="#7a3566", ACCENT_SOFT="#f4e6ef", ACCENT_DARK="#e39ac9", ACCENT_SOFT_DARK="#34192b",
        DOC_URL="https://claude.ai/artifact/F5i831ZTxpUePeyVdzXz8C", LS_KEY="fm-quiz-hrm",
        EXAM_LINE="Mondeling tentamen van 30 minuten: een gesprek met een acteur, vier HRM-vragen en vier arbeidsrechtvragen over de hele periode. Zeg je antwoorden bij open vragen ook hardop."),
}

def main():
    tpl = open(os.path.join(VRAGEN, "template.html"), encoding="utf-8").read()
    for slug, c in VAKKEN.items():
        out = os.path.join(SITE, slug)
        os.makedirs(out, exist_ok=True)
        html = tpl
        for k, v in c.items():
            if k != "gen":
                html = html.replace(f"__{k}__", v)
        assert "__" not in html.replace("__proto__", ""), slug
        open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(HEAD + html + TAIL)
        subprocess.run([sys.executable, os.path.join(VRAGEN, c["gen"]), os.path.join(out, "vragen.json")], check=True)
    print("site gebouwd in", SITE)

if __name__ == "__main__":
    main()
