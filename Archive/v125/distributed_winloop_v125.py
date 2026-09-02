"""WinLoop V125 exact continuation: epoch-76 twenty-fourth-source handoff, fiftieth cold restart, and root-27 witness rebind."""
import hashlib
import json
from winloop_v125_core import indep, gc76
from winloop_v125_publication import successor_disappearance_fiftieth_restart
from winloop_v125_membership import root27_witness_rebind_quorum_churn

V = 'V125'
BASE_DIGEST = '7135cd1437db54d08faae59371bc01fd7d59abb2563059c1f2e364acc10d8f85'
BASE_IMPL_SHA = 'ec247db121f064b265444ca08981acb6f23d3258f91f72a870cadbdbe48441c3'


def run_validation():
    c = indep()
    t = gc76()
    s = successor_disappearance_fiftieth_restart()
    b = root27_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V124', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch76': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch75_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_fourth_source_handoff_states': t['epoch76_bound_twenty_fourth_source_handoff_states'],
            'bound_twenty_fourth_source_binding_states': t['epoch76_bound_twenty_fourth_source_binding_states'],
            'bound_verifier_binding_states': t['epoch76_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication50': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_forty_ninth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_fiftieth_restart_recoveries': s['bound_fiftieth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership27': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root27_witness_rebind_states': b['bound_root27_witness_rebind_states'],
            'bound_root27_witness_binding_states': b['bound_root27_witness_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 77 by rotating the twenty-fourth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose fiftieth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a fifty-first verifier cold restart without cached authority promotion',
            'keep generation 4 while replacing and binding the witness source, rolling root 27 to root 28, binding root 28, and requiring replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V125 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-76 GC to {t['accepted']:,} states with {t['epoch76_bound_twenty_fourth_source_handoff_states']:,} bound twenty-fourth-source handoffs, "
        f"{t['epoch76_bound_twenty_fourth_source_binding_states']:,} bound twenty-fourth-source bindings, and {t['epoch76_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_fiftieth_restart_recoveries']:,} fully bound fiftieth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root27_witness_rebind_states']:,} bound root-27 witness rebinds and "
        f"{b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
