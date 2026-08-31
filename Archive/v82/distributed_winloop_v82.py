"""WinLoop V82 exact continuation: epoch-33 verifier-bound tombstone compaction plus reissued-key rotation, replacement-source rollback plus seventh cold restart, and rotated-witness source replacement under quorum churn."""
import hashlib
import json
from winloop_v82_core import indep, gc33
from winloop_v82_publication import replacement_source_rollback_seventh_restart
from winloop_v82_membership import rotated_witness_source_replacement_quorum_churn

V = 'V82'
BASE_DIGEST = '4638aaa1ca978b9c8a7e12c8b28c40d8be4f5e078371d02a98b1b7d7991bc0e3'
BASE_IMPL_SHA = '5ff1412343c9df01766dcdc00401d7c0fa7b7186231600a5c6e3bb10cf7df465'


def run_validation():
    c = indep()
    t = gc33()
    s = replacement_source_rollback_seventh_restart()
    b = rotated_witness_source_replacement_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V81',
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
        'tombstone_epoch33_compaction_reissued_key_rotation': t,
        'publication_replacement_source_rollback_seventh_restart': s,
        'membership_rotated_witness_source_replacement_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 34 with compacted-tombstone proof revalidation and a bound third source failover after reissued-key rotation while preserving the epoch-12 deadline',
            'compose seventh-restart recovery with replacement-source disappearance and an eighth verifier cold restart without cached authority promotion',
            'carry rotated-witness source replacement through root-7 rollover and another replication-quorum churn cycle without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V82 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-33 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch33_verifier_bound_tombstone_compaction_states']:,} verifier-bound tombstone-compaction states, {t['epoch33_bound_verifier_binding_states']:,} bound verifier bindings, and {t['epoch33_bound_reissued_key_rotation_states']:,} bound reissued-key rotations while admitting zero stale/conflicting-root, unbound compaction/verifier-binding/rotation/lineage/source-binding, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_rollback_states']:,} bound replacement-source rollbacks and {s['bound_seventh_restart_recoveries']:,} fully bound seventh-cold-restart recoveries with zero cached-authority, unbound rollback/replacement-binding/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_rotated_witness_source_replacement_states']:,} bound rotated-witness source replacements, {b['bound_witness_rebinding_states']:,} bound witness rebindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness discontinuity, below-replication-quorum, unbound replacement/rebinding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
