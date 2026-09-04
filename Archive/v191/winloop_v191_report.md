# WinLoop V191 validation report

## Verified result

V191 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-142 GC to 9,406,172,160 states with 6,718,694,400 bound fifty-seventh-source handoffs, 4,031,216,640 bound fifty-seventh-source bindings, and 1,343,738,880 bound verifier completions; admits 683,326,651,392 publication states with 62,120,604,672 fully bound one-hundred-sixteenth-cold-restart recoveries; and admits 11,654,364,400 membership states with 8,324,546,000 bound root-60 witness rebinds, 4,994,727,600 bound witness renewals, and 1,664,909,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `74e491bd9d07ad9ad7ae4a2acf1015ab516f7d5ff146aa24416d47e3fa4c7e99`.

## Predecessor binding

V191 continues from committed V190 on `main`: V190 digest `d90eb3a5fefb37142e4ea26763b90d6d50efd747b026ab6f94d9fd9b0de1d0b4`, implementation SHA-256 `eef135f15b319a66d43f23a74455f889211e67704ac7e6973a3b5e0a33d99280`, validator SHA-256 `0743503bd57a806cfad18e6bb6b92d90e0bb1fe733d0f0d4469d79746d111423`. V191 implementation SHA-256 is `84fe7bd6b475f7e56461ae38815227f08097f764a670f6f36f7ccda1208ee3a9` and standalone validator SHA-256 is `51f341c304fdb8094894df6c200f733ef6e76642277be3db22e57ad559f52b8f`.

Seed transitions are exact from V190: 576 epoch-141 completions (`1,310,561,280 / 2,275,280`), 27,648 restart recoveries (`60,567,644,160 / 2,190,670`), and 760 quorum-churn completions (`1,622,938,200 / 2,135,445`).

## Continuation gates

Epoch 142 hands the rebound proof to a fifty-seventh source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 116 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixteenth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 60 after the root-60 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v191_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V192

Keep independence fail closed absent a committed external verifier artifact; rotate the fifty-seventh-source lineage in epoch 143, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-116 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventeenth cold restart without cached-authority promotion; replace the witness source after the root-60 witness rebind, roll to root 61, bind root 61, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
