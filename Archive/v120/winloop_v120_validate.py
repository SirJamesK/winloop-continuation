#!/usr/bin/env python3
import hashlib
import importlib.util
import json
from pathlib import Path

H = Path(__file__).resolve().parent
BASE_VERSION = 'V119'
BASE_DIGEST = '02eef35bac9f1b1ac5a23d34bda99f93447a517ed75677da0020af5d0497c32c'
BASE_IMPL_SHA = '7b45b652ddf936f2f1bce679aa8834337e398cf2369d8d2fd9033ae4b464f22d'
BASE_EPOCH70_COMPLETE = 87607296
BASE_EPOCH70_DEADLINE_VECTORS = 152096
BASE_FORTY_FOURTH_RESTART_RECOVERIES = 3826897920
BASE_PUB_DEADLINE_VECTORS = 138415
BASE_MEMBERSHIP_QUORUM_CHURN = 98622160
BASE_MEM_DEADLINE_VECTORS = 129766

assert BASE_EPOCH70_COMPLETE // BASE_EPOCH70_DEADLINE_VECTORS == 576
assert BASE_FORTY_FOURTH_RESTART_RECOVERIES // BASE_PUB_DEADLINE_VECTORS == 27648
assert BASE_MEMBERSHIP_QUORUM_CHURN // BASE_MEM_DEADLINE_VECTORS == 760

sp = importlib.util.spec_from_file_location('v120', H / 'distributed_winloop_v120.py')
m = importlib.util.module_from_spec(sp)
sp.loader.exec_module(m)
a = json.loads((H / 'winloop_v120.json').read_text())
assert a == m.run_validation() and a['version'] == 'V120'
assert a['base'] == {'version': BASE_VERSION, 'digest': BASE_DIGEST, 'implementation_sha256': BASE_IMPL_SHA}
assert a['admission'] == {'joint': 21, 'provenance': 22, 'lower': 63, 'preserved': True}
assert a['routing'] == {'active': 'V21 guarded', 'replacement': False}
assert not a['runtime']['new_routing_envelope']

c = m.indep()
assert (c['patterns'], c['hypothetical_gate_admits'], c['conservative_cross_role_credit'], c['bad_acceptances']) == (150, 4, 12, 0)
assert not c['credit_raised'] and not c['committed_external_independence_certificate_present'] and all(c['checks'])

t = m.gc71()
assert (t['patterns'], t['accepted'], t['base_states'], t['epoch70_complete_seed_states'], t['delay_vectors'], t['deadline_vectors'], t['shared_deadline']) == (
    12095523200590218055750012113741820559409208618190045644284055371580996641715758174026264885779831865357647767858787123200, 838252800, 5184, 576, 25108406941546723055343157692830665664409421777856138051584, 161700, 3
)
assert (t['epoch71_twenty_first_lineage_rotation_states'], t['epoch71_bound_twenty_first_lineage_rotation_states'], t['epoch71_twenty_first_lineage_binding_states'], t['epoch71_bound_twenty_first_lineage_binding_states'], t['epoch71_handed_proof_rebind_states'], t['epoch71_bound_handed_proof_rebind_states'], t['epoch71_verifier_binding_states'], t['epoch71_bound_verifier_binding_states'], t['epoch71_complete_states']) == (
    745113600, 651974400, 558835200, 465696000, 372556800, 279417600, 186278400, 93139200, 93139200
)
assert t['deadline_origin'] == 'epoch12' and all(t['checks']) and t['bad_acceptances'] == 0
for k, v in t.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

s = m.replacement_churn_forty_fifth_restart()
assert (s['patterns'], s['accepted'], s['base_states'], s['bound_forty_fourth_restart_seed_states'], s['delay_vectors'], s['deadline_vectors'], s['shared_deadline']) == (
    144112236007274539600065221828095920522064818161234918940958635212144640, 44840632320, 304128, 27648, 392318858461667547739736838950479151006397215279002157056, 147440, 3
)
assert (s['replacement_source_churn_states'], s['bound_replacement_source_churn_states'], s['successor_source_binding_states'], s['bound_successor_source_binding_states'], s['dual_source_reconciliation_states'], s['bound_dual_source_reconciliation_states'], s['forty_fifth_verifier_cold_restart_states'], s['bound_forty_fifth_restart_states'], s['bound_forty_fifth_restart_recoveries']) == (
    40764211200, 36687790080, 32611368960, 28534947840, 24458526720, 20382105600, 16305684480, 12229263360, 4076421120
)
assert all(s['checks']) and s['bad_acceptances'] == 0
for k, v in s.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

b = m.root25_rollover_after_root24_witness_source_replacement()
assert (b['patterns'], b['accepted'], b['base_states'], b['bound_quorum_churn_seed_states'], b['delay_vectors'], b['deadline_vectors'], b['shared_deadline']) == (
    17136851500813492610603975669532557421874228355487398028533324306605670400, 1157149400, 8360, 760, 24519928653854221733733552434404946937899825954937634816, 138415, 3
)
assert (b['witness_source_replacement_states'], b['bound_witness_source_replacement_states'], b['replacement_source_binding_states'], b['bound_replacement_source_binding_states'], b['root25_rollover_states'], b['bound_root25_rollover_states'], b['root25_binding_states'], b['bound_root25_binding_states'], b['replication_quorum_churn_states'], b['bound_replication_quorum_churn_states']) == (
    1051954000, 946758600, 841563200, 736367800, 631172400, 525977000, 420781600, 315586200, 210390800, 105195400
)
assert all(b['checks']) and b['bad_acceptances'] == 0
for k, v in b.items():
    if k.endswith('_acceptances'):
        assert v == 0, (k, v)

h = a['temporal_floor_regression']
assert (h['roots'], h['horizon'], h['floor'], h['budget'], h['h11_floor'], h['h11_budget'], h['carried_from']) == (22, 22, 1, 851, 2, 398, 'V66')
assert a['checkpoint_recovery'] == {'statements': 513, 'max_lag': 64, 'shared_audit': '132 + 4*k', 'frontier_storage_only': True, 'trust_bearing_messages_unchanged': True}
assert a['digest'] == '7d958d0fc2e8e0c1d18c8a82c8f530aa48b8ed82b07086d91b71ea9d04acd382'

for line in (H / 'winloop_v120_SHA256SUMS.txt').read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    d, n = line.split(maxsplit=1)
    n = n.strip()
    if n == 'winloop_v120.json':
        canonical = json.dumps(json.loads((H / n).read_text()), sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == d
    else:
        assert hashlib.sha256((H / n).read_bytes()).hexdigest() == d

print(json.dumps({'version': 'V120', 'validated': True, 'digest': a['digest'], 'headline': a['headline']}, sort_keys=True))
