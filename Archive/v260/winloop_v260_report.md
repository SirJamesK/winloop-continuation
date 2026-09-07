# WinLoop V260 validation report

## Verified result

V260 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-211 GC to 47,035,779,840 states with 36,583,384,320 bound ninety-first-lineage rotations, 26,130,988,800 bound lineage bindings, 15,678,593,280 bound handed-proof rebinds, and 5,226,197,760 bound verifier completions; admits 2,694,422,016,000 publication states with 244,947,456,000 fully bound one-hundred-eighty-fifth-cold-restart recoveries; and admits 72,889,795,000 membership states with 59,637,105,000 bound witness-source replacements, 33,131,725,000 bound root-95 rollovers, 19,879,035,000 bound root-95 bindings, and 6,626,345,000 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `20425a75d5c99d149d8e1b7bbbac2ec20ecc05c2db31c3cd2a740648f6a5a587`.

## Predecessor binding

V260 continues from committed V259 on `main`: V259 digest `73be9257533223ffdd0521c9334c81b7e15062651c10701f37320cfb5d6c8e0b`, implementation SHA-256 `921243c1753cc3a33215be48fdb780e18870cc4ba96e160afa7addb41d706b65`, validator SHA-256 `0f898909b63970a3d97dfe5a7f71100c4a6bcfe059ee16855de39ceec66f90b5`. V260 implementation SHA-256 is `e23eb119a374f4136a866c812d6008437e05a42327f573c66a3f583b581d8708`.

Seed transitions are exact from V259: 576 epoch-211 seeds (`5,143,896,576 / 8,930,376`), 27,648 restart recoveries (`241,059,456,000 / 8,718,875`), and 760 quorum-churn completions (`6,520,606,960 / 8,579,746`).

## Continuation gates

Epoch 211 rotates the ninety-first-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 185 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-fifth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-94 witness rebind, replaces the witness source, rolls to root 95, binds root 95, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v260_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V261

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a ninety-second source in epoch 212, bind that source, and preserve the epoch-12 deadline; compose publication-185 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-eighty-sixth cold restart without cached-authority promotion; keep generation 4 after root-95 rollover, rebind the witness to root 95, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
