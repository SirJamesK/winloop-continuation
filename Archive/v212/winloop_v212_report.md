# WinLoop V212 validation report

## Verified result

V212 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-163 GC to 19,582,477,056 states with 15,230,815,488 bound sixty-seventh-lineage rotations, 10,879,153,920 bound lineage bindings, 6,527,492,352 bound handed-proof rebinds, and 2,175,830,784 bound verifier completions; admits 1,112,688,783,360 publication states with 101,153,525,760 fully bound one-hundred-thirty-seventh-cold-restart recoveries; and admits 29,935,312,440 membership states with 24,492,528,360 bound witness-source replacements, 13,606,960,200 bound root-71 rollovers, 8,164,176,120 bound root-71 bindings, and 2,721,392,040 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `86410329f2ae2218a9aef778c75b26b5f413df3ade426332f764b1bf02800aca`.

## Predecessor binding

V212 continues from committed V211 on `main`: V211 digest `f206faf0b46850b0db0abb0309a5ab9d190efbb21d6d22ea7ef1bf425d499b92`, implementation SHA-256 `668bf61a9c9df2a50f5b64a02256144322e55fb6db6821f73c59f8d47b8c9115`, validator SHA-256 `d4bb5da05d776ca1e7801ee4b260c959bf49e103339bf942be419acf1a8f7f6b`. V212 implementation SHA-256 is `254924e5c1a33df239b28b9257853dcca3631bb7cbbfd7315733ebee279bd212` and standalone validator SHA-256 is `9e365c3814a705749cae52abd97c84cb0a29ac2103c4a580bd1ae165c8f3fe82`.

Seed transitions are exact from V211: 576 epoch-162 completions (`2,130,024,960 / 3,697,960`), 27,648 restart recoveries (`99,001,377,792 / 3,580,779`), and 760 quorum-churn completions (`2,663,078,000 / 3,504,050`).

## Continuation gates

Epoch 163 rotates the sixty-seventh-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 137 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-thirty-seventh cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-70 witness rebind, rolls to root 71, binds root 71, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v212_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V213

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a sixty-eighth source in epoch 164, bind that source, and preserve the epoch-12 deadline; compose publication-137 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-thirty-eighth cold restart without cached-authority promotion; rebind the witness to root 71 after the root-71 rollover, renew that witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
