# WinLoop V213 validation report

## Verified result

V213 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-164 GC to 15,556,020,480 states with 11,111,443,200 bound sixty-eighth-source handoffs, 6,666,865,920 bound sixty-eighth-source bindings, and 2,222,288,640 bound verifier completions; admits 1,136,703,034,368 publication states with 103,336,639,488 fully bound one-hundred-thirty-eighth-cold-restart recoveries; and admits 19,463,858,400 membership states with 13,902,756,000 bound root-71 witness rebinds, 8,341,653,600 bound witness renewals, and 2,780,551,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `b19bc005d17f5a2aeaef039192765e52ca6bfe71e83bd4860c0e2cc211f06bbd`.

## Predecessor binding

V213 continues from committed V212 on `main`: V212 digest `86410329f2ae2218a9aef778c75b26b5f413df3ade426332f764b1bf02800aca`, implementation SHA-256 `254924e5c1a33df239b28b9257853dcca3631bb7cbbfd7315733ebee279bd212`, validator SHA-256 `9e365c3814a705749cae52abd97c84cb0a29ac2103c4a580bd1ae165c8f3fe82`. V213 implementation SHA-256 is `75aa4540a8913a9bfde82709e439446134f86ee1f72ff492207265571639c82e` and standalone validator SHA-256 is `0a10f6edacd659240d665f408145f48f517de3cf817d6d523f7f5ffa12c0e29a`.

Seed transitions are exact from V212: 576 epoch-163 completions (`2,175,830,784 / 3,777,484`), 27,648 restart recoveries (`101,153,525,760 / 3,658,620`), and 760 quorum-churn completions (`2,721,392,040 / 3,580,779`).

## Continuation gates

Epoch 164 hands the rebound proof to a sixty-eighth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 138 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-thirty-eighth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 71 after the root-71 rollover, renews that witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v213_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V214

Keep independence fail closed absent a committed external verifier artifact; rotate the sixty-eighth-source lineage in epoch 165, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-138 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-thirty-ninth cold restart without cached-authority promotion; replace the witness source after the root-71 witness rebind, roll to root 72, bind root 72, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
