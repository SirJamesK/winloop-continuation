# WinLoop V207 validation report

## Verified result

V207 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-158 GC to 13,672,608,768 states with 9,766,149,120 bound sixty-fifth-source handoffs, 5,859,689,472 bound sixty-fifth-source bindings, and 1,953,229,824 bound verifier completions; admits 997,678,218,240 publication states with 90,698,019,840 fully bound one-hundred-thirty-second-cold-restart recoveries; and admits 17,067,060,080 membership states with 12,190,757,200 bound root-68 witness rebinds, 7,314,454,320 bound witness renewals, and 2,438,151,440 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `0dc7f3b24090c61bb65ed06b332d0bb9153484cfc72509e9d395f3584c46566a`.

## Predecessor binding

V207 continues from committed V206 on `main`: V206 digest `a280c66dcf39c5a68b012468dca72bac5a9a3dcf0906854bae79bacc404a13b0`, implementation SHA-256 `153337116cdd9c8df5483d6e29700c94a8f153e37c306f632b4787e0db8f9b6d`, validator SHA-256 `a42c36508eca34b615de16afe67f8be0531f882e061101457111c30eaecdfcdf`. V207 implementation SHA-256 is `533c908a094e71a270078db6055b53f5ebf39a1264da47badc4a1a8a8a66ae9d` and standalone validator SHA-256 is `327160d771fae49d06e410bbc8b5acc7f9958b3e10fce025bd586d0c20ffeb73`.

Seed transitions are exact from V206: 576 epoch-157 completions (`1,910,615,040 / 3,317,040`), 27,648 restart recoveries (`88,697,382,912 / 3,208,094`), and 760 quorum-churn completions (`2,383,971,800 / 3,136,805`).

## Continuation gates

Epoch 158 hands the rebound proof to a sixty-fifth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 132 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-thirty-second cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 68 after the root-68 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v207_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V208

Keep independence fail closed absent a committed external verifier artifact; rotate the sixty-fifth-source lineage in epoch 159, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-132 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-thirty-third cold restart without cached-authority promotion; replace the witness source after the root-68 witness rebind, roll to root 69, bind root 69, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
