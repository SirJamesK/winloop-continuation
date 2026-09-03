# WinLoop V150 validation report

## Verified result

V150 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-101 GC to 3,472,865,280 states with 2,701,117,440 bound thirty-sixth-lineage rotations, 1,929,369,600 bound lineage bindings, 1,157,621,760 bound handed-proof rebinds, and 385,873,920 bound verifier completions; admits 192,424,826,880 publication states with 17,493,166,080 fully bound seventy-fifth-cold-restart recoveries; and admits 5,088,606,600 membership states with 4,163,405,400 bound witness-source replacements, 2,313,003,000 bound root-40 rollovers, 1,387,801,800 bound root-40 bindings, and 462,600,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `398889d8d3f100250b9ef2cce03089ceba73c90894b6abed7c919e959e2aed4f`.

## Predecessor binding

V150 continues from committed V149 on canonical branch `main`.

- V149 validation digest: `1d0c9a4f73c2c9f9c02b8e02a3c808cbb2760697f6d5cc791f620be8ee798048`
- V149 implementation SHA-256: `cef10f9dcee25d82635eff256317bdcfef874f96687a0c254214f566f9ec602e`
- V149 standalone validator SHA-256: `1f196cefc3253097c06d60c52556bb12261dc14477e54abe9476001a90e585e9`
- V150 implementation SHA-256: `777cc3ff4d9c844083997dcbc7fd1f1a4da8ae574a759506687ca01eebda2f37`
- V150 standalone validator SHA-256: `6ba96e314a283ce24968b0906db78d0a9c38153662fdea751225260a4f62f09e`

The seed transitions are exact from V149's fully bound outputs: 576 epoch-100 completions (`371,494,656 / 644,956`), 27,648 seventy-fourth-restart recoveries (`16,828,922,880 / 608,685`), and 760 membership quorum-churn completions (`444,809,760 / 585,276`).

## Continuation gates

Epoch 101 rotates the thirty-sixth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 3,472,865,280; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 75 composes the prior fully bound recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a seventy-fifth cold verifier restart. The exact accepted-state count is 192,424,826,880; cached-authority promotion remains rejected.

Membership at root 40 keeps generation 4 after the root-39 witness rebind, replaces the witness source, rolls to root 40, binds root 40, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 5,088,606,600; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v150_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V151

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; hand the rebound proof to a thirty-seventh source in epoch 102, bind that source, and preserve the epoch-12 deadline; compose publication-75 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a seventy-sixth cold verifier restart without cached-authority promotion; keep generation 4 after root-40 rollover, rebind the witness to root 40, renew the witness binding, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
