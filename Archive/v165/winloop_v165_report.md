# WinLoop V165 validation report

## Verified result

V165 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-116 GC to 4,536,725,760 states with 3,240,518,400 bound forty-fourth-source handoffs, 1,944,311,040 bound forty-fourth-source bindings, and 648,103,680 bound verifier completions; admits 326,160,552,960 publication states with 29,650,959,360 fully bound ninetieth-cold-restart recoveries; and admits 5,523,330,400 membership states with 3,945,236,000 bound root-47 witness rebinds, 2,367,141,600 bound witness renewals, and 789,047,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `2ce9e465accb92df1e7c88102df13a716a827798c34c81f3809fb24a34602723`.

## Predecessor binding

V165 continues from committed V164 on canonical branch `main`.

- V164 validation digest: `2b0092fc11df7b3cb3a8355d95c1821ada8082708567d73ceca71a26b7793166`
- V164 implementation SHA-256: `4f1117801a46d52af44242e0fc86e506b301893576701b512b34661c265848e2`
- V164 standalone validator SHA-256: `531d5e267bdebba7a675c80f7c449b99eac836df98dc0e27c53e631bb2115538`
- V165 implementation SHA-256: `58c9fe655298e48389bec9a03884f924b382c8d538296b8d3fef8145ece2be2c`
- V165 standalone validator SHA-256: `ab88586e91fa38967b122a8b47c4109da0d3dd4c889541fcedc6a381c4af10dd`

The seed transitions are exact from V164's fully bound outputs: 576 epoch-115 completions (`627,745,536 / 1,089,836`), 27,648 eighty-ninth-restart recoveries (`28,704,706,560 / 1,038,220`), and 760 membership quorum-churn completions (`763,595,560 / 1,004,731`).

## Continuation gates

Epoch 116 hands the rebound proof to a forty-fourth source, binds that source, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 4,536,725,760; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 90 composes the prior fully bound recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a ninetieth cold verifier restart. The exact accepted-state count is 326,160,552,960; cached-authority promotion remains rejected.

Membership stays at generation 4 after the root-47 rollover, rebinds the witness to root 47, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 5,523,330,400; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v165_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V166

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; rotate the forty-fourth-source lineage in epoch 117, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-90 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a ninety-first cold verifier restart without cached-authority promotion; keep generation 4 after the root-47 witness rebind, replace the witness source, roll to root 48, bind root 48, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
