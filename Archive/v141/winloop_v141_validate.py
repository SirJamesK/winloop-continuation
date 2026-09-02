#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v141 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v141.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V141'
assert a['base'] == {
    'version':'V140',
    'digest':'26f33253f2a902c2938a7cea71690b590d831e83749ada51f221c1d307e5a43f',
    'implementation_sha256':'927f63c99c57eeacef147f1256838e65af6f428c9e66cb56016bb5605bde14a0',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc92(),m.publication66(),m.membership35()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (257806080//447580) == t['epoch91_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (1883669760,467180)
assert (
    t['epoch92_bound_thirty_second_source_handoff_states'],
    t['epoch92_bound_thirty_second_source_binding_states'],
    t['epoch92_bound_verifier_binding_states'],
) == (1345478400,807287040,269095680)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (11590594560//419220) == s['bound_sixty_fifth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_sixth_restart_recoveries'],
) == (133204718592,437989,12109519872)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_sixth_restart_states'],
) == (108985678848,84766639104,60547599360,36328559616)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (304756200//400995) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (2230250400,419220)
assert (
    b['bound_root35_witness_rebind_states'],
    b['bound_root35_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (1593036000,955821600,318607200)
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
    'distributed_winloop_v141.py',
    'winloop_v141.json',
    'winloop_v141_report.md',
    'winloop_v141_validate.py',
}
seen = set()
for line in (H/'winloop_v141_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v141.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V141',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
