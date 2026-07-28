# Open Questions — Household / Recipient (OQ-HH)

**Persona.** Ownership only disperses wealth if recipients *hold* it. Does the stake stick against the
retirement-account leakage record, and does the account design achieve the required retention without
excess paternalism or welfare loss?
**How to engage.** Claim via Issue (`question-claim.yml`) citing the OQ-ID. Claim links → `CLAIMS.md`.
*(Maintainer-written, contributor-read.)*

---

### OQ-HH-001 — Does the stake stick? (retention vs. leakage)
- **Question.** Given the 401(k)/IRA leakage record (low-income holders tend to leak more), what retention
  rate do low-wealth households actually achieve for a protected-account holding — and does it match what
  the dispersion result requires?
- **What an answer would look like.** An empirical estimate of the achievable retention rate (ρ) for
  low-wealth holders under a protected wrapper, benchmarked against the leakage literature, and checked
  against the stickiness the dispersion model needs (OQ-MD-001).
- **Links to claim.** RT1 (retention) · DS1 (dispersion — this ρ is its stickiness input).
- **Route.** Falsification (published empirical evidence).

### OQ-HH-002 — Does the account design achieve the required retention?
- **Question.** Does the hardship/conversion boundary produce the needed stickiness without over-restricting
  households or reducing welfare?
- **What an answer would look like.** A behavioral / mechanism analysis of the account rules (hardship,
  conversion to home/education/business) showing whether they deliver retention while preserving recipient
  welfare and autonomy.
- **Links to claim.** RT1 (retention — design facet).
- **Route.** Extension (design analysis).

### OQ-HH-003 — Conversion-mechanism outcomes (Provision 11)
- **Question.** Borrowing against / converting to home equity, business equity, or education is unique to
  this proposal — so no existing literature addresses it. What outcomes does the conversion mechanism
  actually produce?
- **What an answer would look like.** Applied-micro estimates of the effect on low-income homeownership,
  small-business formation, and educational attainment / debt avoidance.
- **Links to claim.** RT1 (retention) · F7 (poverty-first reach).
- **Route.** Extension (empirical program-outcomes study).

### OQ-HH-004 — Benefits-cliff / the adult asset-disregard
- **Question.** Placing a U-Share stake into a deep-poverty (SSI / means-tested) household can destroy
  more benefit value than it creates. Enacted law already shows the fix *for minors*: SSA excludes §530A
  (Trump) accounts from SSI income/resource tests during the growth period (through the year the child
  turns 17) — but that exclusion is **guidance-level, not statutory, and ends at adulthood** (post-17
  treatment "forthcoming"; the standard $2,000 SSI resource limit otherwise applies), with a full-balance
  ABLE rollover (SSI-disregarded to $100k) as the disability-gated escape. What **statutory, lifetime**
  disregard design closes the adult gap — and what does it cost?
- **What an answer would look like.** An interaction analysis vs SSI's $2,000 resource limit and
  dollar-for-dollar offsets across Medicaid pathways and SNAP; a disregard design generalizing the
  ABLE $100k model beyond disability and the §530A growth-period exclusion beyond childhood (statute,
  not revocable guidance); and its fiscal/behavioral cost. *(Note the durability angle: a guidance-level
  disregard is more fragile than even a statutory formula — see the lawful-redefinition lesson, OQ-PE-001.)*
- **Links to claim.** F7 (poverty-first ladder — its deepest-tier inversion risk) · RT1 (retention) ·
  CP1 (the §530A precedent/rails).
- **Route.** Falsification (published benefits-interaction evidence) / extension (disregard design).

### OQ-HH-005 — The flow-side disregard gap *(added 2026-07-26 — household stress study)*
- **Question.** Must the statutory asset-disregard extend to *dividend-derived savings* (ABLE-style,
  the §529A/§530A drafting pattern), not just account principal, for U-Shares to function at the SSI
  tier? Under a principal-only disregard, a calibrated SSI-household archetype that saves its dividend
  crosses the $2,000 resource limit at month 43 — the design would punish the deepest-tier household
  for accumulating, which is the behavior the program exists to produce. (Calibrated-archetype model
  output under stated assumptions; reproducible from the shipped archetype and engine files.)
- **What an answer would look like.** A legal-drafting analysis mapping the disregard across SSI, the
  SSI-linked Medicaid pathway, SNAP variants, and HOTMA housing rules — plus the study's second-phase
  dial results (principal-only vs ABLE-style; income-counted vs income-excluded) quantifying what each
  drafting variant is worth in months-to-breach and eligibility retention (pre-registered; the
  addendum ships with this release).
- **Links to claim.** F7 (deepest-tier reach) · RT1 (retention under wrappers) · OQ-HH-004 (the
  benefits-cliff line of work).
- **Route.** Falsification / drafting analysis; the in-house dial test is pre-registered.

### OQ-HH-006 — Dividend value conditional on emergency-credit terms *(added 2026-07-26 — household stress study)*
- **Question.** How much of the dividend's household-resilience value is conditional on the
  emergency-credit regime (APR, credit access) the household faces? The Phase-1 sensitivity sweep
  flipped 44 of 104 threshold verdicts — overwhelmingly on the APR (24%→400%) and credit-cap dials,
  not on dividend presence. Directionally: credit terms move household failure timelines more than a
  single-placement dividend does. An interaction, recorded honestly; not a policy proposal.
- **What an answer would look like.** An empirical mapping of the credit regimes low-wealth households
  actually face (payday and revolving-credit literatures) joined to the study's cliff map — under
  which regimes does the dividend's threshold-tier value survive, and under which is it swamped?
- **Links to claim.** RT1 · DS1 (the household side of dispersion).
- **Route.** Empirical joining (literature × cliff map); reproduction invited.

### OQ-HH-007 — Hardship-valve calibration *(added 2026-07-28 — household stress study, Phase 2)*
- **Question.** What hardship-access rule (caps, replenishment, draw conditions) preserves the
  wrapper's volatility-protection result without the deep-distress drain? The study's second phase
  found the sharp version of both edges: an *uncalibrated* valve converts the protected account to
  cash under deep sustained distress (fully drained in the first crisis), while against
  volatility-scale draws the same valve protects both the household AND most of the stake
  (calibrated seasonal-worker archetype: no borrowing, no housing failure, majority of the account
  retained at the 20-year mark). The empirical shape is now known; the design answer is open.
- **What an answer would look like.** Access-rule variants (draw caps per period, replenishment
  requirements, qualifying-event conditions) run through the shipped four-arm apparatus; a rule that
  holds the volatility result while bounding the deep-distress drain.
- **Links to claim.** RT1 (retention under wrappers) · OQ-HH-005 (the disregard's drafting) — an open
  design question, not a policy proposal.
- **Route.** Extension on the shipped apparatus (`run_household.py`, `model/household_stress.py`).

