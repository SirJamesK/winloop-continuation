# WinLoop V221 validation report

## Verified result

V221 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-172 GC to 18,325,843,200 states with 13,089,888,000 bound seventy-second-source handoffs, 7,853,932,800 bound seventy-second-source bindings, and 2,617,977,600 bound verifier completions; admits 1,341,371,446,272 publication states with 121,942,858,752 fully bound one-hundred-forty-sixth-cold-restart recoveries; and admits 22,994,848,800 membership states with 16,424,892,000 bound root-75 witness rebinds, 9,854,935,200 bound witness renewals, and 3,284,978,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `b959ce47a9d1f4b7ab87297888577a4a509b5d0b1f7774e6be60e8d179cc6cbd`.

## Predecessor binding

V221 continues from committed V220 on `main`: V220 digest `5a51addc1c5f6efbbe22a502fca579bbccc3c2dce87d9669493b81b06baff4a9`, implementation SHA-256 `4f0a5db251997806c847faa8be14d427f8c97d01ae8a1860554ab1b085e5d2f6`, validator SHA-256 `4e5c6fac5256570353a89d7a7af289c2ce9e1698a2edb0a63b1a6766301406e2`. V221 implementation SHA-256 is `b2a95f2c2f9cc3c2472b9662d35c1161161699daba398a85b8cb0d52a2db2ba2` and standalone validator SHA-256 is `9cc581ec49268e1049246edbd8500780e680e38026246c276379499b577a8a30`.

Seed transitions are exact from V220: 576 epoch-171 completions (`2,566,137,600 / 4,455,100`), 27,648 restart recoveries (`119,504,056,320 / 4,322,340`), and 760 quorum-churn completions (`3,218,839,400 / 4,235,315`).

## Continuation gates

Epoch 172 hands the rebound proof to a seventy-second source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 146 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-sixth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 75 after the root-75 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v221_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V222

Keep independence fail closed absent a committed external verifier artifact; rotate the seventy-second-source lineage in epoch 173, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-146 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-seventh cold restart without cached-authority promotion; replace the witness source after the root-75 witness rebind, roll to root 76, bind root 76, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
