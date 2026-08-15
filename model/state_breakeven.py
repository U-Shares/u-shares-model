"""state_breakeven.py -- ECON-016: state fiscal break-even conditions for the 20% placement credit.

THE QUESTION: under what conditions is a state's 20% U-Shares placement credit self-financing
from the state's own budget? This tool publishes the CONDITIONS, never a savings claim.

TWO LEVELS, never conflated:
  Level 1 -- Simple Accounting Break-Even (under full cost realization). Three inputs, hand-
    checkable: state share of program cost, per-enrollee cost, annual placement volume.
  Level 2 -- Budget-Realizable Break-Even. The same frame adjusted by parameters ONLY a state
    fiscal office can supply (marginal-cost realization, channel split, credit timing,
    cashability). If you don't supply them, this tool tells you what's missing -- it will not
    guess.

LEVEL 1'S SIX ENABLING ASSUMPTIONS (they print with every result):
  A. Caseload change counted is a REDUCTION IN NEED -- never an offset (an immediate benefit
     cut caused by receiving a U-Share is not a saving; the household is no better off).
  B. Average per-enrollee spending approximates marginal avoidable cost (realization = 1.0).
  C. The financing share matches the affected eligibility group (ACA expansion adults carry a
     10% state share -- five times less recapture per avoided enrollee than a 50%-share group).
  D. Savings are cashable to the same budget that pays the credit (county savings don't pay a
     state credit).
  E. Credit cost and savings are recognized contemporaneously (they aren't -- see the timing
     output: credits are paid on the FLOW of placements, recapture accrues on the STOCK).
  F. No material cross-program interaction.

FALSIFY ME: copy scenarios/state_template.yml, enter your state's three numbers (and Level-2
parameters if you have them), and run:  python state_breakeven.py scenarios/your_state.yml
All outputs are the formula's response to YOUR stated inputs -- not a prediction for any state.
Provenance: the ECON-016 pre-registration gate and results memo ship with this repository.
"""
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CREDIT_RATE = 0.20  # White Paper Provision 8 (the eleven-provision scheme)

ASSUMPTIONS = "  [Level-1 assumptions A-F apply -- see this file's header. Level 1 is an\n" \
              "   ACCOUNTING break-even; it becomes a FISCAL result only through Level 2.]"

def level1(share, cost, placed):
    credit = CREDIT_RATE * placed
    per_ey = share * cost
    return credit, per_ey, credit / per_ey

def timing(share, cost, placed_per_year, ramp, years=10):
    cum_c = cum_r = 0.0; max_def = 0.0; first = None; rows = []
    for y in range(years):
        cum_c += CREDIT_RATE * placed_per_year
        cum_r += ramp[min(y, len(ramp) - 1)] * share * cost
        d = cum_c - cum_r; max_def = max(max_def, d)
        if first is None and d <= 0: first = y + 1
        rows.append((y + 1, round(cum_c), round(cum_r), round(d)))
    return rows, round(max_def), first

def main():
    scen = None
    if len(sys.argv) > 1:
        try:
            import yaml
            scen = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
        except ImportError:
            sys.exit("PyYAML needed for scenario files: pip install pyyaml")
    if scen:
        s, c, p = float(scen["state_share"]), float(scen["per_enrollee_cost"]), float(scen["annual_placements"])
        label = scen.get("label", "your inputs")
    else:
        s, c, p = 0.40, 8000.0, 10e6
        label = "HYPOTHETICAL ILLUSTRATION (labeled; not any real state)"
    credit, per_ey, be = level1(s, c, p)
    print(f"=== Level 1: Simple Accounting Break-Even -- {label} ===")
    print(f"  inputs: state share {s:.2f} | per-enrollee cost ${c:,.0f} | placements ${p:,.0f}/yr")
    print(f"  credit cost: ${credit:,.0f}/yr")
    print(f"  state saving per avoided enrollee-year: ${per_ey:,.0f}")
    print(f"  BREAK-EVEN: {be:,.1f} avoided enrollee-years/yr "
          f"({CREDIT_RATE*1e6/per_ey:,.1f} per $1M placed)")
    print(ASSUMPTIONS)
    lvl2_keys = ("realization_factor", "enrollment_channel_share", "credit_timing_years")
    supplied = {k: scen[k] for k in lvl2_keys if scen and k in scen}
    if len(supplied) == len(lvl2_keys):
        r = float(supplied["realization_factor"])
        print(f"\n=== Level 2: Budget-Realizable (your parameters) ===")
        print(f"  realizable saving/enrollee-year: ${per_ey * r:,.0f} "
              f"-> break-even {credit/(per_ey*r):,.1f} enrollee-years/yr (x{1/r:.2f} vs Level 1)")
    else:
        missing = [k for k in lvl2_keys if k not in supplied]
        print(f"\n=== Level 2: STATE SUPPLIES -- missing parameters: {', '.join(missing)} ===")
        print("  (Deliberate: no national defaults exist for these. Your fiscal office holds them.)")
    ramp = scen.get("avoided_enrollee_years_ramp") if scen else None
    ramp = ramp or [0, 40, 100, 180, 280, 400, 520, 625, 625, 625]  # the accepted illustration's ramp
    rows, max_def, first = timing(s, c, p, [float(x) for x in ramp])
    print(f"\n=== Timing (ramp {'from your file' if scen and 'avoided_enrollee_years_ramp' in (scen or {}) else 'STYLIZED, labeled'}) ===")
    print(f"  max cumulative pre-break-even deficit: ${max_def:,}")
    print(f"  first cumulative break-even year: {first if first else 'not within 10 years'}")
    print("  NOTE: credits pay on the FLOW of placements; recapture accrues on the STOCK --")
    print("  a ramp that only reaches the steady-state rate never repays the accumulated deficit.")

if __name__ == "__main__":
    main()
