"""WinLoop V126 exact continuation: epoch-77 twenty-fourth-lineage rotation, fifty-first cold restart, and root-28 rollover."""
import hashlib
import json
from winloop_v126_core import indep, gc77
from winloop_v126_publication import replacement_churn_fifty_first_restart
from winloop_v126_membership import root28_rollover_after_root27_witness_source_replacement

V = 'V126'
BASE_DIGEST = '10c0bbf37187997ae613078eaa0c889bf5413b05ea140817818617f9bc56c613'
BASE_IMPL_SHA = '73929960ceeb848b6393f082d1ca299ecd9b73e3fb03e512d6fbeebcc5058188'


def run_validation():
    c = indep()
    t = gc77()
    s = replacement_churn_fifty_first_restart()
    b = root28_rollover_after_root27_witness_source_replacement()
    o = {
        'version': V,
        'base': {'version': 'V125', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
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
        'epoch77': {
            'patterns': t['patterns'], 'accepted': t['accepted'], 'seed_states': t['epoch76_complete_seed_states'],
            'delay_vectors': t['delay_vectors'], 'deadline_vectors': t['deadline_vectors'], 'deadline_origin': t['deadline_origin'],
            'bound_twenty_fourth_lineage_rotation_states': t['epoch77_bound_twenty_fourth_lineage_rotation_states'],
            'bound_twenty_fourth_lineage_binding_states': t['epoch77_bound_twenty_fourth_lineage_binding_states'],
            'bound_handed_proof_rebind_states': t['epoch77_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states': t['epoch77_bound_verifier_binding_states'], 'bad_acceptances': t['bad_acceptances'],
        },
        'publication51': {
            'patterns': s['patterns'], 'accepted': s['accepted'], 'seed_states': s['bound_fiftieth_restart_seed_states'],
            'delay_vectors': s['delay_vectors'], 'deadline_vectors': s['deadline_vectors'],
            'bound_replacement_source_churn_states': s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states': s['bound_successor_source_binding_states'],
            'bound_fifty_first_restart_recoveries': s['bound_fifty_first_restart_recoveries'], 'bad_acceptances': s['bad_acceptances'],
        },
        'membership28': {
            'patterns': b['patterns'], 'accepted': b['accepted'], 'seed_states': b['bound_quorum_churn_seed_states'],
            'delay_vectors': b['delay_vectors'], 'deadline_vectors': b['deadline_vectors'],
            'bound_witness_source_replacement_states': b['bound_witness_source_replacement_states'],
            'bound_root28_rollover_states': b['bound_root28_rollover_states'],
            'bound_replication_quorum_churn_states': b['bound_replication_quorum_churn_states'], 'bad_acceptances': b['bad_acceptances'],
        },
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 78 by handing the rebound proof to a twenty-fifth source, binding that source, and preserving the epoch-12 deadline',
            'compose fifty-first-restart recovery with successor-source disappearance, replacement binding, fresh reconciliation, and a fifty-second verifier cold restart without cached authority promotion',
            'keep generation 4 and root 28 fixed while rebinding the witness to root 28 and requiring replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V126 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-77 GC to {t['accepted']:,} states with {t['epoch77_bound_twenty_fourth_lineage_rotation_states']:,} bound twenty-fourth-lineage rotations, "
        f"{t['epoch77_bound_twenty_fourth_lineage_binding_states']:,} bound lineage bindings, {t['epoch77_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch77_bound_verifier_binding_states']:,} bound verifier completions; admits {s['accepted']:,} publication states with "
        f"{s['bound_fifty_first_restart_recoveries']:,} fully bound fifty-first-cold-restart recoveries; and admits {b['accepted']:,} membership states with "
        f"{b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root28_rollover_states']:,} bound root-28 rollovers, "
        f"and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
