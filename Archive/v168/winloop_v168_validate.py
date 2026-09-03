#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v168 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v168.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V168'
assert a['base'] == {
    'version':'V167',
    'digest':'afc726e917e537c41d479ccfcc1a5e542aa1adcefc449ce9cad6386ebeae7738',
    'implementation_sha256':'c7377a493468d804715eaf1706fc15dd313dfc600362450daac7c8d1834ec831',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc119(),m.publication93(),m.membership49()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (690130944//1198144) == t['epoch118_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (6406283520,1235780)
assert (
    t['epoch119_bound_forty_fifth_lineage_rotation_states'],
    t['epoch119_bound_forty_fifth_lineage_binding_states'],
    t['epoch119_bound_handed_proof_rebind_states'],
    t['epoch119_bound_verifier_binding_states'],
) == (4982664960,3559046400,2135427840,711809280)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (31605396480//1143135) == s['bound_ninety_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_third_restart_recoveries'],
) == (358754254848,1179616,32614023168)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_third_restart_states'],
) == (293526208512,228298162176,163070115840,97842069504)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (841634640//1107414) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (9556608600,1143135)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root49_rollover_states'],
    b['bound_root49_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (7819043400,4343913000,2606347800,868782600)
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
    'distributed_winloop_v168.py',
    'winloop_v168.json',
    'winloop_v168_report.md',
    'winloop_v168_validate.py',
}
seen = set()
for line in (H/'winloop_v168_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v168.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '2d048fd162c2e32fcb3d5c989ac231da522fb23c0fa2673737d492ca0413e0a8'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V168',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
