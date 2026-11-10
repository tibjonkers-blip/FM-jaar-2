"""Bouwstenen voor de figuren en grafieken in de samenvattingen.

De samenvattingen zelf zijn markdown-exports van de Claude-documenten en worden bij een nieuwe export overschreven.
Daarom staan de figuren hier los van: per vak een bestand (inkoop_recht.py, hrm.py, praktijkproject.py) met een lijst FIGUREN.
build_samenvattingen.py zet elke figuur onder de juiste kop en stopt met een foutmelding als een kop niet (meer) bestaat.

Elke bouwsteen geeft html terug. Alle tekst wordt ge-escaped; schrijf dus gewone tekst.
Regels: een figuur herhaalt alleen wat in de samenvatting staat (of zegt erbij dat iets gangbaar is en niet uit de slides komt),
getallen staan altijd als tekst bij de staaf, en kleur is nooit het enige onderscheid.
"""
import html as _html


def e(s):
    return _html.escape(str(s), quote=False)


def F(week, les, kop, fig, pos="end", after=None):
    """Plaats een figuur. week: 0 (overzicht) t/m 7. les: stukje uit de titel van de les (bv. "Inkoop", "Recht", "Arbeidsrecht").
    kop: de exacte tussenkop (###) waaronder de figuur komt, of None voor de inleiding van de les.
    pos: "top" (direct onder de kop) of "end" (onderaan het stuk). after: stukje tekst; de figuur komt na het blok met die tekst."""
    return dict(week=week, les=les, kop=kop, html=fig, pos=pos, after=after)


def fig(titel, body, noot=None, sub=None):
    cap = e(titel) + (f"<small>{e(sub)}</small>" if sub else "")
    n = f'<p class="fig-note">{e(noot)}</p>' if noot else ""
    return f'<figure class="fig"><figcaption>{cap}</figcaption>{body}{n}</figure>'


def _pair(x):
    return (x, None) if isinstance(x, str) else (x[0], x[1] if len(x) > 1 else None)


# ---------------------------------------------------------------- stappen

def _steps(steps, start=1, first_arrow=False, cols=None, numbered=True):
    n = len(steps)
    cols = cols or (n if n <= 5 else (n + 1) // 2)
    out = [f'<ol class="flow" style="--cols:{cols}">']
    for i, s in enumerate(steps):
        t, sub = _pair(s)
        cls = []
        if i % cols != 0 or (i == 0 and first_arrow):
            cls.append("ar")
        if i > 0 or first_arrow:
            cls.append("ad")
        nr = f'<i class="nr">{start + i}</i>' if numbered else ""
        out.append(f'<li class="{" ".join(cls)}">{nr}<b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</li>")
    out.append("</ol>")
    return "".join(out)


def flow(steps, cols=None, numbered=True, loop=None):
    """Stappen na elkaar. steps: lijst van "titel" of ("titel", "toelichting"). loop: tekst bij de pijl terug naar het begin."""
    h = _steps(steps, cols=cols, numbered=numbered)
    if loop:
        h += f'<div class="loopback" aria-hidden="true"></div><p class="loop-note">{e(loop)}</p>'
    return h


def phases(groups, numbered=True, stack=False):
    """Stappen in fasen. groups: lijst van (fasenaam, [stappen], toon) met toon "t1", "t2" of "t3".
    stack=True zet de fasen onder elkaar (bij veel stappen)."""
    out, start = [], 1
    stack = stack or sum(len(g[1]) for g in groups) > 4
    pc = "minmax(0, 1fr)" if stack else " ".join(f"minmax(0, {len(g[1])}fr)" for g in groups)
    out.append(f'<div class="phases{" stack" if stack else ""}" style="--pc:{pc}">')
    for gi, g in enumerate(groups):
        name, steps = g[0], g[1]
        tone = g[2] if len(g) > 2 else "t1"
        out.append(f'<div class="phase {tone}"><h5>{e(name)}</h5>{_steps(steps, start=start, first_arrow=gi > 0 and not stack, cols=len(steps), numbered=numbered)}</div>')
        start += len(steps)
    out.append("</div>")
    return "".join(out)


def lanes(rows, numbered=True):
    """Meerdere rijen stappen onder elkaar om te vergelijken. rows: lijst van (naam, toelichting, [stappen])."""
    out = ['<div class="lanes">']
    for name, sub, steps in rows:
        out.append(f'<div class="lane"><h5>{e(name)}' + (f" <small>{e(sub)}</small>" if sub else "") + f"</h5>{_steps(steps, numbered=numbered)}</div>")
    out.append("</div>")
    return "".join(out)


def ladder(steps, slot=None, stop=False):
    """Beslisladder. steps: lijst van (vraag, toelichting, uitgang) waarbij uitgang de afslag is als het antwoord nee is (of None).
    slot: de uitkomst onderaan; stop=True geeft die een neutraal eindteken in plaats van een vinkje (voor een uitkomst die niet goed nieuws is)."""
    out = ['<ol class="ladder">']
    for i, (q, sub, ex) in enumerate(steps, 1):
        out.append(f'<li><i class="nr">{i}</i><div class="q"><b>{e(q)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</div>"
                   + (f'<span class="exit">{e(ex)}</span>' if ex else "") + "</li>")
    if slot:
        out.append(f'<li class="done{" stop" if stop else ""}"><i class="nr">{"" if stop else "✓"}</i><div class="q"><b>{e(slot)}</b></div></li>')
    out.append("</ol>")
    return "".join(out)


def timeline(items, breed="5.5em"):
    """Tijdlijn van boven naar beneden. items: lijst van (wanneer, wat, toelichting)."""
    out = [f'<ol class="tl" style="--tw:{breed}">']
    for when, what, sub in items:
        out.append(f'<li><span class="when">{e(when)}</span><span class="dot"></span><div class="what"><b>{e(what)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</div></li>")
    out.append("</ol>")
    return "".join(out)


def cycle(items, midden):
    """Kringloop van vier stappen met de klok mee. items: vier keer "titel" of ("titel", "toelichting")."""
    assert len(items) == 4
    out = [f'<div class="cyc" role="group" aria-label="{e(midden)}"><ol>']
    for i, s in enumerate(items, 1):
        t, sub = _pair(s)
        out.append(f'<li><i class="nr">{i}</i><b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</li>")
    out.append("</ol></div>")
    return "".join(out)


# ---------------------------------------------------------------- vlakken

def quad(yas, xas, cellen, ylaag="laag", yhoog="hoog", xlaag="laag", xhoog="hoog"):
    """2x2-matrix. cellen in leesvolgorde: linksboven, rechtsboven, linksonder, rechtsonder.
    Elke cel: (titel, kenmerk, tekst, toon) met toon "t1".."t4" of "t0" (neutraal)."""
    out = [f'<div class="quad"><div class="q-y"><small>{e(ylaag)}</small><span>{e(yas)}</span><small>{e(yhoog)}</small></div><div class="q-grid">']
    for c in cellen:
        t, k, txt = c[0], c[1], c[2]
        tone = c[3] if len(c) > 3 else "t0"
        out.append(f'<div class="q-cell {tone}"><b>{e(t)}</b>' + (f"<small>{e(k)}</small>" if k else "") + (f"<span>{e(txt)}</span>" if txt else "") + "</div>")
    out.append(f'</div><div class="q-x"><small>{e(xlaag)}</small><span>{e(xas)}</span><small>{e(xhoog)}</small></div></div>')
    return "".join(out)


def nest(lagen):
    """Lagen in elkaar, van buiten naar binnen. lagen: lijst van (titel, toelichting)."""
    out, close = [], ""
    for t, sub in lagen:
        out.append(f'<div class="nest"><div class="nest-h"><b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</div>")
        close += "</div>"
    return "".join(out) + close


def tree(root, kids, rootsub=None):
    """Boom met één stam. kids: lijst van (titel, toelichting, [takjes]) waarbij takjes een lijst is van "tekst" of ("titel", "toelichting")."""
    out = [f'<div class="tree"><div class="tree-root">{e(root)}' + (f"<small>{e(rootsub)}</small>" if rootsub else "") + '</div><ul class="tree-kids">']
    for k in kids:
        t, sub = k[0], k[1] if len(k) > 1 else None
        twigs = k[2] if len(k) > 2 else None
        out.append(f'<li><div class="tree-node"><b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else ""))
        if twigs:
            out.append('<ul class="twigs">')
            for tw in twigs:
                a, b = _pair(tw)
                out.append(f"<li><b>{e(a)}</b>" + (f" {e(b)}" if b else "") + "</li>")
            out.append("</ul>")
        out.append("</div></li>")
    out.append("</ul></div>")
    return "".join(out)


def som(delen, uitkomst, op="+"):
    """A + B + C = uitkomst. delen: lijst van "titel" of ("titel", "toelichting"); uitkomst idem."""
    out = ['<div class="sumf">']
    for i, d in enumerate(delen):
        t, sub = _pair(d)
        if i:
            out.append(f'<span class="op" aria-hidden="true">{e(op)}</span>')
        out.append(f"<div><b>{e(t)}</b>" + (f"<span>{e(sub)}</span>" if sub else "") + "</div>")
    t, sub = _pair(uitkomst)
    out.append(f'<span class="op" aria-hidden="true">=</span><div class="res"><b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</div></div>")
    return "".join(out)


def poles(rows):
    """Uitersten tegenover elkaar. rows: lijst van (vraag, (links, toelichting), (rechts, toelichting))."""
    out = ['<div class="poles">']
    for q, l, r in rows:
        (lt, ls), (rt, rs) = _pair(l), _pair(r)
        out.append(f'<div class="pole"><h5>{e(q)}</h5><div><span class="pl"><b>{e(lt)}</b>' + (f"<small>{e(ls)}</small>" if ls else "")
                   + f'</span><span class="mid" aria-hidden="true"></span><span class="pr"><b>{e(rt)}</b>' + (f"<small>{e(rs)}</small>" if rs else "") + "</span></div></div>")
    out.append("</div>")
    return "".join(out)


def cards(items, cols=None):
    """Losse kaarten naast elkaar, zonder volgorde. items: lijst van (teken, titel, toelichting); teken is een kort beeldmerk, bv. "●●"."""
    out = [f'<ul class="cards" style="--cols:{cols or len(items)}">']
    for mark, t, sub in items:
        out.append("<li>" + (f'<i class="mark" aria-hidden="true">{e(mark)}</i>' if mark else "") + f"<b>{e(t)}</b>" + (f"<span>{e(sub)}</span>" if sub else "") + "</li>")
    out.append("</ul>")
    return "".join(out)


def stairs(items, van=46, numbered=True, midden=False):
    """Trap: elke trede is breder dan de vorige. items: lijst van (titel, toelichting). midden=True maakt er een piramide van."""
    n = len(items)
    out = [f'<ol class="stairs{" mid" if midden else ""}">']
    for i, (t, sub) in enumerate(items):
        w = van + (100 - van) * i / max(1, n - 1)
        k = 6 + 22 * i / max(1, n - 1)
        nr = f'<i class="nr">{i + 1}</i>' if numbered else ""
        out.append(f'<li style="--w:{w:.0f}%;--k:{k:.0f}%">{nr}<b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</li>")
    out.append("</ol>")
    return "".join(out)


def pillars(dak, zuilen, basis=None):
    """Huis met zuilen. zuilen: lijst van (titel, toelichting)."""
    out = [f'<div class="pil"><div class="pil-roof">{e(dak)}</div><ol class="pil-cols" style="--n:{len(zuilen)}">']
    for i, z in enumerate(zuilen, 1):
        t, sub = _pair(z)
        out.append(f'<li><i class="nr">{i}</i><b>{e(t)}</b>' + (f"<span>{e(sub)}</span>" if sub else "") + "</li>")
    out.append("</ol>" + (f'<div class="pil-base">{e(basis)}</div>' if basis else "") + "</div>")
    return "".join(out)


def iceberg(boven, onder, bovenkop="Boven water: wat je ziet", onderkop="Onder water: wat je niet ziet"):
    """IJsberg. boven: tekst; onder: lijst van trefwoorden."""
    chips = "".join(f"<li>{e(x)}</li>" for x in onder)
    return (f'<div class="berg"><div class="berg-top"><i aria-hidden="true"></i><div><b>{e(bovenkop)}</b><span>{e(boven)}</span></div></div>'
            f'<div class="berg-sub"><i aria-hidden="true"></i><div><b>{e(onderkop)}</b><ul class="chips">{chips}</ul></div></div></div>')


def pgrid(kolommen, rijen, hoek=""):
    """Raster met rijen en kolommen. rijen: lijst van (rijnaam, [cellen]) waarbij een cel "tekst" of ("tekst", "klein") is."""
    out = [f'<div class="pgrid" style="--n:{len(kolommen)}"><span class="ch corner">{e(hoek)}</span>']
    out += [f'<span class="ch">{e(k)}</span>' for k in kolommen]
    for name, cells in rijen:
        out.append(f'<span class="rh">{e(name)}</span>')
        for k, c in zip(kolommen, cells):
            if c is None:
                out.append('<span class="c empty" aria-hidden="true"></span>')
                continue
            t, sub = _pair(c)
            out.append(f'<span class="c" data-col="{e(k)}"><span>{e(t)}</span>' + (f"<small>{e(sub)}</small>" if sub else "") + "</span>")
    out.append("</div>")
    return "".join(out)


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


# ---------------------------------------------------------------- grafieken

def legend(items):
    """items: lijst van (kleurklasse, tekst), kleurklasse "c1".."c4", "c0" (grijs) of "ref" (streepje)."""
    return '<ul class="legend">' + "".join(f'<li><i class="{c}"></i>{e(t)}</li>' for c, t in items) + "</ul>"


def bars(rows, maxv, vw="6.5em", label=None):
    """Liggende staven met het getal aan het eind van de staaf.
    rows: lijst van dict(label=, sub=, segs=[(waarde, kleurklasse)], val="tekst", start=0, ref=waarde of None, neg=False).
    maxv: de waarde die de volle breedte krijgt."""
    out = [f'<div class="bars" style="--vw:{vw}"' + (f' role="group" aria-label="{e(label)}"' if label else "") + ">"]
    for r in rows:
        out.append('<div class="bar-row"><span class="bar-label">' + e(r["label"]) + (f' <small>{e(r["sub"])}</small>' if r.get("sub") else "") + '</span><span class="bar-track">')
        start = r.get("start", 0)
        for i, (v, c) in enumerate(r["segs"]):
            ml = f"margin-left:calc((100% - var(--vw)) * {start / maxv:.4f});" if (i == 0 and start) else ""
            cls = c + (" neg" if r.get("neg") else "")
            out.append(f'<i class="{cls}" style="{ml}width:calc((100% - var(--vw)) * {v / maxv:.4f})"></i>')
        if r.get("val"):
            tot = start + sum(v for v, _ in r["segs"])
            ref = r.get("ref")
            push = f' style="margin-left:calc((100% - var(--vw)) * {(ref - tot) / maxv:.4f} + 8px)"' if ref is not None and ref > tot else ""
            out.append(f"<b{push}>{e(r['val'])}</b>")
        if r.get("ref") is not None:
            out.append(f'<u style="left:calc((100% - var(--vw)) * {r["ref"] / maxv:.4f})"></u>')
        out.append("</span></div>")
    out.append("</div>")
    return "".join(out)


def seg(parts):
    """Eén staaf in delen (deel van een geheel) met een legenda eronder. parts: lijst van (waarde, kleurklasse, titel, toelichting)."""
    bar = "".join(f'<i class="{c}" style="flex:{v} 1 0"></i>' for v, c, _, _ in parts)
    key = "".join(f'<li><i class="{c}"></i><b>{e(t)}</b>' + (f"<small>{e(s)}</small>" if s else "") + "</li>" for _, c, t, s in parts)
    return f'<div class="seg" aria-hidden="true">{bar}</div><ul class="seg-key">{key}</ul>'


def svg(inner, w=360, h=220, label=""):
    return f'<svg class="chart" viewBox="0 0 {w} {h}" role="img" aria-label="{e(label)}" style="max-width:{w + 40}px">{inner}</svg>'


# ---------------------------------------------------------------- stijl

CSS = r"""
/* ---------- figuren en grafieken ---------- */
.fig { margin: 0; display: flex; flex-direction: column; gap: 12px; padding: 14px 16px 16px; border: 1px solid var(--rule); border-radius: 12px; background: var(--paper); min-width: 0; --ln: color-mix(in srgb, var(--ink-soft) 55%, transparent); }
.fig > figcaption { font-family: var(--font-display); font-weight: 700; font-stretch: 104%; font-size: 0.95rem; line-height: 1.3; }
.fig > figcaption small { display: block; font-weight: 400; font-stretch: 100%; font-size: 0.84rem; color: var(--ink-soft); margin-top: 2px; }
.fig-note, .loop-note { font-size: 0.82rem; line-height: 1.45; color: var(--ink-soft); max-width: 72ch; }
.fig ol, .fig ul { list-style: none; margin: 0; padding: 0; gap: 0; }
.fig { hyphenate-limit-chars: 11 5 4; }
.fig li { max-width: none; }
.fig b { font-weight: 700; }
.fig h5 { margin: 0; font: inherit; }
.fig .nr { flex: none; display: inline-grid; place-items: center; width: 20px; height: 20px; border-radius: 50%; background: var(--accent); color: var(--on-accent); font-style: normal; font-size: 0.72rem; font-weight: 800; line-height: 1; }
.t1 { --tone: var(--accent); --tone-soft: var(--accent-soft); } .t2 { --tone: var(--s2); --tone-soft: var(--s2-soft); }
.t3 { --tone: var(--s3); --tone-soft: var(--s3-soft); } .t4 { --tone: var(--warn); --tone-soft: var(--warn-soft); } .t0 { --tone: var(--ink-soft); --tone-soft: var(--sheet); }

/* stappen */
.flow { display: grid; grid-template-columns: repeat(var(--cols, 4), minmax(0, 1fr)); gap: 8px 20px !important; }
.flow > li { position: relative; display: flex; flex-direction: column; gap: 3px; padding: 10px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.35; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.flow > li > b { font-family: var(--font-display); font-size: 0.9rem; font-stretch: 102%; line-height: 1.25; }
.flow > li > span { color: var(--ink-soft); }
.flow > li.ar::before { content: ""; position: absolute; left: -14px; top: 50%; width: 7px; height: 7px; margin-top: -4px; border-top: 2px solid var(--ink-soft); border-right: 2px solid var(--ink-soft); transform: rotate(45deg); }
.phases { display: grid; grid-template-columns: var(--pc); gap: 8px 20px; }
.phase { display: flex; flex-direction: column; gap: 6px; min-width: 0; }
.phase > h5, .lane > h5 { font-size: 0.82rem; font-weight: 700; }
.phase > h5 { padding: 3px 10px; border-radius: 6px; background: var(--tone-soft); color: var(--tone); }
.phase .nr { background: var(--tone); }
.lanes { display: flex; flex-direction: column; gap: 14px; }
.lane { display: flex; flex-direction: column; gap: 6px; }
.lane > h5 { font-size: 0.88rem; } .lane > h5 small { font-weight: 400; color: var(--ink-soft); font-size: 0.84rem; }
.loopback { height: 12px; margin: -4px 10% 0; border: 2px solid var(--ln); border-top: 0; border-radius: 0 0 12px 12px; position: relative; }
.loopback::before { content: ""; position: absolute; left: -6px; top: -3px; width: 8px; height: 8px; border-top: 2px solid var(--ink-soft); border-left: 2px solid var(--ink-soft); transform: rotate(45deg); }
@media (max-width: 620px) {
  .flow { grid-template-columns: 1fr; gap: 16px !important; }
  .flow > li { flex-direction: row; flex-wrap: wrap; align-items: baseline; gap: 2px 8px; }
  .flow > li > b { flex: 1 1 0; min-width: 0; } .flow > li > span { flex: 1 1 100%; }
  .flow > li.ar::before { display: none; }
  .flow > li.ad::after { content: ""; position: absolute; left: 17px; top: -13px; width: 7px; height: 7px; border-top: 2px solid var(--ink-soft); border-right: 2px solid var(--ink-soft); transform: rotate(135deg); }
  .phases { grid-template-columns: 1fr; gap: 16px; }
  .loopback { display: none; }
}

/* beslisladder */
.ladder > li { display: grid; grid-template-columns: 20px minmax(0, 1fr) minmax(0, 42%); gap: 4px 12px; align-items: start; padding: 10px 0; border-top: 1px solid var(--rule); font-size: 0.86rem; line-height: 1.4; }
.ladder > li:first-child { border-top: 0; padding-top: 0; }
.ladder .nr { margin-top: 1px; }
.ladder .q b { display: block; font-size: 0.92rem; } .ladder .q span { color: var(--ink-soft); }
.ladder .exit { padding: 6px 10px; border-radius: 8px; background: var(--warn-soft); font-size: 0.82rem; }
.ladder > li.done.stop .nr { background: var(--ink-soft); border-radius: 4px; }
.ladder > li.done { padding-bottom: 0; } .ladder > li.done .nr { background: var(--s3); } .ladder > li.done .q { grid-column: 2 / -1; }
@media (max-width: 620px) { .ladder > li { grid-template-columns: 20px minmax(0, 1fr); } .ladder .exit { grid-column: 2; } }

/* tijdlijn */
.tl > li { display: grid; grid-template-columns: var(--tw, 5.5em) 12px minmax(0, 1fr); gap: 0 10px; padding-bottom: 12px; font-size: 0.86rem; line-height: 1.4; }
.tl > li:last-child { padding-bottom: 0; }
.tl .when { font-weight: 700; text-align: right; color: var(--accent); font-variant-numeric: tabular-nums; }
.tl .dot { position: relative; }
.tl .dot::before { content: ""; position: absolute; left: 1px; top: 5px; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }
.tl .dot::after { content: ""; position: absolute; left: 5px; top: 19px; bottom: -14px; width: 2px; background: var(--ln); }
.tl > li:last-child .dot::after { display: none; }
.tl .what b { display: block; } .tl .what span { color: var(--ink-soft); }

/* kringloop van vier */
.cyc { position: relative; max-width: 520px; }
.cyc > ol { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 30px !important; }
.cyc li { position: relative; display: flex; flex-direction: column; gap: 3px; padding: 10px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.35; min-width: 0; hyphens: auto; overflow-wrap: break-word; }
.cyc li > b { font-family: var(--font-display); font-size: 0.92rem; } .cyc li > span { color: var(--ink-soft); }
.cyc li:nth-child(3) { grid-column: 2; grid-row: 2; } .cyc li:nth-child(4) { grid-column: 1; grid-row: 2; }
.cyc li::after { content: ""; position: absolute; width: 8px; height: 8px; border-top: 2px solid var(--ink-soft); border-right: 2px solid var(--ink-soft); }
.cyc li:nth-child(1)::after { right: -19px; top: 50%; margin-top: -4px; transform: rotate(45deg); }
.cyc li:nth-child(2)::after { bottom: -19px; left: 50%; margin-left: -4px; transform: rotate(135deg); }
.cyc li:nth-child(3)::after { left: -19px; top: 50%; margin-top: -4px; transform: rotate(225deg); }
.cyc li:nth-child(4)::after { top: -19px; left: 50%; margin-left: -4px; transform: rotate(315deg); }

/* 2x2 */
.quad { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 8px; }
.q-y { writing-mode: vertical-rl; transform: rotate(180deg); display: flex; justify-content: space-between; align-items: center; gap: 4px; font-size: 0.82rem; font-weight: 600; }
.q-y small, .q-x small { font-weight: 400; color: var(--ink-soft); font-size: 0.76rem; }
.q-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px; }
.q-cell { border-radius: 10px; padding: 11px 12px; background: var(--tone-soft); border: 1px solid var(--rule); display: flex; flex-direction: column; gap: 3px; font-size: 0.84rem; line-height: 1.4; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.q-cell:not(.t0) { border-color: transparent; }
.q-cell b { font-family: var(--font-display); font-size: 0.98rem; font-stretch: 104%; color: var(--tone); } .q-cell.t0 b { color: var(--ink); }
.q-cell small { color: var(--ink-soft); font-size: 0.78rem; }
.q-x { grid-column: 2; display: flex; justify-content: space-between; align-items: baseline; font-size: 0.82rem; font-weight: 600; padding-inline: 4px; }
@media (max-width: 480px) { .q-cell { padding: 9px; font-size: 0.8rem; } .q-cell b { font-size: 0.9rem; } }

/* lagen in elkaar */
.nest { border: 1.5px solid color-mix(in srgb, var(--accent) 55%, transparent); border-radius: 12px; padding: 10px 12px 12px; display: flex; flex-direction: column; gap: 9px; background: color-mix(in srgb, var(--accent) 5%, var(--sheet)); min-width: 0; }
.nest .nest { background: color-mix(in srgb, var(--accent) 11%, var(--sheet)); } .nest .nest .nest { background: color-mix(in srgb, var(--accent) 19%, var(--sheet)); }
.nest-h { display: flex; flex-direction: column; gap: 1px; font-size: 0.84rem; line-height: 1.4; }
.nest-h b { font-family: var(--font-display); font-size: 0.95rem; } .nest-h span { color: var(--ink-soft); }
@media (max-width: 480px) { .nest { padding: 8px 8px 9px; } }

/* boom */
.tree { display: flex; flex-direction: column; align-items: center; }
.tree-root { padding: 9px 16px; border-radius: 10px; background: var(--accent); color: var(--on-accent); font-family: var(--font-display); font-weight: 700; text-align: center; max-width: 100%; font-size: 0.95rem; }
.tree-root small { display: block; font-weight: 400; font-size: 0.8rem; opacity: 0.92; font-family: var(--font-body); }
.tree-kids { display: flex; flex-direction: row; width: 100%; padding-top: 14px !important; position: relative; }
.tree-kids::before { content: ""; position: absolute; top: 0; left: 50%; height: 14px; border-left: 2px solid var(--ln); }
.tree-kids > li { flex: 1 1 0; position: relative; padding: 14px 5px 0; min-width: 0; display: flex; flex-direction: column; }
.tree-kids > li::before { content: ""; position: absolute; top: 0; left: 0; right: 0; border-top: 2px solid var(--ln); }
.tree-kids > li:first-child::before { left: 50%; } .tree-kids > li:last-child::before { right: 50%; }
.tree-kids > li:only-child::before { display: none; }
.tree-kids > li::after { content: ""; position: absolute; top: 0; left: 50%; height: 14px; border-left: 2px solid var(--ln); }
.tree-node { flex: 1; display: flex; flex-direction: column; gap: 3px; padding: 9px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.4; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.tree-node > b { font-family: var(--font-display); font-size: 0.92rem; } .tree-node > span { color: var(--ink-soft); }
.twigs { display: flex; flex-direction: column; gap: 4px !important; margin-top: 5px !important; }
.twigs li { padding: 5px 8px; border-radius: 7px; background: var(--accent-soft); font-size: 0.82rem; }
@media (max-width: 620px) {
  .tree { align-items: stretch; }
  .tree-kids { flex-direction: column; padding: 0 0 0 16px !important; }
  .tree-kids::before { display: none; }
  .tree-kids > li { padding: 8px 0 0; }
  .tree-kids > li::before, .tree-kids > li:first-child::before, .tree-kids > li:last-child::before, .tree-kids > li:only-child::before { display: block; left: -8px; right: auto; width: 8px; top: 26px; }
  .tree-kids > li::after { left: -8px; top: 0; bottom: 0; height: auto; }
  .tree-kids > li:last-child::after { bottom: auto; height: 26px; }
}

/* som */
.sumf { display: flex; flex-wrap: wrap; align-items: stretch; gap: 8px; }
.sumf > div { flex: 1 1 120px; display: flex; flex-direction: column; gap: 3px; padding: 10px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.35; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.sumf > div > b { font-family: var(--font-display); font-size: 0.92rem; } .sumf > div > span { color: var(--ink-soft); }
.sumf > .op { align-self: center; font-weight: 800; font-size: 1.15rem; color: var(--ink-soft); flex: none; line-height: 1; }
.sumf > div.res { background: var(--accent); border-color: var(--accent); color: var(--on-accent); } .sumf > div.res > span { color: inherit; opacity: 0.92; }
@media (max-width: 620px) { .sumf { flex-direction: column; flex-wrap: nowrap; gap: 5px; } .sumf > div { flex: none; } }

/* uitersten */
.poles { display: flex; flex-direction: column; gap: 12px; }
.pole { display: flex; flex-direction: column; gap: 5px; }
.pole h5 { font-size: 0.84rem; font-weight: 700; }
.pole > div { display: grid; grid-template-columns: minmax(0, 1fr) 34px minmax(0, 1fr); align-items: stretch; }
.pole .pl, .pole .pr { display: flex; flex-direction: column; gap: 2px; padding: 8px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.35; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.pole small { color: var(--ink-soft); font-size: 0.8rem; }
.pole .mid { align-self: center; height: 2px; margin-inline: 5px; background: var(--ink-soft); position: relative; }
.pole .mid::before, .pole .mid::after { content: ""; position: absolute; top: -3px; width: 6px; height: 6px; border-top: 2px solid var(--ink-soft); border-right: 2px solid var(--ink-soft); }
.pole .mid::before { left: 0; transform: rotate(225deg); } .pole .mid::after { right: 0; transform: rotate(45deg); }

/* trap */
.stairs { display: flex; flex-direction: column; gap: 5px !important; }
.stairs li { width: var(--w); min-width: min(100%, 250px); display: flex; flex-wrap: wrap; align-items: baseline; gap: 2px 8px; padding: 8px 11px; border-radius: 8px; border: 1px solid var(--rule);
  background: color-mix(in srgb, var(--accent) var(--k), var(--sheet)); font-size: 0.84rem; line-height: 1.35; }
.stairs li > b { font-family: var(--font-display); font-size: 0.92rem; flex: 1 1 0; min-width: 0; } .stairs li > span { flex: 1 1 100%; color: var(--ink-soft); }

.stairs.mid li { margin-inline: auto; }
.cards { display: grid; grid-template-columns: repeat(var(--cols, 3), minmax(0, 1fr)); gap: 8px !important; }
.cards li { display: flex; flex-direction: column; gap: 3px; padding: 10px 11px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 10px; font-size: 0.84rem; line-height: 1.35; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.cards li > b { font-family: var(--font-display); font-size: 0.92rem; } .cards li > span { color: var(--ink-soft); }
.cards .mark { font-style: normal; color: var(--accent); font-size: 1rem; letter-spacing: 0.12em; line-height: 1.2; }
@media (max-width: 620px) { .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

/* huis met zuilen */
.pil { display: flex; flex-direction: column; gap: 6px; }
.pil-roof { text-align: center; font-family: var(--font-display); font-weight: 800; font-stretch: 104%; padding: 10px 9%; background: var(--accent); color: var(--on-accent); clip-path: polygon(5% 0, 95% 0, 100% 100%, 0 100%); font-size: 0.95rem; line-height: 1.25; }
.pil-cols { display: grid; grid-template-columns: repeat(var(--n), minmax(0, 1fr)); gap: 6px !important; }
.pil-cols li { display: flex; flex-direction: column; align-items: center; gap: 4px; padding: 10px 7px; background: var(--sheet); border: 1px solid var(--rule); border-top: 4px solid var(--accent); border-radius: 4px; font-size: 0.8rem; line-height: 1.35; text-align: center; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.pil-cols li > b { font-family: var(--font-display); font-size: 0.88rem; line-height: 1.2; } .pil-cols li > span { color: var(--ink-soft); }
.pil-base { text-align: center; font-size: 0.82rem; padding: 7px 10px; background: var(--sunk); border-radius: 4px; color: var(--ink-soft); }
@media (max-width: 620px) {
  .pil-roof { clip-path: none; border-radius: 10px 10px 0 0; padding-inline: 12px; }
  .pil-cols { grid-template-columns: 1fr; }
  .pil-cols li { flex-direction: row; flex-wrap: wrap; align-items: baseline; text-align: left; gap: 2px 8px; border-top: 1px solid var(--rule); border-left: 4px solid var(--accent); padding: 8px 10px; }
  .pil-cols li > b { flex: 1 1 0; min-width: 0; } .pil-cols li > span { flex: 1 1 100%; }
}

/* ijsberg */
.berg { border: 1px solid var(--rule); border-radius: 10px; overflow: hidden; background: var(--sheet); font-size: 0.86rem; line-height: 1.4; }
.berg-top, .berg-sub { display: grid; grid-template-columns: 70px minmax(0, 1fr); gap: 0 14px; padding-inline: 10px 14px; }
.berg-top { align-items: end; padding-top: 12px; }
.berg-top i { display: block; height: 44px; background: color-mix(in srgb, var(--s2) 38%, var(--sheet)); clip-path: polygon(50% 0, 80% 100%, 20% 100%); }
.berg-top > div { padding-bottom: 10px; display: flex; flex-direction: column; }
.berg-sub { background: var(--s2-soft); border-top: 2px solid color-mix(in srgb, var(--s2) 60%, transparent); padding-bottom: 12px; }
.berg-sub i { display: block; min-height: 104px; background: color-mix(in srgb, var(--s2) 38%, var(--sheet)); clip-path: polygon(20% 0, 80% 0, 100% 40%, 68% 100%, 34% 90%, 0 48%); }
.berg-sub > div { padding-top: 10px; display: flex; flex-direction: column; gap: 8px; }
.berg span { color: var(--ink-soft); }
.chips { display: flex; flex-direction: row; flex-wrap: wrap; gap: 6px !important; }
.chips li { padding: 3px 10px; border-radius: 999px; background: var(--sheet); border: 1px solid var(--rule); font-size: 0.82rem; line-height: 1.4; }
@media (max-width: 480px) { .berg-top, .berg-sub { grid-template-columns: 46px minmax(0, 1fr); gap: 0 10px; } }

/* raster */
.pgrid { display: grid; grid-template-columns: auto repeat(var(--n), minmax(0, 1fr)); gap: 6px; font-size: 0.84rem; line-height: 1.4; }
.pgrid .ch { font-weight: 700; font-size: 0.82rem; text-align: center; padding: 4px 6px; border-radius: 6px; background: var(--sunk); align-self: end; }
.pgrid .ch.corner { background: none; }
.pgrid .rh { font-weight: 700; align-self: center; padding-right: 4px; max-width: 9.5em; overflow-wrap: break-word; hyphens: auto; }
.pgrid .c { display: flex; flex-direction: column; gap: 2px; padding: 8px 10px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; min-width: 0; overflow-wrap: break-word; hyphens: auto; }
.pgrid .c small { color: var(--ink-soft); font-size: 0.8rem; }
.pgrid .c.empty { background: none; border-style: dashed; }
@media (max-width: 620px) {
  .pgrid { grid-template-columns: 1fr; gap: 5px; }
  .pgrid .ch, .pgrid .c.empty { display: none; }
  .pgrid .rh { margin-top: 8px; max-width: none; font-size: 0.9rem; font-family: var(--font-display); } .pgrid .rh:first-of-type { margin-top: 0; }
  .pgrid .c::before { content: attr(data-col); font-weight: 700; font-size: 0.78rem; color: var(--accent); }
}

/* staven */
.legend { display: flex; flex-direction: row; flex-wrap: wrap; gap: 4px 16px !important; font-size: 0.82rem; color: var(--ink-soft); }
.legend li { display: inline-flex; align-items: center; gap: 6px; }
.legend i, .seg-key i { flex: none; width: 11px; height: 11px; border-radius: 3px; }
.legend i.ref { width: 0; height: 14px; border-radius: 0; border-left: 2px solid var(--ink); background: none !important; margin-inline: 4px; }
.c1 { background: var(--c1); } .c2 { background: var(--c2); } .c3 { background: var(--c3); } .c4 { background: var(--c4); } .c0 { background: color-mix(in srgb, var(--ink-soft) 70%, transparent); }
.bars { display: flex; flex-direction: column; gap: 10px; }
.bar-row { display: flex; flex-direction: column; gap: 3px; min-width: 0; }
.bar-label { font-size: 0.86rem; line-height: 1.3; } .bar-label small { color: var(--ink-soft); font-size: 0.82rem; }
.bar-track { position: relative; display: flex; align-items: center; gap: 2px; height: 22px; }
.bar-track i { flex: none; display: block; height: 18px; min-width: 3px; }
.bar-track i:last-of-type { border-radius: 0 4px 4px 0; }
.bar-track i.neg { border-radius: 4px 0 0 4px; }
.bar-track b { margin-left: 6px; font-size: 0.84rem; white-space: nowrap; font-variant-numeric: tabular-nums; }
.bar-track u { position: absolute; top: -3px; bottom: -3px; width: 2px; margin-left: -1px; background: var(--ink); box-shadow: 0 0 0 2px var(--paper); text-decoration: none; }
.seg { display: flex; gap: 2px; height: 22px; }
.seg i { min-width: 3px; height: 100%; } .seg i:first-child { border-radius: 4px 0 0 4px; } .seg i:last-child { border-radius: 0 4px 4px 0; }
.seg-key { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 8px 16px !important; font-size: 0.84rem; line-height: 1.35; }
.seg-key li { display: grid; grid-template-columns: 11px minmax(0, 1fr); gap: 1px 8px; align-items: baseline; align-content: start; }
.seg-key i { align-self: center; } .seg-key small { grid-column: 2; color: var(--ink-soft); font-size: 0.8rem; }

/* svg-grafieken */
.chart { display: block; width: 100%; height: auto; overflow: visible; }
.chart text { font-family: var(--font-body); font-size: 12.5px; fill: var(--ink); }
.chart .mut { fill: var(--ink-soft); } .chart .bold { font-weight: 700; }
.chart .ax { stroke: var(--ink-soft); stroke-width: 1; fill: none; } .chart .gl { stroke: var(--rule); stroke-width: 1; fill: none; }
.chart .l1 { stroke: var(--c1); } .chart .l2 { stroke: var(--c2); } .chart .l3 { stroke: var(--c3); } .chart .l4 { stroke: var(--c4); }
.chart .ln { stroke-width: 2; fill: none; stroke-linecap: round; stroke-linejoin: round; }
.chart .dash { stroke: var(--ink-soft); stroke-width: 1; stroke-dasharray: 3 3; fill: none; }
.chart .f1 { fill: var(--c1); } .chart .f2 { fill: var(--c2); } .chart .f3 { fill: var(--c3); } .chart .f4 { fill: var(--c4); } .chart .fs { fill: var(--paper); }
.chart .ring { stroke: var(--paper); stroke-width: 2; }
@media (max-width: 480px) { .fig { padding: 12px 12px 14px; } }
"""
