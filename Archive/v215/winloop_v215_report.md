# WinLoop V215 validation report

## Verified result

V215 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-166 GC to 16,220,252,160 states with 11,585,894,400 bound sixty-ninth-source handoffs, 6,951,536,640 bound sixty-ninth-source bindings, and 2,317,178,880 bound verifier completions; admits 1,185,763,138,560 publication states with 107,796,648,960 fully bound one-hundred-fortieth-cold-restart recoveries; and admits 20,310,004,400 membership states with 14,507,146,000 bound root-72 witness rebinds, 8,704,287,600 bound witness renewals, and 2,901,429,200 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `b790801c1fff32a8555ea54edd9c7a1bc69a34f4d63b1ddbce5682dc72e260cb`.

## Predecessor binding

V215 continues from committed V214 on `main`: V214 digest `5cead8ef75bda4e6c211afde57c7524cb0061fa33c8384371e6c02d11c0e750a`, implementation SHA-256 `3c5d8052b3cbad363ea8b041c2e274b39fbbcdc7e2a8112f80930dfbbb21c972`, validator SHA-256 `7144558a01c908a559dfea6941dcb2cdf8266e6fcd50d81f73bbb69842fb845e`. V215 implementation SHA-256 is `b175b40f185ee83650a29815e6269241bcaf83da744a1b7a71e36d4c28432a9e` and standalone validator SHA-256 is `2e3987611a14d864d7b099ed4bbaac6373ee543c210a092319f0aff80b46ba8f`.

Seed transitions are exact from V214: 576 epoch-165 completions (`2,269,403,136 / 3,939,936`), 27,648 restart recoveries (`105,550,940,160 / 3,817,670`), and 760 quorum-churn completions (`2,840,561,560 / 3,737,581`).

## Continuation gates

Epoch 166 hands the rebound proof to a sixty-ninth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 140 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-fortieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 72 after the root-72 rollover, renews that witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v215_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V216

Keep independence fail closed absent a committed external verifier artifact; rotate the sixty-ninth-source lineage in epoch 167, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-140 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-first cold restart without cached-authority promotion; replace the witness source after the root-72 witness rebind, roll to root 73, bind root 73, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
