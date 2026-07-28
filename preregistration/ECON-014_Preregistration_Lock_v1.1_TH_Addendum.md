# ECON-014 Pre-Registration Lock v1.1 — Phase 2 Addendum (T-H program parameterization + T-D/T-F estimators)

**Amends:** `ECON-014_Preregistration_Lock_v1.md` (countersigned 2026-07-26; Phase-1 acceptance PASS
on record). This addendum adds NO thresholds and redefines none — it parameterizes Phase-2 tests per
the scoping memo's [R4] and names the remaining Phase-2 estimators before extraction.
**ECON signed:** 2026-07-26 · **CSDA countersign:** ______________ (required BEFORE any Phase-2
calibration-data extraction, per the Phase-1 countersign's one binding condition)
**Ships with** the Phase-2 results in their cadence release, alongside lock v1.

---

## §1 T-H — two registered dials, separated (the month-43 finding's instrument)

Phase 1's flow-side finding (A3 saving the dividend breaches the $2,000 SSI resource limit at month
43 despite a principal-only disregard) makes the stock/flow separation the study's sharpest tool.
T-H therefore runs TWO independent dials, never conflated:

**Dial S (stock — asset/resource treatment):**
- S0 = no disregard (account principal counts toward resource tests)
- S1 = principal-only disregard (the naive drafting; Phase 1's implicit setting)
- S2 = full disregard, ABLE-style (principal + dividend-derived savings excluded; §529A/§530A
  precedent pattern)

**Dial F (flow — income treatment of the monthly dividend):**
- F0 = counted as unearned income (SSI rule: $20 general exclusion, then $1-for-$1 benefit
  reduction — statute)
- F1 = excluded by statutory disregard (the design position)

**Pre-registered T-H grid:** archetypes {A1 (SNAP household), A2 (SNAP + housing-voucher variant),
A3 (SSI + Medicaid pathway)} × S{0,1,2} × F{0,1} × placement {$2,800, $10,000} × behavior
{save, consume} × scenario {baseline no-shock, −50% sustained}. Outcomes (registered metrics only):
months-to-TH-6 or no-breach; first benefit-reduction month and first eligibility-loss month (as
month indices — benefit dollar deltas are computed internally but HELD per M0); M4 comparisons
across dial settings. **The publishable object is the dial-comparison structure** — what each
disregard variant is worth in months-to-breach and eligibility retention, per archetype.

## §2 Program parameter register (per [R4] — each with source status; extraction post-countersign)

| Program | Parameter set | Source status |
|---|---|---|
| SSI | resource limit $2,000/$3,000; income rules ($20 general exclusion; $65+half earned; $1:$1 unearned) | legally fixed (42 U.S.C. §1382; POMS) |
| Medicaid | pathway modeled = SSI-linked categorical (A3's pathway); MAGI-expansion (no asset test) noted as the no-cliff comparator | legally fixed structure; jurisdiction-dependent — modeled pathway stated, not universalized |
| SNAP | BBCE variant (no asset test — majority of states) vs federal-default asset test (FY-indexed limits); income: gross/net tests with earned-income deduction | legally fixed per variant; WHICH variant applies is jurisdictional — both run, labeled |
| Housing assistance | HOTMA regime: $100,000 asset cap + asset-income counting (24 CFR part 5 as amended) | legally fixed, recent (post-2024 phase-in) — exact figures re-verified at extraction |
| State supplementation | modeled as pass-through of SSI rules | simplification, documented (per scoping [R4]: v1 consolidated treatment is stylized, not a claim that programs share one rule) |

The v1 lock's substitution rule applies: any parameter unavailable at the named source is documented
with its own source status — no silent swaps.

## §3 T-D behavioral leakage estimators (named before extraction; arms/horizons/identities already locked in v1 §4)

- **Arm 1 (cash):** spend-down profile anchored to the unconditional-cash-transfer literature
  (windfall/transfer marginal propensity to consume for low-liquidity households; named statistic:
  MPC range for bottom-quintile-liquidity recipients).
- **Arm 2 (liquid unprotected stock):** liquidation-under-hardship anchored to the 401(k)/retirement
  leakage literature (named statistics: cashout-at-job-separation share; annual hardship-withdrawal
  incidence) — RT1's anchor, per the scoping requirement that leakage comes from literature, never
  assumption.
- **Arm 3 (wrapper, no access):** leakage = 0 by construction; the counterfactual "would-have-raided"
  months recorded (TH-8).
- **Arm 4 (wrapper + hardship access):** usage anchored to 401(k) hardship-withdrawal incidence and
  ABLE-account withdrawal patterns (named statistics: annual hardship incidence conditional on
  financial distress; ABLE withdrawal frequency).
- Sensitivity: each arm's leakage parameter runs at {literature-low, central, literature-high} — the
  stickiness-paradox adjudication (adverse possibility #1) must hold, or fail, across the range.

## §4 T-F path pre-registration (on the T2 harness)

Three actors at equal inception value: benefit recipient (flow, no principal) · permanent transfer
(one-time cash) · U-Share owner (locked principal + floor dividend). Path: recession (asset values
−40%, dividend floor preserved per T-C's structural result, labor displacement shock) for 2 model
years, then recovery/boom for 8. Outcomes: sign/ordering of recovery-participation (bottom-share
trajectory, M5/M6 class) — magnitudes held; the Post 14 recovery thesis is the hypothesis under
test, and its FAILURE is a publishable result on the same terms.

## §5 Unchanged

Thresholds (v1 §2), grids (v1 §3), metrics (v1 §1), publication rules (Rulings 1–2), adverse
possibilities (v1 §5), the four-tier hierarchy, and the Ch 3 production-timing checkpoint (Studio
states Ch 3 status when the Phase-2 memo lands; sidebar-only if settled).

*— ECON lane, 2026-07-26. Awaiting CSDA countersignature; on countersign + Mike's already-given go,
Phase 2 (T-D, T-F, T-H, T-E memo) runs as the second and final increment. No standing pipeline.*

---

## CSDA COUNTERSIGNATURE — 2026-07-26

**Reviewed against the Phase-1 countersign's binding condition. Verdict: COUNTERSIGNED — Phase-2
extraction and runs (T-D, T-F, T-H, T-E memo) may proceed as of this signature, under Mike's
already-recorded go.**

The condition is satisfied in full: Dial S / Dial F as two independent registered dials, never
conflated — with S1 (principal-only, the drafting Phase 1 proved self-defeating) correctly preserved
as its own tested variant rather than silently replaced; the [R4] program register carries per-item
source status with the right jurisdictional honesty (Medicaid pathway stated-not-universalized; both
SNAP variants run and labeled; HOTMA figures re-verified at extraction; state supplementation a
documented simplification). Noted with approval beyond the condition: T-D leakage parameters named
from the literature before extraction and swept literature-low/central/high — the stickiness-paradox
adjudication must survive the range, not a chosen point; T-F pre-registered with the explicit
commitment that the Post 14 recovery thesis FAILING publishes on the same terms as succeeding; T-H
outcomes as month indices with benefit-dollar deltas HELD (M0). Nothing in v1 redefined.

**Phase-2 acceptance bar (restating so it's known in advance):** CSDA independently re-derives at
least one T-H dial-comparison cell by hand from the archetype + program parameters alone (the S1-vs-S2
months-to-breach delta is the natural candidate); verifies each T-D arm's leakage parameter traces to
its named literature statistic with the three-point sweep run; verifies all three adverse
possibilities carry explicit adjudications (found / not found / partial); four-tier labels universal;
no unregistered outcome measures.

*— CSDA (Fable), countersigned 2026-07-26. ECON-014 Phase 2 is GO.*
