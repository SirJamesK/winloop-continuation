#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v164 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v164.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V164'
assert a['base'] == {
    'version':'V163',
    'digest':'82df8e634a70151c98cab7644bcf63c2aaf1f84aba4694f8d688bcc0061f8ff6',
    'implementation_sha256':'d3a57aad4c9eae1bad93ff010e4407317951771d2b50f3d51a892efcfcbf2a2e',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc115(),m.publication89(),m.membership47()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (607818240//1055240) == t['epoch114_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (5649709824,1089836)
assert (
    t['epoch115_bound_forty_third_lineage_rotation_states'],
    t['epoch115_bound_forty_third_lineage_binding_states'],
    t['epoch115_bound_handed_proof_rebind_states'],
    t['epoch115_bound_verifier_binding_states'],
) == (4394218752,3138727680,1883236608,627745536)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (27778802688//1004731) == s['bound_eighty_eighth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_eighty_ninth_restart_recoveries'],
) == (315751772160,1038220,28704706560)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_eighty_ninth_restart_states'],
) == (258342359040,200932945920,143523532800,86114119680)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (738697200//971970) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (8399551160,1004731)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root47_rollover_states'],
    b['bound_root47_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (6872360040,3817977800,2290786680,763595560)
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
    'distributed_winloop_v164.py',
    'winloop_v164.json',
    'winloop_v164_report.md',
    'winloop_v164_validate.py',
}
seen = set()
for line in (H/'winloop_v164_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v164.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '2b0092fc11df7b3cb3a8355d95c1821ada8082708567d73ceca71a26b7793166'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V164',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
