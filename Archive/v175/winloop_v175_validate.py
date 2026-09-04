#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v175 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v175.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V175'
assert a['base'] == {
    'version':'V174',
    'digest':'d3b789fd29e8ea22557e04d4927d30c19ee57a5ed19aadb6b88e65c89b2f99d3',
    'implementation_sha256':'6bb55d9d6199961128259da3a04b4f6e7d81ba08406f6c5e2fcb11604fafec20',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc126(),m.publication100(),m.membership52()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (851475456//1478256) == t['epoch125_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6134768640,1521520)
assert (
    t['epoch126_bound_forty_ninth_source_handoff_states'],
    t['epoch126_bound_forty_ninth_source_binding_states'],
    t['epoch126_bound_verifier_binding_states'],
) == (4381977600,2629186560,876395520)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (39119431680//1414910) == s['bound_ninety_ninth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundredth_restart_recoveries'],
) == (443094727680,1456935,40281338880)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundredth_restart_states'],
) == (362532049920,281969372160,201406694400,120844016640)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1044012760//1373701) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (7527321200,1414910)
assert (
    b['bound_root52_witness_rebind_states'],
    b['bound_root52_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (5376658000,3225994800,1075331600)
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
    'distributed_winloop_v175.py',
    'winloop_v175.json',
    'winloop_v175_report.md',
    'winloop_v175_validate.py',
}
seen = set()
for line in (H/'winloop_v175_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v175.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'b3589cf18702887ac108c28ac50ca62e5530367da4141655b686b73d281fe2a1'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V175',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
