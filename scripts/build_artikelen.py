"""Bouwt de artikelenlijst per vak: /artikelen/<vak>/ (alleen Inkoop en recht en HRM).

Data: scripts/artikelen/<module>.py met TITEL, LEAD, WETTEN (volgorde van de groepen) en ARTIKELEN (via A(...)).
Per artikel: nummer, korte titel, inhoud in eigen woorden, de weken waarin het voorkomt (links naar de samenvatting) en
eventueel een waarschuwing (let). Zoeken en filteren per week gebeurt in de browser; er wordt niets bewaard.
"""
import html, importlib.util, os, re
import sitenav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "artikelen")
OUT = os.path.join(ROOT, "site", "artikelen")

VAKKEN = {
    "inkoop-recht": dict(module="inkoop_recht", code="IR", naam="Inkoop en recht", weeklabel="Recht week",
                         accent=("#0b6f82", "#dff0f3", "#63cfe2", "#123447")),
    "hrm": dict(module="hrm", code="HRM", naam="HRM", weeklabel="Arbeidsrecht les",
                accent=("#9a2d6c", "#f6e4ef", "#f095c9", "#3a1a3a")),
}
AFKORTING = {"BW7": "BW", "BW": "BW", "WAZO": "WAZO", "Awgb": "Awgb", "Gw": "Gw",
             "Aw1": "Aw", "Aw2": "Aw", "Aw2A": "Aw", "Aw4": "Aw", "EU": ""}

def load(name):
    spec = importlib.util.spec_from_file_location(f"artikelen_{name}", os.path.join(SRC, f"{name}.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def label(a):
    afk = AFKORTING[a["wet"]]
    return f"Art. {a['nr']} {afk}".strip() if afk else a["nr"]

def check(mod, vak):
    groepen = [g for g, _, _ in mod.WETTEN]
    seen = set()
    for a in mod.ARTIKELEN:
        assert a["wet"] in groepen, f"{vak}: onbekende wet {a['wet']} bij {a['nr']}"
        key = (a["wet"], a["nr"])
        assert key not in seen, f"{vak}: {a['nr']} staat twee keer in {a['wet']}"
        seen.add(key)
        assert a["weken"] and all(1 <= w <= 7 for w in a["weken"]), f"{vak}: weken van {a['nr']}"
        assert a["titel"] and a["inhoud"], f"{vak}: lege titel of inhoud bij {a['nr']}"

LID = re.compile(r"(?:(?<=^)|(?<=\. ))(?=Lid \d+[a-z]?(?: (?:en|t/m) \d+)?(?: sub [a-z])?: )")

LIDKOP = re.compile(r"Lid \d+[a-z]?(?: (?:en|t/m) \d+)?(?: sub [a-z])?: ")

def body(text):
    """Inhoud met meerdere "Lid N: ..." zinnen wordt een lijstje, zodat je de leden snel terugvindt."""
    parts = [p.strip() for p in LID.split(text) if p.strip()]
    if sum(1 for p in parts if LIDKOP.match(p)) < 2:
        return f"<p>{html.escape(text)}</p>"
    out, items = [], []
    for p in parts:
        if LIDKOP.match(p):
            kop, rest = p.split(": ", 1)
            items.append(f"<li><b>{html.escape(kop)}</b> {html.escape(rest)}</li>")
        elif items:
            items[-1] = items[-1][:-5] + " " + html.escape(p) + "</li>"
        else:
            out.append(f"<p>{html.escape(p)}</p>")
    return "".join(out) + f'<ul class="leden">{"".join(items)}</ul>'

def card(a, vak, c):
    weeks = "".join(f'<a class="wk" href="../../samenvattingen/{vak}/#week-{w}">Week {w}</a>' for w in sorted(a["weken"]))
    let = (f'<p class="let"><b>Let op</b> {html.escape(a["let"])}</p>') if a["let"] else ""
    data = html.escape(" ".join([label(a), a["titel"], a["inhoud"], a["let"] or ""]).lower())
    wk = " ".join(str(w) for w in a["weken"])
    aid = "art-" + slug(f"{a['wet']}-{a['nr']}")
    return (f'<article class="art" id="{aid}" data-w="{wk}" data-t="{data}">'
            f'<header><span class="nr">{html.escape(label(a))}</span><h3>{html.escape(a["titel"])}</h3></header>'
            f'{body(a["inhoud"])}{let}'
            f'<footer><span class="wl">Komt voor in</span>{weeks}</footer></article>')

PAGE = r"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITEL__ · __NAAM__</title>
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap">
<style>
:root {
  --paper: #f3f5f8; --sheet: #ffffff; --sunk: #e4e9f1; --ink: #16202f; --ink-soft: #5a6577; --rule: #d9dfe8;
  --accent: __A1__; --accent-soft: __A2__; --on-accent: #ffffff;
  --warn: #8f5d00; --warn-soft: #f9eed6; --mark: #fde99a;
  --font-display: "Archivo", "Arial Nova", "Segoe UI", system-ui, sans-serif;
  --font-body: "Archivo", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
    --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
  --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: calc(env(safe-area-inset-top, 0px) + var(--sb-h, 0px) + 70px); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--font-body); font-size: 16px; line-height: 1.55; }
h1, h2, h3 { font-family: var(--font-display); margin: 0; line-height: 1.15; text-wrap: balance; overflow-wrap: break-word; }
h1 { font-size: clamp(1.9rem, 5vw, 2.6rem); font-weight: 750; letter-spacing: -0.02em; line-height: 1.08; }
@media (max-width: 400px) { h1 { font-size: 1.65rem; } }
p { margin: 0; }
a { color: var(--accent); text-underline-offset: 2px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.band-in { max-width: 860px; }
__TABS_CSS__
__BAR_CSS__
.wrap { max-width: 860px; margin: 0 auto; display: flex; flex-direction: column; gap: 18px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 96px; }

/* zoeken en filteren: blijft bovenaan staan */
.tools { position: relative; z-index: 5; background: var(--paper);
  margin-inline: -4px; padding: 12px 4px 10px; display: flex; flex-direction: column; gap: 10px; border-bottom: 1px solid var(--rule); }
@media (min-width: 700px) { .tools { position: sticky; top: calc(env(safe-area-inset-top, 0px) + var(--sb-h, 0px)); } }
.search { position: relative; }
.search input { width: 100%; font: inherit; color: var(--ink); background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; padding: 11px 14px 11px 42px; }
.search input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.search svg { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 17px; height: 17px; color: var(--ink-soft); pointer-events: none; }
.weeks { display: flex; gap: 4px; flex-wrap: wrap; align-items: center; }
.weeks .wl { font-size: 0.86rem; color: var(--ink-soft); margin-right: 4px; }
.weeks button { font: inherit; font-size: 0.88rem; font-weight: 600; min-height: 36px; min-width: 40px; padding: 4px 10px; border-radius: 8px; cursor: pointer;
  background: var(--sheet); border: 1px solid var(--rule); color: var(--ink-soft); font-variant-numeric: tabular-nums; }
.weeks button:hover { color: var(--ink); }
.weeks button[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.count { font-size: 0.86rem; color: var(--ink-soft); }

/* inhoudsopgave per wet */
.toc { display: flex; flex-wrap: wrap; gap: 6px; list-style: none; margin: 0; padding: 0; }
.toc a { display: inline-flex; gap: 6px; align-items: baseline; padding: 6px 12px; border-radius: 999px; background: var(--sheet); border: 1px solid var(--rule);
  color: var(--ink); text-decoration: none; font-size: 0.9rem; font-weight: 600; }
.toc a:hover { border-color: var(--accent); }
.toc small { color: var(--ink-soft); font-weight: 500; font-variant-numeric: tabular-nums; }

main { display: flex; flex-direction: column; gap: 18px; min-width: 0; }
.group { display: flex; flex-direction: column; gap: 10px; }
.group h2 { font-size: 1.3rem; font-weight: 800; padding-top: 10px; }
.list { display: flex; flex-direction: column; gap: 8px; }
.art { background: var(--sheet); border: 1px solid var(--rule); border-radius: 12px; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.art:target { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.art header { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 12px; }
.art .nr { flex: none; font-weight: 800; font-stretch: 108%; color: var(--accent); font-variant-numeric: tabular-nums; }
.art h3 { font-size: 1.02rem; font-weight: 700; min-width: 0; }
.art > p { max-width: 75ch; overflow-wrap: break-word; }
.art .leden { margin: 0; padding-left: 1.2em; display: flex; flex-direction: column; gap: 4px; max-width: 75ch; }
.art .leden b { font-weight: 700; }
.art .let { background: var(--warn-soft); border-radius: 8px; padding: 8px 12px; font-size: 0.92rem; }
.art .let b { color: var(--warn); margin-right: 4px; }
.art footer { display: flex; flex-wrap: wrap; gap: 4px 6px; align-items: center; font-size: 0.82rem; }
.art footer .wl { color: var(--ink-soft); margin-right: 2px; }
.art .wk { padding: 2px 9px; border-radius: 999px; background: var(--accent-soft); color: var(--accent); font-weight: 700; text-decoration: none; white-space: nowrap; }
.art .wk:hover { text-decoration: underline; }
mark { background: var(--mark); color: inherit; border-radius: 2px; padding: 0 1px; }
.empty { padding: 18px; border: 1px dashed var(--ink-soft); border-radius: 12px; color: var(--ink-soft); }
.source { font-size: 0.9rem; color: var(--ink-soft); max-width: 75ch; }
</style>
</head>
<body>
__SITEBAR__<header class="band" id="top">
<div class="band-in">
  __CRUMBS__
  <div class="title-row"><span class="plate" aria-hidden="true">__CODE__</span><div><span class="kind">Wetsartikelen</span><h1>__TITEL__</h1></div></div>
  <p class="lead">__LEAD__</p>
  <p class="meta"><span><strong>__N__</strong> artikelen</span><span><strong>__NLET__</strong> met een let op</span></p>
  __TABS__
</div>
</header>
<div class="wrap">
<div class="tools" id="tools">
  <div class="search" role="search">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="Zoek op nummer of woord, bijvoorbeeld 7:652 of proeftijd" autocomplete="off" aria-label="Zoek een artikel">
  </div>
  <div class="weeks" role="group" aria-label="Filter op week"><span class="wl">__WEEKLABEL__</span>__WEEKBTNS__</div>
  <p class="count" id="count" aria-live="polite"></p>
</div>
<main id="main">
<nav aria-label="Wetten op deze pagina"><ul class="toc">__TOC__</ul></nav>
__GROUPS__
<p class="empty" id="empty" hidden>Geen artikel gevonden. Probeer een ander woord of zet het weekfilter op Alle.</p>
<p class="source">Bron: de samenvattingen op deze site, de slides en het oefenmateriaal met antwoorden. Een "let op" staat waar de slide, het antwoordmodel en de wet van elkaar verschillen, of waar je zelf moet nalezen. Neem op het tentamen altijd het artikel uit je wettenbundel over.</p>
</main>
</div>
__SITEFOOT__
<script>
(function () {
  var q = document.getElementById('q'), count = document.getElementById('count'), empty = document.getElementById('empty');
  var arts = Array.prototype.slice.call(document.querySelectorAll('.art'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.group'));
  var btns = Array.prototype.slice.call(document.querySelectorAll('.weeks button'));
  var week = '';
  var norm = function (s) { return s.toLowerCase().replace(/\s+/g, ' ').trim(); };
  function apply() {
    var terms = norm(q.value).split(' ').filter(Boolean), shown = 0;
    arts.forEach(function (a) {
      var t = a.getAttribute('data-t'), ok = (!week || (' ' + a.getAttribute('data-w') + ' ').indexOf(' ' + week + ' ') > -1);
      for (var i = 0; ok && i < terms.length; i++) if (t.indexOf(terms[i]) < 0) ok = false;
      a.hidden = !ok; if (ok) shown++;
    });
    groups.forEach(function (g) {
      var n = g.querySelectorAll('.art:not([hidden])').length;
      g.hidden = n === 0;
      var c = document.querySelector('.toc a[href="#' + g.id + '"]');
      if (c) { c.parentNode.hidden = n === 0; c.querySelector('small').textContent = n; }
    });
    empty.hidden = shown > 0;
    count.textContent = (terms.length || week) ? shown + ' van ' + arts.length + ' artikelen' : arts.length + ' artikelen';
  }
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      week = b.getAttribute('data-w');
      btns.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      apply();
    });
  });
  q.addEventListener('input', apply);
  var m = /^#w([1-7])$/.exec(location.hash);
  if (m) { var b = document.querySelector('.weeks button[data-w="' + m[1] + '"]'); if (b) b.click(); }
  apply();
})();
</script>
__BAR_JS__
</body>
</html>
"""

def build():
    totaal = {}
    for vak, c in VAKKEN.items():
        mod = load(c["module"])
        check(mod, vak)
        groups, toc = [], []
        for g, naam, kort in mod.WETTEN:
            items = [a for a in mod.ARTIKELEN if a["wet"] == g]
            if not items:
                continue
            gid = "wet-" + slug(g)
            toc.append(f'<li><a href="#{gid}">{html.escape(kort)} <small>{len(items)}</small></a></li>')
            groups.append(f'<section class="group" id="{gid}" aria-labelledby="{gid}-h"><h2 id="{gid}-h">{html.escape(naam)}</h2>'
                          f'<div class="list">{"".join(card(a, vak, c) for a in items)}</div></section>')
        weken = sorted({w for a in mod.ARTIKELEN for w in a["weken"]})
        btns = ['<button type="button" data-w="" aria-pressed="true">Alle</button>'] + \
               [f'<button type="button" data-w="{w}" aria-pressed="false" aria-label="{c["weeklabel"]} {w}">{w}</button>' for w in weken]
        a1, a2, a3, a4 = c["accent"]
        page = PAGE
        for k, v in dict(TITEL=html.escape(mod.TITEL), NAAM=html.escape(c["naam"]), LEAD=html.escape(mod.LEAD), CODE=c["code"],
                         N=str(len(mod.ARTIKELEN)), NLET=str(sum(1 for a in mod.ARTIKELEN if a["let"])),
                         WEEKLABEL=c["weeklabel"], WEEKBTNS="".join(btns), TOC="".join(toc), GROUPS="\n".join(groups),
                         SITEBAR=sitenav.bar("../../", vak, "casus"), TABS=sitenav.tabs("../../", vak, "art"),
                         CRUMBS=sitenav.crumbs("../../", vak, "Wetsartikelen"), SITEFOOT=sitenav.footer("../../"),
                         TABS_CSS=sitenav.TABS_CSS, BAR_CSS=sitenav.bar_css(), BAR_JS=sitenav.BAR_JS,
                         A1=a1, A2=a2, A3=a3, A4=a4).items():
            page = page.replace(f"__{k}__", v)
        assert "__" not in page, vak
        os.makedirs(os.path.join(OUT, vak), exist_ok=True)
        open(os.path.join(OUT, vak, "index.html"), "w", encoding="utf-8").write(page)
        totaal[vak] = len(mod.ARTIKELEN)
        print("artikelen", vak, len(mod.ARTIKELEN), "artikelen,", len(page) // 1024, "KB")
    return totaal

if __name__ == "__main__":
    build()
