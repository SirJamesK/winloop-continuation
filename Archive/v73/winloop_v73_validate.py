#!/usr/bin/env python3
import hashlib, importlib.util, json
from pathlib import Path
H=Path(__file__).resolve().parent
base=json.loads((H.parent/'v72'/'winloop_v72.json').read_text())
assert base['version']=='V72' and base['digest']=='df8018a5257fb3cd129b2849b5a55f44fb7a3781cd5646bcbb65f29d5fcfbe98'
assert '0e88efa9e47f86aeaff35e22b28a15642f553c33a37a68fad83f75bdbec5a46a  distributed_winloop_v72.py' in (H.parent/'v72'/'winloop_v72_SHA256SUMS.txt').read_text()
sp=importlib.util.spec_from_file_location('v73',H/'distributed_winloop_v73.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
a=json.loads((H/'winloop_v73.json').read_text());assert a==m.run_validation() and a['version']=='V73'
assert a['base']=={'version':'V72','digest':'df8018a5257fb3cd129b2849b5a55f44fb7a3781cd5646bcbb65f29d5fcfbe98','implementation_sha256':'0e88efa9e47f86aeaff35e22b28a15642f553c33a37a68fad83f75bdbec5a46a'}
assert a['admission']=={'joint':21,'provenance':22,'lower':63,'preserved':True} and a['routing']=={'active':'V21 guarded','replacement':False} and not a['runtime']['new_routing_envelope']
c=a['independence_certificate_gate'];assert (c['patterns'],c['hypothetical_gate_admits'],c['conservative_cross_role_credit'],c['bad_acceptances'])==(150,4,12,0) and not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])
t=a['tombstone_epoch24_rotation_dual_root'];assert (t['patterns'],t['accepted'],t['base_states'],t['delay_vectors'],t['deadline_vectors'],t['shared_deadline'])==(4749890231992320000,27148030,59666,16777216,455,3);assert (t['fourth_cycle_replacement_key_rotation_recoveries'],t['dual_rollback_root_disagreement_recoveries'],t['dual_older_root_non_authoritative_recoveries'],t['stale_or_conflicting_root_acceptances'],t['unbound_rotation_acceptances'],t['deadline_reset_acceptances'],t['bad_acceptances'])==(4550,87360,29120,0,0,0,0) and t['deadline_origin']=='epoch12' and all(t['checks'])
s=a['publication_verifier_rollback_two_witness_coldstart'];assert (s['patterns'],s['accepted'],s['base_states'],s['delay_vectors'],s['deadline_vectors'],s['shared_deadline'])==(107520000000000000,5331920,24236,262144,220,3);assert (s['first_replacement_witness_rotation_recoveries'],s['second_replacement_witness_rotation_recoveries'],s['verifier_cold_start_bound_selection_recoveries'],s['secondary_witness_cold_start_selections'],s['cached_join_authority_promotions'],s['unbound_source_selection_acceptances'],s['below_publication_quorum_acceptances'],s['bad_acceptances'])==(1354320,190080,1330560,665280,0,0,0,0) and all(s['checks'])
b=a['collision_reuse_membership_root_compaction'];assert (b['patterns'],b['accepted'],b['base_states'],b['delay_vectors'],b['deadline_vectors'],b['shared_deadline'])==(267181325549568,1343100,8140,65536,165,3);assert (b['concurrent_collision_identity_reuse_recoveries'],b['membership_root_compaction_recoveries'],b['verifier_restart_or_compaction_recoveries'],b['tombstone_generation_bypass_acceptances'],b['unbound_membership_root_acceptances'],b['active_byzantine_acceptances'],b['bad_acceptances'])==(116325,707025,839025,0,0,0,0) and all(b['checks'])
h=a['temporal_floor_regression'];assert (h['roots'],h['horizon'],h['floor'],h['budget'],h['h11_floor'],h['h11_budget'],h['carried_from'])==(22,22,1,851,2,398,'V66')
assert a['checkpoint_recovery']=={'statements':513,'max_lag':64,'shared_audit':'132 + 4*k','frontier_storage_only':True,'trust_bearing_messages_unchanged':True}
for line in (H/'winloop_v73_SHA256SUMS.txt').read_text().splitlines():
    if line.strip():
        d,n=line.split(maxsplit=1);assert hashlib.sha256((H/n.strip()).read_bytes()).hexdigest()==d
print(json.dumps({'version':'V73','validated':True,'digest':a['digest'],'headline':a['headline']},sort_keys=True))
