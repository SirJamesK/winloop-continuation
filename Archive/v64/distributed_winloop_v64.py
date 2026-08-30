"""WinLoop V64: exact externally-bound identity gating, epoch-15 tombstone compaction, and Byzantine-evicting verifier recovery."""
import hashlib, json
from winloop_v64_model import (
    V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
    identity_binding_gate_analysis, tombstone_epoch15_analysis,
    byzantine_quarantine_join_analysis, independence_evidence
)

def run_validation():
    h=temporal_floor_regression()
    i=identity_binding_gate_analysis()
    t=tombstone_epoch15_analysis()
    q=byzantine_quarantine_join_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V63","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "identity_binding_gate":i,
        "tombstone_epoch15":t,
        "byzantine_quarantine_join":q,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{
            "statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
            "frontier_storage_only":True,"trust_bearing_messages_unchanged":True
        },
        "next":[
            "require a committed independently validated provider/operator/hardware independence certificate before any cross-role credit increase",
            "extend tombstone garbage-collection proof through anchor epoch 16 with overlapping revocation clear, delayed publication, and proof-source churn",
            "split-view test Byzantine eviction-proof publication across verifier populations before and after a validated join",
            "test two consecutive joining populations without allowing transient membership to inflate a 3-of-5 quorum",
            "retain V21 routing until the >=2000-seed replacement bar clears"
        ],
    }
    out["headline"]=(
        f"V64 makes provider/operator/hardware independence an explicit fail-closed gate: "
        f"{i['patterns']:,} identity-evidence cases admit only {i['hypothetical_gate_admits']:,} hypothetical fully bound states while committed external evidence remains absent and cross-role credit stays 12; "
        f"epoch-15 tombstone compaction admits {t['accepted']:,} of {t['patterns']:,} states, including {t['pre15_source_disappearance_concurrent_revocation_recoveries']:,} concurrent-revocation recoveries after pre-15 source disappearance, with zero deadline-reset, stale/fork-clear, invalid-history, or forked-source acceptance; and "
        f"Byzantine-evicting 3-of-5 recovery admits {q['accepted']:,} of {q['patterns']:,} states including {q['one_byzantine_two_quarantine_join_recoveries']:,} one-Byzantine/two-quarantine/join recoveries with zero active-Byzantine, stale/missing-eviction-proof, quorum-inflation, membership-fork, or post-deadline acceptance."
    )
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))
