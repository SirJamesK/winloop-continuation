#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v163 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v163.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V163'
assert a['base'] == {
    'version':'V162',
    'digest':'9727195879013d29b8f45b7a1388ec5d1e45209e0b2e8bd4fafca0ef95acd5b9',
    'implementation_sha256':'ade370577361937e46044d282c7a5026bd745cb2ff1ba67b35482833b1d95fba',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc114(),m.publication88(),m.membership46()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (588317184//1021384) == t['epoch113_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4254727680,1055240)
assert (
    t['epoch114_bound_forty_third_source_handoff_states'],
    t['epoch114_bound_forty_third_source_binding_states'],
    t['epoch114_bound_verifier_binding_states'],
) == (3039091200,1823454720,607818240)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (26873026560//971970) == s['bound_eighty_seventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_eighth_restart_recoveries'],
) == (305566829568,1004731,27778802688)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_eighth_restart_states'],
) == (250009224192,194451618816,138894013440,83336408064)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (714346040//939929) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5170880400,971970)
assert (
    b['bound_root46_witness_rebind_states'],
    b['bound_root46_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3693486000,2216091600,738697200)
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
    'distributed_winloop_v163.py',
    'winloop_v163.json',
    'winloop_v163_report.md',
    'winloop_v163_validate.py',
}
seen = set()
for line in (H/'winloop_v163_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v163.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '82df8e634a70151c98cab7644bcf63c2aaf1f84aba4694f8d688bcc0061f8ff6'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V163',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
