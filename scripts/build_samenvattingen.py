"""Zet de samenvattingen (markdown-export van de Claude-documenten) om naar pagina's in site/samenvattingen/<vak>/.

Bron: scripts/samenvattingen/<vak>/overzicht.md en week-1.md t/m week-7.md.
Het tabblad "Logboek portfolio" van Praktijkproject staat bewust niet op de site: dat is persoonlijk en de site is openbaar.

Gebruik: python3 scripts/build_samenvattingen.py
"""
import html, importlib.util, json, os, re
import sitenav

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "scripts", "samenvattingen")
OUT = os.path.join(ROOT, "site", "samenvattingen")

VAKKEN = {
    "inkoop-recht": dict(
        heading="Inkoop en recht", oefen="../../inkoop-recht/",
        doc="https://claude.ai/artifact/VHXx8mhoAqU8B2DEmeEpsg",
        accent=("#0b6f82", "#dff0f3", "#63cfe2", "#123447"), code="IR", band=("#0b6f82", "#0d5e6e"), figuren="inkoop_recht",
        chart=(("#0e86a0", "#b8690a", "#4a4f9c", "#1b7a46"), ("#1f9bb5", "#c08a1e", "#7a82e8", "#2fa870")),
        line="Per week de lesstof van Inkoop en van Recht, met de modellen, beginselen en arresten die je in het casustentamen moet kunnen toepassen.",
        quiz=("https://claude.ai/artifact/EiKpj8QHxrp7C9eTyErJyQ", "../../inkoop-recht/")),
    "hrm": dict(
        heading="HRM voor de FM-professional", oefen="../../hrm/",
        doc="https://claude.ai/artifact/F5i831ZTxpUePeyVdzXz8C",
        accent=("#9a2d6c", "#f6e4ef", "#f095c9", "#3a1a3a"), code="HRM", band=("#8f2a65", "#7a2457"), figuren="hrm",
        chart=(("#9a2d6c", "#b8690a", "#4a4f9c", "#1b7a46"), ("#cf5aa2", "#c08a1e", "#7a82e8", "#2fa870")),
        line="Per week het theoriecollege HRM, het arbeidsrechtcollege en de workshop gespreksvoering, zodat je alles hardop kunt uitleggen op het mondeling.",
        quiz=("https://claude.ai/artifact/Y4EBH9n2uzMQ3i5KkDeVQY", "../../hrm/")),
    "praktijkproject": dict(
        heading="Praktijkproject Business Management", oefen="../../praktijkproject/",
        doc="https://claude.ai/artifact/MNHrxykYerRjrc76rQu4Qg",
        accent=("#9a520a", "#fbecd8", "#f5b65e", "#3a2b1c"), code="BM", band=("#9a520a", "#8a4a0a"), figuren="praktijkproject",
        chart=(("#a85a0b", "#4a4f9c", "#1b7a46", "#9a2d6c"), ("#cc8122", "#7a82e8", "#2fa870", "#cf5aa2")),
        line="Per week de modellen voor je adviespresentatie, met tips voor je portfolio. Oefenvragen, weektoetsen en een eindtoets staan op de oefenpagina. Je logboek voor het portfolio staat alleen in je Claude-document.",
        quiz=None),
}

# ---------------------------------------------------------------- eigen notities per les
# Onder elke les (niet bij het overzicht en losse inleidingen) staat een notitieveld. Wat je daarin typt, staat alleen in de browser
# (localStorage, sleutel fm-notities-<vak>), nooit op de site of in deze repo. Een notitie hangt aan het id van haar les (week-N-<titel>).
# Verandert de titel van een les, dan zou de notitie haar les kwijtraken. Daarom staan alle ids die ooit een notitieveld hadden in
# NOTITIE_SLEUTELS, en stopt de bouw als er een verdwijnt. Zet dan in NOTITIE_ALIASSEN het oude id op het nieuwe; de pagina verhuist
# de notitie bij het openen. (Een notitie zonder les gaat ook zonder alias niet verloren: ze staat dan onderaan in het notitiepaneel.)
NOTITIE_SLEUTELS = os.path.join(SRC, "notitie-sleutels.json")
NOTITIE_ALIASSEN = {"inkoop-recht": {}, "hrm": {}, "praktijkproject": {}}  # oud id -> nieuw id

def check_note_ids(found):
    """found: {vak: [ids]}. Stopt als een eerder bekend id verdwenen is zonder alias; werkt daarna de lijst bij."""
    old = json.load(open(NOTITIE_SLEUTELS, encoding="utf-8")) if os.path.exists(NOTITIE_SLEUTELS) else {}
    gone = []
    for slug, ids in found.items():
        alias = NOTITIE_ALIASSEN.get(slug, {})
        for a, b in alias.items():
            assert b in ids, f"notitie-alias {slug}: {a!r} wijst naar {b!r}, maar die les bestaat niet"
        gone += [f"{slug}: {i}" for i in old.get(slug, []) if i not in ids and i not in alias]
    if gone:
        raise SystemExit("Deze lessen hadden een notitieveld maar bestaan niet meer (titel veranderd?):\n  " + "\n  ".join(gone) +
                         "\nZet in NOTITIE_ALIASSEN (build_samenvattingen.py) per oud id het nieuwe id, zodat de notities meeverhuizen.")
    new = {slug: sorted(set(ids) | set(NOTITIE_ALIASSEN.get(slug, {}))) for slug, ids in found.items()}
    with open(NOTITIE_SLEUTELS, "w", encoding="utf-8") as f:
        json.dump(new, f, ensure_ascii=False, indent=1)
        f.write("\n")

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
        # alleen gewone webadressen, mail en interne links; javascript:, data: e.d. worden platte tekst
        if not re.match(r"(https?://|mailto:|#|\.{0,2}/|[\w-]+(/|\.html|#|$))", url):
            return text
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

def load_figuren(name):
    """Leest scripts/figuren/<name>.py en geeft de lijst FIGUREN terug (leeg als het bestand er niet is)."""
    d = os.path.join(ROOT, "scripts", "figuren")
    f = os.path.join(d, name + ".py")
    if not os.path.exists(f):
        return []
    import sys
    if d not in sys.path:
        sys.path.insert(0, d)
    spec = importlib.util.spec_from_file_location("figuren_" + name, f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.FIGUREN

def place_figuren(bl, figs, key):
    """Zet de figuren van deze week in de blokkenlijst: onder de genoemde kop, bovenaan, onderaan of na een blok met een stukje tekst.
    Stopt met een foutmelding als de kop of de tekst niet precies één keer voorkomt, zodat een figuur nooit stil verdwijnt."""
    out = list(bl)
    for f in figs:
        cur_les, hits = None, []
        for i, (kind, data) in enumerate(out):
            if kind == "h2":
                cur_les = data
                if f["kop"] is None and f["les"] in data:
                    hits.append(i)
            elif kind in ("h3", "h4") and f["kop"] is not None and cur_les and f["les"] in cur_les and html.unescape(plain(data)).strip() == f["kop"]:
                hits.append(i)
        assert len(hits) == 1, f"figuur in {key}: kop {f['les']!r} / {f['kop']!r} komt {len(hits)} keer voor"
        start = hits[0]
        end = next((i for i in range(start + 1, len(out)) if out[i][0] in ("h2", "h3", "h4")), len(out))
        if f["after"]:
            tx = [i for i in range(start + 1, end) if out[i][0] == "html" and f["after"] in html.unescape(re.sub(r"<[^>]+>", "", out[i][1]))]
            assert tx, f"figuur in {key}: tekst {f['after']!r} niet gevonden onder {f['kop']!r}"
            at = tx[0] + 1
        elif f["pos"] == "top":
            at = start + 1
        else:
            at = end
        out.insert(at, ("html", f["html"]))
    return out

def render_week(key, label, md, after="", figs=(), note_ids=None):
    """note_ids: lijst waarin de ids van de lessen met een notitieveld worden verzameld (voor de sleutelcontrole)."""
    bl = place_figuren(blocks(md), figs, key)
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
        out.append(f'<div class="prose">{body}</div>')
        if l["title"] and key != "overzicht":
            # leeg notitieveld; het script onderaan de pagina vult het in (zonder script blijft het verborgen)
            name = (f'{l["tag"]}: ' if l["tag"] else "") + html.unescape(plain(l["title"]))
            out.append(f'<section class="note" id="notitie-{l["id"]}" data-note="{l["id"]}" '
                       f'data-label="{html.escape(label + " · " + name)}" aria-label="{html.escape("Mijn notities bij " + name)}" hidden></section>')
            if note_ids is not None:
                note_ids.append(l["id"])
        out.append("</article>")
    out.append(after)
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,100..900;1,62..125,100..900&display=swap">
<style>
/* Een leesboek per vak, in dezelfde bewegwijzering als de rest van de studieplek: een gekleurde zoneband met het bordje van het vak
   en de zoekbalk, daaronder een vaste weekbalk en per les een kaart met een gekleurd label per leerlijn. */
:root {
  --paper: #eef1f6; --sheet: #ffffff; --sunk: #e4e9f1; --ink: #16202f; --ink-soft: #5a6577; --rule: #d9dfe8;
  --accent: __A1__; --accent-soft: __A2__; --on-accent: #ffffff; --band: __B1__;
  --s1: var(--accent); --s1-soft: var(--accent-soft);
  --s2: #4a4f9c; --s2-soft: #e6e7f5;
  --s3: #1b7a46; --s3-soft: #def2e6;
  --warn: #8f5d00; --warn-soft: #f9eed6;
  --mark: #fde99a;
  --c1: __C1__; --c2: __C2__; --c3: __C3__; --c4: __C4__; /* grafiekkleuren, per thema gecontroleerd op onderscheid en contrast */
  --font-display: "Archivo", "Arial Nova", "Segoe UI", system-ui, sans-serif;
  --font-body: "Archivo", "Segoe UI", system-ui, sans-serif;
  --font-mono: ui-monospace, "Cascadia Mono", Consolas, monospace;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
    --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --band: __B2__;
    --s2: #aab0f2; --s2-soft: #262c5a; --s3: #6fd6a0; --s3-soft: #143224; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
    --c1: __D1__; --c2: __D2__; --c3: __D3__; --c4: __D4__;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #121b2b; --sheet: #1a2539; --sunk: #0e1624; --ink: #e8edf5; --ink-soft: #9eabbf; --rule: #2a3850;
  --accent: __A3__; --accent-soft: __A4__; --on-accent: #111a2a; --band: __B2__;
  --s2: #aab0f2; --s2-soft: #262c5a; --s3: #6fd6a0; --s3-soft: #143224; --warn: #f0c060; --warn-soft: #342a12; --mark: #5a4a12;
  --c1: __D1__; --c2: __D2__; --c3: __D3__; --c4: __D4__;
  color-scheme: dark;
}
* { box-sizing: border-box; }
[hidden] { display: none !important; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: calc(env(safe-area-inset-top, 0px) + var(--sb-h, 0px) + 74px); }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { margin: 0; padding: 0; background: var(--paper); color: var(--ink); font-family: var(--font-body); font-size: 16px; line-height: 1.6; }
.wrap { max-width: 792px; margin: 0 auto; display: flex; flex-direction: column; gap: 22px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 14px 96px; }
h1, h2, h3, h4 { font-family: var(--font-display); text-wrap: balance; margin: 0; line-height: 1.15; }
h1 { font-size: clamp(1.9rem, 5.2vw, 2.7rem); font-weight: 800; font-stretch: 116%; letter-spacing: -0.012em; line-height: 1.08; }
h1, h2, h3, h4 { overflow-wrap: break-word; hyphens: auto; }
@media (max-width: 400px) { h1 { font-size: 1.7rem; font-stretch: 104%; } .lesson-head h2 { font-stretch: 100%; } }
p { margin: 0; }
a { color: var(--accent); text-underline-offset: 2px; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

/* kop: de zoneband van het vak */
.band { background: var(--band); color: #fff; }
.band-in { max-width: 792px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 22px 0; }
.band :focus-visible { outline-color: #fff; }
.lead a { color: #fff; font-weight: 600; white-space: nowrap; } .lead a::after { content: " ↗"; opacity: 0.75; }
__TABS_CSS__
__BAR_CSS__
.title-row { display: flex; align-items: center; gap: 14px; min-width: 0; margin-top: 4px; }
.title-row > div { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
.kind { font-size: 0.92rem; font-weight: 600; color: rgba(255, 255, 255, 0.8); }
.plate { flex: none; min-width: 52px; height: 52px; padding-inline: 8px; border-radius: 10px; background: #fff; color: var(--band);
  display: grid; place-items: center; font-family: var(--font-display); font-weight: 800; font-stretch: 122%; font-size: 1.05rem; letter-spacing: 0.02em; }
.lead { max-width: 62ch; color: rgba(255, 255, 255, 0.86); font-size: 0.95rem; }

/* zoeken */
.search { position: relative; margin-top: 4px; }
.search input { width: 100%; font: inherit; color: var(--ink); background: var(--sheet); border: 1px solid transparent; border-radius: 10px; padding: 12px 14px 12px 42px; }
.search input:focus { outline: none; box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.45); }
.search svg { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 17px; height: 17px; color: var(--ink-soft); pointer-events: none; }
.results { background: var(--sheet); color: var(--ink); border-radius: 10px; display: flex; flex-direction: column; overflow: hidden; }
.results .count { padding: 10px 14px; font-size: 0.82rem; color: var(--ink-soft); border-bottom: 1px solid var(--rule); }
.results a { display: flex; flex-direction: column; gap: 2px; padding: 10px 14px; text-decoration: none; color: var(--ink); border-bottom: 1px solid var(--rule); min-width: 0; }
.results a:last-child { border-bottom: 0; }
.results a:hover { background: var(--accent-soft); }
.results .where { font-size: 0.78rem; font-weight: 600; color: var(--accent); }
.results .what { font-weight: 600; }
.results .snip { font-size: 0.88rem; color: var(--ink-soft); overflow-wrap: anywhere; }
mark { background: var(--mark); color: inherit; border-radius: 2px; padding: 0 1px; }

/* weekbalk */
.weeknav { position: sticky; top: calc(env(safe-area-inset-top, 0px) + var(--sb-h, 0px)); z-index: 5; margin-inline: -4px; padding: 8px 4px; background: var(--paper);
  display: grid; grid-template-columns: auto repeat(7, minmax(0, 1fr)); gap: 4px; }
.weeknav::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 1px; background: var(--rule); opacity: 0; transition: opacity .2s; }
.weeknav.stuck::after { opacity: 1; }
.weeknav a { display: flex; align-items: center; justify-content: center; min-height: 40px; padding: 6px 10px; border-radius: 8px; background: var(--sheet); border: 1px solid var(--rule);
  color: var(--ink-soft); font-weight: 600; font-size: 0.9rem; text-decoration: none; white-space: nowrap; font-variant-numeric: tabular-nums; }
.weeknav a:hover { color: var(--ink); }
.weeknav a[aria-current="true"] { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.weeknav .s { display: none; }
@media (max-width: 560px) { .weeknav .l { display: none; } .weeknav .s { display: inline; } .weeknav a { padding: 6px 4px; font-size: 0.86rem; } }

/* week */
.week { display: flex; flex-direction: column; gap: 16px; }
.week + .week { margin-top: 26px; }
.week-head { display: flex; flex-direction: column; gap: 10px; }
.week-no { font-family: var(--font-display); font-weight: 800; font-stretch: 116%; font-size: 1.75rem; letter-spacing: -0.01em; }
.toc { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 2px; }
.toc a { display: flex; flex-wrap: wrap; gap: 4px 10px; align-items: baseline; padding: 7px 10px; margin-inline: -10px; border-radius: 9px; color: var(--ink); text-decoration: none; }
.toc a:hover { background: var(--sheet); }
.toc a span:last-child { min-width: 0; }

.tag { display: inline-block; font-size: 0.78rem; font-weight: 700;
  padding: 2px 10px; border-radius: 999px; background: var(--s1-soft); color: var(--s1); white-space: nowrap; }
.tag.s2 { background: var(--s2-soft); color: var(--s2); }
.tag.s3 { background: var(--s3-soft); color: var(--s3); }

/* einde van een week: door naar oefenen, de weektoets en de volgende week */
.week-next { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; padding: 14px 16px; border-radius: 14px; background: var(--accent-soft); }
.week-next .wn-label { flex: 1 1 100%; font-weight: 700; font-stretch: 104%; }
.wn-btn { display: inline-flex; align-items: baseline; gap: 8px; padding: 9px 14px; border-radius: 8px; background: var(--sheet); border: 1px solid var(--rule); color: var(--ink); font-weight: 600; font-size: 0.95rem; text-decoration: none; }
.wn-btn:hover { border-color: var(--accent); }
.wn-btn.primary { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.wn-btn small { font-weight: 500; font-size: 0.8rem; opacity: 0.85; }
.wn-btn.quiet { background: transparent; border-color: transparent; color: var(--accent); margin-left: auto; padding-inline: 6px; text-decoration: underline; text-underline-offset: 2px; }
@media (max-width: 480px) { .wn-btn { flex: 1 1 auto; justify-content: center; } .wn-btn.quiet { margin-left: 0; } }

/* les */
.lesson { background: var(--sheet); border: 1px solid var(--rule); border-radius: 14px; padding: 22px; display: flex; flex-direction: column; gap: 16px; min-width: 0;
  }
.lesson-head { display: flex; flex-direction: column; gap: 8px; align-items: flex-start; }
.lesson-head h2 { font-size: 1.4rem; font-weight: 800; font-stretch: 108%; }
.prose { display: flex; flex-direction: column; gap: 14px; min-width: 0; }
.prose > p, .sub > p, .prose li, .sub li { max-width: 68ch; }
.sub { display: flex; flex-direction: column; gap: 12px; padding-top: 14px; border-top: 1px solid var(--rule); min-width: 0; }
.sub:first-child { border-top: 0; padding-top: 0; }
.sub h3 { font-size: 1.1rem; font-weight: 700; font-stretch: 104%; }
.sub h4 { font-size: 1rem; font-weight: 700; }
.sub.hit { animation: hit 1.6s ease-out; border-radius: 6px; }
@keyframes hit { from { background: var(--mark); } to { background: transparent; } }
ul, ol { margin: 0; padding-left: 1.4em; display: flex; flex-direction: column; gap: 6px; }
li > ul, li > ol { margin-top: 6px; }
li::marker { color: var(--ink-soft); }
strong { font-weight: 600; }
blockquote { margin: 0; padding: 12px 16px; border-left: 3px solid var(--accent); background: var(--accent-soft); border-radius: 0 10px 10px 0; font-family: var(--font-display); font-weight: 500; font-size: 1.05rem; line-height: 1.45; }

.callout { display: flex; flex-direction: column; gap: 4px; padding: 12px 16px; border-radius: 12px; background: var(--sunk); max-width: 72ch; }
.callout .c-label { font-size: 0.84rem; font-weight: 700; color: var(--ink-soft); }
.callout.kern { background: var(--accent-soft); }
.callout.kern .c-label { color: var(--accent); }
.callout.kern p { font-size: 1.02rem; }
.callout.warn { background: var(--warn-soft); }
.callout.warn .c-label { color: var(--warn); }
.callout.portfolio, .callout.product { background: transparent; border: 1px dashed var(--ink-soft); }
.from-notes { font-size: 0.76rem; font-weight: 700; color: var(--accent); background: var(--accent-soft); padding: 2px 6px; border-radius: 4px; margin-right: 2px; white-space: nowrap; vertical-align: 1px; }

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
.m-q b { font-family: var(--font-display); font-size: 1rem; font-stretch: 108%; }
.m-q small { color: var(--ink-soft); font-size: 0.78rem; }
.m-q em { font-style: normal; color: var(--ink-soft); font-size: 0.82rem; margin-top: 4px; }
.m-q.win { background: var(--s3-soft); } .m-q.win b { color: var(--s3); }
.m-q.big { background: var(--accent-soft); } .m-q.big b { color: var(--accent); }
.m-q.no b { color: var(--ink-soft); }
.m-axis-x { grid-column: 2; display: flex; justify-content: space-between; align-items: baseline; font-weight: 600; font-size: 0.85rem; padding-inline: 4px; }

__FIG_CSS__

__NOTES_CSS__

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
__SITEBAR__<header class="band" id="top">
<div class="band-in">
  <div class="title-row"><span class="plate" aria-hidden="true">__CODE__</span><div><span class="kind">Samenvattingen per week</span><h1>__HEADING__</h1></div></div>
  <p class="lead">__LINE__ <a href="__DOC__" target="_blank" rel="noopener">Bewerkbare versie in Claude</a></p>
  <div class="search" role="search">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
    <input id="q" type="search" placeholder="Zoek een begrip, model of artikel" autocomplete="off" aria-label="Zoek in de samenvattingen">
  </div>
  <div class="results" id="results" hidden aria-live="polite"></div>
  __TABS__
</div>
</header>
<div class="wrap">
<nav class="weeknav" id="weeknav" aria-label="Weken">__WEEKNAV__</nav>
<main id="main">
__WEEKS__
<section class="notes-panel" id="notities" data-vak="__VAK__" data-heading="__HEADING__" data-alias="__NOTE_ALIAS__" aria-labelledby="np-title" hidden>
  <h2 id="np-title">Je eigen notities</h2>
  <p class="np-count" id="np-count"></p>
  <p id="np-where-off">Wat je onder een les typt, wordt in deze browser op dit apparaat bewaard. Het staat niet op de site en niemand anders kan het zien. Wil je dezelfde notities op je laptop en je telefoon? Koppel dan hieronder elk apparaat met je wachtwoord.</p>
  <p id="np-where-on" hidden>Wat je onder een les typt, wordt in deze browser bewaard en online in je eigen opslag op Netlify, achter je wachtwoord. Zo zie je dezelfde notities op elk apparaat dat je koppelt. Wie de site zonder jouw wachtwoord opent, ziet niets.</p>
  <div class="np-sync">
    <h3>Synchroniseren tussen je apparaten</h3>
    <div id="np-sync-off">
      <p>Vul het wachtwoord in dat je in Netlify bij NOTITIES_WACHTWOORD hebt gezet. Dit apparaat onthoudt daarna een sleutel, niet je wachtwoord zelf. Je koppelt één keer per apparaat; dat geldt dan voor alle drie de vakken.</p>
      <div class="np-row">
        <input type="password" id="np-pw" autocomplete="current-password" placeholder="Wachtwoord voor je notities" aria-label="Wachtwoord voor je notities">
        <button type="button" class="wn-btn primary" id="np-link">Koppel dit apparaat</button>
      </div>
    </div>
    <div id="np-sync-on" hidden>
      <p class="np-sync-state" id="np-sync-state" aria-live="polite"></p>
      <div class="np-actions">
        <button type="button" class="wn-btn" id="np-sync-now">Nu synchroniseren</button>
        <button type="button" class="wn-btn" id="np-unlink">Ontkoppel dit apparaat</button>
      </div>
    </div>
    <p class="np-msg" id="np-sync-msg" role="status" hidden></p>
  </div>
  <div class="callout warn" id="np-warn" hidden><span class="c-label">Deze browser bewaart niets</span><p>Je browser staat opslaan niet toe, bijvoorbeeld in een privévenster. Wat je typt, is weg als je deze pagina sluit. Download je notities voordat je de pagina sluit.</p></div>
  <div class="callout"><span class="c-label">Download af en toe een kopie</span><p>Wis je je browsergegevens, dan zijn je notities op dit apparaat weg. Safari kan bovendien gegevens wissen van een site die je ruim een week niet hebt geopend. Heb je dit apparaat gekoppeld, dan staan ze nog online en komen ze terug zodra je opnieuw koppelt. Een gedownloade kopie is je reserve: daarmee zet je alles terug. Bewaar het bestand bijvoorbeeld in OneDrive of Google Drive.</p></div>
  <div class="np-actions">
    <button type="button" class="wn-btn primary" id="np-download">Download al je notities</button>
    <button type="button" class="wn-btn" id="np-import">Zet terug uit een bestand</button>
    <input type="file" id="np-file" accept=".md,.txt,text/markdown,text/plain" hidden>
  </div>
  <p class="np-msg" id="np-msg" role="status" hidden></p>
  <div class="np-orphans" id="np-orphans" hidden>
    <h3>Notities bij lessen die niet meer op deze pagina staan</h3>
    <p>De titel van deze lessen is veranderd. Je notities zijn er nog: kopieer ze naar de juiste les of laat ze hier staan. Ze gaan mee in je download.</p>
  </div>
</section>
</main>
<footer class="foot">
  <span>Gemaakt van je Claude-samenvattingen. Waar een slide alleen een afbeelding was, staat erbij dat de invulling gangbaar is en niet uit de slides komt; check die in de les.</span>
  <span>Laatst opgebouwd: __BUILT__</span>
</footer>
</div>
<a class="totop" href="#top" id="totop" aria-label="Naar boven" hidden>↑</a>
<button type="button" class="nb-fab" id="nb-fab" aria-expanded="false" aria-controls="notitieblad" hidden><span>Notitieblad</span></button>
<aside class="nb" id="notitieblad" aria-labelledby="nb-title" hidden>
  <div class="nb-head">
    <h2 id="nb-title">Notitieblad</h2>
    <button type="button" class="nb-close" id="nb-close" aria-label="Notitieblad sluiten" title="Sluiten (Esc)">×</button>
  </div>
  <div class="nb-pick">
    <label for="nb-les">Koppel aan les</label>
    <div class="nb-row"><select id="nb-les"></select><button type="button" class="nb-here" id="nb-here" title="Kies de les die nu in beeld is">Les in beeld</button></div>
    <p class="nb-follow" id="nb-follow"></p>
  </div>
  <textarea id="nb-text" class="nb-text" spellcheck="true" placeholder="Typ hier mee tijdens de les. Klik daarna op Opslaan bij les." aria-label="Notitieblad"></textarea>
  <div class="nb-foot">
    <button type="button" class="wn-btn primary" id="nb-save">Opslaan bij les</button>
    <span class="nb-status" id="nb-status" aria-live="polite"></span>
  </div>
  <p class="nb-msg" id="nb-msg" role="status" hidden></p>
</aside>
__NOTES_JS__
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

  // Kom je binnen op een week of een les (#week-3), dan verschuift de tekst nog terwijl het lettertype laadt: zet de plek daarna goed.
  if (location.hash.length > 1) {
    var moved = false;
    ["wheel", "touchstart", "keydown", "mousedown"].forEach(function (ev) { window.addEventListener(ev, function () { moved = true; }, { passive: true, once: true }); });
    var realign = function () {
      var el = document.getElementById(location.hash.slice(1));
      if (el && !moved) { el.scrollIntoView({ behavior: "instant", block: "start" }); current(); }
    };
    window.addEventListener("load", realign);
    if (document.fonts) { document.fonts.ready.then(realign); if (document.fonts.addEventListener) document.fonts.addEventListener("loadingdone", realign); }
  }

  // ---- zoeken
  var q = document.getElementById("q"), box = document.getElementById("results");
  function norm(s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); }
  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var index = Array.prototype.slice.call(document.querySelectorAll(".sub, .lesson")).filter(function (el) {
    return el.classList.contains("sub") || !el.querySelector(".sub");
  }).map(function (el) {
    var week = el.closest("section.week"), lesson = el.closest(".lesson");
    var h = el.querySelector("h3, h4, h2"), ht = h ? h.textContent.trim() : "";
    var src = el.classList.contains("lesson") ? (el.querySelector(".prose") || el) : el;  // zonder het notitieveld
    var text = (src.innerText || src.textContent).replace(/\s+/g, " ").trim();
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
    var mine = window.fmNotes ? window.fmNotes.find(term, norm) : [];  // je eigen notities komen bovenaan
    var total = hits.length + mine.length;
    var html = '<div class="count">' + (total ? total + (total === 1 ? " plek" : " plekken") + " gevonden" + (mine.length ? " (" + mine.length + " in je notities)" : "") + (hits.length > 12 ? ", uit de samenvatting de eerste 12:" : "") : "Niets gevonden. Probeer een ander woord of een kortere zoekterm.") + "</div>";
    mine.slice(0, 6).forEach(function (r) {
      html += '<a href="#' + r.id + '"><span class="where">Mijn notitie</span><span class="what">' + esc(r.label) + '</span><span class="snip">' + snippet(r.text, norm(r.text), term) + "</span></a>";
    });
    hits.slice(0, 12).forEach(function (r) {
      html += '<a href="#' + r.id + '"><span class="where">' + esc(r.week) + ", " + esc(r.lesson) + '</span><span class="what">' + esc(r.title) + '</span><span class="snip">' + snippet(r.text, r.n, term) + "</span></a>";
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
__BAR_JS__
</body>
</html>
"""

NOTES_CSS = """/* eigen notities per les (alleen in de browser bewaard) */
.lesson-head.has-jump { display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 8px 12px; }
.lesson-head.has-jump .tag { grid-column: 1; grid-row: 1; justify-self: start; }
.lesson-head.has-jump h2 { grid-column: 1 / -1; grid-row: 2; }
.note-jump { grid-column: 2; grid-row: 1; display: inline-flex; align-items: center; gap: 6px; min-height: 30px; padding: 3px 11px 3px 9px; border-radius: 999px;
  border: 1px solid var(--rule); color: var(--ink-soft); font-size: 0.82rem; font-weight: 600; text-decoration: none; white-space: nowrap; }
.note-jump:hover { color: var(--accent); border-color: var(--accent); }
.note-jump.has { background: var(--accent-soft); border-color: transparent; color: var(--accent); }
.note-jump svg, .note-add svg, .note-pin svg { width: 16px; height: 16px; flex: none; }
.toc a.has-note > span:last-child::after { content: "notitie"; display: inline-block; margin-left: 8px; padding: 0 7px; border-radius: 999px; background: var(--accent-soft); color: var(--accent);
  font-size: 0.72rem; font-weight: 700; line-height: 1.6; vertical-align: 1px; }

.note { min-width: 0; display: flex; flex-direction: column; gap: 8px; }
.note-add { display: flex; align-items: center; gap: 10px; width: 100%; padding: 12px 14px; border: 1px dashed var(--ink-soft); border-radius: 12px; background: transparent;
  color: var(--ink-soft); font: inherit; font-weight: 600; text-align: left; cursor: pointer; }
.note-add:hover { color: var(--accent); border-color: var(--accent); background: var(--accent-soft); }
.note.open .note-add { display: none; }
.note-box { display: none; flex-direction: column; gap: 8px; padding: 12px 14px 10px; border-radius: 12px; background: var(--sunk); border: 1px solid var(--rule); }
.note.open .note-box { display: flex; }
.note-bar { display: flex; flex-wrap: wrap; align-items: center; gap: 4px 12px; }
.note-title { font-weight: 700; font-stretch: 104%; }
.note-status { flex: 1 1 auto; font-size: 0.8rem; color: var(--ink-soft); }
.note-status.err { color: var(--warn); font-weight: 600; flex-basis: 100%; order: 9; }
.note-pin { display: inline-flex; align-items: center; gap: 6px; min-height: 34px; padding: 5px 11px 5px 9px; border-radius: 8px; border: 1px solid var(--rule); background: var(--sheet);
  color: var(--ink); font: inherit; font-size: 0.84rem; font-weight: 600; cursor: pointer; }
.note-pin:hover { border-color: var(--accent); }
.note-pin[aria-pressed="true"] { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.note-text { display: block; width: 100%; min-height: 7.6em; resize: none; overflow: hidden; font: inherit; font-size: 1rem; line-height: 1.55; color: var(--ink);
  background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; padding: 10px 12px; }
.note-text:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 22%, transparent); }
.note-text::placeholder { color: var(--ink-soft); opacity: 0.85; }
.note-foot { font-size: 0.8rem; color: var(--ink-soft); }
.note-foot button { padding: 0; border: 0; background: none; font: inherit; color: var(--accent); text-decoration: underline; text-underline-offset: 2px; cursor: pointer; }
.note-label { font-weight: 600; font-size: 0.92rem; }
.note.pinned { position: sticky; bottom: calc(var(--kb, 0px) + env(safe-area-inset-bottom, 0px) + 10px); z-index: 4; }
.note.pinned .note-box { background: var(--sheet); border-color: var(--accent); box-shadow: 0 10px 32px rgba(10, 18, 36, 0.24); }
.note.pinned .note-text { max-height: 30vh; overflow-y: auto; }
.note.pinned .note-foot { display: none; }
@media (max-width: 560px) {  /* telefoon: meescrollend veld compact houden, zodat de samenvatting leesbaar blijft */
  .note.pinned .note-box { padding: 8px 10px; gap: 6px; }
  .note.pinned .note-title, .note.pinned .note-status:not(.err) { display: none; }
  .note.pinned .note-bar { justify-content: flex-end; }
  .note.pinned .note-pin { min-height: 30px; padding-block: 3px; }
  .note.pinned .note-text { min-height: 4.8em; max-height: 20vh; }
}
.note.hit .note-box { animation: hit 1.6s ease-out; }
body.note-pinned .totop { display: none; }

.notes-panel { margin-top: 26px; background: var(--sheet); border: 1px solid var(--rule); border-radius: 14px; padding: 22px; display: flex; flex-direction: column; gap: 14px; min-width: 0; }
.notes-panel h2 { font-size: 1.4rem; font-weight: 800; font-stretch: 108%; }
.notes-panel > p, .notes-panel .callout { max-width: 68ch; }
.np-count { font-weight: 600; }
.np-actions { display: flex; flex-wrap: wrap; gap: 8px; }
button.wn-btn { font-family: inherit; cursor: pointer; }
.np-msg { padding: 10px 14px; border-radius: 10px; background: var(--s3-soft); color: var(--ink); max-width: 68ch; }
.np-msg.err { background: var(--warn-soft); }
.np-sync { display: flex; flex-direction: column; gap: 10px; padding: 14px 16px; border-radius: 12px; border: 1px solid var(--rule); max-width: 72ch; }
.np-sync h3 { font-size: 1.05rem; font-weight: 700; font-stretch: 104%; }
.np-sync > div { display: flex; flex-direction: column; gap: 10px; }
.np-row { display: flex; flex-wrap: wrap; gap: 8px; }
.np-row .wn-btn { align-items: center; }
.np-row input { flex: 1 1 220px; min-width: 0; font: inherit; color: var(--ink); background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; padding: 9px 12px; }
.np-row input:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 22%, transparent); }
.np-sync-state { font-weight: 600; }
.np-sync-state.err { color: var(--warn); }
button.wn-btn:disabled { opacity: 0.6; cursor: wait; }
.np-orphans { display: flex; flex-direction: column; gap: 12px; padding-top: 14px; border-top: 1px solid var(--rule); }
.np-orphans h3 { font-size: 1.1rem; font-weight: 700; font-stretch: 104%; }
@media (max-width: 480px) { .notes-panel { padding: 16px; } .note-box { padding: 10px 11px 9px; } }
/* notitieblad: los blad dat in beeld blijft; opslaan zet de tekst bij de gekozen les */
.nb-fab { position: fixed; right: max(16px, env(safe-area-inset-right, 0px)); bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 7;
  display: inline-flex; align-items: center; gap: 8px; min-height: 46px; padding: 10px 16px 10px 13px; border: 0; border-radius: 999px; background: var(--accent); color: var(--on-accent);
  font: inherit; font-weight: 700; cursor: pointer; box-shadow: 0 8px 24px rgba(10, 18, 36, 0.28); }
.nb-fab svg { width: 18px; height: 18px; flex: none; }
.nb-fab:hover { filter: brightness(1.08); }
body.has-nb .totop { bottom: calc(76px + env(safe-area-inset-bottom, 0px)); }
body.nb-open .nb-fab, body.nb-open .totop { display: none; }
.nb { position: fixed; z-index: 30; display: flex; flex-direction: column; gap: 10px; padding: 14px 16px 16px; background: var(--sheet); color: var(--ink);
  border: 1px solid var(--accent); box-shadow: 0 14px 40px rgba(10, 18, 36, 0.3); min-width: 0; }
.nb[hidden] { display: none; }
.nb-head { display: flex; align-items: center; gap: 10px; }
.nb-head h2 { flex: 1 1 auto; font-size: 1.15rem; font-weight: 800; font-stretch: 106%; }
.nb-close { width: 36px; height: 36px; flex: none; border: 1px solid var(--rule); border-radius: 8px; background: var(--sheet); color: var(--ink); font: inherit; font-size: 1.4rem; line-height: 1; cursor: pointer; }
.nb-close:hover { border-color: var(--accent); color: var(--accent); }
.nb-pick { display: flex; flex-direction: column; gap: 5px; min-width: 0; }
.nb-pick label { font-size: 0.84rem; font-weight: 700; color: var(--ink-soft); }
.nb-row { display: flex; gap: 6px; min-width: 0; }
.nb-row select { flex: 1 1 auto; min-width: 0; font: inherit; font-size: 0.92rem; color: var(--ink); background: var(--sheet); border: 1px solid var(--rule); border-radius: 8px; padding: 8px 10px; }
.nb-here { flex: none; font: inherit; font-size: 0.84rem; font-weight: 600; padding: 6px 10px; border: 1px solid var(--rule); border-radius: 8px; background: var(--sheet); color: var(--ink); cursor: pointer; }
.nb-here:hover { border-color: var(--accent); color: var(--accent); }
.nb-row select:focus, .nb-text:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 22%, transparent); }
.nb-follow { font-size: 0.78rem; color: var(--ink-soft); min-height: 1.2em; }
.nb-text { flex: 1 1 auto; min-height: 6em; width: 100%; resize: none; font: inherit; font-size: 1rem; line-height: 1.55; color: var(--ink); background: var(--sunk);
  border: 1px solid var(--rule); border-radius: 8px; padding: 10px 12px; }
.nb-text::placeholder { color: var(--ink-soft); opacity: 0.85; }
.nb-foot { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 12px; }
.nb-status { font-size: 0.8rem; color: var(--ink-soft); }
.nb-msg { font-size: 0.88rem; padding: 8px 12px; border-radius: 8px; background: var(--s3-soft); }
.nb-msg.err { background: var(--warn-soft); }
.nb-msg a { color: var(--accent); font-weight: 600; }
@media (min-width: 1180px) {  /* laptop: blad rechts naast de samenvatting, de tekst schuift op */
  .nb { top: calc(env(safe-area-inset-top, 0px) + var(--sb-h, 0px) + 14px); bottom: 16px; right: 16px; width: 372px; border-radius: 14px; }
  body.nb-open .wrap, body.nb-open .band-in { margin-left: max(16px, calc((100vw - 792px - 404px) / 2)); margin-right: auto; }
}
@media (max-width: 1179.98px) {  /* telefoon en tablet: blad onderin, de samenvatting blijft erboven leesbaar */
  .nb { left: 0; right: 0; bottom: var(--kb, 0px); max-width: 820px; margin: 0 auto; max-height: 52vh; border-radius: 14px 14px 0 0; border-bottom: 0;
    padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px)); gap: 8px; }
  .nb-text { min-height: 5em; }
  body.nb-open main { padding-bottom: 46vh; }
}
@media (max-width: 480px) { .nb { padding: 10px 12px; } .nb-head h2 { font-size: 1.05rem; } .nb-close { width: 32px; height: 32px; } .nb-follow { display: none; } }
@media print { .note:not(.open), .note-pin, .note-foot, .note-jump, .notes-panel, .nb, .nb-fab { display: none !important; } .note-text { height: auto !important; } }"""

NOTES_JS = r"""<script>
/* Eigen notities per les. Ze staan in deze browser (localStorage, sleutel fm-notities-<vak>) en, als je dit apparaat koppelt,
   ook in je eigen online opslag op Netlify (/api/notities, achter je wachtwoord), zodat al je apparaten hetzelfde zien.
   Per les: { t: tekst, u: laatst bewerkt (ISO), l: naam van de les, b: versie online waarop deze tekst voortbouwt }.
   Een gewiste notitie die online stond, blijft als { t: "", b } bewaard, zodat het wissen ook op je andere apparaten aankomt.
   pending: lessen met wijzigingen die nog niet online staan. Downloaden geeft een .md-bestand dat je ook weer terugzet. */
(function () {
  var panel = document.getElementById("notities");
  if (!panel) return;
  var VAK = panel.getAttribute("data-vak"), HEADING = panel.getAttribute("data-heading"), KEY = "fm-notities-" + VAK, SYNC_KEY = "fm-notities-sync";
  var ID = /^[a-z0-9-]{1,90}$/;  // zo zien de ids van lessen eruit (week-3-sourcing); al het andere wordt genegeerd
  var own = function (o, k) { return Object.prototype.hasOwnProperty.call(o, k); };
  var ALIAS = Object.create(null);
  try { var al = JSON.parse(panel.getAttribute("data-alias") || "{}"); if (al && typeof al === "object") Object.keys(al).forEach(function (k) { if (ID.test(k) && typeof al[k] === "string" && ID.test(al[k])) ALIAS[k] = al[k]; }); } catch (e) {}
  var PEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16v4Z"/><path d="m13.5 6.5 4 4"/></svg>';
  var PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 16v6"/><path d="M8.5 3h7l-1 6 3.5 4v3h-12v-3l3.5-4-1-6Z"/></svg>';
  var HINT = "Typ hier tijdens of na de les mee: wat de docent benadrukt, voorbeelden, tentamentips en vragen die je nog hebt.";
  var secs = Object.create(null), timers = Object.create(null), dirty = Object.create(null), pageIds = [], pinned = null;
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); };
  var str = function (v, max) { return typeof v === "string" && v.length <= max ? v : ""; };

  // ---- opslag in deze browser
  var canStore = (function () { try { var k = KEY + ":test"; localStorage.setItem(k, "1"); localStorage.removeItem(k); return true; } catch (e) { return false; } })();
  function empty() { return { notes: Object.create(null), pending: Object.create(null), exported: "" }; }
  // Leest de bewaarde notities. Alleen tekst wordt overgenomen; wat beschadigd of van een ander type is, telt niet mee.
  function read() {
    var out = empty();
    try {
      var raw = localStorage.getItem(KEY); if (!raw) return out;
      var v = JSON.parse(raw);
      if (!v || typeof v !== "object" || Array.isArray(v)) return out;
      if (v.notes && typeof v.notes === "object" && !Array.isArray(v.notes)) {
        Object.keys(v.notes).forEach(function (id) {
          var n = v.notes[id], b = n && str(n.b, 80);
          if (ID.test(id) && n && typeof n === "object" && typeof n.t === "string" && (n.t.trim() || b))
            out.notes[id] = { t: n.t, u: str(n.u, 40), l: str(n.l, 300), b: b };
        });
      }
      if (v.pending && typeof v.pending === "object") Object.keys(v.pending).forEach(function (id) { if (own(out.notes, id)) out.pending[id] = 1; });
      if (typeof v.exported === "string") out.exported = v.exported;
    } catch (e) {}
    return out;
  }
  var store = canStore ? read() : empty();
  function write() {
    if (!canStore) return false;
    try { localStorage.setItem(KEY, JSON.stringify({ v: 1, notes: store.notes, pending: store.pending, exported: store.exported })); return true; }
    catch (e) { canStore = false; $("np-warn").hidden = false; return false; }  // vol of geblokkeerd: verder alleen in het geheugen
  }
  function refresh() { if (canStore) store = read(); }  // eerst ophalen wat een ander tabblad intussen bewaarde
  function live(id) { var n = own(store.notes, id) ? store.notes[id] : null; return n && n.t.trim() ? n : null; }
  function liveIds() { return Object.keys(store.notes).filter(live); }
  var asked = false;
  function askPersist() {  // vraagt de browser de notities niet zomaar op te ruimen
    if (asked) return; asked = true;
    try { if (navigator.storage && navigator.storage.persist) navigator.storage.persisted().then(function (p) { if (!p) return navigator.storage.persist(); }).catch(function () {}); } catch (e) {}
  }

  // ---- tijd
  function when(iso, withTime) {
    var d = new Date(iso); if (isNaN(d)) return "";
    var t = d.toLocaleTimeString("nl-NL", { hour: "2-digit", minute: "2-digit" });
    if (d.toDateString() === new Date().toDateString()) return withTime === false ? "vandaag" : "om " + t;
    var day = d.toLocaleDateString("nl-NL", { day: "numeric", month: "short" });
    return withTime === false ? day : "op " + day + " om " + t;
  }
  function full(iso, withTime) {  // voor in een bestand of in de tekst: altijd een volledige datum
    var d = new Date(iso); if (isNaN(d)) return "";
    var s = d.toLocaleDateString("nl-NL", { day: "numeric", month: "long", year: "numeric" });
    return withTime ? s + " om " + d.toLocaleTimeString("nl-NL", { hour: "2-digit", minute: "2-digit" }) : s;
  }
  function stamp(d) { var p = function (x) { return (x < 10 ? "0" : "") + x; }; return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate()); }

  // ---- een notitieveld
  function labelOf(id) { return secs[id] ? secs[id].getAttribute("data-label") : (own(store.notes, id) && store.notes[id].l) || id; }
  function grow(ta) { if (!ta.offsetParent) return; ta.style.height = "auto"; ta.style.height = (ta.scrollHeight + 2) + "px"; }
  function setStatus(sec, state) {
    var el = sec.querySelector(".note-status"), id = sec.getAttribute("data-note"), n = live(id);
    if (state === "saved" && token) state = store.pending[id] ? (syncErr ? "local" : "pushing") : "synced";
    el.classList.toggle("err", state === "err");
    el.textContent = state === "busy" ? "Wordt bewaard…"
      : state === "err" ? "Niet bewaard: deze browser staat opslaan niet toe. Download je notities voordat je de pagina sluit."
      : state === "pushing" ? "Bewaard, wordt gesynchroniseerd…"
      : state === "local" ? "Bewaard op dit apparaat, nog niet online"
      : state === "synced" ? "Bewaard en gesynchroniseerd " + when(lastSync || new Date().toISOString())
      : state === "saved" ? "Bewaard " + when(n ? n.u : new Date().toISOString())
      : n && n.u ? "Laatst bewerkt " + when(n.u) : "";
  }
  function marks(id) {  // knop bij de les en label in de inhoudsopgave van de week
    var has = !!live(id), sec = secs[id]; if (!sec || sec.classList.contains("orphan")) return;
    var jump = sec.parentNode.querySelector(".note-jump");
    if (jump) { jump.classList.toggle("has", has); jump.lastChild.textContent = has ? "Mijn notities" : "Notitie maken"; }
    var toc = document.querySelector('.toc a[href="#' + id + '"]');
    if (toc) toc.classList.toggle("has-note", has);
  }
  function open(sec, focus) {
    sec.classList.add("open");
    var ta = sec.querySelector("textarea"); grow(ta);
    if (focus) ta.focus({ preventScroll: true });
  }
  function save(id) {
    clearTimeout(timers[id]); delete timers[id];
    if (!dirty[id]) return; delete dirty[id];
    var sec = secs[id], text = sec.querySelector("textarea").value, now = new Date().toISOString();
    refresh();
    var prev = own(store.notes, id) ? store.notes[id] : null;
    if (text.trim()) store.notes[id] = { t: text, u: now, l: sec.getAttribute("data-label") || "", b: prev ? prev.b : "" };
    else if (prev && prev.b) store.notes[id] = { t: "", u: now, l: prev.l, b: prev.b };  // wissen moet ook online gebeuren
    else delete store.notes[id];
    if (own(store.notes, id)) store.pending[id] = 1; else delete store.pending[id];
    var ok = write(), has = !!text.trim();
    setStatus(sec, has ? (ok || token ? "saved" : "err") : "");
    marks(id); info();
    if (ok && has) askPersist();
    schedulePush();
  }
  function flush() { Object.keys(dirty).forEach(save); }
  function setPin(sec) {
    if (sec && document.body.classList.contains("nb-open")) nbOpen(false, false);  // niet twee meescrollende velden tegelijk
    if (pinned) { pinned.classList.remove("pinned"); var b = pinned.querySelector(".note-pin"); b.setAttribute("aria-pressed", "false"); b.lastChild.textContent = "Meescrollen"; }
    pinned = sec || null;
    if (pinned) { pinned.classList.add("pinned"); var c = pinned.querySelector(".note-pin"); c.setAttribute("aria-pressed", "true"); c.lastChild.textContent = "Meescrollen aan"; }
    document.body.classList.toggle("note-pinned", !!pinned);
  }
  function fill(sec) {
    var id = sec.getAttribute("data-note"), n = live(id), ta = sec.querySelector("textarea"), focused = document.activeElement === ta;
    var text = n ? n.t : "";
    if (ta.value !== text) { ta.value = text; if (focused) ta.setSelectionRange(text.length, text.length); }
    if (n || sec.classList.contains("orphan")) sec.classList.add("open");
    else if (pinned !== sec && !focused) sec.classList.remove("open");
    grow(ta); setStatus(sec, ""); marks(id);
  }
  function build(sec, orphan) {
    var id = sec.getAttribute("data-note"), label = sec.getAttribute("data-label") || id;
    secs[id] = sec;
    sec.innerHTML = (orphan ? '<p class="note-label">' + esc(label) + "</p>" : '<button type="button" class="note-add">' + PEN + "<span>Eigen notities bij deze les</span></button>") +
      '<div class="note-box"><div class="note-bar"><span class="note-title">Mijn notities</span><span class="note-status" aria-live="polite"></span>' +
      (orphan ? "" : '<button type="button" class="note-pin" aria-pressed="false" title="Houd dit notitieveld onderin beeld terwijl je door deze les scrolt">' + PIN + "<span>Meescrollen</span></button>") +
      '</div><textarea class="note-text" rows="4" spellcheck="true" placeholder="' + esc(HINT) + '" aria-label="' + esc("Mijn notities bij " + label) + '"></textarea>' +
      '<p class="note-foot"><span class="note-where"></span> <button type="button" class="note-dl">Download een kopie</button> · <a href="#notities" class="note-more"></a></p></div>';
    var ta = sec.querySelector("textarea"), downInside = false;
    sec.addEventListener("pointerdown", function () { downInside = true; setTimeout(function () { downInside = false; }, 400); });
    ta.addEventListener("input", function () {
      dirty[id] = true; grow(ta); setStatus(sec, "busy");
      clearTimeout(timers[id]); timers[id] = setTimeout(function () { save(id); }, 500);
    });
    ta.addEventListener("blur", function () {
      save(id);
      // leeg en weggeklikt: weer inklappen (niet als je op een knop in dit veld klikt)
      setTimeout(function () { if (!orphan && !downInside && !ta.value.trim() && pinned !== sec && !sec.contains(document.activeElement)) sec.classList.remove("open"); }, 0);
    });
    sec.querySelector(".note-dl").addEventListener("click", download);
    if (!orphan) {
      sec.querySelector(".note-add").addEventListener("click", function () { open(sec, true); });
      sec.querySelector(".note-pin").addEventListener("click", function () { setPin(pinned === sec ? null : sec); ta.focus({ preventScroll: true }); });
    }
    where(sec);
    sec.hidden = false;
  }
  function where(sec) {
    sec.querySelector(".note-where").textContent = token ? "Gesynchroniseerd met je andere apparaten." : "Alleen op dit apparaat bewaard.";
    sec.querySelector(".note-more").textContent = token ? "Hoe werkt dit?" : "Koppel je apparaten";
  }
  function redraw() {  // na synchroniseren of terugzetten: velden bijwerken, behalve waar je net typt
    Object.keys(secs).forEach(function (id) { if (!dirty[id]) fill(secs[id]); });
    orphans(); info();
  }

  // ---- paneel onderaan
  function info() {
    var ids = liveIds(), n = ids.length, txt;
    if (!n) txt = "Je hebt nog geen notities bij dit vak. Klik onder een les op ‘Eigen notities bij deze les’ om te beginnen.";
    else {
      txt = "Je hebt notities bij " + n + (n === 1 ? " les" : " lessen") + " van dit vak.";
      var since = ids.filter(function (id) { return !store.exported || (store.notes[id].u || "") > store.exported; }).length;
      if (!store.exported) txt += " Je hebt nog geen kopie gedownload.";
      else if (since) txt += " Sinds je laatste kopie (" + when(store.exported, false) + ") " + (since === 1 ? "is 1 notitie" : "zijn " + since + " notities") + " veranderd.";
      else txt += " Je laatste kopie (" + when(store.exported, false) + ") bevat alles.";
    }
    $("np-count").textContent = txt;
  }
  function msg(text, err) { var el = $("np-msg"); el.textContent = text; el.classList.toggle("err", !!err); el.hidden = false; }
  function orphans() {  // notities waarvan de les niet (meer) op deze pagina staat
    var box = $("np-orphans");
    liveIds().forEach(function (id) {
      if (secs[id]) return;
      var sec = document.createElement("section");
      sec.className = "note open orphan"; sec.id = "notitie-" + id;
      sec.setAttribute("data-note", id); sec.setAttribute("data-label", store.notes[id].l || id);
      box.appendChild(sec); build(sec, true); fill(sec);
    });
    box.hidden = !box.querySelector(".note");
  }

  // ---- downloaden en terugzetten
  function download() {
    flush();
    var ids = pageIds.concat(Object.keys(store.notes).filter(function (id) { return pageIds.indexOf(id) === -1; })).filter(live);
    if (!ids.length) { msg("Je hebt nog geen notities bij dit vak, dus er is nog niets te downloaden.", true); return; }
    var now = new Date(), name = "notities-" + VAK + "-" + stamp(now) + ".md";
    var L = ["# Mijn notities: " + HEADING, "", "<!-- fm-notities " + VAK + " v1 -->",
      "Gedownload van de studieplek op " + full(now.toISOString(), true) + ". Zet dit bestand terug met de knop ‘Zet terug uit een bestand’ onderaan de samenvatting van " + HEADING + ".", ""];
    ids.forEach(function (id) {
      var x = store.notes[id];
      L.push("## " + labelOf(id).replace(/\s+/g, " "), "<!-- notitie " + id + " " + (x.u || "-") + " -->", x.t, "<!-- /notitie -->", "");
    });
    var url = URL.createObjectURL(new Blob([L.join("\n")], { type: "text/markdown;charset=utf-8" }));
    var a = document.createElement("a"); a.href = url; a.download = name; a.hidden = true;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 2000);
    refresh(); store.exported = now.toISOString(); write(); info();
    msg("Gedownload: " + ids.length + (ids.length === 1 ? " notitie" : " notities") + " in " + name + ". Bewaar het bestand buiten je browser, bijvoorbeeld in OneDrive of Google Drive.");
  }
  function restore(txt) {
    txt = txt.replace(/^﻿/, "").replace(/\r\n?/g, "\n");
    var head = txt.match(/<!-- fm-notities (\S+) v1 -->/);
    if (!head) { msg("Dit bestand komt niet van de knop ‘Download al je notities’. Er is niets veranderd.", true); return; }
    if (head[1] !== VAK) {
      var zone = /^[a-z-]{1,40}$/.test(head[1]) && document.querySelector('.sb-zone[href*="/' + head[1] + '/"]');
      msg("Dit bestand hoort bij " + (zone ? zone.title : "een ander vak") + ". Open de samenvatting van dat vak en zet het daar terug. Er is niets veranderd.", true); return;
    }
    flush(); refresh();
    var rx = /(?:^## (.*)\n)?<!-- notitie (\S+) (\S+) -->\n([\s\S]*?)\n?<!-- \/notitie -->/gm, m, added = 0, merged = 0, same = 0, now = new Date().toISOString();
    while ((m = rx.exec(txt))) {
      var id = ALIAS[m[2]] || m[2], u = isNaN(new Date(m[3])) ? "" : m[3], t = m[4];
      if (!ID.test(id) || !t.trim()) continue;
      var cur = live(id), base = own(store.notes, id) ? store.notes[id].b : "";
      if (!cur) { store.notes[id] = { t: t, u: u || now, l: secs[id] ? secs[id].getAttribute("data-label") : str(m[1] || "", 300) || id, b: base }; store.pending[id] = 1; added++; }
      else if (cur.t.indexOf(t) !== -1) same++;
      else if (t.indexOf(cur.t) !== -1) { cur.t = t; cur.u = now; store.pending[id] = 1; merged++; }
      else { cur.t = cur.t.replace(/\s+$/, "") + "\n\nUit je kopie" + (u ? " van " + full(u) : "") + ":\n" + t; cur.u = now; store.pending[id] = 1; merged++; }
    }
    if (!added && !merged && !same) { msg("In dit bestand staan geen notities. Er is niets veranderd.", true); return; }
    var ok = write();
    redraw(); schedulePush();
    var parts = [];
    if (added) parts.push(added + (added === 1 ? " notitie teruggezet" : " notities teruggezet"));
    if (merged) parts.push(merged + (merged === 1 ? " notitie aangevuld met de tekst uit het bestand" : " notities aangevuld met de tekst uit het bestand"));
    if (same) parts.push(same + (same === 1 ? " stond er al" : " stonden er al"));
    msg((ok || token ? "Klaar: " : "Teruggezet, maar alleen tot je deze pagina sluit: ") + parts.join(", ") + ". Je bestaande tekst is nergens overschreven.", !(ok || token));
  }
  $("np-download").addEventListener("click", download);
  $("np-import").addEventListener("click", function () { $("np-file").click(); });
  $("np-file").addEventListener("change", function () {
    var input = this, f = input.files && input.files[0]; if (!f) return;
    if (f.size > 5e6) { msg("Dit bestand is te groot voor een notitiebestand. Er is niets veranderd.", true); input.value = ""; return; }
    var r = new FileReader();
    r.onload = function () { restore(String(r.result || "")); input.value = ""; };
    r.onerror = function () { msg("Het bestand kon niet worden gelezen. Er is niets veranderd.", true); input.value = ""; };
    r.readAsText(f, "utf-8");
  });

  // ---- synchroniseren tussen je apparaten (online opslag op Netlify, zie netlify/functions/notities.mjs)
  function readToken() { try { var v = JSON.parse(localStorage.getItem(SYNC_KEY) || "null"); return v && typeof v.k === "string" && /^[0-9a-f]{64}$/.test(v.k) ? v.k : ""; } catch (e) { return ""; } }
  var token = readToken(), syncing = false, again = false, lastSync = "", syncErr = "", pushTimer = 0;
  function api(method, body, keepalive) {
    var h = { Authorization: "Bearer " + token }; if (body) h["Content-Type"] = "application/json";
    return fetch("/api/notities?vak=" + encodeURIComponent(VAK), { method: method, headers: h, body: body ? JSON.stringify(body) : undefined, cache: "no-store", credentials: "same-origin", keepalive: !!keepalive })
      .then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (j) {
          if (!r.ok || !j || typeof j.notes !== "object") { var e = new Error(j && j.fout || "http-" + r.status); e.status = r.status; throw e; }
          return j;
        });
      });
  }
  // Verwerkt de stand online. Alleen wat op een ander apparaat veranderde, komt binnen; als een notitie hier én daar
  // veranderde, worden beide teksten samengevoegd. Er verdwijnt dus nooit tekst.
  function merge(S) {
    Object.keys(S).forEach(function (id) {
      var s = S[id]; if (!ID.test(id) || !s || typeof s.t !== "string" || typeof s.v !== "string" || dirty[id]) return;
      var L = own(store.notes, id) ? store.notes[id] : null, pend = !!store.pending[id], take = function () {
        // ook een online gewiste notitie onthouden (lege tekst), zodat een nieuwe notitie bij die les meteen online kan
        store.notes[id] = { t: s.t.trim() ? s.t : "", u: str(s.u, 40), l: str(s.l, 300) || (L && L.l) || "", b: s.v };
        delete store.pending[id];
      };
      if (L && L.b === s.v) return;                         // online niets nieuws voor deze les
      if (!L) { take(); return; }
      if (!pend || L.t === s.t) { take(); return; }         // alleen elders veranderd
      if (!s.t.trim()) { L.b = s.v; return; }                // elders gewist, hier bewerkt: tekst blijft
      if (!L.t.trim() || s.t.indexOf(L.t) !== -1) { take(); return; }
      if (L.t.indexOf(s.t) !== -1) { L.b = s.v; return; }
      L.t = s.t.replace(/\s+$/, "") + "\n\n[Samengevoegd: deze les is tegelijk op twee apparaten bewerkt. Hieronder de andere versie, van " + full(L.u, true) + ".]\n" + L.t;
      L.u = new Date().toISOString(); L.b = s.v;
    });
    Object.keys(store.notes).forEach(function (id) {  // stond online, maar is daar weg (opslag leeggemaakt): opnieuw uploaden
      var L = store.notes[id]; if (!L.b || own(S, id)) return;
      L.b = ""; if (L.t.trim()) store.pending[id] = 1; else { delete store.notes[id]; delete store.pending[id]; }
    });
  }
  function round(n) {
    refresh();
    var ids = Object.keys(store.pending).filter(function (id) { return own(store.notes, id) && !dirty[id]; }), sent = Object.create(null), body = { notes: {} };
    ids.forEach(function (id) { var x = store.notes[id]; sent[id] = x.t; body.notes[id] = { t: x.t, u: x.u, l: x.l, b: x.b || "" }; });
    return (ids.length ? api("PUT", body) : api("GET")).then(function (res) {
      refresh();
      (res.accepted || []).forEach(function (id) {
        var x = own(store.notes, id) ? store.notes[id] : null, s = res.notes[id]; if (!x || !s) return;
        x.b = s.v;
        if (x.t === sent[id]) delete store.pending[id];
      });
      merge(res.notes); write();
      var left = Object.keys(store.pending).some(function (id) { return !dirty[id]; });
      if (left && ids.length && n < 3) return round(n + 1);
    });
  }
  function sync() {
    if (!token || !window.fetch) return;
    if (syncing) { again = true; return; }
    syncing = true; again = false; clearTimeout(pushTimer); flush(); syncInfo();
    round(0).then(function () {
      lastSync = new Date().toISOString(); syncErr = "";
    }, function (e) {
      syncErr = e.status === 401 ? "wachtwoord" : e.status === 503 ? "niet-ingesteld" : e.status === 429 || e.status === 409 ? "druk" : "offline";
      if (syncErr === "druk") setTimeout(sync, 20000);
      if (syncErr === "wachtwoord") unlink("Het wachtwoord voor je notities is veranderd. Koppel dit apparaat opnieuw met het nieuwe wachtwoord.");
    }).then(function () {
      syncing = false; redraw(); syncInfo();
      Object.keys(secs).forEach(function (id) { if (!dirty[id] && live(id)) setStatus(secs[id], "saved"); });
      if (again) sync();
    });
  }
  function schedulePush() { if (!token) return; clearTimeout(pushTimer); pushTimer = setTimeout(sync, 2000); }
  function syncInfo() {
    $("np-sync-off").hidden = !!token; $("np-sync-on").hidden = !token;
    $("np-where-off").hidden = !!token; $("np-where-on").hidden = !token;
    Object.keys(secs).forEach(function (id) { where(secs[id]); });
    if (!token) return;
    var st = $("np-sync-state"), pend = Object.keys(store.pending).length;
    st.classList.toggle("err", !!syncErr);
    st.textContent = syncing ? "Bezig met synchroniseren…"
      : syncErr === "offline" ? "Synchroniseren lukt nu niet (geen verbinding?). Je notities staan veilig op dit apparaat en gaan online zodra het weer lukt."
      : syncErr === "niet-ingesteld" ? "De online opslag is uitgezet: NOTITIES_WACHTWOORD ontbreekt in Netlify. Je notities staan veilig op dit apparaat."
      : syncErr === "druk" ? "Het is even druk. De pagina probeert het zo opnieuw; je notities staan veilig op dit apparaat."
      : lastSync ? "Gekoppeld. Laatst gesynchroniseerd " + when(lastSync) + "." + (pend ? " " + pend + (pend === 1 ? " wijziging wacht" : " wijzigingen wachten") + " nog." : "")
      : "Gekoppeld.";
  }
  function sha(text) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(text)).then(function (buf) {
      return Array.prototype.map.call(new Uint8Array(buf), function (b) { return (b < 16 ? "0" : "") + b.toString(16); }).join("");
    });
  }
  function link() {
    var pw = $("np-pw").value, out = $("np-sync-msg");
    var say = function (t, err) { out.textContent = t; out.classList.toggle("err", !!err); out.hidden = false; };
    if (pw.length < 12) { say("Je wachtwoord voor de notities is minstens 12 tekens lang.", true); return; }
    if (!window.crypto || !crypto.subtle || !window.fetch) { say("Deze browser kan niet synchroniseren. Gebruik een recente versie van Chrome, Edge, Firefox of Safari.", true); return; }
    $("np-link").disabled = true; say("Bezig met koppelen…");
    sha("fm-notities:" + pw).then(function (k) {
      var was = token; token = k;
      return api("GET").then(function (res) {
        try { localStorage.setItem(SYNC_KEY, JSON.stringify({ k: k })); } catch (e) {}
        flush(); refresh(); merge(res.notes);
        liveIds().forEach(function (id) { if (!store.notes[id].b) store.pending[id] = 1; });  // wat hier al stond, gaat ook online
        write(); $("np-pw").value = ""; out.hidden = true; syncErr = "";
        sync();
      }, function (e) {
        token = was;
        say(e.status === 401 ? "Dit wachtwoord klopt niet. Gebruik precies het wachtwoord dat in Netlify bij NOTITIES_WACHTWOORD staat."
          : e.status === 503 ? "De online opslag is nog niet ingesteld. Zet in Netlify de omgevingsvariabele NOTITIES_WACHTWOORD (minstens 12 tekens) en publiceer de site daarna opnieuw."
          : e.status === 429 ? "Te veel pogingen. Wacht een minuut en probeer het opnieuw."
          : "De online opslag is niet bereikbaar. Ben je online? Werkt het daarna nog niet, dan staat de functie nog niet op Netlify.", true);
      });
    }).then(function () { $("np-link").disabled = false; syncInfo(); }, function () { $("np-link").disabled = false; say("Koppelen is mislukt. Probeer het opnieuw.", true); });
  }
  function unlink(why) {
    token = ""; lastSync = ""; clearTimeout(pushTimer);
    try { localStorage.removeItem(SYNC_KEY); } catch (e) {}
    var out = $("np-sync-msg"); out.textContent = why; out.classList.toggle("err", /veranderd/.test(why)); out.hidden = false;
    syncInfo(); redraw();
  }
  $("np-link").addEventListener("click", link);
  $("np-pw").addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); link(); } });
  $("np-sync-now").addEventListener("click", sync);
  $("np-unlink").addEventListener("click", function () { unlink("Dit apparaat is ontkoppeld. Je notities staan nog hier en online; nieuwe notities blijven vanaf nu alleen op dit apparaat."); });

  // ---- opbouwen
  Object.keys(ALIAS).forEach(function (old) {  // een les met een nieuwe titel: notitie verhuist mee
    var a = live(old), to = ALIAS[old]; if (!a) return;
    var b = live(to);
    store.notes[to] = b ? { t: b.t.indexOf(a.t) !== -1 ? b.t : b.t.replace(/\s+$/, "") + "\n\n" + a.t, u: b.u, l: b.l, b: b.b } : { t: a.t, u: a.u, l: a.l, b: "" };
    store.pending[to] = 1;
    if (a.b) { store.notes[old] = { t: "", u: new Date().toISOString(), l: a.l, b: a.b }; store.pending[old] = 1; } else { delete store.notes[old]; delete store.pending[old]; }
    write();
  });
  Array.prototype.forEach.call(document.querySelectorAll("section.note[data-note]"), function (sec) {
    var id = sec.getAttribute("data-note");
    pageIds.push(id); build(sec, false);
    var head = sec.parentNode.querySelector(".lesson-head");
    if (head) {
      var j = document.createElement("a");
      j.className = "note-jump"; j.href = "#notitie-" + id; j.innerHTML = PEN + "<span>Notitie maken</span>";
      j.addEventListener("click", function (e) {
        e.preventDefault(); open(sec, false);
        sec.scrollIntoView({ block: "center" }); sec.querySelector("textarea").focus({ preventScroll: true });
      });
      head.appendChild(j); head.classList.add("has-jump");
    }
    fill(sec);
  });
  orphans();
  if (!canStore) $("np-warn").hidden = false;
  info(); syncInfo();
  panel.hidden = false;
  if (token) sync();

  window.addEventListener("pagehide", function () {
    flush();
    if (!token) return;  // laatste wijzigingen nog snel versturen; lukt dat niet, dan gaan ze de volgende keer mee
    var body = { notes: {} }, size = 0;
    Object.keys(store.pending).forEach(function (id) { var x = store.notes[id]; if (x) { body.notes[id] = { t: x.t, u: x.u, l: x.l, b: x.b || "" }; size += x.t.length; } });
    if (size && size < 50000) { try { api("PUT", body, true).catch(function () {}); } catch (e) {} }
  });
  var lastPull = Date.now();
  function pull() { if (token && document.visibilityState === "visible" && Date.now() - lastPull > 15000) { lastPull = Date.now(); sync(); } }
  document.addEventListener("visibilitychange", function () { if (document.visibilityState === "hidden") flush(); else pull(); });
  window.addEventListener("focus", pull);
  window.addEventListener("online", function () { if (token) sync(); });
  setInterval(function () { if (token && document.visibilityState === "visible") { lastPull = Date.now(); sync(); } }, 120000);
  window.addEventListener("storage", function (e) {  // zelfde vak open in een ander tabblad
    if (e.key === SYNC_KEY) { token = readToken(); syncInfo(); redraw(); return; }
    if (e.key !== KEY) return;
    refresh(); redraw();
  });
  var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { Object.keys(secs).forEach(function (id) { grow(secs[id].querySelector("textarea")); }); }, 150); });
  if (document.fonts) document.fonts.ready.then(function () { Object.keys(secs).forEach(function (id) { grow(secs[id].querySelector("textarea")); }); });
  if (window.visualViewport) {  // telefoon: het meescrollende veld boven het toetsenbord houden
    var vv = window.visualViewport, kb = function () { document.documentElement.style.setProperty("--kb", Math.max(0, window.innerHeight - vv.height - vv.offsetTop) + "px"); };
    vv.addEventListener("resize", kb); vv.addEventListener("scroll", kb);
  }

  // ---- notitieblad: los blad dat in beeld blijft. Het klad staat alleen hier (fm-notitieblad-<vak>);
  //      "Opslaan bij les" zet de tekst onder de notitie van de gekozen les, en vanaf daar gaat hij mee in sync en download.
  var NB_KEY = "fm-notitieblad-" + VAK, nbEl = $("notitieblad"), nbFab = $("nb-fab"), nbSel = $("nb-les"), nbTa = $("nb-text"), nbTimer, nbFollow = true;
  var nb = (function () { try { var v = JSON.parse(localStorage.getItem(NB_KEY) || "null"); if (v && typeof v === "object") return { t: str(v.t, 500000), les: ID.test(v.les || "") ? v.les : "", open: v.open === true }; } catch (e) {} return { t: "", les: "", open: false }; })();
  function nbWrite() { try { localStorage.setItem(NB_KEY, JSON.stringify(nb)); return true; } catch (e) { return false; } }
  function nbMsg(html, err) { var el = $("nb-msg"); el.innerHTML = html; el.classList.toggle("err", !!err); el.hidden = !html; }
  function inView() {  // de les waar je nu leest: de laatste les waarvan de bovenkant boven het midden van het scherm staat
    var best = pageIds[0] || "", line = window.innerHeight * 0.45;
    pageIds.forEach(function (id) { var art = secs[id].closest(".lesson"); if (art && art.getBoundingClientRect().top < line) best = id; });
    return best;
  }
  function nbFollowText() { $("nb-follow").textContent = nbFollow ? "Volgt de les die in beeld is. Kies zelf een les om hem vast te zetten." : "Vastgezet op deze les."; }
  function nbPick(id, manual) {
    if (pageIds.indexOf(id) === -1) return;
    nbSel.value = id; nb.les = id; nbWrite();
    if (manual !== undefined) { nbFollow = !manual; nbFollowText(); }
  }
  function nbOpen(open, focus) {
    nb.open = open; nbWrite();
    nbEl.hidden = !open; nbFab.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.classList.toggle("nb-open", open);
    if (open) {
      if (pinned) setPin(null);  // twee meescrollende velden tegelijk is te veel
      if (nbFollow || pageIds.indexOf(nb.les) === -1) nbPick(inView());
      if (focus) nbTa.focus({ preventScroll: true });
    } else if (focus) nbFab.focus();
  }
  function nbSave() {
    var id = nbSel.value, text = nbTa.value.replace(/\s+$/, "").replace(/^\s*\n/, "");
    if (!text.trim()) { nbMsg("Typ eerst iets op het notitieblad.", true); nbTa.focus(); return; }
    if (!secs[id]) { nbMsg("Kies eerst een les.", true); nbSel.focus(); return; }
    if (dirty[id]) save(id);  // wat je net onder de les typte, eerst bewaren
    refresh();
    var cur = live(id), ta = secs[id].querySelector("textarea");
    ta.value = cur ? cur.t.replace(/\s+$/, "") + "\n\n" + text : text;
    dirty[id] = true; save(id); fill(secs[id]); open(secs[id], false);
    nbTa.value = ""; nb.t = ""; nbWrite(); $("nb-status").textContent = "";
    nbFollow = true; nbFollowText();
    nbMsg('Vastgemaakt aan ' + esc(labelOf(id)) + '. <a href="#notitie-' + id + '" data-go="' + id + '">Bekijk bij de les</a>');
  }
  if (nbEl && pageIds.length) {
    var grp = null, gl = "";
    pageIds.forEach(function (id) {  // per week een groep, zodat de namen kort blijven
      var wk = secs[id].closest("section.week"), w = wk ? wk.getAttribute("data-label") || "" : "", o = document.createElement("option");
      if (!grp || w !== gl) { grp = document.createElement("optgroup"); grp.label = gl = w; nbSel.appendChild(grp); }
      var l = labelOf(id); o.value = id; o.textContent = w && l.indexOf(w + " · ") === 0 ? l.slice(w.length + 3) : l; grp.appendChild(o);
    });
    nbFab.insertAdjacentHTML("afterbegin", PEN);
    nbTa.value = nb.t;
    if (nb.les && pageIds.indexOf(nb.les) !== -1) { nbSel.value = nb.les; nbFollow = !nb.t.trim(); }
    nbFollowText();
    nbFab.hidden = false; document.body.classList.add("has-nb");
    nbFab.addEventListener("click", function () { nbOpen(true, true); });
    $("nb-close").addEventListener("click", function () { nbOpen(false, true); });
    nbSel.addEventListener("change", function () { nbPick(nbSel.value, true); nbMsg(""); });
    $("nb-here").addEventListener("click", function () { nbPick(inView(), false); nbMsg(""); });
    $("nb-save").addEventListener("click", nbSave);
    nbTa.addEventListener("input", function () {
      nb.t = nbTa.value; nbMsg("");
      if (nbFollow && nbTa.value.trim()) { nbFollow = false; nbFollowText(); }  // tijdens het typen springt de les niet meer weg
      $("nb-status").textContent = "Klad wordt bewaard…";
      clearTimeout(nbTimer); nbTimer = setTimeout(function () { $("nb-status").textContent = nbWrite() ? "Klad bewaard op dit apparaat" : "Klad niet bewaard: deze browser staat opslaan niet toe"; }, 400);
    });
    nbEl.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { e.preventDefault(); nbOpen(false, true); }
      else if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); nbSave(); }
    });
    $("nb-msg").addEventListener("click", function (e) {
      var a = e.target.closest("a[data-go]"); if (!a) return;
      e.preventDefault(); var sec = secs[a.getAttribute("data-go")]; open(sec, false);
      sec.classList.remove("hit"); void sec.offsetWidth; sec.classList.add("hit");
      sec.scrollIntoView({ block: "center" });
    });
    var nbTick = false;
    window.addEventListener("scroll", function () {
      if (!nb.open || !nbFollow || nbTick) return; nbTick = true;
      requestAnimationFrame(function () { nbTick = false; var id = inView(); if (id && id !== nbSel.value) nbPick(id); });
    }, { passive: true });
    window.addEventListener("pagehide", function () { clearTimeout(nbTimer); nb.t = nbTa.value; nbWrite(); });
    if (nb.open) nbOpen(true, false);
  }

  window.fmNotes = {  // voor de zoekbalk
    find: function (term, norm) {
      return liveIds().filter(function (id) { return norm(store.notes[id].t).indexOf(term) !== -1; }).map(function (id) {
        return { id: "notitie-" + id, label: labelOf(id), text: store.notes[id].t.replace(/\s+/g, " ").trim() };
      });
    }
  };
})();
</script>"""

def figlib_css():
    import sys
    d = os.path.join(ROOT, "scripts", "figuren")
    if d not in sys.path:
        sys.path.insert(0, d)
    import lib
    return lib.CSS

def build():
    import datetime
    built = datetime.date.today().strftime("%-d-%-m-%Y")
    note_ids = {}
    for slug, c in VAKKEN.items():
        note_ids[slug] = []
        src = os.path.join(SRC, slug)
        parts = [("overzicht", "Overzicht", "overzicht.md")] + [(f"week-{i}", f"Week {i}", f"week-{i}.md") for i in range(1, 8)]
        weeks, navs = [], []
        # aantallen voor de knoppen onder elke week: oefenvragen en weektoetsen van die week
        site_vak = os.path.join(ROOT, "site", slug)
        vr = json.load(open(os.path.join(site_vak, "vragen.json"), encoding="utf-8"))
        tw = set(json.load(open(os.path.join(site_vak, "toetsen.json"), encoding="utf-8"))["weken"])
        les_week = {l["id"]: l["week"] for l in vr["lessen"]}
        figuren = load_figuren(c["figuren"])
        import build_begrippen
        begr = build_begrippen.counts(slug)  # {week: aantal begrippen} voor de knop naar de flitskaarten
        n_fig = 0
        for key, label, fn in parts:
            md = open(os.path.join(src, fn), encoding="utf-8").read()
            md = clean_source(md, slug, c)
            after = ""
            if key != "overzicht":
                w = int(key.split("-")[1])
                n = sum(1 for q in vr["vragen"] if les_week.get(q["les"]) == w)
                btn = [f'<span class="wn-label">Week {w} gelezen? Test of je het kunt.</span>']
                if n:
                    btn.append(f'<a class="wn-btn primary" href="{c["oefen"]}#oefenen-w{w}">Oefenvragen week {w} <small>{n} vragen</small></a>')
                if w in tw:
                    btn.append(f'<a class="wn-btn" href="{c["oefen"]}#toetsen-w{w}">Weektoets week {w}</a>')
                if begr.get(w):
                    btn.append(f'<a class="wn-btn" href="../../begrippen/{slug}/#kaarten-w{w}">Begrippen week {w} <small>{begr[w]}</small></a>')
                if w < 7:
                    btn.append(f'<a class="wn-btn quiet" href="#week-{w + 1}">Door naar week {w + 1}</a>')
                after = f'<nav class="week-next" aria-label="Verder na week {w}">{"".join(btn)}</nav>'
            wk = 0 if key == "overzicht" else int(key.split("-")[1])
            figs = [f for f in figuren if f["week"] == wk]
            n_fig += len(figs)
            weeks.append(render_week(key, label, md, after, figs, note_ids[slug]))
            short = "Info" if key == "overzicht" else label.replace("Week ", "W")
            navs.append(f'<a href="#{key}" aria-current="false"><span class="l">{label}</span><span class="s">{short}</span></a>')
        a1, a2, a3, a4 = c["accent"]
        b1, b2 = c["band"]
        page = PAGE
        assert len(set(note_ids[slug])) == len(note_ids[slug]), f"{slug}: twee lessen met hetzelfde id, hun notities zouden door elkaar lopen"
        for k, v in dict(HEADING=html.escape(c["heading"]), LINE=html.escape(c["line"]), DOC=c["doc"], WEEKNAV="".join(navs),
                         VAK=slug, NOTE_ALIAS=html.escape(json.dumps(NOTITIE_ALIASSEN.get(slug, {}))), NOTES_CSS=NOTES_CSS, NOTES_JS=NOTES_JS,
                         SITEBAR=sitenav.bar("../../", slug, "sam"), TABS=sitenav.tabs("../../", slug, "sam"),
                         FIG_CSS=figlib_css(), C1=c["chart"][0][0], C2=c["chart"][0][1], C3=c["chart"][0][2], C4=c["chart"][0][3],
                         D1=c["chart"][1][0], D2=c["chart"][1][1], D3=c["chart"][1][2], D4=c["chart"][1][3],
                         TABS_CSS=sitenav.TABS_CSS, BAR_CSS=sitenav.bar_css(792), BAR_JS=sitenav.BAR_JS,
                         WEEKS="\n".join(weeks), BUILT=built, A1=a1, A2=a2, A3=a3, A4=a4, B1=b1, B2=b2, CODE=c["code"]).items():
            page = page.replace(f"__{k}__", v)
        assert "__" not in page.replace("__proto__", ""), slug
        os.makedirs(os.path.join(OUT, slug), exist_ok=True)
        open(os.path.join(OUT, slug, "index.html"), "w", encoding="utf-8").write(page)
        assert n_fig == len(figuren), f"{slug}: {len(figuren) - n_fig} figuur/figuren met een week buiten 0-7"
        print("samenvatting", slug, len(page) // 1024, "KB,", n_fig, "figuren,", len(note_ids[slug]), "notitievelden")
    check_note_ids(note_ids)

if __name__ == "__main__":
    build()
