#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
import distributed_winloop_v146 as m

H = Path(__file__).resolve().parent
a = json.loads((H/'winloop_v146.json').read_text())

assert a == m.run_validation()
assert a['version'] == 'V146'
assert a['base'] == {
    'version':'V145',
    'digest':'dc9a49657e56df55bd418956d572b97c3150bfa4ba34b4da36a173251ffaad57',
    'implementation_sha256':'76967c68d4aafebcae5b1cc8e8a651e42163aafdb15b61c5ea1386b05bffdaa1',
}
assert a['admission'] == {'joint':21,'provenance':22,'lower':63,'preserved':True}
assert a['routing'] == {'active':'V21 guarded','replacement':False}
assert not a['runtime']['new_routing_envelope']

c,t,s,b = m.indep(),m.gc97(),m.publication71(),m.membership38()

assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit']) == (150,4,12)
assert not c['committed_external_independence_certificate_present']
assert not c['credit_raised']
assert c['bad_acceptances'] == 0 and all(c['checks'])

assert (317548800//551300) == t['epoch96_complete_seed_states'] == 576
assert (t['accepted'],t['deadline_vectors']) == (2974579200,573800)
assert (
    t['epoch97_bound_thirty_fourth_lineage_rotation_states'],
    t['epoch97_bound_thirty_fourth_lineage_binding_states'],
    t['epoch97_bound_handed_proof_rebind_states'],
    t['epoch97_bound_verifier_binding_states'],
) == (2313561600,1652544000,991526400,330508800)
assert t['deadline_origin'] == 'epoch12'
assert t['bad_acceptances'] == 0 and all(t['checks'])

assert (14340049920//518665) == s['bound_seventieth_restart_seed_states'] == 27648
assert (
    s['accepted'],
    s['deadline_vectors'],
    s['bound_seventy_first_restart_recoveries'],
) == (164312451072,540274,14937495552)
assert (
    s['bound_replacement_source_churn_states'],
    s['bound_successor_source_binding_states'],
    s['bound_fresh_reconciliation_states'],
    s['bound_seventy_first_restart_states'],
) == (134437459968,104562468864,74687477760,44812486656)
assert s['bad_acceptances'] == 0 and all(s['checks'])

assert (378206400//497640) == b['bound_quorum_churn_seed_states'] == 760
assert (b['accepted'],b['deadline_vectors']) == (4336039400,518665)
assert (
    b['bound_witness_source_replacement_states'],
    b['bound_root38_rollover_states'],
    b['bound_root38_binding_states'],
    b['bound_replication_quorum_churn_states'],
) == (3547668600,1970927000,1182556200,394185400)
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
    'distributed_winloop_v146.py',
    'winloop_v146.json',
    'winloop_v146_report.md',
    'winloop_v146_validate.py',
}
seen = set()
for line in (H/'winloop_v146_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    expected, name = line.split(maxsplit=1)
    name = name.strip()
    raw = (
        json.dumps(json.loads((H/name).read_text()),sort_keys=True,separators=(',',':')).encode()
        if name == 'winloop_v146.json'
        else (H/name).read_bytes()
    )
    assert hashlib.sha256(raw).hexdigest() == expected
    seen.add(name)
assert seen == required

assert a['digest'] == '0b334216ca86ccf3156d201e0aa8543ed412a0dba574c75accef95f406670cda'
assert a['digest'] == m.run_validation()['digest']
print(json.dumps({
    'version':'V146',
    'validated':True,
    'digest':a['digest'],
    'headline':a['headline'],
}, sort_keys=True))
