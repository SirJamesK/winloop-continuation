# WinLoop V235 validation report

## Verified result

V235 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-186 GC to 23,930,565,120 states with 17,093,260,800 bound seventy-ninth-source handoffs, 10,255,956,480 bound seventy-ninth-source bindings, and 3,418,652,160 bound verifier completions; admits 1,756,118,707,200 publication states with 159,647,155,200 fully bound one-hundred-sixtieth-cold-restart recoveries; and admits 30,157,218,000 membership states with 21,540,870,000 bound root-82 witness rebinds, 12,924,522,000 bound witness renewals, and 4,308,174,000 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `b70205c56c999805490005e930346414ec3fe858800ec3e85e35b2454a3dc5c6`.

## Predecessor binding

V235 continues from committed V234 on `main`: V234 digest `5571e2e304639ebfa7a307b44a0cab6853bba517d07db3d5085521db7a7fcf77`, implementation SHA-256 `8337d74a4aac26d3257955f31ed8b416540338b9468f39700e337507e62a55de`, validator SHA-256 `41c5e3cc77797e6f18c16bff44828f73862926608e2f8717a3d23879b6cde7c4`. V235 implementation SHA-256 is `25b80917e7172b2a486c8bf3d3c65cd3c6e50013e0480c6983b1a0f603155a11` and standalone validator SHA-256 is `2704818a9f08751e5870e4780d7caaccd4d589b52f08b82708252c97a3456d72`.

Seed transitions are exact from V234: 576 epoch-185 completions (`3,356,683,776 / 5,827,576`), 27,648 restart recoveries (`156,726,835,200 / 5,668,650`), and 760 quorum-churn completions (`4,228,883,960 / 5,564,321`).

## Continuation gates

Epoch 186 hands the rebound proof to a seventy-ninth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 160 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixtieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 stays bound to root 82 after rollover, rebinds the witness to root 82, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v235_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V236

Keep independence fail closed absent a committed external verifier artifact; rotate the seventy-ninth-source lineage in epoch 187, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-160 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-first cold restart without cached-authority promotion; keep generation 4 after the root-82 witness rebind, replace the witness source, roll to root 83, bind root 83, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
