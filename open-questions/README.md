# Open Questions — How This Register Works

This is the list of things U-Shares **cannot yet answer** — the honest edge of the work, and the heart of
the [call for papers](../CALL_FOR_PAPERS.md). Each question is an invitation: bring evidence, a sharper
method, or a decisive counter-argument. The questions are organized by the **five perspectives** a serious
reviewer brings, so you can go straight to the objections you're best equipped to press.

## The five registers

| Register | ID prefix | Questions | What this reviewer presses |
|---|---|---|---|
| [mechanism-design.md](mechanism-design.md) | `OQ-MD-###` | 6 | Does the Capital Dispersion Engine actually disperse? Does the incentive induce issuance? |
| [fiscal.md](fiscal.md) | `OQ-FIS-###` | 11 | Cost, durability, reserve sizing, and the employment-contingency of the funding path |
| [political-economy.md](political-economy.md) | `OQ-PE-###` | 2 | Capture, durability, incentive erosion, and "why hasn't this happened?" |
| [household.md](household.md) | `OQ-HH-###` | 4 | Does the stake *stick*? Recipient behavior and welfare |
| [adjacent-policy.md](adjacent-policy.md) | `OQ-AP-###` | 6 | Positioning and interaction vs. UBI, baby bonds, ESOPs, 401(k)s, SWFs |

Twenty-nine questions in all (6 · 11 · 2 · 4 · 6).

## How each question is written

Every entry carries four fields:

- **Question** — the objection, stated plainly.
- **What an answer would look like** — the *form* a credible answer takes, so you know when a question is
  actually resolved rather than merely argued.
- **Links to claim** — the entry in [`CLAIMS.md`](../CLAIMS.md) the question bears on. Answering a question
  can move that claim's status (`supported / contested / open / retired`).
- **Route** — whether a response is a **falsification** or an **extension** (see below).

**OQ-IDs are stable.** Once assigned, an ID is never renumbered, so you can cite `OQ-MD-001` durably in a
paper, an issue, or a scenario file.

## How to claim a question

Open an **Issue** using the `question-claim.yml` template and cite the OQ-ID you're taking up. That stakes
your claim to it (so effort isn't duplicated) and starts the thread. You do **not** edit this register or
`CLAIMS.md` — see the discipline note below.

## Falsification vs. extension

[`CALL_FOR_PAPERS.md`](../CALL_FOR_PAPERS.md) defines *what counts* before anyone submits, so adjudication
is never ad-hoc. In short: a **falsification** is a documented scenario run that flips a claim's stated
disconfirming test, a reproducible error in a derivation or the model code, or published empirical evidence
contradicting a claim's evidence base. Everything else — framing disagreements, values objections,
alternative proposals — is a welcome **extension**, routed accordingly. A credible-but-disputed challenge
parks its claim publicly at `contested`; nobody has to "win" for the disagreement to be visible.

## Register discipline

This register is **maintainer-written, contributor-read.** You contribute by submitting small, templated
units — a scenario file, an issue, a replication report — never by editing the register itself; only the
maintainer updates question and claim statuses. This keeps contribution fast and the register stable and
honest.

## Credit

Contributions are credited on a ladder: **named in the register → an entry in the replication registry →
co-authorship on a revised white paper** for contributions that change a claim's status. See
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) for the full protocol.

---

*Standard: conservative (see M0). These are open questions, not asserted findings; no program magnitude is
claimed here. Staged and **held** — not yet public.*
