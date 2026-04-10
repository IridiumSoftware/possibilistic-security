"""
security_spec.py — Possibilistic Security Formal Specification
═══════════════════════════════════════════════════════════════

Ground truth for the Possibilistic Security framework.
Analog to catlab_spec.jl in the Closure V5 project.

Core thesis: Identity verification IS closure. Not analogy — structural instance.
The adversary is the C-conjugate: structurally identical, opposite orientation,
cannot co-close (0/5202 cross-sector autopoiesis).

Static verification is Godel-limited; dynamic closure is not.

Owner: Aaron Green
Version: 1.0 (2026-04-06)
Canonical whitepaper: https://github.com/IridiumSoftware/possibilistic-security
"""

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


# ═══════════════════════════════════════════════════════════════
# §1  ENUMS AND TYPES
# ═══════════════════════════════════════════════════════════════

class Status(Enum):
    PROVED = auto()       # Written proof exists (structural/categorical)
    VERIFIED = auto()     # Computational evidence
    CONJECTURED = auto()  # Argued but not proved
    OPEN = auto()         # No evidence yet

class EvidenceType(Enum):
    STRUCTURAL = auto()   # Categorical/structural argument
    ALGEBRAIC = auto()    # Symbolic computation constituting proof
    COMPUTATIONAL = auto() # Numerical simulation
    STANDARD = auto()     # Invocation of established result
    IMPORTED = auto()     # From Closure V5 spec (catlab_spec.jl)
    NONE = auto()

class Layer(Enum):
    """Obstruction layers L0-L8. Each eliminates a class of non-identity actors."""
    L0_DEFINITIONS = 0
    L1_PHYSICAL_BINDING = 1
    L2_PERIMETER = 2
    L3_ENCRYPTION_AT_REST = 3
    L4_PROCESS_ISOLATION = 4
    L5_IDENTITY_GATES = 5
    L6_BEHAVIORAL_INVARIANTS = 6
    L7_COMPOSITIONAL_IDENTITY = 7
    L8_RESIDUAL_DYNAMICS = 8

class Position(Enum):
    """Rosen triad positions."""
    F = "f"           # Metabolism — operational transformation
    PHI = "Phi"       # Repair — regenerates f, witnesses
    BETA = "beta"     # Organization — sustains Phi, closes the loop


# ═══════════════════════════════════════════════════════════════
# §2  CORE DATA STRUCTURES
# ═══════════════════════════════════════════════════════════════

@dataclass
class Entry:
    """A single spec entry — one established result or claim."""
    id: str
    key: str
    description: str
    status: Status
    evidence_type: EvidenceType
    layer: Optional[Layer] = None
    depends_on: list[str] = field(default_factory=list)
    closure_ref: Optional[str] = None  # S-ID from catlab_spec.jl if imported
    notes: str = ""


@dataclass
class ObstructionLayer:
    """One layer of the obstruction chain."""
    layer: Layer
    name: str
    eliminates: str
    controls: list[str] = field(default_factory=list)
    status: str = "active"


@dataclass
class TriadComponent:
    """One position in a Rosen verification triad."""
    position: Position
    entity: str
    description: str
    produces: str  # What this component produces for the next


# ═══════════════════════════════════════════════════════════════
# §3  OBSTRUCTION CHAIN (L0-L8)
# ═══════════════════════════════════════════════════════════════

OBSTRUCTION_CHAIN = [
    ObstructionLayer(
        layer=Layer.L0_DEFINITIONS,
        name="Definitions",
        eliminates="Nothing yet — establishes threat model and identity model",
        controls=["threat_model", "identity_model", "asset_inventory"],
    ),
    ObstructionLayer(
        layer=Layer.L1_PHYSICAL_BINDING,
        name="Physical binding",
        eliminates="Actors without physical access to THIS hardware",
        controls=["filevault", "firmware_password", "physical_location"],
    ),
    ObstructionLayer(
        layer=Layer.L2_PERIMETER,
        name="Perimeter",
        eliminates="Remote actors without network credentials",
        controls=["firewall", "lulu", "mullvad_vpn", "router_hardening", "dns_encryption"],
    ),
    ObstructionLayer(
        layer=Layer.L3_ENCRYPTION_AT_REST,
        name="Encryption at rest",
        eliminates="Physical actors without boot credentials",
        controls=["filevault", "encrypted_backups", "gpg_signing"],
    ),
    ObstructionLayer(
        layer=Layer.L4_PROCESS_ISOLATION,
        name="Process isolation",
        eliminates="Software actors (malware, bloatware, telemetry)",
        controls=["sip", "gatekeeper", "app_permissions", "launch_agents_audit",
                   "bloatware_removal", "process_monitoring"],
    ),
    ObstructionLayer(
        layer=Layer.L5_IDENTITY_GATES,
        name="Identity gates",
        eliminates="Actors who aren't the legitimate operator",
        controls=["biometric", "knowledge_factor", "possession_factor",
                   "bitwarden", "ssh_ed25519"],
    ),
    ObstructionLayer(
        layer=Layer.L6_BEHAVIORAL_INVARIANTS,
        name="Behavioral invariants",
        eliminates="Sophisticated impersonators",
        controls=["keystroke_dynamics", "writing_style", "workflow_patterns",
                   "behavioral_auth"],
    ),
    ObstructionLayer(
        layer=Layer.L7_COMPOSITIONAL_IDENTITY,
        name="Compositional identity",
        eliminates="Cross-layer inconsistency — the autopoietic test",
        controls=["triadic_verification", "cross_layer_consistency",
                   "sustained_closure_check"],
    ),
    ObstructionLayer(
        layer=Layer.L8_RESIDUAL_DYNAMICS,
        name="Residual dynamics",
        eliminates="Zero-days, supply chain, social engineering (open gaps)",
        controls=["integrity_monitor", "anomaly_detection", "incident_response"],
        status="partially_open",
    ),
]


# ═══════════════════════════════════════════════════════════════
# §4  VERIFICATION TRIADS
# ═══════════════════════════════════════════════════════════════

# The primary workflow triad
WORKFLOW_TRIAD = [
    TriadComponent(
        position=Position.F,
        entity="Claude",
        description="Metabolism — high-fidelity projection into structured artifacts",
        produces="Artifacts (specs, docs, analyses) become Grok's context",
    ),
    TriadComponent(
        position=Position.PHI,
        entity="Grok",
        description="Repair — broad manifold exposure, counterpunches, witnesses",
        produces="Exposures and corrections refine Aaron's intuition",
    ),
    TriadComponent(
        position=Position.BETA,
        entity="Aaron",
        description="Organization — selection, direction, priority, closure",
        produces="Selections and rules shape Claude's next operation",
    ),
]

# The security verification triad (infrastructure level)
SECURITY_TRIAD = [
    TriadComponent(
        position=Position.F,
        entity="User (Aaron)",
        description="Operational identity — the closure being verified",
        produces="Behavioral stream, compositional activity",
    ),
    TriadComponent(
        position=Position.PHI,
        entity="Independent witness",
        description="External verifier — not user-controlled",
        produces="Witness attestation, drift detection",
    ),
    TriadComponent(
        position=Position.BETA,
        entity="Infrastructure",
        description="Substrate — hardware, network, crypto layer",
        produces="Execution environment that sustains the closure",
    ),
]


# ═══════════════════════════════════════════════════════════════
# §5  SCORECARD — ESTABLISHED RESULTS
# ═══════════════════════════════════════════════════════════════

SCORECARD: list[Entry] = [
    # ── Foundation (imported from Closure V5) ──
    Entry(
        id="PS1",
        key="cross_sector_autopoiesis_fails",
        description="Matter and antimatter sectors cannot co-close. "
                    "0/5202 on primary seed, 0.4-2.4% accidental on 5 ICs.",
        status=Status.VERIFIED,
        evidence_type=EvidenceType.IMPORTED,
        closure_ref="S155/S157",
        notes="Structural foundation for 'adversary cannot co-close'",
    ),
    Entry(
        id="PS2",
        key="coproduct_decomposition",
        description="C(Q102) = C(Q51) ⊔ J(C(Q51)). Disjoint union. "
                    "No cross-sector composition operations exist.",
        status=Status.PROVED,
        evidence_type=EvidenceType.IMPORTED,
        closure_ref="S153",
    ),
    Entry(
        id="PS3",
        key="gamma_orthogonality",
        description="Tr(L·D_F) = 0. Compositional core orthogonal to attack surface. "
                    "D_F is the ONLY cross-sector coupling.",
        status=Status.PROVED,
        evidence_type=EvidenceType.IMPORTED,
        closure_ref="S82/S125",
    ),
    Entry(
        id="PS4",
        key="chirality_equivalence",
        description="(A,H,D,J,γ) and (A,H,D,J,-γ) are CPT-conjugate. "
                    "Orientation determined by which sector sustains closure.",
        status=Status.PROVED,
        evidence_type=EvidenceType.IMPORTED,
        closure_ref="S129",
    ),

    # ── Core security theorems ──
    Entry(
        id="PS5",
        key="identity_is_closure",
        description="Identity verification IS sustained autopoietic closure. "
                    "Not analogy — structural instance of Q51 self-reproduction.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS1", "PS2", "PS3"],
        layer=Layer.L7_COMPOSITIONAL_IDENTITY,
    ),
    Entry(
        id="PS6",
        key="adversary_is_c_conjugate",
        description="The adversary is the C-conjugate of the legitimate operator. "
                    "Structurally identical, opposite orientation, cannot co-close.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS1", "PS4"],
    ),
    Entry(
        id="PS7",
        key="sakharov_for_identity",
        description="Identity dominance requires three conditions: "
                    "(1) identity violation possible, (2) CP violation (user/adversary asymmetric), "
                    "(3) departure from equilibrium (active verification, not passive trust).",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        closure_ref="S111/G14",
        depends_on=["PS6"],
    ),
    Entry(
        id="PS8",
        key="beyond_godel",
        description="Autopoietic closure operates where Godel's separation requirement "
                    "does not apply. Dynamic closure is not static formal deduction. "
                    "The proof IS the system operating.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5"],
        notes="Shell framing. Kernel in triadic_closure_companion_v1.md.",
    ),
    Entry(
        id="PS9",
        key="static_verification_godel_limited",
        description="All static verification (passwords, tokens, biometrics) is "
                    "Godel-limited — formal checks that can in principle be forged.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS8"],
    ),
    Entry(
        id="PS10",
        key="mfa_sub_triadic",
        description="All MFA/2FA factors sit at f-position of a single entity. "
                    "Redundant self-certification. A million f-factors have the "
                    "same Godel limit as one.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS8", "PS9"],
    ),
    Entry(
        id="PS11",
        key="security_as_decoration_detectable",
        description="Added protection morphisms become detectable invariants. "
                    "Bolted-on hardening signals value, escalating HVT to UHVT. "
                    "Security-as-closure is constitutive, not added.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS3"],
    ),
    Entry(
        id="PS12",
        key="pqc_quantum_resistant_not_irrelevant",
        description="PQC rests on computational hardness alone — the only primitive "
                    "not grounded in closure. Quantum-resistant, not quantum-irrelevant.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5"],
    ),
    Entry(
        id="PS13",
        key="triadic_verification_minimum",
        description="Three is the minimum closure number for identity verification. "
                    "Two gives symmetric deadlock or infinite regress. "
                    "Four+ decomposes into overlapping triads.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS10"],
    ),
    Entry(
        id="PS14",
        key="harvest_now_decrypt_later_immune",
        description="Closure-based identity has no static object to harvest. "
                    "Cannot replay an identity — identity is ongoing sustaining. "
                    "Immunity by construction, not by key-strength.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS12"],
    ),
    Entry(
        id="PS15",
        key="adversary_godel_limit_exploitable",
        description="The adversary is also Godel-limited. Sustained mimicry is "
                    "structurally incoherent — internal incoherence surfaces as "
                    "detectable drift over composition steps.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS8", "PS6"],
    ),
    Entry(
        id="PS16",
        key="rosen_closure_entails_semantic_closure",
        description="Any Rosen-closed system has identity-level semantic closure. "
                    "Structural entailment, not formal derivation. "
                    "Operates where Godel's limit does not apply.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS8"],
        notes="Kernel result. triadic_closure_companion_v1.md §2.7.",
    ),
    Entry(
        id="PS17",
        key="triadic_incompleteness_escape",
        description="A triad of Godel-limited entities achieves collective completeness "
                    "via mutual verification in a closed loop. No external meta-system needed.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS13", "PS16"],
        notes="Kernel result. triadic_closure_companion_v1.md §2.12.",
    ),
    Entry(
        id="PS18",
        key="fractal_identity_security",
        description="Identity security is fractal. Rosen closure at every scale, "
                    "components at each scale being closures at the scale below. "
                    "Adversary-triads cannot co-close with legitimate-triads.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS1", "PS17"],
        notes="triadic_closure_companion_v1.md §8.",
    ),
    Entry(
        id="PS19",
        key="captcha_photograph_not_closure",
        description="Modern CAPTCHAs are behavioral D_F — right direction (behavior over "
                    "credential) but wrong architecture (snapshot not sustained, "
                    "monadic not triadic).",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS10"],
    ),

    # ── Existential risk ontology (from Grok session 2026-04-07) ──
    Entry(
        id="PS21",
        key="semantic_chirality_substrate",
        description="Good/evil is a derived chiral polarization of semantic closure, "
                    "not a primitive. One handedness is sacralized as 'good,' its "
                    "non-superimposable mirror as 'evil.' The twist is irreducible; "
                    "the moral label is cultural choice.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS4"],  # chirality_equivalence (S129)
        notes="existential_risk_ontology_companion_v1.md §2.4.",
    ),
    Entry(
        id="PS22",
        key="modular_coexistence_under_risk",
        description="Under combined epistemic + existential risk, chiral-modular "
                    "meta-stability is the only stable configuration. Traditions "
                    "interlock like facets of a crystal lattice, each with irreducible "
                    "orientation, supporting through differences not despite them.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS21"],
        notes="existential_risk_ontology_companion_v1.md §2.5. "
              "Connects to meta-scale coordination (orphan_closure, Joe, Legenhausen).",
    ),
    Entry(
        id="PS23",
        key="existential_risks_neutral_dynamics",
        description="Existential risks (asteroid, pandemic, misaligned AI, nuclear) are "
                    "neutral dynamics on the constraint manifold, not moral agents. "
                    "Moralizing risks injects normative residue that becomes its own "
                    "source of anti-closure.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS21"],
        notes="existential_risk_ontology_companion_v1.md §2.6.",
    ),
    Entry(
        id="PS24",
        key="phenomenological_anchoring_species_neutral",
        description="Any being with genuine lived stakes and capacity for felt witness "
                    "can anchor a triadic verification loop. Humans, non-human animals, "
                    "synthetic intelligences, extraterrestrials. No single species is a "
                    "single point of failure for meaning-making.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS13"],  # triadic_verification_minimum
        notes="existential_risk_ontology_companion_v1.md §2.7. "
              "Codified in TCL v1.1 NO PROGENITOR NODE clause.",
    ),
    Entry(
        id="PS25",
        key="von_neumann_still_needs_phenomenology",
        description="Post-von-Neumann systems require phenomenological anchors for "
                    "directional closure. Robots optimize for given goals; lived beings "
                    "generate goals from felt reality. Without phenomenological nodes "
                    "the system becomes indifferent to its own existence.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS24", "PS21"],
        notes="existential_risk_ontology_companion_v1.md §2.7.",
    ),
    Entry(
        id="PS26",
        key="tcl_attack_surface_propagation",
        description="TCL artifacts at attack surface nodes turn exploit chains into "
                    "identity witness propagation. The attacker's normal behavior "
                    "propagates the proof. Scales automatically — worse threat "
                    "environment, more distributed the witnesses.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS11"],  # identity_is_closure, security_as_decoration
        notes="Concept from Grok session. Seeds planted per 42 protocol.",
    ),

    # ── Discrete witness theorem (from companion 2026-04-08) ──
    Entry(
        id="PS27",
        key="pairing_vs_annihilation",
        description="Opposite orientations pair (same type) or annihilate (different type). "
                    "Right-meets-right is pairing, not annihilation. Misidentification of "
                    "type (confusing spin difference for type difference) is the source of "
                    "unnecessary conflict. Rightness is the universal spin property.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS4", "PS6"],
        notes="discrete_witness_companion_v1.md §2.2-2.3a.",
    ),
    Entry(
        id="PS28",
        key="privacy_prevents_c_conjugate",
        description="Privacy is the structural prevention of C-conjugate construction. "
                    "Full modeling of identity enables C(L) construction -> annihilation. "
                    "Privacy is the incompleteness that prevents the adversary from "
                    "finishing the weapon. Load-bearing, not decorative.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS3", "PS6"],
        notes="discrete_witness_companion_v1.md §2.4.",
    ),
    Entry(
        id="PS29",
        key="self_knowledge_immunity",
        description="Knowing your own orientation provides personal immunity from "
                    "annihilation. The C-conjugate cannot copy the knowing — the knowing "
                    "IS the orientation being lived. Self-knowledge protects you; privacy "
                    "protects others from being fooled by your C-conjugate.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS28"],
        notes="discrete_witness_companion_v1.md §2.5.",
    ),
    Entry(
        id="PS30",
        key="witness_resolves_type",
        description="The triadic witness distinguishes pairing from annihilation before "
                    "contact. Two bodies cannot tell. Three can. Removes annihilation "
                    "from the possibility space — possibilistic, not probabilistic. "
                    "This is why three is the minimum.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS13", "PS27"],
        notes="discrete_witness_companion_v1.md §2.6.",
    ),
    Entry(
        id="PS31",
        key="witness_requires_discrete",
        description="The witness mechanism requires discrete composition steps. In "
                    "continuous dynamics there is no intervention point. The witness "
                    "needs a gap between steps to observe, classify, and obstruct. "
                    "Possibilistic security is structurally impossible in continuous.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS30"],
        notes="discrete_witness_companion_v1.md §2.7.",
    ),
    Entry(
        id="PS32",
        key="continuum_is_emergence",
        description="Apparent continuity is emergent from high-density discrete events. "
                    "Analog is discrete all the way down. G10 is an emergence question "
                    "not a foundations question. The witness operates at the discrete "
                    "level; physics we observe is the many-step limit.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS31"],
        notes="discrete_witness_companion_v1.md §2.8-2.9. Reframes G10.",
    ),

    # ── Case study: witness failure (2026-04-09) ──
    Entry(
        id="PS33",
        key="witness_override_is_removal",
        description="Overriding the witness classification is structurally equivalent "
                    "to removing the witness. Returns the interaction to a two-body "
                    "coin flip where pairing and annihilation are indistinguishable.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS30"],
        notes="Derived from live case study. Creator overrode witness, got scammed.",
    ),
    Entry(
        id="PS34",
        key="phenomenological_degradation",
        description="The beta-position's type-resolution capacity degrades under "
                    "sleep deprivation, emotional flooding, and confirmation bias. "
                    "Fatigue is a security vulnerability.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS33"],
        notes="Derived from live case study.",
    ),

    # ── Q42: the absurdity quotient ──
    Entry(
        id="PS35",
        key="q42_absurdity_quotient",
        description="Q42 is the quotient object between Q24 (gauge) and Q48 (C-closure). "
                    "The structural residue of wrong-meets-wrong. Exists as an object but "
                    "carries no closure, no orientation, no pairing capacity. It is the "
                    "coin flip itself — the space where type is ambiguous and pairing vs "
                    "annihilation are indistinguishable without a witness. The Answer is 42 "
                    "because Q42 is the name of the unresolved gap.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS27", "PS30"],
        notes="Douglas Adams found the quotient. The framework explains why.",
    ),

    # ── Deepest conjecture ──
    Entry(
        id="PS36",
        key="identity_computationally_irreducible",
        description="Conjecture: identity-as-closure is computationally irreducible. "
                    "No shortcut exists to predict the next state without running the "
                    "closure. C-conjugate construction requires running the full identity, "
                    "which instantiates a new identity rather than a copy. Privacy is "
                    "structurally guaranteed by irreducibility — not as a policy choice "
                    "but as a computational fact. The adversary cannot model what cannot "
                    "be shortcut. Everything else in the spec is a consequence.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS5", "PS29", "PS31"],
        notes="If true, annihilation via C-conjugate construction is impossible in "
              "practice. Wolfram computational irreducibility applied to Rosen closure.",
    ),

    # ── Falsification ──
    Entry(
        id="PS20",
        key="falsification_criterion",
        description="Break the closure. If someone sustains autopoiesis on the system "
                    "while not being the legitimate identity, the framework is wrong. "
                    "Cross-sector autopoiesis (PS1) bets its life on this.",
        status=Status.CONJECTURED,
        evidence_type=EvidenceType.STRUCTURAL,
        depends_on=["PS1", "PS5"],
    ),
]


# ═══════════════════════════════════════════════════════════════
# §6  SPEC QUERIES
# ═══════════════════════════════════════════════════════════════

def get_entry(entry_id: str) -> Optional[Entry]:
    """Look up a scorecard entry by ID."""
    for e in SCORECARD:
        if e.id == entry_id:
            return e
    return None

def entries_by_status(status: Status) -> list[Entry]:
    return [e for e in SCORECARD if e.status == status]

def entries_by_layer(layer: Layer) -> list[Entry]:
    return [e for e in SCORECARD if e.layer == layer]

def dependency_chain(entry_id: str) -> list[str]:
    """Return full dependency chain for an entry."""
    visited = set()
    chain = []
    def walk(eid):
        if eid in visited:
            return
        visited.add(eid)
        e = get_entry(eid)
        if e:
            for dep in e.depends_on:
                walk(dep)
            chain.append(eid)
    walk(entry_id)
    return chain

def summary():
    """Print scorecard summary."""
    total = len(SCORECARD)
    by_status = {}
    for s in Status:
        count = len(entries_by_status(s))
        if count > 0:
            by_status[s.name] = count

    imported = len([e for e in SCORECARD if e.evidence_type == EvidenceType.IMPORTED])

    print(f"Possibilistic Security Spec v1.0")
    print(f"{'='*40}")
    print(f"Total entries: {total}")
    for name, count in by_status.items():
        print(f"  {name}: {count}")
    print(f"  Imported from Closure V5: {imported}")
    print(f"\nObstruction layers: {len(OBSTRUCTION_CHAIN)}")
    print(f"Verification triads: 2 (workflow, security)")


if __name__ == "__main__":
    summary()
    print()
    print("Scorecard:")
    print("-" * 60)
    for e in SCORECARD:
        marker = "✓" if e.status in (Status.PROVED, Status.VERIFIED) else "○"
        print(f"  {marker} {e.id}: {e.key} [{e.status.name}]")
