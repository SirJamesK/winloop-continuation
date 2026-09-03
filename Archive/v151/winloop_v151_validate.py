#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v151 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v151.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V151'
assert a['base'] == {
    'version':'V150',
    'digest':'398889d8d3f100250b9ef2cce03089ceba73c90894b6abed7c919e959e2aed4f',
    'implementation_sha256':'777cc3ff4d9c844083997dcbc7fd1f1a4da8ae574a759506687ca01eebda2f37',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc102(),m.publication76(),m.membership40()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (385873920//669920) == t['epoch101_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2804336640,695520)
assert (
    t['epoch102_bound_thirty_seventh_source_handoff_states'],
    t['epoch102_bound_thirty_seventh_source_binding_states'],
    t['epoch102_bound_verifier_binding_states'],
) == (2003097600,1201858560,400619520)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (17493166080//632710) == s['bound_seventy_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_sixth_restart_recoveries'],
) == (199921277952,657359,18174661632)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_sixth_restart_states'],
) == (163571954688,127222631424,90873308160,54523984896)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (462600600//608685) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3366017200,632710)
assert (
    b['bound_root40_witness_rebind_states'],
    b['bound_root40_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2404298000,1442578800,480859600)
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
    'distributed_winloop_v151.py',
    'winloop_v151.json',
    'winloop_v151_report.md',
    'winloop_v151_validate.py',
}
seen = set()
for line in (H/'winloop_v151_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v151.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '3afea34a05ffd64d6f4e5612bfb759c008ed598e196794a5b4b2a446496faf7f'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V151',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
