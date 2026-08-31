"""WinLoop V88 exact continuation: epoch-39 fifth-lineage rotation plus compacted-proof rebind, replacement-source churn plus thirteenth cold restart, and rebound-witness source replacement through root-9 rollover."""
import hashlib
import json
from winloop_v88_core import indep, gc39
from winloop_v88_publication import replacement_churn_thirteenth_restart
from winloop_v88_membership import root9_rollover_after_rebound_witness_replacement

V = 'V88'
BASE_DIGEST = '0429debf7ce2f300b49d31a608be562c0655c42ef652fb27e072a0b150f03145'
BASE_IMPL_SHA = '8e6d7b5d8c170d4f5a8933f7151cda153ff4392597c7e0a16fc0265c05e4c660'


def run_validation():
    c = indep()
    t = gc39()
    s = replacement_churn_thirteenth_restart()
    b = root9_rollover_after_rebound_witness_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V87',
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
        'tombstone_epoch39_fifth_lineage_compacted_proof_rebind': t,
        'publication_replacement_churn_thirteenth_restart': s,
        'membership_rebound_witness_replacement_root9_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 40 by handing the rebound fifth-source proof to a sixth source and binding that source while preserving the epoch-12 deadline',
            'compose thirteenth-restart recovery with successor-source disappearance and a fourteenth verifier cold restart without cached authority promotion',
            'carry the root-9 membership through witness rebind and another quorum-churn cycle without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V88 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-39 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch39_bound_fifth_lineage_rotation_states']:,} bound fifth-lineage rotations, {t['epoch39_bound_compacted_proof_rebind_states']:,} bound compacted-proof rebinds, and {t['epoch39_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound lineage/proof/verifier/source/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_thirteenth_restart_recoveries']:,} fully bound thirteenth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root9_rollover_states']:,} bound root-9 rollovers, {b['bound_root9_binding_states']:,} bound root-9 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
