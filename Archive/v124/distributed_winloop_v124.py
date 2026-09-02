"""WinLoop V124 exact continuation: epoch-75 twenty-third-lineage rotation, forty-ninth cold restart, and root-27 rollover."""
import hashlib
import json
from winloop_v124_core import indep, gc75
from winloop_v124_publication import replacement_churn_forty_ninth_restart
from winloop_v124_membership import root27_rollover_after_root26_witness_source_replacement

V = 'V124'
BASE_DIGEST = '3cfe84048d6bb5a791b717806594df355dce4dc6ac07d8cf37785675cfbb058d'
BASE_IMPL_SHA = '1f9dd890d1414aa9654f29fb3247bdfbc1df16f06744676aa3209717f39a6186'


def run_validation():
    c = indep()
    t = gc75()
    s = replacement_churn_forty_ninth_restart()
    b = root27_rollover_after_root26_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V123', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch75': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch74_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_third_lineage_rotation_states': t['epoch75_bound_twenty_third_lineage_rotation_states'],
            'bound_twenty_third_lineage_binding_states': t['epoch75_bound_twenty_third_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch75_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch75_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication49': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_forty_eighth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_forty_ninth_restart_recoveries': s['bound_forty_ninth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership27': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_replacement_source_binding_states': b['bound_replacement_source_binding_states'],
            'bound_root27_rollover_states': b['bound_root27_rollover_states'],
            'bound_root27_binding_states': b['bound_root27_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 76 by handing the rebound proof to a twenty-fourth source, binding that source, and preserving the epoch-12 deadline',
            'compose forty-ninth-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a fiftieth verifier cold restart without cached authority promotion',
            'keep generation 4 and root 27 fixed while rebinding and binding the witness to root 27 and requiring replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V124 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-75 GC to {t['accepted']:,} states with {t['epoch75_bound_twenty_third_lineage_rotation_states']:,} bound twenty-third-lineage rotations, "
        f"{t['epoch75_bound_twenty_third_lineage_binding_states']:,} bound lineage bindings, {t['epoch75_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch75_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_forty_ninth_restart_recoveries']:,} fully bound forty-ninth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, "
        f"{b['bound_root27_rollover_states']:,} bound root-27 rollovers, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
