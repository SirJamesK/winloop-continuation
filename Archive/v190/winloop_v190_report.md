# WinLoop V190 validation report

## Verified result

V190 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-141 GC to 11,795,051,520 states with 9,173,928,960 bound fifty-sixth-lineage rotations, 6,552,806,400 bound lineage bindings, 3,931,683,840 bound handed-proof rebinds, and 1,310,561,280 bound verifier completions; admits 666,244,085,760 publication states with 60,567,644,160 fully bound one-hundred-fifteenth-cold-restart recoveries; and admits 17,852,320,200 membership states with 14,606,443,800 bound witness-source replacements, 8,114,691,000 bound root-60 rollovers, 4,868,814,600 bound root-60 bindings, and 1,622,938,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `d90eb3a5fefb37142e4ea26763b90d6d50efd747b026ab6f94d9fd9b0de1d0b4`.

## Predecessor binding

V190 continues from committed V189 on `main`: V189 digest `64ad3d3bb583af4d24658888168ef5a242b9d221f16db41925e2853ae9c58ee8`, implementation SHA-256 `031d7f3731dff1d20d5c527b4a11cd5dbcfc3971a1b44303e197cdfdc7b7b2d3`, validator SHA-256 `079317e32d209864301083ba220eee5271bf3be396b29531bdef16b7df770ef3`. V190 implementation SHA-256 is `eef135f15b319a66d43f23a74455f889211e67704ac7e6973a3b5e0a33d99280` and standalone validator SHA-256 is `0743503bd57a806cfad18e6bb6b92d90e0bb1fe733d0f0d4469d79746d111423`.

Seed transitions are exact from V189: 576 epoch-140 completions (`1,277,934,336 / 2,218,636`), 27,648 restart recoveries (`59,040,783,360 / 2,135,445`), and 760 quorum-churn completions (`1,581,678,560 / 2,081,156`).

## Continuation gates

Epoch 141 rotates the fifty-sixth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 115 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-fifteenth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-59 witness rebind, rolls to root 60, binds root 60, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v190_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V191

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a fifty-seventh source in epoch 142, bind that source, and preserve the epoch-12 deadline; compose publication-115 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixteenth cold restart without cached-authority promotion; rebind the witness to root 60 after the root-60 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
