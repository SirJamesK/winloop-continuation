#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v179 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v179.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V179'
assert a['base'] == {
    'version':'V178',
    'digest':'4322827075fb701a166d4eb76162355dbd77fe3d23745ca529c404183a35db08',
    'implementation_sha256':'a8ced41416d596db6a41c3b22bb2208b69488e46ef6172a361971ec46f6fb761',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc130(),m.publication104(),m.membership54()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (954063360//1656360) == t['epoch129_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6866560512,1703016)
assert (
    t['epoch130_bound_fifty_first_source_handoff_states'],
    t['epoch130_bound_fifty_first_source_binding_states'],
    t['epoch130_bound_verifier_binding_states'],
) == (4904686080,2942811648,980937216)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (43904636928//1587986) == s['bound_one_hundred_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_fourth_restart_recoveries'],
) == (496748989440,1633355,45158999040)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_fourth_restart_states'],
) == (406430991360,316112993280,225794995200,135476997120)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1173033400//1543465) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (8448085520,1587986)
assert (
    b['bound_root54_witness_rebind_states'],
    b['bound_root54_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (6034346800,3620608080,1206869360)
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
    'distributed_winloop_v179.py',
    'winloop_v179.json',
    'winloop_v179_report.md',
    'winloop_v179_validate.py',
}
seen = set()
for line in (H/'winloop_v179_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v179.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '6d830cfe5145f29b217e412b8181ed9ca0cccbe54c8c2db4fdf74cbb2a57c2db'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V179',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
