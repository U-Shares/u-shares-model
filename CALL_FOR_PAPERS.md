# Call for Papers — Falsify or Extend U-Shares

We have published the reasoning, the formulas, the models, and a claims register that states, for every claim, **exactly what would disconfirm it.** This is an open call to test that work. We are not asking you to agree — we are asking you to **falsify or extend** it.

## Why a call, not a claim

A call for papers **asserts no magnitude; it invites others to establish them.** It is the honest form of the limits we already publish: where our own modeling is directional, we say so; where a number would require validation we do not yet have, we hold it (register row **M0**) and ask you to supply or overturn it. The call *is* the honesty mechanism — not a preliminary to it.

## What counts as falsification (stated *before* you submit)

So adjudication is never ad-hoc, a **credible falsification** is one of exactly three things:

1. **A scenario run** — on documented data and assumptions — that flips a registered claim's stated *disconfirming test* (submit the scenario file; see [`model/scenarios/`](model/scenarios/)).
2. **An identified error** in a derivation or in the model code, reproducible from the repo.
3. **Published empirical evidence** that directly contradicts a claim's evidence base.

Everything else — disagreement with the framing, values objections, alternative proposals — is **welcome as an *extension* or *commentary*** and routed to the extension path, not the falsification path. It is not a lesser contribution; it is a different one.

**Adjudication.** The maintainer decides, against the published criteria in [`GOVERNANCE.md`](GOVERNANCE.md). A credible-but-disputed challenge is parked publicly at **`contested`** — the honest middle state. Nobody has to "win" for the disagreement to be visible on the record.

## How to contribute (small, templated units — you never edit the register)

| You have… | Submit… | Template |
|---|---|---|
| A scenario that flips a disconfirming test | a scenario file + a Falsification Report | `falsification-report.yml` |
| A challenge to a parameter or assumption | an Assumption Challenge | `assumption-challenge.yml` |
| A new question, dataset, or method | an Extension Proposal | `extension-proposal.yml` |
| Intent to work an open question | a Question Claim (so it isn't double-worked) | `question-claim.yml` |

Only the maintainer updates claim statuses (rubric guardrail 1). Your unit of contribution stays small, templated, and machine-checked before human review.

## Credit ladder (pre-stated)

1. **Named** in the claims register or the replications registry for a credible contribution.
2. **A replication-registry entry** ([`replications/`](replications/)) recording who tested what, and the outcome.
3. **Co-authorship** on the revised white paper when your work changes a claim's status or evidence base.

## The open questions

The full agenda lives in [`open-questions/`](open-questions/), organized by five adversarial perspectives — [mechanism-design](open-questions/mechanism-design.md) (OQ-MD), [fiscal](open-questions/fiscal.md) (OQ-FIS), [political-economy](open-questions/political-economy.md) (OQ-PE), [household](open-questions/household.md) (OQ-HH), [adjacent-policy](open-questions/adjacent-policy.md) (OQ-AP). Each question states what an answer would look like and which claim it bears on.

**The magnitudes are the standing ask.** Every program magnitude is deliberately held (register row **M0**). Independent modeling that *establishes or overturns* them is exactly what we are inviting.

**Two expert gates.** Two classes of finding move only through named expert review: **program magnitudes** (M0) require credentialed-economist validation before any effect size is reported as established, and the **equity-vs-debt classification** (L1) requires a tax/securities counsel-grade opinion. Contributions toward either gate are the highest-value submissions this call can receive.

## Cadence

A **rolling** call. Claim-status changes ship on a periodic cadence, each with a changelog entry naming which claims moved — so critics can cite the exact tagged version they tested. *(Whether to attach a hard deadline — e.g., a special-issue window — is a maintainer decision; see the conformance note.)*

## Who we hope will engage

Academic economists (macro, public finance, labor); tax and securities scholars and practitioners; sovereign- and public-fund governance researchers; heterogeneous-agent modelers; and critics across the spectrum. We are not asking you to agree. We are asking you to test it.

*Standard: conservative. Directional findings are revised as evidence arrives; magnitudes are not asserted until validated (see M0).*
