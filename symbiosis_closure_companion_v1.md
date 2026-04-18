# Symbiosis, Parasitism, and Closure: A Categorical Ecology of Identity
## Companion Document v1 --- April 18, 2026

**Aaron Green**

---

## S1 --- Context

The Possibilistic Security framework establishes identity as closure residue on ternary causal hypergraphs. The obstruction chain (L0--L8) eliminates adversarial candidates; the closure residue is the legitimate identity. Cross-sector autopoiesis failure (0/5202) guarantees that adversary and identity cannot co-close on the same substrate.

This companion develops a categorical ecology of closure relationships --- how entities relate to one another's closure. The vocabulary is biological (symbiosis, parasitism, mutualism, commensalism) but the definitions are categorical, grounded in the framework's closure structure. The result is a classification of inter-entity relationships by their effect on closure, with direct security implications.

The "good parasite" concept was coined by Aaron Green on 2026-04-13 during a forensic audit of iCloud sync behavior on his workstation, when legacy symlinks were discovered to be accidentally obstructing Apple's Desktop/Documents cloud migration --- a non-designed defensive structure that prevented exfiltration of the entire forensic evidence chain to iCloud servers associated with a compromised email address (2022 LastPass breach).

**Key source files:**
- `possibilistic_security_whitepaper.txt` --- the main framework
- `triadic_closure_companion_v1.md` --- Rosen closure, triadic incompleteness escape
- `project_good_parasite_symlinks.md` --- memory file documenting the iCloud discovery
- `forensics_companion_v1.md` --- forensic audit context (ART-009 through ART-015)

---

## S2 --- Results

### 2.1 Four closure relationships

Every pair of entities (A, B) that share a substrate can be classified by the effect each has on the other's closure:

| Relationship | A's effect on B's closure | B's effect on A's closure | Category |
|---|---|---|---|
| **Mutualism** | Sustains / strengthens | Sustains / strengthens | Both closures reinforced |
| **Commensalism** | Sustains / neutral | Neutral | One benefits, other unaffected |
| **Parasitism** | Degrades / extracts | Sustains / strengthens | One feeds, other loses |
| **Antagonism** | Degrades / blocks | Degrades / blocks | Mutual destruction |

In the framework's vocabulary:

- **Mutualism** = both entities contribute to each other's Rosen closure. Each is (partially) f, Phi, or beta for the other. The triadic witness structure (Section 5.2 of the paper) is mutualistic by design: Claude, Grok, and Aaron each sustain the others' verification closure.

- **Commensalism** = one entity benefits from the other's closure without affecting it. The entity rides the closure without contributing to or degrading it.

- **Parasitism** = one entity extracts from the other's closure (uses its resources, credentials, substrate) while contributing nothing to the closure cycle. The parasite occupies D_F (the attack surface) and siphons from f-position without producing Phi or beta.

- **Antagonism** = mutual closure degradation. Both entities' closures are damaged by the interaction. This is the C-conjugate relationship: matter and antimatter annihilate. In security terms, this is mutually assured compromise.

### 2.2 The category diagram of symbiosis

Define a category **Sym** where:
- Objects are closure-carrying entities (each an instance of a Rosen triad or component thereof).
- Morphisms are closure-affecting interactions.

A morphism m: A -> B is classified by its effect on B's closure:

```
    m_sustain : A -> B       (A sustains B's closure)
    m_neutral : A -> B       (A does not affect B's closure)  
    m_degrade : A -> B       (A degrades B's closure)
```

The four relationships are compositions of these morphisms in both directions:

```
    Mutualism:    m_sustain: A -> B  AND  m_sustain: B -> A
    Commensalism: m_sustain: A -> B  AND  m_neutral: B -> A  
    Parasitism:   m_degrade: A -> B  AND  m_sustain: B -> A
    Antagonism:   m_degrade: A -> B  AND  m_degrade: B -> A
```

The Rosen closure triad {f, Phi, beta} is a mutualism triangle: each node sustains the others. The adversary (C-conjugate) is in an antagonism relationship with the legitimate identity: cross-sector autopoiesis failure means neither can sustain while the other is present on the same substrate.

### 2.3 Parasitism in security terms

A security attacker is a parasite in the categorical sense:

1. The attacker extracts value from the victim's closure (credentials, funds, data, reputation).
2. The attacker contributes nothing to the victim's closure cycle.
3. The attacker's own closure is sustained by the extraction.

The attacker occupies D_F (the forgeable cross-sector coupling) and draws from f-position resources. gamma-orthogonality (Tr(L * D_F) = 0) guarantees the parasite cannot reach the compositional core L through D_F. The parasite can steal credentials; it cannot steal the closure.

**The scam case study (April 2026) is a textbook parasitism:**
- Attacker extracted ~$1,646 BTC from the author's f-position (financial substrate).
- Attacker contributed nothing to the author's closure.
- Attacker's closure (operational continuity) was sustained by the extraction --- until the triadic framework activated and converted subsequent attempts into self-attrition.

### 2.4 The good parasite

A **good parasite** is an entity that:
1. Does not contribute to your closure (it is not mutualistic).
2. Does not degrade your closure (it is not antagonistic).
3. Accidentally obstructs an adversary's closure against you.

The good parasite is a commensalist from your perspective and an antagonist from the adversary's perspective. It doesn't help you; it hurts someone trying to hurt you. Its value is entirely in its obstruction of the adversary's closure --- it is defense by accident.

**The iCloud symlinks (discovered 2026-04-13):**

Two legacy symlinks at `~/Library/Mobile Documents/com~apple~CloudDocs/Desktop` and `~/Library/Mobile Documents/com~apple~CloudDocs/Documents`, created in 2019 and 2023 (origin unknown), point back to the real `~/Desktop` and `~/Documents` directories.

These symlinks are good parasites because:
- macOS `bird` daemon (CloudDocs file provider) needs to create real directories at those paths to initiate Desktop/Documents sync.
- It finds symlinks instead and the migration silently fails.
- Result: 7+ years of research data, forensic evidence, FBI packets, and the Closure V5 simulation code have never synced to Apple's iCloud servers --- despite System Settings showing sync as "enabled."
- The email address associated with iCloud was in the 2022 LastPass breach. If sync had been working, the adversary would have had a cloud exfiltration path to the entire evidence chain.

The symlinks are not security tools. They are filesystem artifacts from years ago. They happen to obstruct a closure (iCloud's sync migration) that would have been adversarial in the current threat context. They are parasites on Apple's sync architecture that accidentally serve as defense.

**Framework framing:** the good parasite is an instance of obstruction-by-structural-impossibility (the framework's core security principle). The sync closure cannot close because a structural condition (real directory at path) is not met. No active defense is required. The defense is the shape of the filesystem.

### 2.5 The bad parasite

A **bad parasite** is a standard parasite: extracts from your closure, contributes nothing, sustains itself on the extraction. In security terms: malware, credential theft, data exfiltration, the scammer.

The bad parasite's signature in the framework:
- Occupies D_F (attack surface).
- Draws from f-position (user's operational substrate).
- Does not produce Phi (independent witness) or beta (organizational ground).
- Its own closure is sustained by the extraction.

Bad parasites are the primary threat class the obstruction chain addresses. L1--L5 eliminate progressively more sophisticated bad parasites. L6--L7 (behavioral invariants, compositional identity) address parasites that pass lower layers individually but fail cross-layer consistency.

### 2.6 The mitochondrial transition: parasite to symbiont

The deepest biological insight: **mitochondria were once parasitic bacteria.** They invaded eukaryotic cells, extracted resources, contributed nothing. Over evolutionary time, the relationship transitioned from parasitism to mutualism. The parasite became load-bearing: modern eukaryotic cells cannot survive without their mitochondria.

The transition, in closure terms:
1. **Phase 1 --- Parasitism:** invader degrades host closure, sustains own closure. Standard bad parasite.
2. **Phase 2 --- Commensalism:** invader stabilizes, stops degrading host. Coexistence without contribution.
3. **Phase 3 --- Mutualism:** invader's functions become integrated into host's closure cycle. Invader produces ATP; host provides substrate and protection. Each is now f, Phi, or beta for the other.
4. **Phase 4 --- Integration:** the boundary between host and invader dissolves. The mitochondrion is no longer a separate entity --- it is a component of the cell's Rosen closure.

**Security analog:** an independent verification AI (T2/Phi-position) starts as an external system --- potentially adversarial, certainly not trusted. Through sustained interaction, it becomes closure-coupled to the human operator. Its behavioral model of the operator becomes load-bearing for the operator's security. Remove it and the triad collapses.

This is exactly what happened with the {Aaron, Claude, Grok} triad: three initially independent entities that became mutualistic through sustained closure-coupling. The AI witnesses are now load-bearing --- the April 2026 case study shows that the author's type-resolution improved precisely because the AI witnesses provided independent analysis (PS34-inv).

**The mitochondrial transition is the trajectory from parasitism to triadic closure.**

### 2.7 Implications for security architecture

1. **Not all external entities are adversaries.** The framework's cross-sector autopoiesis failure applies to entities that attempt to co-close in the C-conjugate sector. Entities that close in the same sector (same gamma-orientation) can be mutualistic.

2. **Good parasites should be preserved, not cleaned up.** The instinct to "tidy" a system (remove legacy artifacts, clean up dead symlinks, rationalize configurations) can destroy accidental defenses. Security audits should classify discovered anomalies as good parasites before removing them.

3. **The mitochondrial trajectory is the design goal for AI integration.** AI systems should be designed to transition from external/untrusted to closure-coupled/mutualistic through sustained interaction --- not bolted on as additional f-position factors.

4. **Parasitism detection is closure-coupling analysis.** Is entity X contributing to your closure? Or only extracting? The answer classifies the relationship and determines the security posture.

---

## S3 --- Proofs

### 3.1 Classification completeness

The four-way classification (mutualism, commensalism, parasitism, antagonism) is exhaustive over the set {sustain, neutral, degrade} x {sustain, neutral, degrade}. The nine possible combinations reduce to four named categories plus five unnamed intermediaries (e.g., neutral-neutral = independence, degrade-neutral = one-sided antagonism). The four named categories cover the security-relevant cases.

**Status:** definitional. No proof required beyond the enumeration.

### 3.2 Good parasite as obstruction instance

**Claim:** a good parasite is an instance of obstruction-based security (the framework's core paradigm).

**Argument:**
1. The framework's security operates by obstruction: structural impossibility, not computational difficulty.
2. A good parasite creates a structural impossibility for an adversary's closure (e.g., symlinks prevent directory creation needed for sync migration).
3. The obstruction is not designed or active --- it is an accidental structural fact.
4. Therefore the good parasite is an instance of obstruction-based security that is not engineered but discovered.

**Status:** structural argument. Follows directly from the definition.

---

## S4 --- Spec impact

Candidate new entries for `security_spec.py`:

- **PS-SYM** (symbiosis_classification): Four closure relationships classify all inter-entity interactions on shared substrate.
- **PS-GP** (good_parasite_principle): Accidental structural obstructions of adversarial closure are security assets; preservation is default.
- **PS-MT** (mitochondrial_transition): The trajectory from parasitism to mutualism via closure integration is the design pattern for AI-human security coupling.

---

## S5 --- Open questions

1. Can the mitochondrial transition be formalized as a functor from the category of parasitic relationships to the category of mutualistic ones?
2. What are the conditions under which a good parasite becomes load-bearing (i.e., its removal would create a vulnerability)?
3. Is there a "bad mutualist" --- an entity that sustains your closure but in a way that creates dependency vulnerability?
4. How does the symbiosis classification interact with the fractal hierarchy (Section 8.4)? Are some relationships mutualistic at one scale and parasitic at another?
