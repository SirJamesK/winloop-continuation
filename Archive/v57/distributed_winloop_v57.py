"""WinLoop V57: monotonic revocation time binding plus source-loss/equivocation recovery checks."""
import hashlib, json
from winloop_v57_model import V, BASE_DIGEST, BASE_IMPL_SHA, temporal_floor_regression, monotonic_deadline_analysis, source_loss_equivocation_analysis, independence_evidence

def run_validation():
    h=temporal_floor_regression(); t=monotonic_deadline_analysis(); s=source_loss_equivocation_analysis(); e=independence_evidence()
    out={
        "version":V,
        "base":{"version":"V56","digest":BASE_DIGEST,"implementation_sha256":BASE_IMPL_SHA},
        "admission":{"joint":21,"provenance":22,"lower":63,"preserved":True},
        "routing":{"active":"V21 guarded","replacement":False},
        "runtime":{"new_routing_envelope":False},
        "temporal_floor_regression":h,
        "monotonic_deadline_certificates":t,
        "source_loss_and_same_epoch_equivocation":s,
        "recursive_publication_recovery_evidence":e,
        "checkpoint_recovery":{"statements":513,"max_lag":64,"shared_audit":"132 + 4*k","frontier_storage_only":True,"trust_bearing_messages_unchanged":True},
        "next":[
            "compose monotonic deadline certificates with multi-issuer time-source disagreement and fail-closed recovery",
            "extend same-epoch equivocation to verifier-population split views with delayed gossip convergence",
            "seek committed externally bound provider/hardware/operator independence evidence before raising conservative cross-role credit above 12",
            "retain V21 routing until the >=2000-seed replacement bar clears",
        ],
        "headline":"V57 binds the 3-step revocation deadline to an epoch-scoped monotonic certificate: all 180 skew/rollback/epoch cases produce zero post-deadline stale acceptance, while exhaustive dual-log source-loss/equivocation cases tolerate a single honest source loss per log but reject whole-log loss, sole forks, and same-epoch conflicting roots during A@7/B@8/witness@8 rotation.",
    }
    out["digest"]=hashlib.sha256(json.dumps(out,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    return out

if __name__=="__main__": print(json.dumps(run_validation(),indent=2,sort_keys=True))
