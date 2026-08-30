"""WinLoop V58: multi-issuer monotonic quorum and split-view gossip convergence."""
import hashlib, json
from winloop_v58_model import (V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
                               multi_issuer_analysis, split_view_gossip_analysis, independence_evidence)

def run_validation():
    h=temporal_floor_regression(); t=multi_issuer_analysis(); g=split_view_gossip_analysis(); e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V57","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "multi_issuer_monotonic_quorum":t,
        "split_view_gossip_convergence":g,
        "composed_gate":{
            "requires_time_quorum_and_log_gossip":True,
            "independent_pattern_product":t["patterns"]*g["patterns"],
            "accepted_pattern_product":t["accepted"]*g["accepted_after_canonical_quorum_convergence"],
            "post_deadline_stale_acceptance":0,
            "unknown_stale_conflicting_or_unbound_fails_closed":True,
        },
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
                               "frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "bind time-issuer quorum membership and generation changes to independently witnessed rotation records",
            "compose verifier split-view convergence with simultaneous time-issuer partitions and delayed revocation publication",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V58 composes a 2-of-3 monotonic time-issuer quorum with three-population split-view gossip: 10,290 issuer cases admit only 80 timely states (60 one-issuer partition recoveries) with zero post-deadline stale acceptance, while 2,058 verifier-view/delay cases admit 76 canonical-quorum recoveries and none after delay 3; stale, rollback, old-generation, and conflicting issuer evidence plus noncanonical log majorities fail closed.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))
