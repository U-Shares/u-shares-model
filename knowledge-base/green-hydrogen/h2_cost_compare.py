"""Back-of-envelope hydrogen cost comparison: photocatalytic panels vs PV-electrolysis vs SMR,
expressed in $/kg H2 and in oil- and gas-equivalent energy prices.

Every number is an editable, sourced-or-stated assumption (see the report beside this file).
Run:  python knowledge-base/green-hydrogen/h2_cost_compare.py
Standard library only.
"""

# --- Physical constants -------------------------------------------------------------------
H2_LHV_MMBTU_PER_KG = 0.1137   # 120 MJ/kg lower heating value
H2_DG_KWH_PER_KG = 32.9        # Gibbs free energy (237 kJ/mol); the basis of the STH definition
OIL_MMBTU_PER_BBL = 5.8        # crude oil, approx.


def crf(rate, years):
    """Capital recovery factor."""
    return rate * (1 + rate) ** years / ((1 + rate) ** years - 1)


# --- 1. Photocatalytic panel (particulate photocatalyst sheets in water) ---------------------
def lcoh_photocatalytic(sth, panel_cost_m2=100.0, sep_cost_per_kg=0.50, insolation=2000.0,
                        life=10, rate=0.08, om_frac=0.03):
    """$/kg. sth = solar-to-hydrogen fraction; insolation in kWh/m2/yr (US Southwest ~2000-2300).
    sep_cost_per_kg covers H2/O2 separation, compression and safety (panels emit a mixed gas)."""
    kg_per_m2_yr = insolation * sth / H2_DG_KWH_PER_KG
    annual_cost = panel_cost_m2 * (crf(rate, life) + om_frac)
    return annual_cost / kg_per_m2_yr + sep_cost_per_kg


# --- 2. PV + electrolysis ------------------------------------------------------------------------
def lcoh_pv_electrolysis(elec_usd_mwh=35.0, electrolyzer_usd_kw=1500.0, cap_factor=0.30,
                         kwh_per_kg=52.0, life=20, rate=0.08, om_frac=0.03, other_per_kg=0.30):
    """$/kg. Electrolyzer sized to PV output (capacity factor = solar CF when directly coupled)."""
    kg_per_kw_yr = 8760 * cap_factor / kwh_per_kg
    capex = electrolyzer_usd_kw * (crf(rate, life) + om_frac) / kg_per_kw_yr
    power = elec_usd_mwh / 1000 * kwh_per_kg
    return capex + power + other_per_kg


# --- 3. Steam methane reforming (grey) and with CCS (blue) ---------------------------------------
def lcoh_smr(gas_usd_mmbtu=3.0, mmbtu_per_kg=0.165, non_fuel_per_kg=0.60,
             co2_kg_per_kg=9.0, carbon_usd_t=0.0, ccs=False):
    """$/kg. ccs=True: ~90% capture, +$0.45/kg cost, +8% gas use (approximations)."""
    gas = mmbtu_per_kg * (1.08 if ccs else 1.0)
    extra = 0.45 if ccs else 0.0
    emitted = co2_kg_per_kg * (0.10 if ccs else 1.0)
    return gas * gas_usd_mmbtu + non_fuel_per_kg + extra + emitted / 1000 * carbon_usd_t


def oil_equiv_usd_bbl(usd_per_kg):
    return usd_per_kg / H2_LHV_MMBTU_PER_KG * OIL_MMBTU_PER_BBL


def gas_equiv_usd_mmbtu(usd_per_kg):
    return usd_per_kg / H2_LHV_MMBTU_PER_KG


def row(label, usd_kg):
    print(f"  {label:<58} ${usd_kg:6.2f}/kg   ≈ ${gas_equiv_usd_mmbtu(usd_kg):6.1f}/MMBtu"
          f"   ≈ ${oil_equiv_usd_bbl(usd_kg):5.0f}/bbl-oil-equiv")


if __name__ == "__main__":
    print("\nA. Photocatalytic panels — what STH is needed? ($100/m2, 10-yr life, 2000 kWh/m2/yr)")
    for sth in (0.0065, 0.01, 0.02, 0.05, 0.10, 0.15):
        row(f"STH {sth*100:5.2f}%", lcoh_photocatalytic(sth))
    print("\n   Same, but $50/m2 and 20-yr life (optimistic manufacturing + durability)")
    for sth in (0.01, 0.05, 0.10):
        row(f"STH {sth*100:5.2f}%", lcoh_photocatalytic(sth, panel_cost_m2=50, life=20))

    print("\nB. PV + electrolysis (2026)")
    row("Western capex $1,500/kW, $35/MWh solar, CF 30%", lcoh_pv_electrolysis())
    row("Chinese capex $600/kW,  $25/MWh solar, CF 30%",
        lcoh_pv_electrolysis(elec_usd_mwh=25, electrolyzer_usd_kw=600))
    row("Wind+solar hybrid, $30/MWh, CF 55%, $1,200/kW",
        lcoh_pv_electrolysis(elec_usd_mwh=30, electrolyzer_usd_kw=1200, cap_factor=0.55))

    print("\nC. Natural-gas hydrogen")
    for g in (3.0, 6.0, 12.0):
        row(f"Grey SMR, gas ${g:.0f}/MMBtu, no carbon price", lcoh_smr(gas_usd_mmbtu=g))
    row("Grey SMR, gas $3, carbon $100/t", lcoh_smr(carbon_usd_t=100))
    row("Blue SMR+CCS, gas $3, carbon $100/t", lcoh_smr(carbon_usd_t=100, ccs=True))

    print("\nD. Reference fuels (energy-only parity, LHV basis)")
    for bbl in (60, 100, 120):
        kg = bbl / OIL_MMBTU_PER_BBL * H2_LHV_MMBTU_PER_KG
        print(f"  Crude at ${bbl}/bbl is energy-equivalent to H2 at ${kg:4.2f}/kg")
    for g in (3.0, 12.0):
        print(f"  Gas at ${g:.0f}/MMBtu is energy-equivalent to H2 at ${g*H2_LHV_MMBTU_PER_KG:4.2f}/kg")
    print()
