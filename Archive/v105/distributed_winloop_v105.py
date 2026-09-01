"""WinLoop V105 exact continuation: epoch-56 fourteenth-source handoff, thirtieth cold restart, and root-17 witness rebind."""
import hashlib
import json
from winloop_v105_core import indep, gc56
from winloop_v105_publication import successor_disappearance_thirtieth_restart
from winloop_v105_membership import root17_witness_rebind_quorum_churn

V = 'V105'
BASE_DIGEST = '94102d09f48829cc3c34d00dfd1f936081c4dd040ac099af821d40aa5676c012'
BASE_IMPL_SHA = 'e45302c42c52d2eed16e9d42ee773def8dca1ad918bb60d1ff167895b2f38838'


def run_validation():
    c = indep()
    t = gc56()
    s = successor_disappearance_thirtieth_restart()
    b = root17_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V104',
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
        'tombstone_epoch56_fourteenth_source_handoff': t,
        'publication_successor_disappearance_thirtieth_restart': s,
        'membership_root17_witness_rebind': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 57 by rotating the fourteenth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose thirtieth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a thirty-first verifier cold restart without cached authority promotion',
            'carry root 17 through witness-source replacement, replacement-source binding, root-18 rollover and binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V105 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-56 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch56_bound_fourteenth_source_handoff_states']:,} bound fourteenth-source handoffs, {t['epoch56_bound_fourteenth_source_binding_states']:,} bound fourteenth-source bindings, and {t['epoch56_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound handoff/source/verifier/lineage/proof/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_thirtieth_restart_recoveries']:,} fully bound thirtieth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root17_witness_rebind_states']:,} bound root-17 witness rebinds, {b['bound_root17_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement/prior-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
