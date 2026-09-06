# WinLoop V241 validation report

## Verified result

V241 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-192 GC to 26,645,794,560 states with 19,032,710,400 bound eighty-second-source handoffs, 11,419,626,240 bound eighty-second-source bindings, and 3,806,542,080 bound verifier completions; admits 1,957,273,224,192 publication states with 177,933,929,472 fully bound one-hundred-sixty-sixth-cold-restart recoveries; and admits 33,633,678,400 membership states with 24,024,056,000 bound root-85 witness rebinds, 14,414,433,600 bound witness renewals, and 4,804,811,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `e9654fac5dd38764f680f9078b672010ba80fadad1a664519642cbe68e8a9e26`.

## Predecessor binding

V241 continues from committed V240 on `main`: V240 digest `af32248521f4a70a41d31a5f58008eb994a52f16124f9be3cb41b2d0c3701f81`, implementation SHA-256 `8a327849dec26c1f26de2cf0a71dd1bf60d7e1e1169fccc3d780bc0dfdc6e39a`, validator SHA-256 `50a45c0cebb2ac145033618387caeeb99c9a1a1412466077a96799e3fc278bc7`. V241 implementation SHA-256 is `4aabd6f6898dce6a40954ccd863de6a81299eee8d8cb48e34d42e1448db170af` and standalone validator SHA-256 is `dbc10cec08d6e10794cfc5b1ee3d0ccdd0529f2f42d9beede13e44c774be9616`.

Seed transitions are exact from V240: 576 epoch-192 completions (`3,806,542,080 / 6,608,580`), 27,648 restart recoveries (`177,933,929,472 / 6,435,689`), and 760 quorum-churn completions (`4,804,811,200 / 6,322,120`).

## Continuation gates

Epoch 192 hands the rebound proof to an eighty-second source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 166 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixty-sixth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after root-85 rollover, rebinds the witness to root 85, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v241_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V242

Keep independence fail closed absent a committed external verifier artifact; rotate the eighty-second-source lineage in epoch 193, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-166 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-seventh cold restart without cached-authority promotion; keep generation 4 after the root-85 witness rebind, replace the witness source, roll to root 86, bind root 86, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
