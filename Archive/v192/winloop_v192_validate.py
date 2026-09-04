#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v192 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v192.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V192'
assert a['base'] == {
    'version': 'V191',
    'digest': '74e491bd9d07ad9ad7ae4a2acf1015ab516f7d5ff146aa24416d47e3fa4c7e99',
    'implementation_sha256': '84fe7bd6b475f7e56461ae38815227f08097f764a670f6f36f7ccda1208ee3a9',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc143(), m.publication117(), m.membership61()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1343738880 // 2332880) == t['epoch142_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (12397245696, 2391444)
assert (
    t['epoch143_bound_fifty_seventh_lineage_rotation_states'],
    t['epoch143_bound_fifty_seventh_lineage_binding_states'],
    t['epoch143_bound_handed_proof_rebind_states'],
    t['epoch143_bound_verifier_binding_states'],
) == (9642302208, 6887358720, 4132415232, 1377471744)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (62120604672 // 2246839) == s['bound_one_hundred_sixteenth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_seventeenth_restart_recoveries'],
) == (700698746880, 2303960, 63699886080)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_seventeenth_restart_states'],
) == (573298974720, 445899202560, 318499430400, 191099658240)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1664909200 // 2190670) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (18783574040, 2246839)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root61_rollover_states'],
    b['bound_root61_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (15368378760, 8537988200, 5122792920, 1707597640)
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
    'distributed_winloop_v192.py',
    'winloop_v192.json',
    'winloop_v192_report.md',
    'winloop_v192_validate.py',
}
seen = set()
for line in (H / 'winloop_v192_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v192.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '5d8a590b0829aab473c44a606c569f82a54d2c7c1b63654cbe9ec7b9fbcc1bdb'
print(json.dumps({
    'version':'V192',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
