# Evidence — DS1: The dispersion mechanism

**Claim (register):** Converting a slice of income into held principal measurably compresses the
stationary wealth distribution for low-wealth households (directional; magnitudes held).
**Status: `contested`** — the calibration contest is presented in full below.
**Warrant (proposed):** in Bouchaud-Mézard-class wealth dynamics, wealth concentrates because returns
compound on holdings; placing *retained principal* at the bottom raises the exchange/coupling term for
low-wealth agents, which is exactly the parameter that fattens the lower distribution and compresses the
stationary tail — an effect that survives only at sufficient retention (stickiness).

## Derivation
1. **Framework.** Bouchaud-Mézard exchange economy: stationary Pareto tail index μ = 1 + J/σ² (coupling J
   vs idiosyncratic return volatility σ²). Reproduction of the published stationary behavior validated
   (G0 pass) before any intervention was modeled. Engine: `ushares_abm.py`.
2. **The intervention.** U-Share placement = a flow of principal to low-wealth agents with a retention
   parameter ρ (the "Stickiness Coefficient") and a 5% coupon on issue value. Directional results, all at
   stated parameters: retention dominates the outcome (H1 — with low ρ the effect washes out); placement
   compresses top/bottom ratios more than equal-cost dividend checks (Q1 — "the compression comes from
   holding the principal, not from the size of the check"); redistribution thins the extreme tail (H2);
   per-member household pooling buffers hardship better than earner-tied accounts (H6, common-random-
   number paired runs).
3. **Calibration state.** Top-tail behavior matches the US wealth distribution's Pareto region (G1
   partial pass); the model floors wealth at zero.

## Sensitivity
The compression effect is monotone in ρ and in the placed flow; it weakens as the coupon is diverted to
consumption (low ρ) and is insensitive to the dividend *rate* per se (ownership drives it; income is
separate — the Q1 finding). Holding-cap specification affects the extreme tail (see OQ-MD-005 — the cap
was added after an implausible α≈31 tail appeared in an early build; a credentialed specification review
is invited).

## The contest (presented fairly — why the status is `contested`)
**The negative-wealth / full-Gini calibration gap (WS-4, mechanism-design persona).** Because the ABM
floors wealth at zero, it cannot represent the ~8% of US households with negative net worth; it matches
the top tail but **under-shoots the full Gini**. The full-distribution version of the dispersion claim is
therefore credibly parked: what is demonstrated is compression in a zero-floored economy calibrated to
the Pareto region, not in a debt-bearing, life-cycle economy calibrated to the full Lorenz curve. Closing
this requires an ABM with debt/life-cycle structure re-calibrated to the full distribution, with
sensitivity (OQ-MD-001's stated answer-shape). Effect *sizes* (vs signs and orderings) are additionally
open (OQ-MD-004), and all magnitudes are held (M0).

## Disconfirming test (register)
A realistically-calibrated wealth-dynamics model (negative-wealth households included) showing no material
compression of Gini / tail-index μ at plausible retention (stickiness) values.

## Sources / provenance
`ushares_abm.py` and the ECON-005 increment/result files (`03_AiS_Engine/04_Data Sources/UShares_Analysis/`);
ECON-005 white paper (Dynamics of Capital Dispersion, internal v0.2); Bouchaud & Mézard (2000);
retention-leakage literature (see RT1). *Directional; no magnitude established (see M0).*
