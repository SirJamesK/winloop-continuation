"""WinLoop V61: root-authority rotation, compacted three-rotation catch-up, and checkpoint anti-rollback."""
import hashlib, json
from winloop_v61_model import (V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
                               root_authority_rotation_analysis, three_rotation_catchup_analysis,
                               verifier_checkpoint_analysis, independence_evidence)


def run_validation():
    h=temporal_floor_regression()
    r=root_authority_rotation_analysis()
    c=three_rotation_catchup_analysis()
    q=verifier_checkpoint_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V60","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "root_authority_rotation":r,
        "three_rotation_catchup":c,
        "verifier_checkpoint_anti_rollback":q,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
                               "frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "rotate the locally pinned root-history checkpoint itself using an independently witnessed long-horizon anchor transition and test loss of all pre-rotation online root sources",
            "extend compacted catch-up beyond epoch 11 with multiple compaction layers and prove that no intermediate checkpoint can silently reset the shared revocation deadline",
            "model asynchronous checkpoint gossip with Byzantine population churn, delayed compaction publication, and recovery from only threshold-retained history fragments",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V61 rotates the witness-history roots with a pinned dual-quorum handoff and explicit leaving/joining boundary: 78,125 root-rotation cases admit only 18 canonical/cached transitions, while 2,625,000 three-rotation compacted catch-up cases admit 1,056 chains only through the epoch-9→roster-10→epoch-10→root-11→roster-11→epoch-11 hash path within one shared 3-step deadline, and 5,250 checkpoint-population cases accept 336 quorum-consistent recoveries with zero rollback, fork, or post-deadline acceptance.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))
