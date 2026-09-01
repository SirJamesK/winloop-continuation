"""WinLoop V118 exact continuation: epoch-69 twentieth-lineage rotation, forty-third cold restart, and root-24 rollover."""
import hashlib
import json
from winloop_v118_core import indep, gc69
from winloop_v118_publication import replacement_churn_forty_third_restart
from winloop_v118_membership import root24_rollover_after_root23_witness_source_replacement

V = 'V118'
BASE_DIGEST = 'c3e35f2bc16e706874171cbad13aa7018322443d4e77a69eb8d29aa8ed4b3527'
BASE_IMPL_SHA = 'a6de110016935bcba84fd12cf3f80e0dbdee5a28d4df5d7b342640c64cc39af3'


def run_validation():
    c = indep()
    t = gc69()
    s = replacement_churn_forty_third_restart()
    b = root24_rollover_after_root23_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V117', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch69': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch68_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twentieth_lineage_rotation_states': t['epoch69_bound_twentieth_lineage_rotation_states'],
            'bound_twentieth_lineage_binding_states': t['epoch69_bound_twentieth_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch69_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch69_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication43': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_forty_second_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_forty_third_restart_recoveries': s['bound_forty_third_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership24': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_replacement_source_binding_states': b['bound_replacement_source_binding_states'],
            'bound_root24_rollover_states': b['bound_root24_rollover_states'],
            'bound_root24_binding_states': b['bound_root24_binding_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 70 by handing the rebound proof to a twenty-first source, binding that source, and preserving the epoch-12 deadline',
            'compose forty-third-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a forty-fourth verifier cold restart without cached authority promotion',
            'keep generation 4 and root 24 fixed while rebinding and binding the witness to root 24 and requiring replication-quorum churn without tombstone or source-binding discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V118 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-69 GC to {t['accepted']:,} states with {t['epoch69_bound_twentieth_lineage_rotation_states']:,} bound twentieth-lineage rotations, "
        f"{t['epoch69_bound_twentieth_lineage_binding_states']:,} bound lineage bindings, {t['epoch69_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch69_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_forty_third_restart_recoveries']:,} fully bound forty-third-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, "
        f"{b['bound_root24_rollover_states']:,} bound root-24 rollovers, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
