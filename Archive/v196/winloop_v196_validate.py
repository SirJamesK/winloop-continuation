#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v196 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v196.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V196'
assert a['base'] == {
    'version': 'V195',
    'digest': 'da273f02429d022773cca5ecb8c28ed0ea127a309969e092cdb1190736259617',
    'implementation_sha256': '67b389a983e1e4f5ee9eb8dd03eff4f63d5e8298c25e5da6c84fa2c5ff74af9e',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc147(), m.publication121(), m.membership63()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1482048000 // 2573000) == t['epoch146_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (13662432000, 2635500)
assert (
    t['epoch147_bound_fifty_ninth_lineage_rotation_states'],
    t['epoch147_bound_fifty_ninth_lineage_binding_states'],
    t['epoch147_bound_handed_proof_rebind_states'],
    t['epoch147_bound_verifier_binding_states'],
) == (10626336000, 7590240000, 4554144000, 1518048000)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (68597867520 // 2481115) == s['bound_one_hundred_twentieth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_first_restart_recoveries'],
) == (773131087872, 2542124, 70284644352)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_first_restart_states'],
) == (632561799168, 491992510464, 351423221760, 210853933056)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1840028400 // 2421090) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (20742121400, 2481115)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root63_rollover_states'],
    b['bound_root63_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (16970826600, 9428237000, 5656942200, 1885647400)
assert b['bad_acceptances'] == 0
assert all(b['checks'])

assert a['temporal_floor_regression'] == {
    'roots':22,'horizon':22,'floor':1,'budget':851,
    'h11_floor':2,'h11_budget':398,'carried_from':'V66',
}
assert a['checkpoint_recovery'] == {
    'statements':513,
    'max_lag':64,
    'shared_audit':'132 + 4*k',
    'frontier_storage_only':True,
    'trust_bearing_messages_unchanged':True,
}

required = {
    'distributed_winloop_v196.py',
    'winloop_v196.json',
    'winloop_v196_report.md',
    'winloop_v196_validate.py',
}
seen = set()
for line in (H / 'winloop_v196_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v196.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'd8b8c6225c2254ae4ba26b608e8fb79a3ba8e0fda342c32fd90d7ce8254cbd61'
print(json.dumps({
    'version':'V196',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
