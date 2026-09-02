#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v143 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v143.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V143'
assert a['base'] == {
    'version':'V142',
    'digest':'5a774e0cd53a4547d916be1d8dfc945be4149fc7bd99085436b2d9891ecfb8fe',
    'implementation_sha256':'e700555b44e98620ec073a2379c686971d6619cc6677fe28884f91a0ef8367bf',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc94(),m.publication68(),m.membership36()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (280710144//487344) == t['epoch93_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2048578560,508080)
assert (
    t['epoch94_bound_thirty_third_source_handoff_states'],
    t['epoch94_bound_thirty_third_source_binding_states'],
    t['epoch94_bound_verifier_binding_states'],
) == (1463270400,877962240,292654080)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (12643706880//457310) == s['bound_sixty_seventh_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_eighth_restart_recoveries'],
) == (145127144448,477191,13193376768)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_eighth_restart_states'],
) == (118740390912,92353637376,65966883840,39580130304)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (332871640//437989) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2432889200,457310)
assert (
    b['bound_root36_witness_rebind_states'],
    b['bound_root36_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1737778000,1042666800,347555600)
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
    'distributed_winloop_v143.py',
    'winloop_v143.json',
    'winloop_v143_report.md',
    'winloop_v143_validate.py',
}
seen = set()
for line in (H/'winloop_v143_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v143.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'b1a9bd98e58e2c8f9da9c853c1894471776af1aa6781ea183b7bf9fda1ad3017'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V143',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
