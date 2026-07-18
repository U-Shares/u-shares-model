# Evidence — DR1: The distribution rail (public-fund channels into placement)

**Claim (register, as proposed):** A public-fund distribution rail — inflow channels feeding
credit-funded placement, with a recycling multiplier (κ), a capped holding window, and mandatory
arm's-length separation — adds *reach and speed* to placement rather than additional distributional
compression, which the holding cap already binds (structure only; magnitudes held).
**Status: proposed `open`** — the computed structure is reproducible, but the rail's linchpin (a
transferable credit on *unrealized* appreciation) awaits legal review, and the baseline calibration is
provisional. CSDA applies the final status.
**Warrant (proposed):** paired agent-based runs (common random numbers) show the rail's channels raise
*reach* (κ grows with the holding window) while the bottom-share effect stays marginal under the binding
per-person cap — and affiliation without arm's-length separation collapses recycling to κ≈1 at equal
fiscal cost, which is why the separation is a design requirement, not an ornament.

## What the rail is
Three structurally-identical **inflow channels** (a public/sovereign-fund anchor is the modeled
representative; donation and consideration variants are adapters into the same mechanism) deliver equity
to an intermediary that places U-Shares into qualifying accounts, earning a transferable placement
credit; sale proceeds within a **capped holding window** recycle into further placement (the multiplier
κ); **arm's-length separation** between donor and intermediary is mandatory.

## The computed findings (directional; all reproducible from the fixed-seed grid)
1. **The honest headline first: the rail does NOT buy extra bottom-share compression.** Across a
   144-cell × 100-seed paired grid, the largest marginal bottom-quintile effect was ≈ +0.0001 — because
   the base program already lifts recipients to the per-person holding cap, extra channel issuance
   largely spills. **The rail's value is scale, speed, and reach (κ), plus its credit-cost structure —
   not a bigger distributional delta.** A claim that it *did* compress further would be false-precision.
2. **Recycling rises with the holding window.** κ ranged ≈ **1.02–1.14** across live cells (directional
   model outputs): window 1y → κ≈1.03, 3y → κ≈1.05, 5y → κ≈1.10. Longer windows buy recycling but delay
   distribution and enlarge the market-contingent credit slice — a genuine tradeoff, with a **3-year cap
   at the knee** in this parameterization (knee location sensitive to the appreciation process).
3. **Arm's-length is load-bearing, quantified.** Modeled affiliation (donor and intermediary united)
   captured the monetized credit *without recycling it*: reach collapsed to κ≈1 while the credit cost was
   still incurred — **no distribution benefit at equal-or-greater fiscal cost.** This is the computed
   case for the mandatory separation plus disqualified-person and third-party-appraisal safeguards.
4. **The intermediary's market-contingent credit slice is material** (≈6–33% of total credit across
   cells, rising with appreciation) and is a **risk-adjusted cost band, not a point estimate.**

## Sensitivity
κ is monotone in the window and the appreciation increment; the ΔB5-marginality is a consequence of the
binding cap (relax the cap and the rail's distributional role re-opens — see OQ-MD-005 on the cap
specification); channel mix (anchor vs adapters) is a follow-on sweep, not yet run.

## Honest limits (why `open` is proposed)
- **The legal crux.** The intermediary's credit accrues partly on **unrealized appreciation** — legally
  aggressive and fiscally open-ended in the model's own caveat; the window cap is the modeled
  mitigation, but viability is a legal-review question (kin to L1), not a modeling result.
- **The κ ceiling is unset.** General-business-credit limits (IRC §38(c)) bound κ in practice; the
  numeric ceiling needs a buyer-pool tax-capacity estimate. Modeled κ is uncapped.
- **Provisional baseline.** Results inherit the provisional calibration (see DS1's contest); they are
  paired-difference structural findings, robust in *sign and ordering*, with magnitudes held.
- All computed ranges above (κ, cost shares) are **reproducible directional model outputs — no magnitude
  established (see M0).**

## Disconfirming test (proposed)
A calibrated run or legal determination showing the rail cannot lawfully sustain κ materially above 1
(e.g., the unrealized-appreciation credit fails legal review, or the §38(c) ceiling binds at κ≈1) — or a
run showing channel issuance materially degrades the base program's distributional result.

## Sources / provenance
`econ007_swfpwf.py` (144-cell × 100-seed common-random-number grid; pre-registered; fixed seeds;
checkpointed) + `econ007_grid_result.json` + the ECON-007 scaffold/grid notes (2026-06-15); the base ABM
(`ushares_abm.py`, see DS1); §6418 transferable-credit market practice; IRC §38(c). *Directional; no
magnitude established (see M0).*
