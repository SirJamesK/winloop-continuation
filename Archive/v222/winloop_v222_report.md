# WinLoop V222 validation report

## Verified result

V222 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-173 GC to 24,034,599,936 states with 18,693,577,728 bound seventy-second-lineage rotations, 13,352,555,520 bound lineage bindings, 8,011,533,312 bound handed-proof rebinds, and 2,670,511,104 bound verifier completions; admits 1,368,560,793,600 publication states with 124,414,617,600 fully bound one-hundred-forty-seventh-cold-restart recoveries; and admits 36,872,189,640 membership states with 30,168,155,160 bound witness-source replacements, 16,760,086,200 bound root-76 rollovers, 10,056,051,720 bound root-76 bindings, and 3,352,017,240 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `8c68646e4126e35e3388fd07ec0fd03d75dd8a622752806a7f3af36295215770`.

## Predecessor binding

V222 continues from committed V221 on `main`: V221 digest `b959ce47a9d1f4b7ab87297888577a4a509b5d0b1f7774e6be60e8d179cc6cbd`, implementation SHA-256 `b2a95f2c2f9cc3c2472b9662d35c1161161699daba398a85b8cb0d52a2db2ba2`, validator SHA-256 `9cc581ec49268e1049246edbd8500780e680e38026246c276379499b577a8a30`. V222 implementation SHA-256 is `37e040bfa868b7ddeb33234fa0a8f179a6bcb913fa8e4d5ff8d49cf463ed24cb` and standalone validator SHA-256 is `544553db1f4882b2d502876120bf75eb22619f939ec76dcd9e63773ea39511f7`.

Seed transitions are exact from V221: 576 epoch-172 completions (`2,617,977,600 / 4,545,100`), 27,648 restart recoveries (`121,942,858,752 / 4,410,549`), and 760 quorum-churn completions (`3,284,978,400 / 4,322,340`).

## Continuation gates

Epoch 173 rotates the seventy-second-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 147 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-seventh cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-75 witness rebind, rolls to root 76, binds root 76, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v222_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V223

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventy-third source in epoch 174, bind that source, and preserve the epoch-12 deadline; compose publication-147 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-eighth cold restart without cached-authority promotion; rebind the witness to root 76 after the root-76 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
