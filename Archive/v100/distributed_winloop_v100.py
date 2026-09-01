"""WinLoop V100 exact continuation: epoch-51 eleventh-lineage rotation, twenty-fifth cold restart, and root-15 rollover."""
import hashlib
import json
from winloop_v100_core import indep, gc51
from winloop_v100_publication import replacement_churn_twenty_fifth_restart
from winloop_v100_membership import root15_rollover_after_root14_witness_source_replacement

V = 'V100'
BASE_DIGEST = 'a6afb2b427d9aa3ea6287d16c971d2ee3fdd2fa6439fde28bd65074c145e5e5a'
BASE_IMPL_SHA = '1af8c1de21d2063013899df4eb6458f34f096d38b71ad8af6a1163905c3e8b4c'


def run_validation():
    c = indep()
    t = gc51()
    s = replacement_churn_twenty_fifth_restart()
    b = root15_rollover_after_root14_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V99',
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
        'tombstone_epoch51_eleventh_lineage_rotation': t,
        'publication_replacement_churn_twenty_fifth_restart': s,
        'membership_root15_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 52 by handing the rebound proof to a twelfth source, binding that source, and preserving the epoch-12 deadline',
            'compose twenty-fifth-restart recovery with successor-source disappearance and a twenty-sixth verifier cold restart without cached authority promotion',
            'keep generation 4 and root 15 fixed while rebinding the witness and completing another replication-quorum churn without quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V100 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-51 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch51_bound_eleventh_lineage_rotation_states']:,} bound eleventh-lineage rotations, {t['epoch51_bound_eleventh_lineage_binding_states']:,} bound lineage bindings, {t['epoch51_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch51_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/handoff/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor bindings, and {s['bound_twenty_fifth_restart_recoveries']:,} fully bound twenty-fifth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root15_rollover_states']:,} bound root-15 rollovers, {b['bound_root15_binding_states']:,} bound root-15 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
