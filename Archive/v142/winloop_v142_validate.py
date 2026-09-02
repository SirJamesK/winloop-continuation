#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v142 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v142.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V142'
assert a['base'] == {
    'version':'V141',
    'digest':'76c0966e707da82a1ce441e559e87e70a9f6b5d4e62c94e3496c763f79dd8b72',
    'implementation_sha256':'91bcf4fc858cec4637f5994bba758074b7c9551b15c6b8e74ab8cfc50cfadb25',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc93(),m.publication67(),m.membership36()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (269095680//467180) == t['epoch92_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2526391296,487344)
assert (
    t['epoch93_bound_thirty_second_lineage_rotation_states'],
    t['epoch93_bound_thirty_second_lineage_binding_states'],
    t['epoch93_bound_handed_proof_rebind_states'],
    t['epoch93_bound_verifier_binding_states'],
) == (1964971008,1403550720,842130432,280710144)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (12109519872//437989) == s['bound_sixty_sixth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_seventh_restart_recoveries'],
) == (139080775680,457310,12643706880)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_seventh_restart_states'],
) == (113793361920,88505948160,63218534400,37931120640)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (318607200//419220) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3661588040,437989)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root36_rollover_states'],
    b['bound_root36_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (2995844760,1664358200,998614920,332871640)
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
    'distributed_winloop_v142.py',
    'winloop_v142.json',
    'winloop_v142_report.md',
    'winloop_v142_validate.py',
}
seen = set()
for line in (H/'winloop_v142_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v142.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '5a774e0cd53a4547d916be1d8dfc945be4149fc7bd99085436b2d9891ecfb8fe'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V142',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
