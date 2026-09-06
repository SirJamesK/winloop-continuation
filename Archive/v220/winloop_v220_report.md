# WinLoop V220 validation report

## Verified result

V220 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-171 GC to 23,095,238,400 states with 17,962,963,200 bound seventy-first-lineage rotations, 12,830,688,000 bound lineage bindings, 7,698,412,800 bound handed-proof rebinds, and 2,566,137,600 bound verifier completions; admits 1,314,544,619,520 publication states with 119,504,056,320 fully bound one-hundred-forty-fifth-cold-restart recoveries; and admits 35,407,233,400 membership states with 28,969,554,600 bound witness-source replacements, 16,094,197,000 bound root-75 rollovers, 9,656,518,200 bound root-75 bindings, and 3,218,839,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `5a51addc1c5f6efbbe22a502fca579bbccc3c2dce87d9669493b81b06baff4a9`.

## Predecessor binding

V220 continues from committed V219 on `main`: V219 digest `bdd9099d31d841569264ab616de4002c3f62c8d73bee3a2c18871af0c8715ac1`, implementation SHA-256 `1bbf385305e0ae766d00f589acc46aa18c50b88779f7620f2332101f98a4e1d0`, validator SHA-256 `607924467b423dd66adbcc49e30e626d4d0000c10b81c56ddff6afc812462d0a`. V220 implementation SHA-256 is `4f0a5db251997806c847faa8be14d427f8c97d01ae8a1860554ab1b085e5d2f6` and standalone validator SHA-256 is `4e5c6fac5256570353a89d7a7af289c2ce9e1698a2edb0a63b1a6766301406e2`.

Seed transitions are exact from V219: 576 epoch-170 completions (`2,514,986,496 / 4,366,296`), 27,648 restart recoveries (`117,097,989,120 / 4,235,315`), and 760 quorum-churn completions (`3,153,594,160 / 4,149,466`).

## Continuation gates

Epoch 171 rotates the seventy-first-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 145 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-fifth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-74 witness rebind, rolls to root 75, binds root 75, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v220_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V221

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventy-second source in epoch 172, bind that source, and preserve the epoch-12 deadline; compose publication-145 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-sixth cold restart without cached-authority promotion; rebind the witness to root 75 after the root-75 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
