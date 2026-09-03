#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v153 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v153.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V153'
assert a['base'] == {
    'version':'V152',
    'digest':'17430082bf575ea4328babf4df75a1b346e3fedac8fda5157d7b50d55d539658',
    'implementation_sha256':'e6403ea2b35412c4e5137f6b5d5fe369ca6282b9319f1b16ed8963e544a57ccf',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc104(),m.publication78(),m.membership41()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (415736064//721764) == t['epoch103_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3018597120,748660)
assert (
    t['epoch104_bound_thirty_eighth_source_handoff_states'],
    t['epoch104_bound_thirty_eighth_source_binding_states'],
    t['epoch104_bound_verifier_binding_states'],
) == (2156140800,1293684480,431228160)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (18873630720//682640) == s['bound_seventy_seventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_eighth_restart_recoveries'],
) == (215493239808,708561,19590294528)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_eighth_restart_states'],
) == (176312650752,137132061696,97951472640,58770883584)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (499592840//657359) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3631644800,682640)
assert (
    b['bound_root41_witness_rebind_states'],
    b['bound_root41_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2594032000,1556419200,518806400)
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
    'distributed_winloop_v153.py',
    'winloop_v153.json',
    'winloop_v153_report.md',
    'winloop_v153_validate.py',
}
seen = set()
for line in (H/'winloop_v153_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v153.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '34b2597dfdc52db53fc6d8af5451852420af1c78150edb28159df60eec7d9610'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V153',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
