# WinLoop V200 validation report

## Verified result

V200 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-151 GC to 15,010,894,080 states with 11,675,139,840 bound sixty-first-lineage rotations, 8,339,385,600 bound lineage bindings, 5,003,631,360 bound handed-proof rebinds, and 1,667,877,120 bound verifier completions; admits 850,390,548,480 publication states with 77,308,231,680 fully bound one-hundred-twenty-fifth-cold-restart recoveries; and admits 22,832,288,600 membership states with 18,680,963,400 bound witness-source replacements, 10,378,313,000 bound root-65 rollovers, 6,226,987,800 bound root-65 bindings, and 2,075,662,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `fb27d2d370d8ff674d8931d0e29914e00e4c1da719f317577ffc75e783bdec8a`.

## Predecessor binding

V200 continues from committed V199 on `main`: V199 digest `501c8219d470a49bbc8e25bbac739a1fc39f3aa4193b26f07908b1272f5b45a5`, implementation SHA-256 `8fa3bcedd8ef97911088ed2657bbf560f5a8d354e10647253015e1e1026b1d9c`, validator SHA-256 `e186b738f41d2e258437e1c0d08f1d6b7b78269fd2d315fc8414869d4a392dff`. V200 implementation SHA-256 is `28e0fce71b89b64e73ce779c3927c3365a2b8a1f1f3fdb0ff47bbd8d54bb1ee7` and standalone validator SHA-256 is `ae9a9fe3e2d85d8d98fafc8339c9689a5673682895639daba9e156f34606b467`.

Seed transitions are exact from V199: 576 epoch-150 completions (`1,629,536,256 / 2,829,056`), 27,648 restart recoveries (`75,510,420,480 / 2,731,135`), and 760 quorum-churn completions (`2,027,015,760 / 2,667,126`).

## Continuation gates

Epoch 151 rotates the sixty-first-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 125 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-twenty-fifth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-64 witness rebind, rolls to root 65, binds root 65, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v200_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V201

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a sixty-second source in epoch 152, bind that source, and preserve the epoch-12 deadline; compose publication-125 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-twenty-sixth cold restart without cached-authority promotion; rebind the witness to root 65 after the root-65 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
