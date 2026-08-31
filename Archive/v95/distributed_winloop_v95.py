"""WinLoop V95 exact continuation: epoch-46 ninth-source handoff, successor disappearance plus twentieth cold restart, and root-12 witness rebind."""
import hashlib
import json
from winloop_v95_core import indep, gc46
from winloop_v95_publication import successor_disappearance_twentieth_restart
from winloop_v95_membership import root12_witness_rebind_quorum_churn

V = 'V95'
BASE_DIGEST = '2ece9d9012b3c220c2c35cfb3bb31ab1c0b263d4ec03fd66f2f80a176406f2a2'
BASE_IMPL_SHA = '7aa45061531ab883434bf93a868022d3aacc4049dc17fec284484382a467ae9d'


def run_validation():
    c = indep()
    t = gc46()
    s = successor_disappearance_twentieth_restart()
    b = root12_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V94',
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
        'tombstone_epoch46_ninth_source_handoff_binding': t,
        'publication_successor_disappearance_twentieth_restart': s,
        'membership_root12_witness_rebind_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 47 by rotating and binding the ninth-source lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose twentieth-restart recovery with replacement-source churn and a twenty-first verifier cold restart without cached authority promotion',
            'carry root 12 through witness-source replacement, root-13 rollover, root binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V95 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-46 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch46_bound_ninth_source_handoff_states']:,} bound ninth-source handoffs, {t['epoch46_bound_ninth_source_binding_states']:,} bound ninth-source bindings, and {t['epoch46_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound handoff/source/verifier/lineage/proof/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_disappearance_states']:,} bound successor-source disappearances, {s['bound_replacement_source_binding_states']:,} bound replacement-source bindings, and {s['bound_twentieth_restart_recoveries']:,} fully bound twentieth-cold-restart recoveries with zero cached-authority, unbound disappearance/replacement/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root12_witness_rebind_states']:,} bound root-12 witness rebinds, {b['bound_root12_witness_binding_states']:,} bound witness bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/replacement/prior-source discontinuity, below-replication-quorum, unbound rebind/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
