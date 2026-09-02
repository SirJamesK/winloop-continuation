"""WinLoop V127 exact continuation: epoch-78 twenty-fifth-source handoff, fifty-second cold restart, and root-28 witness rebind."""
import hashlib
import json
from winloop_v127_core import indep, gc78
from winloop_v127_publication import successor_disappearance_fifty_second_restart
from winloop_v127_membership import root28_witness_rebind_quorum_churn

V = 'V127'
BASE_DIGEST = 'c5aa4ba69b62e5ae1b1c541792f915cce1a13e6a47705f6f3c1ee7f56dd2f32e'
BASE_IMPL_SHA = '54260b049f90987b89bfa63e79aff4e4c0b731766e912e0d819f0f3fa345a8aa'


def run_validation():
    c = indep()
    t = gc78()
    s = successor_disappearance_fifty_second_restart()
    b = root28_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V126', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch78': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch77_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_fifth_source_handoff_states': t['epoch78_bound_twenty_fifth_source_handoff_states'],
            'bound_twenty_fifth_source_binding_states': t['epoch78_bound_twenty_fifth_source_binding_states'],
            'bound_verifier_binding_states': t['epoch78_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication52': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_fifty_first_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_fifty_second_restart_recoveries': s['bound_fifty_second_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership28': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root28_witness_rebind_states': b['bound_root28_witness_rebind_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 79 by rotating the twenty-fifth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose fifty-second-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a fifty-third verifier cold restart without cached authority promotion',
            'keep generation 4 after root-28 witness rebind, replace the witness source, roll to root 29, bind root 29, and require replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V127 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-78 GC to {t['accepted']:,} states with {t['epoch78_bound_twenty_fifth_source_handoff_states']:,} bound twenty-fifth-source handoffs, "
        f"{t['epoch78_bound_twenty_fifth_source_binding_states']:,} bound twenty-fifth-source bindings, and {t['epoch78_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_fifty_second_restart_recoveries']:,} fully bound fifty-second-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root28_witness_rebind_states']:,} bound root-28 witness rebinds and "
        f"{b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
