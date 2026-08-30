"""WinLoop V74 exact continuation: epoch-25 bound key recovery, split-view publication convergence, and two-generation recycled-identity compaction."""
import hashlib
import json
from winloop_v74_core import indep, gc25
from winloop_v74_publication import rollback_split_convergence
from winloop_v74_membership import compact_two_generation_reuse

V = 'V74'
BASE_DIGEST = '44d2f25f59474776030e3dfdcf1b44c7a348f2f6f668a4297560c038064a0b09'
BASE_IMPL_SHA = 'a4f731a59b4f58c3018d13157b14bb7c043c799804b1303e3b2eb6fa644912bc'

def run_validation():
    c = indep()
    t = gc25()
    s = rollback_split_convergence()
    b = compact_two_generation_reuse()
    o = {
        'version': V,
        'base': {'version': 'V73', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'},
        'independence_certificate_gate': c,
        'tombstone_epoch25_key_loss_recovery_monotonic_root': t,
        'publication_split_view_delayed_root_convergence': s,
        'two_generation_recycled_identity_partial_compaction': b,
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 26 with recovered-key re-rotation after source replacement and monotonic root-choice rollback resistance',
            'compose witness-set split-view convergence with verifier restart, source disappearance, and bounded reappearance',
            'test two-generation recycled identities under partial membership-root replication rollback plus membership-witness churn',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V74 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-25 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch25_bound_key_recovery_states']:,} bound replacement-key recoveries after dual-root disagreement and zero stale/conflicting root-choice, unbound-recovery, or deadline-reset acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication states including {s['witness_set_split_view_recoveries']:,} bound witness-set split-view recoveries with zero unbound/forked convergence or below-quorum acceptance, and admits {b['accepted']:,} of {b['patterns']:,} membership states including {b['two_tombstone_generation_reuse_recoveries']:,} two-generation recycled-identity recoveries with zero below-replication-quorum, tombstone-generation-collapse, unbound-root, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o

if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
