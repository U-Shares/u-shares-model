# Evidence — RT1: The required retention is plausible under a protected wrapper (not yet estimated)

**Claim (register):** Low-wealth holders can achieve the retention rate ρ the dispersion result requires,
under a protected account wrapper (anchored to 401(k)/IRA leakage literature; not yet estimated).
**Status: `open`.**
**Warrant (proposed):** the 401(k)/IRA leakage literature bounds what low-wealth holders retain in
unprotected wrappers, while ABLE and §530A's growth-period exclusion show protected wrappers produce
materially higher stickiness — the required ρ is plausible but not yet empirically estimated.

## Why retention is load-bearing
The dispersion mechanism (DS1) is monotone in ρ: with low retention the placed principal leaks out and
the compression washes out (the H1 result — retention *dominates* the outcome, more than the dividend
rate or placement size). RT1 is therefore DS1's key empirical input, and the household-side twin of the
mechanism claim.

## The evidence base
1. **The leakage literature (the anchor, cutting both ways).** Pre-retirement leakage from 401(k)/IRA
   wrappers is substantial; **low-income holders leak more** (hardship withdrawals, cashouts at job
   change); and — the sobering datum — *granted* money does not stick better than earned money. An
   unprotected U-Share stake would leak. This is the honest floor of the estimate.
2. **Wrapper design moves ρ (the counter-evidence).** The U-Share account is deliberately harder-walled
   than a 401(k): value leaves only by hardship or **conversion to another capital asset** (home,
   education, business — Provision 11), not cash-out. Enacted precedents show harder walls produce
   stickiness: §530A accounts bar withdrawal during the entire growth period (a legally enforced ρ≈1 for
   minors); ABLE accounts hold assets with means-test protection to $100k. The design question is the
   *adult* wrapper (see OQ-HH-002/HH-004).
3. **The household-structure result.** Per-member pooling (the Household Reservoir Operator, H6) buffers
   idiosyncratic hardship shocks better than earner-tied accounts at the same total — raising effective
   household-level retention; governed by the unmeasured within-household shock correlation (OQ-MD-003).

## Honest limits (why `open`)
No empirical ρ estimate exists for *this* wrapper for *adult, low-wealth* holders — the leakage
literature measures different wrappers, and the enacted hard-wall precedents cover minors (§530A) or the
disability-gated (ABLE). Conversion-to-capital (unique to this design) has no outcome literature at all
(OQ-HH-003). The dispersion-required ρ threshold itself is a model quantity (held, M0).

## Disconfirming test (register)
An empirical ρ estimate under comparable wrappers materially below the dispersion model's requirement.

## Annotation — household stress study, Phase 1 *(added 2026-07-26; status-neutral)*
At a single $2,800 placement under sustained severe income shocks, dividend effects are mostly
arithmetic-tier (runway extension) rather than threshold-tier — the study's pre-registered
"too-small-to-matter" adverse possibility PARTIALLY materialized and is reported here per its
bidirectional commitment (final adjudication in the second phase). The counter-structure in the same
map: threshold-tier value concentrates under income VOLATILITY (calibrated seasonal-worker archetype:
high-cost-borrowing entry delayed +6 months at $2,800 under a −50% shock, with a clean placement-size
dose–response reaching AVOIDED at accumulated-holdings scale), and a market crash to −80% produces
zero threshold events in any arm — the floor severs the crash-to-budget channel structurally. All
figures are calibrated-archetype model outputs under stated assumptions, reproducible from the shipped
scenario files; deterministic incidence, not probabilities; dollar magnitudes held (M0). The
pre-registration lock ships in this release for date verification.

## Sources / provenance
Retirement-leakage literature (401(k)/IRA cashout and hardship studies — the retention anchor);
`h6_household_pooling.py`, `h1_retest.py` (ECON-005 line); §530A verification memo (2026-07-18); ABLE
(§529A) design; OQ-HH-001/-002/-003/-004. *Directional (see M0).*
