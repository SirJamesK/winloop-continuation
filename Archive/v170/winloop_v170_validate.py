#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v170 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v170.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V170'
assert a['base'] == {
    'version':'V169',
    'digest':'0f9ac6b0c9a51bb20da324c5d429b049c1055fa649b6a1ec5208e2106fdc8ffb',
    'implementation_sha256':'134550703fd4eaa035434431dd3c505d5b56f2561ae84d34f58c5f4a611ec282',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc121(),m.publication95(),m.membership50()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (733936896//1274196) == t['epoch120_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6808665600,1313400)
assert (
    t['epoch121_bound_forty_sixth_lineage_rotation_states'],
    t['epoch121_bound_forty_sixth_lineage_binding_states'],
    t['epoch121_bound_handed_proof_rebind_states'],
    t['epoch121_bound_verifier_binding_states'],
) == (5295628800,3782592000,2269555200,756518400)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (33643883520//1216865) == s['bound_ninety_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_fifth_restart_recoveries'],
) == (381647185920,1254890,34695198720)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_fifth_restart_states'],
) == (312256788480,242866391040,173475993600,104085596160)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (896508160//1179616) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (10172991400,1216865)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root50_rollover_states'],
    b['bound_root50_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (8323356600,4624087000,2774452200,924817400)
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
    'distributed_winloop_v170.py',
    'winloop_v170.json',
    'winloop_v170_report.md',
    'winloop_v170_validate.py',
}
seen = set()
for line in (H/'winloop_v170_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v170.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'bde19cca2adacecbdaccb7ec8124bfbf6933750bd81749be0ae2c98c688a209f'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V170',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
