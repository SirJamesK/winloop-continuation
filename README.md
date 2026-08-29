# WinLoop Continuation

GitHub is the canonical source of truth for the WinLoop continuation project.

## Repository structure

- `Archive/vNN/` — immutable, versioned WinLoop artifacts. The highest numeric `vNN` is the current completed version.
- `AGENT.md` — scheduler bootstrap and hard invariants.
- `SCHEDULED_TASK_PROMPT.md` — canonical recurring technical/operational contract.
- `GITHUB_POLICY.md` — repository, branch, persistence, and publication policy.
- `CHATGPT_PROJECT_SETUP.md` — ChatGPT-side organizational notes.

The current historical baseline is `Archive/v42/`. Each successful scheduled run should create exactly one next version directory (`v43`, `v44`, …), validate it, and commit it directly to `main`.

## Persistence

WinLoop artifacts are stored in this repository, not in ChatGPT Library/conversation files. Temporary execution scratch may be used only for validation and is not durable state.

## Branch policy

Scheduled continuation uses only the repository default branch (`main`). No feature/release branches or pull requests are used for scheduled WinLoop work.

## Scheduled output

The full result lives under `Archive/vNN/`. ChatGPT scheduled output is intentionally concise: version, verified headline result, commit SHA/blocker, and archive path.
