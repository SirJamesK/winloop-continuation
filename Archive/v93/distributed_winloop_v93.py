"""WinLoop V93 exact continuation: epoch-44 eighth-source handoff, successor disappearance plus eighteenth cold restart, and root-11 witness rebind."""
import hashlib
import json
from winloop_v93_core import indep, gc44
from winloop_v93_publication import successor_disappearance_eighteenth_restart
from winloop_v93_membership import root11_witness_rebind_quorum_churn

V = 'V93'
BASE_DIGEST = '16397218b4eb268e2a3ac0dc41be627f8df093ca8285ea129ac91d44d4b6f810'
BASE_IMPL_SHA = '5199ab84663bbbbfd90f6c6c6a59e0bc96867805f26b236d69d23a93b014c907'


def run_validation():
    c = indep()
    t = gc44()
    s = successor_disappearance_eighteenth_restart()
    b = root11_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V92',
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
        'tombstone_epoch44_eighth_source_handoff_binding': t,
        'publication_successor_disappearance_eighteenth_restart': s,
        'membership_root11_witness_rebind_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 45 by rotating and binding the eighth-source lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose eighteenth-restart recovery with replacement-source churn and a nineteenth verifier cold restart without cached authority promotion',
            'carry root 11 through witness-source replacement, root-12 rollover, root binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V93 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-44 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch44_bound_eighth_source_handoff_states']:,} bound eighth-source handoffs, {t['epoch44_bound_eighth_source_binding_states']:,} bound eighth-source bindings, and {t['epoch44_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound handoff/source/verifier/lineage/proof/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_eighteenth_restart_recoveries']:,} fully bound eighteenth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root11_witness_rebind_states']:,} bound root-11 witness rebinds, {b['bound_root11_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement/prior-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
