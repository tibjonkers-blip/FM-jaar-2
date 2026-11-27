"""Gedeelde navigatie van de studieplek, gebruikt door alle bouwscripts.

- bar():   de vaste wegwijzerbalk bovenaan elke pagina: Home, de drie vakken (bordjes IR, HRM, BM) en een menu met alle pagina's.
- tabs():  de tabbladen op de zoneband, op elke pagina van een vak dezelfde: Samenvatting, Oefenen, Weektoetsen (en Casustoetsen bij BM,
           Wetsartikelen bij IR en HRM).
- crumbs(): kruimelpad boven de titel van een vakpagina (Home / vak / onderdeel).
- footer(): voettekst onderaan elke pagina met alle onderdelen per vak.
- BAR_CSS (balk, menu en voettekst), TABS_CSS (kop van een vakpagina plus tabbladen), BAR_JS. De Claude-artifactversie krijgt alleen TABS_CSS.
  Kleuren komen uit de tokens van de pagina zelf (--accent, --ink, --sheet, ...), zodat kop en tabbladen op elke pagina hetzelfde zijn.

Elke pagina geeft `root` mee: het relatieve pad naar de startpagina ("" op de startpagina, "../" op een vakpagina, "../../" daaronder).
"""

ZONES = [
    dict(slug="inkoop-recht", code="IR", naam="Inkoop en recht", cls="ir"),
    dict(slug="hrm", code="HRM", naam="HRM", cls="hrm"),
    dict(slug="praktijkproject", code="BM", naam="Business management", cls="bm"),
]
CASUS = [("waalhop", "Waalhop"), ("heidezoom", "Heidezoom")]
ARTIKELEN = ("inkoop-recht", "hrm")  # vakken met een lijst wetsartikelen (/artikelen/<vak>/, build_artikelen.py)

HOME_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 11.5 12 4l8 7.5"/><path d="M6.5 10v9.5h11V10"/><path d="M10 19.5v-5h4v5"/></svg>'
MENU_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def bar(root, zone=None, kind="home"):
    """kind: 'home', 'oefen' (vakpagina), 'sam' (samenvatting) of 'casus'. zone: slug van het vak waar je bent."""
    def zone_href(z):
        if kind == "sam":
            return f"{root}samenvattingen/{z['slug']}/"
        return f"{root}{z['slug']}/"
    out = ['<a class="skip" href="#main">Naar de inhoud</a>',
           '<header class="sitebar" id="sitebar"><div class="sb-in">']
    cur = ' aria-current="page"' if kind == "home" else ""
    out.append(f'<a class="sb-home" href="{root or "./"}"{cur}>{HOME_ICON}<span>Home</span></a>')
    out.append('<nav class="sb-zones" aria-label="Vakken">')
    for z in ZONES:
        here = ' aria-current="true"' if z["slug"] == zone else ""
        carry = " data-carry" if kind in ("sam", "oefen") else ""
        name = f'<span>{z["naam"]}</span>' if z["naam"] != z["code"] else ""
        out.append(f'<a class="sb-zone {z["cls"]}" href="{zone_href(z)}" title="{z["naam"]}" aria-label="{z["naam"]}"{here}{carry}><b>{z["code"]}</b>{name}</a>')
    out.append("</nav>")
    out.append(f'<details class="sb-menu"><summary aria-label="Menu: alle pagina\'s">{MENU_ICON}<span>Menu</span></summary><div class="sb-panel">')
    for z in ZONES:
        out.append(f'<div class="sb-col {z["cls"]}"><span class="sb-colhead"><b>{z["code"]}</b>{z["naam"]}</span><div class="sb-links">')
        out.append(f'<a href="{root}samenvattingen/{z["slug"]}/">Samenvatting</a>')
        out.append(f'<a href="{root}{z["slug"]}/#oefenen" data-default>Oefenvragen</a>')
        out.append(f'<a href="{root}{z["slug"]}/#toetsen">Weektoetsen</a>')
        if z["slug"] in ARTIKELEN:
            out.append(f'<a href="{root}artikelen/{z["slug"]}/">Wetsartikelen</a>')
        if z["slug"] == "praktijkproject":
            for s, n in CASUS:
                out.append(f'<a href="{root}bedrijfskunde/{s}/">Casustoets {n}</a>')
        out.append("</div></div>")
    out.append("</div></details></div></header>")
    return "".join(out)


def tabs(root, slug, current, ids=False, doc_ext=None):
    """Tabbladen van één vak. current: 'sam', 'oefenen', 'toetsen', 'casus' of 'art'.
    ids=True (vakpagina): Oefenen en Weektoetsen wisselen op de pagina zelf en krijgen een teller.
    doc_ext: in de Claude-artifactversie verwijst Samenvatting naar het Claude-document."""
    def tab(key, href, lang, kort, extra=""):
        cur = ' aria-current="page"' if key == current else ""
        tid = f' id="tab-{key}"' if ids and key in ("oefenen", "toetsen") else ""
        n = f' <span class="n" id="n-{key}"></span>' if ids and key in ("oefenen", "toetsen") else ""
        label = f'<span class="l">{lang}</span><span class="s">{kort}</span>' if lang != kort else lang
        return f'<a class="tab{extra}" href="{href}"{tid}{cur}>{label}{n}</a>'
    out = ['<nav class="tabs" aria-label="Onderdelen van dit vak" id="tabs">']
    if doc_ext:
        out.append(f'<a class="tab ext" href="{doc_ext}" target="_blank" rel="noopener">Samenvatting</a>')
    else:
        out.append(tab("sam", f"{root}samenvattingen/{slug}/", "Samenvatting", "Samenvatting"))
    page = "" if ids else f"{root}{slug}/"
    out.append(tab("oefenen", f"{page}#oefenen", "Oefenen", "Oefenen"))
    out.append(tab("toetsen", f"{page}#toetsen", "Weektoetsen", "Toetsen"))
    if slug in ARTIKELEN and not doc_ext:
        out.append(tab("art", f"{root}artikelen/{slug}/", "Wetsartikelen", "Artikelen"))
    if slug == "praktijkproject" and not doc_ext:
        out.append(tab("casus", f"{root}bedrijfskunde/{CASUS[0][0]}/", "Casustoetsen", "Casus"))
    out.append("</nav>")
    return "".join(out)


def crumbs(root, slug=None, here=None):
    """Kruimelpad boven de titel: Home › vak › onderdeel. here: naam van deze pagina (laatste stap, zonder link)."""
    z = next((z for z in ZONES if z["slug"] == slug), None)
    out = ['<nav class="crumbs" aria-label="Kruimelpad">', f'<a href="{root or "./"}">Home</a>']
    if z and here:
        out.append(f'<i aria-hidden="true">/</i><a href="{root}{z["slug"]}/">{z["naam"]}</a>')
    elif z:
        out.append(f'<i aria-hidden="true">/</i><span aria-current="page">{z["naam"]}</span>')
    if here:
        out.append(f'<i aria-hidden="true">/</i><span aria-current="page">{here}</span>')
    out.append("</nav>")
    return "".join(out)


def footer(root):
    """Voettekst onderaan elke pagina van de site: alle onderdelen per vak, zodat je vanaf het eind van een pagina verder kunt."""
    out = ['<footer class="sitefoot"><div class="sf-in">',
           f'<div class="sf-about"><a class="sf-home" href="{root or "./"}">Studieplek FM jaar 2</a>'
           '<p>Periode 2: samenvattingen, oefenvragen en weektoetsen. Toetsperiode 11 t/m 22 januari 2027.</p>'
           '<a class="sf-top" href="#">Terug naar boven</a></div>']
    for z in ZONES:
        out.append(f'<div class="sf-col {z["cls"]}"><span class="sf-head"><b>{z["code"]}</b>{z["naam"]}</span>')
        out.append(f'<a href="{root}samenvattingen/{z["slug"]}/">Samenvatting</a>')
        out.append(f'<a href="{root}{z["slug"]}/#oefenen">Oefenvragen</a>')
        out.append(f'<a href="{root}{z["slug"]}/#toetsen">Weektoetsen</a>')
        if z["slug"] in ARTIKELEN:
            out.append(f'<a href="{root}artikelen/{z["slug"]}/">Wetsartikelen</a>')
        if z["slug"] == "praktijkproject":
            for s, n in CASUS:
                out.append(f'<a href="{root}bedrijfskunde/{s}/">Casustoets {n}</a>')
        out.append("</div>")
    out.append("</div></footer>")
    return "".join(out)


HEAD_CSS = """
/* ---------- kop van een vakpagina: licht vlak met een streep in de vakkleur, bordje, kruimelpad en tabbladen ---------- */
.band { background: var(--sheet, var(--surface)); color: var(--ink); border-bottom: 1px solid var(--rule, var(--line)); box-shadow: inset 0 4px 0 var(--accent); }
.band-in { margin: 0 auto; display: flex; flex-direction: column; gap: 12px; padding-block: 26px 0;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.band :focus-visible { outline-color: var(--accent); }
.band h1 { color: var(--ink); }
.crumbs { display: flex; flex-wrap: wrap; align-items: center; gap: 2px 6px; font-size: 0.86rem; color: var(--ink-soft, var(--muted)); margin: -6px 0 -2px; }
.crumbs a { color: inherit; text-decoration: none; font-weight: 500; }
.crumbs a:hover { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; }
.crumbs i { font-style: normal; opacity: 0.55; }
.crumbs [aria-current] { color: var(--ink); font-weight: 600; }
.title-row { display: flex; align-items: center; gap: 14px; min-width: 0; }
.title-row > div { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.title-row h1 { min-width: 0; }
.plate { flex: none; min-width: 52px; height: 52px; padding-inline: 8px; border-radius: 10px; background: var(--accent); color: var(--on-accent, var(--accent-ink, #fff));
  display: grid; place-items: center; font-weight: 800; font-stretch: 112%; font-size: 1.02rem; letter-spacing: 0.02em; }
.kind { font-size: 0.9rem; font-weight: 600; color: var(--accent); }
.band .lead, .band .examline { max-width: 66ch; color: var(--ink-soft, var(--muted)); font-size: 0.96rem; margin: 0; }
.band .lead a { color: var(--accent); font-weight: 600; white-space: nowrap; }
.band .meta { display: flex; flex-wrap: wrap; gap: 6px 18px; color: var(--ink-soft, var(--muted)); font-size: 0.93rem; }
.band .meta strong { color: var(--ink); }
@media (max-width: 400px) { .plate { min-width: 44px; height: 44px; font-size: 0.9rem; border-radius: 9px; } .title-row { gap: 12px; } }
"""

TABS_CSS = HEAD_CSS + """
/* ---------- tabbladen: onderstreept, op elke pagina van een vak dezelfde ---------- */
.tabs { display: flex; gap: 6px; margin-top: 6px; margin-bottom: -1px; max-width: 100%; }
.tab { border: 0; background: transparent; padding: 11px 12px 12px; border-bottom: 3px solid transparent; font-weight: 600; color: var(--ink-soft, var(--muted));
  text-decoration: none; font-size: 0.97rem; line-height: 1.3; display: inline-flex; gap: 8px; align-items: center; white-space: nowrap; }
.tab:first-child { margin-left: -12px; }
.tab:hover { color: var(--ink); border-bottom-color: var(--rule, var(--line)); }
.tab[aria-current="page"], .tab[aria-current="page"]:hover { color: var(--accent); border-bottom-color: var(--accent); }
.tab .n { font-size: 0.74rem; font-weight: 600; padding: 1px 7px; border-radius: 999px; background: var(--sunk, var(--surface-2)); color: var(--ink-soft, var(--muted)); }
.tab[aria-current="page"] .n { background: var(--accent-soft); color: var(--accent); }
.tab .n:empty { display: none; }
.tab .s { display: none; }
.tab.ext { order: 9; }
.tab.ext::after { content: "\\2197"; font-size: 0.8em; opacity: 0.75; }
@media (max-width: 600px) {
  .tabs { width: 100%; gap: 0; }
  .tab, .tab:first-child { flex: 1 1 auto; justify-content: center; padding: 10px 4px 11px; font-size: 0.9rem; margin-left: 0; }
  .tab .l, .tab .n { display: none; } .tab .s { display: inline; }
}
@media (max-width: 350px) { .tab { font-size: 0.84rem; padding-inline: 2px; } }
"""

BAR_CSS = """
/* ---------- wegwijzerbalk: op elke pagina vast bovenaan ---------- */
:root { --sb-h: 48px; --sb-bg: #1d2b4f; --z-ir: #0b6f82; --z-hrm: #8f2a65; --z-bm: #9a520a; --zt-ir: #0b6f82; --zt-hrm: #9a2d6c; --zt-bm: #9a520a; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --sb-bg: #1f3160; --z-ir: #0d5e6e; --z-hrm: #7a2457; --z-bm: #8a4a0a; --zt-ir: #63cfe2; --zt-hrm: #f095c9; --zt-bm: #f5b65e; } }
:root[data-theme="dark"] { --sb-bg: #1f3160; --z-ir: #0d5e6e; --z-hrm: #7a2457; --z-bm: #8a4a0a; --zt-ir: #63cfe2; --zt-hrm: #f095c9; --zt-bm: #f5b65e; }
@media (max-width: 560px) { :root { --sb-h: 46px; } }
.skip { position: absolute; left: 8px; top: -80px; z-index: 60; background: #fff; color: #16202f; padding: 10px 14px; border-radius: 8px; font-weight: 700; text-decoration: none; }
.skip:focus { top: calc(env(safe-area-inset-top, 0px) + 6px); }
.sitebar { position: sticky; top: 0; z-index: 40; background: var(--sb-bg); color: #fff; padding-top: env(safe-area-inset-top, 0px);
  font-family: "Archivo", "Segoe UI", system-ui, sans-serif; font-size: 16px; line-height: 1.2; box-shadow: 0 1px 0 rgba(255, 255, 255, 0.14); }
.sitebar :focus-visible { outline: 2px solid #fff; outline-offset: 2px; }
.sb-in { max-width: __W__px; margin: 0 auto; height: var(--sb-h); display: flex; align-items: center; gap: 4px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.sb-home { display: inline-flex; align-items: center; gap: 7px; height: 34px; padding: 0 11px 0 8px; margin-left: -8px; border-radius: 8px; color: #fff; text-decoration: none; font-weight: 700; font-size: 0.95rem; }
.sb-home svg { width: 19px; height: 19px; flex: none; }
.sb-home:hover, .sb-home[aria-current="page"] { background: rgba(255, 255, 255, 0.14); }
.sb-zones { display: flex; align-items: stretch; height: 100%; gap: 2px; margin-left: 6px; padding-left: 10px; position: relative; }
.sb-zones::before { content: ""; position: absolute; left: 0; top: 50%; height: 22px; margin-top: -11px; width: 1px; background: rgba(255, 255, 255, 0.24); }
.sb-zone { display: inline-flex; align-items: center; gap: 8px; padding: 0 3px; color: #fff; text-decoration: none; font-weight: 600; font-size: 0.9rem; white-space: nowrap; }
.sb-zone b { display: grid; place-items: center; min-width: 38px; height: 30px; padding: 0 7px; border-radius: 7px; font-weight: 800; font-stretch: 118%; font-size: 0.8rem; letter-spacing: 0.02em;
  background: var(--zc); color: #fff; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.3); }
.sb-zone span { display: none; padding-right: 8px; color: rgba(255, 255, 255, 0.9); }
.sb-zone:hover b { box-shadow: inset 0 0 0 2px #fff; }
.sb-zone:hover span { color: #fff; text-decoration: underline; text-underline-offset: 3px; }
.sb-zone[aria-current="true"] b { background: #fff; color: var(--zc); box-shadow: none; }
.sb-zone[aria-current="true"] span { color: #fff; font-weight: 700; }
.sitebar .ir { --zc: var(--z-ir); --zt: var(--zt-ir); } .sitebar .hrm { --zc: var(--z-hrm); --zt: var(--zt-hrm); } .sitebar .bm { --zc: var(--z-bm); --zt: var(--zt-bm); }
@media (min-width: 900px) { .sb-zone span { display: inline; } .sb-zones { gap: 6px; } }
.sb-menu { margin-left: auto; position: relative; }
.sb-menu > summary { list-style: none; display: inline-flex; align-items: center; gap: 8px; height: 34px; padding: 0 12px 0 10px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.4);
  cursor: pointer; font-weight: 700; font-size: 0.92rem; user-select: none; -webkit-user-select: none; }
.sb-menu > summary::-webkit-details-marker { display: none; }
.sb-menu > summary svg { width: 18px; height: 18px; flex: none; }
.sb-menu > summary:hover { background: rgba(255, 255, 255, 0.14); }
.sb-menu[open] > summary { background: #fff; color: #1d2b4f; box-shadow: none; }
@media (max-width: 400px) { .sb-menu > summary { padding: 0 8px; } .sb-menu > summary span { display: none; } .sb-home { padding-right: 8px; } .sb-zones { margin-left: 2px; padding-left: 8px; } }
.sb-panel { position: absolute; right: 0; top: calc(100% + 9px); width: min(700px, calc(100vw - 32px)); max-height: calc(100vh - var(--sb-h) - 28px); overflow-y: auto;
  background: var(--sheet, var(--surface)); color: var(--ink); border: 1px solid var(--rule, var(--line)); border-radius: 14px; box-shadow: 0 14px 36px rgba(10, 18, 36, 0.28);
  padding: 14px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.sb-col { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.sb-colhead { display: flex; align-items: center; gap: 9px; font-weight: 800; font-size: 0.92rem; line-height: 1.15; min-height: 38px; padding: 2px 4px 6px; border-bottom: 2px solid var(--zc); }
.sb-colhead b { display: grid; place-items: center; min-width: 34px; height: 26px; padding: 0 6px; border-radius: 6px; background: var(--zc); color: #fff; font-stretch: 118%; font-size: 0.74rem; letter-spacing: 0.02em; }
.sb-links { display: flex; flex-direction: column; gap: 2px; }
.sb-links a { display: flex; align-items: center; min-height: 40px; padding: 6px 10px; border-radius: 8px; color: var(--ink); text-decoration: none; font-weight: 600; font-size: 0.95rem; }
.sb-links a:hover { background: color-mix(in srgb, var(--zt) 14%, transparent); color: var(--zt); }
.sb-links a[aria-current="page"] { background: color-mix(in srgb, var(--zt) 14%, transparent); color: var(--zt); font-weight: 700; }
.sb-panel :focus-visible { outline-color: var(--zt); }
@media (max-width: 620px) {
  .sb-panel { grid-template-columns: 1fr; gap: 12px; }
  .sb-links { flex-direction: row; flex-wrap: wrap; gap: 6px; }
  .sb-links a { border: 1px solid var(--rule, var(--line)); padding: 6px 12px; font-size: 0.92rem; }
  .sb-links a[aria-current="page"] { border-color: var(--zt); }
}

/* ---------- voettekst: alle onderdelen per vak ---------- */
.sitefoot { margin-top: 40px; border-top: 1px solid var(--rule, var(--line)); background: var(--sheet, var(--surface)); color: var(--ink-soft, var(--muted));
  font-family: "Archivo", "Segoe UI", system-ui, sans-serif; font-size: 0.9rem; line-height: 1.45; }
.sf-in { max-width: __W__px; margin: 0 auto; display: grid; grid-template-columns: 1.3fr repeat(3, minmax(0, 1fr)); gap: 28px;
  padding: 30px max(16px, env(safe-area-inset-right, 0px)) calc(36px + env(safe-area-inset-bottom, 0px)) max(16px, env(safe-area-inset-left, 0px)); }
.sf-about { display: flex; flex-direction: column; gap: 8px; align-items: flex-start; }
.sf-about p { margin: 0; max-width: 34ch; }
.sf-home { font-weight: 800; color: var(--ink); text-decoration: none; font-size: 1rem; }
.sf-top { color: var(--ink-soft, var(--muted)); font-weight: 600; }
.sf-col { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.sf-head { display: flex; align-items: center; gap: 8px; font-weight: 700; color: var(--ink); margin-bottom: 6px; }
.sf-head b { display: grid; place-items: center; min-width: 32px; height: 22px; padding: 0 5px; border-radius: 5px; background: var(--zc); color: #fff; font-size: 0.7rem; font-stretch: 112%; letter-spacing: 0.02em; }
.sf-col a { color: var(--ink-soft, var(--muted)); text-decoration: none; padding: 3px 0; }
.sf-col a:hover { color: var(--zt); text-decoration: underline; text-underline-offset: 3px; }
.sitefoot .ir { --zc: var(--z-ir); --zt: var(--zt-ir); } .sitefoot .hrm { --zc: var(--z-hrm); --zt: var(--zt-hrm); } .sitefoot .bm { --zc: var(--z-bm); --zt: var(--zt-bm); }
@media (max-width: 820px) { .sf-in { grid-template-columns: repeat(3, minmax(0, 1fr)); } .sf-about { grid-column: 1 / -1; } }
@media (max-width: 520px) { .sf-in { grid-template-columns: 1fr 1fr; gap: 22px 16px; padding-bottom: calc(88px + env(safe-area-inset-bottom, 0px)); } .sf-col.bm { grid-column: 1 / -1; } }
"""

BAR_JS = """<script>
(function () {
  var bar = document.getElementById("sitebar"); if (!bar) return;
  var menu = bar.querySelector("details");
  document.addEventListener("click", function (e) { if (menu.open && !menu.contains(e.target)) menu.open = false; });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && menu.open) { menu.open = false; menu.querySelector("summary").focus(); } });
  menu.addEventListener("click", function (e) { if (e.target.closest("a")) menu.open = false; });
  function path(p) { return p.replace(/index\\.html$/, ""); }
  // in het menu de pagina markeren waar je nu bent
  function mark() {
    var here = path(location.pathname), hash = location.hash.replace(/-w\\d+$/, "");
    Array.prototype.forEach.call(bar.querySelectorAll(".sb-panel a"), function (a) {
      var u = new URL(a.href, location.href);
      var same = path(u.pathname) === here && (!u.hash || u.hash === hash || (!/^#(oefenen|toetsen)$/.test(hash) && a.hasAttribute("data-default")));
      if (same) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
  }
  window.sitenavMark = mark;
  // naar een ander vak: blijf in hetzelfde onderdeel (oefenen, toetsen of dezelfde week van de samenvatting)
  Array.prototype.forEach.call(bar.querySelectorAll("a[data-carry]"), function (a) {
    a.addEventListener("click", function () {
      var h = location.hash, wk = document.querySelector('.weeknav a[aria-current="true"]');
      if (wk && window.scrollY > 200) h = wk.getAttribute("href");
      if (/^#(oefenen|toetsen|week-\\d)$/.test(h)) a.href = a.href.split("#")[0] + h;
    });
  });
  window.addEventListener("hashchange", mark); mark();
})();
</script>"""


BREEDTE = 1180  # breedte van balk en voettekst, op elke pagina gelijk zodat de navigatie niet verspringt


def bar_css():
    return BAR_CSS.replace("__W__", str(BREEDTE))
