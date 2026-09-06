# WinLoop V227 validation report

## Verified result

V227 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-178 GC to 20,606,197,248 states with 14,718,712,320 bound seventy-fifth-source handoffs, 8,831,227,392 bound seventy-fifth-source bindings, and 2,943,742,464 bound verifier completions; admits 1,510,030,494,720 publication states with 137,275,499,520 fully bound one-hundred-fifty-second-cold-restart recoveries; and admits 25,906,452,880 membership states with 18,504,609,200 bound root-78 witness rebinds, 11,102,765,520 bound witness renewals, 3,700,921,840 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `bee0d1231718e8ae5d97a97dfa5871b670634456cc738a5e2d6fb7401c92f916`.

## Predecessor binding

V227 continues from committed V226 on `main`: V226 digest `28ba0ac5011094061962ae84c33557e5fdcf50f57e50434b171df865d853a593`, implementation SHA-256 `680e5d510e2fbe06505e0a60f1ba80967e99c49b4f1460c656bdaa56461b679c`, validator SHA-256 `a686588c6cebcbb4c7a09a1a337500358f24552b25e9e422485092e584304bcd`. V227 implementation SHA-256 is `57a05fc5c32a9fcd1ee2dece1881d710f8a3b84ce2a42940f8ab3667849d862a` and standalone validator SHA-256 is `de1176f271909f5a557ca8b3b4f67f9468851de0fc7d78164e25495a0020fd02`.

Seed transitions are exact from V226: 576 epoch-177 completions (`2,887,672,320 / 5,013,320`), 27,648 restart recoveries (`134,635,640,832 / 4,869,634`), and 760 quorum-churn completions (`3,629,292,600 / 4,775,385`).

## Continuation gates

Epoch 178 hands the rebound proof to a seventy-fifth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 152 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-fifty-second cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 78 after the root-78 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v227_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V228

Keep independence fail closed absent a committed external verifier artifact; rotate the seventy-fifth-source lineage in epoch 179, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-152 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-fifty-third cold restart without cached-authority promotion; replace the witness source after the root-78 witness rebind, roll to root 79, bind root 79, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
