from itertools import product
from math import comb

D = 3
BASE_V85_EPOCH36_COMPLETE_STATIC_STATES = 576


def q(n):
    # Exact count of nonnegative n-coordinate deadline vectors with total <= 3.
    return comb(n + D, D)


def indep():
    cert = ('absent', 'current', 'cached', 'stale', 'conflict', 'self')
    anchor = ('current', 'cached', 'missing', 'stale', 'fork')
    relation = ('disjoint', 'provider', 'operator', 'hardware', 'unknown')
    ok = lambda c, a, r: c in cert[1:3] and a in anchor[:2] and r == 'disjoint'
    admitted = [x for x in product(cert, anchor, relation) if ok(*x)]
    return {
        'patterns': len(cert) * len(anchor) * len(relation),
        'hypothetical_gate_admits': len(admitted),
        'committed_external_independence_certificate_present': False,
        'conservative_cross_role_credit': 12,
        'credit_raised': False,
        'bad_acceptances': sum(
            1 for c, a, r in admitted
            if c not in cert[1:3] or a not in anchor[:2] or r != 'disjoint'
        ),
        'checks': [
            ok('current', 'current', 'disjoint'),
            ok('cached', 'cached', 'disjoint'),
            not ok('stale', 'current', 'disjoint'),
            not ok('self', 'current', 'disjoint'),
            all(not ok('current', 'current', r) for r in relation[1:]),
        ],
    }


_GC37_EXPECTED = {
    0: (0, 0, 0, 0, 0),
    1: (1, 0, 0, 0, 0),
    2: (2, 0, 0, 0, 0),
    3: (2, 1, 0, 0, 0),
    4: (2, 2, 0, 0, 0),
    5: (2, 2, 1, 0, 0),
    6: (2, 2, 2, 0, 0),
    7: (2, 2, 2, 1, 0),
    8: (2, 2, 2, 2, 0),
    9: (2, 2, 2, 2, 1),
    10: (2, 2, 2, 2, 2),
}


def _gc37_ok(phase, lineage_rerotation, fourth_lineage_binding,
             root_rollover, root_binding, verifier_binding,
             carried_root, continuity, source_binding, rotated_key_binding,
             third_source_binding, fourth_source_binding, deadline_reset):
    # 3 denotes unknown/unbound/conflicting trust-bearing evidence.
    if any(x == 3 for x in (
        lineage_rerotation, fourth_lineage_binding, root_rollover,
        root_binding, verifier_binding, carried_root, continuity,
        source_binding, rotated_key_binding, third_source_binding,
        fourth_source_binding
    )):
        return False
    if deadline_reset != 0:
        return False
    # V85 completed epoch 36 only with the carried root and all prior source/key
    # bindings fixed; epoch 37 may roll the root only after fourth-source lineage
    # re-rotation and explicit fourth-lineage binding complete.
    if carried_root != 1 or continuity != 1:
        return False
    if source_binding != 2 or rotated_key_binding != 2:
        return False
    if third_source_binding != 2 or fourth_source_binding != 2:
        return False
    return _GC37_EXPECTED.get(phase) == (
        lineage_rerotation, fourth_lineage_binding, root_rollover,
        root_binding, verifier_binding
    )


def gc37():
    tails = [
        (phase, *state, 1, 1, 2, 2, 2, 2, 0)
        for phase, state in _GC37_EXPECTED.items()
    ]
    assert all(_gc37_ok(*x) for x in tails)
    z = q(30)
    seed = BASE_V85_EPOCH36_COMPLETE_STATIC_STATES
    static_accepted = seed * len(tails)

    rerotation_states = sum(x[1] in (1, 2) for x in tails) * seed
    bound_rerotation = sum(x[1] == 2 for x in tails) * seed
    lineage_binding_states = sum(x[2] in (1, 2) for x in tails) * seed
    bound_lineage_binding = sum(x[2] == 2 for x in tails) * seed
    rollover_states = sum(x[3] in (1, 2) for x in tails) * seed
    bound_rollover = sum(x[3] == 2 for x in tails) * seed
    root_binding_states = sum(x[4] in (1, 2) for x in tails) * seed
    bound_root_binding = sum(x[4] == 2 for x in tails) * seed
    verifier_states = sum(x[5] in (1, 2) for x in tails) * seed
    bound_verifier = sum(x[5] == 2 for x in tails) * seed
    complete = sum(x[0] == 10 for x in tails) * seed

    rerotation_bad = sum(x[1] == 3 for x in tails) * seed
    lineage_binding_bad = sum(x[2] == 3 for x in tails) * seed
    rollover_bad = sum(x[3] == 3 for x in tails) * seed
    root_binding_bad = sum(x[4] == 3 for x in tails) * seed
    verifier_bad = sum(x[5] == 3 for x in tails) * seed
    stale_root = sum(x[6] in (2, 3) for x in tails) * seed
    continuity_break = sum(x[7] in (2, 3) for x in tails) * seed
    source_bad = sum(x[8] == 3 for x in tails) * seed
    key_binding_bad = sum(x[9] != 2 for x in tails) * seed
    third_source_bad = sum(x[10] != 2 for x in tails) * seed
    fourth_source_bad = sum(x[11] != 2 for x in tails) * seed
    deadline_reset = sum(x[12] != 0 for x in tails) * seed
    bad = (
        rerotation_bad + lineage_binding_bad + rollover_bad + root_binding_bad
        + verifier_bad + stale_root + continuity_break + source_bad
        + key_binding_bad + third_source_bad + fourth_source_bad + deadline_reset
    )

    checks = [
        _gc37_ok(0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0),
        _gc37_ok(2, 2, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0),
        _gc37_ok(4, 2, 2, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0),
        _gc37_ok(6, 2, 2, 2, 0, 0, 1, 1, 2, 2, 2, 2, 0),
        _gc37_ok(8, 2, 2, 2, 2, 0, 1, 1, 2, 2, 2, 2, 0),
        _gc37_ok(10, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0),
        not _gc37_ok(10, 3, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0),
        not _gc37_ok(10, 2, 3, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0),
        not _gc37_ok(10, 2, 2, 3, 2, 2, 1, 1, 2, 2, 2, 2, 0),
        not _gc33uöö²ƒÂ"Â"Â"Â2Â"ÂÂÂ"Â"Â"Â"Â’À¢æ÷Böv33uöö²ƒÂ"Â"Â"Â"Â2ÂÂÂ"Â"Â"Â"Â’À¢æ÷Böv337_ok(10, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 0),
        not _gc37_ok(10, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0),
        not _gc33uöö²ƒÂ"Â"Â"Â"Â"ÂÂÂ2Â"Â"Â"Â’À¢æ÷Böv33uöö²ƒÂ"Â"Â"Â"Â"ÂÂÂ"ÂÂ"Â"Â’À¢æ÷Böv337_ok(10, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 2, 0),
        not _gc37_ok(10, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1, 0),
        not _gc33uöö²ƒÂ"Â"Â"Â"Â"ÂÂÂ"Â"Â"Â"Â’À¢Ð ¢7FF–5÷GFW&ç2Ò6VVB¢¢ƒB¢¢"’¢0¢GFW&ç2Ò7FF–5÷GFW&ç2¢ƒB¢¢3’¢ ¢&WGW&â°¢wGFW&ç2s¢GFW&ç2À¢v66WFVBs¢7FF–5ö66WFVB¢¢À¢v&6U÷7FFW2s¢7FF–5ö66WFVBÀ¢vWö6ƒ3eö6ö×ÆWFU÷6VVE÷7FFW2s¢6VVBÀ¢vFVÆ•÷fV7F÷'2s¢B¢¢3À¢vFVFÆ–æU÷fV7F÷'2s¢¢À¢w6†&VEöFVFÆ–æRs¢2À¢vFVFÆ–æUö÷&–v–âs¢vWö6ƒ"rÀ¢vWö6ƒ3uöf÷W'F…÷6÷W&6UöÆ–æVvU÷&W&÷FF–öå÷7FFW2s¢&W&÷FF–öå÷7FFW2¢¢À¢vWö6ƒ3uö&÷VæEöf÷W'F…÷6÷W&6UöÆ–æVvU÷&W&÷FF–öå÷7FFW2s¢&÷VæE÷&W&÷FF–öâ¢¢À¢vWö6ƒ3uöf÷W'F…öÆ–æVvUö&–æF–æu÷7FFW2s¢Æ–æVvUö&–æF–æu÷7FFW2¢¢À¢vWö6ƒ3uö&÷VæEöf÷W'F…öÆ–æVvUö&–æF–æu÷7FFW2s¢&÷VæEöÆ–æVvUö&–æF–ær¢¢À¢vWö6ƒ3u÷&ö÷E÷&öÆÆ÷fW%÷7FFW2s¢&öÆÆ÷fW%÷7FFW2¢¢À¢vWö6ƒ3uö&÷VæE÷&ö÷E÷&öÆÆ÷fW%÷7FFW2s¢&÷VæE÷&öÆÆ÷fW"¢¢À¢vWö6ƒ3u÷&ö÷Eö&–æF–æu÷7FFW2s¢&ö÷Eö&–æF–æu÷7FFW2¢¢À¢vWö6ƒ3uö&÷VæE÷&ö÷Eö&–æF–æu÷7FFW2s¢&÷VæE÷&ö÷Eö&–æF–ær¢¢À¢vWö6ƒ3u÷fW&–f–W%ö&–æF–æu÷7FFW2s¢fW&–f–W%÷7FFW2¢¢À¢vWö6ƒ3uö&÷VæE÷fW&–f–W%ö&–æF–æu÷7FFW2s¢&÷VæE÷fW&–f–W"¢¢À¢vWö6ƒ3uö6ö×ÆWFU÷7FFW2s¢6ö×ÆWFR¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æuöf÷W'F…÷6÷W&6UöÆ–æVvU÷&W&÷FF–öåö66WFæ6W2s¢&W&÷FF–öåö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æuöf÷W'F…öÆ–æVvUö&–æF–æuö66WFæ6W2s¢Æ–æVvUö&–æF–æuö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷&ö÷E÷&öÆÆ÷fW%ö66WFæ6W2s¢&öÆÆ÷fW%ö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷&ö÷Eö&–æF–æuö66WFæ6W2s¢&ö÷Eö&–æF–æuö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷fW&–f–W%ö&–æF–æuö66WFæ6W2s¢fW&–f–W%ö&B¢¢À¢w7FÆUö÷%ö6öæfÆ–7F–æu÷&ö÷Eö6†ö–6Uö66WFæ6W2s¢7FÆU÷&ö÷B¢¢À¢wFöÖ'7FöæU÷&ö÷EöF—66öçF–çV—G•ö66WFæ6W2s¢6öçF–çV—G•ö'&V²¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷6÷W&6Uö&–æF–æuö66WFæ6W2s¢6÷W&6Uö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷&÷FFVEö¶W•ö&–æF–æuö66WFæ6W2s¢¶W•ö&–æF–æuö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æu÷F†—&E÷6÷W&6Uö&–æF–æuö66WFæ6W2s¢F†—&E÷6÷W&6Uö&B¢¢À¢wVæ&÷VæEö÷%ö6öæfÆ–7F–æuöf÷W'F…÷6÷W&6Uö&–æF–æuö66WFæ6W2s¢f÷W'F…÷6÷W&6Uö&B¢¢À¢vFVFÆ–æU÷&W6WEö66WFæ6W2s¢FVFÆ–æU÷&W6WB¢¢À¢v&Eö66WFæ6W2s¢&B¢¢À¢v6†V6·2s¢6†V6·2À¢Ð