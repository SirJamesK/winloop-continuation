# WinLoop V171 validation report

## Verified result

V171 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-122 GC to 5,456,908,800 states with 3,897,792,000 bound forty-seventh-source handoffs, 2,338,675,200 bound forty-seventh-source bindings, and 779,558,400 bound verifier completions; admits 393,450,089,472 publication states with 35,768,189,952 fully bound ninety-sixth-cold-restart recoveries; and admits 6,676,014,800 membership states with 4,768,582,000 bound root-50 witness rebinds, 2,861,149,200 bound witness renewals, and 953,716,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `f172d28c7de90221819e46a4117ea47ebc3d5c2d01019d71579ee7e4c9988b81`.

## Predecessor binding

V171 continues from committed V170 on canonical branch `main`.

- V170 validation digest: `bde19cca2adacecbdaccb7ec8124bfbf6933750bd81749be0ae2c98c688a209f`
- V170 implementation SHA-256: `b0b69c9be3d5bc641f1058df0cac7cd51fd1b98e26b037b79c4f85f124a1d378`
- V170 standalone validator SHA-256: `3426b0f2e84e3b8f0984e0c0262b5f29469a18730c5057238a550cb793952150`
- V171 implementation SHA-256: `9afd36b7c73880cafea5b5bf822db8da592d6971ded0c5fb03f089dd99c72c11`
- V171 standalone validator SHA-256: `c34d62fada131327ab18e9c6d44096a9fb93c4904e35e44176329449753c7a58`

The seed transitions are exact from V170's fully bound outputs: 576 epoch-121 completions (`756,518,400 / 1,313,400`), 27,648 ninety-fifth-restart recoveries (`34,695,198,720 / 1,254,890`), and 760 membership quorum-churn completions (`924,817,400 / 1,216,865`).

## Continuation gates

Epoch 122 hands the rebound proof to a forty-seventh source, binds that source, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 5,456,908,800; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 96 composes the prior fully bound recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a ninety-sixth cold verifier restart. The exact accepted-state count is 393,450,089,472; cached-authority promotion remains rejected.

Membership stays at generation 4 after the root-50 rollover, rebinds the witness to root 50, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 6,676,014,800; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v171_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V172

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; rotate the forty-seventh-source lineage in epoch 123, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-96 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a ninety-seventh cold verifier restart without cached-authority promotion; keep generation 4 after the root-50 witness rebind, replace the witness source, roll to root 51, bind root 51, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
