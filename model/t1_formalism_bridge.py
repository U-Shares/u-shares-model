"""
t1_formalism_bridge.py  --  ECON-013 Test T1: reconciling r>g-as-topology with the tail index
==============================================================================================
CLAIM (MQ4, The Last Economy Ch10): Piketty's r>g is geometry -- r is the compounding
Circular Flow captured at network hubs, g the linear Gradient Flow at the periphery;
inequality deepens as r outruns g.

OUR FORMALISM (Bouchaud-Mezard family): the stationary wealth tail is Pareto with
exponent mu = 1 + J/sigma^2 -- concentration deepens as recirculation J weakens
relative to the variance of multiplicative capital returns sigma^2.

THE BRIDGE (the claim under test): these are the SAME DIAL in two languages --
  J (exchange/mixing: wages, spending, transfers)  <->  the g-side (linear recirculation)
  sigma^2 (idiosyncratic compounding of holdings)   <->  the r-side (circular-flow returns)
so his "AI pours fuel on r and collapses g" = our "sigma up, J down" = mu falling
toward 1 (maximal concentration). U-Shares in this language: the coupon+placement
RAISE J for the bottom; the holding cap TRIMS effective compounding at the top.

TEST: run the T2 kernel at alpha=0 (pure BM mixing) across J values; measure the
Hill tail exponent and the top-1% share; check the measured exponent tracks
1 + J/sigma^2 monotonically (finite-N Hill is noisy -- ordering and rough level,
not decimals). DEC-039: directional; sign/ordering only.
"""

import numpy as np

SEED = 20260722
N = 5000
YEARS = 300            # long horizon for stationarity
DT = 0.1
STEPS = int(YEARS / DT)
SIGMA = 0.20
J_GRID = [0.02, 0.04, 0.08, 0.16]
HILL_K = 250           # top-k order statistics for the Hill estimator

rng = np.random.default_rng(SEED)


def run_bm(Jv: float) -> np.ndarray:
    w = np.ones(N)
    sqdt = np.sqrt(DT)
    for _ in range(STEPS):
        w *= np.exp((-0.5 * SIGMA**2) * DT + SIGMA * sqdt * rng.standard_normal(N))
        m = w.mean()
        w += Jv * DT * (m - w)          # BM mean-field exchange (alpha=0 kernel)
        w = np.maximum(w, 1e-12)
        w *= N / w.sum()                # normalize total (removes global drift)
    return w


def hill(w: np.ndarray, k: int) -> float:
    s = np.sort(w)[::-1][: k + 1]
    return 1.0 / np.mean(np.log(s[:-1] / s[-1]))   # tail exponent (Pareto alpha)


print("=" * 74)
print("ECON-013 T1 -- THE FORMALISM BRIDGE:  measured tail vs  mu = 1 + J/sigma^2")
print(f"N={N} yrs={YEARS} sigma={SIGMA} | Hill k={HILL_K} | seed={SEED}")
print("=" * 74)
print(f"\n{'J':>6} | {'J/sig^2':>8} | {'predicted mu':>12} | {'measured Hill':>13} | "
      f"{'top-1% share':>12} | {'bottom-40%':>10}")
print("-" * 74)
for Jv in J_GRID:
    w = run_bm(Jv)
    s = np.sort(w)
    top1 = s[int(0.99 * N):].sum() / s.sum()
    b40 = s[: int(0.40 * N)].sum() / s.sum()
    print(f"{Jv:>6.2f} | {Jv/SIGMA**2:>8.2f} | {1 + Jv/SIGMA**2:>12.2f} | "
          f"{hill(w, HILL_K):>13.2f} | {top1:>12.3f} | {b40:>10.3f}")

print("""
READ: if measured Hill rises with J and sits near 1 + J/sigma^2 (ordering exact,
level approximate), the bridge holds: his r>g geometry and our tail index are one
dial. Then 'AI fuels r, collapses g' == 'sigma up, J down' == mu -> 1, and the
U-Shares levers are, formally: coupon+placement = dJ_bottom > 0; holding cap =
effective-sigma trim at the top. Wages-as-mixing-force (T2b) is the J-term
reading of his g-collapse.

DONE. Directional; sign/ordering only; no magnitude established (DEC-039).""")
