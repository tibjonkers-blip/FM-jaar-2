"""Zet de samenvattingen (markdown-export van de Claude-documenten) om naar pagina's in site/samenvattingen/<vak>/.

Bron: scripts/samenvattingen/<vak>/overzicht.md en week-1.md t/m week-7.md.
Het tabblad "Logboek portfolio" van Praktijkproject staat bewust niet op de site: dat is persoonlijk en de site is openbaar.

Gebruik: python3 scripts/build_samenvattingen.py
"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "samenvattingen")
OUT = os.path.join(ROOT, "site", "samenvattingen")

VAKKEN = {
    "inkoop-recht": dict(
        heading="Inkoop en recht", oefen="../../inkoop-recht/",
        doc="https://claude.ai/artifact/VHXx8mhoAqU8B2DEmeEpsg",
        accent=("#0b6a7d", "#e0eff2", "#62c4d7", "#13313a"),
        line="Per week de lesstof van Inkoop en van Recht, met de modellen, beginselen en arresten die je in het casustentamen moet kunnen toepassen.",
        quiz=("https://claude.ai/artifact/EiKpj8QHxrp7C9eTyErJyQ", "../../inkoop-recht/")),
    "hrm": dict(
        heading="HRM voor de FM-professional", oefen="../../hrm/",
        doc="https://claude.ai/artifact/F5i831ZTxpUePeyVdzXz8C",
        accent=("#7a3566", "#f4e6ef", "#e39ac9", "#34192b"),
        line="Per week het theoriecollege HRM, het arbeidsrechtcollege en de workshop gespreksvoering, zodat je alles hardop kunt uitleggen op het mondeling.",
        quiz=("https://claude.ai/artifact/Y4EBH9n2uzMQ3i5KkDeVQY", "../../hrm/")),
    "praktijkproject": dict(
        heading="Praktijkproject Business Management", oefen="../../praktijkproject/",
        doc="https://claude.ai/artifact/MNHrxykYerRjrc76rQu4Qg",
        accent=("#8a5a12", "#f5ead9", "#e3b466", "#33260f"),
        line="Per week de modellen voor je adviespresentatie, met tips voor je portfolio. Oefenvragen, weektoetsen en een eindtoets staan op de oefenpagina. Je logboek voor het portfolio staat alleen in je Claude-document.",
        quiz=None),
}

# ---------------------------------------------------------------- bronbewerking

def clean_source(md, slug, c):
    """Haalt Claude-specifieke stukken uit de export en zet links om naar de site."""
    md = re.sub(r"^[A-Z][a-z]{2} \d{1,2}, \d{4} · @\S+\s*$\n?", "", md, flags=re.M)  # datum en naam
    if c["quiz"]:
        md = md.replace(f"]({c['quiz'][0]})", f"]({c['quiz'][1]})")
    # lege "Na de les aangevuld"-blokken weglaten
    md = re.sub(r"^### Na de les aangevuld\s*\n\s*\*Nog leeg[^\n]*\*\s*(\n|$)", "", md, flags=re.M)
    md = md.replace('ik vul het blok "Na de les aangevuld" aan', "ik vul de samenvatting dan aan")
    md = md.replace("Per les vind je een samenvatting in een eigen tab (Week 1, Week 2, ...).",
                    "Per les vind je hieronder een samenvatting, per week gegroepeerd.")
    md = md.replace("Lees vóór de les de samenvatting in de tab van die week.", "Lees vóór de les de samenvatting van die week.")
    md = md.replace("De oefenvragen staan in de quizpagina van dit vak.",
                    "De oefenvragen en weektoetsen staan op de oefenpagina van dit vak.")
    md = md.replace("Er is geen tentamen, dus in dit document staan geen quizvragen.",
                    "Er is geen tentamen. Om de modellen te oefenen staan er wel oefenvragen, weektoetsen en een eindtoets op de oefenpagina van dit vak.")
    md = md.replace("Wel vind je per les de modellen die je in je advies moet kunnen toepassen, en een logboek voor je portfolio.",
                    "Hier vind je per les de modellen die je in je advies moet kunnen toepassen. Je logboek voor het portfolio staat niet op deze openbare site, alleen in je Claude-document.")
    md = md.replace('Vul daarom elke week de tab "Logboek portfolio" in',
                    f'Vul daarom elke week het logboek in (tab "Logboek portfolio" in je [Claude-document]({c["doc"]}))')
    return md

FORMULA = """<div class="formula" role="math" aria-label="verkoopprijs is 100 gedeeld door 100 min marge procent, maal kostprijs, is 100 gedeeld door 80 maal 6, is 7,50">
<span class="grp"><span>verkoopprijs</span><span class="op">=</span></span>
<span class="grp"><span class="frac"><span>100</span><span>100 − marge%</span></span><span class="op">×</span><span>kostprijs</span></span>
<span class="grp"><span class="op">=</span><span class="frac"><span>100</span><span>80</span></span><span class="op">×</span><span>6</span></span>
<span class="grp"><span class="op">=</span><b>€ 7,50</b></span></div>"""

MATRIX = """<figure class="matrix" aria-label="Impact/Effort-matrix met vier kwadranten">
<div class="m-axis-y"><span>Impact</span><small>hoog ↑ laag</small></div>
<div class="m-grid">
<div class="m-q win"><b>Quick wins</b><small>veel impact, weinig moeite</small><span>Snel effect, kweekt draagvlak</span><em>Vb: verplichte velden en een automatische ontvangstbevestiging (servicedesk)</em></div>
<div class="m-q big"><b>Structurele verbetering</b><small>veel impact, meer moeite</small><span>Pakt de oorzaak bij de wortel aan</span><em>Vb: automatische routering en een meldingenbord (servicedesk)</em></div>
<div class="m-q fill"><b>Fill-ins</b><small>weinig impact, weinig moeite</small></div>
<div class="m-q no"><b>Niet doen</b><small>weinig impact, veel moeite</small></div>
</div>
<div class="m-axis-x"><small>laag</small><span>Moeite (effort)</span><small>hoog</small></div>
</figure>"""

# ---------------------------------------------------------------- inline

ESC = re.compile(r"\\([\\`*_{}\[\]()#+\-.!|>~])")

def inline(s):
    keep = []
    def stash(m):
        keep.append(html.escape(m.group(1)))
        return f"\x00{len(keep) - 1}\x00"
    s = ESC.sub(stash, s)
    s = html.escape(s, quote=False)
    def link(m):
        text, url = m.group(1), m.group(2)
        ext = url.startswith("http")
        attrs = ' target="_blank" rel="noopener"' if ext else ""
        return f'<a href="{html.escape(url)}"{attrs}>{text}</a>'
    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], s)
    return s

def plain(s):
    return re.sub(r"<[^>]+>", "", inline(s))

# ---------------------------------------------------------------- blokken

CALLOUTS = [
    (re.compile(r"^De kern:\s*"), "kern", "De kern"),
    (re.compile(r"^\*\*Tastba(?:re|ar) product(?:en)? deze week\*\*:\s*"), "product", "Tastbaar product deze week"),
    (re.compile(r"^\*\*Kritische noot\*\*:?\s*|^Kritische noot:\s*"), "warn", "Kritische noot"),
    (re.compile(r"^\*\*Kritische tip\*\*:?\s*"), "warn", "Kritische tip"),
    (re.compile(r"^\*\*Let op\*\*:?\s*|^Let op:\s*"), "warn", "Let op"),
    (re.compile(r"^\*\*Voor je portfolio\*\*:?\s*"), "portfolio", "Voor je portfolio"),
]

def para(text):
    for rx, cls, label in CALLOUTS:
        if rx.match(text):
            body = rx.sub("", text, count=1)
            body = body[:1].upper() + body[1:]
            return f'<div class="callout {cls}"><span class="c-label">{label}</span><p>{inline(body)}</p></div>'
    m = re.match(r"^(Uit de notities|Tip uit de notities):\s*", text)
    if m:
        body = text[m.end():]
        return f'<p><span class="from-notes">{m.group(1)}</span> {inline(body[:1].upper() + body[1:])}</p>'
    return f"<p>{inline(text)}</p>"

def table(rows):
    def cells(line):
        line = line.strip()
        if line.startswith("|"): line = line[1:]
        if line.endswith("|"): line = line[:-1]
        return [x.strip() for x in line.split("|")]
    head = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    corner = head[0] == ""
    out = ['<div class="scroll"><table>', "<thead><tr>"]
    out += [f"<th>{inline(h)}</th>" for h in head]
    out.append("</tr></thead><tbody>")
    for r in body:
        r = (r + [""] * len(head))[: len(head)]
        out.append("<tr>")
        for i, v in enumerate(r):
            tag = "th" if (i == 0 and corner) else "td"
            out.append(f"<{tag}>{inline(v)}</{tag}>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

LI = re.compile(r"^(\s*)(?:(\d+)\.|[-*])\s+(.*)$")

def lists(lines):
    """Lijsten met één nestingsniveau (3 of meer spaties inspringen)."""
    out, stack = [], []  # stack: list of (indent, tag)
    for line in lines:
        m = LI.match(line)
        if not m:  # vervolgregel van het laatste item
            out[-1] = out[-1][:-5] + " " + inline(line.strip()) + "</li>"
            continue
        ind, num, text = len(m.group(1)), m.group(2), m.group(3)
        tag = "ol" if num else "ul"
        if not stack or ind > stack[-1][0]:
            start = f' start="{num}"' if num and num != "1" and not stack else ""
            if stack:  # sublijst in het laatste item
                out[-1] = out[-1][:-5]
            out.append(f"<{tag}{start}>")
            stack.append((ind, tag))
        else:
            while stack and ind < stack[-1][0]:
                out.append(f"</{stack.pop()[1]}></li>")
        out.append(f"<li>{inline(text)}</li>")
    while stack:
        t = stack.pop()[1]
        out.append(f"</{t}>" + ("</li>" if stack else ""))
    return "".join(out)

def blocks(md):
    """Geeft een lijst (soort, data) terug: ('h1'|'h2'|'h3', tekst) of ('html', html)."""
    lines = md.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1; continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            out.append((f"h{min(len(m.group(1)), 4)}", m.group(2).strip())); i += 1; continue
        if line.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"): j += 1
            code = "\n".join(lines[i + 1:j])
            if "verkoopprijs" in code:
                out.append(("html", FORMULA))
            else:
                out.append(("html", f'<div class="scroll"><pre><code>{html.escape(code)}</code></pre></div>'))
            i = j + 1; continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|\s*:?-{3}", lines[i + 1]):
            j = i
            while j < len(lines) and lines[j].startswith("|"): j += 1
            out.append(("html", table(lines[i:j]))); i = j; continue
        if LI.match(line) and not line.startswith(" "):
            j = i
            while j < len(lines) and lines[j].strip() and (LI.match(lines[j]) or lines[j].startswith("   ")): j += 1
            out.append(("html", lists(lines[i:j]))); i = j; continue
        if line.startswith(">"):
            j = i
            while j < len(lines) and lines[j].startswith(">"): j += 1
            text = " ".join(l.lstrip("> ").strip() for l in lines[i:j])
            out.append(("html", f"<blockquote><p>{inline(text)}</p></blockquote>")); i = j; continue
        if line.startswith("&#91;embedded content: Impact/Effort"):
            out.append(("html", MATRIX)); i += 1; continue
        j = i
        while j < len(lines) and lines[j].strip() and not re.match(r"^(#{1,6}\s|\||```|>)", lines[j]) and not (j > i and LI.match(lines[j])):
            j += 1
        out.append(("html", para(" ".join(l.strip() for l in lines[i:j])))); i = j
    return out

# ---------------------------------------------------------------- lessen en structuur

def stream(tag):
    t = tag.lower()
    if "arbeidsrecht" in t or t.startswith("recht"): return "s2"
    if "workshop" in t or "training" in t: return "s3"
    return "s1"

def split_title(title):
    m = re.match(r"^(.*?):\s+(.+)$", title)
    if not m:
        return None, title
    tag, rest = m.group(1), m.group(2)
    if re.fullmatch(r"Week \d+", tag):
        tag = "Les"
    return tag, rest[:1].upper() + rest[1:]

def slugify(s):
    s = s.lower()
    for a, b in (("é", "e"), ("ë", "e"), ("è", "e"), ("ï", "i"), ("ö", "o"), ("ü", "u"), ("á", "a"), ("ó", "o")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48]

def render_week(key, label, md):
    bl = blocks(md)
    lessons, cur, sub = [], None, None
    intro = []
    for kind, data in bl:
        if kind == "h1":
            continue
        if kind == "h2":
            if sub is not None:
                cur["parts"].append("</section>")
            tag, title = split_title(data)
            cur = dict(tag=tag, title=title, raw=data, id=f"{key}-{slugify(title)}", parts=[], subs=0)
            lessons.append(cur); sub = None
            continue
        if cur is None:  # tekst vóór de eerste les
            cur = dict(tag=None, title=None, raw=None, id=f"{key}-intro", parts=[], subs=0)
            lessons.append(cur)
        if kind in ("h3", "h4"):
            if sub is not None:
                cur["parts"].append("</section>")
            cur["subs"] += 1
            sid = f"{cur['id']}-{cur['subs']}"
            h = "h3" if kind == "h3" else "h4"
            cur["parts"].append(f'<section class="sub" id="{sid}"><{h}>{inline(data)}</{h}>')
            sub = sid
            continue
        cur["parts"].append(data)
    if sub is not None:
        cur["parts"].append("</section>")
    out = [f'<section class="week" id="{key}" data-label="{html.escape(label)}">']
    named = [l for l in lessons if l["title"]]
    head = [f'<div class="week-head"><span class="week-no">{html.escape(label)}</span>']
    if key != "overzicht" and len(named) > 1:
        head.append('<ul class="toc">')
        for l in named:
            t = f'<span class="tag {stream(l["tag"] or "")}">{html.escape(l["tag"])}</span>' if l["tag"] else ""
            head.append(f'<li><a href="#{l["id"]}">{t}<span>{inline(l["title"])}</span></a></li>')
        head.append("</ul>")
    head.append("</div>")
    out += head
    for l in lessons:
        body = "".join(l["parts"])
        assert body.count("<section") == body.count("</section>"), l["id"]
        out.append(f'<article class="lesson" id="{l["id"]}" data-lesson="{html.escape(l["tag"] or plain(l["title"] or label))}">')
        if l["title"]:
            out.append('<header class="lesson-head">')
            if l["tag"]:
                out.append(f'<span class="tag {stream(l["tag"])}">{html.escape(l["tag"])}</span>')
            out.append(f"<h2>{inline(l['title'])}</h2></header>")
        out.append(f'<div class="prose">{body}</div></article>')
    out.append("</section>")
    return "".join(out)

# ---------------------------------------------------------------- pagina

PAGE = r"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Samenvatting __HEADING__</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="../../favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
/* Een leesboek per vak: één smalle leeskolom, een vaste weekbalk bovenin, per les een kaart met een gekleurd label per leerlijn. */
:root {
  --paper: #f1f4f3; --sheet: #ffffff; --sunk: #e8eeec; --ink: #14201c; --ink-soft: #54625e; --rule: #d5dedb;
  --accent: __A1__; --accent-soft: __A2__; --on-accent: #ffffff;
  --s1: var(--accent); --s1-soft: var(--accent-soft);
  --s2: #4a4f9c; --s2-soft: #e6e7f5;
  --s3: #1c7543; --s3-soft: #def1e5;
  --warn: #8f5d00; --warn-soft: #f8edd3;
  --mark: #fde99a;
  --font-display: "Bricolage Grotesque", "Segoe UI", system-ui, sans-serif;
  --font-body: "Instrument Sans", "Segoe UI", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #0f1514; --sheet: #172020; --sunk: #121a19; --ink: #e4ebe9; --ink-soft: #9badaa; --rule: #283432;
    --accent: __A3__; --accent-soft: __A4__; --on-accent: #0f1514;
    --s2: #a9aef0; --s2-soft: #23254a; --s3: #6dd39a; --s3-soft: #15301f; --warn: #efbd5a; --warn-soft: #33290f; --mark: #5a4a12;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #0f1514; --sheet: #172020; --sunk: #121a19; --ink: #e4ebe9; --ink-soft: #9badaa; --rule: #283432;
  --accent: __A3__; --accent-soft: __A4__; --on-accent: #0f1514;
  --s2: #a9aef0; --s2-soft: #23254a; --s3: #6dd39a; --s3-soft: #15301f; --warn: #efbd5a; --warn-soft: #33290f; --mark: #5a4a12;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: calc(env(safe-area-inset-top, 0px) + 74px); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body {
  margin: 0; background: var(--paper); color: var(--ink); font-family: var(--font-body); font-size: 16px; line-height: 1.6;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px));
  padding-block: 20px 0;
}
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); background: var(--paper); z-index: 10; }
.wrap { max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: 22px; padding-bottom: 96px; }
h1, h2, h3, h4 { font-family: var(--font-display); text-wrap: balance; margin: 0; line-height: 1.15; }
h1 { font-size: clamp(1.9rem, 5.2vw, 2.7rem); font-weight: 800; letter-spacing: -0.02em; }
p { margin: 0; }
a { color: var(--accent); text-underline-offset: 2px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.eyebrow { font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.09em; text-transform: uppercase; color: var(--ink-soft); }

/* kop */
.top { display: flex; flex-direction: column; gap: 10px; }
.crumbs { display: flex; flex-wrap: wrap; gap: 6px 16px; align-items: baseline; font-size: 0.88rem; font-weight: 500; }
.crumbs a { text-decoration: none; } .crumbs a:hover { text-decoration: underline; }
.crumbs .ext::after { content: " ↗"; color: var(--ink-soft); }
.lead { max-width: 62ch; color: var(--ink-soft); font-size: 0.95rem; }

/* zoeken */
.search { position: relative; margin-top: 6px; }
.search input { width: 100%; font: inherit; color: var(--ink); background: var(--sheet); border: 1px solid var(--rule); border-radius: 12px; padding: 11px 14px 11px 40px; }
.search input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
.search svg { position: absolute; left: 13px; top: 50%; transform: translateY(-50%); width: 17px; height: 17px; color: var(--ink-soft); pointer-events: none; }
.results { background: var(--sheet); border: 1px solid var(--rule); border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; }
.results .count { padding: 10px 14px; font-size: 0.82rem; color: var(--ink-soft); border-bottom: 1px solid var(--rule); }
.results a { display: flex; flex-direction: column; gap: 2px; padding: 10px 14px; text-decoration: none; color: var(--ink); border-bottom: 1px solid var(--rule); min-width: 0; }
.results a:last-child { border-bottom: 0; }
.results a:hover { background: var(--accent-soft); }
.results .where { font-family: var(--font-mono); font-size: 0.7rem; letter-spacing: 0.05em; text-transform: uppercase; color: var(--ink-soft); }
.results .what { font-weight: 600; }
.results .snip { font-size: 0.88rem; color: var(--ink-soft); overflow-wrap: anywhere; }
mark { background: var(--mark); color: inherit; border-radius: 2px; padding: 0 1px; }

/* weekbalk */
.weeknav { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; margin-inline: -4px; padding: 8px 4px; background: var(--paper);
  display: grid; grid-template-columns: auto repeat(7, minmax(0, 1fr)); gap: 4px; }
.weeknav::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 1px; background: var(--rule); opacity: 0; transition: opacity .2s; }
.weeknav.stuck::after { opacity: 1; }
.weeknav a { display: flex; align-items: center; justify-content: center; min-height: 40px; padding: 6px 10px; border-radius: 10px; background: var(--sunk);
  color: var(--ink-soft); font-weight: 600; font-size: 0.9rem; text-decoration: none; white-space: nowrap; font-variant-numeric: tabular-nums; }
.weeknav a:hover { color: var(--ink); }
.weeknav a[aria-current="true"] { background: var(--accent); color: var(--on-accent); }
.weeknav .s { display: none; }
@media (max-width: 560px) { .weeknav .l { display: none; } .weeknav .s { display: inline; } .weeknav a { padding: 6px 4px; font-size: 0.86rem; } }

/* week */
.week { display: flex; flex-direction: column; gap: 16px; }
.week + .week { margin-top: 26px; }
.week-head { display: flex; flex-direction: column; gap: 10px; }
.week-no { font-family: var(--font-display); font-weight: 800; font-size: 1.7rem; letter-spacing: -0.015em; }
.toc { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; }
.toc a { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline; padding: 7px 10px; margin-inline: -10px; border-radius: 9px; color: var(--ink); text-decoration: none; }
.toc a:hover { background: var(--sheet); }
.toc a span:last-child { min-width: 0; }

.tag { display: inline-block; font-family: var(--font-mono); font-size: 0.68rem; font-weight: 500; letter-spacing: 0.06em; text-transform: uppercase;
  padding: 3px 8px; border-radius: 999px; background: var(--s1-soft); color: var(--s1); white-space: nowrap; }
.tag.s2 { background: var(--s2-soft); color: var(--s2); }
.tag.s3 { background: var(--s3-soft); color: var(--s3); }

/* les */
.lesson { background: var(--sheet); border: 1px solid var(--rule); border-radius: 16px; padding: 22px; display: flex; flex-direction: column; gap: 16px; min-width: 0;
  }
.lesson-head { display: flex; flex-direction: column; gap: 8px; align-items: flex-start; }
.lesson-head h2 { font-size: 1.4rem; font-weight: 700; letter-spacing: -0.01em; }
.prose { display: flex; flex-direction: column; gap: 14px; min-width: 0; }
.prose > p, .sub > p, .prose li, .sub li { max-width: 68ch; }
.sub { display: flex; flex-direction: column; gap: 12px; padding-top: 14px; border-top: 1px solid var(--rule); min-width: 0; }
.sub:first-child { border-top: 0; padding-top: 0; }
.sub h3 { font-size: 1.1rem; font-weight: 700; }
.sub h4 { font-size: 1rem; font-weight: 700; }
.sub.hit { animation: hit 1.6s ease-out; border-radius: 6px; }
@keyframes hit { from { background: var(--mark); } to { background: transparent; } }
ul, ol { margin: 0; padding-left: 1.4em; display: flex; flex-direction: column; gap: 6px; }
li > ul, li > ol { margin-top: 6px; }
li::marker { color: var(--ink-soft); }
strong { font-weight: 600; }
blockquote { margin: 0; padding: 12px 16px; border-left: 3px solid var(--accent); background: var(--accent-soft); border-radius: 0 10px 10px 0; font-family: var(--font-display); font-weight: 500; font-size: 1.05rem; line-height: 1.45; }

.callout { display: flex; flex-direction: column; gap: 4px; padding: 12px 16px; border-radius: 12px; background: var(--sunk); max-width: 72ch; }
.callout .c-label { font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-soft); }
.callout.kern { background: var(--accent-soft); }
.callout.kern .c-label { color: var(--accent); }
.callout.kern p { font-size: 1.02rem; }
.callout.warn { background: var(--warn-soft); }
.callout.warn .c-label { color: var(--warn); }
.callout.portfolio, .callout.product { background: transparent; border: 1px dashed var(--rule); }
.from-notes { font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--accent); background: var(--accent-soft); padding: 2px 6px; border-radius: 4px; margin-right: 2px; white-space: nowrap; vertical-align: 1px; }

.scroll { overflow-x: auto; max-width: 100%; -webkit-overflow-scrolling: touch; border: 1px solid var(--rule); border-radius: 12px; }
table { border-collapse: collapse; width: 100%; font-size: 0.9rem; line-height: 1.45; }
th, td { text-align: left; vertical-align: top; padding: 9px 12px; border-top: 1px solid var(--rule); min-width: 7.5em; }
thead th { border-top: 0; background: var(--sunk); font-weight: 600; font-size: 0.84rem; }
tbody th { font-weight: 600; background: var(--sunk); }
td:first-child { font-weight: 500; }
pre { margin: 0; padding: 12px 14px; font-family: var(--font-mono); font-size: 0.85rem; }

.formula { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 8px; padding: 16px 18px; border: 1px solid var(--rule); border-radius: 12px; font-variant-numeric: tabular-nums; }
.formula .grp { display: inline-flex; align-items: center; gap: 8px; white-space: nowrap; }
.formula .op { color: var(--ink-soft); }
.formula .frac { display: inline-flex; flex-direction: column; align-items: center; font-size: 0.92em; }
.formula .frac span:first-child { border-bottom: 1.5px solid currentColor; padding: 0 6px 2px; }
.formula .frac span:last-child { padding: 2px 6px 0; }
.formula b { color: var(--accent); font-size: 1.05rem; }

.matrix { margin: 0; display: grid; grid-template-columns: auto minmax(0, 1fr); grid-template-rows: auto auto; gap: 8px; }
.m-axis-y { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; writing-mode: vertical-rl; transform: rotate(180deg); font-weight: 600; font-size: 0.85rem; }
.m-axis-y small, .m-axis-x small { color: var(--ink-soft); font-weight: 400; font-size: 0.75rem; }
.m-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 6px; }
.m-q { border-radius: 12px; padding: 12px; display: flex; flex-direction: column; gap: 3px; background: var(--sunk); min-width: 0; font-size: 0.88rem; line-height: 1.4; overflow-wrap: anywhere; hyphens: auto; }
.m-q b { font-family: var(--font-display); font-size: 1rem; }
.m-q small { color: var(--ink-soft); font-size: 0.78rem; }
.m-q em { font-style: normal; color: var(--ink-soft); font-size: 0.82rem; margin-top: 4px; }
.m-q.win { background: var(--s3-soft); } .m-q.win b { color: var(--s3); }
.m-q.big { background: var(--accent-soft); } .m-q.big b { color: var(--accent); }
.m-q.no b { color: var(--ink-soft); }
.m-axis-x { grid-column: 2; display: flex; justify-content: space-between; align-items: baseline; font-weight: 600; font-size: 0.85rem; padding-inline: 4px; }

.foot { color: var(--ink-soft); font-size: 0.84rem; display: flex; flex-direction: column; gap: 6px; border-top: 1px solid var(--rule); padding-top: 16px; }
.totop { position: fixed; right: max(16px, env(safe-area-inset-right, 0px)); bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 6;
  width: 44px; height: 44px; border-radius: 50%; border: 1px solid var(--rule); background: var(--sheet); color: var(--ink); display: grid; place-items: center; text-decoration: none;
  box-shadow: 0 2px 8px rgba(0,0,0,.12); font-size: 1.1rem; }

@media (max-width: 480px) {
  .lesson { padding: 16px; border-radius: 14px; }
  .lesson-head h2 { font-size: 1.22rem; }
  .callout { padding: 11px 13px; }
  .m-q { padding: 10px; font-size: 0.82rem; }
}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <nav class="crumbs" aria-label="Navigatie">__CRUMBS__</nav>
  <span class="eyebrow">Samenvattingen · periode 2</span>
  <h1>__HEADING__</h1>
  <p class="lead">__LINE__</p>
  <div class="search" role="search">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="Zoek een begrip, model of artikel" autocomplete="off" aria-label="Zoek in de samenvattingen">
  </div>
  <div class="results" id="results" hidden aria-live="polite"></div>
</header>
<nav class="weeknav" id="weeknav" aria-label="Weken">__WEEKNAV__</nav>
<main id="main">
__WEEKS__
</main>
<footer class="foot">
  <span>Gemaakt van je Claude-samenvattingen. Waar een slide alleen een afbeelding was, staat erbij dat de invulling gangbaar is en niet uit de slides komt; check die in de les.</span>
  <span>Laatst opgebouwd: __BUILT__</span>
</footer>
</div>
<a class="totop" href="#top" id="totop" aria-label="Naar boven" hidden>↑</a>
<script>
(function () {
  var nav = document.getElementById("weeknav");
  var links = Array.prototype.slice.call(nav.querySelectorAll("a"));
  var weeks = Array.prototype.slice.call(document.querySelectorAll("section.week"));
  var totop = document.getElementById("totop");
  totop.addEventListener("click", function (e) { e.preventDefault(); window.scrollTo({ top: 0, behavior: "smooth" }); history.replaceState(null, "", location.pathname); });

  function current() {
    var y = nav.getBoundingClientRect().bottom + 24, cur = weeks[0];
    for (var i = 0; i < weeks.length; i++) { if (weeks[i].getBoundingClientRect().top <= y) cur = weeks[i]; }
    links.forEach(function (a) { a.setAttribute("aria-current", a.getAttribute("href") === "#" + cur.id ? "true" : "false"); });
    nav.classList.toggle("stuck", nav.getBoundingClientRect().top <= (parseFloat(getComputedStyle(nav).top) || 0) + 0.5 && window.scrollY > 40);
    totop.hidden = window.scrollY < 900;
  }
  var ticking = false;
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(function () { ticking = false; current(); }); } }, { passive: true });
  window.addEventListener("resize", current);
  current();

  // ---- zoeken
  var q = document.getElementById("q"), box = document.getElementById("results");
  function norm(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var index = Array.prototype.slice.call(document.querySelectorAll(".sub, .lesson")).filter(function (el) {
    return el.classList.contains("sub") || !el.querySelector(".sub");
  }).map(function (el) {
    var week = el.closest("section.week"), lesson = el.closest(".lesson");
    var h = el.querySelector("h3, h4, h2"), ht = h ? h.textContent.trim() : "";
    var text = (el.innerText || el.textContent).replace(/\s+/g, " ").trim();
    if (ht && text.indexOf(ht) === 0) text = text.slice(ht.length).trim();
    return { el: el, id: el.id, week: week.getAttribute("data-label"), lesson: lesson.getAttribute("data-lesson"),
             title: ht || lesson.getAttribute("data-lesson"), text: text, n: norm(text), nt: norm(ht) };
  });
  function snippet(text, n, term) {
    var i = n.indexOf(term);
    if (i === -1) return esc(text.slice(0, 150)) + (text.length > 150 ? "…" : "");
    var a = Math.max(0, i - 60), b = Math.min(text.length, i + term.length + 90);
    if (a > 0) { var sp = text.indexOf(" ", a); if (sp !== -1 && sp < i) a = sp + 1; }
    var pre = (a > 0 ? "…" : "") + esc(text.slice(a, i)), hit = esc(text.slice(i, i + term.length)), post = esc(text.slice(i + term.length, b)) + (b < text.length ? "…" : "");
    return pre + "<mark>" + hit + "</mark>" + post;
  }
  function run() {
    var term = norm(q.value.trim());
    if (term.length < 2) { box.hidden = true; box.innerHTML = ""; return; }
    var hits = index.filter(function (r) { return r.n.indexOf(term) !== -1 || r.nt.indexOf(term) !== -1; });
    hits.sort(function (a, b) { return (b.nt.indexOf(term) !== -1) - (a.nt.indexOf(term) !== -1); });
    var html = '<div class="count">' + (hits.length ? hits.length + (hits.length === 1 ? " plek" : " plekken") + " gevonden" + (hits.length > 12 ? ", de eerste 12:" : "") : "Niets gevonden. Probeer een ander woord of een kortere zoekterm.") + "</div>";
    hits.slice(0, 12).forEach(function (r) {
      html += '<a href="#' + r.id + '"><span class="where">' + esc(r.week) + " · " + esc(r.lesson) + '</span><span class="what">' + esc(r.title) + '</span><span class="snip">' + snippet(r.text, r.n, term) + "</span></a>";
    });
    box.innerHTML = html; box.hidden = false;
  }
  q.addEventListener("input", run);
  q.addEventListener("keydown", function (e) { if (e.key === "Escape") { q.value = ""; run(); } });
  box.addEventListener("click", function (e) {
    var a = e.target.closest("a"); if (!a) return;
    var el = document.getElementById(a.getAttribute("href").slice(1));
    if (el) { el.classList.remove("hit"); void el.offsetWidth; el.classList.add("hit"); }
  });
})();
</script>
</body>
</html>
"""

def build():
    import datetime
    built = datetime.date.today().strftime("%-d-%-m-%Y")
    for slug, c in VAKKEN.items():
        src = os.path.join(SRC, slug)
        parts = [("overzicht", "Overzicht", "overzicht.md")] + [(f"week-{i}", f"Week {i}", f"week-{i}.md") for i in range(1, 8)]
        weeks, navs = [], []
        for key, label, fn in parts:
            md = open(os.path.join(src, fn), encoding="utf-8").read()
            md = clean_source(md, slug, c)
            weeks.append(render_week(key, label, md))
            short = "Info" if key == "overzicht" else label.replace("Week ", "W")
            navs.append(f'<a href="#{key}" aria-current="false"><span class="l">{label}</span><span class="s">{short}</span></a>')
        crumbs = ['<a href="../../" id="top">← Studieplek</a>']
        if c["oefen"]:
            crumbs.append(f'<a href="{c["oefen"]}">Oefenvragen en weektoetsen</a>')
        crumbs.append(f'<a class="ext" href="{c["doc"]}" target="_blank" rel="noopener">Bewerkbare versie in Claude</a>')
        a1, a2, a3, a4 = c["accent"]
        page = PAGE
        for k, v in dict(HEADING=html.escape(c["heading"]), LINE=html.escape(c["line"]), CRUMBS="".join(crumbs), WEEKNAV="".join(navs),
                         WEEKS="\n".join(weeks), BUILT=built, A1=a1, A2=a2, A3=a3, A4=a4).items():
            page = page.replace(f"__{k}__", v)
        assert "__" not in page.replace("__proto__", ""), slug
        os.makedirs(os.path.join(OUT, slug), exist_ok=True)
        open(os.path.join(OUT, slug, "index.html"), "w", encoding="utf-8").write(page)
        print("samenvatting", slug, len(page) // 1024, "KB")

if __name__ == "__main__":
    build()
