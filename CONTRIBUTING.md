# Contributing

The most useful contribution you can make here is **well-argued disagreement.** This repo exists to have
its claims tested. Three contribution paths, smallest unit first:

## 1. Falsification (the headline path)
Take a claim from [`CLAIMS.md`](CLAIMS.md) and flip its stated disconfirming test:
- **Scenario run:** copy a file in `model/scenarios/`, change the assumptions (documented, sourced),
  rerun (`python model/run_scenario.py your_scenario.yml`), and submit the scenario file + output via a
  **falsification report** issue. This is the preferred unit — small, reproducible, machine-checkable.
- **Model/derivation error:** a reproducible error in the code or a formula (`FORMULAS.md`).
- **Published empirical evidence** directly contradicting a claim's evidence base
  (`claims/evidence/<ID>.md`).
What counts is pre-stated in [`CALL_FOR_PAPERS.md`](CALL_FOR_PAPERS.md); adjudication rules in
[`GOVERNANCE.md`](GOVERNANCE.md).

## 2. Answering an open question
Claim a question from [`open-questions/`](open-questions/) by opening a **question-claim** issue citing
its OQ-ID (stakes the question so effort isn't duplicated). Each question states what an answer would
look like.

## 3. Extension / commentary
Framing disagreements, alternative designs, comparative analyses — welcome via an **extension proposal**
issue. Not a falsification path, and not less valued for it.

## Credit
A pre-stated ladder: **named in the register** (any contribution that informs a status decision) → **an
entry in `replications/`** (replication/falsification attempts, whatever their outcome) → **co-authorship
on a revised white paper** (contributions that change a claim's status). Strong disagreement is credited
identically to support.

## Ground rules
Registers and `CLAIMS.md` are maintainer-written — contribute through the templated units above, not by
editing them. No contribution asserts a program magnitude as settled (see `CLAIMS.md` row M0). Be
specific; cite sources; expect your challenge to be taken seriously.
