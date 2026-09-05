# WinLoop V217 validation report

## Verified result

V217 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-168 GC to 16,903,127,808 states with 12,073,662,720 bound seventieth-source handoffs, 7,244,197,632 bound seventieth-source bindings, and 2,414,732,544 bound verifier completions; admits 1,236,214,932,480 publication states with 112,383,175,680 fully bound one-hundred-forty-second-cold-restart recoveries; and admits 21,180,324,480 membership states with 15,128,803,200 bound root-73 witness rebinds, 9,077,281,920 bound witness renewals, and 3,025,760,640 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `5ffe5d638e87cce710b96b9da77f92110cdc014beaabaf30d3fae1ff02a6980d`.

## Predecessor binding

V217 continues from committed V216 on `main`: V216 digest `d075f685dd19d79eed4c7b23d8fcb1a7ee60fede5ec4052f4f0d8a463c11f203`, implementation SHA-256 `ae69c111c664ec27bcf538cf270f0a0bb097a7062ce003d06adc47cf0d75670b`, validator SHA-256 `3125d9a4d6924a5a0bd971cf12a0a280fc71012f0a3ef897a79efdb39e23b65b`. V217 implementation SHA-256 is `46b21bfad0f7b8e243d077dd28ea35dd7c1d8d8c01d4d1267a40fd214f6bbf48` and standalone validator SHA-256 is `ba45de8b298038d8a327d7b5719787376eb30cea7a5ebae7ab06590df77567f3`.

Seed transitions are exact from V216: 576 epoch-167 completions (`2,365,620,480 / 4,106,980`), 27,648 restart recoveries (`110,073,987,072 / 3,981,264`), and 760 quorum-churn completions (`2,963,160,200 / 3,898,895`).

## Continuation gates

Epoch 168 hands the rebound proof to a seventieth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 142 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-second cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 73 after the root-73 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v217_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V218

Keep independence fail closed absent a committed external verifier artifact; rotate the seventieth-source lineage in epoch 169, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-142 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-third cold restart without cached-authority promotion; replace the witness source after the root-73 witness rebind, roll to root 74, bind root 74, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
