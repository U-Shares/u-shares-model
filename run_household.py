"""ECON-014 public scenario runner -- edit a household_*.yml, rerun, compare.

Usage:  python run_household.py household_scenarios/household_A1_cashier.yml

Loads one household scenario file (calibrated archetype + editable scenario block),
runs the pre-registered Phase-1 engine (household_stress.py) for each dividend arm,
and prints threshold first-crossing months, orderings, and the ON-vs-OFF verdict
(AVOIDED / DELAYED / NO EFFECT) per the locked M4 metric.

Outputs are months and orderings only -- calibrated-archetype model outputs under
stated assumptions, deterministic incidence, never probabilities. See
ECON-014_Preregistration_Lock_v1.md (shipped alongside) for the threshold register,
metric definitions, and publication rules.
"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from household_stress import build_budget, simulate, compare  # noqa: E402

try:
    import yaml
except ImportError:
    sys.exit("This runner needs PyYAML:  pip install pyyaml")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    path = sys.argv[1]
    with open(path, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    arch = doc["parameters"]
    scen = doc["scenario"]
    placement = float(doc["placement"]["value"])
    shock_mult = float(scen["shock_mult"]["value"])
    shock_months = int(scen["shock_months"]["value"])
    budget = build_budget(arch)

    print("ECON-014 scenario run:", doc["archetype"], "-", doc.get("description", ""))
    print("  shock: labor x %.2f for %s months | placement $%.0f (dividend $%.2f/mo)"
          % (shock_mult, shock_months, placement, 0.05 * placement / 12.0))
    runs = {}
    for arm in scen.get("div_mode_arms", ["off", "on"]):
        s = {"shock_mult": shock_mult, "shock_months": shock_months}
        if arm != "off":
            s.update({"placement": placement, "div_mode": arm})
        runs[arm] = simulate(arch, budget, s)
        firsts = runs[arm]["first"]
        print("  arm %-8s first-crossing months: %s" % (
            arm.upper(),
            ", ".join("%s=m%d" % (k, v) for k, v in sorted(firsts.items(), key=lambda x: x[1]))
            or "none"))
    if "off" in runs and "on" in runs:
        print("  verdict (M4, ON vs OFF):")
        for thid, v in compare(runs["off"], runs["on"]).items():
            print("    %-5s %s" % (thid, v))
    print("Reminder: months/orderings are the publishable class; this is a calibrated "
          "archetype under stated assumptions, not 'a typical family'.")


if __name__ == "__main__":
    main()
