#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v145 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v145.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V145'
assert a['base'] == {
    'version':'V144',
    'digest':'4c10b24d11b22884ff40ff4c8f4c8b02452bace93f4fe1ae0d9898631cc3e8cd',
    'implementation_sha256':'f9e087367cdb8e872549c8b65cd0669de145cae97a802e0574b5526712dc02eb',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc96(),m.publication70(),m.membership37()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (304932096//529396) == t['epoch95_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2222841600,551300)
assert (
    t['epoch96_bound_thirty_fourth_source_handoff_states'],
    t['epoch96_bound_thirty_fourth_source_binding_states'],
    t['epoch96_bound_verifier_binding_states'],
) == (1587744000,952646400,317548800)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (13758750720//497640) == s['bound_sixty_ninth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventieth_restart_recoveries'],
) == (157740549120,518665,14340049920)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventieth_restart_states'],
) == (129060449280,100380349440,71700249600,43020149760)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (362665160//477191) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2647444800,497640)
assert (
    b['bound_root37_witness_rebind_states'],
    b['bound_root37_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1891032000,1134619200,378206400)
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
    'distributed_winloop_v145.py',
    'winloop_v145.json',
    'winloop_v145_report.md',
    'winloop_v145_validate.py',
}
seen = set()
for line in (H/'winloop_v145_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v145.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'dc9a49657e56df55bd418956d572b97c3150bfa4ba34b4da36a173251ffaad57'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V145',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
