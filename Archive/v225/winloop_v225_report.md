# WinLoop V225 validation report

## Verified result

V225 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-176 GC to 19,826,231,040 states with 14,161,593,600 bound seventy-fourth-source handoffs, 8,496,956,160 bound seventy-fourth-source bindings, and 2,832,318,720 bound verifier completions; admits 1,452,328,289,280 publication states with 132,029,844,480 fully bound one-hundred-fiftieth-cold-restart recoveries; and admits 24,910,155,200 membership states with 17,792,968,000 bound root-77 witness rebinds, 10,675,780,800 bound witness renewals, and 3,558,593,600 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `35d53f4b0c77714b37b84dec8d148cbeb9fc8f27ee587dcfd1b458f1f97e56eb`.

## Predecessor binding

V225 continues from committed V224 on `main`: V224 digest `65da90f1923d812e3a7d8da6404b1dc45c3fdc65c4acf5c9287ae6116b682770`, implementation SHA-256 `e6e84a7e9cca3c64a933c2cc68e37efd63eadb4d1cc274a37028f9287880db03`, validator SHA-256 `281dac678467c56da42e7fdeb9fd16c52a17603521fc8e407a1192e30a50639b`. V225 implementation SHA-256 is `a0713101dd488665b6a7f6d90413a6066084a2512198ef822db6cb76e69f1daf` and standalone validator SHA-256 is `ad9be40b61c2b517af1aff2831194caf3f372ebb8ef3db461e2e3b988262eca4`.

Seed transitions are exact from V224: 576 epoch-175 completions (`2,777,677,056 / 4,822,356`), 27,648 restart recoveries (`129,457,889,280 / 4,682,360`), and 760 quorum-churn completions (`3,488,818,760 / 4,590,551`).

## Continuation gates

Epoch 176 hands the rebound proof to a seventy-fourth source, binds that source, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 150 composes successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-fiftieth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 rebinds the witness to root 77 after the root-77 rollover, renews the witness binding, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v225_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V226

Keep independence fail closed absent a committed external verifier artifact; rotate the seventy-fourth-source lineage in epoch 177, bind that lineage, rebind the handed proof, and preserve the epoch-12 deadline; compose publication-150 recovery with replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-fifty-first cold restart without cached-authority promotion; replace the witness source after the root-77 witness rebind, roll to root 78, bind root 78, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
