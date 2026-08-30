"""WinLoop V75 exact continuation: epoch-26 key re-rotation, restart-bound source reappearance, and membership-root rollback/witness churn."""
import hashlib
import json
from winloop_v75_core import indep, gc26
from winloop_v75_publication import restart_loss_reappearance_convergence
from winloop_v75_membership import rollback_witness_churn_two_generation_reuse

V = 'V75'
BASE_DIGEST = 'b56ea2b452bf5d2ed56737d8b59a3bed6c4b2cd42e45a6f64c4bef3d55ae30cd'
BASE_IMPL_SHA = '32466596df72658d1f3c95369df372e586080205673c60e954f92a7e96b08d90'

def run_validation():
    c = indep()
    t = gc26()
    s = restart_loss_reappearance_convergence()
    b = rollback_witness_churn_two_generation_reuse()
    o = {
        'version': V,
        'base': {'version': 'V74', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'},
        'independence_certificate_gate': c,
        'tombstone_epoch26_recovered_key_rerotation_rollback_resistance': t,
        'publication_restart_source_loss_bounded_reappearance': s,
        'two_generation_membership_root_rollback_witness_churn': b,
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 27 with re-rotated-key loss/recovery and replacement-source lineage rollover without deadline reset',
            'compose bounded source reappearance with a second verifier restart and split witness-set rollback after reappearance',
            'test two-generation recycled identities through membership-root rollback recovery followed by a second witness-set churn generation',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V75 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-26 GC to {t['accepted']:,} of {t['patterns']:,} states including {t['epoch26_recovered_key_rerotation_states']:,} recovered-key re-rotation states after bound source replacement with zero stale/conflicting root-choice, unbound-source, unbound-re-rotation, or deadline-reset acceptance, admits {s['accepted']:,} of {s['patterns']:,} publication states including {s['bounded_source_reappearance_recoveries']:,} bounded source-reappearance recoveries across verifier restart and source disappearance with zero cached-restart, conflicting-loss, unbound/forked-reappearance, or below-quorum acceptance, and admits {b['accepted']:,} of {b['patterns']:,} membership states including {b['membership_witness_churn_recoveries']:,} partial-replication rollback/witness-churn recoveries with zero below-replication-quorum, unbound/conflicting-rollback, unbound/forked-witness, tombstone-generation-collapse, unbound-root, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o

if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
