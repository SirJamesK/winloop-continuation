# WinLoop V218 validation report

## Verified result

V218 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-169 GC to 22,180,677,120 states with 17,251,637,760 bound seventieth-lineage rotations, 12,322,598,400 bound lineage bindings, 7,393,559,040 bound handed-proof rebinds, and 2,464,519,680 bound verifier completions; admits 1,261,968,795,648 publication states with 114,724,435,968 fully bound one-hundred-forty-third-cold-restart recoveries; and admits 33,981,602,600 membership states with 27,803,129,400 bound witness-source replacements, 15,446,183,000 bound root-74 rollovers, 9,267,709,800 bound root-74 bindings, and 3,089,236,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `cf01c740ed5953098e5203e235fc3e9c1d4b4b45572900a030930011ea00e2f6`.

## Predecessor binding

V218 continues from committed V217 on `main`: V217 digest `5ffe5d638e87cce710b96b9da77f92110cdc014beaabaf30d3fae1ff02a6980d`, implementation SHA-256 `46b21bfad0f7b8e243d077dd28ea35dd7c1d8d8c01d4d1267a40fd214f6bbf48`, validator SHA-256 `ba45de8b298038d8a327d7b5719787376eb30cea7a5ebae7ab06590df77567f3`. V218 implementation SHA-256 is `db3babd9d8463385103551f5aa33cf16d59b04eb3a4ab3274f3ec75faf34868f` and standalone validator SHA-256 is `e4573d933feffeca31350849931302b2f246c4c6ff51b65835a07a2a57f8a2cb`.

Seed transitions are exact from V217: 576 epoch-168 completions (`2,414,732,544 / 4,192,244`), 27,648 restart recoveries (`112,383,175,680 / 4,064,785`), and 760 quorum-churn completions (`3,025,760,640 / 3,981,264`).

## Continuation gates

Epoch 169 rotates the seventieth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 143 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-third cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-73 witness rebind, rolls to root 74, binds root 74, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v218_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V219

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventy-first source in epoch 170, bind that source, and preserve the epoch-12 deadline; compose publication-143 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-forty-fourth cold restart without cached-authority promotion; rebind the witness to root 74 after the root-74 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
