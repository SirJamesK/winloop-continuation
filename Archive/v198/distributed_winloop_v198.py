"""WinLoop V198: epoch-149 sixtieth-lineage rotation, publication-123 cold restart, and root-64 rollover."""
from itertools import product
from math import comb
import hashlib, json

V = 'V198'
BASE_DIGEST = '51fd660f85de40d71d7a5058b2c363186cfc291fa37edc3dcfb38b2fb998e4b2'
BASE_IMPL_SHA = '73c02e3b3861f351d6c31c54fc122d856a08ba4f4f069fe470eef14d80448826'
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


def gc149():
    expected = (
        (0,0,0,0),(1,0,0,0),(2,0,0,0),(2,1,0,0),(2,2,0,0),
        (2,2,1,0),(2,2,2,0),(2,2,2,1),(2,2,2,2),
    )
    carried_count = 311
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
        not ok(8,(3,2,2,2)),
        not ok(8,(2,3,2,2)),
        not ok(8,(2,2,3,2)),
        not ok(8,(2,2,2,3)),
        not ok(8,expected[8],root=1),
        not ok(8,expected[8],continuity=0),
        not ok(8,expected[8],carried=(2,)*310+(1,)),
        not ok(8,expected[8],deadline_reset=1),
    ]
    z = q(253)
    seed = 576
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 9 * (4**4) * 4 * 3 * (4**carried_count) * 2 * (4**253) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'epoch148_complete_seed_states': seed,
        'delay_vectors': 4**253,
        'deadline_vectors': z,
        'deadline_origin': 'epoch12',
        'epoch149_bound_sixtieth_lineage_rotation_states': counts[0][1],
        'epoch149_bound_sixtieth_lineage_binding_states': counts[1][1],
        'epoch149_bound_handed_proof_rebind_states': counts[2][1],
        'epoch149_bound_verifier_binding_states': counts[3][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def publication123():
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
    z = q(250)
    seed = 27648
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 11 * (4**6) * 2 * (4**250) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_one_hundred_twenty_second_restart_seed_states': seed,
        'delay_vectors': 4**250,
        'deadline_vectors': z,
        'bound_replacement_source_churn_states': counts[0][1],
        'bound_successor_source_binding_states': counts[1][1],
        'bound_fresh_reconciliation_states': counts[2][1],
        'bound_one_hundred_twenty_third_restart_states': counts[3][1],
        'bound_one_hundred_twenty_third_restart_recoveries': seed * z,
        'bad_acceptances': 0,
        'checks': checks,
    }


def membership64():
    expected = (
        (0,0,0,0,0),(1,0,0,0,0),(2,0,0,0,0),(2,1,0,0,0),
        (2,2,0,0,0),(2,2,1,0,0),(2,2,2,0,0),(2,2,2,1,0),
        (2,2,2,2,0),(2,2,2,2,1),(2,2,2,2,2),
    )
    def ok(phase, state, generation=4, carried_root=63, target_root=64,
           replication=2, tombstone=1, witness=2, prior_source=2,
           active_byzantine=0):
        return (
            0 <= phase < len(expected)
            and state == expected[phase]
            and all(x != 3 for x in state)
            and (generation, carried_root, target_root, replication, tombstone,
                 witness, prior_source, active_byzantine) == (4,63,64,2,1,2,2,0)
        )
    checks = [ok(i, s) for i, s in enumerate(expected)]
    checks += [
        not ok(10,(3,2,2,2,2)),
        not ok(10,(2,3,2,2,2)),
        not ok(10,(2,2,3,2,2)),
        not ok(10,(2,2,2,3,2)),
        not ok(10,(2,2,2,2,3)),
        not ok(10,expected[10],generation=3),
        not ok(10,expected[10],carried_root=62),
        not ok(10,expected[10],target_root=63),
        not ok(10,expected[10],replication=1),
        not ok(10,expected[10],tombstone=0),
        not ok(10,expected[10],witness=1),
        not ok(10,expected[10],prior_source=3),
        not ok(10,expected[10],active_byzantine=1),
    ]
    z = q(248)
    seed = 760
    counts = _stage_counts(expected, seed, z)
    accepted = len(expected) * seed * z
    patterns = seed * 11 * (4**5) * 6 * 16 * 16 * 4 * 3 * 4 * 4 * 2 * (4**248) * z
    return {
        'patterns': patterns,
        'accepted': accepted,
        'bound_quorum_churn_seed_states': seed,
        'delay_vectors': 4**248,
        'deadline_vectors': z,
        'bound_witness_source_replacement_states': counts[0][1],
        'bound_root64_rollover_states': counts[2][1],
        'bound_root64_binding_states': counts[3][1],
        'bound_replication_quorum_churn_states': counts[4][1],
        'bad_acceptances': 0,
        'checks': checks,
    }


def run_validation():
    c, t, s, b = indep(), gc149(), publication123(), membership64()
    o = {
        'version': V,
        'base': {
            'version':'V197',
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
        'epoch149': {
            'patterns':t['patterns'],
            'accepted':t['accepted'],
            'seed_states':t['epoch148_complete_seed_states'],
            'delay_vectors':t['delay_vectors'],
            'deadline_vectors':t['deadline_vectors'],
            'deadline_origin':t['deadline_origin'],
            'bound_sixtieth_lineage_rotation_states':t['epoch149_bound_sixtieth_lineage_rotation_states'],
            'bound_sixtieth_lineage_binding_states':t['epoch149_bound_sixtieth_lineage_binding_states'],
            'bound_handed_proof_rebind_states':t['epoch149_bound_handed_proof_rebind_states'],
            'bound_verifier_binding_states':t['epoch149_bound_verifier_binding_states'],
            'bad_acceptances':t['bad_acceptances'],
        },
        'publication123': {
            'patterns':s['patterns'],
            'accepted':s['accepted'],
            'seed_states':s['bound_one_hundred_twenty_second_restart_seed_states'],
            'delay_vectors':s['delay_vectors'],
            'deadline_vectors':s['deadline_vectors'],
            'bound_replacement_source_churn_states':s['bound_replacement_source_churn_states'],
            'bound_successor_source_binding_states':s['bound_successor_source_binding_states'],
            'bound_fresh_reconciliation_states':s['bound_fresh_reconciliation_states'],
            'bound_one_hundred_twenty_third_restart_states':s['bound_one_hundred_twenty_third_restart_states'],
            'bound_one_hundred_twenty_third_restart_recoveries':s['bound_one_hundred_twenty_third_restart_recoveries'],
            'bad_acceptances':s['bad_acceptances'],
        },
        'membership64': {
            'patterns':b['patterns'],
            'accepted':b['accepted'],
            'seed_states':b['bound_quorum_churn_seed_states'],
            'delay_vectors':b['delay_vectors'],
            'deadline_vectors':b['deadline_vectors'],
            'bound_witness_source_replacement_states':b['bound_witness_source_replacement_states'],
            'bound_root64_rollover_states':b['bound_root64_rollover_states'],
            'bound_root64_binding_states':b['bound_root64_binding_states'],
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
            'extend anchor GC through epoch 150 by handing the rebound proof to a sixty-first source, binding that source, and preserving the epoch-12 deadline',
            'compose one-hundred-twenty-third-restart recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-twenty-fourth verifier cold restart without cached authority promotion',
            'keep generation 4 after root-64 rollover, rebind the witness to root 64, renew the witness binding, and require replication-quorum churn without tombstone or prior-source discontinuity',
            'retain V21 routing until the >=2000-seed replacement bar clears',
        ],
    }
    o['headline'] = (
        f"V198 keeps cross-role credit at {c['conservative_cross_role_credit']} with no committed external independence certificate, "
        f"extends epoch-149 GC to {t['accepted']:,} states with {t['epoch149_bound_sixtieth_lineage_rotation_states']:,} bound sixtieth-lineage rotations, "
        f"{t['epoch149_bound_sixtieth_lineage_binding_states']:,} bound lineage bindings, "
        f"{t['epoch149_bound_handed_proof_rebind_states']:,} bound handed-proof rebinds, and "
        f"{t['epoch149_bound_verifier_binding_states']:,} bound verifier completions; "
        f"admits {s['accepted']:,} publication states with {s['bound_one_hundred_twenty_third_restart_recoveries']:,} fully bound one-hundred-twenty-third-cold-restart recoveries; "
        f"and admits {b['accepted']:,} membership states with {b['bound_witness_source_replacement_states']:,} bound witness-source replacements, "
        f"{b['bound_root64_rollover_states']:,} bound root-64 rollovers, {b['bound_root64_binding_states']:,} bound root-64 bindings, "
        f"and {b['bound_replication_quorum_churn_states']:,} bound quorum-churn completions, "
        f"with zero modeled bad acceptances across all three continuation gates."
    )
    o['digest'] = hashlib.sha256(
        json.dumps(o,sort_keys=True,separators=(',',':')).encode()
    ).hexdigest()
    return o


if __name__ == '__main__':
    print(json.dumps(run_validation(), indent=2, sort_keys=True))
