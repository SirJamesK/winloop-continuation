# WinLoop V265 validation report

## Verified result

V265 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-216 GC to 39,556,258,560 states with 28,254,470,400 bound ninety-fourth-source handoffs, 16,952,682,240 bound ninety-fourth-source bindings, and 5,650,894,080 bound verifier completions; admits 2,915,171,804,160 publication states with 265,015,618,560 fully bound one-hundred-ninetieth-cold-restart recoveries; and admits 50,205,478,400 membership states with 35,861,056,000 bound root-97 witness rebinds, 21,516,633,600 bound witness renewals, and 7,172,211,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `81870ca05d1b9c0a25caa34fc83019f629c46ce4c358f6f943ed3d7f7b89d670`.

## Predecessor binding

V265 continues from committed V264 on `main`: V264 digest `128a91fc09591669f3f572286e2e72d2c9a267d32fc6987d33fbf435fe38ce13`, implementation SHA-256 `44b2d6407bf380a8736dc55768e88460180023a0f193a360e6995931bc00f0ef`, validator SHA-256 `be09278d1979c6370615ca07d6048781a3588e0dec528e488757a44260bebea4`. V265 implementation SHA-256 is `286953d7f75fca97934ec3023fc7f0b7ac663e84018ddb274db84fc21636b8fc`.

Seed transitions are exact from V264: 576 epoch-216 seeds (`5,564,180,736 / 9,660,036`), 27,648 restart recoveries (`260,917,493,760 / 9,437,120`), and 760 quorum-churn completions (`7,060,727,560 / 9,290,431`).

## Continuation gates

Epoch 216 hands the rebound proof to the ninety-fourth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 190 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-ninetieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-97 rollover, rebinds the witness to root 97, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v265_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V266

Keep independence fail closed absent a committed external verifier artifact; rotate the ninety-fourth-source lineage in epoch 217, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-190 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-ninety-first cold restart without cached-authority promotion; keep generation 4 after the root-97 witness rebind, replace the witness source, roll to root 98, bind root 98, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
