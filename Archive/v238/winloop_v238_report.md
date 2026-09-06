# WinLoop V238 validation report

## Verified result

V238 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-189 GC to 32,482,114,560 states with 25,263,866,880 bound eightieth-lineage rotations, 18,045,619,200 bound lineage bindings, 10,827,371,520 bound handed-proof rebinds, and 3,609,123,840 bound verifier completions; admits 1,854,878,496,768 publication states with 168,625,317,888 fully bound one-hundred-sixty-third-cold-restart recoveries; and admits 50,071,760,200 membership states with 40,967,803,800 bound witness-source replacements, 22,759,891,000 bound root-84 rollovers, 13,655,934,600 bound root-84 bindings, and 4,551,978,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `121e245f32f30eeed75f38c99deacf287b322a7e28cedb3f8ec89a296b8322f7`.

## Predecessor binding

V238 continues from committed V237 on `main`: V237 digest `01deee922875c4c8dd58991e21edde9ef9c45b29ae1f0cf238666a9ff71aa619`, implementation SHA-256 `3e51dd4b92d6d15cb946dc28d7f223a8ddf4369b634c91ac910d292b7921ab7a`, validator SHA-256 `7dd66e6f6eccc5c467962fbca7f725cc0a44d5aa3a047818b034519570724191`. V238 implementation SHA-256 is `d976ae45df7621a64e87ed3ffec7cdafe095e523b8cbade5756135f42f4bab42` and standalone validator SHA-256 is `4605e180557d4f5af90e5f6f4bae8968c9d031d0614e0084ed9ec4bb239203e9`.

Seed transitions are exact from V237: 576 epoch-188 completions (`3,544,867,584 / 6,154,284`), 27,648 restart recoveries (`165,596,175,360 / 5,989,445`), and 760 quorum-churn completions (`4,469,715,040 / 5,881,204`).

## Continuation gates

Epoch 189 rotates the eightieth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 163 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-third cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 stays bound after the root-83 witness rebind, replaces the witness source, rolls to root 84, binds root 84, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v238_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V239

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-first source in epoch 190, bind that source, and preserve the epoch-12 deadline; compose publication-163 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixty-fourth cold restart without cached-authority promotion; keep generation 4 after the root-84 rollover, rebind the witness to root 84, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
