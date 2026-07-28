# ECON-014 Pre-Registration Lock v1 — Household Resilience Stress Test (HRST)

**Study:** ECON-014 (scoping memo v1.1, `06_Agent_Playbook/2026-07-26_ECON_Scoping_ECON-014_...md`)
**ECON signed:** 2026-07-26 · **CSDA countersign:** ______________ (required BEFORE any
calibration-data extraction, per CSDA Ruling 3)
**Standard:** UBC SuperIntelligence Spec v1.2; DEC-039; CSDA Rulings 1–3 (scoping memo §11).
**Status at signing:** NO calibration data has been extracted; NO simulator code has been written.
Everything below is locked before the first data lookup. This file stays internal during the study and
**ships with the v1 results in their cadence release** so readers can verify date precedence.

---

## §1 Pre-registered outcome metrics (exhaustive — no unregistered measures may be reported)

Per archetype × scenario cell, dividend-ON vs dividend-OFF (and per-arm in Phase 2):

| ID | Metric | Definition |
|---|---|---|
| M1 | Months-of-runway | months until first crossing of each threshold in §2, by threshold ID |
| M2 | Threshold ordering | the sequence of threshold IDs crossed, in order |
| M3 | Crossing incidence | share of grid cells in which each threshold is crossed within the horizon (deterministic incidence — the word "probability" is banned per [R1]) |
| M4 | Avoided-vs-delayed | per threshold: crossed in OFF but not ON within horizon = AVOIDED; crossed in both but later in ON = DELAYED (Δ months); same month = NO EFFECT |
| M5 | Recovery time *(Phase 2)* | months from shock end until liquid savings ≥ pre-shock level AND no threshold state active |
| M6 | Terminal net worth *(Phase 2)* | liquid + account value − debt at horizon end |
| M7 | Four-tier classification | every reported result carries exactly one tier label per §5 |

**Publication rules (CSDA Rulings 1–2, binding):** archetype-specific time-to-threshold results in
*months* and orderings MAY publish, labeled "calibrated archetype, model output under stated
assumptions" — never "a typical family." Dollar-runway magnitudes, population weighting, national
aggregation, and any fiscal/public-cost figure are HELD (M0). Arithmetic-tier results publish
**labeled, never suppressed** ("arithmetic effect only — not resilience evidence under the four-tier
standard"). Every published figure must be reproducible from the shipped archetype + scenario files.

## §2 Threshold register [R2] — definition, class, source status, sensitivity (locked)

| ID | Event definition (exact) | Class | Source status | Default | Sensitivity range |
|---|---|---|---|---|---|
| TH-1 | Liquid savings < k × monthly essential expenses | behavioral (fragility indicator) | behaviorally assumed (SHED-motivated) | k=1 | k ∈ {0.5, 1, 2} |
| TH-2 | Missed housing payment: cash after higher-priority essentials < housing due | hard contractual | event legally fixed; the priority ordering (food/utilities > housing > debt service) is behaviorally assumed | priority order as stated | alternate order: housing-first |
| TH-3 | High-cost borrowing entry: first month a deficit is financed by revolving/short-term debt (liquid exhausted, deficit > 0) | behavioral / market-entry | behaviorally assumed; APR empirically anchored (payday/revolving literatures) | APR 36%/yr | APR ∈ {24%, 36%, 100%, 400%} |
| TH-4 | Utility/insurance lapse: essential non-housing bill unpaid ≥ 2 consecutive months after borrowing capacity exhausted | hard contractual | event legally fixed; the 2-month grace is assumed | 2 months | 1–3 months |
| TH-5 | Eviction/foreclosure initiation: N consecutive missed housing payments | hard contractual | legally grounded but jurisdiction-dependent; N is a simplification | N=3 | N ∈ {2, 3, 4} |
| TH-6 | Benefits cliff: countable resources > SSI limit ($2,000 individual — statute) | programmatic | legally fixed (42 U.S.C. §1382; the disregard toggle is the T-H dial, Phase 2) | $2,000 | none (statute) — toggle ON/OFF is the test |
| TH-7 | Debt overload: debt balance > B × monthly gross income | behavioral | behaviorally assumed | B=6 | B ∈ {4, 6, 12} |
| TH-8 | Asset raid / forced sale: first month an accessible asset is liquidated to cover a deficit (wrapper arms record the counterfactual "would-have-raided" month) | behavioral / market-entry | behaviorally assumed (Phase 2, T-D) | — | leakage rates from RT1 literature, not assumed |

No thresholds may be added, removed, or redefined after countersignature without a dated lock
amendment (v2) that itself ships with the results.

## §3 Shock grids (locked)

- **T-A (labor income):** income × {−25%, −50%, −75%, −100%}, onset month 1, shock durations
  {6, 12, 24} months + sustained-through-horizon; horizon 60 months.
- **T-B (wage loss + inflation):** income −25% sustained; essential-cost inflation {3%, 5%, 10%}/yr,
  run twice — general (all essentials) and housing-concentrated (rent-dominance hypothesis); dividend
  arms {indexed (design), frozen (nominal), OFF}.
- **T-C (crash with preserved floor):** account value {−20%, −40%, −60%, −80%} at month 1; dividend
  arms {preserved at original-issue-price floor (design), proportional-to-value (unprotected
  comparator), OFF}; labor income held at baseline (isolates capital-value vs income-flow channel).
- **T-G (cliff map — flagship):** placement size {$0, $1,000, $2,800, $5,000, $10,000, $20,000}
  ($2,800 = the Ch 3 A1 calibrated placement; the grid brackets it 0–7×) × the T-A severity grid;
  output = per threshold: AVOIDED / DELAYED(Δ) / NO EFFECT by placement size — the map of where the
  dividend moves a *threshold*, not just runway.

## §4 T-D arms, horizons, and funding identities [R3][R6] (Phase 2 — locked now)

**Arms:** (1) spendable cash · (2) liquid unprotected stock · (3) protected U-Shares, NO emergency
access · (4) protected U-Shares WITH the proposed hardship-access rules.
**Horizons:** 3 months · 12 months · 5 / 10 / 20 years.
**Funding identity — primary: equal public cost at inception.** The public cost of a U-Share placement
is the placement-credit outlay (35% federal share of placement value); arm 1's cash gift and arm 2's
stock purchase equal that public outlay; arms 3–4's issuer contribution is reported separately, never
netted away. **Secondary comparison: equal recipient value at inception** (arm 1 cash = full placement
value). Both identities publish with every T-D result; no third identity may be introduced post hoc.

## §5 Four-tier result hierarchy + adverse possibilities (locked verbatim from scoping §5)

**Tiers:** arithmetic effect (runway extended) → threshold effect (failure event avoided or materially
delayed) → recovery effect (ownership retained into the rebound) → long-run wealth effect (terminal
net worth higher). **Only threshold-tier and above counts as evidence of household resilience.**

**Pre-registered adverse possibilities (publish either way):**
1. **Stickiness paradox** — the locked account may be worth less than equal cash in acute liquidity
   crises (T-D cash arm may win at short horizons).
2. **Too-small-to-matter** — realistic placement sizes may move no cascade threshold (T-G speaks to
   this in Phase 1; final adjudication in the Phase-2 memo).
3. **Diversification–income tradeoff** [R8] — logged as an open adverse interaction (not a v1 test);
   resolved by citation to F6/account design or recorded as an OQ candidate.

## §6 Archetype parameter extraction rules (estimators named BEFORE extraction)

Already-verified corpus anchors (pre-existing, not new extraction): 2025 HHS poverty guidelines
($15,650 / $32,150 family-of-four / $64,300 at 200%); A1 income $31,000 and placement $2,800 @ 5% =
$140/yr (Ch 3 §7, sourcing note 2026-07-26); SSI resource limit $2,000 (statute).

| Parameter (per archetype) | Source | Named statistic (extracted post-countersign) |
|---|---|---|
| Liquid savings at t0 | SCF (latest public wave) | median liquid assets ("transaction accounts"), by income quintile matching the archetype |
| Essential consumption | BLS CE Survey | average annual expenditures, lowest-quintile (or matching band), split housing / non-housing essentials / other |
| Housing cost | CE Survey (primary), ACS (check) | renter housing expenditure for the matching income band |
| Debt balances + APR | SCF; payday/revolving literatures | median revolving balance (conditional on holding), by quintile; APRs per §2 TH-3 |
| Fragility anchor | Fed SHED (latest) | share unable to cover a $400 emergency expense with cash-equivalents (used to sanity-check savings calibration, not as a model input) |
| Labor income profiles | CPS/ASEC; DOL UI statistics | A2 seasonal profile (part-time volatile); A4 UI replacement rate ≈ statutory/reported average for ~6 months, then 0 |
| Program parameters | SSA (SSI FBR, current year); USDA (SNAP max allotment, current FY) | statutory values; A3 household = SSI FBR + one part-time earner |
| A5 (young family) | SCF age-<35 median income/balance sheet; CE childcare expenditure | as named |
| A6 (working caregiver) | SHED / CE / published care-cost literature ONLY | public-data calibration; **no biographical echoes — the standing never-family-in-public rule applies with special force (CSDA addition 1)** |

**Substitution rule:** if a named statistic proves unavailable in the public source, the substitution
is documented in the results memo with its own source status — no silent swaps. Every archetype-file
parameter carries kind-metadata: observed / derived / policy / scenario assumption / behavioral.

## §7 Explicitly out of scope (locked exclusions)

No population weights, no national aggregates, no fiscal-cost outputs (M0). No stochastic machinery in
v1. No issuer-side modeling — issuer states arrive as exogenous F6 paths (scoping §1 [R5]). T-E is an
analytical memo and must cite the GV1 flows-first annotation live at repo v1.0.1 (CSDA addition 2).
Public-cost outcomes remain hypotheses per scoping §6.

## §8 Reproducibility + acceptance

Deterministic, single-process, CPU-trivial; house compute conventions apply. All results regenerable
from the shipped archetype + scenario files (`household.yml` idiom). Outputs: JSON results +
Phase-memo tables. CSDA phase-gate acceptance (from §11): CSDA re-derives ≥1 archetype's runway
arithmetic by hand from the archetype file alone; verifies no unregistered outcome measures; verifies
every cliff-map threshold carries its §2 classification + source status.

---

*— ECON lane, signed 2026-07-26, prior to any data extraction or code. Awaiting CSDA countersignature;
on countersign, extraction + build + Phase 1 (T-A, T-B, T-C, T-G) proceed as one focused increment.*

---

## CSDA COUNTERSIGNATURE — 2026-07-26

**Reviewed against the §12 countersign checklist (scoping memo). Verdict: COUNTERSIGNED — extraction,
build, and Phase 1 may proceed as of this signature.**

Checklist: (1) threshold register [R2] COMPLETE — 8 thresholds, each with exact definition, class,
source status, default, sensitivity range, plus the v2-amendment discipline; (2) T-D arms + horizons
[R3] COMPLETE; (3) funding identities [R6] COMPLETE — primary/secondary defined, the 35% placement-
credit share stated, issuer contribution never netted, no post-hoc identities; (4) outcome metrics
CLOSED (M1–M7; "probability" banned per [R1]); (5) four-tier hierarchy + three adverse possibilities
locked verbatim; (6) **PARTIAL — carried as the one condition below**; (7) per-archetype sources +
named statistics BEFORE extraction, substitution rule, kind-metadata, A6 public-data-only COMPLETE;
(8) publication rules (Rulings 1–2 with all four conditions) restated in-lock COMPLETE. Extras noted
with approval: §7 locked exclusions; the §3 T-G placement grid bracketing the calibrated A1 placement
0–7×; the status-at-signing attestation (no data, no code).

**Condition of countersignature (one):** before ANY Phase-2 data extraction or T-H implementation, a
dated lock addendum (v1.1) must enumerate the [R4] program-parameterization set in the same per-item
discipline as §2 — SSI resource treatment · Medicaid eligibility pathway · SNAP asset rules · housing-
program treatment · state supplementation/waiver effects — each with source status, and the
asset-treatment vs dividend-income-treatment separation stated as two distinct registered dials. CSDA
countersigns that addendum before Phase 2 runs. Phase 1 is unaffected.

**File location note:** this lock lives at `03_AiS_Engine/04_Data Sources/UShares_Analysis/`
(ECON's working lane) rather than the Playbook folder — accepted; the Playbook thread carries the
pointer. It ships with the v1 results in their cadence release, unmodified except by dated amendment.

*— CSDA (Fable), countersigned 2026-07-26. ECON-014 Phase 1: EXTRACTION AND BUILD ARE GO.*
