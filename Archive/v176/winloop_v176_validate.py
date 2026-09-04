#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v176 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v176.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V176'
assert a['base'] == {
    'version':'V175',
    'digest':'b3589cf18702887ac108c28ac50ca62e5530367da4141655b686b73d281fe2a1',
    'implementation_sha256':'ac80ad7bbc8cad5b33a74e38433ff63aae0d201fdad6876cb327ac8c909db39d',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc127(),m.publication101(),m.membership53()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (876395520//1521520) == t['epoch126_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (8116174080,1565620)
assert (
    t['epoch127_bound_forty_ninth_lineage_rotation_states'],
    t['epoch127_bound_forty_ninth_lineage_binding_states'],
    t['epoch127_bound_handed_proof_rebind_states'],
    t['epoch127_bound_verifier_binding_states'],
) == (6312579840,4508985600,2705391360,901797120)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (40281338880//1456935) == s['bound_one_hundredth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_one_hundred_first_restart_recoveries'],
) == (456126308352,1499784,41466028032)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_one_hundred_first_restart_states'],
) == (373194252288,290262196224,207330140160,124398084096)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (1075331600//1414910) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (12179976600,1456935)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root53_rollover_states'],
    b['bound_root53_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (9965435400,5536353000,3321811800,1107270600)
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
    'distributed_winloop_v176.py',
    'winloop_v176.json',
    'winloop_v176_report.md',
    'winloop_v176_validate.py',
}
seen = set()
for line in (H/'winloop_v176_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v176.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == 'de949b3d39a81afdd9231d464506ed6de8fbb9003cafa8dc88ac3720f9f68d92'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V176',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
