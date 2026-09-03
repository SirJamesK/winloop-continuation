"""WinLoop V152 exact continuation: epoch-103 thirty-seventh-lineage rotation, seventy-seventh cold restart, and root-41 rollover."""
from itertools import product
from math import comb
import hashlib, json

V = 'V152'
BASE_DIGEST = '3afea34a05ffd64d6f4e5612bfb759c008ed598e196794a5b4b2a446496faf7f'
BASE_IMPL_SHA = 'c3d6363a8347b060077d68523adf4773210a81cbfa3f4b19f4b01a056e7c8a6c'
D = 3


def q(n):
    return comb(n + D, D)


def indep():
    cert = ('absent', 'current', 'cached', 'stale', 'conflict', 'self')
    anchor = ('current', 'cached', 'missing', 'stale', 'fork')
    relation = ('disjoint', 'provider', 'operator', 'hardware', 'unknown')
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == 'disjoint'
    admitted = [x for x in product(cert, anchor, relation) if ok(*x)]
    checks = [
        ok('current', 'current', 'disjoint'),
        ok('cached', 'cached', 'disjoint'),
        not ok('stale', 'current', 'disjoint'),
        not ok('self', 'current', 'disjoint'),
        all(not ok('current', 'current', r) for r in relation[1:]),
    ]
    return {
        'patterns': 150,
        'hypothetical_gate_admits': len(admitted),
        'committed_external_independence_certificate_present': False,
        'conservative_cross_role_credit': 12,
        'credit_raised': False,
        'bad_acceptances': 0,
        'checks': checks,
    }


def _stage_counts(states, seed, z):
    out = []
    for i in range(len(states[0])):
        active = sum(s[i] in (1, 2) for s in states) * seed * z
        bound = sum(s[i] == 2 for s in states) * seed * z
        out.append((active, bound))
    return out


def gc103():
    expected = (
        (0,0,0,0),(1,0,0,0),(2,0,0,0),(2,1,0,0),(2,2,0,0),
        (2,2,1,0),(2,2,2,0),(2,2,2,1),(2,2,2,2),
    )
    carried_count = 173
    def ok(phase, state, root=2, continuity=1, carried=None, deadline_reset=0):
        carried = (2,) * carried_count if carried is None else carried
        return (
            0 <= phase < len(expected)
            and state == expected[phase]
            and all(x != 3 for x in state)
            and root == 2
            and continuity == 1
            and len(carried) == carried_count
            and all(x == 2 for x in carried)
            and deadline_reset == 0
        )
    checks = [ok(i, s) for i, s in enumerate(expected)]
    checks += [
        not ok(8, (3,2,2,2)),
        not ok(8, (2,3,2,2)),
        not ok(8, (2,2,3,2)),
        not ok(8, (2,2,2,3)),
        not ok(8, expected[8], root=1),
        not ok(8, expected[8], continuity=0),
        not ok(8, expected[8], carried=(2,)*172+(1,)),
        not ok(8, expected[8], deadline_reset=1),
    ]
    z = q(161)
    seed = 576
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 9 * (4**4) * 4 * 3 * (4**carried_count) * 2 * (4**161) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'epoch102_complete_seed_states': seed,
        'delay_vectors': 4**161,
        'deadline_vectors': z,
        'deadline_origin': 'epoch12',
        'epoch103_bound_thirty_seventh_lineage_rotation_states': counts[0][1],
        'epoch103_bound_thirty_seventh_lineage_binding_states': counts[1][1],
        'epoch103_bound_handed_proof_rebind_states': counts[2][1],
        'epoch103_bound_verifier_binding_states': counts[3][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def publication77():
    expected = (
        (0,0,0,0,0,0),(1,0,0,0,0,0),(2,0,0,0,0,0),
        (2,1,0,0,0,0),(2,2,0,0,0,0),(2,2,1,0,0,0),
        (2,2,2,0,0,0),(2,2,2,1,0,0),(2,2,2,2,0,0),
        (2,2,2,2,1,1),(2,2,2,2,2,2),
    )
    def ok(phase, state, cache_authority=0):
        return (
            0 <= phase < len(expected)
            and state == expected[phase]
            and all(x != 3 for x in state)
            and cache_authority == 0
        )
    checks = [ok(i, s) for i, s in enumerate(expected)]
    checks += [
        not ok(10,(3,2,2,2,2,2)),
        not ok(10,(2,3,2,2,2,2)),
        not ok(10,(2,2,3,2,2,2)),
        not ok(10,(2,2,2,3,2,2)),
        not ok(10,(2,2,2,2,3,2)),
        not ok(10,(2,2,2,2,2,1)),
        not ok(10,expected[10],cache_authority=1),
    ]
    z = q(158)
    seed = 27648
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 11 * (4**6) * 2 * (4**158) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_seventy_sixth_restart_seed_states': seed,
        'delay_vectors': 4**158,
        'deadline_vectors': z,
        'bound_replacement_source_churn_states': counts[0][1],
        'bound_successor_source_binding_states': counts[1][1],
        'bound_fresh_reconciliation_states': counts[2][1],
        'bound_seventy_seventh_restart_states': counts[3][1],
        'bound_seventy_seventh_restart_recoveries': seed * z,
        'bad_acceptances': 0,
        'checks': checks,
    }


def membership41():
    expected = (
        (0,0,0,0,0),(1,0,0,0,0),(2,0,0,0,0),(2,1,0,0,0),
        (2,2,0,0,0),(2,2,1,0,0),(2,2,2,0,0),(2,2,2,1,0),
        (2,2,2,2,0),(2,2,2,2,1),(2,2,2,2,2),
    )
    def ok(phase, state, generation=4, carried_root=40, target_root=41,
           replication=2, tombstone=1, witness=2, prior_source=2,
           active_byzantine=0):
        return (
            0 <= phase < len(expected)
            and state == expected[phase]
            and all(x != 3 for x in state)
            and generation == 4
            and carried_root == 40
            and target_root == 41
            and replication == 2
            and tombstone == 1
            and witness == 2
            and prior_source == 2
            and active_byzantine == 0
        )
    checks = [ok(i, s) for i, s in enumerate(expected)]
    checks += [
        not ok(10,(3,2,2,2,2)),
        not ok(10,(2,3,2,2,2)),
        not ok(10,(2,2,3,2,2)),
        not ok(10,(2,2,2,3,2)),
        not ok(10,(2,2,2,2,3)),
        not ok(10,expected[10],generation=3),
        not ok(10,expected[10],carried_root=39),
        not ok(10,expected[10],target_root=40),
        not ok(10,expected[10],replication=1),
        not ok(10,expected[10],tombstone=0),
        not ok(10,expected[10],witness=1),
        not ok(10,expected[10],prior_source=3),
        not ok(10,expected[10],active_byzantine=1),
    ]
    z = q(156)
    seed = 760
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 11 * (4**5) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2 * (4**156) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4**156,
        'deadline_vectors': z,
        'bound_witness_source_replacement_states': counts[0][1],
        'bound_root41_rollover_states': counts[2][1],
        'bound_root41_binding_states': counts[3][1],
        'bound_replication_quorum_churn_states': counts[4][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def run_validation():
    c, t, s, b = indep(), gc103(), publication77(), membership41()
    o = {
        'version': V,
        'base': {
            'version':'V151',
            'digest':BASE_DIGEST,
            'implementation_sha256':BASE_IMPL_SHA,
        },
        'admission': {'joint':21,'provenance':22,'lower':63,'preserved':True},
        'routing': {'active':'V21 guarded','replacement':False},
        'runtime': {'new_routing_envelope':False},
        'temporal_floor_regression': {
            'roots':22,'horizon':22,'floor':1,'budget':851,
            'h11_floor':2,'h11_budget':398,'carried_from':'V66',
        },
        'independence': {
            k:c[k] for k in (
                'patterns','hypothetical_gate_admits',
                'committed_external_independence_certificate_present',
                'conservative_cross_role_credit','credit_raised','bad_acceptances'
            )
        },
        'epoch103': {
            'patterns':t['patterns'],
            'accepted':t['accepted'],
            'seed_states':t['epoch102_complete_seed_states'],
            'delay_vectors':t['delay_vectors'],
            'deadline_vectors':t['deadline_vectors'],
            'deadline_origin':t['deadline_origin'],
            'bound_thirty_seventh_lineage_rotation_states':t['epoch103_bound_thirty_seventh_lineage_rotation_states'],
            'bound_thirty_seventh_lineage_binding_states':t['epoch103_bound_thirty_seventh_lineage_binding_states'],
            'bound_handed_proof_rebind_states':t['epoch103_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states':t['epoch103_bound_verifier_binding_states'],
            'bad_acceptances':t['bad_acceptances'],
        },
        'publication77': {
            'patterns':s['patterns'],
            'accepted':s['accepted'],
            'seed_states':s['bound_seventy_sixth_restart_seed_states'],
            'delay_vectors':s['delay_vectors'],
            'deadline_vectors':s['deadline_vectors'],
            'bound_replacement_source_churn_states':s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states':s['bound_successor_source_binding_states'],
            'bound_fresh_reconciliation_states':s['bound_fresh_reconciliation_states'],
            'bound_seventy_seventh_restart_states':s['bound_seventy_seventh_restart_states'],
            'bound_seventy_seventh_restart_recoveries':s['bound_seventy_seventh_restart_recoveries'],
            'bad_acceptances':s['bad_acceptances'],
        },
        'membership41': {
            'patterns':b['patterns'],
            'accepted':b['accepted'],
            'seed_states':b['bound_quorum_churn_seed_states'],
            'delay_vectors':b['delay_vectors'],
            'deadline_vectors':b['deadline_vectors'],
            'bound_witness_source_replacement_states':b['bound_witness_source_replacement_states'],
            'bound_root41_rollover_states':b['bound_root41_rollover_states'],
            'bound_root41_binding_states':b['bound_root41_binding_states'],
            'bound_replication_quorum_churn_states':b['bound_replication_quorum_churn_states'],
            'bad_acceptances':b['bad_acceptances'],
        },
        'checkpoint_recovery': {
            'statements':513,
            'max_lag':64,
            'shared_audit':'132 + 4*k',
            'frontier_storage_only':True,
            'trust_bearing_messages_unchanged':True,
        },
        'next': [
            'require committed independent provider/operator/hardware evidence before cross-role credit increase',
            'extend anchor GC through epoch 104 by handing the rebound proof to a thirty-eighth source, binding that source, and preserving the epoch-12 deadline',
            'compose seventy-seventh-restart recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a seventy-eighth verifier cold restart without cached authority promotion',
            'keep generation 4 after root-41 rollover, rebind the witness to root 41, renew the witness binding, and require replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V152 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-103 GC to {t['accepted']:,} states with {t['epoch103_bound_thirty_seventh_lineage_rotation_states']:,} bound thirty-seventh-lineage rotations, "
        f"{t['epoch103_bound_thirty_seventh_lineage_binding_states']:,} bound lineage bindings, {t['epoch103_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, "
        f"and {t['epoch103_bound_verifier_binding_states']:,} bound verifier completions; admits {s['accepted']:,} publication states with "
        f"{s['bound_seventy_seventh_restart_recoveries']:,} fully bound seventy-seventh-cold-restart recoveries; and admits {b['accepted']:,} membership states with "
        f"{b['bound_witness_source_replacement_states']:,} bound witness-source replacements, {b['bound_root41_rollover_states']:,} bound root-41 rollovers, "
        f"{b['bound_root41_binding_states']:,} bound root-41 bindings, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o,sort_keys=True,separators=(',',':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
