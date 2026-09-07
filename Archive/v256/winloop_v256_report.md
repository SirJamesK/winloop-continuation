# WinLoop V256 validation report

## Verified result

V256 keeps cross-role credit at 12 with no committed external independence certificate, extends epoch-207 GC to 44,119,676,160 states with 34,315,303,680 bound eighty-ninth-lineage rotations, 24,510,931,200 bound lineage bindings, 14,706,558,720 bound handed-proof rebinds, and 4,902,186,240 bound verifier completions; admits 2,526,070,136,832 publication states with 229,642,739,712 fully bound one-hundred-eighty-first-cold-restart recoveries; and admits 68,311,691,800 membership states with 55,891,384,200 bound witness-source replacements, 31,050,769,000 bound root-93 rollovers, 18,630,461,400 bound root-93 bindings, and 6,210,153,800 bound quorum-churn completions, with zero modeled bad acceptances across all three continuation gates.

Validation digest: `897d379f4dace02b4c69586e1ce71e57cb7b4347cdaf6cfe301f32ae2a1c5984`.

## Predecessor binding

V256 continues from committed V255 on `main`: V255 digest `8717cbfa612546507e3c852f4d7056fce635371a285abde3e20054b35c7f1f48`, implementation SHA-256 `9642c46e6f7794281c50af8ea0d3ab6c316826748f4db6ced9b9783551124777`, validator SHA-256 `c6635ded0965e7f27c929ca22844ffe1eab4ee99aced26da33d1fc0b6376aff7`. V256 implementation SHA-256 is `029224b548bfd0c25d907a85b52d8b25d0409043c48269c9bc64fbf5a0394ca1`.

Seed transitions are exact from V255: 576 epoch-207 seeds (`4,823,331,840 / 8,373,840`), 27,648 restart recoveries (`225,918,858,240 / 8,171,255`), and 760 quorum-churn completions (`6,108,902,800 / 8,038,030`).

## Continuation gates

Epoch 207 rotates the eighty-ninth-source lineage, binds that lineage, rebinds the handed proof, and completes verifier binding while preserving the epoch-12 deadline; modeled stale, conflicting, continuity, carried-proof, root, and deadline-reset mutations fail closed.

Publication 181 composes replacement-source churn, successor-source binding, fresh reconciliation, and a one-hundred-eighty-first cold verifier restart; cached-authority promotion remains rejected.

Membership generation 4 remains bound after the root-92 witness rebind, replaces the witness source, rolls to root 93, binds root 93, and requires replication-quorum churn while preserving tombstone and prior-source continuity; stale-root, weak-replication, wrong-witness, prior-source-discontinuity, and active-Byzantine mutations fail closed.

## Preserved bounds

V21 guarded routing remains active. Admission remains joint cut 21, provenance cut 22, synthetic lower cost 63. Cross-role credit stays 12 because no committed external independence certificate exists. Temporal bounds remain horizon 22/floor 1/budget 851 and horizon 11/floor 2/budget 398. Checkpoint recovery remains 513 statements, max lag 64, frontier-only storage, unchanged trust-bearing paths, and shared-audit accounting `132 + 4*k`.

## Validation

`winloop_v256_validate.py` regenerates the result, checks exact predecessor arithmetic, gate counts, fail-closed mutations, preserved invariants, and every SHA-256 manifest entry. JSON is manifest-hashed in canonical compact form.

## Unresolved frontier for V257

Keep independence fail closed absent a committed external verifier artifact; hand the rebound proof to a ninetieth source in epoch 208, bind that source, and preserve the epoch-12 deadline; compose publication-181 recovery with successor-source disappearance, replacement-source binding, fresh reconciliation, and a one-hundred-eighty-second cold restart without cached-authority promotion; keep generation 4 after the root-93 rollover, rebind the witness to root 93, renew the witness binding, and require replication-quorum churn; retain V21 guarded routing until a replacement clears the >=2,000-seed bar with honest message accounting.
