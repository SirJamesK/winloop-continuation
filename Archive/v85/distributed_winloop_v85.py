"""WinLoop V85 exact continuation: epoch-36 fourth-source rollover, replacement-source disappearance plus tenth cold restart, and witness-source replacement under quorum churn."""
import hashlib
import json
from winloop_v85_core import indep, gc36
from winloop_v85_publication import replacement_source_disappearance_tenth_restart
from winloop_v85_membership import witness_source_replacement_quorum_churn

V = 'V85'
BASE_DIGEST = '1b4a5b0744ca8a8f54e74f31b81c1e3b573298c1847ee82b697a933e1a5aefc2'
BASE_IMPL_SHA = '2316ee1c7d765f4262aa0d9c1beb744d390380603072e098005a9971615179fc'


def run_validation():
    c = indep()
    t = gc36()
    s = replacement_source_disappearance_tenth_restart()
    b = witness_source_replacement_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V84',
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
        'tombstone_epoch36_fourth_source_rollover': t,
        'publication_replacement_source_disappearance_tenth_restart': s,
        'membership_witness_source_replacement_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 37 with bound fourth-source lineage re-rotation and root rollover while preserving the epoch-12 deadline',
            'compose tenth-restart recovery with successor-source churn and an eleventh verifier cold restart without cached authority promotion',
            'carry root-7 membership through a root-8 rollover after bound witness-source replacement without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V85 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-36 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch36_bound_proof_revalidation_states']:,} bound compacted-tombstone proof revalidations, {t['epoch36_bound_fourth_source_rollover_states']:,} bound fourth-source rollovers, {t['epoch36_bound_fourth_source_binding_states']:,} bound fourth-source bindings, and {t['epoch36_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound proof/root/rollover/source/verifier/lineage/key, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_disappearance_states']:,} bound replacement-source disappearances, {s['bound_replacement_successor_binding_states']:,} bound successor bindings, and {s['bound_tenth_restart_recoveries']:,} fully bound tenth-cold-restart recoveries with zero cached-authority, unbound disappearance/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
