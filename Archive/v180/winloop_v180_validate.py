#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v180 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v180.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V180'
assert a['base'] == {
    'version':'V179',
    'digest':'6d830cfe5145f29b217e412b8181ed9ca0cccbe54c8c2db4fdf74cbb2a57c2db',
    'implementation_sha256':'c724781e87bdf47b7dfb22a2e16ac22bf7d8b1c20ae305b0892febe0543ff960',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc131(),m.publication105(),m.membership55()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (980937216//1703016) == t['epoch130_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (9074799360,1750540)
assert (
    t['epoch131_bound_fifty_first_lineage_rotation_states'],
    t['epoch131_bound_fifty_first_lineage_binding_states'],
    t['epoch131_bound_handed_proof_rebind_states'],
    t['epoch131_bound_verifier_binding_states'],
) == (7058177280,5041555200,3024933120,1008311040)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (45158999040//1633355) == s['bound_one_hundred_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_fifth_restart_recoveries'],
) == (510807306240,1679580,46437027840)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_fifth_restart_states'],
) == (417933250560,325059194880,232185139200,139311083520)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1206869360//1587986) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (13654847800,1633355)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root55_rollover_states'],
    b['bound_root55_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (11172148200,6206749000,3724049400,1241349800)
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
    'distributed_winloop_v180.py',
    'winloop_v180.json',
    'winloop_v180_report.md',
    'winloop_v180_validate.py',
}
seen = set()
for line in (H/'winloop_v180_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v180.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'fb9c7c992e3a40990dee4924e8be1194dfbeaff449cd38b02f9b921b5482eb70'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V180',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
