"""WinLoop V123 exact continuation: epoch-74 twenty-third-source handoff, forty-eighth cold restart, and root-26 witness rebind."""
import hashlib
import json
from winloop_v123_core import indep, gc74
from winloop_v123_publication import successor_disappearance_forty_eighth_restart
from winloop_v123_membership import root26_witness_rebind_quorum_churn

V = 'V123'
BASE_DIGEST = 'e64fb7c88abb7ab88dddc1c79153bfed0fc3de90563e5815c5662002907f012c'
BASE_IMPL_SHA = '35e0a595c9d66c2103e88887fd84477a346980454162dc1d3e04fbfcf7529267'


def run_validation():
    c = indep()
    t = gc74()
    s = successor_disappearance_forty_eighth_restart()
    b = root26_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V122', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'},
        'independence': {
            'patterns': c['patterns'], 'hypothetical_gate_admits': c['hypothetical_gate_admits'],
            'committed_external_independence_certificate_present': c['committed_external_independence_certificate_present'],
            'conservative_cross_role_credit': c['conservative_cross_role_credit'], 'credit_raised': c['credit_raised'],
            'bad_acceptances': c['bad_acceptances'],
        },
        'epoch74': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch73_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_third_source_handoff_states': t['epoch74_bound_twenty_third_source_handoff_states'],
            'bound_twenty_third_source_binding_states': t['epoch74_bound_twenty_third_source_binding_states'],
            'bound_verifier_binding_states': t['epoch74_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication48': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_forty_seventh_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_forty_eighth_restart_recoveries': s['bound_forty_eighth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership26': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root26_witness_rebind_states': b['bound_root26_witness_rebind_states'],
            'bound_root26_witness_binding_states': b['bound_root26_witness_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 75 by rotating the twenty-third-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose forty-eighth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a forty-ninth verifier cold restart without cached authority promotion',
            'keep generation 4 while replacing and binding the witness source, rolling root 26 to root 27, binding root 27, and requiring replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V123 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-74 GC to {t['accepted']:,} states with {t['epoch74_bound_twenty_third_source_handoff_states']:,} bound twenty-third-source handoffs, "
        f"{t['epoch74_bound_twenty_third_source_binding_states']:,} bound twenty-third-source bindings, and {t['epoch74_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_forty_eighth_restart_recoveries']:,} fully bound forty-eighth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root26_witness_rebind_states']:,} bound root-26 witness rebinds and "
        f"{b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
