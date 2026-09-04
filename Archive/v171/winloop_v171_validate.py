#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v171 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v171.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V171'
assert a['base'] == {
    'version':'V170',
    'digest':'bde19cca2adacecbdaccb7ec8124bfbf6933750bd81749be0ae2c98c688a209f',
    'implementation_sha256':'b0b69c9be3d5bc641f1058df0cac7cd51fd1b98e26b037b79c4f85f124a1d378',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc122(),m.publication96(),m.membership50()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (756518400//1313400) == t['epoch121_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (5456908800,1353400)
assert (
    t['epoch122_bound_forty_seventh_source_handoff_states'],
    t['epoch122_bound_forty_seventh_source_binding_states'],
    t['epoch122_bound_verifier_binding_states'],
) == (3897792000,2338675200,779558400)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (34695198720//1254890) == s['bound_ninety_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_sixth_restart_recoveries'],
) == (393450089472,1293699,35768189952)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_sixth_restart_states'],
) == (321913709568,250377329664,178840949760,107304569856)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (924817400//1216865) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (6676014800,1254890)
assert (
    b['bound_root50_witness_rebind_states'],
    b['bound_root50_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4768582000,2861149200,953716400)
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
    'distributed_winloop_v171.py',
    'winloop_v171.json',
    'winloop_v171_report.md',
    'winloop_v171_validate.py',
}
seen = set()
for line in (H/'winloop_v171_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v171.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'f172d28c7de90221819e46a4117ea47ebc3d5c2d01019d71579ee7e4c9988b81'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V171',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
