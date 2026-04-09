"""
test_security_spec.py — Structural validation for Possibilistic Security spec.
Analog to test_catlab_spec.jl.

Run: python test_security_spec.py
"""

import sys
from security_spec import (
    SCORECARD, OBSTRUCTION_CHAIN, WORKFLOW_TRIAD, SECURITY_TRIAD,
    Status, EvidenceType, Layer, Position,
    get_entry, entries_by_status, dependency_chain,
)


def test_entry_ids_unique():
    ids = [e.id for e in SCORECARD]
    assert len(ids) == len(set(ids)), f"Duplicate IDs: {[x for x in ids if ids.count(x) > 1]}"

def test_entry_keys_unique():
    keys = [e.key for e in SCORECARD]
    assert len(keys) == len(set(keys)), f"Duplicate keys: {[x for x in keys if keys.count(x) > 1]}"

def test_dependencies_exist():
    ids = {e.id for e in SCORECARD}
    for e in SCORECARD:
        for dep in e.depends_on:
            assert dep in ids, f"{e.id} depends on {dep} which does not exist"

def test_no_circular_dependencies():
    for e in SCORECARD:
        chain = dependency_chain(e.id)
        assert e.id in chain, f"Dependency chain for {e.id} is broken"

def test_proved_entries_have_evidence():
    for e in SCORECARD:
        if e.status == Status.PROVED:
            assert e.evidence_type not in (EvidenceType.COMPUTATIONAL, EvidenceType.NONE), \
                f"{e.id} is PROVED but evidence type is {e.evidence_type.name}"

def test_imported_entries_have_closure_ref():
    for e in SCORECARD:
        if e.evidence_type == EvidenceType.IMPORTED:
            assert e.closure_ref is not None, f"{e.id} is IMPORTED but has no closure_ref"

def test_obstruction_chain_complete():
    layers = {ol.layer for ol in OBSTRUCTION_CHAIN}
    for l in Layer:
        assert l in layers, f"Layer {l.name} missing from obstruction chain"

def test_obstruction_chain_ordered():
    values = [ol.layer.value for ol in OBSTRUCTION_CHAIN]
    assert values == sorted(values), "Obstruction chain is not in order"

def test_triads_have_all_positions():
    for name, triad in [("workflow", WORKFLOW_TRIAD), ("security", SECURITY_TRIAD)]:
        positions = {tc.position for tc in triad}
        for p in Position:
            assert p in positions, f"{name} triad missing {p.name} position"

def test_triads_have_exactly_three():
    assert len(WORKFLOW_TRIAD) == 3, f"Workflow triad has {len(WORKFLOW_TRIAD)} components"
    assert len(SECURITY_TRIAD) == 3, f"Security triad has {len(SECURITY_TRIAD)} components"

def test_pinned_counts():
    """Pinned counts — update these when spec changes."""
    assert len(SCORECARD) == 26, f"Expected 26 entries, got {len(SCORECARD)}"
    assert len(entries_by_status(Status.PROVED)) == 3
    assert len(entries_by_status(Status.VERIFIED)) == 1
    assert len(entries_by_status(Status.CONJECTURED)) == 22
    assert len(OBSTRUCTION_CHAIN) == 9


# ── Run all tests ──

def run_tests():
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
            print(f"  ✓ {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"  ✗ {t.__name__}: {e}")
        except Exception as e:
            failed += 1
            print(f"  ✗ {t.__name__}: {type(e).__name__}: {e}")

    print(f"\n{'='*40}")
    print(f"  {passed} passed, {failed} failed, {passed+failed} total")
    return failed == 0


if __name__ == "__main__":
    print("Possibilistic Security — Spec Tests")
    print("=" * 40)
    ok = run_tests()
    sys.exit(0 if ok else 1)
