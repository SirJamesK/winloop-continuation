#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v158 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v158.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V158'
assert a['base'] == {
    'version':'V157',
    'digest':'3804b07e96cb5d35586c9472e4deff835af0fb966d340330b588d83fb6d43973',
    'implementation_sha256':'9868da75f0937a6987ed88e13a1dc6cf6830c892357940f9ee5bd59731a18a8f',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc109(),m.publication83(),m.membership44()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (497044224//862924) == t['epoch108_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4630348800,893200)
assert (
    t['epoch109_bound_fortieth_lineage_rotation_states'],
    t['epoch109_bound_fortieth_lineage_binding_states'],
    t['epoch109_bound_handed_proof_rebind_states'],
    t['epoch109_bound_verifier_binding_states'],
) == (3601382400,2572416000,1543449600,514483200)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (22638320640//818805) == s['bound_eighty_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_third_restart_recoveries'],
) == (257914533888,848046,23446775808)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_third_restart_states'],
) == (211020982272,164127430656,117233879040,70340327424)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (600585440//790244) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (6845209800,818805)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root44_rollover_states'],
    b['bound_root44_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (5600626200,3111459000,1866875400,622291800)
assert b['bad_acceptances'] == 0 and all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,'max_lag':64,'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v158.py',
    'winloop_v158.json',
    'winloop_v158_report.md',
    'winloop_v158_validate.py',
}
seen = set()
for line in (H/'winloop_v158_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v158.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'f3d3df7343986d4f4ea79d6bb9d2024a923732a5bac4328e1c60f88792484a47'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V158',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
