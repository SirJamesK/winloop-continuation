"""WinLoop V97 exact continuation: epoch-48 tenth-source handoff, twenty-second cold restart, and root-13 witness rebind."""
import hashlib
import json
from winloop_v97_core import indep, gc48
from winloop_v97_publication import successor_disappearance_twenty_second_restart
from winloop_v97_membership import root13_witness_rebind_quorum_churn

V = 'V97'
BASE_DIGEST = '5b5719a56d2c3a6469e499966eafd9e5e3db0df04140084c489fc03a739dac90'
BASE_IMPL_SHA = '659e05188ca0fdd1e4146b4539f2bee73c6e67de0c6ac41331903d2fe543e559'


def run_validation():
    c = indep()
    t = gc48()
    s = successor_disappearance_twenty_second_restart()
    b = root13_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V96',
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
        'tombstone_epoch48_tenth_source_handoff_binding': t,
        'publication_successor_disappearance_twenty_second_restart': s,
        'membership_root13_witness_rebind_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 49 by rotating and binding the tenth-source lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose twenty-second-restart recovery with replacement-source churn and a twenty-third verifier cold restart without cached authority promotion',
            'carry root 13 through witness-source replacement and root-14 rollover without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V97 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-48 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch48_bound_tenth_source_handoff_states']:,} bound tenth-source handoffs, {t['epoch48_bound_tenth_source_binding_states']:,} bound tenth-source bindings, and {t['epoch48_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound handoff/source/verifier/lineage/proof/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_twenty_second_restart_recoveries']:,} fully bound twenty-second-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root13_witness_rebind_states']:,} bound root-13 witness rebinds, {b['bound_root13_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement/prior-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
