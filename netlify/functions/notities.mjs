// Online opslag voor de eigen notities op de samenvattingen, zodat ze op al je apparaten hetzelfde zijn.
//
// - De notities staan in Netlify Blobs (store "notities", per vak één document), niet in de repo en niet op de site.
// - Toegang alleen met het wachtwoord uit de omgevingsvariabele NOTITIES_WACHTWOORD (in Netlify instellen, minstens 12 tekens).
//   De browser stuurt nooit het wachtwoord zelf mee, maar een sleutel die ervan is afgeleid (zie sleutel()).
// - Elke notitie heeft een versie (v). Een apparaat mag een notitie alleen overschrijven als het de laatste versie kende (b);
//   anders krijgt het de nieuwe versie terug en voegt het zelf samen, zodat er nooit tekst van een ander apparaat verdwijnt.
//
// GET /api/notities?vak=hrm               -> { notes: { <les-id>: { t, u, l, v } } }   (t "" = verwijderd)
// PUT /api/notities?vak=hrm  { notes: { <les-id>: { t, u, l, b } } }  -> { notes, accepted: [ids] }
import { getStore } from "@netlify/blobs";
import { createHash, randomUUID, timingSafeEqual } from "node:crypto";

const VAKKEN = new Set(["inkoop-recht", "hrm", "praktijkproject"]);
const ID = /^[a-z0-9-]{1,90}$/;
const MAX_BODY = 3_000_000, MAX_TEKST = 500_000;

export const config = {
  path: "/api/notities",
  // tegen wachtwoord raden: hooguit 90 verzoeken per minuut per IP-adres (normaal gebruik zit daar ver onder)
  rateLimit: { windowLimit: 90, windowSize: 60, aggregateBy: ["ip", "domain"] },
};

// Zelfde afleiding als in de browser: sha-256 van "fm-notities:" + wachtwoord, als hex.
const sleutel = (wachtwoord) => createHash("sha256").update("fm-notities:" + wachtwoord, "utf8").digest("hex");

const antwoord = (status, body) =>
  new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", "x-content-type-options": "nosniff" },
  });

const gelijk = (a, b) => {
  const x = createHash("sha256").update(String(a)).digest(), y = createHash("sha256").update(String(b)).digest();
  return timingSafeEqual(x, y);
};

const tekst = (v, max) => (typeof v === "string" && v.length <= max ? v : null);

async function lees(store, vak) {
  const cur = await store.getWithMetadata(vak, { type: "json" });
  const data = cur && cur.data && typeof cur.data === "object" && cur.data.notes && typeof cur.data.notes === "object" ? cur.data : { notes: {} };
  return { data, etag: cur ? cur.etag : null, bestond: !!cur };
}

export default async (req) => {
  const geheim = process.env.NOTITIES_WACHTWOORD || "";
  if (geheim.length < 12) return antwoord(503, { fout: "niet-ingesteld" });

  const auth = req.headers.get("authorization") || "";
  if (!gelijk(auth.startsWith("Bearer ") ? auth.slice(7) : "", sleutel(geheim))) return antwoord(401, { fout: "wachtwoord" });

  const vak = new URL(req.url).searchParams.get("vak");
  if (!VAKKEN.has(vak)) return antwoord(400, { fout: "vak" });

  const store = getStore({ name: "notities", consistency: "strong" });

  if (req.method === "GET") {
    const { data } = await lees(store, vak);
    return antwoord(200, { notes: data.notes });
  }
  if (req.method !== "PUT") return antwoord(405, { fout: "methode" });

  const raw = await req.text();
  if (raw.length > MAX_BODY) return antwoord(413, { fout: "te-groot" });
  let body;
  try { body = JSON.parse(raw); } catch { return antwoord(400, { fout: "json" }); }
  const binnen = body && typeof body.notes === "object" && !Array.isArray(body.notes) ? body.notes : null;
  if (!binnen) return antwoord(400, { fout: "notes" });
  const nieuw = [];
  for (const [id, n] of Object.entries(binnen)) {
    const t = n && tekst(n.t, MAX_TEKST), u = n && tekst(n.u, 40), l = n && tekst(n.l, 300), b = n && tekst(n.b ?? "", 80);
    if (!ID.test(id) || t === null || u === null || l === null || b === null) return antwoord(400, { fout: "notitie", id });
    nieuw.push({ id, t, u, l, b });
  }

  // Lezen, samenvoegen en alleen wegschrijven als niemand er intussen iets aan veranderde; anders opnieuw.
  for (let poging = 0; poging < 6; poging++) {
    if (poging) await new Promise((r) => setTimeout(r, 40 * poging + Math.random() * 80));  // even wachten bij gelijktijdige opslag
    const { data, etag, bestond } = await lees(store, vak);
    const accepted = [];
    for (const n of nieuw) {
      const huidig = Object.hasOwn(data.notes, n.id) ? data.notes[n.id] : null;
      if (((huidig && huidig.v) || "") !== n.b) continue;  // een ander apparaat was eerder: de browser voegt samen
      data.notes[n.id] = { t: n.t, u: n.u, l: n.l, v: new Date().toISOString() + "-" + randomUUID().slice(0, 8) };
      accepted.push(n.id);
    }
    if (!accepted.length) return antwoord(200, { notes: data.notes, accepted });
    const res = etag ? await store.setJSON(vak, data, { onlyIfMatch: etag })
      : !bestond ? await store.setJSON(vak, data, { onlyIfNew: true })
      : await store.setJSON(vak, data);  // geen ETag ontvangen (hoort niet te gebeuren): dan zonder voorwaarde
    if (res.modified) return antwoord(200, { notes: data.notes, accepted });
  }
  return antwoord(409, { fout: "druk" });
};
