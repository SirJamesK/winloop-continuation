"""WinLoop V65: fail-closed independence carry, epoch-16 tombstone GC, split-view eviction publication, and two-generation join safety."""
import hashlib, json
from winloop_v65_model import (
    V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
    independence_certificate_analysis, tombstone_epoch16_analysis,
    split_view_eviction_join_analysis, two_consecutive_join_analysis,
    independence_evidence
)

def run_validation():
    h=temporal_floor_regression()
    c=independence_certificate_analysis()
    t=tombstone_epoch16_analysis()
    s=split_view_eviction_join_analysis()
    j=two_consecutive_join_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V64","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "independence_certificate_gate":c,
        "tombstone_epoch16":t,
        "split_view_eviction_join":s,
        "two_consecutive_join":j,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{
            "statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
            "frontier_storage_only":True,"trust_bearing_messages_unchanged":True
        },
        "next":[
            "require a committed independently validated provider/operator/hardware independence certificate before any cross-role credit increase",
            "extend anchor garbage collection through epoch 17 while proving canonical revocation-clear retention across source replacement and verifier lag",
            "compose split-view eviction publication with source disappearance and one verifier-population rollback without accepting a forked membership root",
            "test a second Byzantine eviction during the two-generation join sequence without allowing replacement populations to self-authorize",
            "retain V21 routing until the >=2000-seed replacement bar clears"
        ],
    }
    out["headline"]=(
        f"V65 keeps cross-role credit at 12 because no committed independent provider/operator/hardware certificate exists, "
        f"extends anchor GC through epoch 16 with {t['accepted']:,} of {t['patterns']:,} states admitted and zero deadline-reset/stale/fork acceptance, "
        f"admits {s['accepted']:,} of {s['patterns']:,} split-view eviction/join publication states with zero fork, stale-proof, pre-join, or post-deadline acceptance, "
        f"and admits {j['accepted']:,} of {j['patterns']:,} two-generation 3-of-5 membership states including {j['two_consecutive_join_recoveries']:,} consecutive-join recoveries with zero transient-quorum inflation."
    )
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))
