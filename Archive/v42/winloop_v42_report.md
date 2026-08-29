# WinLoop Continuation — V42

**Status:** reconstructed from the preserved latest V42 scheduled-task contract. The original V42 sandbox attachments were not present in the current Library/file surface, so these are regenerated continuation artifacts, not byte-identical recovery.

## Latest accepted state

- Carried endpoint baseline: **21 roots** (V13 theorem, not re-proved here).
- Integrated admission: joint cut >= 21, synthetic lower cost >= 60, every non-endpoint route >= 22.
- Deep hardened V42: **joint 21 / provenance 22 — PASS**.
- Common privileged fabric without final fabric-local possession: **joint 21 / provenance 21 — REJECT**.
- Four-root common privileged core surviving two epochs: **joint/provenance peak 18 — provenance wins**.
- Shared audit accounting: **132 + 4*k messages per audit epoch**.
- Active routing baseline remains the carried **V21 guarded router**.

## V42 direction

The next step is to recursively decompose the accepted four-root common privileged fabric into privileged cloud/PAM tenancy, HSM management/custody/issuance/rotation, operator IAM/key custody, provider/build/CA dependencies, and independent fabric-local possession. Any shortcut below joint 21, lower-cost 60, or non-endpoint 22 must fail admission.

## Reproducibility

Run:

```bash
python distributed_winloop_v42.py
python winloop_v42_validate.py
```

The JSON artifact preserves the full V42 continuation contract used to regenerate this package.
