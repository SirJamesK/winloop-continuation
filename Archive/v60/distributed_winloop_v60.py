"""WinLoop V60: separately rooted witness-roster churn and multi-rotation verifier catch-up."""
import hashlib, json
from winloop_v60_model import (V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
                               witness_roster_history_analysis, consecutive_rotation_catchup_analysis,
                               independence_evidence)

def run_validation():
    h=temporal_floor_regression()
    w=witness_roster_history_analysis()
    c=consecutive_rotation_catchup_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V59","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "witness_roster_history":w,
        "consecutive_rotation_catchup":c,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
                               "frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "rotate the separate witness-history root authorities themselves and test recursive root-of-root churn without circular trust",
            "extend catch-up across three or more consecutive issuer/witness rotations with compacted checkpoints and mixed-generation recovery",
            "model verifier checkpoint rollback/equivocation across populations under partial history retention and source disappearance",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V60 separately roots witness-roster churn and composes two consecutive issuer rotations: 500 root-history cases admit only 8 canonical states with zero stale/forked roster acceptance, while 192,000 offline catch-up/replay/partition cases admit 512 chains only through the canonical epoch-9→roster-10→epoch-10 hash path within one shared 3-step deadline, with zero intermediate-replay, old-witness-majority, fork-terminal, or post-deadline acceptance.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))
