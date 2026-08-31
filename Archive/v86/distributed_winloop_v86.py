"""WinLoop V86 exact continuation: epoch-37 fourth-source lineage re-rotation plus root rollover, successor-source churn plus eleventh cold restart, and root-8 membership rollover after bound witness replacement."""
import hashlib
import json
from winloop_v86_core import indep, gc37
from winloop_v86_publication import successor_source_churn_eleventh_restart
from winloop_v86_membership import root8_rollover_after_witness_replacement

V = 'V86'
BASE_DIGEST = 'b6ba3ffd84e137cca1c1f84954b606cd574dafe1f9406e05a3bdecd13609c780'
BASE_IMPL_SHA = 'b6c36b31c68d23c78471b947ac077d2c8bed3b76726999ed06c100b7d3784854'


def run_validation():
    c = indep()
    t = gc37()
    s = successor_source_churn_eleventh_restart()
    b = root8_rollover_after_witness_replacement()
    o = {
        'version': V,
        'base': {
            'version': 'V85',
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
        'tombstone_epoch37_fourth_lineage_root_rollover': t,
        'publication_successor_source_churn_eleventh_restart': s,
        'membership_root8_rollover_after_witness_replacement': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 38 with root-rolled fourth-source proof compaction and a bound fifth-source handoff while preserving the epoch-12 deadline',
            'compose eleventh-restart recovery with successor-source disappearance and a twelfth verifier cold restart without cached authority promotion',
            'rebind the root-8 witness after rollover and carry it through another replication-quorum churn cycle without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V86 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-37 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch37_bound_fourth_source_lineage_rerotation_states']:,} bound fourth-source lineage re-rotations, {t['epoch37_bound_root_rollover_states']:,} bound root rollovers, {t['epoch37_bound_root_binding_states']:,} bound root bindings, and {t['epoch37_bound_verifier_binding_states']:,} bound verifier completions while admitting zero stale/conflicting-root, unbound re-rotation/lineage/root/verifier/source/key, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_successor_source_churn_states']:,} bound successor-source churn states, {s['bound_successor_source_binding_states']:,} bound successor bindings, and {s['bound_eleventh_restart_recoveries']:,} fully bound eleventh-cold-restart recoveries with zero cached-authority, unbound churn/successor/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root8_rollover_states']:,} bound root-8 rollovers, {b['bound_root8_binding_states']:,} bound root-8 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness/replacement-source discontinuity, below-replication-quorum, unbound rollover/binding/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
