# WinLoop V219 validation report

## Verified result

V219 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-170 GC to 17,604,905,472 states with 12,574,932,480 bound seventy-first-source handoffs, 7,544,959,488 bound seventy-first-source bindings, and 2,514,986,496 bound verifier completions; admits 1,288,077,880,320 publication states with 117,097,989,120 fully bound one-hundred-forty-fourth-cold-restart recoveries; and admits 22,075,159,120 membership states with 15,767,970,800 bound root-74 witness rebinds, 9,460,782,480 bound witness renewals, and 3,153,594,160 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `bdd9099d31d841569264ab616de4002c3f62c8d73bee3a2c18871af0c8715ac1`.

## Predecessor binding

V219 continues from committed V218 on `main`: V218 digest `cf01c740ed5953098e5203e235fc3e9c1d4b4b45572900a030930011ea00e2f6`, implementation SHA-256 `db3babd9d8463385103551f5aa33cf16d59b04eb3a4ab3274f3ec75faf34868f`, validator SHA-256 `e4573d933feffeca31350849931302b2f246c4c6ff51b65835a07a2a57f8a2cb`. V219 implementation SHA-256 is `1bbf385305e0ae766d00f589acc46aa18c50b88779f7620f2332101f98a4e1d0` and standalone validator SHA-256 is `607924467b423dd66adbcc49e30e626d4d0000c10b81c56ddff6afc812462d0a`.

Seed transitions are exact from V218: 576 epoch-169 completions (`2,464,519,680 / 4,278,680`), 27,648 restart recoveries (`114,724,435,968 / 4,149,466`), and 760 quorum-churn completions (`3,089,236,600 / 4,064,785`).

## Continuation gates

Epoch 170 hands the rebound proof to a seventy-first source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 144 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-fourth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 74 after the root-74 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v219_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V220

Keep independence fail closed absent a committed external verifier artifact; rotate the seventy-first-source lineage in epoch 171, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-144 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-fifth cold restart without cached-authority promotion; replace the witness source after the root-74 witness rebind, roll to root 75, bind root 75, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
