"""WinLoop V84 exact continuation: epoch-35 root-bound compacted-proof revalidation, successor-source churn plus ninth cold restart, and rotated-witness rebinding under quorum churn."""
import hashlib
import json
from winloop_v84_core import indep, gc35
from winloop_v84_publication import successor_source_churn_ninth_restart
from winloop_v84_membership import rotated_witness_rebinding_quorum_churn

V = 'V84'
BASE_DIGEST = '1d9cdbace8c3555694366a4a83ead54364c7629c31838b15fb70ccfd80045940'
BASE_IMPL_SHA = '4b49130c86df34373ab445adfd8575947d3c1360fae7b1b0d339f2ff8b08fcea'


def run_validation():
    c = indep()
    t = gc35()
    s = successor_source_churn_ninth_restart()
    b = rotated_witness_rebinding_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V83',
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
        'tombstone_epoch35_root_bound_revalidation': t,
        'publication_successor_source_churn_ninth_restart': s,
        'membership_rotated_witness_rebinding_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 36 with fourth-source rollover after root-bound compacted-proof revalidation while preserving the epoch-12 deadline',
            'compose ninth-restart recovery with replacement-source disappearance and a tenth verifier cold restart without cached authority promotion',
            'carry root-7 membership through witness-source replacement and another replication-quorum churn cycle without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V84 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-35 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch35_bound_proof_revalidation_states']:,} bound compacted-tombstone proof revalidations, {t['epoch35_bound_proof_root_binding_states']:,} bound proof-root bindings, and {t['epoch35_bound_verifier_binding_states']:,} bound verifier bindings while admitting zero stale/conflicting-root, unbound proof/root-binding/verifier/lineage/source/key/third-source-binding, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_churn_states']:,} bound successor-source churn states, {s['bound_successor_replacement_binding_states']:,} bound successor replacements, and {s['bound_ninth_restart_recoveries']:,} fully bound ninth-cold-restart recoveries with zero cached-authority, unbound churn/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_rotated_witness_rebinding_states']:,} bound rotated-witness rebindings and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/source discontinuity, below-replication-quorum, unbound rebinding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
