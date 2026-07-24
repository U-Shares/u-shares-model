"""
t2b_pump_frontier.py  --  ECON-013 Test T2b: the alpha-sweep and PUMP-RATE FRONTIER
====================================================================================
T2 (first run) showed, at one attachment strength (alpha=1.5) and one pump rate
(1%/yr): preferential attachment devours the periphery alone; the U-Shares pump +
wrapper hold it; stopping the pump resumes erosion at the wrapper-leak timescale.

T2b maps the terrain: FOR EACH attachment strength alpha, WHAT PUMP RATE (placement
flow as a share of total wealth per year) HOLDS THE LINE?  Two thresholds:
  PARITY : bottom-40%% share at yr 120 >= the no-PA egalitarian baseline (~0.20)
           -- "U-Shares under PA does at least as well as the old economy without PA."
  PLATEAU: >= 0.35 (near the cap-bound plateau T2 found) -- "full counter."

Same minimal structural model as T2 (see t2_preferential_attachment.py docstring);
common random numbers across ALL cells; sign/ordering only; parameters illustrative.
DEC-039: directional; no magnitude established.
"""

import numpy as np

SEED = 20260722
N = 2000
YEARS = 120
DT = 0.1
STEPS = int(YEARS / DT)
SIGMA = 0.20
J = 0.05
COUPON = 0.05
RHO = 0.85
CAP = 3.0
HARDSHIP = 0.03

ALPHAS = [1.0, 1.2, 1.35, 1.5, 1.65, 1.8]
PUMPS = [0.0, 0.0025, 0.005, 0.0075, 0.010, 0.015, 0.020]   # placement, /yr of total wealth
PARITY, PLATEAU = 0.20, 0.35

rng = np.random.default_rng(SEED)
NOISE = rng.standard_normal((STEPS, N)).astype(np.float64)


def b40_at_end(alpha: float, place_rate: float) -> float:
    """Bottom-40% share of total wealth at year 120 (U-Shares ON iff place_rate>0)."""
    w = np.ones(N)
    a = np.zeros(N)
    sqdt = np.sqrt(DT)
    ushares = place_rate > 0.0
    for t in range(STEPS):
        w *= np.exp((-0.5 * SIGMA**2) * DT + SIGMA * sqdt * NOISE[t])
        W = w.sum()
        pool = J * DT * W
        w -= J * DT * w
        wa = np.power(w, alpha) if alpha != 1.0 else w.copy()
        w += pool * (wa / wa.sum())
        if ushares:
            total = W + a.sum()
            order = np.argsort(w + a)
            poor = order[: N // 10]
            room = np.maximum(CAP - a[poor], 0.0)
            add = np.minimum(room, place_rate * DT * total / max(len(poor), 1))
            coup = COUPON * DT * a
            to_acct = np.minimum(RHO * coup, np.maximum(CAP - a, 0.0))
            to_free = coup - to_acct
            cost = add.sum() + coup.sum()
            w *= max(1.0 - cost / W, 0.0)
            a[poor] += add
            a += to_acct
            w += to_free
            leak = HARDSHIP * DT * a
            a -= leak
            w += leak
    s = np.sort(w + a)
    return s[: int(0.40 * N)].sum() / s.sum()


print("=" * 80)
print("ECON-013 T2b -- ALPHA-SWEEP x PUMP-RATE FRONTIER")
print(f"N={N} yrs={YEARS} J={J} sigma={SIGMA} coupon={COUPON} rho={RHO} cap={CAP} "
      f"leak={HARDSHIP}/yr | seed={SEED} (common random numbers, all cells)")
print("=" * 80)
print("\nBottom-40% share of total wealth at year 120  (rows: alpha; cols: pump rate /yr)\n")

hdr = f"{'alpha':>6} | " + " | ".join(f"{p:>6.2%}" for p in PUMPS)
print(hdr)
print("-" * len(hdr))
grid = {}
for al in ALPHAS:
    row = []
    for p in PUMPS:
        v = b40_at_end(al, p)
        grid[(al, p)] = v
        row.append(v)
    print(f"{al:>6.2f} | " + " | ".join(f"{v:>6.3f}" for v in row))

print(f"\nTHE FRONTIER  (minimum pump rate reaching each threshold at yr {YEARS})")
print(f"{'alpha':>6} | {'no-pump b40':>11} | {'parity >=0.20':>13} | {'plateau >=0.35':>14}")
print("-" * 56)
for al in ALPHAS:
    base = grid[(al, 0.0)]
    par = next((p for p in PUMPS[1:] if grid[(al, p)] >= PARITY), None)
    pla = next((p for p in PUMPS[1:] if grid[(al, p)] >= PLATEAU), None)
    fmt = lambda x: f"{x:.2%}" if x is not None else f">{PUMPS[-1]:.2%}"
    print(f"{al:>6.2f} | {base:>11.3f} | {fmt(par):>13} | {fmt(pla):>14}")

print("\nREAD (sign/ordering): how fast does the required pump grow with attachment")
print("strength -- gently (a modest permanent flow suffices across the range) or")
print("explosively (a threshold alpha beyond which no plausible pump holds)?")
print("\nDONE. Directional; illustrative parameters; no magnitude established (DEC-039).")
