"""ECON-014 Household Resilience Stress Test (HRST) - Phase 1 simulator.

Governed by ECON-014_Preregistration_Lock_v1.md (CSDA-countersigned). Deterministic
monthly cash-flow engine over the six calibrated archetypes in econ014_archetypes.json.
Runs T-A (labor loss), T-B (wage loss + inflation), T-C (crash w/ preserved floor),
T-G (cliff map) plus the one-at-a-time threshold sensitivity annex.

Outputs econ014_phase1_results.json. All metrics are the lock's M1-M4/M7; M5/M6 are
recorded raw but flagged Phase-2. Deterministic incidence only - no probabilities.

Behavioral rules NOT in the lock's threshold register (documented engine structure):
  R-a Discretionary spending funds only from current-month income surplus, never from
      savings; in deficit months it drops to zero before any liquid draw (optimistic-
      for-resilience in ALL arms equally; deltas unaffected).
  R-b Surplus waterfall: debt paydown first, then liquid rebuild.
  R-c Unpaid-obligation order under exhausted credit (lock TH-2 priority): debt-service
      interest capitalizes first, housing missed second, non-housing essentials third.
  R-d Transfers fixed at baseline through shocks (except A4's UI rule) - flagged
      limitation; overstates stress in all arms equally.
  R-e UI applies only to A4 (the lock's named-statistic rule); -100% arms for other
      archetypes are no-UI worst cases, flagged.
  R-f A3 consumes surplus above a $1,900 liquid buffer (statute-induced behavior under
      the $2,000 SSI resource limit); the A3_save variant accumulates instead and
      reports the TH-6 crossing month (the dividend-accumulation observation).
  R-g Calendar: t=1 is January (A2 seasonality).
"""
import json
import sys
import os

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
HORIZON = 60

TH_DEFAULTS = {"k1": 1.0, "apr": 0.36, "util_grace": 2, "evict_n": 3, "debt_b": 6.0}


def load_archetypes():
    with open(os.path.join(HERE, "econ014_archetypes.json"), "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["archetypes"], data["_meta"]


def build_budget(arch):
    """Baseline monthly budget. Shares-based (CE lowest-quintile shares x resources)
    or explicit (A5/A6). Returns dict of baseline obligations."""
    labor = arch["labor_monthly"]["value"]
    transfers = arch["transfers_monthly"]["value"]
    resources = labor + transfers
    debt0 = arch["debt_start"]["value"]
    if "explicit_budget" in arch:
        eb = arch["explicit_budget"]
        rent = eb["rent"]
        ess_nh = (eb["utilities"] + eb["operations"] + eb["food"]
                  + eb.get("childcare", 0.0) + eb.get("care_costs", 0.0)
                  + eb["transport_essential"] + eb["healthcare"])
        contractual = eb.get("student_loan", 0.0)
        childcare = eb.get("childcare", 0.0)
    else:
        sh = arch["shares"]
        housing_cat = sh["housing_cat"] * resources
        rent = 0.65 * housing_cat
        util = 0.25 * housing_cat
        ops = 0.10 * housing_cat
        food = sh["food"] * resources
        transport_ess = 0.7 * sh["transport"] * resources
        health = sh["healthcare"] * resources
        ess_nh = util + ops + food + transport_ess + health
        contractual = 0.0
        childcare = 0.0
    disc = max(0.0, resources - rent - ess_nh - contractual - debt0 * TH_DEFAULTS["apr"] / 12.0)
    return {"resources": resources, "labor": labor, "transfers": transfers,
            "rent": rent, "ess_nh": ess_nh, "contractual": contractual,
            "disc": disc, "childcare": childcare}


def simulate(arch, budget, scen, th=None):
    """One deterministic 60-month run. Returns threshold first-crossing months,
    ordering, and raw trackers."""
    th = dict(TH_DEFAULTS, **(th or {}))
    mrate = th["apr"] / 12.0
    labor0 = budget["labor"]
    transfers = budget["transfers"]
    liquid = arch["liquid_start"]["value"]
    debt = arch["debt_start"]["value"]
    cap = arch.get("borrow_cap_override",
                   th["debt_b"] * (labor0 + transfers))
    placement = scen.get("placement", 0.0)
    div0 = 0.05 * placement / 12.0
    div_mode = scen.get("div_mode", "off")  # off|on|indexed|frozen|proportional
    pi = scen.get("pi", 0.0)
    pi_variant = scen.get("pi_variant", "general")  # general|housing
    f = (1.0 + pi) ** (1.0 / 12.0) if pi > 0 else 1.0
    drop = scen.get("account_drop", 0.0)
    account_value = placement * (1.0 - drop)
    mult = scen.get("shock_mult", 1.0)
    dur = scen.get("shock_months", HORIZON)
    seasonal = arch.get("seasonal_profile")
    ssi_limit = arch.get("ssi_resource_limit", {}).get("value")
    a3_consume = ssi_limit is not None and not scen.get("save_dividend", False)
    ui_rep = arch.get("ui_replacement", {}).get("value") if isinstance(
        arch.get("ui_replacement"), dict) else None
    ui_months = int(arch.get("ui_months", {}).get("value", 0)) if isinstance(
        arch.get("ui_months"), dict) else 0

    first = {}   # TH id -> first month
    events = []  # (month, TH)
    miss_housing_consec = 0
    ess_unpaid_consec = 0

    def fire(thid, m):
        if thid not in first:
            first[thid] = m
            events.append((m, thid))

    for t in range(1, HORIZON + 1):
        infl = f ** (t - 1)
        rent_t = budget["rent"] * (infl if pi > 0 else 1.0)
        if pi_variant == "housing" and pi > 0:
            ess_t = budget["ess_nh"]  # housing-concentrated: only rent inflates
        else:
            ess_t = budget["ess_nh"] * (infl if pi > 0 else 1.0)
        smult = 1.0
        if seasonal:
            cal = ((t - 1) % 12) + 1
            if cal in seasonal["months_low"]:
                smult = seasonal["mult_low"]
            elif cal in seasonal["months_high"]:
                smult = seasonal["mult_high"]
        shock = mult if t <= dur else 1.0
        labor = labor0 * shock * smult
        ui = 0.0
        if ui_rep and mult == 0.0 and t <= min(ui_months, dur):
            ui = ui_rep * labor0
        if div_mode in ("on", "frozen"):
            div = div0
        elif div_mode == "indexed":
            div = div0 * infl
        elif div_mode == "proportional":
            div = div0 * (1.0 - drop)
        else:
            div = 0.0
        # childcare scales with employment share (A5 rule)
        ess_month = ess_t
        if arch.get("childcare_scales_with_employment") and budget["childcare"] > 0:
            ess_month = ess_t - budget["childcare"] * (1.0 - shock) * (infl if (pi > 0 and pi_variant != "housing") else 1.0)
        income = labor + transfers + ui + div
        debt_min = debt * mrate
        obligations = ess_month + rent_t + budget["contractual"] + debt_min

        if income >= obligations:
            disc_paid = min(budget["disc"], income - obligations)
            surplus = income - obligations - disc_paid
            pay = min(debt, surplus)
            debt -= pay
            liquid += surplus - pay
            miss_housing_consec = 0
            ess_unpaid_consec = 0
        else:
            shortfall = obligations - income
            use = min(liquid, shortfall)
            liquid -= use
            rem = shortfall - use
            if rem > 1e-9:
                avail = max(0.0, cap - debt)
                b = min(avail, rem)
                if b > 1e-9:
                    debt += b
                    fire("TH-3", t)
                rem -= b
                if debt >= cap - 1e-9 and b > 0:
                    fire("TH-7", t)
            if rem > 1e-9:
                # R-c order: debt interest capitalizes, then housing, then essentials
                unpaid_debt = min(debt_min, rem)
                debt += unpaid_debt
                rem -= unpaid_debt
                if rem > 1e-9:
                    unpaid_housing = min(rent_t, rem)
                    rem -= unpaid_housing
                    if unpaid_housing > 1e-9:
                        fire("TH-2", t)
                        miss_housing_consec += 1
                        if miss_housing_consec >= th["evict_n"]:
                            fire("TH-5", t)
                    if rem > 1e-9:
                        ess_unpaid_consec += 1
                        if ess_unpaid_consec >= th["util_grace"]:
                            fire("TH-4", t)
                    else:
                        ess_unpaid_consec = 0
                else:
                    miss_housing_consec = 0
                    ess_unpaid_consec = 0
            else:
                miss_housing_consec = 0
                ess_unpaid_consec = 0
        # A3 statute-induced consumption above buffer (R-f)
        if a3_consume and liquid > 1900.0:
            liquid = 1900.0
        if ssi_limit and liquid > ssi_limit:
            fire("TH-6", t)
        if liquid < th["k1"] * (ess_month + rent_t):
            fire("TH-1", t)

    ordering = [thid for (_, thid) in sorted(events)]
    return {"first": first, "ordering": ordering,
            "end_liquid": round(liquid, 2), "end_debt": round(debt, 2),
            "end_account_value_PHASE2_METRIC": round(account_value, 2)}


def compare(off, on):
    """M4: per-threshold AVOIDED / DELAYED(d) / EARLIER / NO EFFECT, ON vs OFF."""
    out = {}
    ths = set(off["first"]) | set(on["first"])
    for thid in sorted(ths):
        mo, mn = off["first"].get(thid), on["first"].get(thid)
        if mo is not None and mn is None:
            out[thid] = "AVOIDED"
        elif mo is None and mn is not None:
            out[thid] = "APPEARS_IN_ON(m%d)" % mn
        elif mo is not None and mn is not None:
            d = mn - mo
            out[thid] = ("DELAYED(+%d)" % d) if d > 0 else (
                "EARLIER(%d)" % d if d < 0 else "NO_EFFECT")
    return out


def run_all():
    archs, meta = load_archetypes()
    P = meta["placement_default"]["value"]
    results = {"_lock": "ECON-014_Preregistration_Lock_v1.md",
               "_date": "2026-07-26", "_horizon_months": HORIZON}

    # ---- T-A: labor income shocks ----
    ta = {}
    for name, arch in archs.items():
        budget = build_budget(arch)
        ta[name] = {}
        for sev in (0.25, 0.50, 0.75, 1.00):
            for dur in (6, 12, 24, HORIZON):
                key = "sev%d_dur%s" % (int(sev * 100), "sust" if dur == HORIZON else dur)
                off = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": dur})
                on = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": dur,
                                             "placement": P, "div_mode": "on"})
                ta[name][key] = {"OFF": off, "ON": on, "M4": compare(off, on)}
    results["T-A"] = ta

    # ---- T-B: wage loss + inflation ----
    tb = {}
    for name, arch in archs.items():
        budget = build_budget(arch)
        tb[name] = {}
        for pi in (0.03, 0.05, 0.10):
            for variant in ("general", "housing"):
                base = {"shock_mult": 0.75, "shock_months": HORIZON,
                        "pi": pi, "pi_variant": variant, "placement": P}
                off = simulate(arch, budget, dict(base, div_mode="off"))
                frozen = simulate(arch, budget, dict(base, div_mode="frozen"))
                indexed = simulate(arch, budget, dict(base, div_mode="indexed"))
                key = "pi%d_%s" % (int(pi * 100), variant)
                tb[name][key] = {"OFF": off, "FROZEN": frozen, "INDEXED": indexed,
                                 "M4_indexed_vs_off": compare(off, indexed),
                                 "M4_indexed_vs_frozen": compare(frozen, indexed)}
    results["T-B"] = tb

    # ---- T-C: crash with preserved floor (no income shock) ----
    tc = {}
    for name, arch in archs.items():
        budget = build_budget(arch)
        tc[name] = {}
        for drop in (0.2, 0.4, 0.6, 0.8):
            base = {"account_drop": drop, "placement": P}
            pres = simulate(arch, budget, dict(base, div_mode="on"))
            prop = simulate(arch, budget, dict(base, div_mode="proportional"))
            off = simulate(arch, budget, dict(base, div_mode="off"))
            tc[name]["drop%d" % int(drop * 100)] = {
                "PRESERVED": pres, "PROPORTIONAL": prop, "OFF": off,
                "M4_preserved_vs_off": compare(off, pres)}
    results["T-C"] = tc

    # ---- T-G: cliff map ----
    tg = {}
    for name, arch in archs.items():
        budget = build_budget(arch)
        tg[name] = {}
        for sev in (0.25, 0.50, 0.75, 1.00):
            base_off = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON})
            row = {}
            for pl in (1000.0, 2800.0, 5000.0, 10000.0, 20000.0):
                on = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON,
                                             "placement": pl, "div_mode": "on"})
                row["P%d" % int(pl)] = {"first": on["first"], "M4_vs_P0": compare(base_off, on)}
            tg[name]["sev%d" % int(sev * 100)] = {"P0_first": base_off["first"], "by_placement": row}
    results["T-G"] = tg

    # ---- A3 dividend-accumulation observation (TH-6 flow-side) ----
    arch = archs["A3_daniel_ssi_household"]
    budget = build_budget(arch)
    save_run = simulate(arch, budget, {"placement": P, "div_mode": "on",
                                       "save_dividend": True})
    results["A3_save_variant_TH6_observation"] = {
        "first": save_run["first"],
        "note": "A3 saving (not consuming) the dividend: month at which accumulated cash "
                "crosses the $2,000 SSI resource limit - the FLOW side of the benefits "
                "cliff, distinct from the account-principal disregard (feeds Phase 2 T-H)."}

    # ---- Sensitivity annex: one-at-a-time over locked ranges (A1 + A2, sustained) ----
    annex = {"verdict_flips": 0, "cells": 0, "flip_detail": []}
    sweeps = ([("k1", v) for v in (0.5, 1.0, 2.0)]
              + [("evict_n", v) for v in (2, 3, 4)]
              + [("apr", v) for v in (0.24, 0.36, 1.00, 4.00)]
              + [("debt_b", v) for v in (4.0, 6.0, 12.0)])
    for name in ("A1_continental_cashier", "A2_consuela_seasonal"):
        arch = archs[name]
        budget = build_budget(arch)
        for sev in (0.25, 0.50, 0.75, 1.00):
            base_m4 = None
            for (param, val) in sweeps:
                th = {param: val}
                off = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON}, th)
                on = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON,
                                             "placement": P, "div_mode": "on"}, th)
                m4 = compare(off, on)
                verdict = {k: ("A" if v == "AVOIDED" else "D" if v.startswith("DELAYED")
                               else "0") for k, v in m4.items()}
                annex["cells"] += 1
                if param == "k1" and val == 1.0 and base_m4 is None:
                    base_m4 = verdict
            # flip check: defaults vs each sweep value
            th_def_off = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON})
            th_def_on = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON,
                                                "placement": P, "div_mode": "on"})
            vd = {k: ("A" if v == "AVOIDED" else "D" if v.startswith("DELAYED") else "0")
                  for k, v in compare(th_def_off, th_def_on).items()}
            for (param, val) in sweeps:
                if (param, val) in (("k1", 1.0), ("evict_n", 3), ("apr", 0.36), ("debt_b", 6.0)):
                    continue
                off = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON},
                               {param: val})
                on = simulate(arch, budget, {"shock_mult": 1 - sev, "shock_months": HORIZON,
                                             "placement": P, "div_mode": "on"}, {param: val})
                vs = {k: ("A" if v == "AVOIDED" else "D" if v.startswith("DELAYED") else "0")
                      for k, v in compare(off, on).items()}
                for thid in set(vd) | set(vs):
                    if vd.get(thid, "-") != vs.get(thid, "-"):
                        annex["verdict_flips"] += 1
                        annex["flip_detail"].append(
                            "%s sev%d %s=%s %s: %s->%s" % (name, int(sev * 100), param,
                                                           val, thid, vd.get(thid, "-"),
                                                           vs.get(thid, "-")))
    results["sensitivity_annex"] = annex

    out = os.path.join(HERE, "econ014_phase1_results.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1)
    print("wrote", out)

    # ---- compact console summaries ----
    print("\n=== Baseline budgets (derived closure) ===")
    for name, arch in archs.items():
        b = build_budget(arch)
        print("%-28s res=%7.0f rent=%6.0f ess_nh=%6.0f contr=%4.0f disc=%6.0f" %
              (name, b["resources"], b["rent"], b["ess_nh"], b["contractual"], b["disc"]))

    print("\n=== T-A sustained: first TH-2 (missed housing) month, OFF vs ON($2,800) ===")
    for name in archs:
        row = []
        for sev in (25, 50, 75, 100):
            cell = ta[name]["sev%d_dursust" % sev]
            row.append("sev%d: %s->%s" % (sev,
                       cell["OFF"]["first"].get("TH-2", "-"),
                       cell["ON"]["first"].get("TH-2", "-")))
        print("%-28s %s" % (name, "  ".join(str(x) for x in row)))

    print("\n=== T-G cliff map: any AVOIDED verdicts (threshold-tier effects) ===")
    n_avoid = 0
    for name in archs:
        for sev in (25, 50, 75, 100):
            for pl, cell in tg[name]["sev%d" % sev]["by_placement"].items():
                for thid, v in cell["M4_vs_P0"].items():
                    if v == "AVOIDED":
                        n_avoid += 1
                        print("  %s sev%d %s %s AVOIDED" % (name, sev, pl, thid))
    if n_avoid == 0:
        print("  (none - no threshold avoided at any placement/severity in the grid)")
    print("\nSensitivity annex: %d verdict flips across %d cells" %
          (annex["verdict_flips"], annex["cells"]))
    if annex["flip_detail"]:
        for d in annex["flip_detail"][:20]:
            print("  flip:", d)


if __name__ == "__main__":
    run_all()
