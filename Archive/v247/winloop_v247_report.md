# WinLoop V247 validation report

## Verified result

V247 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-198 GC to 29,559,011,328 states with 21,113,579,520 bound eighty-fifth-source handoffs, 12,668,147,712 bound eighty-fifth-source bindings, and 4,222,715,904 bound verifier completions; admits 2,173,230,259,200 publication states with 197,566,387,200 fully bound one-hundred-seventy-second-cold-restart recoveries; and admits 37,367,541,680 membership states with 26,691,101,200 bound root-88 witness rebinds, 16,014,660,720 bound witness renewals, and 5,338,220,240 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `57bcb3dfe34793d065b9aeb05534a61bbc1e3c1fcfd26acd7f7b88f23447a3f4`.

## Predecessor binding

V247 continues from committed V246 on `main`: V246 digest `1e84da39dd605279a3b8a3aa354da47a6e1c0f9104d3c4ed61162b0c27bfc526`, implementation SHA-256 `8a67a9d7812a4063663251db86c46c04b6850406e3d848b2d3555d0cbe817f8e`, validator SHA-256 `c875bff76850ea0a8aa1a0ac9c352c96c1cf76eaef9ab90c9b868e226374eec9`. V247 implementation SHA-256 is `7eca83d7f3a31c53294b21bcc942beefa9d2f30d21c1edf5cb89f422b25be73c` and standalone validator SHA-256 is `57a7897a47d8df692d9c14b70f3513410194ffae31f2c8b924b351de817ed5a0`.

Seed transitions are exact from V246: 576 epoch-198 completions (`4,151,347,200 / 7,207,200`), 27,648 restart recoveries (`194,198,833,152 / 7,023,974`), and 760 quorum-churn completions (`5,246,709,400 / 6,903,565`).

## Continuation gates

Epoch 198 hands the rebound proof to the eighty-fifth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 172 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-second cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-88 rollover, rebinds the witness to root 88, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v247_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V248

Keep independence fail closed absent a committed external verifier artifact; rotate the eighty-fifth-source lineage in epoch 199, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-172 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-third cold restart without cached-authority promotion; keep generation 4 after the root-88 witness rebind, replace the witness source, roll to root 89, bind root 89, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
