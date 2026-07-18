#!/usr/bin/env python3
"""
run_scenario.py — the one-command reproducibility path (falsify-by-scenario-file).

Reproduces the repo's F1 headline end-to-end: net incremental federal receipts from
an AI-driven GDP uplift, under an employment-regime scenario YOU control.

    python model/run_scenario.py model/scenarios/stable.yml
    python model/run_scenario.py --all          # the three named regimes side by side
    python model/run_scenario.py my_regime.yml  # YOUR assumptions — the falsification path

The decomposition (FORMULAS.md §1):
    R = dGDP·[ λ·τ_L + (1−λ)·τ_K·(1−foreign)·realiz ] + d_emp·wage_base·GDP

Every parameter comes from the scenario file; nothing is hard-coded except the
documented defaults, all overridable. Output is DIRECTIONAL: this
reproduces the published structure, not a settled magnitude. To contest claim F1,
submit a scenario file whose documented assumptions flip its disconfirming test
(see CLAIMS.md and CONTRIBUTING.md).

Requires: Python 3.10+, PyYAML. No other dependencies; runs in <1s.
"""

import argparse
import sys
from pathlib import Path

# Portable console output (Windows cp1252 consoles included).
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required:  pip install pyyaml")

HERE = Path(__file__).resolve().parent
SCENARIOS = HERE / "scenarios"

# Documented defaults (FORMULAS.md §1 parameter table). Any scenario file may override any of them.
DEFAULTS = dict(
    gdp=46.6e12,      # baseline GDP anchor, $ (CBO-derived 2036; an anchor, not a forecast)
    uplift=0.03,      # cumulative GDP level uplift from AI (Acemoglu ~0.01 ... Goldman ~0.07)
    lam=0.55,         # marginal labor share of the new GDP (0.30 displacement ... 0.62 reinstatement)
    tau_L=0.26,       # effective federal rate on incremental wages (payroll + income)
    tau_K=0.15,       # effective federal rate on incremental domestic, realized capital income
    foreign=0.18,     # share of capital income leaking to foreign owners (Treasury TIC)
    realiz=0.60,      # near-term realization fraction of capital income
    d_emp=0.0,        # employment-LEVEL change (-0.02 displacement ... +0.02 reinstatement)
    wage_base=0.132,  # wage-riding receipts as a share of GDP (payroll 5.7% + wage income tax ~7.5%)
    naive_share=0.178,  # total federal receipts / GDP (the naive benchmark)
)


def load_scenario(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}
    unknown = set(raw) - set(DEFAULTS) - {"name", "notes", "source"}
    if unknown:
        sys.exit(f"{path.name}: unknown parameter(s) {sorted(unknown)} — see DEFAULTS in this script")
    p = {**DEFAULTS, **{k: v for k, v in raw.items() if k in DEFAULTS}}
    p["name"] = raw.get("name", path.stem)
    p["notes"] = raw.get("notes", "")
    return p


def receipts(p: dict) -> dict:
    dgdp = p["uplift"] * p["gdp"]
    share = p["lam"] * p["tau_L"] + (1 - p["lam"]) * p["tau_K"] * (1 - p["foreign"]) * p["realiz"]
    comp = dgdp * share
    emp = p["d_emp"] * p["wage_base"] * p["gdp"]
    naive = dgdp * p["naive_share"]
    return dict(share=share, comp=comp, emp=emp, net=comp + emp, naive=naive, dgdp=dgdp)


def money(x: float) -> str:
    return f"${x/1e9:,.0f}B"


def report(p: dict) -> None:
    r = receipts(p)
    print(f"\nscenario: {p['name']}" + (f"  -  {p['notes']}" if p["notes"] else ""))
    print(f"  uplift {p['uplift']:.1%} of GDP ({money(r['dgdp'])})  |  lam={p['lam']:.2f}  "
          f"d_emp={p['d_emp']:+.1%}  foreign={p['foreign']:.0%}")
    print(f"  receipts per $1 of new GDP : {r['share']:.1%}   (naive benchmark {p['naive_share']:.1%})")
    print(f"  composition channel        : {money(r['comp'])}/yr")
    print(f"  employment-level channel   : {money(r['emp'])}/yr")
    print(f"  NET incremental receipts   : {money(r['net'])}/yr   (naive: {money(r['naive'])}/yr)")
    if r["net"] <= 0:
        print("  -> receipts non-positive: under this regime the funding rule correctly yields NO budget.")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scenario", nargs="?", help="path to a scenario .yml")
    ap.add_argument("--all", action="store_true", help="run the three named regimes side by side")
    args = ap.parse_args()

    if args.all:
        for name in ("displacement", "stable", "increasing"):
            report(load_scenario(SCENARIOS / f"{name}.yml"))
    elif args.scenario:
        report(load_scenario(Path(args.scenario)))
    else:
        ap.print_help()
        sys.exit(1)
    print("\nDirectional output: structure reproduced, no magnitude established (see CLAIMS.md row M0).")


if __name__ == "__main__":
    main()
