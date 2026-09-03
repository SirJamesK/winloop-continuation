# WinLoop V157 validation report

## Verified result

V157 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-108 GC to 3,479,309,568 states with 2,485,221,120 bound fortieth-source handoffs, 1,491,132,672 bound fortieth-source bindings, and 497,044,224 bound verifier completions; admits 249,021,527,040 publication states with 22,638,320,640 fully bound eighty-second-cold-restart recoveries; and admits 4,204,098,080 membership states with 3,002,927,200 bound root-43 witness rebinds, 1,801,756,320 bound witness renewals, and 600,585,440 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `3804b07e96cb5d35586c9472e4deff835af0fb966d340330b588d83fb6d43973`.

## Predecessor binding

V157 continues from committed V156 on canonical branch `main`.

- V156 validation digest: `3db99058ca4aefcf159517a3afec5b912f3ec19b25c8079f480d56b3db2f33da`
- V156 implementation SHA-256: `90da6d7348aeb725e3b1c65b826ec6547e7761ac49ac26ed1480d1c0b47451ee`
- V156 standalone validator SHA-256: `863ee476c014bd299d947b223831a6f4aa04ec1b191a44a3217526c145e65cd2`
- V157 implementation SHA-256: `9868da75f0937a6987ed88e13a1dc6cf6830c892357940f9ee5bd59731a18a8f`
- V157 standalone validator SHA-256: `6317ff11cef5b1e7d56c9d345e7a480477162a84d41e9c6f1ead3c1661ef3723`

The seed transitions are exact from V156's fully bound outputs: 576 epoch-107 completions (`480,003,840 / 833,340`), 27,648 eighty-first-restart recoveries (`21,848,666,112 / 790,244`), and 760 membership quorum-churn completions (`579,389,800 / 762,355`).

## Continuation gates

Epoch 108 hands the rebound proof to a fortieth source, binds that source, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 3,479,309,568; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 82 composes the prior fully bound recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and an eighty-second cold verifier restart. The exact accepted-state count is 249,021,527,040; cached-authority promotion remains rejected.

Membership at root 43 keeps generation 4 after the root-43 rollover, rebinds the witness to root 43, renews that witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 4,204,098,080; modeled stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v157_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V158

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; rotate the fortieth-source lineage in epoch 109, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-82 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and an eighty-third cold verifier restart without cached-authority promotion; keep generation 4 after the root-43 witness rebind, replace the witness source, roll to root 44, bind root 44, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
