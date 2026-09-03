# WinLoop V170 validation report

## Verified result

V170 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-121 GC to 6,808,665,600 states with 5,295,628,800 bound forty-sixth-lineage rotations, 3,782,592,000 bound lineage bindings, 2,269,555,200 bound handed-proof rebinds, and 756,518,400 bound verifier completions; admits 381,647,185,920 publication states with 34,695,198,720 fully bound ninety-fifth-cold-restart recoveries; and admits 10,172,991,400 membership states with 8,323,356,600 bound witness-source replacements, 4,624,087,000 bound root-50 rollovers, 2,774,452,200 bound root-50 bindings, and 924,817,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `bde19cca2adacecbdaccb7ec8124bfbf6933750bd81749be0ae2c98c688a209f`.

## Predecessor binding

V170 continues from committed V169 on canonical branch `main`.

- V169 validation digest: `0f9ac6b0c9a51bb20da324c5d429b049c1055fa649b6a1ec5208e2106fdc8ffb`
- V169 implementation SHA-256: `134550703fd4eaa035434431dd3c505d5b56f2561ae84d34f58c5f4a611ec282`
- V169 standalone validator SHA-256: `36a560e5ad242966bb1a8993870ffc874b143e474cc164d9fce8cc058bd5d350`
- V170 implementation SHA-256: `b0b69c9be3d5bc641f1058df0cac7cd51fd1b98e26b037b79c4f85f124a1d378`
- V170 standalone validator SHA-256: `3426b0f2e84e3b8f0984e0c0262b5f29469a18730c5057238a550cb793952150`

The seed transitions are exact from V169's fully bound outputs: 576 epoch-120 completions (`733,936,896 / 1,274,196`), 27,648 ninety-fourth-restart recoveries (`33,643,883,520 / 1,216,865`), and 760 membership quorum-churn completions (`896,508,160 / 1,179,616`).

## Continuation gates

Epoch 121 rotates the forty-sixth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 6,808,665,600; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 95 composes the prior fully bound recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a ninety-fifth cold verifier restart. The exact accepted-state count is 381,647,185,920; cached-authority promotion remains rejected.

Membership stays at generation 4 after the root-49 witness rebind, replaces the witness source, rolls to root 50, binds root 50, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 10,172,991,400; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v170_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V171

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; hand the rebound proof to a forty-seventh source in epoch 122, bind that source, and preserve the epoch-12 deadline; compose publication-95 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a ninety-sixth cold verifier restart without cached-authority promotion; keep generation 4 after the root-50 rollover, rebind the witness to root 50, renew the witness binding, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
