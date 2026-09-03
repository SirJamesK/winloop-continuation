# WinLoop V166 validation report

## Verified result

V166 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-117 GC to 6,020,075,520 states with 4,682,280,960 bound forty-fourth-lineage rotations, 3,344,486,400 bound lineage bindings, 2,006,691,840 bound handed-proof rebinds, and 668,897,280 bound verifier completions; admits 336,795,604,992 publication states with 30,617,782,272 fully bound ninety-first-cold-restart recoveries; and admits 8,965,640,200 membership states with 7,335,523,800 bound witness-source replacements, 4,075,291,000 bound root-48 rollovers, 2,445,174,600 bound root-48 bindings, and 815,058,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `993479ae487202702932dddc0873e4a186a3f44e99e7946ceddb44db664986fe`.

## Predecessor binding

V166 continues from committed V165 on canonical branch `main`.

- V165 validation digest: `2ce9e465accb92df1e7c88102df13a716a827798c34c81f3809fb24a34602723`
- V165 implementation SHA-256: `58c9fe655298e48389bec9a03884f924b382c8d538296b8d3fef8145ece2be2c`
- V165 standalone validator SHA-256: `ab88586e91fa38967b122a8b47c4109da0d3dd4c889541fcedc6a381c4af10dd`
- V166 implementation SHA-256: `f476f36f3eaeb7d2f1f333d59c665290538270775f38cf8dc57ebe15a48f26cc`
- V166 standalone validator SHA-256: `e52d3b2d0880ef39758a36e9c114c8eaa02b5dbcc60ba32dd5bd0f470f430735`

The seed transitions are exact from V165's fully bound outputs: 576 epoch-116 completions (`648,103,680 / 1,125,180`), 27,648 ninetieth-restart recoveries (`29,650,959,360 / 1,072,445`), and 760 membership quorum-churn completions (`789,047,200 / 1,038,220`).

## Continuation gates

Epoch 117 rotates the forty-fourth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 6,020,075,520; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 91 composes the prior fully bound recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a ninety-first cold verifier restart. The exact accepted-state count is 336,795,604,992; cached-authority promotion remains rejected.

Membership stays at generation 4 after the root-47 witness rebind, replaces the witness source, rolls to root 48, binds root 48, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 8,965,640,200; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v166_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V167

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; hand the rebound proof to a forty-fifth source in epoch 118, bind that source, and preserve the epoch-12 deadline; compose publication-91 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a ninety-second cold verifier restart without cached-authority promotion; keep generation 4 after the root-48 rollover, rebind the witness to root 48, renew the witness binding, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
