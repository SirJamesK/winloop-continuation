#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v150 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v150.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V150'
assert a['base'] == {
    'version':'V149',
    'digest':'1d0c9a4f73c2c9f9c02b8e02a3c808cbb2760697f6d5cc791f620be8ee798048',
    'implementation_sha256':'cef10f9dcee25d82635eff256317bdcfef874f96687a0c254214f566f9ec602e',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc101(),m.publication75(),m.membership40()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (371494656//644956) == t['epoch100_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3472865280,669920)
assert (
    t['epoch101_bound_thirty_sixth_lineage_rotation_states'],
    t['epoch101_bound_thirty_sixth_lineage_binding_states'],
    t['epoch101_bound_handed_proof_rebind_states'],
    t['epoch101_bound_verifier_binding_states'],
) == (2701117440,1929369600,1157621760,385873920)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (16828922880//608685) == s['bound_seventy_fourth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_fifth_restart_recoveries'],
) == (192424826880,632710,17493166080)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_fifth_restart_states'],
) == (157438494720,122452162560,87465830400,52479498240)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (444809760//585276) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5088606600,608685)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root40_rollover_states'],
    b['bound_root40_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4163405400,2313003000,1387801800,462600600)
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
    'distributed_winloop_v150.py',
    'winloop_v150.json',
    'winloop_v150_report.md',
    'winloop_v150_validate.py',
}
seen = set()
for line in (H/'winloop_v150_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v150.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '398889d8d3f100250b9ef2cce03089ceba73c90894b6abed7c919e959e2aed4f'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V150',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
