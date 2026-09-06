# WinLoop V240 validation report

## Verified result

V240 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-191 GC to 33,659,608,320 states with 26,179,695,360 bound eighty-first-lineage rotations, 18,699,782,400 bound lineage bindings, 11,219,869,440 bound handed-proof rebinds, and 3,739,956,480 bound verifier completions; admits 1,922,733,711,360 publication states with 174,793,973,760 fully bound one-hundred-sixty-fifth-cold-restart recoveries; and admits 51,914,722,200 membership states with 42,475,681,800 bound witness-source replacements, 23,597,601,000 bound root-85 rollovers, 14,158,560,600 bound root-85 bindings, and 4,719,520,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `af32248521f4a70a41d31a5f58008eb994a52f16124f9be3cb41b2d0c3701f81`.

## Predecessor binding

V240 continues from committed V239 on `main`: V239 digest `b411292e695de9e34b42ca5eeb1d1483b2aeb032d7d7808abbdfb534adc64cee`, implementation SHA-256 `249eb4e15eb07326bed2a7185868660bb002c73848b82367adb22df61d29e084`, validator SHA-256 `0eb21ce50f2d3737002bc2ff44b2efb5beaf334cf50592ad4456f070f6c64a70`. V240 implementation SHA-256 is `8a327849dec26c1f26de2cf0a71dd1bf60d7e1e1169fccc3d780bc0dfdc6e39a` and standalone validator SHA-256 is `50a45c0cebb2ac145033618387caeeb99c9a1a1412466077a96799e3fc278bc7`.

Seed transitions are exact from V239: 576 epoch-190 completions (`3,674,151,936 / 6,378,736`), 27,648 restart recoveries (`171,691,176,960 / 6,209,895`), and 760 quorum-churn completions (`4,635,244,560 / 6,099,006`).

## Continuation gates

Epoch 191 rotates the eighty-first-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 165 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-sixty-fifth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 stays bound after the root-84 witness rebind, replaces the witness source, rolls to root 85, binds root 85, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v240_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V241

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to an eighty-second source in epoch 192, bind that source, and preserve the epoch-12 deadline; compose publication-165 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-sixty-sixth cold restart without cached-authority promotion; keep generation 4 after the root-85 rollover, rebind the witness to root 85, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
