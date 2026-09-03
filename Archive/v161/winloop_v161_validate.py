#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v161 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v161.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V161'
assert a['base'] == {
    'version':'V160',
    'digest':'bfe50fea5241d4d06161ae84b40c7ae64443aed6b1b54d875922b291df242284',
    'implementation_sha256':'0b8f6a2d0bbd3e7ac17f7f2d5cd8033be5ed7554fd35ff9d299485e6f2e35af9',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc112(),m.publication86(),m.membership45()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (550575360//955860) == t['epoch111_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3984664320,988260)
assert (
    t['epoch112_bound_forty_second_source_handoff_states'],
    t['epoch112_bound_forty_second_source_binding_states'],
    t['epoch112_bound_verifier_binding_states'],
) == (2846188800,1707713280,569237760)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (25120972800//908600) == s['bound_eighty_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_sixth_restart_recoveries'],
) == (285858726912,939929,25987156992)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_sixth_restart_states'],
) == (233884412928,181910098944,129935784960,77961470976)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (667261000//877975) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (4833752000,908600)
assert (
    b['bound_root45_witness_rebind_states'],
    b['bound_root45_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3452680000,2071608000,690536000)
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
    'distributed_winloop_v161.py',
    'winloop_v161.json',
    'winloop_v161_report.md',
    'winloop_v161_validate.py',
}
seen = set()
for line in (H/'winloop_v161_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v161.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '86c9f6d0247009fcb27d1fa3577c4a4c5d8e47d2bb681113b4abdeffb478dd6d'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V161',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
