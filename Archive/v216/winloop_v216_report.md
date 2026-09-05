# WinLoop V216 validation report

## Verified result

V216 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-167 GC to 21,290,584,320 states with 16,559,343,360 bound sixty-ninth-lineage rotations, 11,828,102,400 bound lineage bindings, 7,096,861,440 bound handed-proof rebinds, and 2,365,620,480 bound verifier completions; admits 1,210,813,857,792 publication states with 110,073,987,072 fully bound one-hundred-forty-first-cold-restart recoveries; and admits 32,594,762,200 membership states with 26,668,441,800 bound witness-source replacements, 14,815,801,000 bound root-73 rollovers, 8,889,480,600 bound root-73 bindings, and 2,963,160,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `d075f685dd19d79eed4c7b23d8fcb1a7ee60fede5ec4052f4f0d8a463c11f203`.

## Predecessor binding

V216 continues from committed V215 on `main`: V215 digest `b790801c1fff32a8555ea54edd9c7a1bc69a34f4d63b1ddbce5682dc72e260cb`, implementation SHA-256 `b175b40f185ee83650a29815e6269241bcaf83da744a1b7a71e36d4c28432a9e`, validator SHA-256 `2e3987611a14d864d7b099ed4bbaac6373ee543c210a092319f0aff80b46ba8f`. V216 implementation SHA-256 is `ae69c111c664ec27bcf538cf270f0a0bb097a7062ce003d06adc47cf0d75670b` and standalone validator SHA-256 is `3125d9a4d6924a5a0bd971cf12a0a280fc71012f0a3ef897a79efdb39e23b65b`.

Seed transitions are exact from V215: 576 epoch-166 completions (`2,317,178,880 / 4,022,880`), 27,648 restart recoveries (`107,796,648,960 / 3,898,895`), and 760 quorum-churn completions (`2,901,429,200 / 3,817,670`).

## Continuation gates

Epoch 167 rotates the sixty-ninth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 141 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-72 witness rebind, rolls to root 73, binds root 73, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v216_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V217

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventieth source in epoch 168, bind that source, and preserve the epoch-12 deadline; compose publication-141 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-second cold restart without cached-authority promotion; rebind the witness to root 73 after the root-73 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
