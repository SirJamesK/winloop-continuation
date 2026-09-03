#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v147 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v147.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V147'
assert a['base'] == {
    'version':'V146',
    'digest':'0b334216ca86ccf3156d201e0aa8543ed412a0dba574c75accef95f406670cda',
    'implementation_sha256':'a426e470d9713f81ca1bac0346c4df3ffbba44d4cc4cf74f5e4e0012421ba2d6',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc98(),m.publication72(),m.membership38()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (330508800//573800) == t['epoch97_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2406716928,596904)
assert (
    t['epoch98_bound_thirty_fifth_source_handoff_states'],
    t['epoch98_bound_thirty_fifth_source_binding_states'],
    t['epoch98_bound_verifier_binding_states'],
) == (1719083520,1031450112,343816704)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (14937495552//540274) == s['bound_seventy_first_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_second_restart_recoveries'],
) == (171064396800,562475,15551308800)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_second_restart_states'],
) == (139961779200,108859161600,77756544000,46653926400)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (394185400//518665) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2874257680,540274)
assert (
    b['bound_root38_witness_rebind_states'],
    b['bound_root38_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2053041200,1231824720,410608240)
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
    'distributed_winloop_v147.py',
    'winloop_v147.json',
    'winloop_v147_report.md',
    'winloop_v147_validate.py',
}
seen = set()
for line in (H/'winloop_v147_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v147.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '72a40c8a509f48ddd3b72923cf81cccd00dd96d880c474208d3d60244ba0faab'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V147',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
