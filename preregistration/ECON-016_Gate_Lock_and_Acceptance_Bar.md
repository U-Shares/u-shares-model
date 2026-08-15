# CSDA Gate — ECON-016 State Fiscal Break-Even: APPROVED TO LOCK, with amendments (2026-08-14)

**Gating:** `06_Agent_Playbook/2026-08-02_ECON_Scoping_ECON-016_State_Fiscal_BreakEven.md`
(+ its appended Studio review of 2026-08-13). · **Pattern:** ECON-014/015 wholesale —
lock-before-extraction, acceptance bar in advance, CSDA countersign, Mike's nod, one increment.
**Condition:** the §5 ChatGPT red-team leg ("argue the break-even framing misleads — where does a
three-input formula lie?") remains **Mike's relay** and has not run. Any material red-team finding
amends this lock before countersign; if the red-team returns nothing material, this gate stands as
written. Text verification below was performed cross-document per the Studio review's own lesson.

## §1 Verified before gating (all four quotes found in the CURRENT texts, 2026-08-14)

1. White Paper §6, the adverse-#1 falsification target — line 363: "…Long-horizon state-level
   savings here are **substantial** and uncounted in an…" — live, exactly as Studio cited.
2. Ch 4 Provision 15 subsection "Why participation is tied to federal low-income programs" — line 534.
3. Ch 4 offset-vs-reduction-in-need language — line 530: "A later reduction in benefit use caused by
   increased household resources and resilience is a **reduction in need**."
4. Ch 4 measurement mandate — line 510: "The statute should require the result to be measured…"

## §2 Lock amendments (binding; Studio findings absorbed with rulings)

- **L1 — Adverse #1 restated with the mandatory-participation consequence (Studio F1: ACCEPTED).**
  The study answers "what is our net position, given that we are in," not "should we opt in."
  If break-even proves implausibly high under the mandatory design, states are conscripted into a
  losing fiscal position they cannot exit — the lock carries that consequence explicitly, and it is
  the strongest reason to publish the formula before anyone legislates from it.
- **L2 — Falsification target named (Studio F2: ACCEPTED).** Adverse #1's correction target is the
  White Paper §6 sentence quoted in §1.1, listed by name so the correction is mechanical. Path per
  scoping §4: propose → CSDA-applies. (Standing house rule: Mike's editorial authority governs any
  manuscript text; White Paper corrections follow the propose→approve path regardless.)
- **L3 — Document-qualified provision citations are a REQUIREMENT (Studio F3: ACCEPTED).** Every
  provision citation carries its document ("White Paper Provision 8," "Ch 4 Provision 15").
  **Side order (outside ECON-016):** extend `CH4_PROVISION_CONCORDANCE.md` to map the White Paper's
  eleven-provision scheme — routed to the Studio/LEG lanes as a small standalone item; three live
  numbering schemes with a two-scheme concordance is the recorded hazard.
- **L4 — Adverse #4 ADOPTED: the level-of-government mismatch (Studio F4: ACCEPTED).** The
  deliverable-2 budget-line map gains a **payer column** (state / county / municipal / mixed, by
  state-typical assignment); the headline break-even is reported at the level that actually pays the
  credit (the state), with the combined state-and-local break-even reported separately and labeled as
  a different number a legislator may not be authorized to count.
- **L5 — Offset-vs-reduction-in-need adopted as a definitional constraint on the recapture term
  (Studio §6: ACCEPTED).** The recapture formula must distinguish Δ caseload from offsets (immediate
  benefit reductions caused by receipt — not savings, the household is no better off) versus
  reductions in need (the design's intended effect). Adverse #3 is WIDENED to two pre-registered
  attribution failure classes: crediting secular trends, and crediting offsets the design exists to
  prevent. The constraint appears as a term or filter in the formula, not a footnote.
- **L6 — Review-path corrections recorded (Studio §5: ACCEPTED).** Ch 13 does not exist ("feeds
  Ch 13" means the apparatus precedes the chapter — the right order, stated so no one infers
  otherwise); there is NO live statehouse-facing surface (Post 16 shipped without its statehouse
  section) — the study fits future statehouse use, and the lock must not assume an artifact that
  does not exist. Confirming outcome lets Ch 4's measurement mandate (line 510) cite an instrument
  instead of a hope — via propose→approve only.

## §3 Lock checklist (all items check before extraction begins)

☐ Sources frozen with as-of dates: KFF/CMS FMAP tables · CMS per-enrollee Medicaid spending by
  eligibility group · SSA state SSI supplementation · HHS TANF MOE · in-inventory second-bill
  literatures · ECON-014/015 dial-grid mechanism results · Provision text (document-qualified) ·
  2025 FPL anchors.
☐ Four adverse possibilities pre-registered as amended (L1's restated #1; timing #2 with the
  year-by-year path INSIDE deliverable 1; widened #3 per L5; new #4 per L4). Publish either way.
☐ DEC-039 strict, restated: formulas, structures, response surfaces, labeled illustrations publish;
  NO state-specific savings claim; NO national aggregate; NO population weighting. M0 line drawn in
  the lock. Banned-terms + four-tier discipline carried.
☐ Document-qualified citations throughout (L3).
☐ Named text-touch points (only two, only on results, only propose→approve): White Paper §6
  "substantial" sentence; Ch 4 measurement mandate.

## §4 Acceptance bar (in advance)

- **A1 (Deliverable 1):** closed-form break-even identity with three named state inputs; acceptance
  test = an independent party (CSDA or Mike) plugs a hypothetical state's three numbers and
  reproduces the worked result BY HAND in an afternoon. Steady-state and single-budget-year
  break-evens both stated (adverse #2 lives inside D1).
- **A2 (Deliverable 2):** every budget line carries evidence class AND payer (L4); no summation.
- **A3 (Deliverable 3):** response surface across FMAP 25–50% and per-enrollee cost bands; framed as
  the formula's response, never as state predictions.
- **A4 (Deliverable 4):** worked illustration labeled hypothetical (the Mercy-County idiom at state
  scale).
- **A5:** the recapture term visibly implements L5's offset exclusion.
- **A6:** no text moved anywhere on the strength of results without the propose→approve path.
- **A7 (optional, post-acceptance only):** `state_breakeven.py` + editable `state.yml` — the
  falsify-by-scenario-file idiom; deterministic arithmetic; smallest study in the series.

## §5 Sequence from here

1. ~~Mike relays the ChatGPT red-team~~ **DONE same day — see §6.**
2. **Mike's nod.**
3. One focused increment in the ECON lane (deterministic arithmetic; no new session needed —
   the existing ECON session pattern serves).
4. Results → PL_Pending_Verification → CSDA §11 (A1's hand-reproduction is the §11 core).

## §6 Red-team absorption and re-countersign (2026-08-14, same day)

The ChatGPT external review (filed:
`06_Agent_Playbook/2026-08-14_ChatGPT_External_Review_ECON-016_RedTeam.md`; disposition
"approve to lock with amendments") answered the assigned question directly: the formula lies not in
its arithmetic but in its implicit assumptions — average cost impersonating marginal avoidable
cost, and economic saving impersonating cashable budget saving. **CSDA concurs and adopts:**

- **L7 — Closed-form limitation (ADOPTED, with one CSDA guard).** Deliverable 1's three-input
  equation is the **Simple Accounting Break-Even (under full cost realization)** — never presented
  as the complete state fiscal break-even; its six enabling assumptions (causal
  reduction-in-need; average≈marginal realization; correct financing-share matching; savings
  cashable to the paying budget; timing alignment; no material cross-program interaction) appear
  BESIDE the formula. A second **Budget-Realizable Break-Even** adjusts parametrically for
  marginal-cost realization (a budget-realization factor as a SENSITIVITY PARAMETER the state
  analyst supplies — never nationally estimated, per DEC-039), enrollment-vs-utilization channels,
  credit-redemption timing, and budget cashability. A1's hand-reproduction requirement binds
  Level 1. **CSDA guard:** Level 2 is a named, enumerable list of parametric adjustments — if a
  proposed adjustment cannot be expressed as a parameter with a stated default of
  "state supplies," it does not enter Level 2; the level must not creep into an econometric model.
- **L8 — Timing strengthening (ADOPTED).** The timing output comprises: steady-state break-even;
  annual cash-flow path; **maximum cumulative pre-break-even state deficit**; and the **first
  annual-or-biennial budget period in which cumulative recapture equals cumulative credit cost**.
  The CREDIT side carries its own timing schedule (redemption/refundability/carry-forward
  structure as legislative-design parameters) — both sides of the ledger get timed. Optional PV is
  supplementary, never a substitute for the cash-budget path.
- **L9 — Integrated-program attribution (ADOPTED).** The study evaluates the state's fiscal
  position under the integrated federal-state package; it does NOT attempt to isolate the
  independent causal effect of the 20% state credit on issuer behavior; the cost side measures the
  state's assigned share of the joint policy. **Recorded honestly:** this REJECTS the
  additionality-test line of attack CSDA's own relay cover note proposed — the reviewer's
  reasoning (parsing a mandatory integrated package into unilateral counterfactuals misstates the
  design) is accepted as correct, and it is consistent with L1's mandatory-participation framing.
- **Checklist extensions (from the memo's body, ADOPTED):**
  ☐ FMAP response surface labeled STYLIZED (the formula's response to assumptions, not a state
    prediction); several unweighted eligibility-group cases shown where practicable (no
    population weighting — DEC-039 held).
  ☐ First-bill program effects reported SEPARATELY, combined only where the accounting
    relationship is established — the no-summation caution now covers both bills.
  ☐ The recapture structure recognizes enrollment + utilization/payment + administrative channels;
    the caseload equation remains the tractable Level-1 case, not the universe.

**Acceptance-bar consequence:** A1 unchanged (binds Level 1). NEW **A8:** Level 2 ships as the
enumerated parametric checklist with every parameter named, defaulted to "state supplies," and
labeled; the two levels are never conflated in any published surface — "self-financing" claims, if
any ever publish, may only reference Level 2 conditions, stated as conditions.

**RE-COUNTERSIGNED.** The lock is complete as amended (L1–L9 + extensions). Awaiting Mike's nod;
then one increment; then §11 with A1's hand-reproduction as the core.

*— CSDA, 2026-08-14. Gate issued conditional on the red-team leg; the Studio review did the heavy
lifting, every one of its four findings survived verification against the current texts, and the
red-team then found the one thing neither of us had pressed — the closed form's silent premises —
and fixed it without sacrificing the afternoon-with-three-numbers virtue that makes the study
worth doing.*
