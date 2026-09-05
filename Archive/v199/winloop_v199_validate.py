#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v199 as m

H = Path(__file__).resolve().parent
a = json.loads((H / 'winloop_v199.json').read_text())
assert a == m.run_validation()

assert a['version'] == 'V199'
assert a['base'] == {
    'version': 'V198',
    'digest': 'ca138afa9c8b6f868fda5bfd279cf4d5f083ea1dd7381dbed53d72601d9f0ff0',
    'implementation_sha256': '236b4651f2770a7a4fe1e635b301d771b7908d4429c19618a794b5f2801e2af9',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c, t, s, b = m.indep(), m.gc150(), m.publication124(), m.membership64()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert all(c['checks'])

assert (1591787520 // 2763520) == t['epoch149_complete_seed_states'] == 576
assert (t['accepted'], t['deadline_vectors']) == (11406753792, 2829056)
assert (
    t['epoch150_bound_sixty_first_source_handoff_states'],
    t['epoch150_bound_sixty_first_source_binding_states'],
    t['epoch150_bound_verifier_binding_states'],
) == (8147681280, 4888608768, 1629536256)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0
assert all(t['checks'])

assert (73740699648 // 2667126) == s['bound_one_hundred_twenty_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_twenty_fourth_restart_recoveries'],
) == (830614625280, 2731135, 75510420480)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_twenty_fourth_restart_states'],
) == (679593784320, 528572943360, 377552102400, 226531261440)
assert s['bad_acceptances'] == 0
assert all(s['checks'])

assert (1979135000 // 2604125) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'], b['deadline_vectors']) == (14189110320, 2667126)
assert (
    b['bound_root64_witness_rebind_states'],
    b['bound_root64_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (10135078800, 6081047280, 2027015760)
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
    'distributed_winloop_v199.py',
    'winloop_v199.json',
    'winloop_v199_report.md',
    'winloop_v199_validate.py',
}
seen = set()
for line in (H / 'winloop_v199_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H / name).read_text()), sort_keys=True, separators=(',', ':')).encode()
        if name == 'winloop_v199.json'
        else (H / name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)

assert seen == required
assert a['digest'] == '501c8219d470a49bbc8e25bbac739a1fc39f3aa4193b26f07908b1272f5b45a5'
print(json.dumps({
    'version':'V199',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
