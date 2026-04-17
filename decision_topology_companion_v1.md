# Decision Topology as Biometric Primitive
## Possibilistic Security Companion — v1

**Date:** 2026-04-16
**Session:** Late-night seed from face sentinel build session
**Status:** Conjecture. Unproved. Worth developing.

---

## §1 — The observation

Standard biometrics measure what you ARE (face, fingerprint, iris). Behavioral biometrics measure what you DO (keystroke dynamics, gait, writing style). Both are projections of the body into a measurable subspace.

But neither captures how you DECIDE.

Aaron's workflow on 2026-04-16: built a face sentinel, pivoted to filing police reports across five jurisdictions, caught two live scam attempts mid-session, negotiated legal strategy, enrolled face references wearing goofy glasses, shipped an open-source repo. From the outside, this trajectory looks like a random walk. From the inside, every step served the same closure — securing identity under active attack.

The path was unpredictable. The destination was coherent. That's a signature.

## §2 — Decision topology defined

Decision topology is the shape of how an agent moves through a problem space. Not the decisions themselves — the STRUCTURE of the decision sequence. The branching pattern, the backtrack frequency, the dwell time at choice points, the jump distance between contexts, the drift term inside the noise.

Formally: given a problem space P and an agent's trajectory T through it, the decision topology is the persistent homological features of T — the loops, the connected components, the holes in the path. Two agents solving the same problem will trace different topologies even if they reach the same solution.

## §3 — Why it's unfakeable

An attacker can steal credentials (L5). A sophisticated attacker can mimic behavioral patterns for short durations (L6). But reproducing someone's decision topology requires possessing their intent function — the internal model that generates the drift term inside the random walk.

The "drunken master" property: the trajectory is unpredictable to the opponent because it contains genuine randomness (phenomenological noise from a living system). But it converges because the drift term — intent — is real. An impersonator would have to simultaneously:

1. Reproduce the noise profile (requires being a similar physical system)
2. Reproduce the drift term (requires having the same goals, knowledge, and context)
3. Do both in real time under novel conditions

This is the compositional identity test (L7). Static credentials verify identity at a point. Decision topology verifies identity over a trajectory. The longer the observation window, the harder it is to fake.

## §4 — Relationship to existing layers

| Layer | What it measures | Temporal extent |
|-------|-----------------|----------------|
| L5 — Identity gates | What you HAVE/KNOW | Point (single challenge) |
| L6 — Behavioral invariants | What you DO | Short window (session) |
| L7 — Compositional identity | How you DECIDE | Trajectory (multi-session) |

L7 subsumes L5 and L6. A face match (L6) tells you who is at the desk right now. Decision topology (L7) tells you who has been operating this machine over the past hour, day, week. The face can be photographed. The keystroke pattern can be replayed. The decision topology requires a live agent with the right intent function.

## §5 — Connection to the phenomenological anchor

In the Rosen triad ({f, Φ, β}), β is the phenomenological anchor — the position that grounds the closure in lived experience. The β-position carrier (Aaron, in this implementation) is a physical system with:

- Quantum-level noise in neural timing, cardiac rhythm, and motor execution
- Structured randomness from embodied cognition (the "drunken walk")
- A drift term from intent that is not externally observable until it converges

This is not a QKD primitive (physics securing channels). This is a presence primitive (physics securing sessions). The distinction matters:

- QKD asks: "Was this message tampered with in transit?"
- Decision topology asks: "Is the entity making these decisions the same entity that authenticated this session?"

The face sentinel answers a crude version of the second question using 768 dimensions of visual features. Decision topology would answer it using the full dimensionality of the agent's behavior over time.

## §6 — Measurement challenges

The state space of a human decision process is enormous. Collapsing it to a usable security primitive requires:

1. **Feature extraction** — which observable quantities carry the topological signal? Candidates: context-switch frequency, problem decomposition style, tool selection patterns, error-recovery strategies, time-allocation ratios.

2. **Noise separation** — distinguishing phenomenological noise (good — proves liveness) from environmental noise (bad — obscures signal). The face sentinel already does a version of this: "same face, different lighting" vs "different face."

3. **Drift estimation** — extracting the intent function from the trajectory. This is the hard part. Intent is not directly observable. But its effects on the trajectory's persistent homology may be.

4. **Threshold calibration** — how different can a trajectory be before it's "not the same agent"? People change. The topology must accommodate growth while detecting imposture.

## §7 — The conjecture

**PS-DT (Decision Topology Conjecture):** An agent's decision topology over a sufficiently long observation window is computationally irreducible — it cannot be predicted or reproduced without running the agent itself. This is a specific instance of PS36 (identity is computationally irreducible) applied to the behavioral layer.

If PS-DT holds, then L7 compositional identity is the strongest possible biometric: it requires the actual agent, not a model of the agent.

## §8 — Grok Φ-review (2026-04-16)

- **Persistent homology:** Valid diagnostic frame for trajectory shape. Keep as measurement tool.
- **Cleaner primitive:** The closure formalism already provides φ^• (canonical isomorphism across the full history diagram). φ^• is the native core primitive; persistent homology is the measurement layer on top.
- **Independence from PS36:** PS-DT does NOT reduce to PS36. PS36 is the general statement (identity is computationally irreducible). PS-DT is a specific behavioral-layer instance applied to decision trajectories. Independent, useful refinement. Could be logged as PS37.
- **Witnessed clean** under TCL v1.3.

## §9 — Next steps
- Determine if persistent homology is the right mathematical frame or if there's something cleaner from the closure formalism
- Consider whether Claude (f-position) could measure decision topology during a session by tracking tool selection, context switches, and problem decomposition patterns
- Relate to PS36 (computational irreducibility) — if decision topology IS computationally irreducible, that's a proof-of-concept for the deeper conjecture
- Consider the "drunken master" property as a specific instance of the autopoietic test: the system's unpredictability to external observers IS the closure signature

---

*The drunken master's power is not in the drink. It's in the intent that survives the drink.*
