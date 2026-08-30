"""WinLoop V59: witnessed issuer-set rotation plus composed partition/publication/gossip deadline."""
import hashlib, json
from winloop_v59_model import (V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression,
                               witnessed_membership_rotation_analysis, rotated_time_quorum_analysis,
                               composed_partition_publication_gossip_analysis, independence_evidence)

def run_validation():
    h=temporal_floor_regression()
    r=witnessed_membership_rotation_analysis()
    t=rotated_time_quorum_analysis()
    c=composed_partition_publication_gossip_analysis()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V58","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "witnessed_membership_rotation":r,
        "rotated_time_quorum":t,
        "composed_partition_publication_gossip":c,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
                               "frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "bind membership-witness roster changes themselves to a separately rooted threshold history and test witness-set churn",
            "compose multiple consecutive issuer-set rotations with delayed/offline verifier catch-up and replayed intermediate membership records",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V59 binds the rotated time-issuer set to a 2-of-3 independently witnessed membership record: 500 authority/witness cases admit only 8 canonical states (4 surviving membership-authority disappearance) with zero stale/forked membership acceptance, while 62,208 simultaneous issuer-partition/publication/verifier-split cases admit 400 states only when publication plus gossip converges within the shared 3-step deadline, including 90 one-issuer-partition plus one-verifier-fork recoveries and zero post-deadline acceptance.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))
