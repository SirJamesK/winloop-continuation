"""WinLoop V106 exact continuation: epoch-57 fourteenth-lineage rotation, thirty-first cold restart, and root-18 rollover."""
import hashlib
import json
from winloop_v106_core import indep, gc57
from winloop_v106_publication import replacement_churn_thirty_first_restart
from winloop_v106_membership import root18_rollover_after_root17_witness_source_replacement

V = 'V106'
BASE_DIGEST = '75043a86bdeafbc42ac05e4fcf027d8d917da7af8945a0c47ce5c63a5b062c6b'
BASE_IMPL_SHA = 'ceffdfac9abe91537bd571aefa1bfcf626b72066200579d347aa34e25a7a5696'


def run_validation():
    c = indep()
    t = gc57()
    s = replacement_churn_thirty_first_restart()
    b = root18_rollover_after_root17_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V105',
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
        'tombstone_epoch57_fourteenth_lineage_rotation': t,
        'publication_replacement_churn_thirty_first_restart': s,
        'membership_root18_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 58 by handing the rebound proof to a fifteenth source, binding that source, and preserving the epoch-12 deadline',
            'compose thirty-first-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a thirty-second verifier cold restart without cached authority promotion',
            'keep generation 4 and root 18 fixed while rebinding the witness and requiring replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V106 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-57 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch57_bound_fourteenth_lineage_rotation_states']:,} bound fourteenth-lineage rotations, {t['epoch57_bound_fourteenth_lineage_binding_states']:,} bound lineage bindings, {t['epoch57_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch57_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_thirty_first_restart_recoveries']:,} fully bound thirty-first-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root18_rollover_states']:,} bound root-18 rollovers, {b['bound_root18_binding_states']:,} bound root-18 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
