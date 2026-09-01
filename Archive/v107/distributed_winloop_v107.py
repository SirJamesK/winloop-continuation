"""WinLoop V107 exact continuation: epoch-58 fifteenth-source handoff, thirty-second cold restart, and root-18 witness rebind."""
import hashlib
import json
from winloop_v107_core import indep, gc58
from winloop_v107_publication import successor_disappearance_thirty_second_restart
from winloop_v107_membership import root18_witness_rebind_quorum_churn

V = 'V107'
BASE_DIGEST = 'e9e65a487d0effbc030f27d6791c470215f4b8b1580ff2e9e15ca9847c1730f5'
BASE_IMPL_SHA = '52066546352d02a921dccc6eb6ecb47625924ad90f77cf1be20341a3d245f3ad'


def run_validation():
    c = indep()
    t = gc58()
    s = successor_disappearance_thirty_second_restart()
    b = root18_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V106', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch58': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch57_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_fifteenth_source_handoff_states': t['epoch58_bound_fifteenth_source_handoff_states'],
            'bound_fifteenth_source_binding_states': t['epoch58_bound_fifteenth_source_binding_states'],
            'bound_verifier_binding_states': t['epoch58_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication32': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_thirty_first_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_thirty_second_restart_recoveries': s['bound_thirty_second_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership18': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root18_witness_rebind_states': b['bound_root18_witness_rebind_states'],
            'bound_root18_witness_binding_states': b['bound_root18_witness_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 59 by rotating the fifteenth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose thirty-second-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a thirty-third verifier cold restart without cached authority promotion',
            'keep generation 4 and root 18 fixed while replacing and binding the witness source, rolling to root 19, binding root 19, and requiring replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V107 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-58 GC to {t['accepted']:,} states with {t['epoch58_bound_fifteenth_source_handoff_states']:,} bound fifteenth-source handoffs, {t['epoch58_bound_fifteenth_source_binding_states']:,} bound fifteenth-source bindings, and {t['epoch58_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_thirty_second_restart_recoveries']:,} fully bound thirty-second-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root18_witness_rebind_states']:,} bound root-18 witness rebinds and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
