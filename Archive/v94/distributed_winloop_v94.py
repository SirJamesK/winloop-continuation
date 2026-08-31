"""WinLoop V94 exact continuation: epoch-45 eighth-lineage rotation, replacement churn plus nineteenth cold restart, and root-12 rollover."""
import hashlib
import json
from winloop_v94_core import indep, gc45
from winloop_v94_publication import replacement_churn_nineteenth_restart
from winloop_v94_membership import root12_rollover_after_root11_witness_source_replacement

V = 'V94'
BASE_DIGEST = '2c920279f12e75debfe52649e41fdd83a072b929d88ad66facecd1719b7877ff'
BASE_IMPL_SHA = '864efa8cf146e104218e60404a4709b5a40094bbebf4318836e8915df363b03b'


def run_validation():
    c = indep()
    t = gc45()
    s = replacement_churn_nineteenth_restart()
    b = root12_rollover_after_root11_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V93',
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
        'tombstone_epoch45_eighth_lineage_handed_proof_rebind': t,
        'publication_replacement_churn_nineteenth_restart': s,
        'membership_witness_replacement_root12_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 46 by handing the rebound proof to a ninth source, binding that source, and preserving the epoch-12 deadline',
            'compose nineteenth-restart recovery with successor-source disappearance and a twentieth verifier cold restart without cached authority promotion',
            'carry root 12 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V94 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-45 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch45_bound_eighth_lineage_rotation_states']:,} bound eighth-lineage rotations, {t['epoch45_bound_eighth_lineage_binding_states']:,} bound lineage bindings, {t['epoch45_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch45_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_nineteenth_restart_recoveries']:,} fully bound nineteenth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root12_rollover_states']:,} bound root-12 rollovers, {b['bound_root12_binding_states']:,} bound root-12 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
