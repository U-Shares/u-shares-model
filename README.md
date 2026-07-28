# U-Shares: Open Economic Research

**Abstract.** U-Shares is a proposal to broaden capital ownership: companies voluntarily issue a class of
equity carrying a mandatory, insured 5% dividend on issue price; a transferable tax credit places those
shares into protected household accounts, poorest first; and a narrow, PBGC-style public reserve stands
behind the dividend floor. This repository publishes the economic reasoning behind that design — the
methods, formulas, directional findings, parameter ranges, and open questions — together with a claims
register stating, for every load-bearing claim, its status and the test that would disconfirm it. It is
published to invite validation, calibration, and refutation. Nothing here asserts a settled program
magnitude; the governing rule is *publish what we expect to revise; never what we'd have to retract.*

> ## What this does NOT claim
> - **No settled magnitudes.** How much ownership the program would place, what an AI boom would yield in
>   receipts, the exact size of any reserve — all deliberately withheld pending validated modeling and
>   credentialed review ([`CLAIMS.md`](CLAIMS.md) row M0).
> - **No deficit-neutrality.** The funding rule is *designed* not to worsen the deficit; whether it
>   succeeds is an open question (F2/F3), not a claim.
> - **No proven adoption.** Favorable issuance economics are measured (F5); actual firm adoption is the
>   stated open edge (F4).
> - **Contested claims are displayed, not defended away.** Three claims currently sit at `contested`
>   (F6, F7, DS1) with the challenge presented in full in their evidence files.
> - **Facts current as of 2026-07-18** (re-verified at release; fast-moving items re-checked the day
>   visibility flips).

## Reproduce a headline number in 60 seconds

```
python model/run_scenario.py --all
```

reproduces claim **F1**'s central result — net incremental federal receipts under three employment
regimes — from documented, editable parameters. To contest it, copy a scenario file in
`model/scenarios/`, change the assumptions, rerun, and submit it ([`CONTRIBUTING.md`](CONTRIBUTING.md)).
Python 3.10+ and PyYAML only.

## Five on-ramps, by the objection you're best equipped to press

| If you are a… | Start here |
|---|---|
| **Mechanism-design economist** — *does the dispersion engine actually disperse?* | [`open-questions/mechanism-design.md`](open-questions/mechanism-design.md) · evidence [`DS1`](claims/evidence/DS1.md) |
| **Fiscal / public-finance economist** — *does the funding path survive displacement, and is the reserve sized right?* | [`open-questions/fiscal.md`](open-questions/fiscal.md) · evidence [`F1`](claims/evidence/F1.md), [`F6`](claims/evidence/F6.md) |
| **Political-economy / governance scholar** — *can any public fund be made un-raidable?* | [`open-questions/political-economy.md`](open-questions/political-economy.md) · evidence [`GV1`](claims/evidence/GV1.md) |
| **Household-finance / benefits researcher** — *does the stake stick, and does it survive the benefits cliff?* | [`open-questions/household.md`](open-questions/household.md) · evidence [`RT1`](claims/evidence/RT1.md), [`F7`](claims/evidence/F7.md) |
| **Policy comparativist** — *why this and not baby bonds, ESOPs, UBI — or the enacted Trump Accounts?* | [`open-questions/adjacent-policy.md`](open-questions/adjacent-policy.md) · evidence [`CP1`](claims/evidence/CP1.md) |

## The findings, in brief (all directional; statuses govern)

1. **The funding path is employment-contingent** (F1, `open`): most federal revenue rides on wages, so
   AI-driven receipts fund the program if employment holds or grows and starve it under net displacement.
2. **The draw rule is safe in the spend year; cycle-neutrality is unproven** (F2/F3, `open`): realized-
   only + no-borrow cannot mechanically worsen the baseline, but the dividend's deductibility runs in
   recessions and a Treasuries reserve drawn down is itself borrowing.
3. **Issuance economics are favorable and cycle-robust; adoption is the open question** (F4 `supported`,
   F5 `supported`): the after-tax cost of the deductible 5% coupon (~3.95%) was cleared by 77–99% of the
   firm-weighted corporate universe across 2007–2025, including both recessions.
4. **The safety side may be one modest reserve — contested** (F6): two independent models size the floor
   backstop and the recession deductibility cost to the same order; whether that constitutes
   *affordability* on a consolidated federal balance sheet is disputed and displayed.
5. **The reach is designed poverty-first — contested at the deepest tier** (F7): without a statutory
   asset-disregard (the enacted §530A childhood exclusion is the precedent; no adult disregard exists),
   means-tested benefit cliffs can invert the ladder exactly where it claims to help first.

## How to read this repository

**Provenance notation.** Evidence files cite internal review artifacts by ID: *WS-4* is the five-persona adversarial panel review (2026-07); *KS-n* are its numbered kill-shot findings; *ECON-nnn / Increment* memos are the internal work orders behind each derivation. They are dated provenance, not public documents.

[`CLAIMS.md`](CLAIMS.md) — the register; ground truth for what is and isn't claimed ·
[`CALL_FOR_PAPERS.md`](CALL_FOR_PAPERS.md) — the open invitation and what counts as falsification ·
[`FORMULAS.md`](FORMULAS.md) — the load-bearing equations · [`CODE_MANIFEST.md`](CODE_MANIFEST.md) — the
models and how to reproduce or contest the runs · [`open-questions/`](open-questions/) — 33 questions
across five reviewer perspectives · [`GOVERNANCE.md`](GOVERNANCE.md) · [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Citing this work

```bibtex
@software{blake_ushares_2026,
  author     = {Blake, Mike},
  title      = {U-Shares: Open Economic Research},
  year       = {2026},
  url        = {https://github.com/U-Shares/u-shares-model},
  note       = {Directional findings only; no program magnitude asserted.
                Cite the tagged release you examined.}
}
```

Machine-readable citation in [`CITATION.cff`](CITATION.cff); cite the specific tagged release you
examined so critique targets a fixed version. License: MIT (code) / CC-BY 4.0 (prose, figures) — see
[`LICENSE.md`](LICENSE.md).

---

*We invite economists, tax and public-finance scholars, and governance researchers to validate,
calibrate, or refute this work. Disagreement, clearly argued, is the most useful contribution you can
make — and it is credited (see the ladder in `CONTRIBUTING.md`).*
