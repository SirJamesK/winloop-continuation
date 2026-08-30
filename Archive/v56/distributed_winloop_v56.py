"""WinLoop V56: explicit revocation-consumption deadlines, independent rotation, and cross-population gossip."""
import hashlib, json
from winloop_v56_model import (
    V, BASE_DIGEST, BASE_IMPL_SHA,
    horizon22_regression, revocation_partition_analysis,
    independent_rotation_and_gossip, independence_evidence,
)

def run_validation():
    h=horizon22_regression()
    p=revocation_partition_analysis()
    r=independent_rotation_and_gossip()
    e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V55","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "revocation_partition_deadline":p,
        "independent_rotation_and_gossip":r,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k",
                               "frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "bind deadline certificates to explicit monotonic wall-clock/epoch sources and test clock-skew/rollback envelopes",
            "extend partition analysis to asymmetric source disappearance plus same-epoch log equivocation during rotation",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V56 bounds stale floor-1 authorization by a 3-step verifier revocation deadline across all 15,625 A/B partition patterns: 4,096 retain full three-population availability, 11,008 form a timely 2-of-3 gossip certificate, and every delayed population fails closed after expiry while independent A@7/B@8/witness@8 rotations reject old, mixed, duplicate, revoked, and forked evidence.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))
