# WinLoop V224 validation report

## Verified result

V224 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-175 GC to 24,999,093,504 states with 19,443,739,392 bound seventy-third-lineage rotations, 13,888,385,280 bound lineage bindings, 8,333,031,168 bound handed-proof rebinds, and 2,777,677,056 bound verifier completions; admits 1,424,036,782,080 publication states with 129,457,889,280 fully bound one-hundred-forty-ninth-cold-restart recoveries; and admits 38,377,006,360 membership states with 31,399,368,840 bound witness-source replacements, 17,444,093,800 bound root-77 rollovers, 10,466,456,280 bound root-77 bindings, and 3,488,818,760 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `65da90f1923d812e3a7d8da6404b1dc45c3fdc65c4acf5c9287ae6116b682770`.

## Predecessor binding

V224 continues from committed V223 on `main`: V223 digest `62d96c27f3c96895071e075642c995453acc0829eaf6d17eb07d97cea65fa9e9`, implementation SHA-256 `22c5292be717e06cee099860f6c616cd603944006087335b954dd898ba80d106`, validator SHA-256 `12b8a9a148f343ea31aaf4c9fd96b29d6d645bfe1902289a1e5a9938022e5482`. V224 implementation SHA-256 is `e6e84a7e9cca3c64a933c2cc68e37efd63eadb4d1cc274a37028f9287880db03` and standalone validator SHA-256 is `281dac678467c56da42e7fdeb9fd16c52a17603521fc8e407a1192e30a50639b`.

Seed transitions are exact from V223: 576 epoch-174 completions (`2,723,742,720 / 4,728,720`), 27,648 restart recoveries (`126,919,554,048 / 4,590,551`), and 760 quorum-churn completions (`3,419,962,000 / 4,499,950`).

## Continuation gates

Epoch 175 rotates the seventy-third-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 149 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-forty-ninth cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-76 witness rebind, rolls to root 77, binds root 77, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness-source, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v224_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V225

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a seventy-fourth source in epoch 176, bind that source, and preserve the epoch-12 deadline; compose publication-149 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-fiftieth cold restart without cached-authority promotion; rebind the witness to root 77 after the root-77 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
