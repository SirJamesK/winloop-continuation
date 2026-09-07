# WinLoop V255 validation report

## Verified result

V255 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-206 GC to 33,763,322,880 states with 24,116,659,200 bound eighty-ninth-source handoffs, 14,469,995,520 bound eighty-ninth-source bindings, and 4,823,331,840 bound verifier completions; admits 2,485,107,440,640 publication states with 225,918,858,240 fully bound one-hundred-eightieth-cold-restart recoveries; and admits 42,762,319,600 membership states with 30,544,514,000 bound root-92 witness rebinds, 18,326,708,400 bound witness renewals, and 6,108,902,800 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `8717cbfa612546507e3c852f4d7056fce635371a285abde3e20054b35c7f1f48`.

## Predecessor binding

V255 continues from committed V254 on `main`: V254 digest `c7492aa24a00bed66cbb17ae8018b0a29f1c7da7d16628ac42d9841615373e4e`, implementation SHA-256 `cec47071c42e0f3452b61c1fb5565c68d1010bedc89c4eb66e9130b9b7596497`, validator SHA-256 `b8e6c6c5defea89a9e0b746241a7ad20aa36dd8b7edb744811db118b576f645e`. V255 implementation SHA-256 is `9642c46e6f7794281c50af8ea0d3ab6c316826748f4db6ced9b9783551124777`.

Seed transitions are exact from V254: 576 epoch-206 seeds (`4,745,327,616 / 8,238,416`), 27,648 restart recoveries (`222,235,453,440 / 8,038,030`), and 760 quorum-churn completions (`6,008,758,360 / 7,906,261`).

## Continuation gates

Epoch 206 hands the rebound proof to an eighty-ninth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 180 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-eightieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-92 rollover, rebinds the witness to root 92, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v255_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V256

Keep independence fail closed absent a committed external verifier artifact; rotate the eighty-ninth-source lineage in epoch 207, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-180 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-first cold restart without cached-authority promotion; keep generation 4 after the root-92 witness rebind, replace the witness source, roll to root 93, bind root 93, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
