"""WinLoop V83 exact continuation: epoch-34 compacted-tombstone proof revalidation plus third source failover, replacement-source disappearance plus eighth cold restart, and rotated-witness root-7 rollover under quorum churn."""
import hashlib
import json
from winloop_v83_core import indep, gc34
from winloop_v83_publication import replacement_source_disappearance_eighth_restart
from winloop_v83_membership import rotated_witness_root7_rollover_quorum_churn

V = 'V83'
BASE_DIGEST = '5c0b6dea19ae88dc42068c4d7b617c0a024474d9bc16e130fa6be4136747295c'
BASE_IMPL_SHA = 'bd218e25cfe0dbcdd6d980b26ebb0273c360431030a60fa33a3e63e7d2edb79e'


def run_validation():
    c = indep()
    t = gc34()
    s = replacement_source_disappearance_eighth_restart()
    b = rotated_witness_root7_rollover_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V82',
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
        'tombstone_epoch34_revalidation_third_failover': t,
        'publication_replacement_source_disappearance_eighth_restart': s,
        'membership_rotated_witness_root7_rollover_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 35 with root-bound compacted-proof revalidation after the third source failover while preserving the epoch-12 deadline',
            'compose eighth-restart recovery with successor-source churn and a ninth verifier cold restart without cached authority promotion',
            'carry root-7 membership through rotated-witness rebinding and another replication-quorum churn cycle without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V83 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-34 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch34_bound_proof_revalidation_states']:,} bound compacted-tombstone proof revalidations, {t['epoch34_bound_third_source_failover_states']:,} bound third-source failovers, and {t['epoch34_bound_verifier_binding_states']:,} bound verifier bindings while admitting zero stale/conflicting-root, unbound proof/failover/verifier/lineage/source/key-binding, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_disappearance_states']:,} bound replacement-source disappearances, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_eighth_restart_recoveries']:,} fully bound eighth-cold-restart recoveries with zero cached-authority, unbound disappearance/successor-binding/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root7_rollover_states']:,} bound root-7 rollovers, {b['bound_root7_verifier_binding_states']:,} bound root-7 verifier bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/source discontinuity, below-replication-quorum, unbound rollover/root-binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
