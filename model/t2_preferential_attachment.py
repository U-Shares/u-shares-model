"""
t2_preferential_attachment.py  --  ECON-013 Test T2 (the Mostaque stress test, headline)
=========================================================================================
CLAIM UNDER TEST (MQ5, The Last Economy): preferential attachment makes capital
re-concentration a topological law ("to ask for equality is to ask for water to
flow uphill") -- so dispersion mechanisms are futile against the network's pull.
COUNTER-CLAIM (U-Shares): dispersion is not an act but a CONTINUOUS PUMP -- the
sticky wrapper + cap hold placed principal against the gradient while the coupon
keeps pumping; remove the pump and the periphery decays only at the wrapper's
leak rate, not instantly.

DESIGN (minimal structural model -- deliberately SEPARATE from the calibrated
ECON-005 engine; tests sign/ordering only; all parameters illustrative):
  Free wealth w_i: GBM noise + a CONSERVATIVE exchange kernel with one dial:
    each step every agent contributes J*dt*w_i to a pool, redistributed
    proportional to w_i^alpha:
      alpha = 0.0  -> classic BM mean-field mixing (net drift J*(mean - w))
      alpha = 1.0  -> neutral (receipt share = wealth share; zero net)
      alpha = 1.5  -> PREFERENTIAL ATTACHMENT (super-proportional; rich gain)
    Conservation is exact (pool in = pool out).
  U-Shares layer: protected account a_i (off-market, sticky):
    placement PLACE/yr into accounts of the poorest decile (by w+a), to CAP;
    coupon c*a_i/yr, retained share rho -> a (capped), remainder -> w;
    both funded by a pro-rata levy on w (the productive economy pays);
    hardship leak h/yr of a -> w (the wrapper's imperfection, RT1).
  ARMS (common random numbers -- identical GBM draws):
    A  alpha=0.0, U-Shares OFF   (BM baseline sanity)
    B  alpha=1.5, U-Shares OFF   (his world: does the bottom collapse?)
    C  alpha=1.5, U-Shares ON    (pump + wrapper vs the gradient)
    D  alpha=1.5, ON, PUMP OFF at year 60 (re-concentration decay test)
  METRICS: bottom-40% share and top-1% share of TOTAL wealth (w+a), yearly.

DEC-039: directional; sign/ordering only; no magnitude established.
Compute conventions: single-process vectorized (seconds); fixed seed; no
parallel harness needed (below the bar).
"""

import numpy as np

SEED = 20260722
N = 2000
YEARS = 120
DT = 0.1
STEPS = int(YEARS / DT)
SIGMA = 0.20          # idiosyncratic GBM volatility
J = 0.05              # exchange intensity (BM coupling scale)
ALPHA_PA = 1.5        # preferential-attachment exponent (alpha=0 -> BM baseline)
PLACE_RATE = 0.010    # placement flow per year, as a fraction of TOTAL wealth
COUPON = 0.05         # 5% on protected balances
RHO = 0.85            # retention of coupon into the account
CAP = 3.0             # holding cap, in units of initial mean wealth (~Provision-17 spirit)
HARDSHIP = 0.03       # wrapper leak, /yr of protected balance
PUMP_OFF_YR = 60      # arm D: placement + coupon stop here; wrapper persists

rng = np.random.default_rng(SEED)
NOISE = rng.standard_normal((STEPS, N))   # common random numbers across all arms


def run(alpha, ushares_on, pump_off_year=None):
    w = np.ones(N)                        # free wealth
    a = np.zeros(N)                       # protected accounts
    sqdt = np.sqrt(DT)
    b40_idx = int(0.40 * N)
    top1_idx = int(0.99 * N)
    hist = []
    for t in range(STEPS):
        yr = t * DT
        # GBM idiosyncratic returns on free wealth
        w *= np.exp((-0.5 * SIGMA**2) * DT + SIGMA * sqdt * NOISE[t])
        # conservative exchange kernel with attachment dial
        W = w.sum()
        pool = J * DT * W
        w -= J * DT * w
        wa = np.power(w, alpha) if alpha != 1.0 else w
        w += pool * (wa / wa.sum())
        if ushares_on:
            pumping = (pump_off_year is None) or (yr < pump_off_year)
            if pumping:
                total = W + a.sum()
                # placement into the poorest decile (by total holdings), capped
                order = np.argsort(w + a)
                poor = order[: N // 10]
                room = np.maximum(CAP - a[poor], 0.0)
                budget = PLACE_RATE * DT * total
                add = np.minimum(room, budget / max(len(poor), 1))
                # coupon on all protected balances
                coup = COUPON * DT * a
                to_acct = np.minimum(RHO * coup, np.maximum(CAP - a, 0.0))
                to_free = coup - to_acct
                # fund placement + coupon by pro-rata levy on free wealth
                cost = add.sum() + coup.sum()
                w *= max(1.0 - cost / W, 0.0)
                a[poor] += add
                a += to_acct
                w += to_free
            # hardship leak runs always (the wrapper is imperfect)
            leak = HARDSHIP * DT * a
            a -= leak
            w += leak
        if t % int(1 / DT) == 0:          # yearly sample
            tot = w + a
            s = np.sort(tot)
            T = s.sum()
            hist.append((yr, s[:b40_idx].sum() / T, s[top1_idx:].sum() / T))
    return hist


def at(hist, yr):
    return min(hist, key=lambda r: abs(r[0] - yr))


print("=" * 78)
print("ECON-013 T2 -- PREFERENTIAL ATTACHMENT vs THE STICKY WRAPPER")
print(f"N={N} yrs={YEARS} J={J} sigma={SIGMA} alpha_PA={ALPHA_PA} place={PLACE_RATE}/yr "
      f"rho={RHO} cap={CAP} leak={HARDSHIP}/yr | seed={SEED} (common random numbers)")
print("=" * 78)

A = run(0.0, False)
B = run(ALPHA_PA, False)
C = run(ALPHA_PA, True)
D = run(ALPHA_PA, True, PUMP_OFF_YR)

print(f"\n{'year':>5} | {'A base b40/top1':>16} | {'B PA b40/top1':>15} | "
      f"{'C PA+US b40/top1':>17} | {'D pump-off b40':>14}")
print("-" * 78)
for yr in (20, 40, 60, 70, 80, 100, 120):
    ra, rb, rc, rd = at(A, yr), at(B, yr), at(C, yr), at(D, yr)
    print(f"{yr:>5} | {ra[1]:>7.3f}/{ra[2]:<7.3f} | {rb[1]:>6.3f}/{rb[2]:<7.3f} | "
          f"{rc[1]:>7.3f}/{rc[2]:<8.3f} | {rd[1]:>13.3f}")

# decay diagnostics for arm D
c60, d60 = at(C, PUMP_OFF_YR)[1], at(D, PUMP_OFF_YR)[1]
b_end = at(B, YEARS - 1)[1]
d_end = at(D, YEARS - 1)[1]
gain60 = d60 - at(B, PUMP_OFF_YR)[1]
gain_end = d_end - b_end
print(f"\n[D] bottom-40 share at pump-off (yr {PUMP_OFF_YR}): {d60:.3f} "
      f"(gain over PA-alone: {gain60:+.3f})")
print(f"[D] at yr {YEARS}: {d_end:.3f} (gain retained over PA-alone: {gain_end:+.3f}; "
      f"{100*gain_end/max(gain60,1e-9):.0f}% of the pump-off gain kept after "
      f"{YEARS-PUMP_OFF_YR}y, wrapper leak {HARDSHIP}/yr)")
print("\nREAD (sign/ordering only): B-vs-A = does PA concentrate (his claim)?  "
      "C-vs-B = does the pump+wrapper hold the periphery against PA?  "
      "D = when the pump stops, does the share collapse (his prediction) or decay "
      "slowly at ~the wrapper leak rate (our 'continuous pump' framing)?")
print("\nDONE. Directional; illustrative parameters; no magnitude established (DEC-039).")
