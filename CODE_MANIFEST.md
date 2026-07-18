# Code Manifest

## Reproduce one headline number in 60 seconds (the falsify-by-scenario-file path)

```
python model/run_scenario.py --all
```

reproduces claim **F1**'s headline end-to-end — net incremental federal receipts under the three
employment regimes — from documented parameters (`FORMULAS.md` §1). To contest it, copy a file in
`model/scenarios/`, change the assumptions, rerun, and submit the scenario file with your sources
(see `CONTRIBUTING.md`). Requires Python 3.10+ and PyYAML only; runs in under a second.

Each model is a small, reproducible script (fixed seeds; parameters declared at the top; standard
Python + numpy/scipy). Together they let a third party **reproduce or contest** every run. Parameters
are inputs to vary; outputs are directional, not established magnitudes.

| Model | Question it answers | Method | Key inputs | Data source |
|---|---|---|---|---|
| `ai_growth_receipts_gate.py` | Does AI GDP become federal receipts? | Receipts decomposition across 3 employment regimes | uplift, λ, τ_L/τ_K, foreign, d_emp | CBO/BEA receipts shares; Acemoglu/PWBM/Goldman growth; BLS labor share; Treasury TIC foreign ownership |
| `deficit_guardrail.py` | Is the credit deficit-neutral, and how much can it place? | Realized-only account dynamics; S_max = s·R/c; recession stress | s, c, R, cap, horizon | receipts from the gate; Provision-17 cap; 21% corporate rate |
| `claim3b_cyclical_stress.py` | Which firms can profitably issue, across the cycle? | Share of corporate universe clearing 3.95% / 5% / 7.58% bars, 2007–2025 | ROIC thresholds | Damodaran NYU EVA datasets (2007–2025) |
| `claim3_roa_replication.py` | Replicate the 7.58% self-financing break-even | Industry ROIC vs the claimed bar | thresholds | Damodaran NYU (Jan 2026) |
| `track_d_distribution.py` | How far up the poverty-first ladder does it reach? | Depth-first tier fill from S_max | capacity, tier populations, cap | Census poverty / ≤200%-FPL (approximate) |
| `tail_reserve_model.py` | How big a reserve backstops the floor? | One-factor Gaussian copula; Monte-Carlo ES / ruin | PD, ρ, LGD, notional | PBGC premium structure; insurance/Basel framework |
| `econ007_swfpwf.py` | Does a public-fund distribution rail add reach (κ) without degrading the base result? (DR1) | Paired ABM grid (144 cells × 100 seeds, common random numbers, pre-registered) | channels, holding window, appreciation, arm's-length flag | Base ABM (DS1); §6418 credit-market practice |

## What ships at launch vs. what follows
**At launch,** the runnable code is `model/run_scenario.py` + `model/scenarios/` (the F1 reproduction
above). The remaining models in the table below are documented here for transparency and are packaged
with their working papers in the post-launch buildout — each is a small, fixed-seed script whose method
and parameters are fully stated in `FORMULAS.md` and the relevant `claims/evidence/` file.

## Reproducing
- Python 3.13, `numpy`, `scipy`; `xlrd` for the legacy Damodaran `.xls` files.
- Each script prints its tables to stdout; parameters are at the top of each file and meant to be changed.
- Damodaran datasets are publicly downloadable (NYU Stern); the cyclical files are archived year-snapshots.

## Caveats (carried into every result)
- Damodaran data is **industry-level** (a supply proxy, not a firm census) and uses **ROIC** (a close
  cousin of ROA, running somewhat higher); survivorship bias ~1–2%.
- The employment dial (`d_emp`) is the contested parameter; the growth ladder spans published estimates.
- Tier populations are approximate (pin to Census SPM before quoting).
- No output is an established magnitude — see `CLAIMS.md` (row M0).
