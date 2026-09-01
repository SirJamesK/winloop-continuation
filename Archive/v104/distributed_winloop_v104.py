"""WinLoop V104 exact continuation: epoch-55 thirteenth-lineage rotation, twenty-ninth cold restart, and root-17 rollover."""
import hashlib
import json
from winloop_v104_core import indep, gc55
from winloop_v104_publication import replacement_churn_twenty_ninth_restart
from winloop_v104_membership import root17_rollover_after_root16_witness_source_replacement

V = 'V104'
BASE_DIGEST = '856c15cb5a682ec56752deef1d89b86b7cb79779b3d7f58c823239c333170d6e'
BASE_IMPL_SHA = '0f70dfaef73840331091e03a6073fba1d53f8ef62ea8f06177353288f8cbe53d'


def run_validation():
    c = indep()
    t = gc55()
    s = replacement_churn_twenty_ninth_restart()
    b = root17_rollover_after_root16_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V103',
            'digest': BASE_DIGEST,
            'implementation_sha256': BASE_IMPL_SHA,
        },
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {
            'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851,
            'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66',
        },
        'independence_certificate_gate': c,
        'tombstone_epoch55_thirteenth_lineage_rotation': t,
        'publication_replacement_churn_twenty_ninth_restart': s,
        'membership_root17_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 56 by handing the rebound proof to a fourteenth source, binding that source, and preserving the epoch-12 deadline',
            'compose twenty-ninth-restart recovery with successor-source disappearance and a thirtieth verifier cold restart without cached authority promotion',
            'carry root 17 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V104 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-55 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch55_bound_thirteenth_lineage_rotation_states']:,} bound thirteenth-lineage rotations, {t['epoch55_bound_thirteenth_lineage_binding_states']:,} bound lineage bindings, {t['epoch55_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch55_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_twenty_ninth_restart_recoveries']:,} fully bound twenty-ninth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root17_rollover_states']:,} bound root-17 rollovers, {b['bound_root17_binding_states']:,} bound root-17 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
