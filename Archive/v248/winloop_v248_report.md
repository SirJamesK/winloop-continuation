# WinLoop V248 validation report

## Verified result

V248 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-199 GC to 38,654,081,280 states with 30,064,285,440 bound eighty-fifth-lineage rotations, 21,474,489,600 bound lineage bindings, 12,884,693,760 bound handed-proof rebinds, and 4,294,897,920 bound verifier completions; admits 2,210,699,132,928 publication states with 200,972,648,448 fully bound one-hundred-seventy-third-cold-restart recoveries; and admits 59,738,679,000 membership states with 48,877,101,000 bound witness-source replacements, 27,153,945,000 bound root-89 rollovers, 16,292,367,000 bound root-89 bindings, and 5,430,789,000 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `e870c97516fa22f8756317b401dc465dd0be10f9e8264ccb33db678175c58c9e`.

## Predecessor binding

V248 continues from committed V247 on `main`: V247 digest `57bcb3dfe34793d065b9aeb05534a61bbc1e3c1fcfd26acd7f7b88f23447a3f4`, implementation SHA-256 `7eca83d7f3a31c53294b21bcc942beefa9d2f30d21c1edf5cb89f422b25be73c`, validator SHA-256 `57a7897a47d8df692d9c14b70f3513410194ffae31f2c8b924b351de817ed5a0`. V248 implementation SHA-256 is `2f5066f8d93733ebb7f5dbf630dd20bf0a162e4622af5537b565159c1966895a` and standalone validator SHA-256 is `173a2114c5ee3aa85c2c1bd151c87f802608baa97a0f08585fde2058c68e1171`.

Seed transitions are exact from V247: 576 epoch-199 completions (`4,222,715,904 / 7,331,104`), 27,648 restart recoveries (`197,566,387,200 / 7,145,775`), and 760 quorum-churn completions (`5,338,220,240 / 7,023,974`).

## Continuation gates

Epoch 199 rotates the eighty-fifth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 173 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-third cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-88 witness rebind, replaces the witness source, rolls to root 89, binds root 89, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness-source, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v248_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V249

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-sixth source in epoch 200, bind that source, and preserve the epoch-12 deadline; compose publication-173 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-fourth cold restart without cached-authority promotion; keep generation 4 after the root-89 rollover, rebind the witness to root 89, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
