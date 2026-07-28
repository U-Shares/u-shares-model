# Changelog

Rolling cadence: every release entry states **which claims were added, changed status, or were retired**
— so critics can cite the exact version they engaged. Statuses are maintainer-stewarded (see
`GOVERNANCE.md`).

## 2026-07-28 — v1.0.2 (the household stress study)

**No claim added, changed status, or retired.** The complete pre-registered household stress study —
both phases run under locks countersigned before any data extraction, all three pre-registered
adverse possibilities explicitly adjudicated and published either way (locks ship with this release
for date verification):
- **Open questions 29 → 31:** OQ-HH-005 (the flow-side disregard gap — the month-43 SSI-limit breach
  under a principal-only disregard), OQ-HH-006 (dividend value conditional on emergency-credit terms —
  the 44/104 verdict-flip sensitivity finding).
- **Evidence annotations (status-neutral):** RT1 and F7 carry the Phase-1 verdicts INCLUDING the
  partially-materialized "too-small-to-matter" adverse possibility, per the study's bidirectional
  commitment.
- **Phase-2 additions:** OQ-HH-007 (hardship-valve calibration — the stickiness paradox's design
  question), OQ-MD-007 (above-floor composition and recovery participation); F7 dial-table supplement
  (the disregard variants in months, including the ~$4,800 income-side statutory breakpoint).
  Register: 33 open questions.
- **Ships with:** `model/household_stress.py` + `model/econ014_phase2.py` (engine + Phase-2 tests,
  mid-run fix log in header), `model/econ014_archetypes.json` (per-parameter kinds + sources), both
  results JSONs, `household_scenarios/` (six editable per-archetype scenario files) +
  `run_household.py` (one-command reproduction), and both pre-registration locks under
  `preregistration/` — shipped verbatim so readers can date-check that thresholds, metrics, and the
  adverse possibilities were locked before any data was extracted.

## 2026-07-26 — v1.0.1 (first cadence release)

**No claim added, changed status, or retired.** Rolling-cadence additions from a structured
engagement with *The Last Economy* (Intelligent Internet, 2025):
- **Open questions 26 → 29:** OQ-FIS-011 (asset-evaporation stress on reserve tail correlation),
  OQ-MD-006 (the pump-rate frontier; harnesses ship with this release), OQ-AP-006 (corporate-form
  persistence and the issuance counterparty).
- **Evidence annotations (status-neutral):** F6 — evaporation stress cells escalate the 1-in-200
  reserve 2.4×–4.3× over central, directional; GV1 — model and Alaska history independently agree the
  protection priority is flows first, wrapper second.
- **CP1 comparison extended** with the intelligence-endowment member (*The Last Economy*) — complement,
  not competitor.
- **New model harnesses (4) + scenario:** `model/t2_preferential_attachment.py` (does preferential
  attachment defeat the dispersion mechanism?), `model/t2b_pump_frontier.py` (what placement flow
  holds the periphery?), `model/t2c_wrapper_breach.py` (is a breached wrapper recoverable?),
  `model/t1_formalism_bridge.py` (r>g-as-topology vs the wealth-tail index — same dial?); scenario
  `model/scenarios/mostaque-world.yml`. Manifest rows in `CODE_MANIFEST.md` for all four.

## 2026-07-18 — Initial release

**Claims register established** (14 IDs): F1–F7 (funding, issuance, reserve, reach) · L1 (legal
classification) · M0 (magnitudes held) · DS1 (dispersion) · GV1 (governance/durability) · RT1
(retention) · CP1 (comparative positioning) · DR1 (distribution rail).

- Statuses at release: **supported** F4, F5 · **contested** F6, F7, DS1 (challenges presented in full in
  their evidence files) · **open** F1, F2, F3, L1, M0, GV1, RT1, CP1, DR1 · **retired** none.
- 26 open questions across five reviewer perspectives (`open-questions/`).
- One-command reproduction of F1 (`model/run_scenario.py`); falsify-by-scenario-file path live.
- Facts current as of 2026-07-18 (see the README's dated note).

*Pre-release provenance: the register and evidence base passed an internal adversarial review, an
external two-reviewer design pass, and a five-persona adversarial panel before publication; three claims
enter at `contested` as a result — displayed, not defended away.*
