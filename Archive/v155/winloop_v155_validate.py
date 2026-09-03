#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v155 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v155.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V155'
assert a['base'] == {
    'version':'V154',
    'digest':'d6fa08811511c3dd75c3abc6bbfa8e993625e874c20d13702d9a1548513eaf76',
    'implementation_sha256':'5dbb2af22d761d624a9bc16845ecad8c4c8b57784cd3251451cbbc2799dabd3d',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc106(),m.publication80(),m.membership42()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (447100416//776216) == t['epoch105_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3243502080,804440)
assert (
    t['epoch106_bound_thirty_ninth_source_handoff_states'],
    t['epoch106_bound_thirty_ninth_source_binding_states'],
    t['epoch106_bound_verifier_binding_states'],
) == (2316787200,1390072320,463357440)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (20324874240//735130) == s['bound_seventy_ninth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eightieth_restart_recoveries'],
) == (231853501440,762355,21077591040)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eightieth_restart_states'],
) == (189698319360,147543137280,105387955200,63232773120)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (538506360//708561) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3910891600,735130)
assert (
    b['bound_root42_witness_rebind_states'],
    b['bound_root42_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2793494000,1676096400,558698800)
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
    'distributed_winloop_v155.py',
    'winloop_v155.json',
    'winloop_v155_report.md',
    'winloop_v155_validate.py',
}
seen = set()
for line in (H/'winloop_v155_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v155.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'a2f8a8f3cfe1397b12cbb3367fc4c8ea148cfc863ed4be9b4e4fb6765677047e'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V155',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
