"""WinLoop V81 exact continuation: epoch-32 verifier-bound old-key tombstone consumption after second failover, rollback-source disappearance plus sixth cold restart, and witness rotation/root-6 rollover under quorum churn."""
import hashlib
import json
from winloop_v81_core import indep, gc32
from winloop_v81_publication import rollback_source_disappearance_sixth_restart
from winloop_v81_membership import witness_rotation_root6_rollover_quorum_churn

V = 'V81'
BASE_DIGEST = 'fd2fe31eeaa0047f7e320b03fa73305d5a546d310a886996e425079b24fae8ee'
BASE_IMPL_SHA = '4a82699b7830cbb1fb63fd409736654c486611582e1f26b9e1653a7bf22fcc1a'


def run_validation():
    c = indep()
    t = gc32()
    s = rollback_source_disappearance_sixth_restart()
    b = witness_rotation_root6_rollover_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V80',
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
        'tombstone_epoch32_second_failover_verifier_bound_consumption': t,
        'publication_rollback_source_disappearance_sixth_restart': s,
        'membership_witness_rotation_root6_rollover_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 33 with verifier-bound tombstone compaction and reissued-key rotation after second-failover consumption while preserving the epoch-12 deadline',
            'compose sixth-restart recovery with replacement-source rollback and a seventh verifier cold restart without cached authority promotion',
            'carry root-6 rollover through rotated-witness source replacement and another replication-quorum churn cycle without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V81 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-32 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch32_bound_second_source_failover_states']:,} bound second-failover states, {t['epoch32_bound_verifier_binding_states']:,} bound verifier bindings, and {t['epoch32_bound_old_key_tombstone_consumption_states']:,} bound old-key tombstone consumptions while admitting zero stale/conflicting-root, unbound failover/verifier-binding/consumption/lineage/source-binding, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_rollback_source_disappearance_states']:,} bound rollback-source disappearances and {s['bound_sixth_restart_recoveries']:,} fully bound sixth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement-binding/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_rotation_states']:,} bound witness-rotation states, {b['bound_root6_rollover_states']:,} bound root-6 rollover states, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness discontinuity, below-replication-quorum, unbound rotation/rollover/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
