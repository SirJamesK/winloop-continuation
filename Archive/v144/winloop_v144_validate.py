#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v144 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v144.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V144'
assert a['base'] == {
    'version':'V143',
    'digest':'b1a9bd98e58e2c8f9da9c853c1894471776af1aa6781ea183b7bf9fda1ad3017',
    'implementation_sha256':'46112be6a5c931b7bfb053e162c3e4f4a1fed81ca22df85a7aaef16b0308929b',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc95(),m.publication69(),m.membership37()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (292654080//508080) == t['epoch94_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2744388864,529396)
assert (
    t['epoch95_bound_thirty_third_lineage_rotation_states'],
    t['epoch95_bound_thirty_third_lineage_binding_states'],
    t['epoch95_bound_handed_proof_rebind_states'],
    t['epoch95_bound_verifier_binding_states'],
) == (2134524672,1524660480,914796288,304932096)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (13193376768//477191) == s['bound_sixty_eighth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_sixty_ninth_restart_recoveries'],
) == (151346257920,497640,13758750720)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_sixty_ninth_restart_states'],
) == (123828756480,96311255040,68793753600,41276252160)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (347555600//457310) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (3989316760,477191)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root37_rollover_states'],
    b['bound_root37_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3263986440,1813325800,1087995480,362665160)
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
    'distributed_winloop_v144.py',
    'winloop_v144.json',
    'winloop_v144_report.md',
    'winloop_v144_validate.py',
}
seen = set()
for line in (H/'winloop_v144_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v144.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '4c10b24d11b22884ff40ff4c8f4c8b02452bace93f4fe1ae0d9898631cc3e8cd'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V144',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
