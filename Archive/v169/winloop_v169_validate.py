#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v169 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v169.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V169'
assert a['base'] == {
    'version':'V168',
    'digest':'2d048fd162c2e32fcb3d5c989ac231da522fb23c0fa2673737d492ca0413e0a8',
    'implementation_sha256':'bda2c17270c8e18467fd8081e630cc3248a0aab7c888f2088915a543aa4ea118',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc120(),m.publication94(),m.membership49()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (711809280//1235780) == t['epoch119_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (5137558272,1274196)
assert (
    t['epoch120_bound_forty_sixth_source_handoff_states'],
    t['epoch120_bound_forty_sixth_source_binding_states'],
    t['epoch120_bound_verifier_binding_states'],
) == (3669684480,2201810688,733936896)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (32614023168//1179616) == s['bound_ninety_third_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_ninety_fourth_restart_recoveries'],
) == (370082718720,1216865,33643883520)
assert (
    s['bound_successor_source_disappearance_states'],
    s['bound_replacement_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_ninety_fourth_restart_states'],
) == (302794951680,235507184640,168219417600,100931650560)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (868782600//1143135) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (6275557120,1179616)
assert (
    b['bound_root49_witness_rebind_states'],
    b['bound_root49_witness_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4482540800,2689524480,896508160)
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
    'distributed_winloop_v169.py',
    'winloop_v169.json',
    'winloop_v169_report.md',
    'winloop_v169_validate.py',
}
seen = set()
for line in (H/'winloop_v169_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v169.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '0f9ac6b0c9a51bb20da324c5d429b049c1055fa649b6a1ec5208e2106fdc8ffb'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V169',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
