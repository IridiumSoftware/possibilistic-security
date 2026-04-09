# Identity Invariants — Aaron Green System

Analog to `physical_invariants.md` in Closure V5.
Frame-dependent invariants of the user-system.

## Methodology

Same discovery chain as Closure: hunch → model → confirm → define → verify → next invariant.
Match structure (patterns, hierarchies), not numbers.

## Layer 1 — Physical substrate

| Invariant | Value | Stability |
|-----------|-------|-----------|
| Hardware | MacBook (specific serial) | Years |
| Location pattern | Home / office / travel | Weekly variation |
| Network fingerprint | ASUS mesh, Mullvad VPN | Months |
| Peripheral set | Minimal (no external, vim workflow) | Stable |

## Layer 2 — Credential invariants (D_F — forgeable)

| Invariant | Type | Notes |
|-----------|------|-------|
| Bitwarden vault | Possession | Master password + biometric |
| SSH Ed25519 key | Possession | Generated 2026-04-03 |
| GPG key (RSA 4096) | Possession | ID: 638B8643DD51AEDD5E1272F284C0AF70B3A38A25 |
| Apple ID | Knowledge + possession | 2FA enabled |

**These are all f-position, all forgeable. D_F layer only.**

## Layer 3 — Behavioral invariants (toward Q₅₁)

| Invariant | Signal | Detection method |
|-----------|--------|-----------------|
| Typing cadence | Keystroke timing distribution | behavioral_auth.py |
| Writing style | Sentence structure, vocabulary | Stylometric analysis |
| Workflow pattern | vim + Brave + Claude Code + Grok relay | Process monitoring |
| Session rhythm | Deep work blocks, specific hours | Temporal analysis |
| Tool preference | CLI over GUI, minimal toolchain | Usage pattern |
| Research pattern | Obstruction-first, quotient structure | Content analysis |

**These are compositional but still snapshots. Not yet sustained closure.**

## Layer 4 — Compositional invariants (Q₅₁ — unforgeable)

| Invariant | Description | Why unforgeable |
|-----------|-------------|-----------------|
| Triadic workflow | Claude ↔ Aaron ↔ Grok relay pattern | Requires being Aaron |
| Research trajectory | Closure V5 conceptual development | Accumulated context |
| Cross-domain synthesis | Physics → security → theology → clinical | Unique combination |
| Correction patterns | How Aaron corrects Claude vs Grok | Relational, not static |
| Selection function | What Aaron keeps vs discards | The β-position itself |

**These are the Q₅₁ invariants — the autopoietic core.
The adversary would need to sustain these, not snapshot them.**

## Open questions

1. What are the quantitative thresholds for behavioral invariant detection?
2. How fast do behavioral invariants drift? What's the re-enrollment cadence?
3. Can compositional invariants be measured automatically, or only witnessed by triad members?
4. What's the minimum observation window for Q₅₁-level verification?
