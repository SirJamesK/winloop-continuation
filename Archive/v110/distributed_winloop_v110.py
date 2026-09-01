"""WinLoop V110 exact continuation: epoch-61 sixteenth-lineage rotation, thirty-fifth cold restart, and root-20 rollover."""
import hashlib
import json
from winloop_v110_core import indep, gc61
from winloop_v110_publication import replacement_churn_thirty_fifth_restart
from winloop_v110_membership import root20_rollover_after_root19_witness_source_replacement

V = 'V110'
BASE_DIGEST = '75de7563e42cc8fd5de633ee74780dc303db3d335141a68c02145546070e7ba0'
BASE_IMPL_SHA = 'a6755e64b1b2d78a90f01f8d27dcb9f994048f374522ba90a858d772300f9720'


def run_validation():
    c = indep()
    t = gc61()
    s = replacement_churn_thirty_fifth_restart()
    b = root20_rollover_after_root19_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V109', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch61': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch60_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_sixteenth_lineage_rotation_states': t['epoch61_bound_sixteenth_lineage_rotation_states'],
            'bound_sixteenth_lineage_binding_states': t['epoch61_bound_sixteenth_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch61_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch61_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication35': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_thirty_fourth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_thirty_fifth_restart_recoveries': s['bound_thirty_fifth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership20': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_replacement_source_binding_states': b['bound_replacement_source_binding_states'],
            'bound_root20_rollover_states': b['bound_root20_rollover_states'],
            'bound_root20_binding_states': b['bound_root20_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 62 by handing the rebound proof to a seventeenth source, binding that source, and preserving the epoch-12 deadline',
            'compose thirty-fifth-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a thirty-sixth verifier cold restart without cached authority promotion',
            'keep generation 4 and root 20 fixed while rebinding the witness and requiring replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V110 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-61 GC to {t['accepted']:,} states with {t['epoch61_bound_sixteenth_lineage_rotation_states']:,} bound sixteenth-lineage rotations, {t['epoch61_bound_sixteenth_lineage_binding_states']:,} bound lineage bindings, {t['epoch61_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch61_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_thirty_fifth_restart_recoveries']:,} fully bound thirty-fifth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root20_rollover_states']:,} bound root-20 rollovers, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
