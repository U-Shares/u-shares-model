"""
t2c_wrapper_breach.py  --  ECON-013 Test T2c: attachment reaches the accounts
==============================================================================
T2b's flat pump frontier rested on ONE assumption: the protected account is
OFF-MARKET -- attachment dynamics cannot touch it. T2c breaks that assumption
two ways and measures the damage:

  MARKET PERMEABILITY (pi): a fraction pi of protected balances participates in
    the attachment exchange -- accounts contribute pi-weighted to the pool
    (deducted from the account) while receipts land in free wealth. Models legal/
    product erosion that lets account value leak onto the open battlefield.
  FEE RAKE (rake): a skim of rake/yr on protected balances routed to the top
    decile's free wealth. Models the realistic American breach -- not
    confiscation but fee capture / financialization (lawful erosion, GV1's
    domain).

Setting: the T2 arm-C configuration (alpha=1.5 attachment, pump 1%/yr, coupon 5%,
rho=0.85, cap, leak 3%/yr), common random numbers. Metric: bottom-40% share of
total wealth at year 120. Then a compensation probe: at the worst breach cells,
can a BIGGER pump restore parity (>=0.20)?

T2c measures the MECHANICS of a breach, not its PROBABILITY -- the probability is
a legal/political question (GV1). DEC-039: directional; sign/ordering only.
"""

import numpy as np

SEED = 20260722
N = 2000
YEARS = 120
DT = 0.1
STEPS = int(YEARS / DT)
SIGMA = 0.20
J = 0.05
ALPHA = 1.5
COUPON = 0.05
RHO = 0.85
CAP = 3.0
HARDSHIP = 0.03

rng = np.random.default_rng(SEED)
NOISE = rng.standard_normal((STEPS, N)).astype(np.float64)


def b40(place_rate, pi_mkt=0.0, rake=0.0):
    w = np.ones(N)
    a = np.zeros(N)
    sqdt = np.sqrt(DT)
    for t in range(STEPS):
        w *= np.exp((-0.5 * SIGMA**2) * DT + SIGMA * sqdt * NOISE[t])
        # attachment exchange over free wealth PLUS the permeable slice of accounts
        base = w + pi_mkt * a
        pool = J * DT * base.sum()
        w -= J * DT * w
        a_contrib = J * DT * pi_mkt * a
        a -= a_contrib                                  # account value leaks to the field
        ba = np.power(base, ALPHA)
        w += pool * (ba / ba.sum())                     # receipts land in FREE wealth
        # U-Shares machinery (pump always on in T2c)
        total = w.sum() + a.sum()
        order = np.argsort(w + a)
        poor = order[: N // 10]
        room = np.maximum(CAP - a[poor], 0.0)
        add = np.minimum(room, place_rate * DT * total / max(len(poor), 1))
        coup = COUPON * DT * a
        to_acct = np.minimum(RHO * coup, np.maximum(CAP - a, 0.0))
        cost = add.sum() + coup.sum()
        w *= max(1.0 - cost / w.sum(), 0.0)
        a[poor] += add
        a += to_acct
        w += coup - to_acct
        # fee rake: skim accounts, route to the top decile's free wealth
        if rake > 0.0:
            skim = rake * DT * a
            a -= skim
            rich = order[-N // 10:]
            w[rich] += skim.sum() / len(rich)
        # hardship leak (the wrapper's honest imperfection)
        leak = HARDSHIP * DT * a
        a -= leak
        w += leak
    s = np.sort(w + a)
    return s[: int(0.40 * N)].sum() / s.sum()


print("=" * 76)
print("ECON-013 T2c -- WRAPPER BREACH: attachment reaches the accounts")
print(f"alpha={ALPHA} pump=1%/yr coupon={COUPON} rho={RHO} cap={CAP} leak={HARDSHIP}"
      f" | N={N} yrs={YEARS} seed={SEED} (common random numbers)")
print("(T2 arm-C intact-wrapper reference at these settings: b40 ~ 0.400)")
print("=" * 76)

print("\n[1] MARKET PERMEABILITY (pi) -- accounts join the attachment exchange")
print(f"{'pi':>6} | {'b40 @ yr120':>11}")
print("-" * 22)
for pi in (0.0, 0.10, 0.25, 0.50, 1.00):
    print(f"{pi:>6.2f} | {b40(0.010, pi_mkt=pi):>11.3f}")

print("\n[2] FEE RAKE -- skim on accounts routed to the top decile")
print(f"{'rake/yr':>8} | {'b40 @ yr120':>11}")
print("-" * 24)
for rk in (0.0, 0.0025, 0.005, 0.010, 0.020):
    print(f"{rk:>8.2%} | {b40(0.010, rake=rk):>11.3f}")

print("\n[3] COMPENSATION PROBE -- can a bigger pump buy the share back?")
print("    worst cells above, pump raised 1% -> 2% -> 3%/yr")
for label, kw in (("pi=0.50", dict(pi_mkt=0.50)), ("pi=1.00", dict(pi_mkt=1.00)),
                  ("rake=1%/yr", dict(rake=0.010)), ("rake=2%/yr", dict(rake=0.020))):
    row = " | ".join(f"pump {p:.0%}: {b40(p, **kw):.3f}" for p in (0.01, 0.02, 0.03))
    print(f"  {label:>11} -> {row}")

print("""
READ (sign/ordering): [1]-[2] = how fast does the periphery's share fall as the
wrapper's walls become permeable?  [3] = is a breach PUMPABLE (more placement
restores the line) or STRUCTURAL (no plausible pump compensates)? If structural,
the wrapper's legal integrity -- not the pump size -- is the load-bearing member,
and the whole defense budget belongs on the walls (GV1).

DONE. Directional; illustrative parameters; no magnitude established (DEC-039).""")
