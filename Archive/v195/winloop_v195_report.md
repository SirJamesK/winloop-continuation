# WinLoop V195 validation report

## Verified result

V195 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-146 GC to 10,374,336,000 states with 7,410,240,000 bound fifty-ninth-source handoffs, 4,446,144,000 bound fifty-ninth-source bindings, and 1,482,048,000 bound verifier completions; admits 754,576,542,720 publication states with 68,597,867,520 fully bound one-hundred-twentieth-cold-restart recoveries; and admits 12,880,198,800 membership states with 9,200,142,000 bound root-62 witness rebinds, 5,520,085,200 bound witness renewals, and 1,840,028,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `da273f02429d022773cca5ecb8c28ed0ea127a309969e092cdb1190736259617`.

## Predecessor binding

V195 continues from committed V194 on `main`: V194 digest `f10a0d3e935a0e68efd38997e26eb14be519f1d0d13ff5e269eda11eee7cd042`, implementation SHA-256 `24405395df930ba9ea77f88fe7f0b93c1a4dfefb2b9cc1027f419cb49ffa1020`, validator SHA-256 `d9f5f6d7dd034e7419d17ed03e3c0d2f9a6cc8df01428b81925038c724f1978e`. V195 implementation SHA-256 is `67b389a983e1e4f5ee9eb8dd03eff4f63d5e8298c25e5da6c84fa2c5ff74af9e` and standalone validator SHA-256 is `bfc46d9c08c2f61e301fad7123f97735ded584e05632cfc2c170e4b583ff4d63`.

Seed transitions are exact from V194: 576 epoch-145 completions (`1,446,621,696 / 2,511,496`), 27,648 restart recoveries (`66,938,296,320 / 2,421,090`), and 760 quorum-churn completions (`1,795,151,160 / 2,362,041`).

## Continuation gates

Epoch 146 hands the rebound proof to the fifty-ninth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 120 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-twentieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 62 after the root-62 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v195_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V196

Keep independence fail closed absent a committed external verifier artifact; rotate the fifty-ninth-source lineage in epoch 147, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-120 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-twenty-first cold restart without cached-authority promotion; keep generation 4 after the root-62 witness rebind, replace the witness source, roll to root 63, bind root 63, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
