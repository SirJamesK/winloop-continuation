# WinLoop V251 validation report

## Verified result

V251 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-202 GC to 31,614,589,440 states with 22,581,849,600 bound eighty-seventh-source handoffs, 13,549,109,760 bound eighty-seventh-source bindings, and 4,516,369,920 bound verifier completions; admits 2,325,684,759,552 publication states with 211,425,887,232 fully bound one-hundred-seventy-sixth-cold-restart recoveries; and admits 40,004,325,200 membership states with 28,574,518,000 bound root-90 witness rebinds, 17,144,710,800 bound witness renewals, and 5,714,903,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `41d57be0cd6ddedde3f3b8714a1a677d169178fd7ed4ebbbd3885ca71023fe82`.

## Predecessor binding

V251 continues from committed V250 on `main`: V250 digest `d23b85e71f6792aa0fa159af5cd5c76170beff3f2d50dc8dce8ed662336c1b95`, implementation SHA-256 `f61d8efcf9d68136b056aaa4f38457b2b5321a268d6562fcead98a235cdad58b`, validator SHA-256 `dea3d48f1e739e9175ae1c0cb85d459907146567d6e37c06529a88908f899602`. V251 implementation SHA-256 is `940c57926616cd3e83efc7f5808b2833be8e406a90068b3dcc80e092fe8e3d88` and standalone validator SHA-256 is `f4651c84c3e02e81850c4ba2b02b324f6c136a7e5bff7c4ebe3ac94a4406e25d`.

Seed transitions are exact from V250: 576 epoch-202 completions (`4,441,720,320 / 7,711,320`), 27,648 restart recoveries (`207,902,177,280 / 7,519,610`), and 760 quorum-churn completions (`5,619,124,600 / 7,393,585`).

## Continuation gates

Epoch 202 hands the rebound proof to an eighty-seventh source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 176 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-sixth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-90 rollover, rebinds the witness to root 90, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v251_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V252

Keep independence fail closed absent a committed external verifier artifact; rotate the eighty-seventh-source lineage in epoch 203, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-176 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-seventh cold restart without cached-authority promotion; keep generation 4 after the root-90 witness rebind, replace the witness source, roll to root 91, bind root 91, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
