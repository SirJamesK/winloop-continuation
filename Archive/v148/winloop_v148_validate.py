#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v148 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v148.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V148'
assert a['base'] == {
    'version':'V147',
    'digest':'72a40c8a509f48ddd3b72923cf81cccd00dd96d880c474208d3d60244ba0faab',
    'implementation_sha256':'49c6f1fd6e79e43303b05e227d5f7580b14768cb9236ec5950fb00ad9743575f',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc99(),m.publication73(),m.membership39()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (343816704//596904) == t['epoch98_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (3217294080,620620)
assert (
    t['epoch99_bound_thirty_fifth_lineage_rotation_states'],
    t['epoch99_bound_thirty_fifth_lineage_binding_states'],
    t['epoch99_bound_handed_proof_rebind_states'],
    t['epoch99_bound_verifier_binding_states'],
) == (2502339840,1787385600,1072431360,357477120)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (15551308800//562475) == s['bound_seventy_second_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_third_restart_recoveries'],
) == (177998819328,585276,16181710848)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_third_restart_states'],
) == (145635397632,113271975936,80908554240,48545132544)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (410608240//540274) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (4702291000,562475)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root39_rollover_states'],
    b['bound_root39_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3847329000,2137405000,1282443000,427481000)
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
    'distributed_winloop_v148.py',
    'winloop_v148.json',
    'winloop_v148_report.md',
    'winloop_v148_validate.py',
}
seen = set()
for line in (H/'winloop_v148_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v148.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '8859796c5b9e5888bff5a7e6a7e01a2f6f1a52015e65c93ea9cf387121232be2'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V148',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
