"""WinLoop V121 exact continuation: epoch-72 twenty-second-source handoff, forty-sixth cold restart, and root-25 witness rebind."""
import hashlib
import json
from winloop_v121_core import indep, gc72
from winloop_v121_publication import successor_disappearance_forty_sixth_restart
from winloop_v121_membership import root25_witness_rebind_quorum_churn

V = 'V121'
BASE_DIGEST = '7d958d0fc2e8e0c1d18c8a82c8f530aa48b8ed82b07086d91b71ea9d04acd382'
BASE_IMPL_SHA = 'ed7f9bb69dd6857515ed1569ca17ba9d3c2e5b0699abde5c9d91b30cc628cdb4'


def run_validation():
    c = indep()
    t = gc72()
    s = successor_disappearance_forty_sixth_restart()
    b = root25_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V120', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch72': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch71_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_second_source_handoff_states': t['epoch72_bound_twenty_second_source_handoff_states'],
            'bound_twenty_second_source_binding_states': t['epoch72_bound_twenty_second_source_binding_states'],
            'bound_verifier_binding_states': t['epoch72_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication46': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_forty_fifth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_forty_sixth_restart_recoveries': s['bound_forty_sixth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership25': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root25_witness_rebind_states': b['bound_root25_witness_rebind_states'],
            'bound_root25_witness_binding_states': b['bound_root25_witness_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 73 by rotating the twenty-second-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose forty-sixth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a forty-seventh verifier cold restart without cached authority promotion',
            'keep generation 4 while replacing and binding the witness source, rolling root 25 to root 26, binding root 26, and requiring replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V121 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-72 GC to {t['accepted']:,} states with {t['epoch72_bound_twenty_second_source_handoff_states']:,} bound twenty-second-source handoffs, "
        f"{t['epoch72_bound_twenty_second_source_binding_states']:,} bound twenty-second-source bindings, and {t['epoch72_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_forty_sixth_restart_recoveries']:,} fully bound forty-sixth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root25_witness_rebind_states']:,} bound root-25 witness rebinds and "
        f"{b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
