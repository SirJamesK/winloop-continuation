#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v154 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v154.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V154'
assert a['base'] == {
    'version':'V153',
    'digest':'34b2597dfdc52db53fc6d8af5451852420af1c78150edb28159df60eec7d9610',
    'implementation_sha256':'18e20967e7550d18d659ac7263e9f45d32b3f1d9293796ae2a98f2098d474835',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc105(),m.publication79(),m.membership42()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (431228160//748660) == t['epoch104_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (4023903744,776216)
assert (
    t['epoch105_bound_thirty_eighth_lineage_rotation_states'],
    t['epoch105_bound_thirty_eighth_lineage_binding_states'],
    t['epoch105_bound_handed_proof_rebind_states'],
    t['epoch105_bound_verifier_binding_states'],
) == (3129702912,2235502080,1341301248,447100416)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (19590294528//708561) == s['bound_seventy_eighth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_ninth_restart_recoveries'],
) == (223573616640,735130,20324874240)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_ninth_restart_states'],
) == (182923868160,142274119680,101624371200,60974622720)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (518806400//682640) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5923569960,708561)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root42_rollover_states'],
    b['bound_root42_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4846557240,2692531800,1615519080,538506360)
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
    'distributed_winloop_v154.py',
    'winloop_v154.json',
    'winloop_v154_report.md',
    'winloop_v154_validate.py',
}
seen = set()
for line in (H/'winloop_v154_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v154.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'd6fa08811511c3dd75c3abc6bbfa8e993625e874c20d13702d9a1548513eaf76'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V154',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
