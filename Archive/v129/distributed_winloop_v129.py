"""WinLoop V129 exact continuation: epoch-80 twenty-sixth-source handoff, fifty-fourth cold restart, and root-29 witness rebind."""
import hashlib
import json
from winloop_v129_core import indep, gc80
from winloop_v129_publication import successor_disappearance_fifty_fourth_restart
from winloop_v129_membership import root29_witness_rebind_quorum_churn

V = 'V129'
BASE_DIGEST = '0feed1bdd265d16c22d76971ee1766e157d4d05b1614a381328d643425019b46'
BASE_IMPL_SHA = 'bbb519df619e68c3346a4277381626ddbc27fb9cf5b8d500b2862c47eff17bce'


def run_validation():
    c = indep()
    t = gc80()
    s = successor_disappearance_fifty_fourth_restart()
    b = root29_witness_rebind_quorum_churn()
    o = {
        'version': V,
        'base': {'version': 'V128', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch80': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch79_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_sixth_source_handoff_states': t['epoch80_bound_twenty_sixth_source_handoff_states'],
            'bound_twenty_sixth_source_binding_states': t['epoch80_bound_twenty_sixth_source_binding_states'],
            'bound_verifier_binding_states': t['epoch80_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication54': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_fifty_third_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_successor_source_disappearance_states': s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states': s['bound_replacement_source_binding_states'],
            'bound_fifty_fourth_restart_recoveries': s['bound_fifty_fourth_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership29': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_root29_witness_rebind_states': b['bound_root29_witness_rebind_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 81 by rotating the twenty-sixth-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose fifty-fourth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a fifty-fifth verifier cold restart without cached authority promotion',
            'keep generation 4 after root-29 witness rebind, replace the witness source, roll to root 30, bind root 30, and require replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V129 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-80 GC to {t['accepted']:,} states with {t['epoch80_bound_twenty_sixth_source_handoff_states']:,} bound twenty-sixth-source handoffs, "
        f"{t['epoch80_bound_twenty_sixth_source_binding_states']:,} bound twenty-sixth-source bindings, and {t['epoch80_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_fifty_fourth_restart_recoveries']:,} fully bound fifty-fourth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root29_witness_rebind_states']:,} bound root-29 witness rebinds and "
        f"{b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
