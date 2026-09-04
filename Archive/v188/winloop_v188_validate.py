#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v188 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v188.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V188'
assert a['base'] == {
    'version': 'V187',
    'digest': 'b505e22669e9e070113c712e81b9359d1cda67604fda40e48ba8e8ea71c3a827',
    'implementation_sha256': '58321d9c9c98539725b880dc245129a3133a9a1a706a552ecccf78a28534c2d3',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc139(), m.publication113(), m.membership59()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1214313984 // 2108184) == t['epoch138_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (11212680960, 2162940)
assert (
    t['epoch139_bound_fifty_fifth_lineage_rotation_states'],
    t['epoch139_bound_fifty_fifth_lineage_binding_states'],
    t['epoch139_bound_handed_proof_rebind_states'],
    t['epoch139_bound_verifier_binding_states'],
) == (8720974080, 6229267200, 3737560320, 1245853440)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (56064476160 // 2027795) == s['bound_one_hundred_twelfth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_thirteenth_restart_recoveries'],
) == (632937811968, 2081156, 57539801088)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_thirteenth_restart_states'],
) == (517858209792, 402778607616, 287699005440, 172619403264)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1501269040 // 1975354) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (16952366200, 2027795)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root59_rollover_states'],
    b['bound_root59_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (13870117800, 7705621000, 4623372600, 1541124200)
assert b['bad_acceptances'] == 0
assert all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,
    'max_lag':64,
    'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,
    'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v188.py',
    'winloop_v188.json',
    'winloop_v188_report.md',
    'winloop_v188_validate.py',
}
seen = set()
for line in (H / 'winloop_v188_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v188.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'eac0be515ec185bc4a59aa8064cb29d6bddb3eff8ccaa393ae292e0cb2ba1d1f'
print(json.dumps({
    'version':'V188',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
