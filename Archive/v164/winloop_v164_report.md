# WinLoop V164 validation report

## Verified result

V164 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-115 GC to 5,649,709,824 states with 4,394,218,752 bound forty-third-lineage rotations, 3,138,727,680 bound lineage bindings, 1,883,236,608 bound handed-proof rebinds, and 627,745,536 bound verifier completions; admits 315,751,772,160 publication states with 28,704,706,560 fully bound eighty-ninth-cold-restart recoveries; and admits 8,399,551,160 membership states with 6,872,360,040 bound witness-source replacements, 3,817,977,800 bound root-47 rollovers, 2,290,786,680 bound root-47 bindings, and 763,595,560 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `2b0092fc11df7b3cb3a8355d95c1821ada8082708567d73ceca71a26b7793166`.

## Predecessor binding

V164 continues from committed V163 on canonical branch `main`.

- V163 validation digest: `82df8e634a70151c98cab7644bcf63c2aaf1f84aba4694f8d688bcc0061f8ff6`
- V163 implementation SHA-256: `d3a57aad4c9eae1bad93ff010e4407317951771d2b50f3d51a892efcfcbf2a2e`
- V163 standalone validator SHA-256: `7cdfb3a2331fd5a3e0326e7642525c1282a6d8d5df0957f083999feb98f704e5`
- V164 implementation SHA-256: `4f1117801a46d52af44242e0fc86e506b301893576701b512b34661c265848e2`
- V164 standalone validator SHA-256: `531d5e267bdebba7a675c80f7c449b99eac836df98dc0e27c53e631bb2115538`

The seed transitions are exact from V163's fully bound outputs: 576 epoch-114 completions (`607,818,240 / 1,055,240`), 27,648 eighty-eighth-restart recoveries (`27,778,802,688 / 1,004,731`), and 760 membership quorum-churn completions (`738,697,200 / 971,970`).

## Continuation gates

Epoch 115 rotates the forty-third-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while retaining the epoch-12 deadline origin. The exact accepted-state count is 5,649,709,824; every modeled stale, conflicting, incomplete, continuity-broken, root-broken, carried-proof-broken, or deadline-reset mutation is rejected.

Publication 89 composes the prior fully bound recovery with replacement-source churn, successor-source binding, fresh reconciliation, and an eighty-ninth cold verifier restart. The exact accepted-state count is 315,751,772,160; cached-authority promotion remains rejected.

Membership stays at generation 4 after the root-46 witness rebind, replaces the witness source, rolls to root 47, binds root 47, and requires replication-quorum churn while preserving tombstone and prior-source continuity. The exact accepted-state count is 8,399,551,160; modeled stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations are rejected.

## Preserved bounds

V21 guarded routing remains active; no replacement runtime envelope is claimed. Admission remains joint false-WIN cut 21, provenance cut 22, and synthetic lower cost 63. Cross-role credit remains 12 because no committed external independence certificate was found. Temporal horizon 22 floor 1 budget 851 and horizon 11 floor 2 budget 398 are preserved. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation method

`winloop_v164_validate.py` independently imports the implementation, regenerates the validation object, checks predecessor seed arithmetic, exact gate counts, fail-closed mutation checks, preserved admission/routing/temporal/checkpoint invariants, and every SHA-256 manifest entry. The JSON manifest entry is hashed in canonical compact JSON form; all other manifest entries use raw-file SHA-256.

## Unresolved frontier for V165

Continue exactly one version: keep independence fail closed unless an immutable external verifier artifact is committed; hand the rebound proof to a forty-fourth source in epoch 116, bind that source, and preserve the epoch-12 deadline; compose publication-89 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a ninetieth cold verifier restart without cached-authority promotion; keep generation 4 after the root-47 rollover, rebind the witness to root 47, renew the witness binding, and require replication-quorum churn while preserving tombstone/prior-source continuity; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
