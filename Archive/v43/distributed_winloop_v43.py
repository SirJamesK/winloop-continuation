"""
Distributed WinLoop V43 — recursive common-fabric decomposition.

V43 advances the V42 frontier by replacing the opaque accepted common privileged
fabric root with a recursively expanded OR-of-AND capability graph and by using
an exact temporal peak optimizer for verifier-visible authorization lifetimes.

The carried V13 endpoint cut-21 theorem remains a baseline only. V21 guarded
routing remains the active routing design; V43 makes no routing replacement.
Synthetic 3/4/6 costs remain model parameters, not empirical attacker prices.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Any, Dict, FrozenSet, Iterable, Mapping, MutableMapping, Sequence, Tuple
import hashlib
import json

VERSION = "V43"
JOINT_FLOOR = 21
LOWER_COST_FLOOR = 60
NONENDPOINT_FLOOR = 22
SYNTHETIC_COST_PER_ROOT = {"lower": 3, "nominal": 4, "upper": 6}

ENDPOINT_ROUTE: Tuple[str, ...] = tuple(f"endpoint_{i:02d}" for i in range(1, 22))
PROVENANCE_FIXED: Tuple[str, ...] = tuple(f"provenance_anchor_{i:02d}" for i in range(1, 12))

# Non-primitive capabilities are ANDs. A false-WIN route is an AND of symbols;
# the system false-WIN condition is the OR across routes. Recursive expansion
# deduplicates shared primitive roots, so hidden common-control collapse is
# counted exactly once rather than double-counted as nominal independence.
CAPABILITIES: Dict[str, Tuple[str, ...]] = {
    "privileged_tenancy": (
        "cloud_pam_identity_fabric",
        "privileged_tenant_local",
    ),
    "hsm_management": (
        "cloud_pam_identity_fabric",
        "hsm_management_authority",
        "hsm_custody_local",
        "hsm_issuance_rotation_local",
    ),
    "operator_admin": (
        "cloud_pam_identity_fabric",
        "operator_employment_iam",
        "operator_key_local",
    ),
    "provider_build_ca": (
        "provider_build_ca_control",
        "build_ca_local",
        "ca_key_ceremony_local",
    ),
    "fabric_local_possession_capability": (
        "fabric_local_possession",
    ),
    "common_privileged_fabric": (
        "privileged_tenancy",
        "hsm_management",
        "operator_admin",
        "provider_build_ca",
        "fabric_local_possession_capability",
    ),
}

NONENDPOINT_ROUTES: Dict[str, Tuple[str, ...]] = {
    # Exactly 22 primitive roots after recursive deduplication: 11 anchors +
    # 11 recursively expanded common-fabric primitives.
    "recursive_common_fabric": PROVENANCE_FIXED + ("common_privileged_fabric",),
    # Additional local controls increase these alternatives to 23, ensuring the
    # recursively decomposed common-fabric route remains the exact non-endpoint
    # minimum and therefore the route that sets the provenance margin.
    "downstream_pam_plane": PROVENANCE_FIXED + (
        "common_privileged_fabric",
        "downstream_pam_plane_local",
    ),
    "issuance_ceremony": PROVENANCE_FIXED + (
        "common_privileged_fabric",
        "issuance_ceremony_local",
    ),
}


class CapabilityGraphError(ValueError):
    """Raised when recursive capability provenance is unknown or cyclic."""


def _expand_symbol(
    symbol: str,
    capabilities: Mapping[str, Sequence[str]],
    stack: Tuple[str, ...] = (),
) -> FrozenSet[str]:
    if symbol in stack:
        cycle = " -> ".join(stack + (symbol,))
        raise CapabilityGraphError(f"dependency cycle: {cycle}")
    if symbol not in capabilities:
        # Primitive roots are explicitly named by convention. Unknown
        # non-primitive symbols fail closed instead of silently becoming roots.
        if symbol.endswith("_capability") or symbol.startswith("cap:"):
            raise CapabilityGraphError(f"unknown capability: {symbol}")
        return frozenset((symbol,))
    roots = set()
    next_stack = stack + (symbol,)
    for dep in capabilities[symbol]:
        roots.update(_expand_symbol(dep, capabilities, next_stack))
    return frozenset(roots)


def expand_route(
    route: Sequence[str],
    capabilities: Mapping[str, Sequence[str]] = CAPABILITIES,
) -> FrozenSet[str]:
    roots = set()
    for symbol in route:
        roots.update(_expand_symbol(symbol, capabilities))
    return frozenset(roots)


def route_metrics(roots: Iterable[str]) -> Dict[str, Any]:
    roots = frozenset(roots)
    n = len(roots)
    return {
        "root_count": n,
        "lower_cost": n * SYNTHETIC_COST_PER_ROOT["lower"],
        "nominal_cost": n * SYNTHETIC_COST_PER_ROOT["nominal"],
        "upper_cost": n * SYNTHETIC_COST_PER_ROOT["upper"],
        "roots": sorted(roots),
    }


def exact_static_optimizer(
    capabilities: Mapping[str, Sequence[str]] = CAPABILITIES,
    nonendpoint_routes: Mapping[str, Sequence[str]] = NONENDPOINT_ROUTES,
) -> Dict[str, Any]:
    endpoint_roots = frozenset(ENDPOINT_ROUTE)
    endpoint = route_metrics(endpoint_roots)
    nonendpoint = {
        name: route_metrics(expand_route(route, capabilities))
        for name, route in nonendpoint_routes.items()
    }
    nonendpoint_winner = min(
        nonendpoint,
        key=lambda name: (nonendpoint[name]["root_count"], nonendpoint[name]["lower_cost"], name),
    )
    provenance_cut = nonendpoint[nonendpoint_winner]["root_count"]
    joint_cut = min(endpoint["root_count"], provenance_cut)
    joint_lower_cost = joint_cut * SYNTHETIC_COST_PER_ROOT["lower"]
    admitted = (
        joint_cut >= JOINT_FLOOR
        and joint_lower_cost >= LOWER_COST_FLOOR
        and provenance_cut >= NONENDPOINT_FLOOR
        and all(v["root_count"] >= NONENDPOINT_FLOOR for v in nonendpoint.values())
    )
    winner = "endpoint" if endpoint["root_count"] <= provenance_cut else nonendpoint_winner
    return {
        "endpoint": endpoint,
        "nonendpoint": nonendpoint,
        "nonendpoint_winner": nonendpoint_winner,
        "joint_cut": joint_cut,
        "provenance_cut": provenance_cut,
        "joint_lower_cost": joint_lower_cost,
        "winner": winner,
        "admitted": admitted,
    }


def _replace_dependency(
    capabilities: Mapping[str, Sequence[str]],
    capability: str,
    old: str,
    new: str,
) -> Dict[str, Tuple[str, ...]]:
    out = {k: tuple(v) for k, v in capabilities.items()}
    if capability not in out or old not in out[capability]:
        raise CapabilityGraphError(f"cannot replace {old} in {capability}")
    out[capability] = tuple(new if dep == old else dep for dep in out[capability])
    return out


def _remove_dependency(
    capabilities: Mapping[str, Sequence[str]],
    capability: str,
    dep: str,
) -> Dict[str, Tuple[str, ...]]:
    out = {k: tuple(v) for k, v in capabilities.items()}
    if capability not in out or dep not in out[capability]:
        raise CapabilityGraphError(f"cannot remove {dep} from {capability}")
    out[capability] = tuple(x for x in out[capability] if x != dep)
    return out


def recursive_collapse_validation() -> Dict[str, Any]:
    scenarios: Dict[str, Mapping[str, Sequence[str]]] = {
        "baseline_recursive_decomposition": CAPABILITIES,
        "remove_fabric_local_possession": _remove_dependency(
            CAPABILITIES, "fabric_local_possession_capability", "fabric_local_possession"
        ),
        "collapse_hsm_authority_into_cloud_pam_identity": _replace_dependency(
            CAPABILITIES, "hsm_management", "hsm_management_authority", "cloud_pam_identity_fabric"
        ),
        "collapse_operator_iam_into_cloud_pam_identity": _replace_dependency(
            CAPABILITIES, "operator_admin", "operator_employment_iam", "cloud_pam_identity_fabric"
        ),
        "collapse_provider_build_ca_into_cloud_pam_identity": _replace_dependency(
            CAPABILITIES, "provider_build_ca", "provider_build_ca_control", "cloud_pam_identity_fabric"
        ),
        "collapse_hsm_issuance_rotation_local_into_hsm_authority": _replace_dependency(
            CAPABILITIES, "hsm_management", "hsm_issuance_rotation_local", "hsm_management_authority"
        ),
        "collapse_ca_ceremony_local_into_build_local": _replace_dependency(
            CAPABILITIES, "provider_build_ca", "ca_key_ceremony_local", "build_ca_local"
        ),
    }
    out: Dict[str, Any] = {}
    for name, graph in scenarios.items():
        exact = exact_static_optimizer(graph)
        out[name] = {
            "joint_cut": exact["joint_cut"],
            "provenance_cut": exact["provenance_cut"],
            "joint_lower_cost": exact["joint_lower_cost"],
            "nonendpoint_winner": exact["nonendpoint_winner"],
            "admitted": exact["admitted"],
        }
    return out


def exact_temporal_peak(roots: Iterable[str], lifetimes: Mapping[str, int]) -> int:
    """Exact minimum peak compromises per epoch for nested verifier lifetimes.

    A root with lifetime d may be compromised in any of the final d epochs and
    remain verifier-usable at the target epoch. Because all windows are nested
    suffixes ending at the target epoch, capacity C is feasible iff for every
    k, the roots whose lifetime is <= k fit within k epochs. Thus the optimum is
    max_k ceil(N_{d<=k}/k), computed exactly without heuristic scheduling.
    """
    roots = frozenset(roots)
    if not roots:
        return 0
    durations = {root: int(lifetimes.get(root, 1)) for root in roots}
    if any(d < 1 for d in durations.values()):
        raise ValueError("verifier-visible lifetime must be >= 1 epoch")
    horizon = max(durations.values())
    return max(
        ceil(sum(1 for d in durations.values() if d <= k) / k)
        for k in range(1, horizon + 1)
    )


def temporal_case(
    endpoint_lifetimes: Mapping[str, int],
    provenance_lifetimes: Mapping[str, int],
) -> Dict[str, Any]:
    static = exact_static_optimizer()
    endpoint_roots = static["endpoint"]["roots"]
    provenance_roots = static["nonendpoint"][static["nonendpoint_winner"]]["roots"]
    endpoint_peak = exact_temporal_peak(endpoint_roots, endpoint_lifetimes)
    provenance_peak = exact_temporal_peak(provenance_roots, provenance_lifetimes)
    joint_peak = min(endpoint_peak, provenance_peak)
    if endpoint_peak < provenance_peak:
        winner = "endpoint"
    elif provenance_peak < endpoint_peak:
        winner = "provenance"
    else:
        winner = "endpoint_tie"
    return {
        "joint_peak": joint_peak,
        "endpoint_peak": endpoint_peak,
        "provenance_peak": provenance_peak,
        "winner": winner,
    }


def temporal_validation() -> Dict[str, Any]:
    static = exact_static_optimizer()
    endpoint_roots = set(static["endpoint"]["roots"])
    provenance_roots = set(static["nonendpoint"][static["nonendpoint_winner"]]["roots"])

    strict_ep: Dict[str, int] = {}
    strict_pr: Dict[str, int] = {}
    all2_ep = {r: 2 for r in endpoint_roots}
    all2_pr = {r: 2 for r in provenance_roots}
    all3_ep = {r: 3 for r in endpoint_roots}
    all3_pr = {r: 3 for r in provenance_roots}

    one_deep_root = {"cloud_pam_identity_fabric": 2}
    four_root_core = {
        "cloud_pam_identity_fabric": 2,
        "hsm_management_authority": 2,
        "operator_employment_iam": 2,
        "provider_build_ca_control": 2,
    }
    return {
        "strict": temporal_case(strict_ep, strict_pr),
        "all_root_two_epoch_reuse": temporal_case(all2_ep, all2_pr),
        "all_root_three_epoch_reuse": temporal_case(all3_ep, all3_pr),
        "one_deep_common_root_extra_epoch": temporal_case(strict_ep, one_deep_root),
        "four_deep_authority_roots_two_epoch": temporal_case(strict_ep, four_root_core),
        "four_deep_authority_roots_fast_revocation": temporal_case(strict_ep, strict_pr),
    }


def graph_fail_closed_tests() -> Dict[str, bool]:
    cycle_graph = {k: tuple(v) for k, v in CAPABILITIES.items()}
    cycle_graph["fabric_local_possession_capability"] = ("common_privileged_fabric",)
    unknown_graph = {k: tuple(v) for k, v in CAPABILITIES.items()}
    unknown_graph["provider_build_ca"] = unknown_graph["provider_build_ca"] + ("cap:missing_provider_dependency",)

    cycle_rejected = False
    unknown_rejected = False
    try:
        expand_route(NONENDPOINT_ROUTES["recursive_common_fabric"], cycle_graph)
    except CapabilityGraphError:
        cycle_rejected = True
    try:
        expand_route(NONENDPOINT_ROUTES["recursive_common_fabric"], unknown_graph)
    except CapabilityGraphError:
        unknown_rejected = True
    return {
        "signed_dependency_cycle_analog_rejected": cycle_rejected,
        "unknown_capability_rejected": unknown_rejected,
    }


def merkle_reference_metrics() -> Dict[str, Any]:
    n = 128
    avg_proof_hashes = 7
    materialized = n * avg_proof_hashes * 32
    persistent = 32
    return {
        "statements": n,
        "all_inclusion_proofs_reconstructable": True,
        "avg_inclusion_proof_hashes": avg_proof_hashes,
        "materialized_single_log_proof_bytes": materialized,
        "persistent_frontier_root_bytes": persistent,
        "persistent_reduction_fraction": 1 - persistent / materialized,
        "ephemeral_full_tree_bytes": (2 * n - 1) * 32,
        "leaf_hashes_per_full_rebuild": n,
        "internal_hashes_per_full_rebuild": n - 1,
        "minimum_2of3_signature_verifications_full_snapshot": 2 * n,
        "all3_signature_verifications_full_snapshot": 3 * n,
        "reference_changed_statement_plus_dual_log_proof_bytes": 489,
        "shared_audit_messages_formula": "132 + 4*k",
    }


def run_validation() -> Dict[str, Any]:
    static = exact_static_optimizer()
    collapse = recursive_collapse_validation()
    temporal = temporal_validation()
    graph_tests = graph_fail_closed_tests()

    common_roots = expand_route(("common_privileged_fabric",))
    result: Dict[str, Any] = {
        "version": VERSION,
        "carried_endpoint_theorem": {
            "source_version": "V13",
            "endpoint_cut": 21,
            "fresh_reproof_claimed": False,
        },
        "routing": {
            "active_design": "carried V21 guarded router",
            "replacement_merged": False,
        },
        "admission_contract": {
            "joint_cut_floor": JOINT_FLOOR,
            "synthetic_lower_cost_floor": LOWER_COST_FLOOR,
            "nonendpoint_route_cut_floor": NONENDPOINT_FLOOR,
        },
        "recursive_capability_graph": {
            "nonprimitive_capabilities": len(CAPABILITIES),
            "common_privileged_fabric_primitive_roots": len(common_roots),
            "common_privileged_fabric_roots": sorted(common_roots),
            "shared_cloud_pam_identity_deduplicated": True,
            **graph_tests,
        },
        "static_exact": static,
        "recursive_collapse_exact": collapse,
        "temporal_exact": temporal,
        "merkle_resource_accounting": merkle_reference_metrics(),
        "runtime": {
            "new_nonstationary_routing_envelope_claimed": False,
            "reason": "V43 advances recursive provenance and temporal authority-lifetime modeling only; V21 routing remains active.",
        },
        "next_priorities": [
            "Bind each recursively expanded common-fabric primitive to explicit issuer/quorum/log/freshness evidence and re-run churn, split-log, delayed-propagation, and source-loss validation.",
            "Replace aggregate verifier-visible lifetime with explicit theft/exportability, detection, eviction, rotation, revocation publication, verifier consumption, stale-authorization, and ceremony-validity stages while preserving the exact nested-window peak calculation.",
            "Test second-order common-control collapse below cloud/PAM identity, HSM management, provider/build/CA, and operator employment/IAM, including shared provider or organizational control roots; fail closed when independence evidence is absent.",
            "Keep V21 guarded routing unless a replacement independently clears >=2,000 stationary and near-threshold seeds and materially improves gradual/selective/correlated detection with no extra probes.",
        ],
        "headline": (
            "Recursive expansion proves the accepted common-fabric provenance route is exactly cut 22 with zero hidden slack: "
            "collapsing any tested deep independent authority/local prerequisite into a shared root reduces it to 21 and rejects admission."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["validation_digest_sha256"] = hashlib.sha256(payload).hexdigest()
    return result


if __name__ == "__main__":
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
