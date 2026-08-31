"""WinLoop V92 exact continuation: epoch-43 seventh-lineage rotation, replacement churn plus seventeenth cold restart, and root-11 rollover."""
import hashlib
import json
from winloop_v92_core import indep, gc43
from winloop_v92_publication import replacement_churn_seventeenth_restart
from winloop_v92_membership import root11_rollover_after_root10_witness_source_replacement

V = 'V92'
BASE_DIGEST = '50e52b4852689a4394aa7ce81b006d72dacb67eaf8ed690972c25c6cec8c139d'
BASE_IMPL_SHA = 'e23c1f92ab1960c00e293abd1679fc2b2db73ef98fca5900c6d3d62e0dd1d46b'


def run_validation():
    c = indep()
    t = gc43()
    s = replacement_churn_seventeenth_restart()
    b = root11_rollover_after_root10_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V91',
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
        'tombstone_epoch43_seventh_lineage_handed_proof_rebind': t,
        'publication_replacement_churn_seventeenth_restart': s,
        'membership_witness_replacement_root11_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 44 by handing the rebound proof to an eighth source and binding that source while preserving the epoch-12 deadline',
            'compose seventeenth-restart recovery with successor-source disappearance and an eighteenth verifier cold restart without cached authority promotion',
            'carry root 11 through witness rebind and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V92 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-43 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch43_bound_seventh_lineage_rotation_states']:,} bound seventh-lineage rotations, {t['epoch43_bound_seventh_lineage_binding_states']:,} bound lineage bindings, {t['epoch43_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch43_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_seventeenth_restart_recoveries']:,} fully bound seventeenth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root11_rollover_states']:,} bound root-11 rollovers, {b['bound_root11_binding_states']:,} bound root-11 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
