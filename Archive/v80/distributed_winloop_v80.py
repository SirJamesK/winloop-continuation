"""WinLoop V80 exact continuation: epoch-31 reissued-key consumption and old-key tombstone collection across failover, rollback-safe fifth verifier restart, and root-5 split-view recovery under quorum churn."""
import hashlib
import json
from winloop_v80_core import indep, gc31
from winloop_v80_publication import reconciliation_rollback_fifth_restart
from winloop_v80_membership import root5_split_view_quorum_churn

V = 'V80'
BASE_DIGEST = '968738223d2343e72f1670df27df2610806431b2022863fa0a7a320d58cfe453'
BASE_IMPL_SHA = 'b2f8c5cad73a5947229c57a0b344bf93dcc1908fe80f8d24cb9a47dd31113984'


def run_validation():
    c = indep()
    t = gc31()
    s = reconciliation_rollback_fifth_restart()
    b = root5_split_view_quorum_churn()
    o = {
        'version': V,
        'base': {
            'version': 'V79',
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
        'tombstone_epoch31_reissued_key_consumption_failover_collection': t,
        'publication_reconciliation_rollback_fifth_restart': s,
        'membership_root5_split_view_quorum_churn': b,
        'checkpoint_recovery': {
            'statements': 513,
            'max_lag': 64,
            'shared_audit': '132 + 4*k',
            'frontier_storage_only': True,
            'trust_bearing_messages_unchanged': True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 32 with verifier-bound old-key tombstone consumption after a second source failover while preserving the epoch-12 deadline',
            'compose fifth-restart recovery with rollback-source disappearance and a sixth verifier cold restart without cached authority promotion',
            'carry root-5 split-view recovery through witness rotation and root-6 rollover under replication-quorum churn without generation or root regression',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V80 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-31 GC to {t['accepted']:,} of {t['patterns']:,} states with {t['epoch31_bound_reissued_key_consumption_states']:,} bound reissued-key consumptions, {t['epoch31_bound_source_failover_states']:,} bound source-failover states, and {t['epoch31_bound_old_key_tombstone_collection_states']:,} bound old-key tombstone collections while admitting zero stale/conflicting-root, unbound consumption/failover/collection/lineage/source-binding, tombstone-discontinuity, or deadline-reset states; "
        f"admits {s['accepted']:,} of {s['patterns']:,} publication states with {s['bound_reconciliation_rollback_states']:,} bound reconciliation rollbacks and {s['bound_fifth_restart_recoveries']:,} fully bound fifth-cold-restart recoveries with zero cached-authority, unbound rollback/source-binding/reconciliation/restart/consumption, or below-quorum acceptance; "
        f"and admits {b['accepted']:,} of {b['patterns']:,} membership states with {b['bound_root5_split_view_recovery_states']:,} bound root-5 split-view recoveries and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions with zero generation/root regression, tombstone/witness discontinuity, below-replication-quorum, unbound split/recovery/churn, or active-Byzantine acceptance."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
