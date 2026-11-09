(function () {
  const KEY = "__KEY__";
  const HINT = "__HINT__";
  const fmt = n => (Math.round(n * 2) / 2).toString().replace(".", ",");
  const $ = (s, el = document) => el.querySelector(s);
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  /* ---------- opslag ---------- */
  let state = { answers: {}, self: {}, mc: {}, mcChecked: {}, claude: {}, timer: { dur: 120, elapsed: 0, since: null } };
  try { const raw = localStorage.getItem(KEY); if (raw) state = Object.assign(state, JSON.parse(raw)); } catch (e) {}
  let saveT;
  function save() { clearTimeout(saveT); saveT = setTimeout(() => { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} }, 250); }

  const byTopic = id => QUESTIONS.filter(q => q.topic === id);
  const maxOf = qs => qs.reduce((s, q) => s + q.pts, 0);

  /* ---------- weergave ---------- */
  const topicsEl = $("#topics");
  for (const t of TOPICS) {
    const qs = byTopic(t.id);
    const c = CASES[t.id];
    const sec = document.createElement("section");
    sec.className = "topic"; sec.id = "t-" + t.id; sec.dataset.topic = t.id;
    sec.innerHTML = `
      <div class="topic-head"><h2>${esc(t.label)}</h2><span class="meta">${qs.length} vragen · ${maxOf(qs)} punten</span></div>
      <article class="casus" id="casus-${t.id}">
        <div class="instr">${t.id === "recht" ? "Toelichting" : "Gebruik onderstaande tekst voor het beantwoorden van de vragen"}</div>
        <h3>${esc(c.titel)}</h3>
        ${c.html}
      </article>`;
    for (const q of qs) sec.appendChild(q.type === "mc" ? mcCard(q) : openCard(q));
    topicsEl.appendChild(sec);
  }

  function openCard(q) {
    const el = document.createElement("article");
    el.className = "q"; el.id = "q-" + q.id;
    el.innerHTML = `
      <div class="q-head"><span class="qid">${q.id}</span><span class="tag">${esc(q.model_naam)}</span><span class="pts">${q.pts} ${q.pts === 1 ? "punt" : "punten"}</span></div>
      <p class="prompt">${esc(q.q)}</p>
      <textarea id="a-${q.id}" aria-label="Jouw antwoord op vraag ${q.id}" placeholder="Typ je antwoord. Noem het model, leg uit en onderbouw met de casus."></textarea>
      <div class="actions">
        <button class="btn" type="button" data-act="model" aria-expanded="false">Modelantwoord</button>
        <button class="btn primary claude-only" type="button" data-act="claude" hidden>Laat Claude nakijken</button>
        <span class="empty-msg" hidden>Schrijf eerst een antwoord.</span>
        <span class="saved" aria-live="polite"></span>
      </div>
      <section class="panel-model" hidden>
        <h4>Modelantwoord</h4>
        <div class="model-body">${q.model}</div>
        <h4>Beoordelingspunten · vink aan wat in jouw antwoord staat</h4>
        <ul class="rubric">${q.rubric.map((r, i) => `<li><label><input type="checkbox" id="r-${q.id}-${i}" data-i="${i}"><span>${esc(r[0])}</span><span class="rp">${r[1]} p</span></label></li>`).join("")}</ul>
        <div class="selfscore"></div>
      </section>
      <section class="panel-claude" hidden aria-live="polite"></section>`;
    const ta = $("textarea", el);
    ta.value = state.answers[q.id] || "";
    const savedEl = $(".saved", el);
    ta.addEventListener("input", () => {
      state.answers[q.id] = ta.value; save();
      savedEl.textContent = "Opgeslagen"; $(".empty-msg", el).hidden = true;
      markStale(q, el); updateScores();
    });
    const mBtn = $('[data-act="model"]', el), mPanel = $(".panel-model", el);
    mBtn.addEventListener("click", () => {
      mPanel.hidden = !mPanel.hidden; mBtn.setAttribute("aria-expanded", String(!mPanel.hidden));
      mBtn.textContent = mPanel.hidden ? "Modelantwoord" : "Verberg modelantwoord";
    });
    const checks = el.querySelectorAll(".rubric input");
    const saved = state.self[q.id] || [];
    checks.forEach((cb, i) => {
      cb.checked = !!saved[i];
      cb.addEventListener("change", () => {
        state.self[q.id] = Array.from(checks).map(c => c.checked); save(); renderSelf(q, el); updateScores();
      });
    });
    renderSelf(q, el);
    $('[data-act="claude"]', el).addEventListener("click", () => grade(q, el));
    if (state.claude[q.id]) renderClaude(q, el, state.claude[q.id]);
    return el;
  }

  function selfPts(q) { const s = state.self[q.id] || []; return q.rubric.reduce((sum, r, i) => sum + (s[i] ? r[1] : 0), 0); }
  function renderSelf(q, el) { $(".selfscore", el).textContent = `Jouw score: ${fmt(selfPts(q))} / ${q.pts}`; }

  function mcCard(q) {
    const el = document.createElement("article");
    el.className = "q"; el.id = "q-" + q.id;
    const L = ["A", "B", "C", "D"];
    el.innerHTML = `
      <div class="q-head"><span class="qid">${q.id}</span><span class="tag">Meerkeuze</span><span class="pts">${q.pts} punt</span></div>
      <p class="mc-casus">${esc(q.casus)}</p>
      <p class="prompt">${esc(q.q)}</p>
      <div class="opts" role="radiogroup" aria-label="Antwoordopties ${q.id}">
        ${q.options.map((o, i) => `<label class="opt" for="mc-${q.id}-${i}"><input type="radio" name="mc-${q.id}" id="mc-${q.id}-${i}" value="${i}"><span><span class="ol">${L[i]}</span>${esc(o)}</span></label>`).join("")}
      </div>
      <div class="actions">
        <button class="btn primary" type="button" data-act="check">Controleer</button>
        <button class="btn ghost" type="button" data-act="again" hidden>Opnieuw proberen</button>
        <span class="empty-msg" hidden>Kies eerst een antwoord.</span>
      </div>
      <div class="mc-result" hidden></div>`;
    const radios = el.querySelectorAll('input[type="radio"]');
    if (state.mc[q.id] != null) radios[state.mc[q.id]].checked = true;
    radios.forEach(r => r.addEventListener("change", () => {
      state.mc[q.id] = Number(r.value); state.mcChecked[q.id] = false; save(); renderMc(q, el); updateScores();
    }));
    $('[data-act="check"]', el).addEventListener("click", () => {
      if (state.mc[q.id] == null) { $(".empty-msg", el).hidden = false; return; }
      state.mcChecked[q.id] = true; save(); renderMc(q, el); updateScores();
    });
    $('[data-act="again"]', el).addEventListener("click", () => {
      delete state.mc[q.id]; state.mcChecked[q.id] = false; radios.forEach(r => (r.checked = false)); save(); renderMc(q, el); updateScores();
    });
    renderMc(q, el);
    return el;
  }

  function renderMc(q, el) {
    const checked = !!state.mcChecked[q.id], pick = state.mc[q.id];
    const L = ["A", "B", "C", "D"];
    el.querySelectorAll(".opt").forEach((o, i) => {
      o.classList.toggle("right", checked && i === q.correct);
      o.classList.toggle("wrong", checked && i === pick && i !== q.correct);
    });
    el.querySelectorAll('input[type="radio"]').forEach(r => (r.disabled = checked));
    $('[data-act="check"]', el).hidden = checked;
    $('[data-act="again"]', el).hidden = !checked;
    $(".empty-msg", el).hidden = true;
    const res = $(".mc-result", el);
    res.hidden = !checked;
    if (checked) {
      const ok = pick === q.correct;
      res.className = "mc-result " + (ok ? "ok" : "no");
      res.innerHTML = `<strong>${ok ? "Goed." : "Niet goed. Het juiste antwoord is " + L[q.correct] + "."}</strong>${esc(q.uitleg)}`;
    }
  }

  /* ---------- nakijken door Claude ---------- */
  let sample = null;
  const plain = html => {
    const t = document.createElement("textarea");
    t.innerHTML = html.replace(/<br\s*\/?>/gi, "\n").replace(/<li>/gi, "\n- ").replace(/<\/(p|li|ol|ul|h3|div|tr)>/gi, "\n").replace(/<\/t[dh]>/gi, " | ").replace(/<[^>]+>/g, "");
    return t.value.replace(/\n{3,}/g, "\n\n").trim();
  };

  function buildPrompt(q, answer) {
    const rub = q.rubric.map(r => `- ${r[0]} (${r[1]} punt${r[1] === 1 ? "" : "en"})`).join("\n");
    return `Je bent een strenge maar eerlijke examinator voor het vak Facilitaire Bedrijfskunde (hbo Facility Management, tweede jaar). Het tentamen bestaat uit open vragen bij casussen. Beoordeel het antwoord van een student op één vraag.

CASUS
${plain(CASES[q.topic].html)}

VRAAG ${q.id} (maximaal ${q.pts} punten)
${q.q}

MODELANTWOORD
${plain(q.model)}

BEOORDELINGSPUNTEN
${rub}

ANTWOORD VAN DE STUDENT
"""
${answer}
"""

Regels voor het beoordelen:
- Geef alleen punten voor wat de student echt opschrijft. Vul niets aan en lees niets welwillend in.
- Een ander, maar inhoudelijk juist voorbeeld uit de casus dan in het modelantwoord telt volledig mee.
- Vraagt de vraag om onderbouwing met de casus en ontbreekt die, geef dan voor dat onderdeel hoogstens de helft van de punten.
- Een verkeerd model of een verkeerde term levert voor dat onderdeel geen punten op.
- Gebruik hele of halve punten. Het totaal ligt tussen 0 en ${q.pts}.
- Schrijf in het Nederlands, zakelijk en kort. Spreek de student aan met "je".

Antwoord met alleen JSON in precies deze vorm:
{"punten": 2.5, "oordeel": "één zin met je eindoordeel", "goed": ["wat goed is"], "ontbreekt": ["wat ontbreekt of onjuist is"], "tip": "één concrete tip om dit antwoord te verbeteren"}`;
  }

  const running = {};
  async function grade(q, el) {
    const answer = (state.answers[q.id] || "").trim();
    if (!answer) { $(".empty-msg", el).hidden = false; return; }
    if (!sample) return;
    if (running[q.id]) { running[q.id].abort(); return; }
    const ctl = new AbortController(); running[q.id] = ctl;
    const btn = $('[data-act="claude"]', el), panel = $(".panel-claude", el);
    btn.textContent = "Stop";
    panel.hidden = false;
    panel.innerHTML = `<h4>Beoordeling door Claude</h4><div class="busy">Claude kijkt je antwoord na. Dit duurt meestal 10 tot 40 seconden.</div>`;
    try {
      const r = await sample.json(buildPrompt(q, answer), { modelTier: "default", signal: ctl.signal });
      let p = Number(r && r.punten);
      if (!isFinite(p)) throw { code: "invalid_json" };
      p = Math.max(0, Math.min(q.pts, Math.round(p * 2) / 2));
      const res = {
        punten: p,
        oordeel: String(r.oordeel || ""),
        goed: Array.isArray(r.goed) ? r.goed.map(String).slice(0, 6) : [],
        ontbreekt: Array.isArray(r.ontbreekt) ? r.ontbreekt.map(String).slice(0, 6) : [],
        tip: String(r.tip || ""),
        voor: answer
      };
      state.claude[q.id] = res; save();
      renderClaude(q, el, res); updateScores();
    } catch (e) {
      const code = e && e.code;
      if (code === "cancelled") {
        if (state.claude[q.id]) renderClaude(q, el, state.claude[q.id]); else panel.hidden = true;
      } else if (["not_granted", "sampling_disabled", "not_declared", "capability_disabled", "capability_removed"].includes(code)) {
        disableClaude("Nakijken door Claude is niet toegestaan of niet beschikbaar in deze weergave. Zelf nakijken met het modelantwoord werkt wel.");
        panel.hidden = true;
      } else if (code === "rate_limited") {
        panel.innerHTML = `<h4>Beoordeling door Claude</h4><div class="busy">Je hebt Claude net veel gevraagd. Probeer het over een paar minuten opnieuw.</div>`;
      } else if (code === "session_expired") {
        panel.innerHTML = `<h4>Beoordeling door Claude</h4><div class="busy">Je bent uitgelogd. Log opnieuw in bij Claude en probeer het nog eens.</div>`;
      } else {
        panel.innerHTML = `<h4>Beoordeling door Claude</h4><div class="busy">Het nakijken is niet gelukt. Klik nog eens op "Laat Claude nakijken".</div>`;
      }
    } finally {
      delete running[q.id];
      btn.textContent = "Laat Claude nakijken";
    }
  }

  function renderClaude(q, el, res) {
    const panel = $(".panel-claude", el);
    panel.hidden = false;
    panel.innerHTML = `
      <div class="verdict"><h4>Beoordeling door Claude</h4><strong>${fmt(res.punten)} / ${q.pts}</strong></div>
      <div></div>
      <div class="lbl good" hidden>Goed</div><ul class="l-good" hidden></ul>
      <div class="lbl bad" hidden>Ontbreekt of onjuist</div><ul class="l-bad" hidden></ul>
      <div class="tipline" hidden><span class="lbl">Tip: </span><span class="tip"></span></div>
      <div class="stale" hidden>Je hebt je antwoord aangepast na deze beoordeling. Laat het opnieuw nakijken voor een actuele score.</div>`;
    panel.children[1].textContent = res.oordeel;
    const fill = (sel, lblSel, arr) => {
      const ul = $(sel, panel); arr.forEach(t => { const li = document.createElement("li"); li.textContent = t; ul.appendChild(li); });
      ul.hidden = !arr.length; $(lblSel, panel).hidden = !arr.length;
    };
    fill(".l-good", ".lbl.good", res.goed);
    fill(".l-bad", ".lbl.bad", res.ontbreekt);
    if (res.tip) { $(".tip", panel).textContent = res.tip; $(".tipline", panel).hidden = false; }
    markStale(q, el);
  }
  function markStale(q, el) {
    const res = state.claude[q.id]; const s = $(".panel-claude .stale", el);
    if (res && s) s.hidden = (state.answers[q.id] || "").trim() === res.voor;
  }

  function disableClaude(msg) {
    sample = null;
    document.querySelectorAll(".claude-only").forEach(b => (b.hidden = true));
    if (msg) $("#claude-note").textContent = msg;
  }

  (async () => {
    try {
      const s = window.claude && window.claude.use ? await window.claude.use("sample") : null;
      if (!s) { disableClaude(); return; }
      sample = s;
      document.querySelectorAll(".claude-only").forEach(b => (b.hidden = false));
      $("#claude-note").textContent = "Zelf nakijken: vink bij het modelantwoord aan welke punten je hebt. Claude geeft een tweede oordeel; recht telt automatisch.";
    } catch (e) { disableClaude(); }
  })();

  /* ---------- scores en navigatie ---------- */
  function topicStats(id) {
    const qs = id === "alles" ? QUESTIONS : byTopic(id);
    let done = 0, self = 0, cl = 0, clMax = 0, clN = 0;
    for (const q of qs) {
      if (q.type === "mc") {
        if (state.mcChecked[q.id]) { done++; if (state.mc[q.id] === q.correct) self += q.pts; }
      } else {
        if ((state.answers[q.id] || "").trim()) done++;
        self += selfPts(q);
        const r = state.claude[q.id]; if (r) { cl += r.punten; clMax += q.pts; clN++; }
      }
    }
    return { n: qs.length, done, self, max: maxOf(qs), cl, clMax, clN };
  }

  const nav = $("#nav");
  const NAV = [{ id: "alles", label: "Alle onderwerpen" }].concat(TOPICS.map(t => ({ id: t.id, label: t.label })));
  nav.innerHTML = NAV.map(t => `<button type="button" data-t="${t.id}"><span class="nl">${esc(t.label)}</span><span class="nm"></span></button>`).join("");
  nav.addEventListener("click", e => {
    const b = e.target.closest("button[data-t]"); if (!b) return;
    const id = b.dataset.t;
    if (id === "alles") { history.replaceState(null, "", location.pathname + location.search); show("alles"); }
    else location.hash = id;
    window.scrollTo({ top: 0 });
  });

  function show(id) {
    const valid = NAV.some(t => t.id === id) ? id : "alles";
    document.querySelectorAll(".topic").forEach(s => (s.hidden = valid !== "alles" && s.dataset.topic !== valid));
    $("#intro").hidden = valid !== "alles";
    nav.querySelectorAll("button").forEach(b => b.setAttribute("aria-current", String(b.dataset.t === valid)));
  }
  window.addEventListener("hashchange", () => show(location.hash.slice(1)));
  show(location.hash.slice(1) || "alles");

  function updateScores() {
    nav.querySelectorAll("button").forEach(b => {
      const s = topicStats(b.dataset.t);
      $(".nm", b).textContent = `${s.done}/${s.n} · ${fmt(s.self)}/${s.max}p`;
    });
    const a = topicStats("alles");
    $("#score").innerHTML = `
      <div class="big" style="display:contents"><dt>Zelf nagekeken</dt><dd>${fmt(a.self)} / ${a.max}</dd></div>
      <dt>Beantwoord</dt><dd>${a.done} / ${a.n}</dd>
      <dt>Claude (${a.clN} ${a.clN === 1 ? "vraag" : "vragen"})</dt><dd>${a.clN ? fmt(a.cl) + " / " + a.clMax : "–"}</dd>`;
  }
  updateScores();

  /* ---------- timer ---------- */
  const clock = $("#clock"), tStart = $("#t-start"), tDur = $("#t-dur"), tHint = $("#t-hint");
  tDur.value = String(state.timer.dur || 120);
  let tick = null;
  const remaining = () => state.timer.dur * 60000 - (state.timer.elapsed + (state.timer.since ? Date.now() - state.timer.since : 0));
  function drawClock() {
    const r = remaining();
    const neg = r <= 0, s = Math.max(0, Math.ceil(r / 1000));
    clock.textContent = `${String(Math.floor(s / 60)).padStart(2, "0")}:${String(s % 60).padStart(2, "0")}`;
    clock.classList.toggle("over", neg);
    if (neg && state.timer.since) { pause(); tHint.textContent = "De tijd is om. Rond je laatste antwoord af en kijk je werk na."; }
  }
  function run() { state.timer.since = Date.now(); save(); tStart.textContent = "Pauze"; tDur.disabled = true; tick = setInterval(drawClock, 500); }
  function pause() { if (state.timer.since) { state.timer.elapsed += Date.now() - state.timer.since; state.timer.since = null; save(); } clearInterval(tick); tStart.textContent = remaining() > 0 && state.timer.elapsed > 0 ? "Verder" : "Start"; tDur.disabled = state.timer.elapsed > 0; }
  tStart.addEventListener("click", () => { if (state.timer.since) pause(); else if (remaining() > 0) run(); });
  $("#t-reset").addEventListener("click", () => { clearInterval(tick); state.timer = { dur: Number(tDur.value), elapsed: 0, since: null }; save(); tStart.textContent = "Start"; tDur.disabled = false; tHint.textContent = HINT; drawClock(); });
  tDur.addEventListener("change", () => { state.timer.dur = Number(tDur.value); save(); drawClock(); });
  if (state.timer.since) run(); else { tStart.textContent = state.timer.elapsed > 0 && remaining() > 0 ? "Verder" : "Start"; tDur.disabled = state.timer.elapsed > 0; }
  drawClock();

  /* ---------- alles wissen ---------- */
  const confirmBox = $("#confirm");
  $("#reset-all").addEventListener("click", () => { confirmBox.hidden = false; $("#confirm-no").focus(); });
  $("#confirm-no").addEventListener("click", () => (confirmBox.hidden = true));
  $("#confirm-yes").addEventListener("click", () => {
    Object.values(running).forEach(c => c.abort());
    try { localStorage.removeItem(KEY); } catch (e) {}
    state = { answers: {}, self: {}, mc: {}, mcChecked: {}, claude: {}, timer: { dur: Number(tDur.value), elapsed: 0, since: null } };
    clearInterval(tick); tStart.textContent = "Start"; tDur.disabled = false;
    document.querySelectorAll(".q").forEach(el => {
      const ta = $("textarea", el); if (ta) ta.value = "";
      el.querySelectorAll("input").forEach(i => { i.checked = false; i.disabled = false; });
      const pc = $(".panel-claude", el); if (pc) { pc.hidden = true; pc.innerHTML = ""; }
      const pm = $(".panel-model", el); if (pm) { pm.hidden = true; const b = $('[data-act="model"]', el); b.textContent = "Modelantwoord"; b.setAttribute("aria-expanded", "false"); }
      const sv = $(".saved", el); if (sv) sv.textContent = "";
      const q = QUESTIONS.find(x => "q-" + x.id === el.id);
      if (q && q.type === "mc") renderMc(q, el); else if (q) renderSelf(q, el);
    });
    confirmBox.hidden = true; updateScores(); drawClock(); window.scrollTo({ top: 0 });
  });
})();
