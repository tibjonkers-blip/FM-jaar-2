"""Bouwt de begrippenpagina's site/begrippen/<vak>/index.html: een begrippenlijst per les, flitskaarten en een dictee.

Bron: scripts/begrippen/<vak>.py (lijst B met b(les, begrip, uitleg, art, ook)). De lessen (week, onderdeel, titel) komen uit de
gebouwde site/<vak>/vragen.json, dus draai dit na de vraaggeneratoren (build_site.py doet dat).
Voortgang (welke begrippen je kent) staat alleen in de browser: localStorage fm-begrippen-<vak>.

Gebruik: python3 scripts/build_begrippen.py
"""
import html, importlib.util, json, os, re, sys
import sitenav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "begrippen")
OUT = os.path.join(ROOT, "site", "begrippen")

VAKKEN = {
    "inkoop-recht": dict(bron="inkoop_recht", heading="Inkoop en recht", code="IR",
        accent=("#0b6f82", "#dff0f3", "#63cfe2", "#123447"), band=("#0b6f82", "#0d5e6e")),
    "hrm": dict(bron="hrm", heading="HRM voor de FM-professional", code="HRM",
        accent=("#9a2d6c", "#f6e4ef", "#f095c9", "#3a1a3a"), band=("#8f2a65", "#7a2457")),
    "praktijkproject": dict(bron="praktijkproject", heading="Praktijkproject Business Management", code="BM",
        accent=("#9a520a", "#fbecd8", "#f5b65e", "#3a2b1c"), band=("#9a520a", "#8a4a0a")),
}


def slugify(s):
    s = s.lower()
    for a, b in (("é", "e"), ("ë", "e"), ("è", "e"), ("ï", "i"), ("ö", "o"), ("ü", "u"), ("á", "a"), ("ó", "o"), ("×", "x")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48]


def load(slug):
    """Geeft (lessen, begrippen) voor een vak. lessen: de lessen uit vragen.json die begrippen hebben, in lesvolgorde."""
    c = VAKKEN[slug]
    if SRC not in sys.path:
        sys.path.insert(0, SRC)
    spec = importlib.util.spec_from_file_location("begrippen_" + c["bron"], os.path.join(SRC, c["bron"] + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    vr = json.load(open(os.path.join(ROOT, "site", slug, "vragen.json"), encoding="utf-8"))
    lessen = {l["id"]: l for l in vr["lessen"]}
    items, seen = [], set()
    for x in m.B:
        assert x["les"] in lessen, f"begrippen {slug}: les {x['les']!r} bestaat niet in vragen.json ({x['begrip']})"
        i = f"{x['les']}-{slugify(x['begrip'])}"
        assert i not in seen, f"begrippen {slug}: dubbel begrip {x['begrip']!r} in {x['les']}"
        seen.add(i)
        items.append(dict(x, id=i))
    used = [l for l in vr["lessen"] if any(x["les"] == l["id"] for x in items)]
    order = {l["id"]: n for n, l in enumerate(used)}
    items.sort(key=lambda x: order[x["les"]])  # stabiel: binnen een les de volgorde van het bronbestand
    return used, items


def counts(slug):
    """{week: aantal begrippen} voor de knoppen onder de samenvatting en op de startpagina."""
    lessen, items = load(slug)
    wk = {l["id"]: l["week"] for l in lessen}
    out = {}
    for x in items:
        out[wk[x["les"]]] = out.get(wk[x["les"]], 0) + 1
    return out


PAGE = r"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Begrippen __HEADING__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Begrippenlijst __HEADING__ per les, met flitskaarten en een dictee.">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap">
<style>
/* Begrippen per vak, in de bewegwijzering van de studieplek: zoneband met bordje en tabbladen, daaronder een keuzepaneel
   (weken en onderdelen) en drie manieren van oefenen: de lijst, flitskaarten en een dictee. */
:root {
  --paper: #eef1f6; --sheet: #ffffff; --sunk: #e4e9f1; --ink: #16202f; --ink-soft: #5a6577; --rule: #d9dfe8;
  --accent: __A1__; --accent-soft: __A2__; --on-accent: #ffffff; --band: __B1__;
  --good: #1b7a46; --good-soft: #def2e6; --bad: #b3261e; --bad-soft: #fbe3e1; --warn: #8f5d00; --warn-soft: #f9eed6; --mark: #fde99a;
  --font: "Archivo", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
    --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --band: __B2__;
    --good: #6fd6a0; --good-soft: #143224; --bad: #ff9a8f; --bad-soft: #3d1a1a; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
  --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --band: __B2__;
  --good: #6fd6a0; --good-soft: #143224; --bad: #ff9a8f; --bad-soft: #3d1a1a; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: var(--font); font-size: 16px; line-height: 1.55; }
button, input, select { font: inherit; color: inherit; }
button { cursor: pointer; }
h1, h2, h3 { margin: 0; line-height: 1.15; text-wrap: balance; overflow-wrap: break-word; hyphens: auto; }
h1 { font-size: clamp(1.9rem, 5.2vw, 2.7rem); font-weight: 800; font-stretch: 116%; letter-spacing: -0.012em; line-height: 1.08; }
h2 { font-size: 1.25rem; font-weight: 800; font-stretch: 108%; }
p { margin: 0; }
a { color: var(--accent); text-underline-offset: 2px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
@media (max-width: 400px) { h1 { font-size: 1.7rem; font-stretch: 104%; } }

.band-in { max-width: 860px; }
__TABS_CSS__
__BAR_CSS__

.wrap { max-width: 860px; margin: 0 auto; display: flex; flex-direction: column; gap: 18px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 20px 80px; }
main { display: flex; flex-direction: column; gap: 18px; min-width: 0; }
.panel { background: var(--sheet); border: 1px solid var(--rule); border-radius: 14px; padding: 18px 20px; display: flex; flex-direction: column; gap: 14px; min-width: 0; }
.small { font-size: 0.9rem; color: var(--ink-soft); }
.filter-head { display: flex; align-items: baseline; gap: 12px; margin-bottom: 8px; flex-wrap: wrap; }
.filter-label { font-weight: 700; }
.linkbtn { border: 0; background: none; padding: 0; color: var(--accent); text-decoration: underline; text-underline-offset: 2px; font-size: 0.9rem; }
.chips { display: flex; flex-wrap: wrap; gap: 8px; }
.chip { border: 1px solid var(--rule); background: var(--sheet); color: var(--ink-soft); border-radius: 999px; padding: 7px 14px; font-weight: 500; display: inline-flex; gap: 8px; align-items: baseline; }
.chip:hover { border-color: var(--accent); }
.chip .n { font-size: 0.76rem; color: var(--ink-soft); font-variant-numeric: tabular-nums; }
.chip[aria-pressed="true"] { background: var(--accent-soft); border-color: var(--accent); color: var(--accent); font-weight: 700; }
.chip[aria-pressed="true"] .n { color: var(--accent); opacity: 0.8; }
.sel-summary { font-weight: 600; }
.bar { height: 8px; border-radius: 99px; background: var(--sunk); overflow: hidden; display: flex; }
.bar i { display: block; height: 100%; background: var(--good); }

/* modi */
.modes { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px; padding: 4px; background: var(--sunk); border-radius: 12px; }
.modes button { border: 0; background: transparent; border-radius: 9px; padding: 10px 8px; font-weight: 700; color: var(--ink-soft); }
.modes button[aria-pressed="true"] { background: var(--sheet); color: var(--accent); box-shadow: 0 1px 3px rgba(10, 18, 36, 0.12); }
.row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.btn { border: 1px solid var(--rule); background: var(--sheet); border-radius: 9px; padding: 10px 16px; font-weight: 600; min-height: 44px; }
.btn:hover:not(:disabled) { border-color: var(--accent); }
.btn.primary { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.btn.good { background: var(--good-soft); border-color: var(--good); color: var(--good); }
.btn.bad { background: var(--bad-soft); border-color: var(--bad); color: var(--bad); }
.btn:disabled { opacity: 0.5; cursor: default; }
.opt { display: inline-flex; align-items: center; gap: 8px; font-size: 0.95rem; }
.opt input { width: 18px; height: 18px; accent-color: var(--accent); }
.seg { display: inline-flex; border: 1px solid var(--rule); border-radius: 9px; overflow: hidden; }
.seg button { border: 0; background: var(--sheet); padding: 8px 12px; font-weight: 600; color: var(--ink-soft); font-size: 0.92rem; }
.seg button + button { border-left: 1px solid var(--rule); }
.seg button[aria-pressed="true"] { background: var(--accent-soft); color: var(--accent); }
.empty { padding: 18px; border: 1px dashed var(--rule); border-radius: 12px; color: var(--ink-soft); }

/* lijst */
.search { position: relative; }
.search input { width: 100%; border: 1px solid var(--rule); background: var(--sheet); border-radius: 10px; padding: 11px 14px 11px 40px; }
.search input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.search svg { position: absolute; left: 13px; top: 50%; transform: translateY(-50%); width: 17px; height: 17px; color: var(--ink-soft); pointer-events: none; }
.les { display: flex; flex-direction: column; gap: 0; background: var(--sheet); border: 1px solid var(--rule); border-radius: 14px; overflow: hidden; }
.les-head { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 14px; padding: 14px 18px; background: var(--sunk); }
.les-head > div:first-child { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1 1 260px; }
.les-head small { font-weight: 700; color: var(--accent); font-size: 0.82rem; }
.les-head h3 { font-size: 1.05rem; font-weight: 700; }
.les-head .row { gap: 6px; }
.les-head .btn { min-height: 36px; padding: 6px 12px; font-size: 0.88rem; }
dl { margin: 0; }
.term { display: grid; grid-template-columns: minmax(0, 15em) minmax(0, 1fr); gap: 4px 18px; padding: 12px 18px; border-top: 1px solid var(--rule); }
.term dt { font-weight: 700; display: flex; gap: 8px; align-items: baseline; }
.term dd { margin: 0; min-width: 0; }
.term .art { display: block; margin-top: 3px; font-size: 0.86rem; font-weight: 600; color: var(--accent); }
.dot { flex: none; width: 9px; height: 9px; border-radius: 50%; border: 1.5px solid var(--ink-soft); transform: translateY(-1px); }
.dot.k { background: var(--good); border-color: var(--good); }
.dot.n { background: var(--bad); border-color: var(--bad); }
mark { background: var(--mark); color: inherit; border-radius: 2px; }
.legend { display: flex; flex-wrap: wrap; gap: 6px 16px; font-size: 0.85rem; color: var(--ink-soft); align-items: center; }
.legend span { display: inline-flex; gap: 6px; align-items: center; }
@media (max-width: 600px) { .term { grid-template-columns: 1fr; padding: 12px 16px; } .les-head { padding: 12px 16px; } }

/* oefenen: kaart en dictee */
.stage { display: flex; flex-direction: column; gap: 14px; }
.meta { display: flex; justify-content: space-between; gap: 10px; flex-wrap: wrap; font-size: 0.88rem; color: var(--ink-soft); font-weight: 600; }
.card { position: relative; width: 100%; min-height: 260px; border: 1px solid var(--rule); border-radius: 16px; background: var(--sheet); padding: 26px 24px 22px;
  display: flex; flex-direction: column; gap: 14px; align-items: center; justify-content: center; text-align: center; box-shadow: 0 2px 10px rgba(10, 18, 36, 0.06); }
.card:hover { border-color: var(--accent); }
.card .side { font-size: 0.8rem; font-weight: 700; color: var(--accent); }
.card .front { font-size: clamp(1.35rem, 4.4vw, 1.9rem); font-weight: 800; font-stretch: 108%; line-height: 1.2; overflow-wrap: anywhere; hyphens: auto; }
.card .front.long { font-size: 1.08rem; font-weight: 500; font-stretch: 100%; line-height: 1.5; max-width: 60ch; }
.card .back { display: flex; flex-direction: column; gap: 8px; max-width: 60ch; padding-top: 14px; border-top: 1px solid var(--rule); width: 100%; }
.card .back .ans { font-size: 1.05rem; }
.card .back .ans.big { font-size: 1.4rem; font-weight: 800; font-stretch: 108%; }
.card .art { font-size: 0.9rem; font-weight: 600; color: var(--accent); }
.card .hint { font-size: 0.82rem; color: var(--ink-soft); }
.answer-row { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 10px; }
.answer-row .btn { min-height: 52px; }
.prompt { background: var(--sheet); border: 1px solid var(--rule); border-radius: 16px; padding: 22px; display: flex; flex-direction: column; gap: 12px; }
.prompt .q { font-size: 1.08rem; line-height: 1.55; }
.prompt .q.big { font-size: 1.45rem; font-weight: 800; font-stretch: 108%; }
.prompt label { font-weight: 700; font-size: 0.92rem; }
.prompt input[type=text], .prompt textarea { width: 100%; border: 1.5px solid var(--rule); background: var(--paper); border-radius: 10px; padding: 12px 14px; font-size: 1.05rem; }
.prompt textarea { min-height: 110px; resize: vertical; font-family: inherit; }
.prompt input:focus, .prompt textarea:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.fb { border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 6px; }
.fb.good { background: var(--good-soft); } .fb.good b { color: var(--good); }
.fb.bad { background: var(--bad-soft); } .fb.bad b { color: var(--bad); }
.fb.self { background: var(--sunk); }
.done { text-align: center; align-items: center; }
.score { font-size: 2.6rem; font-weight: 800; font-stretch: 116%; line-height: 1; color: var(--accent); }
.keys { font-size: 0.82rem; color: var(--ink-soft); }
@media (max-width: 480px) { .panel { padding: 16px; } .card { min-height: 220px; padding: 22px 16px 18px; } .prompt { padding: 16px; } .keys { display: none; } }
.foot { color: var(--ink-soft); font-size: 0.84rem; border-top: 1px solid var(--rule); padding-top: 16px; display: flex; flex-direction: column; gap: 6px; }
</style>
</head>
<body>
__SITEBAR__<header class="band" id="top">
<div class="band-in">
  __CRUMBS__
  <div class="title-row"><span class="plate" aria-hidden="true">__CODE__</span><div><span class="kind">Begrippen</span><h1>__HEADING__</h1></div></div>
  <p class="lead">__N__ begrippen uit de samenvattingen, per les. Lees ze in de lijst, oefen met flitskaarten of typ ze in een dictee. Kies één les, een paar weken of alles.</p>
  __TABS__
</div>
</header>
<div class="wrap">
<main id="main">
  <section class="panel" aria-labelledby="sel-title">
    <h2 id="sel-title">Kies wat je oefent</h2>
    <div>
      <div class="filter-head"><span class="filter-label" id="lbl-weeks">Weken</span><button class="linkbtn" id="weeks-all">alle weken</button><button class="linkbtn" id="weeks-none">geen</button></div>
      <div class="chips" id="week-chips" role="group" aria-labelledby="lbl-weeks"></div>
    </div>
    <div>
      <div class="filter-head"><span class="filter-label" id="lbl-parts">Onderdelen</span></div>
      <div class="chips" id="part-chips" role="group" aria-labelledby="lbl-parts"></div>
    </div>
    <p class="sel-summary" id="sel-summary" aria-live="polite"></p>
    <div class="bar" aria-hidden="true"><i id="sel-bar" style="width:0"></i></div>
  </section>

  <div class="modes" role="group" aria-label="Manier van oefenen">
    <button type="button" data-mode="lijst" aria-pressed="true">Lijst</button>
    <button type="button" data-mode="kaarten" aria-pressed="false">Flitskaarten</button>
    <button type="button" data-mode="dictee" aria-pressed="false">Dictee</button>
  </div>

  <section id="pane-lijst" class="stage" aria-label="Begrippenlijst">
    <div class="search" role="search">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      <input id="q" type="search" placeholder="Zoek een begrip, uitleg of artikel" autocomplete="off" aria-label="Zoek in de begrippen">
    </div>
    <div class="legend"><span><i class="dot k"></i>ken je</span><span><i class="dot n"></i>nog niet</span><span><i class="dot"></i>nog niet geoefend</span>
      <label class="opt"><input type="checkbox" id="only-open"> alleen wat ik nog niet ken</label></div>
    <div id="list"></div>
  </section>

  <section id="pane-kaarten" class="stage" aria-label="Flitskaarten" hidden>
    <div class="panel">
      <div class="row"><span class="filter-label">Voorkant</span>
        <div class="seg" role="group" aria-label="Voorkant van de kaart"><button type="button" data-dir="b" aria-pressed="true">Begrip</button><button type="button" data-dir="u" aria-pressed="false">Uitleg</button></div></div>
      <label class="opt"><input type="checkbox" id="k-open"> alleen wat ik nog niet ken</label>
      <div class="row"><button type="button" class="btn primary" id="k-start">Start de kaarten</button><span class="small" id="k-info"></span></div>
    </div>
    <div id="k-stage" class="stage" hidden>
      <div class="meta"><span id="k-where"></span><span id="k-count"></span></div>
      <button type="button" class="card" id="k-card" aria-live="polite"></button>
      <div class="answer-row"><button type="button" class="btn bad" id="k-no">Nog niet</button><button type="button" class="btn good" id="k-yes">Ken ik</button></div>
      <p class="keys">Spatie draait de kaart om, pijl links is "nog niet", pijl rechts is "ken ik".</p>
    </div>
    <div id="k-done" class="panel done" hidden></div>
  </section>

  <section id="pane-dictee" class="stage" aria-label="Dictee" hidden>
    <div class="panel">
      <div class="row"><span class="filter-label">Je typt</span>
        <div class="seg" role="group" aria-label="Wat typ je"><button type="button" data-dt="b" aria-pressed="true">Het begrip</button><button type="button" data-dt="u" aria-pressed="false">De uitleg</button></div></div>
      <p class="small" id="d-uitleg-info">Je ziet de uitleg en typt het begrip. Kleine typfouten rekent de dictee goed, met de juiste spelling erbij.</p>
      <label class="opt"><input type="checkbox" id="d-open"> alleen wat ik nog niet ken</label>
      <div class="row"><button type="button" class="btn primary" id="d-start">Start het dictee</button><span class="small" id="d-info"></span></div>
    </div>
    <div id="d-stage" class="stage" hidden>
      <div class="meta"><span id="d-where"></span><span id="d-count"></span></div>
      <form class="prompt" id="d-form" autocomplete="off">
        <p class="q" id="d-q"></p>
        <label for="d-in" id="d-lbl">Welk begrip is dit?</label>
        <input type="text" id="d-in" autocapitalize="off" autocorrect="off" spellcheck="false">
        <textarea id="d-ta" hidden></textarea>
        <div class="row" id="d-ask"><button type="submit" class="btn primary" id="d-check">Controleer</button><button type="button" class="btn" id="d-hint">Hint</button><button type="button" class="btn" id="d-skip">Weet ik niet</button></div>
        <div id="d-fb" class="fb" hidden></div>
        <div class="row" id="d-after" hidden></div>
      </form>
    </div>
    <div id="d-done" class="panel done" hidden></div>
  </section>
</main>
<footer class="foot">
  <p>Alle begrippen komen uit de samenvattingen van de lessen. Staat er "gangbare invulling" bij, dan stond het niet uitgeschreven op de slides; check het dan in de les of je literatuur. Wetsartikelen staan erbij zoals in de samenvatting.</p>
  <p>Wat je kent, onthoudt deze browser op dit apparaat. <button class="linkbtn" id="reset">Wis mijn voortgang voor deze selectie</button></p>
</footer>
</div>
<script type="application/json" id="data">__DATA__</script>
<script>
(function () {
  "use strict";
  var D = JSON.parse(document.getElementById("data").textContent);
  var LS = "fm-begrippen-" + D.vak;
  var $ = function (id) { return document.getElementById(id); };
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function isObj(v) { return v && typeof v === "object" && !Array.isArray(v); }
  // localStorage lezen: type controleren en terugvallen op de standaardwaarde (zelfde patroon als lsGet in de oefenpagina)
  function lsGet(fb) { try { var v = JSON.parse(localStorage.getItem(LS)); return isObj(v) ? v : fb; } catch (e) { return fb; } }
  function lsSet(v) { try { localStorage.setItem(LS, JSON.stringify(v)); } catch (e) {} }
  var store = lsGet({});
  var st = isObj(store.st) ? store.st : {};
  var LES = {}; D.lessen.forEach(function (l) { LES[l.id] = l; });
  var W = []; var P = [];
  D.lessen.forEach(function (l) { if (W.indexOf(l.week) < 0) W.push(l.week); if (P.indexOf(l.onderdeel) < 0) P.push(l.onderdeel); });
  W.sort(function (a, b) { return a - b; });
  var sel = { w: W.slice(), p: P.slice() };
  if (isObj(store.sel)) {
    if (Array.isArray(store.sel.w)) { var w = store.sel.w.filter(function (x) { return W.indexOf(x) >= 0; }); sel.w = w; }
    if (Array.isArray(store.sel.p)) { var p = store.sel.p.filter(function (x) { return P.indexOf(x) >= 0; }); if (p.length) sel.p = p; }
  }
  var opts = { dir: store.dir === "u" ? "u" : "b", dt: store.dt === "u" ? "u" : "b" };
  function save() { lsSet({ st: st, sel: sel, dir: opts.dir, dt: opts.dt }); }
  function status(id) { var s = st[id]; return isObj(s) && typeof s.k === "boolean" ? (s.k ? "k" : "n") : ""; }
  function mark(id, known) { st[id] = { k: known, t: Date.now() }; save(); }
  function inSel(x) { var l = LES[x.les]; return sel.w.indexOf(l.week) >= 0 && sel.p.indexOf(l.onderdeel) >= 0; }
  function current() { return D.items.filter(inSel); }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function lesLabel(l) { return "Week " + l.week + " · " + l.onderdeel; }
  function rangeLabel(ws) {
    ws = ws.slice().sort(function (a, b) { return a - b; }); var out = [];
    for (var i = 0; i < ws.length;) { var j = i; while (j + 1 < ws.length && ws[j + 1] === ws[j] + 1) j++; out.push(i === j ? String(ws[i]) : ws[i] + "–" + ws[j]); i = j + 1; }
    return out.join(", ");
  }
  function selLabel() {
    if (!sel.w.length) return "Geen week gekozen";
    var s = sel.w.length === W.length ? "Alle weken" : (sel.w.length === 1 ? "Week " : "Weken ") + rangeLabel(sel.w);
    if (sel.p.length !== P.length) s += " · " + P.filter(function (p) { return sel.p.indexOf(p) >= 0; }).join(", ");
    return s;
  }

  // ---------- keuzepaneel
  function chip(key, label, n, on, fn) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "chip"; b.dataset.key = key; b.setAttribute("aria-pressed", String(on));
    b.innerHTML = "<span>" + esc(label) + "</span><span class=\"n\">" + n + "</span>";
    b.setAttribute("aria-label", label + ", " + n + " begrippen");
    b.addEventListener("click", function () { fn(); save(); refresh(key); });
    return b;
  }
  function toggle(arr, v) { var i = arr.indexOf(v); if (i >= 0) arr.splice(i, 1); else arr.push(v); }
  function renderSel(focusKey) {
    var wc = $("week-chips"); wc.innerHTML = "";
    W.forEach(function (w) {
      var n = D.items.filter(function (x) { var l = LES[x.les]; return l.week === w && sel.p.indexOf(l.onderdeel) >= 0; }).length;
      wc.appendChild(chip("w" + w, "Week " + w, n, sel.w.indexOf(w) >= 0, function () { toggle(sel.w, w); }));
    });
    var pc = $("part-chips"); pc.innerHTML = "";
    P.forEach(function (p) {
      var n = D.items.filter(function (x) { var l = LES[x.les]; return l.onderdeel === p && sel.w.indexOf(l.week) >= 0; }).length;
      pc.appendChild(chip("p" + p, p, n, sel.p.indexOf(p) >= 0, function () { toggle(sel.p, p); if (!sel.p.length) sel.p = P.slice(); }));
    });
    if (focusKey) { var el = document.querySelector('.chip[data-key="' + focusKey + '"]'); if (el) el.focus(); }
    var c = current(), k = c.filter(function (x) { return status(x.id) === "k"; }).length;
    var n = c.filter(function (x) { return status(x.id) === "n"; }).length;
    $("sel-summary").textContent = selLabel() + ": " + c.length + " begrippen" + (c.length ? " · " + k + " ken je, " + n + " nog niet, " + (c.length - k - n) + " nog niet geoefend" : "");
    $("sel-bar").style.width = c.length ? (100 * k / c.length) + "%" : "0";
  }
  $("weeks-all").addEventListener("click", function () { sel.w = W.slice(); save(); refresh(); });
  $("weeks-none").addEventListener("click", function () { sel.w = []; save(); refresh(); });
  function onlyLesson(id) { var l = LES[id]; sel.w = [l.week]; sel.p = [l.onderdeel]; save(); }

  // ---------- lijst
  function norm(s) { return String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function hl(text, q) {
    var t = esc(text); if (!q) return t;
    var n = norm(text), i = n.indexOf(q); if (i < 0) return t;
    return esc(text.slice(0, i)) + "<mark>" + esc(text.slice(i, i + q.length)) + "</mark>" + esc(text.slice(i + q.length));
  }
  function renderList() {
    var q = norm($("q").value.trim()), only = $("only-open").checked;
    var c = current().filter(function (x) {
      if (only && status(x.id) === "k") return false;
      return !q || norm(x.begrip + " " + x.uitleg + " " + (x.art || "") + " " + x.ook.join(" ")).indexOf(q) >= 0;
    });
    var out = [];
    D.lessen.forEach(function (l) {
      var xs = c.filter(function (x) { return x.les === l.id; }); if (!xs.length) return;
      out.push('<section class="les" id="les-' + l.id + '"><header class="les-head"><div><small>' + esc(lesLabel(l)) + '</small><h3>' + esc(l.titel) + '</h3></div>' +
        '<div class="row"><button type="button" class="btn" data-les="' + l.id + '" data-go="kaarten">Flitskaarten</button><button type="button" class="btn" data-les="' + l.id + '" data-go="dictee">Dictee</button></div></header><dl>');
      xs.forEach(function (x) {
        var s = status(x.id);
        out.push('<div class="term"><dt><i class="dot ' + s + '" title="' + (s === "k" ? "ken je" : s === "n" ? "nog niet" : "nog niet geoefend") + '"></i><span>' + hl(x.begrip, q) + '</span></dt><dd>' +
          hl(x.uitleg, q) + (x.art ? '<span class="art">' + hl(x.art, q) + "</span>" : "") + "</dd></div>");
      });
      out.push("</dl></section>");
    });
    $("list").innerHTML = out.length ? out.join("") : '<p class="empty">' + (current().length ? "Geen begrippen gevonden met deze zoekterm of filter." : "Kies hierboven minstens één week.") + "</p>";
  }
  $("q").addEventListener("input", renderList);
  $("only-open").addEventListener("change", renderList);
  $("list").addEventListener("click", function (e) {
    var b = e.target.closest("button[data-les]"); if (!b) return;
    onlyLesson(b.dataset.les); setMode(b.dataset.go); refresh();
    (b.dataset.go === "kaarten" ? startCards : startDictee)();
    window.scrollTo({ top: $("main").offsetTop - 60 });
  });

  // ---------- modi en deeplinks (#lijst, #kaarten-w3, #dictee-w2)
  var mode = "lijst";
  function setMode(m) {
    mode = m;
    Array.prototype.forEach.call(document.querySelectorAll(".modes button"), function (b) { b.setAttribute("aria-pressed", String(b.dataset.mode === m)); });
    ["lijst", "kaarten", "dictee"].forEach(function (k) { $("pane-" + k).hidden = k !== m; });
    if (location.hash.replace(/-w\d+$/, "") !== "#" + m) history.replaceState(null, "", "#" + m);
  }
  Array.prototype.forEach.call(document.querySelectorAll(".modes button"), function (b) { b.addEventListener("click", function () { setMode(b.dataset.mode); refresh(); }); });
  function fromHash() {
    var m = /^#(lijst|kaarten|dictee)(?:-w(\d+))?$/.exec(location.hash);
    if (!m) return;
    if (m[2] && W.indexOf(+m[2]) >= 0) { sel.w = [+m[2]]; sel.p = P.slice(); save(); }
    setMode(m[1]);
  }

  // ---------- gedeelde stapel voor kaarten en dictee
  function pool(onlyOpen) { var c = current(); if (onlyOpen) c = c.filter(function (x) { return status(x.id) !== "k"; }); return shuffle(c); }
  function infoLine(id, onlyOpen) { var n = pool(onlyOpen).length; $(id).textContent = n ? n + " begrippen in deze ronde" : (current().length ? "Je kent alles in deze selectie." : "Kies hierboven minstens één week."); return n; }
  function segInit(attr, key) {
    Array.prototype.forEach.call(document.querySelectorAll("[data-" + attr + "]"), function (b) {
      b.setAttribute("aria-pressed", String(b.dataset[attr] === opts[key]));
      b.addEventListener("click", function () { opts[key] = b.dataset[attr]; save(); segInit2(attr, key); if (key === "dt") dtInfo(); });
    });
  }
  function segInit2(attr, key) { Array.prototype.forEach.call(document.querySelectorAll("[data-" + attr + "]"), function (b) { b.setAttribute("aria-pressed", String(b.dataset[attr] === opts[key])); }); }
  segInit("dir", "dir"); segInit("dt", "dt");

  // masker: het begrip (en zijn andere namen) uit de uitleg halen, anders verklapt de vraag het antwoord
  function reEsc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
  function masked(x) {
    var t = x.uitleg;
    [x.begrip].concat(x.ook).filter(function (s) { return s.length >= 3; }).sort(function (a, b) { return b.length - a.length; }).forEach(function (s) {
      var re; try { re = new RegExp("(?<![\\p{L}\\p{N}])" + reEsc(s) + "(?![\\p{L}\\p{N}])", "giu"); } catch (e) { re = new RegExp(reEsc(s), "gi"); }
      t = t.replace(re, "…");
    });
    return t;
  }

  // de ronde in beeld brengen (op een telefoon staat het keuzepaneel erboven)
  function into(id) { var el = $(id), top = el.getBoundingClientRect().top + scrollY - 64; if (Math.abs(top - scrollY) > 40) window.scrollTo({ top: top }); }

  // ---------- flitskaarten
  var K = null;
  function startCards() {
    var list = pool($("k-open").checked);
    $("k-done").hidden = true;
    if (!list.length) { infoLine("k-info", $("k-open").checked); $("k-stage").hidden = true; return; }
    K = { list: list, i: 0, flipped: false, yes: 0, miss: [] };
    $("k-stage").hidden = false; showCard(); into("k-stage"); $("k-card").focus({ preventScroll: true });
  }
  function showCard() {
    var x = K.list[K.i], l = LES[x.les], b = opts.dir === "b";
    $("k-where").textContent = lesLabel(l) + ": " + l.titel;
    $("k-count").textContent = (K.i + 1) + " van " + K.list.length;
    var front = b ? '<span class="side">Begrip</span><span class="front">' + esc(x.begrip) + "</span>"
                  : '<span class="side">Uitleg</span><span class="front long">' + esc(masked(x)) + "</span>";
    var back = b ? '<span class="ans">' + esc(x.uitleg) + "</span>" : '<span class="ans big">' + esc(x.begrip) + "</span>";
    if (x.art) back += '<span class="art">' + esc(x.art) + "</span>";
    $("k-card").innerHTML = front + (K.flipped ? '<div class="back">' + back + "</div>" : '<span class="hint">Tik om om te draaien</span>');
    $("k-card").setAttribute("aria-label", K.flipped ? "Kaart, achterkant zichtbaar" : "Kaart, tik om om te draaien");
  }
  function answerCard(known) {
    if (!K) return;
    var x = K.list[K.i]; mark(x.id, known);
    if (known) K.yes++; else K.miss.push(x);
    K.i++; K.flipped = false;
    if (K.i >= K.list.length) return endCards();
    showCard(); renderSel();
  }
  function endCards() {
    $("k-stage").hidden = true; var d = $("k-done"); d.hidden = false;
    d.innerHTML = '<span class="score">' + K.yes + " / " + K.list.length + '</span><p>' + (K.miss.length ? K.miss.length + " begrippen ken je nog niet. Oefen die meteen nog een keer." : "Alles gekend in deze ronde.") + "</p>" +
      '<div class="row" style="justify-content:center">' + (K.miss.length ? '<button type="button" class="btn primary" id="k-again">Oefen de ' + K.miss.length + " die je nog niet kent</button>" : "") +
      '<button type="button" class="btn" id="k-new">Nieuwe ronde</button></div>';
    var miss = K.miss; K = null; refresh();
    if (miss.length) $("k-again").addEventListener("click", function () { K = { list: shuffle(miss), i: 0, flipped: false, yes: 0, miss: [] }; d.hidden = true; $("k-stage").hidden = false; showCard(); $("k-card").focus(); });
    $("k-new").addEventListener("click", startCards);
    ($("k-again") || $("k-new")).focus();
  }
  $("k-start").addEventListener("click", startCards);
  $("k-open").addEventListener("change", function () { infoLine("k-info", this.checked); });
  $("k-card").addEventListener("click", function () { if (!K) return; K.flipped = !K.flipped; showCard(); });
  $("k-yes").addEventListener("click", function () { answerCard(true); });
  $("k-no").addEventListener("click", function () { answerCard(false); });
  document.addEventListener("keydown", function (e) {
    if (mode !== "kaarten" || !K || $("k-stage").hidden || e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.target.tagName; if (t === "INPUT" || t === "TEXTAREA" || t === "SELECT") return;
    if (e.key === " " && e.target !== $("k-card")) { e.preventDefault(); K.flipped = !K.flipped; showCard(); }
    else if (e.key === "ArrowRight") { e.preventDefault(); answerCard(true); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); answerCard(false); }
  });

  // ---------- dictee
  function simple(s) { return norm(s).replace(/\(.*?\)/g, " ").replace(/^(de|het|een)\s+/, "").replace(/[^a-z0-9]+/g, ""); }
  function lev(a, b) {
    var m = a.length, n = b.length, d = []; for (var i = 0; i <= m; i++) { d[i] = [i]; } for (var j = 1; j <= n; j++) d[0][j] = j;
    for (i = 1; i <= m; i++) for (j = 1; j <= n; j++) d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    return d[m][n];
  }
  function judge(x, ans) {
    var a = simple(ans); if (!a) return "leeg";
    var names = [x.begrip].concat(x.ook).map(simple).filter(Boolean);
    if (names.indexOf(a) >= 0) return "goed";
    for (var i = 0; i < names.length; i++) { var t = names[i], max = t.length >= 10 ? 2 : t.length >= 5 ? 1 : 0; if (max && lev(a, t) <= max) return "bijna"; }
    return "fout";
  }
  var Dc = null;
  function dtInfo() {
    $("d-uitleg-info").textContent = opts.dt === "b" ? "Je ziet de uitleg en typt het begrip. Kleine typfouten rekent de dictee goed, met de juiste spelling erbij."
      : "Je ziet het begrip en schrijft de uitleg in je eigen woorden. Daarna vergelijk je met de samenvatting en kijk je zelf na.";
  }
  function startDictee() {
    var list = pool($("d-open").checked);
    $("d-done").hidden = true;
    if (!list.length) { infoLine("d-info", $("d-open").checked); $("d-stage").hidden = true; return; }
    Dc = { list: list, i: 0, good: 0, miss: [], hint: 0 };
    $("d-stage").hidden = false; showQ(); into("d-stage");
  }
  function showQ() {
    var x = Dc.list[Dc.i], l = LES[x.les], typeB = opts.dt === "b";
    Dc.hint = 0; Dc.answered = false;
    $("d-where").textContent = lesLabel(l) + ": " + l.titel;
    $("d-count").textContent = (Dc.i + 1) + " van " + Dc.list.length + " · " + Dc.good + " goed";
    $("d-q").className = typeB ? "q" : "q big";
    $("d-q").textContent = typeB ? masked(x) : x.begrip;
    $("d-lbl").textContent = typeB ? "Welk begrip is dit?" : "Wat betekent dit? Schrijf het in je eigen woorden.";
    $("d-in").hidden = !typeB; $("d-ta").hidden = typeB; $("d-hint").hidden = !typeB;
    $("d-lbl").setAttribute("for", typeB ? "d-in" : "d-ta");
    $("d-in").value = ""; $("d-ta").value = ""; $("d-in").disabled = false; $("d-ta").disabled = false;
    $("d-in").placeholder = "";
    $("d-fb").hidden = true; $("d-after").hidden = true; $("d-ask").hidden = false;
    (typeB ? $("d-in") : $("d-ta")).focus({ preventScroll: true });
  }
  function feedback(kind, html, buttons) {
    var fb = $("d-fb"); fb.className = "fb " + kind; fb.innerHTML = html; fb.hidden = false;
    $("d-ask").hidden = true; $("d-in").disabled = true; $("d-ta").disabled = true;
    var a = $("d-after"); a.innerHTML = ""; a.hidden = false;
    buttons.forEach(function (b) {
      var el = document.createElement("button"); el.type = "button"; el.className = "btn" + (b.cls ? " " + b.cls : ""); el.textContent = b.label;
      el.addEventListener("click", b.fn); a.appendChild(el);
    });
    a.firstChild.focus({ preventScroll: true });
  }
  function solution(x) { return "<span><strong>" + esc(x.begrip) + "</strong>" + (x.ook.length ? " <small>(ook: " + esc(x.ook.join(", ")) + ")</small>" : "") + "</span>" + (x.art ? '<span class="small">' + esc(x.art) + "</span>" : ""); }
  function record(x, ok) { mark(x.id, ok); if (ok) Dc.good++; else Dc.miss.push(x); }
  function nextQ() { Dc.i++; if (Dc.i >= Dc.list.length) return endDictee(); showQ(); renderSel(); }
  var NEXT = function () { return { label: Dc && Dc.i + 1 >= Dc.list.length ? "Bekijk je score" : "Volgende", cls: "primary", fn: nextQ }; };
  $("d-form").addEventListener("submit", function (e) {
    e.preventDefault(); if (!Dc || Dc.answered) return;
    var x = Dc.list[Dc.i];
    if (opts.dt === "u") {
      if (!$("d-ta").value.trim()) { $("d-ta").focus(); return; }
      Dc.answered = true;
      feedback("self", "<b>Vergelijk met de samenvatting</b><span>" + esc(x.uitleg) + "</span>" + (x.art ? '<span class="small">' + esc(x.art) + "</span>" : "") + "<span>Had je de kern goed?</span>",
        [{ label: "Goed", cls: "good", fn: function () { record(x, true); nextQ(); } }, { label: "Nog niet", cls: "bad", fn: function () { record(x, false); nextQ(); } }]);
      return;
    }
    var r = judge(x, $("d-in").value);
    if (r === "leeg") { $("d-in").focus(); return; }
    Dc.answered = true;
    if (r === "goed" || r === "bijna") {
      record(x, true);
      feedback("good", "<b>" + (r === "goed" ? "Goed" : "Goed, let op de spelling") + "</b>" + solution(x), [NEXT()]);
    } else {
      record(x, false);
      feedback("bad", "<b>Niet goed</b><span>Jij typte: " + esc($("d-in").value) + "</span>" + solution(x),
        [NEXT(), { label: "Toch goed rekenen", fn: function () { Dc.miss.pop(); Dc.good++; mark(x.id, true); nextQ(); } }]);
    }
  });
  $("d-hint").addEventListener("click", function () {
    if (!Dc) return; var t = Dc.list[Dc.i].begrip; Dc.hint = Math.min(Dc.hint + 1, Math.max(1, t.length - 1));
    $("d-in").placeholder = t.slice(0, Dc.hint) + t.slice(Dc.hint).replace(/[^\s\-\/]/g, "_");
    $("d-in").focus();
  });
  $("d-skip").addEventListener("click", function () {
    if (!Dc || Dc.answered) return; var x = Dc.list[Dc.i]; Dc.answered = true; record(x, false);
    feedback("bad", "<b>Het antwoord</b>" + solution(x), [NEXT()]);
  });
  function endDictee() {
    $("d-stage").hidden = true; var d = $("d-done"); d.hidden = false;
    d.innerHTML = '<span class="score">' + Dc.good + " / " + Dc.list.length + '</span><p>' + (Dc.miss.length ? "Dit wist je nog niet: " + Dc.miss.map(function (x) { return esc(x.begrip); }).join(", ") + "." : "Alles goed in deze ronde.") + "</p>" +
      '<div class="row" style="justify-content:center">' + (Dc.miss.length ? '<button type="button" class="btn primary" id="d-again">Oefen de ' + Dc.miss.length + " fouten opnieuw</button>" : "") +
      '<button type="button" class="btn" id="d-new">Nieuw dictee</button></div>';
    var miss = Dc.miss; Dc = null; refresh();
    if (miss.length) $("d-again").addEventListener("click", function () { Dc = { list: shuffle(miss), i: 0, good: 0, miss: [], hint: 0 }; d.hidden = true; $("d-stage").hidden = false; showQ(); });
    $("d-new").addEventListener("click", startDictee);
    ($("d-again") || $("d-new")).focus();
  }
  $("d-start").addEventListener("click", startDictee);
  $("d-open").addEventListener("change", function () { infoLine("d-info", this.checked); });

  $("reset").addEventListener("click", function () { current().forEach(function (x) { delete st[x.id]; }); save(); refresh(); });

  // selectie veranderd: lopende ronde stoppen, alles opnieuw tekenen
  function refresh(focusKey) {
    renderSel(focusKey); renderList();
    if (typeof focusKey === "string") { K = null; Dc = null; $("k-stage").hidden = true; $("d-stage").hidden = true; $("k-done").hidden = true; $("d-done").hidden = true; }
    infoLine("k-info", $("k-open").checked); infoLine("d-info", $("d-open").checked);
  }
  window.addEventListener("hashchange", function () { fromHash(); refresh(""); });
  dtInfo(); fromHash(); refresh();
})();
</script>
__SITEFOOT__
__BAR_JS__
</body>
</html>
"""


def build():
    for slug, c in VAKKEN.items():
        lessen, items = load(slug)
        data = dict(vak=slug, lessen=[dict(id=l["id"], week=l["week"], onderdeel=l["onderdeel"], titel=l["titel"]) for l in lessen],
                    items=[dict(id=x["id"], les=x["les"], begrip=x["begrip"], uitleg=x["uitleg"], art=x["art"], ook=x["ook"]) for x in items])
        js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
        a1, a2, a3, a4 = c["accent"]
        b1, b2 = c["band"]
        page = PAGE
        for k, v in dict(HEADING=html.escape(c["heading"]), CODE=c["code"], N=str(len(items)), DATA=js,
                         SITEBAR=sitenav.bar("../../", slug, "begrip"), TABS=sitenav.tabs("../../", slug, "begrip"),
                         CRUMBS=sitenav.crumbs("../../", slug, "Begrippen"), SITEFOOT=sitenav.footer("../../"),
                         TABS_CSS=sitenav.TABS_CSS, BAR_CSS=sitenav.bar_css(), BAR_JS=sitenav.BAR_JS,
                         A1=a1, A2=a2, A3=a3, A4=a4, B1=b1, B2=b2).items():
            page = page.replace(f"__{k}__", v)
        assert "__" not in page.replace("__proto__", ""), slug
        os.makedirs(os.path.join(OUT, slug), exist_ok=True)
        open(os.path.join(OUT, slug, "index.html"), "w", encoding="utf-8").write(page)
        print("begrippen", slug, len(items), "begrippen in", len(lessen), "lessen,", len(page) // 1024, "KB")


if __name__ == "__main__":
    build()
