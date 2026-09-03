#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v149 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v149.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V149'
assert a['base'] == {
    'version':'V148',
    'digest':'8859796c5b9e5888bff5a7e6a7e01a2f6f1a52015e65c93ea9cf387121232be2',
    'implementation_sha256':'955762ea633af64e9ad1b158ec614a3c0ac3211b1b77c3762caaee33fa27c7c5',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc100(),m.publication74(),m.membership39()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (357477120//620620) == t['epoch99_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2600462592,644956)
assert (
    t['epoch100_bound_thirty_sixth_source_handoff_states'],
    t['epoch100_bound_thirty_sixth_source_binding_states'],
    t['epoch100_bound_verifier_binding_states'],
) == (1857473280,1114483968,371494656)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (16181710848//585276) == s['bound_seventy_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_fourth_restart_recoveries'],
) == (185118151680,608685,16828922880)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_fourth_restart_states'],
) == (151460305920,117802460160,84144614400,50486768640)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (427481000//562475) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3113668320,585276)
assert (
    b['bound_root39_witness_rebind_states'],
    b['bound_root39_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2224048800,1334429280,444809760)
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
    'distributed_winloop_v149.py',
    'winloop_v149.json',
    'winloop_v149_report.md',
    'winloop_v149_validate.py',
}
seen = set()
for line in (H/'winloop_v149_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v149.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '1d0c9a4f73c2c9f9c02b8e02a3c808cbb2760697f6d5cc791f620be8ee798048'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V149',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
