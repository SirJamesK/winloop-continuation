# WinLoop V261 validation report

## Verified result

V261 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-212 GC to 37,165,605,120 states with 26,546,860,800 bound ninety-second-source handoffs, 15,928,116,480 bound ninety-second-source bindings, and 5,309,372,160 bound verifier completions; admits 2,737,647,424,512 publication states with 248,877,038,592 fully bound one-hundred-eighty-sixth-cold-restart recoveries; and admits 47,132,540,000 membership states with 33,666,100,000 bound root-95 witness rebinds, 20,199,660,000 bound witness renewals, and 6,733,220,000 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `8610ec2b9b60aeb1e4a44662255ad519f50606fef9f511289642bcd8ed0d6623`.

## Predecessor binding

V261 continues from committed V260 on `main`: V260 digest `20425a75d5c99d149d8e1b7bbbac2ec20ecc05c2db31c3cd2a740648f6a5a587`, implementation SHA-256 `e23eb119a374f4136a866c812d6008437e05a42327f573c66a3f583b581d8708`, validator SHA-256 `6d151d10f44c344b15df9a863c622b07093156307d19a919288f12de438c5684`. V261 implementation SHA-256 is `26932d997f8dc048edcc0053e4aca5fbed51e6705f1ca7e7216c7bf08d9b9828`.

Seed transitions are exact from V260: 576 epoch-212 seeds (`5,226,197,760 / 9,073,260`), 27,648 restart recoveries (`244,947,456,000 / 8,859,500`), and 760 quorum-churn completions (`6,626,345,000 / 8,718,875`).

## Continuation gates

Epoch 212 hands the rebound proof to the ninety-second source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 186 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-eighty-sixth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-95 rollover, rebinds the witness to root 95, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v261_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V262

Keep independence fail closed absent a committed external verifier artifact; rotate the ninety-second-source lineage in epoch 213, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-186 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-seventh cold restart without cached-authority promotion; keep generation 4 after the root-95 witness rebind, replace the witness source, roll to root 96, bind root 96, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
