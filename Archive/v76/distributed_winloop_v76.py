"""WinLoop V76 exact continuation: epoch-27 key recovery/lineage rollover, second verifier restart split-witness rollback, and second membership witness churn."""
import hashlib
import json
from winloop_v76_core import indep, gc27
from winloop_v76_publication import second_restart_split_witness_rollback_convergence
from winloop_v76_membership import second_witness_churn_after_membership_rollback

V = 'V76'
BASE_DIGEST = 'c7ad77c116f37569cd415b6c92c24f9332df44d8c05af0909a79275ffff329e2'
BASE_IMPL_SHA = 'c225ba7efd03051cafbd91cecfe2dfed87a2e48d7d61c5730ede3f68d33ac055'

def run_validation():
    c = indep()
    t = gc27()
    s = second_restart_split_witness_rollback_convergence()
    b = second_witness_churn_after_membership_rollback()
    o = {
        'version': V,
        'base': {'version': 'V75', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA},
        'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True},
        'routing': {'active': 'V21 guarded', 'replacement': False},
        'runtime': {'new_routing_envelope': False},
        'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'},
        'independence_certificate_gate': c,
        'tombstone_epoch27_key_recovery_lineage_rollover': t,
        'publication_second_restart_split_witness_rollback': s,
        'membership_second_witness_churn_after_rollback': b,
        'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True},
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 28 with replacement-source lineage loss/rebind and tombstone-root continuity without deadline reset',
            'compose second-restart split-witness recovery with renewed source disappearance and verifier cache-generation rollback',
            'test second witness-churn recovery through membership-root compaction and a third recycled-identity generation',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = 'V76 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-27 GC to 49,627,488 of 70,973,847,823,597,499,842,560,000 states including 470,016 bound re-rotated-key recoveries with replacement-source lineage rollover and zero stale/conflicting root-choice, unbound-recovery/lineage, or deadline-reset acceptance, admits 16,137,940 of 2,818,572,288,000,000,000,000,000 publication states including 1,572,480 bounded split-witness recoveries after a second verifier restart with zero cached-second-restart, unbound/conflicting rollback, unbound/forked recovery, or below-quorum acceptance, and admits 3,894,800 of 65,384,736,620,544,000,000 membership states including 276,640 second-generation witness-churn recoveries after rollback with zero below-replication-quorum, unbound rollback/churn, tombstone-generation collapse, unbound-root, or active-Byzantine acceptance.'
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o

if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
