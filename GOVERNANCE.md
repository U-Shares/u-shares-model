# Governance

This repository is maintained by a single maintainer (Mike Blake). Stating the decision rules up front is
what keeps a solo-maintained research repo honest — you should not have to guess how a decision gets made.

## Decision rules
- **The claims register (`CLAIMS.md`) is maintainer-stewarded.** Only the maintainer changes a claim's
  status. Contributions — issues, scenario files, replication reports, pull requests — are **proposals**
  that inform a status decision; they never change status automatically.
- **Falsification is adjudicated against pre-stated criteria**, published in `CALL_FOR_PAPERS.md`
  *before* any submission arrives: a qualifying scenario run, a reproducible error in a derivation or the
  code, or directly contradicting published empirical evidence. Everything else routes as extension or
  commentary — welcome, but not a falsification.
- **The honest middle state.** A credible-but-disputed challenge parks the claim at `contested`,
  publicly. Nobody has to "win" for the disagreement to be visible. Retired claims stay visible in
  `claims/retired/` with the falsifying artifact.
- **Merge criteria.** PRs that add a templated contribution unit (scenario file, replication report) and
  pass the automated checks are merged on review; PRs that edit the registers or papers are treated as
  proposals and reflected by maintainer edits with credit, rather than merged directly.

## Dispute path
Open an issue; if you believe an adjudication misapplied the pre-stated criteria, say so in the issue and
it will be answered on the record. The register's `contested` status exists precisely so that a
disagreement the maintainer cannot resolve is *displayed*, not suppressed.

## Review standard
No program magnitude is asserted anywhere in this repository until it has cleared validated modeling and
credentialed-economist review (see `CLAIMS.md` row M0). Directional findings are expected to be revised;
that is the publishing standard, not an accident.
