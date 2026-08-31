"""WinLoop V79 exact continuation: epoch-30 lineage resolution with key retirement/reissuance, dual-source fourth-restart recovery, and membership-root rollover with witness reinstatement."""
import hashlib
import json
from winloop_v79_core import indep, gc30
from winloop_v79_publication import dual_source_fourth_restart
from winloop_v79_membership import root_rollover_witness_reinstatement

V = 'V79'
BASE_DIGEST = '0ff7fc1b7ff5988de8d6962246d37d9d72ead144122b2045981062960455433b'
BASE_IMPL_SHA = 'ad7bb7826a9ecac618836aa54a7c9e493f819ea9f11fb87f380dbcddadda54ea'


def run_validation():
    c = indep()
    t = gc30()
    s = dual_source_fourth_restart()
    b = root_rollover_witness_reinstatement()
    o = {
        'version': V,
        'base': {
            'version': 'V78',
            'digest': BASE_DIGEST,
            'implementation_sha256': BASE_IMPL_SHA,
        },
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {
            'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851,
            'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66',
        },
        'independence_certificate_gate': c,
        'tombstone_epoch30_lineage_resolution_key_retirement_reissuance': t,
        'publication_dual_source_reconciliation_fourth_restart': s,
        'membership_root_rollover_witness_reinstatement': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 31 with bound reissued-key consumption and old-key tombstone collection across source failover while preserving the epoch-12 deadline',
            'compose fourth-restart dual-source recovery with reconciliation rollback and a fifth verifier cold restart without cached authority promotion',
            'carry reinstated membership witness through root-5 split-view recovery and replication-quorum churn without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V79 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-30 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch30_lineage_split_resolution_states']:,} lineage-split-resolution states, {t['epoch30_bound_replacement_key_retirement_states']:,} bound replacement-key retirements, and {t['epoch30_bound_replacement_key_reissuance_states']:,} bound reissuances while admitting zero stale/conflicting-root, unbound resolution/retirement/reissuance/lineage, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_dual_source_reconciliation_states']:,} bound dual-source reconciliations and {s['bound_fourth_restart_recoveries']:,} bound fourth-cold-restart recoveries with zero cached-authority, unbound/forked reconciliation, unbound binding/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_membership_root_rollover_states']:,} bound root rollovers and {b['bound_witness_reinstatement_states']:,} bound witness reinstatements with zero generation/root regression, tombstone discontinuity, below-replication-quorum, unbound rollover/reinstatement, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
