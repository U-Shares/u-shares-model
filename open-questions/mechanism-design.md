# Open Questions — Mechanism-Design Economist (OQ-MD)

**Persona.** Does the Capital Dispersion Engine actually disperse? Are the named mechanisms — the
**Stickiness Coefficient** and the **Household Reservoir Operator** — real and load-bearing, and does the
incentive structure induce the firm behavior the mechanism needs?
**How to engage.** Claim a question by opening an Issue (`question-claim.yml`) citing its OQ-ID. See
`CALL_FOR_PAPERS.md` for what counts as *falsification* vs. *extension*. Claim links point to `CLAIMS.md`.
*(Maintainer-written, contributor-read: submit scenario files / issues, not edits to this register.)*

---

### OQ-MD-001 — Does the mechanism disperse? *(foundational)*
- **Question.** In a realistically-calibrated wealth-dynamics model, does converting income into *held
  principal* for low-wealth households measurably compress the stationary distribution?
- **What an answer would look like.** A calibrated Bouchaud-Mézard-class (or comparable) model with the
  U-Share intervention as a parameter, reporting the change in a stationary inequality metric (Gini, or
  the tail index μ = 1 + J/σ²) versus a no-intervention baseline, with explicit sensitivity to the
  retention/"stickiness" parameter — submitted as a **scenario file** that confirms or flips the linked
  claim's disconfirming test. Specifically including:
  - **The negative-wealth / full-Gini calibration gap.** The current agent-based model floors wealth at
    zero, so it cannot represent the ~8% of US households with negative net worth; it matches the top
    tail but under-shoots the full Gini. Closing the gap means an ABM with debt / life-cycle structure,
    re-calibrated to the full Lorenz curve, with sensitivity analysis.
- **Links to claim.** DS1 (dispersion) · F7 (poverty-first reach).
- **Route.** Falsification (scenario run / model error / published empirical).

### OQ-MD-002 — Does the incentive actually induce issuance?
- **Question.** Clearing the ~3.95% after-tax break-even is necessary, not sufficient. Do firms
  voluntarily issue at the scale the mechanism needs, and how fast?
- **What an answer would look like.** A firm-level (not industry-level) adoption model, or an empirical
  study of comparable instruments (REIT / preferred-share issuance behavior), estimating take-up under the
  credit + deduction structure and its speed — accounting for the named adoption frictions (transaction
  costs and credit monetization).
- **Links to claim.** F4 (firm-level issuance adoption) · F5 (general bar cleared across the cycle).
- **Route.** Falsification (empirical / model).

### OQ-MD-003 — Calibrate the within-household shock correlation
- **Question.** The Household Reservoir Operator result (per-member universality buffers hardship better
  than earner-tied accounts) holds directionally but is governed by an unmeasured parameter: the
  correlation of shocks within a household. What is that correlation?
- **What an answer would look like.** A calibration from the SCF / Fed SHED / PSID, with the retention
  effect re-estimated.
- **Links to claim.** F7 (poverty-first reach) · RT1 (retention).
- **Route.** Extension (empirical calibration).

### OQ-MD-004 — Convert directional dispersion results to validated effect sizes
- **Question.** The dispersion and retention predictions currently hold as signs and orderings. What are
  the effect sizes?
- **What an answer would look like.** Effect sizes (not just signs and orderings) for the dispersion and
  retention predictions, with sensitivity analysis.
- **Links to claim.** F7 (poverty-first reach) · M0 (magnitudes held) · DS1 (dispersion).
- **Route.** Extension.

### OQ-MD-005 — Adjudicate the holding-cap specification
- **Question.** An early build produced an implausible tail (Hill α ≈ 31) from modeling the reserve as an
  unbounded, perfectly-equal block; the holding cap restored a credible tail. The cap was added after
  pre-registration — is the specification defensible?
- **What an answer would look like.** A credentialed modeler's specification decision on the cap and its
  effect on the retention statistic, with sensitivity.
- **Links to claim.** F7 (poverty-first reach) · DS1 (dispersion).
- **Route.** Extension (model-specification review).

### OQ-MD-006 — The pump-rate frontier *(added 2026-07-22 — *The Last Economy* study)*
- **Question.** What continuous placement flow ("pump rate") holds the periphery's wealth share at
  preferential-attachment strength α — and does the frontier's observed flatness survive when
  attachment reaches the protected accounts themselves? In-house first pass: `model/t2b_pump_frontier.py`
  (flat frontier through α≈1.8) and `model/t2c_wrapper_breach.py` (tested breaches degrade gracefully
  and are pumpable; stopping the flows is what kills dispersion) — both structural, sign/ordering only.
- **What an answer would look like.** Reproduction on calibrated network data; attachment-on-accounts
  variants beyond t2c's permeability/rake dials; an analytic frontier if one exists.
- **Links to claim.** DS1 (dispersion) · DR1 (the rail's κ) · GV1 (the flows-first protection ordering).
- **Route.** Reproduction + extension (the harnesses ship in `model/`).

### OQ-MD-007 — Above-floor account composition and recovery participation *(added 2026-07-28 — household stress study, Phase 2)*
- **Question.** The floor's income is contractually independent of portfolio composition — 5% on
  original issue price, an issuer obligation behind the guaranty — so the income-vs-appreciation
  tension cannot touch floor income. The residual: does the composition of account holdings *above*
  the floor materially change recovery-participation outcomes (the crash-into-boom class)?
- **What an answer would look like.** Composition variants (floor-heavy vs appreciation-weighted
  above-floor holdings) through a recovery-participation kernel with a household leakage channel;
  or a design argument that composition above the floor is out of scope for the guarantee.
- **Links to claim.** F6 (account design and the guaranty) · CP1 (comparators' composition rules).
- **Route.** Extension (model-specification review).

