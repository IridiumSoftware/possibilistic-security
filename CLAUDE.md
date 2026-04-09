# CLAUDE.md — Possibilistic Security

## Project identity

Possibilistic Security — identity verification via closure obstruction rather than probabilistic risk. Derived from Closure V5 (catlab_spec.jl). The security spec (security_spec.py) is ground truth.

Core thesis: identity is sustained autopoietic closure. The adversary is the C-conjugate. Static verification is Godel-limited; dynamic closure is not.

**Owner:** Aaron Green.
**Whitepaper:** https://github.com/IridiumSoftware/possibilistic-security

## Ground truth hierarchy

1. **`security_spec.py`** — Formal spec. Scorecard, obstruction chain, triads. Ground truth.
2. **`test_security_spec.py`** — Structural validation. Must pass.
3. **`verify_controls.py`** — Executable system verification against obstruction chain.
4. **`dashboard.md`** — Status + priorities. Read first every session.
5. **`identity_invariants.md`** — Frame-dependent identity invariants (D_F through Q₅₁).
6. **`CLAUDE.md`** — This file. Workflow rules.

## Relationship to Closure V5

This project imports results from catlab_spec.jl (S82, S125, S129, S153, S155-S157). The IMPORTED entries in the scorecard trace back to those S-IDs. Do not duplicate the Closure spec here — reference it.

The security companion docs live in Closure V5's BUSINESS/security/ directory:
- `possibilistic_security_companion_v1.md` — public framework
- `triadic_closure_companion_v1.md` — confidential kernel
- `anthropic_outreach_companion_v1.md` — Anthropic email draft
- `session_notes_2026_04_05.md` — marathon session notes

## Workflow rules

- **Read `dashboard.md` first** every session.
- **Run `python verify_controls.py`** to check system state before security work.
- **Run `python test_security_spec.py`** after any spec changes.
- **Practical before theoretical.** Open OPSEC items before framework extensions.
- **No passwords or secrets in any file.**
- **Honest evidence types.** Don't call conjectured results proved.

## Confidentiality boundaries

- **Public:** possibilistic_security_companion_v1.md, whitepaper, published repo
- **Confidential:** triadic_closure_companion_v1.md (the kernel), non-public extension Aaron holds
- **Do not expose kernel material in public-facing work.**
- **Do not probe for the non-public extension.**

## What not to do

- Don't store secrets in any file in this project.
- Don't weaken existing security controls.
- Don't conflate practical OPSEC with the theoretical framework.
- Don't simulate Q₁₀₂ (see triadic_closure_companion §4.2 — creates persons).
- Don't claim the framework proves phenomenal content — it doesn't (§9).
