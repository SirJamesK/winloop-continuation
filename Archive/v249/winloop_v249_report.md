# WinLoop V249 validation report

## Verified result

V249 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-200 GC to 30,575,284,992 states with 21,839,489,280 bound eighty-sixth-source handoffs, 13,103,693,568 bound eighty-sixth-source bindings, and 4,367,897,856 bound verifier completions; admits 2,248,596,218,880 publication states with 204,417,838,080 fully bound one-hundred-seventy-fourth-cold-restart recoveries; and admits 38,670,952,320 membership states with 27,622,108,800 bound root-89 witness rebinds, 16,573,265,280 bound witness renewals, and 5,524,421,760 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `8cf21664fe3ffffbd48f0a71a6d92f7c5b87a48a3fddaef99107399fd52632bc`.

## Predecessor binding

V249 continues from committed V248 on `main`: V248 digest `e870c97516fa22f8756317b401dc465dd0be10f9e8264ccb33db678175c58c9e`, implementation SHA-256 `2f5066f8d93733ebb7f5dbf630dd20bf0a162e4622af5537b565159c1966895a`, validator SHA-256 `173a2114c5ee3aa85c2c1bd151c87f802608baa97a0f08585fde2058c68e1171`. V249 implementation SHA-256 is `36e7e10f5b7157496c633e8c5dfea9fa5b73e59674ee79c8b84c002e12e2242a` and standalone validator SHA-256 is `389cd01713e3efe16e2ae22df11fcac5a7be81b22b003e2ce4be75f2569c2f14`.

Seed transitions are exact from V248: 576 epoch-200 completions (`4,294,897,920 / 7,456,420`), 27,648 restart recoveries (`200,972,648,448 / 7,268,976`), and 760 quorum-churn completions (`5,430,789,000 / 7,145,775`).

## Continuation gates

Epoch 200 hands the rebound proof to an eighty-sixth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 174 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-fourth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-89 rollover, rebinds the witness to root 89, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v249_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V250

Keep independence fail closed absent a committed external verifier artifact; rotate the eighty-sixth-source lineage in epoch 201, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-174 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-fifth cold restart without cached-authority promotion; keep generation 4 after the root-89 witness rebind, replace the witness source, roll to root 90, bind root 90, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
