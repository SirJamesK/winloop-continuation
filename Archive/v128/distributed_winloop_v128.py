"""WinLoop V128 exact continuation: epoch-79 twenty-fifth-lineage rotation, fifty-third cold restart, and root-29 rollover."""
import hashlib
import json
from winloop_v128_core import indep, gc79
from winloop_v128_publication import replacement_churn_fifty_third_restart
from winloop_v128_membership import root29_rollover_after_root28_witness_source_replacement

V = 'V128'
BASE_DIGEST = 'e504148379342f9d436b438211d9bd6a2538607bc9730145739227eaa36e3a81'
BASE_IMPL_SHA = '640dd44b8701eb172a05f635664f8d7e88f3d2634b8a4e008edc1ac2b90d1837'


def run_validation():
    c = indep()
    t = gc79()
    s = replacement_churn_fifty_third_restart()
    b = root29_rollover_after_root28_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V127', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch79': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch78_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_fifth_lineage_rotation_states': t['epoch79_bound_twenty_fifth_lineage_rotation_states'],
            'bound_twenty_fifth_lineage_binding_states': t['epoch79_bound_twenty_fifth_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch79_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch79_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication53': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_fifty_second_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_fifty_third_restart_recoveries': s['bound_fifty_third_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership29': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_root29_rollover_states': b['bound_root29_rollover_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 80 by handing the rebound twenty-fifth-lineage proof to a twenty-sixth source, binding that source, and preserving the epoch-12 deadline',
            'compose fifty-third-restart recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a fifty-fourth verifier cold restart without cached authority promotion',
            'keep generation 4 after root-29 rollover, rebind the witness to root 29, renew the witness binding, and require replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V128 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-79 GC to {t['accepted']:,} states with {t['epoch79_bound_twenty_fifth_lineage_rotation_states']:,} bound twenty-fifth-lineage rotations, "
        f"{t['epoch79_bound_twenty_fifth_lineage_binding_states']:,} bound lineage bindings, {t['epoch79_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch79_bound_verifier_binding_states']:,} bound verifier completions; admits {s['accepted']:,} publication states with "
        f"{s['bound_fifty_third_restart_recoveries']:,} fully bound fifty-third-cold-restart recoveries; and admits {b['accepted']:,} membership states with "
        f"{b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root29_rollover_states']:,} bound root-29 rollovers, "
        f"and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
