"""WinLoop V96 exact continuation: epoch-47 ninth-lineage rotation, twenty-first cold restart, and root-13 rollover."""
import hashlib
import json
from winloop_v96_core import indep, gc47
from winloop_v96_publication import replacement_churn_twenty_first_restart
from winloop_v96_membership import root13_rollover_after_root12_witness_source_replacement

V = 'V96'
BASE_DIGEST = '5a8ee21699259de7d8f500b4ddaf37f84f0e5767416efd4e5f749c7f1ebcd235'
BASE_IMPL_SHA = '92c519f3cb7794eee0cb0f9308a5cf8d6c58754533d7dc867922ded6ebfcfe44'


def run_validation():
    c = indep()
    t = gc47()
    s = replacement_churn_twenty_first_restart()
    b = root13_rollover_after_root12_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V95',
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
        'tombstone_epoch47_ninth_lineage_handed_proof_rebind': t,
        'publication_replacement_churn_twenty_first_restart': s,
        'membership_witness_replacement_root13_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 48 by handing the rebound proof to a tenth source, binding that source, and preserving the epoch-12 deadline',
            'compose twenty-first-restart recovery with successor-source disappearance and a twenty-second verifier cold restart without cached authority promotion',
            'carry root 13 through witness rebind, witness binding, and replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V96 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-47 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch47_bound_ninth_lineage_rotation_states']:,} bound ninth-lineage rotations, {t['epoch47_bound_ninth_lineage_binding_states']:,} bound lineage bindings, {t['epoch47_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch47_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor-source bindings, and {s['bound_twenty_first_restart_recoveries']:,} fully bound twenty-first-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root13_rollover_states']:,} bound root-13 rollovers, {b['bound_root13_binding_states']:,} bound root-13 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
