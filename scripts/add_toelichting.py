"""Zet de uitleg ("Waarom dit klopt") bij de modelantwoorden van open vragen en casusvragen.

De teksten staan per vak in scripts/toelichting/<vak>.py als dict T: sleutel = vraag-id, of <casus-id>-s<n> voor
deelvraag n (vanaf 0) van een casus. Gebruik: add_toelichting.py <slug> <map met vragen.json en toetsen.json>.
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

def load(slug):
    f = os.path.join(HERE, "toelichting", slug.replace("-", "_") + ".py")
    if not os.path.exists(f):
        return {}
    spec = importlib.util.spec_from_file_location("tl_" + slug.replace("-", "_"), f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.T

def main(slug, d):
    T = load(slug)
    used, missing = set(), []
    vp = os.path.join(d, "vragen.json"); tp = os.path.join(d, "toetsen.json")
    v = json.load(open(vp, encoding="utf-8")); t = json.load(open(tp, encoding="utf-8"))
    qs = v["vragen"] if isinstance(v, dict) else v
    for q in qs:
        if q["type"] == "open":
            if q["id"] in T: q["toelichting"] = T[q["id"]]; used.add(q["id"])
            else: missing.append(q["id"])
    for q in t["items"]:
        if q["type"] == "open":
            if q["id"] in T: q["toelichting"] = T[q["id"]]; used.add(q["id"])
            else: missing.append(q["id"])
        elif q["type"] == "casus":
            for i, s in enumerate(q["subvragen"]):
                k = f'{q["id"]}-s{i}'
                if k in T: s["toelichting"] = T[k]; used.add(k)
                else: missing.append(k)
    json.dump(v, open(vp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(t, open(tp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    extra = sorted(set(T) - used)
    print(f"toelichting {slug}: {len(used)} gekoppeld, {len(missing)} zonder uitleg" + (f", onbekende sleutels: {extra[:5]}" if extra else ""))
    if "--missing" in sys.argv: print(" ".join(missing))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
