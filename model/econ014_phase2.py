"""ECON-014 Phase 2 - T-D (wrapper test), T-H (benefits dials), T-F (recovery participation).

Governed by ECON-014_Preregistration_Lock_v1.md + v1.1 addendum (both CSDA-countersigned).
Reuses household_stress.py budget construction (Phase-1-accepted). Deterministic.

Extracted leakage anchors (v1.1 section 3 named statistics, extracted 2026-07-26):
  - 401(k) cashout at job separation: 41.4% of departing employees (162,360 employees /
    28 firms, 2014-16; UBC Sauder + Leeds, HBR Nov 2022); 85% of those drain fully.
  - Hardship withdrawals: 6% of participants in 2025 (Vanguard How America Saves 2025;
    5% 2024, 1.7% 2020; >1/3 to avoid foreclosure/eviction).
  - MPC out of transfers, first 3 months, nondurables: 0.1-0.5, low-liquidity households
    at the high end (NBER w27693 family; CEPR/JPMC liquidity gradient).
  - ABLE withdrawal patterns: thin public statistics -> SUBSTITUTION RULE: arm-4
    discretionary leakage proxied by the 401(k) hardship-incidence range, documented.
Mapping to annual erosion rates of the REMAINING transfer-derived balance (documented
derivation, three-point sweeps per the addendum):
  arm1 cash lam: {low 0.40, central 0.70, high 0.90}/yr   (MPC range annualized)
  arm2 stock lam: {low 0.06, central 0.12, high 0.25}/yr  (41.4% per ~4yr job cycle
       ~= 0.10/yr + 6%/yr hardship incidence; bracketed)
  arm4 wrapper+access lam: {low 0.00, central 0.02, high 0.06}/yr (hardship-incidence
       proxy per substitution rule)
Program parameters (v1.1 section 2, extracted): SNAP federal-default asset limit FY2026
$3,000 ($4,500 elderly/disabled); BBCE variant = no asset test; SSI $2,000/$994 FBR/$20
general exclusion/$1:$1 unearned (statute); HOTMA $100,000 statutory base (indexed;
never binds at tested placements; substitution rule documented).

T-D distress path (engine structure, documented): a -50% 12-month labor shock starting
month 2, recurring every 60 months (months 2-13, 62-73, 122-133, 182-193), on the
archetype's Phase-1 budget. The first crisis is EARLY by design: the stickiness-paradox
question lives at the 3- and 12-month horizons, so acute distress must be inside them.
Horizons = snapshot months {3, 12, 60, 120, 240}.

MID-RUN FIX LOG (dated; CSDA acceptance condition - all fixes made 2026-07-26, BEFORE any
Phase-2 result was reported; the reported results are from the post-fix engine only):
  FIX-1 (2026-07-26): T-D distress path originally started the first crisis at month 13,
    leaving the 3- and 12-month horizons free of distress - the stickiness-paradox
    question was untestable at exactly the horizons it lives at. First crisis moved to
    months 2-13 (this made the ADVERSE finding observable; it did not favor the design).
  FIX-2 (2026-07-26): arm 1's cash pot was initialized but never drawn in the deficit
    waterfall - the cash arm entered high-cost borrowing with money in hand (TH-3 month 4
    artifact). Added the liquid -> cash-pot -> borrowing draw order. This STRENGTHENED
    the wrapper's competitor, as pre-registered fairness requires.
  FIX-3 (2026-07-26): three T-F/arm-4 corrections in one pass: (a) the permanent-transfer
    arm was injected as unlevied free wealth, violating the pre-registered equal-cost
    identity - now prepays the identical levy stream; (b) arm-4 floor-base reduction
    changed from a min() approximation to share-proportional (dividends ride remaining
    original-issue shares); (c) the fixed-cohort diagnostic added alongside the
    registered bottom-40 share (disclosed to CSDA, ratified as a labeled diagnostic).
Asset growth r = 5%/yr (scenario assumption, both stock and U-Shares underlying);
unprotected stock yields 2%/yr market dividend (spendable); U-Shares pays the 5% floor
on ORIGINAL issue price. Arm ordering under deficit (documented): liquid -> [arm 2:
sell stock (TH-8) | arm 4: hardship withdrawal] -> high-cost borrowing (TH-3) -> unpaid
cascade (as Phase 1).
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from household_stress import load_archetypes, build_budget, TH_DEFAULTS  # noqa: E402

R_ANNUAL = 0.05
MKT_YIELD = 0.02
FLOOR = 0.05
P_DEFAULT = 2800.0
CREDIT_SHARE = 0.35
HORIZONS = [3, 12, 60, 120, 240]
LAM = {"arm1": {"low": 0.40, "central": 0.70, "high": 0.90},
       "arm2": {"low": 0.06, "central": 0.12, "high": 0.25},
       "arm4": {"low": 0.00, "central": 0.02, "high": 0.06}}


def shock_mult_td(t):
    """-50% labor for months 2-13 of each 60-month cycle (early first crisis)."""
    c = ((t - 1) % 60) + 1
    return 0.5 if 2 <= c <= 13 else 1.0


def run_td_arm(arch, budget, arm, value, lam_annual, months=240):
    """One T-D arm. value = inception asset value for this arm.
    arm: 1 cash, 2 liquid stock, 3 wrapper no-access, 4 wrapper + hardship access."""
    mrate = TH_DEFAULTS["apr"] / 12.0
    g = (1.0 + R_ANNUAL) ** (1.0 / 12.0)
    lam_m = 1.0 - (1.0 - lam_annual) ** (1.0 / 12.0)
    liquid = arch["liquid_start"]["value"]
    debt = arch["debt_start"]["value"]
    cap = arch.get("borrow_cap_override",
                   TH_DEFAULTS["debt_b"] * budget["resources"])
    pot = value if arm in (1, 2) else 0.0        # accessible transfer-derived balance
    acct = value if arm in (3, 4) else 0.0       # protected account (grows; inaccessible in 3)
    orig = value                                  # original issue price (floor base)
    first, events = {}, []
    miss_h, ess_un = 0, 0
    snaps = {}

    def fire(thid, m):
        if thid not in first:
            first[thid] = m
            events.append((m, thid))

    for t in range(1, months + 1):
        labor = budget["labor"] * shock_mult_td(t)
        income = labor + budget["transfers"]
        if arm == 2:
            income += pot * (MKT_YIELD / 12.0)            # market dividend, spendable
        if arm in (3, 4):
            income += FLOOR * orig / 12.0                 # the floor, on original price
        debt_min = debt * mrate
        obligations = budget["ess_nh"] + budget["rent"] + budget["contractual"] + debt_min
        if income >= obligations:
            disc_paid = min(budget["disc"], income - obligations)
            surplus = income - obligations - disc_paid
            pay = min(debt, surplus)
            debt -= pay
            liquid += surplus - pay
            miss_h, ess_un = 0, 0
        else:
            rem = obligations - income
            use = min(liquid, rem)
            liquid -= use
            rem -= use
            if rem > 1e-9 and arm == 1 and pot > 1e-9:    # cash used directly (no event)
                s = min(pot, rem)
                pot -= s
                rem -= s
            if rem > 1e-9 and arm == 2 and pot > 1e-9:    # forced sale (TH-8)
                s = min(pot, rem)
                pot -= s
                rem -= s
                fire("TH-8", t)
            if rem > 1e-9 and arm == 4 and acct > 1e-9:   # hardship withdrawal
                wd = min(acct, rem)
                orig *= (acct - wd) / acct                 # share-proportional floor-base fall
                acct -= wd
                rem -= wd
                fire("TH-8", t)                            # access event recorded under TH-8
            if rem > 1e-9 and arm == 3 and acct > 1e-9 and "TH8_counterfactual" not in first:
                first["TH8_counterfactual"] = t            # would-have-raided month (lock TH-8)
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
                up_d = min(debt_min, rem)
                debt += up_d
                rem -= up_d
                if rem > 1e-9:
                    up_h = min(budget["rent"], rem)
                    rem -= up_h
                    if up_h > 1e-9:
                        fire("TH-2", t)
                        miss_h += 1
                        if miss_h >= TH_DEFAULTS["evict_n"]:
                            fire("TH-5", t)
                    if rem > 1e-9:
                        ess_un += 1
                        if ess_un >= TH_DEFAULTS["util_grace"]:
                            fire("TH-4", t)
                    else:
                        ess_un = 0
                else:
                    miss_h, ess_un = 0, 0
            else:
                miss_h, ess_un = 0, 0
        # growth + behavioral leakage on the asset
        if arm == 2:
            pot *= g
            pot *= (1.0 - lam_m)                          # discretionary liquidation, consumed
        elif arm == 1:
            pot *= (1.0 - lam_m)                          # cash spent down (non-essential)
        elif arm in (3, 4):
            acct *= g
            if arm == 4 and lam_m > 0 and acct > 0:
                wd = acct * lam_m                          # discretionary hardship-rule leakage
                orig *= (acct - wd) / acct                 # share-proportional
                acct -= wd
        if t in HORIZONS:
            snaps[t] = {"asset": round(pot + acct, 2), "debt": round(debt, 2),
                        "liquid": round(liquid, 2),
                        "th_so_far": {k: v for k, v in first.items() if v <= t}}
    return {"first": first, "snapshots": snaps}


def run_td(archs):
    out = {}
    for name in archs:
        arch = archs[name]
        budget = build_budget(arch)
        out[name] = {}
        for ident, vals in (("I1_equal_public_cost",
                             {"arm1": CREDIT_SHARE * P_DEFAULT, "arm2": CREDIT_SHARE * P_DEFAULT,
                              "arm3": P_DEFAULT, "arm4": P_DEFAULT}),
                            ("I2_equal_recipient_value",
                             {"arm1": P_DEFAULT, "arm2": P_DEFAULT,
                              "arm3": P_DEFAULT, "arm4": P_DEFAULT})):
            out[name][ident] = {}
            for lev in ("low", "central", "high"):
                cells = {}
                cells["arm1"] = run_td_arm(arch, budget, 1, vals["arm1"], LAM["arm1"][lev])
                cells["arm2"] = run_td_arm(arch, budget, 2, vals["arm2"], LAM["arm2"][lev])
                cells["arm3"] = run_td_arm(arch, budget, 3, vals["arm3"], 0.0)
                cells["arm4"] = run_td_arm(arch, budget, 4, vals["arm4"], LAM["arm4"][lev])
                out[name][ident][lev] = cells
    return out


# ---------------- T-H: benefits dials ----------------

def run_th(archs):
    """Deterministic benefit-rule tracker, 60-month horizon."""
    SSI_LIMIT, SSI_EXCL = 2000.0, 20.0
    SNAP_ASSET = 3000.0
    results = {}
    grid_archs = {"A1_continental_cashier": "SNAP_default_and_BBCE",
                  "A2_consuela_seasonal": "SNAP_plus_voucher",
                  "A3_daniel_ssi_household": "SSI_Medicaid"}
    for name, prog in grid_archs.items():
        arch = archs[name]
        liquid0 = arch["liquid_start"]["value"]
        results[name] = {"program_frame": prog, "cells": {}}
        for P in (2800.0, 10000.0):
            div_m = FLOOR * P / 12.0
            for S in (0, 1, 2):
                for F in (0, 1):
                    for beh in ("save", "consume"):
                        for scen in ("baseline", "shock50"):
                            key = "P%d_S%d_F%d_%s_%s" % (int(P), S, F, beh, scen)
                            div_sav = 0.0
                            elig_loss = None
                            ben_red = None
                            th6 = None
                            for t in range(1, 61):
                                if beh == "save" and scen == "baseline":
                                    div_sav += div_m
                                # under shock, dividend is consumed by deficits; no accumulation
                                liquid = liquid0 if scen == "baseline" else max(0.0, liquid0 - 400.0 * t)
                                countable = liquid + div_sav
                                if S == 0:
                                    countable += P
                                if S == 2:
                                    countable -= div_sav
                                if prog == "SSI_Medicaid":
                                    if F == 0 and div_m > SSI_EXCL and ben_red is None:
                                        ben_red = t
                                    if countable > SSI_LIMIT and elig_loss is None:
                                        elig_loss = t   # SSI suspended; Medicaid (linked pathway) same month
                                        th6 = t
                                else:
                                    if F == 0 and ben_red is None:
                                        ben_red = t     # SNAP net-income rule: benefit falls ~30 cents/$ from month 1
                                    if countable > SNAP_ASSET and elig_loss is None:
                                        elig_loss = t   # federal-default variant only; BBCE never (labeled)
                                        th6 = t
                            results[name]["cells"][key] = {
                                "eligibility_loss_month_default_variant": elig_loss,
                                "benefit_reduction_month_F0": ben_red,
                                "TH6_month": th6,
                                "note_BBCE": "no asset test - eligibility loss n/a" if prog != "SSI_Medicaid" else None}
    return results


# ---------------- T-F: recovery participation (T2-harness-derived kernel) ----------------

def run_tf():
    import numpy as np
    SEED = 20260726
    N, YEARS, DT = 2000, 10, 0.1
    STEPS = int(YEARS / DT)
    SIGMA, J, ALPHA = 0.20, 0.05, 1.5
    PLACE, COUPON, RHO, CAP, LEAK = 0.010, 0.05, 0.85, 3.0, 0.03
    CRASH_END, CRASH_W, J_CRASH, BOOM_MU = 2.0, 0.6, 0.4, 0.04
    rng = np.random.default_rng(SEED)
    NOISE = rng.standard_normal((STEPS, N))

    def kernel(mode, cost_stream=None):
        w = np.ones(N)
        # cohort: the t=0 poorest decile by pre-noise wealth is degenerate (all equal),
        # so fix the cohort as the poorest decile after the first noise step in the
        # NO-INTERVENTION dynamics -- identical across arms (common random numbers).
        w_probe = np.exp((-0.5 * SIGMA ** 2) * DT + SIGMA * (DT ** 0.5) * NOISE[0])
        cohort = np.argsort(w_probe)[: N // 10]               # fixed membership, all arms
        a = np.zeros(N)
        sqdt = DT ** 0.5
        b40 = int(0.40 * N)
        hist, costs = [], []
        if mode == "P" and cost_stream is not None:
            total_cost = sum(cost_stream)
            W0 = w.sum()
            w *= max(1.0 - total_cost / W0, 0.0)              # SAME levy, prepaid once
            w[cohort] += total_cost / max(len(cohort), 1)
        for t in range(STEPS):
            yr = t * DT
            in_crash = yr < CRASH_END
            if t == 0 and mode != "pre":
                w *= CRASH_W                                   # the crash hits free wealth
            mu = 0.0 if in_crash else BOOM_MU
            Jt = J * (J_CRASH if in_crash else 1.0)            # severed wage-mixing (T2b)
            w *= np.exp((mu - 0.5 * SIGMA ** 2) * DT + SIGMA * sqdt * NOISE[t])
            W = w.sum()
            pool = Jt * DT * W
            w -= Jt * DT * w
            wa = np.power(w, ALPHA)
            w += pool * (wa / wa.sum())
            cost = 0.0
            if mode == "U":
                total = W + a.sum()
                order = np.argsort(w + a)
                poor = order[: N // 10]
                room = np.maximum(CAP - a[poor], 0.0)
                budget = PLACE * DT * total
                add = np.minimum(room, budget / max(len(poor), 1))
                coup = COUPON * DT * a                         # floor: coupon regardless of crash
                to_a = np.minimum(RHO * coup, np.maximum(CAP - a, 0.0))
                cost = add.sum() + coup.sum()
                w *= max(1.0 - cost / W, 0.0)
                a[poor] += add
                a += to_a
                w += coup - to_a
                leak = LEAK * DT * a
                a -= leak
                w += leak
            elif mode == "R" and cost_stream is not None:
                cost = cost_stream[t]
                order = np.argsort(w)
                poor = order[: N // 10]
                w *= max(1.0 - cost / W, 0.0)
                w[poor] += cost / max(len(poor), 1)            # spendable flow, no principal
            costs.append(cost)
            if t % int(1 / DT) == 0:
                tot = w + a
                srt = np.sort(tot)
                hist.append((round(yr, 1), srt[:b40].sum() / srt.sum(),
                             tot[cohort].sum() / tot.sum()))
        return hist, costs

    u_hist, u_costs = kernel("U")
    r_hist, _ = kernel("R", u_costs)                           # same levy stream, as flow
    p_hist, _ = kernel("P", u_costs)                           # same total, prepaid once
    n_hist, _ = kernel("none")

    def at(h, yr):
        r = min(h, key=lambda x: abs(x[0] - yr))
        return r[1], r[2]
    out = {}
    for yr in (0.5, 1.0, 2.0, 5.0, 10.0):
        row = {}
        for label, h in (("none", n_hist), ("benefit_flow", r_hist),
                         ("permanent_transfer", p_hist), ("ushare_owner", u_hist)):
            b40s, cohs = at(h, yr)
            row[label] = {"b40_share": round(b40s, 4), "cohort_share": round(cohs, 4)}
        out["yr%.1f" % yr] = row
    return out


def main():
    archs, _ = load_archetypes()
    results = {"_locks": ["ECON-014_Preregistration_Lock_v1.md",
                          "ECON-014_Preregistration_Lock_v1.1_TH_Addendum.md"],
               "_date": "2026-07-26"}
    results["T-D"] = run_td(archs)
    results["T-H"] = run_th(archs)
    results["T-F"] = run_tf()
    out = os.path.join(HERE, "econ014_phase2_results.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1)
    print("wrote", out)

    # ---- console summaries ----
    print("\n=== T-H: A3 (SSI) eligibility-loss / TH-6 months (save behavior, baseline) ===")
    for key, c in results["T-H"]["A3_daniel_ssi_household"]["cells"].items():
        if "_save_baseline" in key:
            print("  %-24s elig_loss=%-5s ben_red(F0)=%-5s TH6=%s" %
                  (key, c["eligibility_loss_month_default_variant"],
                   c["benefit_reduction_month_F0"], c["TH6_month"]))
    print("\n=== T-D: A1, I2 equal recipient value, central leakage - threshold firsts ===")
    a1 = results["T-D"]["A1_continental_cashier"]["I2_equal_recipient_value"]["central"]
    for arm in ("arm1", "arm2", "arm3", "arm4"):
        print("  %s first=%s asset@240=%s" % (arm, a1[arm]["first"],
              a1[arm]["snapshots"][240]["asset"]))
    print("\n=== T-D: A1 I2 central - asset remaining by horizon (ordering only) ===")
    for h in HORIZONS:
        row = {arm: a1[arm]["snapshots"][h]["asset"] for arm in a1}
        order = sorted(row, key=lambda k: -row[k])
        print("  m%-4d ranking: %s" % (h, " > ".join(order)))
    print("\n=== T-F: crash->boom -- b40 quantile share / fixed-cohort share ===")
    for yr, row in results["T-F"].items():
        print("  %-7s " % yr + "  ".join(
            "%s=%.3f/%.3f" % (k, v["b40_share"], v["cohort_share"])
            for k, v in row.items()))


if __name__ == "__main__":
    main()
