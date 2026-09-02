#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v140 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v140.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V140'
assert a['base'] == {
    'version':'V139',
    'digest':'f4d35aa553777f77968ed2b0aaeae17c515520e4dc1086be8d02a9c90849f968',
    'implementation_sha256':'f30f3a1753f368a0d75e71bbb215f6d9a49189c79d43f5b44fd457caee564323',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc91(),m.publication65(),m.membership35()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (246836736//428536) == t['epoch90_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2320254720,447580)
assert (
    t['epoch91_bound_thirty_first_lineage_rotation_states'],
    t['epoch91_bound_thirty_first_lineage_binding_states'],
    t['epoch91_bound_handed_proof_rebind_states'],
    t['epoch91_bound_verifier_binding_states'],
) == (1804642560,1289030400,773418240,257806080)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (11086709760//400995) == s['bound_sixty_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_fifth_restart_recoveries'],
) == (127496540160,419220,11590594560)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_fifth_restart_states'],
) == (104315351040,81134161920,57952972800,34771783680)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (291312560//383306) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3352318200,400995)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root35_rollover_states'],
    b['bound_root35_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2742805800,1523781000,914268600,304756200)
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
    'distributed_winloop_v140.py',
    'winloop_v140.json',
    'winloop_v140_report.md',
    'winloop_v140_validate.py',
}
seen = set()
for line in (H/'winloop_v140_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v140.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V140',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
