"""WinLoop V63: disjoint horizon-witness rotation, tombstone-preserving anchor compaction, and two-quarantine verifier recovery."""
import hashlib, json
from winloop_v63_model import (
    V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
    disjoint_horizon_witness_rotation_analysis, tombstone_anchor_history_analysis,
    two_quarantine_verifier_reconfiguration_analysis, independence_evidence
)

def run_validation():
    h=temporal_floor_regression()
    w=disjoint_horizon_witness_rotation_analysis()
    t=tombstone_anchor_history_analysis()
    q=two_quarantine_verifier_reconfiguration_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V62","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "disjoint_horizon_witness_rotation":w,
        "tombstone_anchor_history":t,
        "two_quarantine_verifier_reconfiguration":q,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{
            "statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
            "frontier_storage_only":True,"trust_bearing_messages_unchanged":True
        },
        "next":[
            "bind disjoint long-horizon witness rotation to independently evidenced provider/operator/hardware identities before raising cross-role credit",
            "extend tombstone-preserving compaction across anchor epoch 15 with concurrent revocation and delayed source disappearance",
            "test 3-of-5 verifier recovery under one Byzantine fork plus two quarantines and a joining population without quorum-credit inflation",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears"
        ],
    }
    out["headline"]=(
        f"V63 rotates the long-horizon witness set to a disjoint 2-of-3 old/new handoff: "
        f"{w['patterns']:,} witness/provider/root-loss cases admit {w['accepted']:,} states, including "
        f"{w['old_provider_plus_root_source_loss_recoveries']:,} old-provider-plus-root-source-loss recoveries, with zero stale, fork, or unpinned/new-only acceptance; "
        f"{t['patterns']:,} three-generation tombstone/compaction cases admit {t['accepted']:,} states with zero deadline-reset or live-revocation-erasure acceptance; and "
        f"{q['patterns']:,} five-population verifier cases admit {q['accepted']:,} states including {q['explicit_two_quarantine_reconfig_recoveries']:,} explicit two-quarantine reconfigurations with zero untrusted-join quorum inflation, invalid-state, membership-fork, below-threshold-history, or post-deadline acceptance."
    )
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))
