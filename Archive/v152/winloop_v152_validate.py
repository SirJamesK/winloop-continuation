#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v152 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v152.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V152'
assert a['base'] == {
    'version':'V151',
    'digest':'3afea34a05ffd64d6f4e5612bfb759c008ed598e196794a5b4b2a446496faf7f',
    'implementation_sha256':'c3d6363a8347b060077d68523adf4773210a81cbfa3f4b19f4b01a056e7c8a6c',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc103(),m.publication77(),m.membership41()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (400619520//695520) == t['epoch102_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3741624576,721764)
assert (
    t['epoch103_bound_thirty_seventh_lineage_rotation_states'],
    t['epoch103_bound_thirty_seventh_lineage_binding_states'],
    t['epoch103_bound_handed_proof_rebind_states'],
    t['epoch103_bound_verifier_binding_states'],
) == (2910152448,2078680320,1247208192,415736064)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (18174661632//657359) == s['bound_seventy_sixth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_seventh_restart_recoveries'],
) == (207609937920,682640,18873630720)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_seventh_restart_states'],
) == (169862676480,132115415040,94368153600,56620892160)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (480859600//632710) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (5495521240,657359)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root41_rollover_states'],
    b['bound_root41_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (4496335560,2497964200,1498778520,499592840)
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
    'distributed_winloop_v152.py',
    'winloop_v152.json',
    'winloop_v152_report.md',
    'winloop_v152_validate.py',
}
seen = set()
for line in (H/'winloop_v152_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v152.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '17430082bf575ea4328babf4df75a1b346e3fedac8fda5157d7b50d55d539658'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V152',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
