# WinLoop V201 validation report

## Verified result

V201 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-152 GC to 11,947,703,040 states with 8,534,073,600 bound sixty-second-source handoffs, 5,120,444,160 bound sixty-second-source bindings, and 1,706,814,720 bound verifier completions; admits 870,477,898,752 publication states with 79,134,354,432 fully bound one-hundred-twenty-sixth-cold-restart recoveries; and admits 14,875,571,200 membership states with 10,625,408,000 bound root-65 witness rebinds, 6,375,244,800 bound witness renewals, and 2,125,081,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `452003633bf644ddc617ae166900bf18d19595410343e46eab3c2770070ded00`.

## Predecessor binding

V201 continues from committed V200 on `main`: V200 digest `fb27d2d370d8ff674d8931d0e29914e00e4c1da719f317577ffc75e783bdec8a`, implementation SHA-256 `28e0fce71b89b64e73ce779c3927c3365a2b8a1f1f3fdb0ff47bbd8d54bb1ee7`, validator SHA-256 `ae9a9fe3e2d85d8d98fafc8339c9689a5673682895639daba9e156f34606b467`. V201 implementation SHA-256 is `1349a415a8419a85dde0bfcf3aa3590efff45f95b7ab6baa6d441b2885279628` and standalone validator SHA-256 is `a63aec196a435e19f7c01d885a661bef42dcca2e20b17486e74292cfdb4868e0`.

Seed transitions are exact from V200: 576 epoch-151 completions (`1,667,877,120 / 2,895,620`), 27,648 restart recoveries (`77,308,231,680 / 2,796,160`), and 760 quorum-churn completions (`2,075,662,600 / 2,731,135`).

## Continuation gates

Epoch 152 hands the rebound proof to a sixty-second source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 126 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-twenty-sixth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 65 after the root-65 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v201_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V202

Keep independence fail closed absent a committed external verifier artifact; rotate the sixty-second-source lineage in epoch 153, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-126 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-twenty-seventh cold restart without cached-authority promotion; replace the witness source after the root-65 witness rebind, roll to root 66, bind root 66, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
