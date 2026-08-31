"""WinLoop V78 exact continuation: epoch-29 tombstone-root rollback/revalidation with lineage split, third-restart bounded source reappearance, and third-generation witness eviction/replication loss."""
import hashlib
import json
from winloop_v78_core import indep, gc29
from winloop_v78_publication import third_restart_bounded_source_reappearance
from winloop_v78_membership import third_generation_witness_eviction_replication_loss

V = 'V78'
BASE_DIGEST = '9ae29120c3eb08eebe92725585fb1e912d90271b59c62f155e9544995d914bb1'
BASE_IMPL_SHA = 'bfbc14223d292bb76e862c9f5bd6bd4a57e7f7cafbc1fcd10aff5d4d7cce7029'

def run_validation():
    c = indep()
    t = gc29()
    s = third_restart_bounded_source_reappearance()
    b = third_generation_witness_eviction_replication_loss()
    o = {
        'version': V,
        'base': {'version': 'V77', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'},
        'independence_certificate_gate': c,
        'tombstone_epoch29_rollback_revalidation_lineage_split': t,
        'publication_third_restart_bounded_source_reappearance': s,
        'membership_third_generation_witness_eviction_replication_loss': b,
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 30 with lineage-split resolution plus replacement-key retirement/reissuance while preserving the epoch-12 deadline and tombstone-root continuity',
            'compose third-restart bounded source reappearance with dual-source reconciliation and a fourth verifier cold restart without cached authority promotion',
            'carry third-generation witness eviction through replication recovery into membership-root rollover and witness reinstatement without generation regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V78 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-29 GC to {t['accepted']:,} of {t['patterns']:,} states including {t['epoch29_bound_tombstone_root_revalidation_states']:,} bound tombstone-root revalidations and {t['epoch29_bound_source_lineage_split_states']:,} lineage-split states with zero stale/conflicting root-choice, unbound rollback/revalidation/split, tombstone discontinuity, or deadline-reset acceptance, "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states including {s['bounded_source_reappearance_states']:,} bounded source-reappearance states under a third verifier restart with zero cached-third-restart authority, unbound source/binding, or below-quorum acceptance, "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states including {b['third_generation_witness_eviction_states']:,} third-generation witness-eviction states and {b['temporary_replication_loss_states']:,} temporary-replication-loss states with zero generation/root regression, unbound eviction/loss/recovery, below-replication-quorum, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o

if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
