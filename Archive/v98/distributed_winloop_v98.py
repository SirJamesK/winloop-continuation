"""WinLoop V98 exact continuation: epoch-49 tenth-lineage rotation, twenty-third cold restart, and root-14 rollover."""
import hashlib
import json
from winloop_v98_core import indep, gc49
from winloop_v98_publication import replacement_churn_twenty_third_restart
from winloop_v98_membership import root14_rollover_after_root13_witness_source_replacement

V = 'V98'
BASE_DIGEST = 'fbdc509251dde7057cd18fffc534f63e2bdb819e32bb5c516a1e5ba7b17fb4b2'
BASE_IMPL_SHA = 'c82fc5c1cb51eb78e500b3cd9f1d8bc67117f0e8a3d9616133e0e7c016f9c4ac'


def run_validation():
    c = indep()
    t = gc49()
    s = replacement_churn_twenty_third_restart()
    b = root14_rollover_after_root13_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V97',
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
        'tombstone_epoch49_tenth_lineage_handed_proof_rebind': t,
        'publication_replacement_churn_twenty_third_restart': s,
        'membership_witness_replacement_root14_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 50 by handing the rebound proof to an eleventh source, binding that source, and preserving the epoch-12 deadline',
            'compose twenty-third-restart recovery with successor-source disappearance and a twenty-fourth verifier cold restart without cached authority promotion',
            'carry root 14 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V98 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-49 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch49_bound_tenth_lineage_rotation_states']:,} bound tenth-lineage rotations, {t['epoch49_bound_tenth_lineage_binding_states']:,} bound lineage bindings, {t['epoch49_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch49_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_twenty_third_restart_recoveries']:,} fully bound twenty-third-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root14_rollover_states']:,} bound root-14 rollovers, {b['bound_root14_binding_states']:,} bound root-14 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
