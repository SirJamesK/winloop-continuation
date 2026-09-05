# WinLoop V196 validation report

## Verified result

V196 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-147 GC to 13,662,432,000 states with 10,626,336,000 bound fifty-ninth-lineage rotations, 7,590,240,000 bound lineage bindings, 4,554,144,000 bound handed-proof rebinds, and 1,518,048,000 bound verifier completions; admits 773,131,087,872 publication states with 70,284,644,352 fully bound one-hundred-twenty-first-cold-restart recoveries; and admits 20,742,121,400 membership states with 16,970,826,600 bound witness-source replacements, 9,428,237,000 bound root-63 rollovers, 5,656,942,200 bound root-63 bindings, and 1,885,647,400 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `d8b8c6225c2254ae4ba26b608e8fb79a3ba8e0fda342c32fd90d7ce8254cbd61`.

## Predecessor binding

V196 continues from committed V195 on `main`: V195 digest `da273f02429d022773cca5ecb8c28ed0ea127a309969e092cdb1190736259617`, implementation SHA-256 `67b389a983e1e4f5ee9eb8dd03eff4f63d5e8298c25e5da6c84fa2c5ff74af9e`, validator SHA-256 `bfc46d9c08c2f61e301fad7123f97735ded584e05632cfc2c170e4b583ff4d63`. V196 implementation SHA-256 is `63279d0778a217a030a2974d57635e0010942774625e178e0573f868565a1a32` and standalone validator SHA-256 is `edb1a9fbbe056dc7b37bf0f57868cf23e026420bed5e82e1c52b346f5e699c8c`.

Seed transitions are exact from V195: 576 epoch-146 completions (`1,482,048,000 / 2,573,000`), 27,648 restart recoveries (`68,597,867,520 / 2,481,115`), and 760 quorum-churn completions (`1,840,028,400 / 2,421,090`).

## Continuation gates

Epoch 147 rotates the fifty-ninth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; all modeled stale/conflicting/incomplete/continuity/root/carried-proof/deadline-reset mutations fail closed.

Publication 121 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-twenty-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 replaces the witness source after the root-62 witness rebind, rolls to root 63, binds root 63, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, missing-tombstone, weak-replication, wrong-witness, prior-source discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v196_validate.py` regenerates the result, checks predecessor arithmetic, exact gate counts, fail-closed mutations, preserved invariants, and all SHA-256 manifest entries. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V197

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a sixtieth source in epoch 148, bind that source, and preserve the epoch-12 deadline; compose publication-121 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-twenty-second cold restart without cached-authority promotion; rebind the witness to root 63 after the root-63 rollover, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
