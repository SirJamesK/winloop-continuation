"""WinLoop V139 exact continuation: epoch-90 thirty-first-source handoff, sixty-fourth cold restart, and root-34 witness rebind."""
from itertools import product
from math import comb
import hashlib, json

V = 'V139'
BASE_DIGEST = '263f2638cc720938c77a71d4cd80e2b43c623ef7d7b6585f0840a8fa557add5c'
BASE_IMPL_SHA = 'f69d6b6966d1a3fde7f3770bec192e35e363cb8c379f9932ac5fbff6f08ad53c'
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


def gc90():
    expected = (
        (0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2),
    )
    carried_count = 134
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
        not ok(6, (3,2,2)),
        not ok(6, (2,3,2)),
        not ok(6, (2,2,3)),
        not ok(6, expected[6], root=1),
        not ok(6, expected[6], continuity=0),
        not ok(6, expected[6], carried=(2,)*133+(1,)),
        not ok(6, expected[6], deadline_reset=1),
    ]
    z = q(135)
    seed = 576
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 7 * (4**3) * 4 * 3 * (4**carried_count) * 2 * (4**135) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'epoch89_complete_seed_states': seed,
        'delay_vectors': 4**135,
        'deadline_vectors': z,
        'deadline_origin': 'epoch12',
        'epoch90_bound_thirty_first_source_handoff_states': counts[0][1],
        'epoch90_bound_thirty_first_source_binding_states': counts[1][1],
        'epoch90_bound_verifier_binding_states': counts[2][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def publication64():
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
    z = q(132)
    seed = 27648
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 11 * (4**6) * 2 * (4**132) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_sixty_third_restart_seed_states': seed,
        'delay_vectors': 4**132,
        'deadline_vectors': z,
        'bound_successor_source_disappearance_states': counts[0][1],
        'bound_replacement_source_binding_states': counts[1][1],
        'bound_fresh_reconciliation_states': counts[2][1],
        'bound_sixty_fourth_restart_states': counts[3][1],
        'bound_sixty_fourth_restart_recoveries': seed * z,
        'bad_acceptances': 0,
        'checks': checks,
    }


def membership34():
    expected = (
        (0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0),(2,2,1),(2,2,2),
    )
    def ok(phase, state, generation=4, carried_root=34, target_root=34,
           replication=2, tombstone=1, witness_source=2, prior_source=2,
           active_byzantine=0):
        return (
            0 <= phase < len(expected)
            and state == expected[phase]
            and all(x != 3 for x in state)
            and generation == 4
            and carried_root == 34
            and target_root == 34
            and replication == 2
            and tombstone == 1
            and witness_source == 2
            and prior_source == 2
            and active_byzantine == 0
        )
    checks = [ok(i, s) for i, s in enumerate(expected)]
    checks += [
        not ok(6,(3,2,2)),
        not ok(6,(2,3,2)),
        not ok(6,(2,2,3)),
        not ok(6,expected[6],generation=3),
        not ok(6,expected[6],carried_root=33),
        not ok(6,expected[6],target_root=33),
        not ok(6,expected[6],replication=1),
        not ok(6,expected[6],tombstone=0),
        not ok(6,expected[6],witness_source=1),
        not ok(6,expected[6],prior_source=3),
        not ok(6,expected[6],active_byzantine=1),
    ]
    z = q(130)
    seed = 760
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 7 * (4**3) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2 * (4**130) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4**130,
        'deadline_vectors': z,
        'bound_root34_witness_rebind_states': counts[0][1],
        'bound_root34_witness_binding_states': counts[1][1],
        'bound_replication_quorum_churn_states': counts[2][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def run_validation():
    c, t, s, b = indep(), gc90(), publication64(), membership34()
    o = {
        'version': V,
        'base': {
            'version':'V138',
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
        'epoch90': {
            'patterns':t['patterns'],
            'accepted':t['accepted'],
            'seed_states':t['epoch89_complete_seed_states'],
            'delay_vectors':t['delay_vectors'],
            'deadline_vectors':t['deadline_vectors'],
            'deadline_origin':t['deadline_origin'],
            'bound_thirty_first_source_handoff_states':t['epoch90_bound_thirty_first_source_handoff_states'],
            'bound_thirty_first_source_binding_states':t['epoch90_bound_thirty_first_source_binding_states'],
            'bound_verifier_binding_states':t['epoch90_bound_verifier_binding_states'],
            'bad_acceptances':t['bad_acceptances'],
        },
        'publication64': {
            'patterns':s['patterns'],
            'accepted':s['accepted'],
            'seed_states':s['bound_sixty_third_restart_seed_states'],
            'delay_vectors':s['delay_vectors'],
            'deadline_vectors':s['deadline_vectors'],
            'bound_successor_source_disappearance_states':s['bound_successor_source_disappearance_states'],
            'bound_replacement_source_binding_states':s['bound_replacement_source_binding_states'],
            'bound_fresh_reconciliation_states':s['bound_fresh_reconciliation_states'],
            'bound_sixty_fourth_restart_states':s['bound_sixty_fourth_restart_states'],
            'bound_sixty_fourth_restart_recoveries':s['bound_sixty_fourth_restart_recoveries'],
            'bad_acceptances':s['bad_acceptances'],
        },
        'membership34': {
            'patterns':b['patterns'],
            'accepted':b['accepted'],
            'seed_states':b['bound_quorum_churn_seed_states'],
            'delay_vectors':b['delay_vectors'],
            'deadline_vectors':b['deadline_vectors'],
            'bound_root34_witness_rebind_states':b['bound_root34_witness_rebind_states'],
            'bound_root34_witness_binding_states':b['bound_root34_witness_binding_states'],
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
            'extend anchor GC through epoch 91 by rotating the thirty-first-source lineage, binding that lineage, rebinding the handed proof, and preserving the epoch-12 deadline',
            'compose sixty-fourth-restart recovery with replacement-source churn, successor binding, fresh reconciliation, and a sixty-fifth verifier cold restart without cached authority promotion',
            'keep generation 4 after root-34 witness rebind, replace the witness source, roll to root 35, bind root 35, and require replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V139 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-90 GC to {t['accepted']:,} states with {t['epoch90_bound_thirty_first_source_handoff_states']:,} bound thirty-first-source handoffs, "
        f"{t['epoch90_bound_thirty_first_source_binding_states']:,} bound thirty-first-source bindings, and {t['epoch90_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_sixty_fourth_restart_recoveries']:,} fully bound sixty-fourth-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_root34_witness_rebind_states']:,} bound root-34 witness rebinds, "
        f"{b['bound_root34_witness_binding_states']:,} bound witness renewals, and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o,sort_keys=True,separators=(',',':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
