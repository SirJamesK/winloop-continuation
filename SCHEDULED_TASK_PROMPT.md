# WinLoop Continuation — Scheduled Agent Contract

This file is the canonical recurring-agent contract for `SirJamesK/winloop-continuation`.

## Repository and branch invariants

- Repository: **only** `SirJamesK/winloop-continuation`.
- Branch: write directly only to the repository default branch when it is `main` or `master`; current canonical branch is `main`.
- Never create feature/release branches or pull requests for scheduled continuation work.
- Never write WinLoop artifacts to any other repository.
- GitHub is the durable source of truth.
- Do **not** persist generated WinLoop artifacts to ChatGPT Library, conversation files, or any ChatGPT file folder. Transient execution scratch may be used only when required to validate code and must not be treated as durable state.

## Versioned repository structure

- Historical/versioned artifacts live under `Archive/vNN/`.
- Determine the current version by listing `Archive/` and selecting the highest valid numeric `vNN` directory.
- Fetch and inspect the latest version's implementation, validation JSON, report, standalone validator, and SHA-256 manifest from that directory.
- Produce exactly one next version: `v(NN+1)`.
- Write the complete validated next-version artifact set under `Archive/v(NN+1)/`.
- Never overwrite or mutate an earlier `Archive/vNN/` version except to repair a demonstrably corrupt/incomplete commit, and report such a repair explicitly.
- Keep root project-control files (`AGENT.md`, `SCHEDULED_TASK_PROMPT.md`, `GITHUB_POLICY.md`, `README.md`) current when the operating contract changes. Do not duplicate large runtime artifacts at repository root.

## Architecture contract carried from V42

Preserve these constraints unless a later committed version contains a stronger, explicitly validated replacement:

- The carried V13 endpoint theorem is a baseline only; do not claim to re-prove it without a fresh independent certificate.
- V21 guarded routing remains the active routing baseline unless a replacement independently clears its acceptance bar.
- Admission requires all of:
  - joint false-WIN cut >= 21;
  - synthetic lower cost >= 60;
  - every non-endpoint false-WIN route cut >= 22.
- V42's accepted deep/common privileged fabric requires independent fabric-local/current authorization and rejects provenance cut 21.
- Temporal modeling uses verifier-visible stolen-authorization lifetime as the operative security variable.
- Recursive evidence fails closed on unknown, stale, conflicting, cyclic, or insufficient dependencies.
- Merkle frontier/root persistence is a storage optimization only and must not alter authority, quorum, publication, monitor/gossip, or trust-bearing message paths.
- Shared-audit accounting remains `132 + 4*k` messages per audit epoch unless a stronger design is validated with honest accounting.
- Synthetic 3/4/6 costs are model parameters, not empirical attacker prices.

## Continuation priorities

On each run, continue from the highest committed archive version, not from chat memory. Advance the unresolved technical frontier in that version's report/prompt. For the V42 frontier specifically, recursively decompose the accepted common privileged fabric below current roots: privileged cloud/PAM tenancy, HSM management/custody/issuance/rotation, operator employment/IAM/key custody, provider/build/CA dependencies, and fabric-local possession. Put new prerequisites into the same exact static and temporal OR-of-AND optimizer. Reject any shortcut below the admission contract.

Keep recursively testing common-root collapse, temporal key/authorization reuse, detection/eviction/rotation/revocation publication/verifier consumption, stale authorization, evidence lifetime, churn/freshness, split-log recovery, delayed propagation, and source disappearance. Unknown provenance fails closed.

Keep V21 routing unless a replacement has zero stationary and near-threshold false activations over >=2,000 seeds **and** materially lower gradual/selective/correlated detection delay with no extra probes. Only then claim a new runtime envelope and count every online/shared message class honestly.

Use RFC 9162, RFC 9334, RFC 9711, and RFC 9943 patterns where useful, without claiming that signed metadata proves physical, organizational, hardware, supply-chain, or cloud-control independence.

## Required artifacts per version

Each `Archive/vNN/` must contain at minimum:

- `distributed_winloop_vNN.py`
- `winloop_vNN.json`
- `winloop_vNN_report.md`
- `winloop_vNN_validate.py`
- `winloop_vNN_SHA256SUMS.txt`

Add reproducibility/support files only when they materially improve verification.

## Validation and publication

- Validate the implementation before publishing.
- Re-run the standalone validator against the exact content being committed.
- Ensure the manifest hashes the committed artifact set correctly.
- Commit directly to `main`/`master` only after validation passes.
- After writing, re-read the committed paths or commit metadata to verify publication succeeded.
- If GitHub write access, repository visibility, branch policy, validation, or required evidence fails, **fail closed**: do not fabricate a version or claim publication.

## Scheduled ChatGPT response

Keep the scheduled response concise. Return only:

1. new version number;
2. one-sentence verified headline result;
3. GitHub commit SHA (or exact blocker);
4. repository path such as `Archive/v43/`.

Do not attach or persist the generated files to ChatGPT. Do not paste the full technical report into the scheduled-chat response.

A recurring scheduled task does not have a supported control to force every run into a brand-new top-level ChatGPT conversation. Do not falsely claim that it created a new chat. Use the versioned GitHub archive as the authoritative per-version separation.

Do not claim hidden infrastructure access, unrestricted networking, covert communication, self-modification of model weights/runtime, or capabilities not actually exposed.