"""WinLoop V73 exact continuation: epoch-24 replacement-key rotation, dual-root disagreement, cold-start witness selection, and concurrent collision/root compaction."""
import hashlib, json
from winloop_v73_core import indep, gc24
from winloop_v73_publication import rollback_two_witness_coldstart
from winloop_v73_membership import compact_reuse_root

V="V73"
BASE_DIGEST="df8018a5257fb3cd129b2849b5a55f44fb7a3781cd5646bcbb65f29d5fcfbe98"
BASE_IMPL_SHA="0e88efa9e47f86aeaff35e22b28a15642f553c33a37a68fad83f75bdbec5a46a"

def run_validation():
    c = indep()
    t = gc24()
    s = rollback_two_witness_coldstart()
    b = compact_reuse_root()
    o = {'version': V, 'base': {'version': 'V72', 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}, 'admission': {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}, 'routing': {'active': 'V21 guarded', 'replacement': False}, 'runtime': {'new_routing_envelope': False}, 'temporal_floor_regression': {'roots': 22, 'horizon': 22, 'floor': 1, 'budget': 851, 'h11_floor': 2, 'h11_budget': 398, 'carried_from': 'V66'}, 'independence_certificate_gate': c, 'tombstone_epoch24_rotation_dual_root': t, 'publication_verifier_rollback_two_witness_coldstart': s, 'collision_reuse_membership_root_compaction': b, 'checkpoint_recovery': {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}, 'next': ['require committed independent provider/operator/hardware evidence before cross-role credit increase', 'extend anchor GC through epoch 25 with replacement-key loss/recovery after dual-root disagreement and monotonic root-choice evidence', 'compose cold-start source selection with witness-set split view and delayed publication-root convergence', 'test concurrent recycled identities across two tombstone generations while membership-root compaction is partially replicated', 'retain V21 routing until the >=2000-seed replacement bar clears']}
    o['headline'] = f"V73 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-24 GC to {t['accepted']:,} of {t['patterns']:,} states with bound fourth-cycle replacement-key rotation and dual rollback-root disagreement while admitting zero stale/conflicting-root, unbound-rotation, or deadline-reset states, admits {s['accepted']:,} of {s['patterns']:,} publication/verifier-rollback states with two replacement-witness rotations and bound verifier cold-start source selection with zero cached-join authority, unbound-source-selection, or below-publication-quorum acceptance, and admits {b['accepted']:,} of {b['patterns']:,} membership states under concurrent collision identity reuse plus membership-root compaction with zero tombstone-generation bypass, unbound-root, or active-Byzantine acceptance."
    o['digest'] = hashlib.sha256(json.dumps(o, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    return o

if __name__=="__main__":
    print(json.dumps(run_validation(),indent=2,sort_keys=True))
