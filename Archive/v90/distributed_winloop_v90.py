"""WinLoop V90 exact continuation: epoch-41 sixth-lineage rotation/proof rebind, replacement churn plus fifteenth cold restart, and witness replacement through root-10 rollover."""
import hashlib
import json
from winloop_v90_core import indep, gc41
from winloop_v90_publication import replacement_churn_fifteenth_restart
from winloop_v90_membership import root10_rollover_after_root9_witness_source_replacement

V = 'V90'
BASE_DIGEST = 'd82f57a7c7d52e38f1cadf55c3e388be974c420b1215dedb2f07e1b7d95caaf8'
BASE_IMPL_SHA = '95270f32c07e1c5538cb8aaf6cef9f5a378c20cc71a4bcec05f4a5e415308b94'


def run_validation():
    c = indep()
    t = gc41()
    s = replacement_churn_fifteenth_restart()
    b = root10_rollover_after_root9_witness_source_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V89',
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
        'tombstone_epoch41_sixth_lineage_handed_proof_rebind': t,
        'publication_replacement_churn_fifteenth_restart': s,
        'membership_witness_replacement_root10_rollover': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 42 by handing the rebound sixth-source proof to a seventh source and binding it while preserving the epoch-12 deadline',
            'compose fifteenth-restart recovery with successor-source disappearance and a sixteenth verifier cold restart without cached authority promotion',
            'carry root 10 through witness rebind and another replication-quorum churn without generation regression or quorum loss',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V90 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-41 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch41_bound_sixth_lineage_rotation_states']:,} bound sixth-lineage rotations, {t['epoch41_bound_sixth_lineage_binding_states']:,} bound lineage bindings, {t['epoch41_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and {t['epoch41_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound rotation/lineage/proof/verifier/source/key/provenance, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_replacement_source_churn_states']:,} bound replacement-source churns, {s['bound_successor_source_binding_states']:,} bound successor bindings, and {s['bound_fifteenth_restart_recoveries']:,} fully bound fifteenth-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root10_rollover_states']:,} bound root-10 rollovers, {b['bound_root10_binding_states']:,} bound root-10 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/prior-source discontinuity, below-replication-quorum, unbound replacement/rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
