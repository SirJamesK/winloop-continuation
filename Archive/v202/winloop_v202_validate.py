#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v202 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v202.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V202'
assert a['base'] == {
    'version': 'V201',
    'digest': '452003633bf644ddc617ae166900bf18d19595410343e46eab3c2770070ded00',
    'implementation_sha256': '1349a415a8419a85dde0bfcf3aa3590efff45f95b7ab6baa6d441b2885279628',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc153(), m.publication127(), m.membership66()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1706814720 // 2963220) == t['epoch152_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (15717182976, 3031864)
assert (
    t['epoch153_bound_sixty_second_lineage_rotation_states'],
    t['epoch153_bound_sixty_second_lineage_binding_states'],
    t['epoch153_bound_handed_proof_rebind_states'],
    t['epoch153_bound_verifier_binding_states'],
) == (12224475648, 8731768320, 5239060992, 1746353664)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (79134354432 // 2862209) == s['bound_one_hundred_twenty_sixth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_seventh_restart_recoveries'],
) == (890879109120, 2929290, 80989009920)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_seventh_restart_states'],
) == (728901089280, 566923069440, 404945049600, 242967029760)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (2125081600 // 2796160) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (23928067240, 2862209)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root66_rollover_states'],
    b['bound_root66_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (19577509560, 10876394200, 6525836520, 2175278840)
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
    'distributed_winloop_v202.py',
    'winloop_v202.json',
    'winloop_v202_report.md',
    'winloop_v202_validate.py',
}
seen = set()
for line in (H / 'winloop_v202_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v202.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == 'e194d32b893a6b83e899bb34a19462d0cb6826210541ab5c4ad689f7f31de56f'
print(json.dumps({
    'version':'V202',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
