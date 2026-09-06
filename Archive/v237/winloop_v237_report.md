# WinLoop V237 validation report

## Verified result

V237 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-188 GC to 24,814,073,088 states with 17,724,337,920 bound eightieth-source handoffs, 10,634,602,752 bound eightieth-source bindings, and 3,544,867,584 bound verifier completions; admits 1,821,557,928,960 publication states with 165,596,175,360 fully bound one-hundred-sixty-second-cold-restart recoveries; and admits 31,288,005,280 membership states with 22,348,575,200 bound root-83 witness rebinds, 13,409,145,120 bound witness renewals, and 4,469,715,040 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `01deee922875c4c8dd58991e21edde9ef9c45b29ae1f0cf238666a9ff71aa619`.

## Predecessor binding

V237 continues from committed V236 on `main`: V236 digest `2a95cce899a035bc349fbf013ccacdd426fbc624b07a281aff1065a154dc3ea7`, implementation SHA-256 `7a7593a0a2f52c29fb2806db426014389d3720c3d04550c801ccce4eead1b813`, validator SHA-256 `4dca0b4514929fd5aaa6009bf4b365a4e3ca0b8c25028fbad5aae4a18ab79374`. V237 implementation SHA-256 is `3e51dd4b92d6d15cb946dc28d7f223a8ddf4369b634c91ac910d292b7921ab7a` and standalone validator SHA-256 is `7dd66e6f6eccc5c467962fbca7f725cc0a44d5aa3a047818b034519570724191`.

Seed transitions are exact from V236: 576 epoch-187 completions (`3,481,378,560 / 6,044,060`), 27,648 restart recoveries (`162,603,528,192 / 5,881,204`), and 760 quorum-churn completions (`4,388,449,000 / 5,774,275`).

## Continuation gates

Epoch 188 hands the rebound proof to the eightieth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 162 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixty-second cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 stays bound after the root-83 rollover, rebinds the witness to root 83, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v237_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V238

Keep independence fail closed absent a committed external verifier artifact; rotate the eightieth-source lineage in epoch 189, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-162 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-third cold restart without cached-authority promotion; keep generation 4 after the root-83 witness rebind, replace the witness source, roll to root 84, bind root 84, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
