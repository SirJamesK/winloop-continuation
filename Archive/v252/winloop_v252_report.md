# WinLoop V252 validation report

## Verified result

V252 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-203 GC to 41,326,661,376 states with 32,142,958,848 bound eighty-seventh-lineage rotations, 22,959,256,320 bound lineage bindings, 13,775,553,792 bound handed-proof rebinds, and 4,591,851,264 bound verifier completions; admits 2,364,881,080,320 publication states with 214,989,189,120 fully bound one-hundred-seventy-seventh-cold-restart recoveries; and admits 63,929,413,240 membership states with 52,305,883,560 bound witness-source replacements, 29,058,824,200 bound root-91 rollovers, 17,435,294,520 bound root-91 bindings, and 5,811,764,840 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `e6c68201bf26c21e1f4e744a3576595de240af3475ef872c1c93cacb2dfdf631`.

## Predecessor binding

V252 continues from committed V251 on `main`: V251 digest `41d57be0cd6ddedde3f3b8714a1a677d169178fd7ed4ebbbd3885ca71023fe82`, implementation SHA-256 `940c57926616cd3e83efc7f5808b2833be8e406a90068b3dcc80e092fe8e3d88`, validator SHA-256 `f4651c84c3e02e81850c4ba2b02b324f6c136a7e5bff7c4ebe3ac94a4406e25d`. V252 implementation SHA-256 is `40918a49ed9c0fe83bab377f26fdcd9ac4f58898289208cd3c0158313b7e0a68` and standalone validator SHA-256 is `c19069f23734568af1321ed64aad27525e4a383a6986f4092bc3e5b47f1e7361`.

Seed transitions are exact from V251: 576 epoch-203 completions (`4,516,369,920 / 7,840,920`), 27,648 restart recoveries (`211,425,887,232 / 7,647,059`), and 760 quorum-churn completions (`5,714,903,600 / 7,519,610`).

## Continuation gates

Epoch 203 rotates the eighty-seventh-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 177 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-seventy-seventh cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-90 witness rebind, replaces the witness source, rolls to root 91, binds root 91, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v252_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V253

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-eighth source in epoch 204, bind that source, and preserve the epoch-12 deadline; compose publication-177 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-seventy-eighth cold restart without cached-authority promotion; keep generation 4 after the root-91 rollover, rebind the witness to root 91, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
