"""Bouwt toetsen.json per vak uit de week-vraagbanken in scripts/toetsen/.

Elke week heeft een vraagbank met 3 x de samenstelling (bijv. 24 meerkeuzevragen, 6 open vragen
en 3 casussen). Dit script verdeelt die over drie vaste, niet-overlappende versies (A, B, C),
gelijk verdeeld over de onderdelen.
Optionele bestanden <vak>_eind.py, <vak>_eind2.py, ... bevatten eindtoetsen over alle weken met eigen vragen
(week 0, versie E, E2, ...; titel en uitleg via EIND_TITEL en EIND_UITLEG). Die vragen komen niet in de
weektoetsen, de mix of het proeftentamen.
Gebruik: python3 scripts/build_toetsen.py <ir|hrm|pp> <uitvoerbestand>
"""
import json, os, sys, glob, collections

HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "toetsen")
VERSIES = ["A", "B", "C"]

CONFIG = {
    "ir": dict(vak="Inkoop en recht voor de FM professional", prefix="ir_w",
               samenstelling=dict(mc=8, open=2, casus=1),
               proef=dict(titel="Proeftentamen over alle weken", mc=16, open=4, casus=2,
                          uitleg="Zoals het echte tentamen: inkoop en recht door elkaar, met meerkeuze, open vragen en casussen over week 1 tot en met 6.")),
    "hrm": dict(vak="HRM voor de FM-professional", prefix="hrm_w",
                samenstelling=dict(mc=8, open=2, casus=1),
                proef=dict(titel="Proeftentamen: zoals het mondeling", open_per_onderdeel={"HRM-theorie": 4, "Arbeidsrecht": 4}, casus_onderdeel="Gespreksvoering", casus=1,
                           uitleg="Net als het mondeling: vier HRM-vragen, vier arbeidsrechtvragen en een gesprekscasus. Zeg je antwoorden eerst hardop en schrijf ze daarna kort op.")),
    "pp": dict(vak="Praktijkproject Business Management", prefix="pp_w",
               samenstelling=dict(mc=6, open=2, casus=1),
               proef=dict(titel="Mix over alle weken", mc=12, open=4, casus=2,
                          uitleg="Elke keer een nieuwe trekking uit de vraagbanken van week 1 tot en met 7: modellen herkennen, uitleggen en toepassen op een FM-casus.")),
}
EIND = {
    "ir": dict(titel="Eindtoets over alle stof",
               uitleg="Een vaste toets met eigen vragen die niet in de weektoetsen zitten. Inkoop en recht door elkaar, met casussen die meerdere weken combineren, zoals op het tentamen."),
    "pp": dict(titel="Eindtoets over het hele verbetertraject",
               uitleg="Een vaste toets met eigen vragen die niet in de weektoetsen zitten. Je volgt één organisatie van verbeterrichting tot overdracht en past de modellen van alle weken toe."),
}

def load(prefix, eind_files=()):
    """Laadt de weekbanken en daarna de eindtoetsen; geeft (items, eindtoetsen) terug."""
    ns = {}
    exec(open(os.path.join(HERE, "lib.py"), encoding="utf-8").read(), ns)
    for f in sorted(glob.glob(os.path.join(HERE, prefix + "*.py"))):
        exec(open(f, encoding="utf-8").read(), ns)
    eind = []
    for nr, f in enumerate(eind_files, start=1):
        start = len(ns["T"])
        ns.pop("EIND_TITEL", None); ns.pop("EIND_UITLEG", None)
        exec(open(f, encoding="utf-8").read(), ns)
        versie = "E" if nr == 1 else f"E{nr}"
        for t in ns["T"][start:]:
            assert t["week"] == 0, f"{t['id']}: eindtoetsvraag moet week 0 hebben"
            t["versie"] = versie
        eind.append(dict(key="eind" if nr == 1 else f"eind{nr}", versie=versie,
                         titel=ns.get("EIND_TITEL"), uitleg=ns.get("EIND_UITLEG")))
    return ns["T"], eind

def check(items):
    errs = []
    ids = [t["id"] for t in items]
    dup = [i for i, n in collections.Counter(ids).items() if n > 1]
    if dup: errs.append(f"dubbele ids: {dup}")
    for t in items:
        if t["type"] == "mc":
            if not (0 <= t["juist"] < len(t["opties"])): errs.append(f"{t['id']}: juist buiten bereik")
            if len(t["opties"]) != 4: errs.append(f"{t['id']}: {len(t['opties'])} opties")
        elif t["type"] == "open":
            if not t["punten"]: errs.append(f"{t['id']}: geen punten")
        elif t["type"] == "casus":
            if not t["subvragen"]: errs.append(f"{t['id']}: geen subvragen")
            for s in t["subvragen"]:
                if not s["punten"]: errs.append(f"{t['id']}: subvraag zonder punten")
    return errs

def assign_versions(items):
    by_week = collections.defaultdict(list)
    for t in items:
        if t["week"] > 0:
            by_week[t["week"]].append(t)
    report = {}
    for w, ts in sorted(by_week.items()):
        for typ in ("mc", "open"):
            per_ond = collections.defaultdict(list)
            for t in ts:
                if t["type"] == typ: per_ond[t["onderdeel"]].append(t)
            k = 0
            for ond in sorted(per_ond):
                for t in per_ond[ond]:
                    t["versie"] = VERSIES[k % 3]; k += 1
        cas = [t for t in ts if t["type"] == "casus"]
        for i, t in enumerate(cas): t["versie"] = VERSIES[i % 3]
        cnt = collections.Counter((t["versie"], t["type"]) for t in ts)
        report[w] = {v: (cnt[(v, "mc")], cnt[(v, "open")], cnt[(v, "casus")]) for v in VERSIES}
    return report

def main():
    key, out = sys.argv[1], sys.argv[2]
    c = CONFIG[key]
    eind_files = sorted(glob.glob(os.path.join(HERE, f"{key}_eind*.py")))
    items, eindtoetsen = load(c["prefix"], eind_files)
    errs = check(items)
    if errs:
        print("\n".join(errs)); sys.exit(1)
    report = assign_versions(items)
    weken = sorted({t["week"] for t in items if t["week"] > 0})
    data = dict(vak=c["vak"], samenstelling=c["samenstelling"], proef=c["proef"], weken=weken, items=items)
    data["eindtoetsen"] = []
    for i, e in enumerate(eindtoetsen):
        tc = collections.Counter(t["type"] for t in items if t.get("versie") == e["versie"])
        meta = dict(EIND[key]) if i == 0 and key in EIND else {}
        if e["titel"]: meta["titel"] = e["titel"]
        if e["uitleg"]: meta["uitleg"] = e["uitleg"]
        assert meta.get("titel") and meta.get("uitleg"), f"{key} eindtoets {i + 1}: titel of uitleg ontbreekt"
        data["eindtoetsen"].append(dict(meta, key=e["key"], versie=e["versie"], mc=tc["mc"], open=tc["open"], casus=tc["casus"]))
    json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    tc = collections.Counter(t["type"] for t in items)
    print(f"{key}: {len(items)} items {dict(tc)}")
    for w, r in report.items(): print(f"  week {w}: " + "  ".join(f"{v}={r[v]}" for v in VERSIES))
    for e in data["eindtoetsen"]: print(f"  {e['key']}: {e['mc']} mc, {e['open']} open, {e['casus']} casus · {e['titel']}")

if __name__ == "__main__":
    main()
