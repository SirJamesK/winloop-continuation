"""WinLoop V91 exact continuation: epoch-42 seventh-source handoff, successor disappearance plus sixteenth cold restart, and root-10 witness rebind."""
import hashlib
import json
from winloop_v91_core import indep, gc42
from winloop_v91_publication import successor_disappearance_sixteenth_restart
from winloop_v91_membership import root10_witness_rebind_quorum_churn

V = 'V91'
BASE_DIGEST = 'c929ba9482320badd2fc31a8592f7cbe5403666fa47a57dbb54d8a82ceaba3cb'
BASE_IMPL_SHA = 'e5f4f9c2a1c557e9c104a77be9443a6e67a9f3fa89c327e38cf8e29a847258b4'


def run_validation():
    c = indep()
    t = gc42()
    s = successor_disappearance_sixteenth_restart()
    b = root10_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V90',
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
        'tombstone_epoch42_seventh_source_handoff_binding': t,
        'publication_successor_disappearance_sixteenth_restart': s,
        'membership_root10_witness_rebind_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 43 by rotating and binding the seventh-source lineage and rebinding the handed proof while preserving the epoch-12 deadline',
            'compose sixteenth-restart recovery with replacement-source churn and a seventeenth verifier cold restart without cached authority promotion',
            'carry root 10 through witness-source replacement and root-11 rollover without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V91 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-42 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch42_bound_seventh_source_handoff_states']:,} bound seventh-source handoffs, {t['epoch42_bound_seventh_source_binding_states']:,} bound seventh-source bindings, and {t['epoch42_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound handoff/source/verifier/lineage/proof/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_sixteenth_restart_recoveries']:,} fully bound sixteenth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root10_witness_rebind_states']:,} bound root-10 witness rebinds, {b['bound_root10_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement/prior-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
