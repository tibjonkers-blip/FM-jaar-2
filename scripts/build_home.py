"""Bouwt de startpagina site/index.html en site/favicon.svg, met de aantallen uit de gebouwde vakpagina's."""
import json, os
import sitenav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")

def eind_txt(n):
    return "" if not n else (" en eindtoets" if n == 1 else f" en {n} eindtoetsen")

def counts(slug):
    if not os.path.exists(os.path.join(SITE, slug, "vragen.json")):
        return None
    v = json.load(open(os.path.join(SITE, slug, "vragen.json"), encoding="utf-8"))
    t = json.load(open(os.path.join(SITE, slug, "toetsen.json"), encoding="utf-8"))
    weken = t["weken"]
    return dict(vragen=len(v["vragen"]), lessen=len(v["lessen"]), weken=len(weken), toetsen=len(weken) * 3,
                items=len(t["items"]), eind=len(t.get("eindtoetsen", [])))

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1d2b4f"/><path d="M18 17h18M18 17v30M18 31h14" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none"/><rect x="10" y="54" width="15" height="4" fill="#0b9ab3"/><rect x="25" y="54" width="15" height="4" fill="#c23c8a"/><rect x="40" y="54" width="14" height="4" fill="#d07a14"/></svg>
"""

PAGE = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Studieplek FM periode 2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Samenvattingen, oefenvragen per les en weektoetsen voor Inkoop en recht, HRM en het praktijkproject.">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap">
<style>
/* Bewegwijzering zoals in een gebouw: een donkerblauwe lobbyband, daaronder een streep in de drie zonekleuren en per vak
   een zone met een eigen signaalkleur, een zonebordje (IR, HRM, BM) en drie deuren: lezen, oefenen, toetsen. */
:root {
  --paper: #eef1f6; --sheet: #ffffff; --sunk: #e4e9f1; --ink: #16202f; --ink-soft: #5a6577; --rule: #d9dfe8;
  --lobby: #1d2b4f; --on-band: #ffffff;
  --teal: #0b6f82; --teal-soft: #dff0f3; --teal-band: #0b6f82;
  --plum: #9a2d6c; --plum-soft: #f6e4ef; --plum-band: #8f2a65;
  --ochre: #9a520a; --ochre-soft: #fbecd8; --ochre-band: #9a520a;
  --good: #1b7a46;
  --font: "Archivo", "Segoe UI", system-ui, sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850; --lobby: #1f3160;
    --teal: #63cfe2; --teal-soft: #123447; --teal-band: #0d5e6e; --plum: #f095c9; --plum-soft: #3a1a3a; --plum-band: #7a2457;
    --ochre: #f5b65e; --ochre-soft: #3a2b1c; --ochre-band: #8a4a0a; --good: #6fd6a0;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850; --lobby: #1f3160;
  --teal: #63cfe2; --teal-soft: #123447; --teal-band: #0d5e6e; --plum: #f095c9; --plum-soft: #3a1a3a; --plum-band: #7a2457;
  --ochre: #f5b65e; --ochre-soft: #3a2b1c; --ochre-band: #8a4a0a; --good: #6fd6a0;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
body { margin: 0; padding: 0; background: var(--paper); color: var(--ink); font-family: var(--font); font-size: 16px; line-height: 1.55; font-variant-numeric: tabular-nums; }
.in { width: 100%; max-width: 1080px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
h1, h2 { margin: 0; line-height: 1.08; text-wrap: balance; font-stretch: 116%; }
h1 { font-size: clamp(2.2rem, 6vw, 3.6rem); font-weight: 800; letter-spacing: -0.015em; }
h2 { font-size: 1.45rem; font-weight: 800; }
p { margin: 0; }
a { color: inherit; }
:focus-visible { outline: 2px solid var(--ink); outline-offset: 2px; }

/* lobbyband */
.lobby { background: var(--lobby); color: var(--on-band); }
.lobby .in { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 20px 32px; align-items: end; padding-block: 34px 40px; }
.intro { display: flex; flex-direction: column; gap: 12px; min-width: 0; }
.where { font-size: 0.92rem; color: rgba(255, 255, 255, 0.75); }
.lead { color: rgba(255, 255, 255, 0.86); max-width: 58ch; font-size: 1.02rem; }
.clock { background: #fff; color: #16202f; border-radius: 12px; padding: 14px 20px 16px; display: flex; flex-direction: column; gap: 2px; min-width: 210px; }
.clock strong { font-weight: 800; font-stretch: 120%; font-size: 3rem; line-height: 1; letter-spacing: -0.01em; color: var(--lobby); }
:root[data-theme="dark"] .clock strong { color: #1d2b4f; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .clock strong { color: #1d2b4f; } }
.clock span { font-size: 0.88rem; color: #5a6577; }
.clock #days-l { color: #16202f; font-weight: 600; }
.stripe { display: grid; grid-template-columns: repeat(3, 1fr); height: 6px; }
.stripe i:nth-child(1) { background: var(--teal-band); } .stripe i:nth-child(2) { background: var(--plum-band); } .stripe i:nth-child(3) { background: var(--ochre-band); }
@media (max-width: 640px) {
  .lobby .in { grid-template-columns: 1fr; padding-block: 26px 30px; }
  .clock { flex-direction: row; align-items: baseline; gap: 10px; flex-wrap: wrap; min-width: 0; }
  .clock strong { font-size: 2.2rem; order: -2; } #days-l { order: -1; } .clock span:first-child { flex-basis: 100%; }
}

main.in { display: flex; flex-direction: column; gap: 36px; padding-block: 28px 64px; }

/* zones */
.grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; align-items: start; }
@media (max-width: 920px) { .grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 620px) { .grid { grid-template-columns: 1fr; } }
.vak { background: var(--sheet); border: 1px solid var(--rule); border-radius: 14px; overflow: hidden; display: flex; flex-direction: column; min-width: 0; }
.vak-head { padding: 18px 20px 20px; background: var(--c-band); color: #fff; display: flex; flex-direction: column; gap: 8px; }
.vak-top { display: flex; align-items: center; justify-content: space-between; gap: 12px; }
.plate { min-width: 46px; height: 46px; padding-inline: 8px; border-radius: 9px; background: #fff; color: var(--c-band); display: grid; place-items: center;
  font-weight: 800; font-stretch: 122%; font-size: 0.98rem; letter-spacing: 0.02em; }
.exam { font-size: 0.86rem; font-weight: 600; color: rgba(255, 255, 255, 0.9); text-align: right; }
.vak-head h2 { margin-top: 6px; }
.vak-head p { font-size: 0.92rem; color: rgba(255, 255, 255, 0.86); }
.doors { display: flex; flex-direction: column; padding: 8px; gap: 2px; }
.door { display: grid; grid-template-columns: 38px minmax(0, 1fr) auto; gap: 2px 12px; align-items: center; padding: 11px 10px; border-radius: 10px; text-decoration: none; }
.door:hover { background: var(--c-soft); }
.door .ic { grid-row: span 2; width: 38px; height: 38px; border-radius: 9px; display: grid; place-items: center; background: var(--c-soft); color: var(--c); }
.door:hover .ic { background: var(--c-band); color: #fff; }
.door .ic svg { width: 19px; height: 19px; }
.door b { font-weight: 700; }
.door small { grid-column: 2; font-size: 0.84rem; color: var(--ink-soft); }
.door .arr { grid-row: span 2; grid-column: 3; color: var(--ink-soft); display: grid; }
.door .arr svg { width: 18px; height: 18px; }
.door:hover .arr { color: var(--c); }
.door .ext { font-size: 0.8em; color: var(--ink-soft); }
.subhead { font-size: 0.86rem; color: var(--ink-soft); font-weight: 700; margin: 6px 18px 0; padding-top: 14px; border-top: 1px solid var(--rule); }
.prog { grid-column: 2; display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: var(--good); font-weight: 600; }
.prog i { flex: 1; max-width: 120px; height: 4px; border-radius: 2px; background: var(--sunk); overflow: hidden; }
.prog i::after { content: ""; display: block; height: 100%; width: var(--p); background: var(--good); }
.teal { --c: var(--teal); --c-soft: var(--teal-soft); --c-band: var(--teal-band); }
.plum { --c: var(--plum); --c-soft: var(--plum-soft); --c-band: var(--plum-band); }
.ochre { --c: var(--ochre); --c-soft: var(--ochre-soft); --c-band: var(--ochre-band); }

/* werkwijze: echt drie stappen na elkaar */
.how { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; }
@media (max-width: 760px) { .how { grid-template-columns: 1fr; } }
.how div { display: grid; grid-template-columns: 34px minmax(0, 1fr); gap: 2px 12px; align-items: start; }
.how .nr { grid-row: span 2; width: 34px; height: 34px; border-radius: 50%; background: var(--lobby); color: #fff; display: grid; place-items: center; font-weight: 800; font-stretch: 116%; }
.how b { font-size: 1.05rem; font-stretch: 108%; }
.how p { font-size: 0.93rem; color: var(--ink-soft); }
__BAR_CSS__
footer { font-size: 0.86rem; color: var(--ink-soft); border-top: 1px solid var(--rule); padding-top: 16px; display: flex; flex-direction: column; gap: 4px; }
</style>
</head>
<body>
__SITEBAR__<header class="lobby">
  <div class="in">
    <div class="intro">
      <span class="where">Facility Management, jaar 2</span>
      <h1>Studieplek periode 2</h1>
      <p class="lead">Lees per week de samenvatting, oefen dezelfde dag de vragen van die les en maak aan het eind van de week een weektoets. Zo leer je vanaf de eerste les voor de toetsweken.</p>
    </div>
    <div class="clock" aria-live="polite"><span>Toetsperiode 11 t/m 22 januari 2027</span><strong id="days">–</strong><span id="days-l">dagen te gaan</span></div>
  </div>
</header>
<div class="stripe" aria-hidden="true"><i></i><i></i><i></i></div>
<main class="in" id="main">
  <div class="grid">
    <section class="vak teal" aria-labelledby="v1">
      <div class="vak-head"><div class="vak-top"><span class="plate" aria-hidden="true">IR</span><span class="exam">Schriftelijk casustentamen</span></div><h2 id="v1">Inkoop en recht</h2><p>In ANS, inkoop en recht elk 50%. De helft van de inkooppunten is voor toepassen.</p></div>
      <nav class="doors">
        __DOOR_SAM_IR__
        <a class="door" href="inkoop-recht/#oefenen">__IC_Q__<b>Oefenvragen per les</b><small>__IR_VRAGEN__ vragen, met herhaal- en foutenronde</small><span class="prog" id="p-ir-q" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>
        <a class="door" href="inkoop-recht/#toetsen">__IC_T__<b>Weektoetsen</b><small>__IR_TOETSEN__ toetsen (A, B, C per week), mix, proeftentamen__IR_EIND__</small><span class="prog" id="p-ir-t" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>
      </nav>
    </section>
    <section class="vak plum" aria-labelledby="v2">
      <div class="vak-head"><div class="vak-top"><span class="plate" aria-hidden="true">HRM</span><span class="exam">Mondeling, 30 minuten</span></div><h2 id="v2">HRM</h2><p>Gesprek met een acteur, vier HRM-vragen en vier arbeidsrechtvragen over de hele periode.</p></div>
      <nav class="doors">
        __DOOR_SAM_HRM__
        <a class="door" href="hrm/#oefenen">__IC_Q__<b>Oefenvragen per les</b><small>__HRM_VRAGEN__ vragen, met herhaal- en foutenronde</small><span class="prog" id="p-hrm-q" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>
        <a class="door" href="hrm/#toetsen">__IC_T__<b>Weektoetsen</b><small>__HRM_TOETSEN__ toetsen (A, B, C per week), mix, proefmondeling__HRM_EIND__</small><span class="prog" id="p-hrm-t" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>
      </nav>
    </section>
    <section class="vak ochre" aria-labelledby="v3">
      <div class="vak-head"><div class="vak-top"><span class="plate" aria-hidden="true">BM</span><span class="exam">Presentatie en portfolio</span></div><h2 id="v3">Business management</h2><p>Praktijkproject: de adviespresentatie (30 min plus 15 min vragen) telt 100%, het portfolio moet voldoende zijn. Plus de casustoetsen bedrijfskunde uit periode 1.</p></div>
      <nav class="doors">
        __DOOR_SAM_PP__
        __DOORS_PP__
        <a class="door" href="https://claude.ai/artifact/MNHrxykYerRjrc76rQu4Qg" target="_blank" rel="noopener">__IC_L__<b>Logboek portfolio <span class="ext">↗</span></b><small>Staat alleen in je Claude-document, niet op deze site</small><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>
      </nav>
      __BK__
    </section>
  </div>

  <section class="how" aria-label="Zo werk je ermee">
    <div><span class="nr">1</span><b>Voor de les</b><p>Lees de samenvatting van die week. Gebruik de zoekbalk om een begrip of artikel snel terug te vinden.</p></div>
    <div><span class="nr">2</span><b>Na de les</b><p>Maak dezelfde dag de oefenvragen van die les. Fout beantwoorde vragen komen terug in de foutenronde.</p></div>
    <div><span class="nr">3</span><b>Eind van de week</b><p>Maak versie A van de weektoets. Twijfel je nog, doe dan later B of C; die hebben andere vragen.</p></div>
  </section>

  <footer>
    <span>Je voortgang en toetscijfers worden alleen in deze browser bewaard. Op een andere telefoon of laptop begin je opnieuw.</span>
    <span>Deze site is openbaar. Persoonlijke dingen, zoals je logboek, staan er bewust niet op.</span>
  </footer>
</main>
<script>
(function () {
  var d = Math.ceil((new Date(2027, 0, 11) - new Date().setHours(0, 0, 0, 0)) / 864e5);
  var end = new Date(2027, 0, 23) - new Date();
  document.getElementById("days").textContent = d > 0 ? d : (end > 0 ? "nu" : "klaar");
  document.getElementById("days-l").textContent = d > 1 ? "dagen te gaan" : d === 1 ? "dag te gaan" : (end > 0 ? "de toetsperiode loopt" : "de toetsperiode is voorbij");
  function get(k) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : null; } catch (e) { return null; } }
  function show(id, n, tot, word) {
    if (!n) return;
    var el = document.getElementById(id); if (!el) return;
    el.innerHTML = "<i style=\\"--p:" + Math.min(100, Math.round(n / tot * 100)) + "%\\"></i>" + n + " van " + tot + " " + word;
    el.hidden = false;
  }
  __PROG__.forEach(function (v) {
    var p = get(v[1]) || {}, t = get(v[1] + ":toetsen") || {};
    var goed = Object.keys(p).filter(function (k) { return p[k] && p[k].status === "goed"; }).length;
    var gemaakt = Object.keys(t).filter(function (k) { return /^w\\d+-[ABC]$/.test(k) && t[k] && (t[k].laatste || t[k].laatsteCijfer != null); }).length;
    show("p-" + v[0] + "-q", goed, v[2], "goed");
    show("p-" + v[0] + "-t", gemaakt, v[3], "gemaakt");
  });
})();
</script>
__BAR_JS__
</body>
</html>
"""

ICONS = {
    "S": '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/><path d="M9 8h7M9 12h5"/></svg></span>',
    "Q": '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6v.6"/><path d="M12 17.5h.01"/></svg></span>',
    "T": '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 8l1.5 1.5L13 7M9 14l1.5 1.5L13 13"/><path d="M15 8.5h1M15 14.5h1"/></svg></span>',
    "C": '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h18v13H3z"/><path d="M8 7V4h8v3"/><path d="M3 12h18"/></svg></span>',
    "L": '<span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/></svg></span>',
}

def door_sam(slug, small):
    return (f'<a class="door" href="samenvattingen/{slug}/">{ICONS["S"]}<b>Samenvattingen</b>'
            f'<small>{small}</small><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>')

def build():
    ir, hrm, pp = counts("inkoop-recht"), counts("hrm"), counts("praktijkproject")
    prog = [["ir", "fm-quiz-inkoop-recht", ir["vragen"], ir["toetsen"]], ["hrm", "fm-quiz-hrm", hrm["vragen"], hrm["toetsen"]]]
    doors_pp = ""
    if pp:
        prog.append(["pp", "fm-quiz-praktijkproject", pp["vragen"], pp["toetsen"]])
        doors_pp = (f'<a class="door" href="praktijkproject/#oefenen">{ICONS["Q"]}<b>Oefenvragen per les</b><small>{pp["vragen"]} vragen over de modellen en de adviespresentatie</small><span class="prog" id="p-pp-q" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>\n'
                    f'        <a class="door" href="praktijkproject/#toetsen">{ICONS["T"]}<b>Weektoetsen</b><small>{pp["toetsen"]} toetsen (A, B, C per week), mix{eind_txt(pp["eind"])}</small><span class="prog" id="p-pp-t" hidden></span><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>')
    import build_bedrijfskunde
    bk = build_bedrijfskunde.counts()
    bk_doors = "".join(
        f'\n        <a class="door" href="bedrijfskunde/{slug}/">{ICONS["C"]}<b>{c["titel"]}</b><small>{c["open"]} casusvragen en {c["mc"]} meerkeuzevragen recht</small><span class="arr"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg></span></a>'
        for slug, c in bk.items())
    vals = dict(
        SITEBAR=sitenav.bar("", None, "home"), BAR_CSS=sitenav.bar_css(1080), BAR_JS=sitenav.BAR_JS,
        PROG=json.dumps(prog), DOORS_PP=doors_pp, IR_EIND=eind_txt(ir["eind"]), HRM_EIND=eind_txt(hrm["eind"]),
        BK=f'<p class="subhead">Casustoetsen bedrijfskunde, periode 1</p>\n      <nav class="doors">{bk_doors}\n      </nav>',
        IR_VRAGEN=ir["vragen"], IR_TOETSEN=ir["toetsen"], HRM_VRAGEN=hrm["vragen"], HRM_TOETSEN=hrm["toetsen"],
        IC_Q=ICONS["Q"], IC_T=ICONS["T"], IC_L=ICONS["L"],
        DOOR_SAM_IR=door_sam("inkoop-recht", "Week 1 t/m 7, inkoop en recht per les"),
        DOOR_SAM_HRM=door_sam("hrm", "Week 1 t/m 7: theorie, arbeidsrecht en gespreksvoering"),
        DOOR_SAM_PP=door_sam("praktijkproject", "Modellen per week, adviespresentatie en portfoliotips"),
    )
    page = PAGE
    for k, v in vals.items():
        page = page.replace(f"__{k}__", str(v))
    assert "__" not in page, page[page.index("__") - 40: page.index("__") + 40]
    open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(page)
    open(os.path.join(SITE, "favicon.svg"), "w", encoding="utf-8").write(FAVICON)
    print("startpagina:", ir, hrm)

if __name__ == "__main__":
    build()
