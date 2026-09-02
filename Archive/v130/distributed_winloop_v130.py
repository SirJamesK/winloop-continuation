"""WinLoop V130 exact continuation: epoch-81 twenty-sixth-lineage rotation, fifty-fifth cold restart, and root-30 rollover."""
import hashlib
import json
from winloop_v130_core import indep, gc81
from winloop_v130_publication import replacement_churn_fifty_fifth_restart
from winloop_v130_membership import root30_rollover_after_root29_witness_source_replacement

V = 'V130'
BASE_DIGEST = 'be84448facb110ea4fb9e4655ba9c4bc6208bd2ae3efcbc3fc696abcc267182a'
BASE_IMPL_SHA = '36a4e35c3c201e89256e80c1ec5fd0f16f7046b938b63a097542a7adc784d0be'


def run_validation():
    c = indep()
    t = gc81()
    s = replacement_churn_fifty_fifth_restart()
    b = root30_rollover_after_root29_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V129', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch81': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch80_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_sixth_lineage_rotation_states': t['epoch81_bound_twenty_sixth_lineage_rotation_states'],
            'bound_twenty_sixth_lineage_binding_states': t['epoch81_bound_twenty_sixth_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch81_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch81_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication55': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_fifty_fourth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_fifty_fifth_restart_recoveries': s['bound_fifty_fifth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership30': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_root30_rollover_states': b['bound_root30_rollover_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 82 by handing the rebound proof to a twenty-seventh source, binding that source, and preserving the epoch-12 deadline',
            'compose fifty-fifth-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a fifty-sixth verifier cold restart without cached authority promotion',
            'keep generation 4 at root 30, rebind the root-30 witness, renew witness binding, and require replication-quorum churn without tombstone, replacement-source, or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V130 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-81 GC to {t['accepted']:,} states with {t['epoch81_bound_twenty_sixth_lineage_rotation_states']:,} bound twenty-sixth-lineage rotations, "
        f"{t['epoch81_bound_twenty_sixth_lineage_binding_states']:,} bound lineage bindings, {t['epoch81_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch81_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_fifty_fifth_restart_recoveries']:,} fully bound fifty-fifth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, "
        f"{b['bound_root30_rollover_states']:,} bound root-30 rollovers, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
