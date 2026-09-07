# WinLoop V264 validation report

## Verified result

V264 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-215 GC to 50,077,626,624 states with 38,949,265,152 bound ninety-third-lineage rotations, 27,820,903,680 bound lineage bindings, 16,692,542,208 bound handed-proof rebinds, and 5,564,180,736 bound verifier completions; admits 2,870,092,431,360 publication states with 260,917,493,760 fully bound one-hundred-eighty-ninth-cold-restart recoveries; and admits 77,668,003,160 membership states with 63,546,548,040 bound witness-source replacements, 35,303,637,800 bound root-97 rollovers, 21,182,182,680 bound root-97 bindings, and 7,060,727,560 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `128a91fc09591669f3f572286e2e72d2c9a267d32fc6987d33fbf435fe38ce13`.

## Predecessor binding

V264 continues from committed V263 on `main`: V263 digest `7e7d22a01ba8499261cb6d2b1947f6e686b3c003eacb6ffc2b30350c5bbab120`, implementation SHA-256 `a3ded951d5e6ecf9ddfbd95e4e1df9f08f92a20a33e861a787c71ca1cff89c9a`, validator SHA-256 `dae0ce682deef9b363ddb04c166b8c17641c6784a8b2237fdf9bf32a7a998924`. V264 implementation SHA-256 is `44b2d6407bf380a8736dc55768e88460180023a0f193a360e6995931bc00f0ef`.

Seed transitions are exact from V263: 576 epoch-215 seeds (`5,478,359,040 / 9,511,040`), 27,648 restart recoveries (`256,861,836,288 / 9,290,431`), and 760 quorum-churn completions (`6,950,405,200 / 9,145,270`).

## Continuation gates

Epoch 215 rotates the ninety-third-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 189 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-ninth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-96 witness rebind, replaces the witness source, rolls to root 97, binds root 97, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v264_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V265

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a ninety-fourth source in epoch 216, bind that source, and preserve the epoch-12 deadline; compose publication-189 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-ninetieth cold restart without cached-authority promotion; keep generation 4 after root-97 rollover, rebind the witness to root 97, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
