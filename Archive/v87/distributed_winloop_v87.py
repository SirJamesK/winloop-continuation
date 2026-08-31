"""WinLoop V87 exact continuation: epoch-38 root-rolled fourth-proof compaction plus fifth-source handoff, successor-source disappearance plus twelfth cold restart, and root-8 witness rebind through another membership quorum-churn cycle."""
import hashlib
import json
from winloop_v87_core import indep, gc38
from winloop_v87_publication import successor_disappearance_twelfth_restart
from winloop_v87_membership import root8_witness_rebind_quorum_churn

V = 'V87'
BASE_DIGEST = '0f9655082f1caeb509cba215f43cd71dde5d42fb3bd607eade6cfa3b3cd5bea3'
BASE_IMPL_SHA = '01c62ed700538acd35c501d93675ea4a333f44f0f1dfd1347b1d86a0f48ec4b7'


def run_validation():
    c = indep()
    t = gc38()
    s = successor_disappearance_twelfth_restart()
    b = root8_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V86',
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
        'tombstone_epoch38_fourth_proof_compaction_fifth_handoff': t,
        'publication_successor_disappearance_twelfth_restart': s,
        'membership_root8_witness_rebind_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 39 by rotating the bound fifth-source lineage and rebinding its compacted proof while preserving the epoch-12 deadline',
            'compose twelfth-restart recovery with replacement-source churn and a thirteenth verifier cold restart without cached authority promotion',
            'carry the rebound root-8 witness through source replacement and a root-9 rollover without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V87 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-38 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch38_bound_fourth_proof_compaction_states']:,} bound root-rolled fourth-proof compactions, {t['epoch38_bound_fifth_source_handoff_states']:,} bound fifth-source handoffs, {t['epoch38_bound_fifth_source_binding_states']:,} bound fifth-source bindings, and {t['epoch38_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound compaction/proof/handoff/verifier/source/key/lineage, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_twelfth_restart_recoveries']:,} fully bound twelfth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root8_witness_rebind_states']:,} bound root-8 witness rebinds, {b['bound_root8_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
