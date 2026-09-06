# WinLoop V236 validation report

## Verified result

V236 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-187 GC to 31,332,407,040 states with 24,369,649,920 bound seventy-ninth-lineage rotations, 17,406,892,800 bound lineage bindings, 10,444,135,680 bound handed-proof rebinds, and 3,481,378,560 bound verifier completions; admits 1,788,638,810,112 publication states with 162,603,528,192 fully bound one-hundred-sixty-first-cold-restart recoveries; and admits 48,272,939,000 membership states with 39,496,041,000 bound witness-source replacements, 21,942,245,000 bound root-83 rollovers, 13,165,347,000 bound root-83 bindings, and 4,388,449,000 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `2a95cce899a035bc349fbf013ccacdd426fbc624b07a281aff1065a154dc3ea7`.

## Predecessor binding

V236 continues from committed V235 on `main`: V235 digest `b70205c56c999805490005e930346414ec3fe858800ec3e85e35b2454a3dc5c6`, implementation SHA-256 `25b80917e7172b2a486c8bf3d3c65cd3c6e50013e0480c6983b1a0f603155a11`, validator SHA-256 `2704818a9f08751e5870e4780d7caaccd4d589b52f08b82708252c97a3456d72`. V236 implementation SHA-256 is `7a7593a0a2f52c29fb2806db426014389d3720c3d04550c801ccce4eead1b813` and standalone validator SHA-256 is `4dca0b4514929fd5aaa6009bf4b365a4e3ca0b8c25028fbad5aae4a18ab79374`.

Seed transitions are exact from V235: 576 epoch-186 completions (`3,418,652,160 / 5,935,160`), 27,648 restart recoveries (`159,647,155,200 / 5,774,275`), and 760 quorum-churn completions (`4,308,174,000 / 5,668,650`).

## Continuation gates

Epoch 187 rotates the seventy-ninth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 161 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 stays bound across the root-83 rollover, replaces the witness source, rolls to root 83, binds root 83, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v236_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V237

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eightieth source in epoch 188, bind that source, and preserve the epoch-12 deadline; compose publication-161 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixty-second cold restart without cached-authority promotion; keep generation 4 after root-83 rollover, rebind the witness to root 83, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
