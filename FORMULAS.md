# Formulas

The load-bearing equations, stated plainly and reproducibly. Parameters are inputs to vary, not settled
values; ranges are shown. These define *method*, not *results*.

## 1. Receipts from AI growth (the gate)
Net incremental federal receipts from a GDP uplift, decomposed by where the income lands:

```
R = dGDP · [ λ·τ_L + (1−λ)·τ_K·(1−foreign)·realiz ]  +  d_emp · wage_base · GDP
```

| symbol | meaning | range used |
|---|---|---|
| dGDP | incremental GDP (uplift × baseline GDP) | uplift 1%–7% (Acemoglu→Goldman) |
| λ | marginal labor share of new GDP | 0.30 (displacement) – 0.62 (reinstatement); 0.55 ≈ measured labor share |
| τ_L | effective federal rate on incremental wages | ~0.26 (payroll + income) |
| τ_K | effective federal rate on domestic, realized capital income | ~0.15 |
| foreign | leakage of capital income to foreign owners | ~0.18 (record-high US-equity foreign ownership) |
| realiz | near-term realization fraction of capital income | ~0.60 |
| d_emp | employment-level change (the contested dial) | −2% (displacement) … +2% (reinstatement) |
| wage_base | wage-based receipts as a share of GDP | ~0.132 (payroll + wage income tax) |

*Key property:* with ~15 of ~17.8 receipts-points riding on wages, `R` goes negative under enough net
displacement — the program's binding macro risk.

## 2. Program capacity (the guardrail)
Steady-state placeable stock, when the dividend's ongoing deductibility absorbs the dedicated budget:

```
S_max = s · R / c
```

| symbol | meaning | range |
|---|---|---|
| s | share of incremental receipts dedicated to the program | 10%–100% (policy choice) |
| c | ongoing dividend-deductibility cost rate | ≈ 5% × 21% = 1.05%/yr (holder-mix dependent) |

Reach per person in a tier = `S_max / tier_population`, capped at the per-person holding cap.

## 3. Issuance break-evens
```
general issuance bar   = dividend × (1 − corporate_tax) = 5% × (1 − 21%) = 3.95%   (after-tax cost)
discount-to-poverty bar ≈ 7.58%   (the extra ~3.6 pp is the cost of the discount, not of issuing)
```
A firm gains by issuing when its after-tax return on the deployed capital exceeds the general bar.

## 4. Backstop reserve (the safety side)
One-factor Gaussian copula (Vasicek/Basel ASRF), the standard correlated-default framework:

```
conditional_default(M) = Φ( (Φ⁻¹(PD) − √ρ·M) / √(1−ρ) )
annual loss (frac of insured notional) = default_fraction × dividend × LGD
reserve ≈ Expected-Shortfall at the chosen ruin tolerance (e.g., 99.5% / 1-in-200)
```

| symbol | meaning | range |
|---|---|---|
| PD | annual probability an issuer misses the floor | 1%–5% |
| ρ | asset correlation (joint-default driver) | 0.10–0.30 (Basel corporate band) |
| M | systematic (economy) factor | N(0,1) |
| LGD | loss given default (net of recourse) | ~0.5–1.0 |

*Result orientation (directional; no magnitude asserted):* the floor-backstop reserve and the
deductibility-in-recession reserve size to the **same order of magnitude**, so one combined reserve can
meet both rather than two. The dollar figure is deliberately withheld (a held magnitude — see the claims
register and OQ-FIS-004/-010). Note too that a Treasuries-invested reserve drawn down in a claim year is
itself a form of borrowing — it is not costless safety capital.

*All parameters are illustrative inputs. No output here is an established magnitude (see M0).*
