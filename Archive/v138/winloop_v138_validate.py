#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v138 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v138.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V138'
assert a['base'] == {
    'version':'V137',
    'digest':'5cc2db015b3c0df4faa87efb3dc927fb80f5f87d31790cab791788059e7b5352',
    'implementation_sha256':'802bed4662e3cb1c297c2f80684bcb7bc83674549cfcc2b5b2dc21e415ea1107',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc89(),m.publication63(),m.membership34()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (225840384//392084) == t['epoch88_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2125647360,410040)
assert (
    t['epoch89_bound_thirtieth_lineage_rotation_states'],
    t['epoch89_bound_thirtieth_lineage_binding_states'],
    t['epoch89_bound_handed_proof_rebind_states'],
    t['epoch89_bound_verifier_binding_states'],
) == (1653281280,1180915200,708549120,236183040)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (10123176960//366145) == s['bound_sixty_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_third_restart_recoveries'],
) == (116574087168,383306,10597644288)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_third_restart_states'],
) == (95378798592,74183510016,52988221440,31792932864)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (265623040//349504) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3060972200,366145)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root34_rollover_states'],
    b['bound_root34_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2504431800,1391351000,834810600,278270200)
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
    'distributed_winloop_v138.py',
    'winloop_v138.json',
    'winloop_v138_report.md',
    'winloop_v138_validate.py',
}
seen = set()
for line in (H/'winloop_v138_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v138.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V138',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
