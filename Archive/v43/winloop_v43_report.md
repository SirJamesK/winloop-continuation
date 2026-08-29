# WinLoop Continuation — V43

**Status:** validated recursive-provenance advancement from the committed V42 reconstruction. V43 does not re-prove the carried V13 endpoint theorem and does not replace the V21 guarded router.

## Verified advancement

V43 removes the opaque treatment of the accepted V42 common privileged fabric and expands it recursively into explicit AND prerequisites for privileged cloud/PAM tenancy, HSM management/custody/issuance/rotation, operator employment/IAM/key custody, provider/build/CA control, ceremony-local control, and independent fabric-local possession. Shared primitive roots are deduplicated by the exact OR-of-AND optimizer rather than double-counted as independent authorities.

The recursively expanded common privileged fabric contains **11 unique primitive roots**. Combined with the 11 fixed non-endpoint provenance anchors, the exact minimum non-endpoint false-WIN route is **22 roots**. The downstream PAM-plane and issuance/ceremony alternatives are **23 roots** each. The carried endpoint route remains **21 roots**, giving **joint cut 21 / provenance cut 22 / synthetic lower joint cost 63 — PASS**.

## Deep common-root collapse tests

The baseline recursive decomposition is admitted at provenance cut 22. Each tested hidden-collapse scenario consumes the entire one-root provenance margin and reduces the minimum non-endpoint route to **21 — REJECT**:

- fabric-local possession removed;
- HSM-management authority collapsed into the shared cloud/PAM identity fabric;
- operator employment/IAM collapsed into the shared cloud/PAM identity fabric;
- provider/build/CA control collapsed into the shared cloud/PAM identity fabric;
- HSM issuance/rotation-local control collapsed into HSM-management authority;
- CA ceremony-local control collapsed into build-local control.

This is the central V43 result: the accepted recursively decomposed common-fabric route has **zero hidden static slack** beyond the required provenance cut 22. Independence at these deep roots is therefore admission-critical rather than cosmetic metadata.

## Exact temporal optimizer

V43 replaces case-only temporal constants with an exact nested-window peak optimizer. A root with verifier-visible authorization lifetime `d` may be acquired in any of the final `d` epochs and remain usable at the target epoch. For nested suffix windows, the exact minimum peak compromises per epoch is:

`max_k ceil(N(lifetime <= k) / k)`.

The optimizer reproduces the carried V42 cardinalities and maps them onto explicit deep roots:

- strict lifetimes: **joint 21 / provenance 22**;
- all-root two-epoch reuse: **joint 11 / provenance 11**;
- all-root three-epoch reuse: **joint 7 / provenance 8**;
- only `cloud_pam_identity_fabric` usable one extra epoch: **provenance 21** (final margin consumed);
- four deep authority roots usable for two epochs (`cloud_pam_identity_fabric`, `hsm_management_authority`, `operator_employment_iam`, `provider_build_ca_control`): **joint/provenance peak 18**, provenance wins;
- verifier-effective revocation before the next epoch restores **joint 21 / provenance 22**.

Thus the temporal attack surface is governed by verifier-visible authorization lifetime at the recursively decomposed roots, not merely by nominal key rotation.

## Fail-closed recursive graph checks

The capability expander rejects dependency cycles and unknown non-primitive capability references. Unknown or cyclic provenance is not silently reclassified as an independent primitive root.

## Preserved contracts

- Carried V13 endpoint cut: **21**, baseline only; no fresh re-proof claimed.
- Admission: joint cut >= 21, synthetic lower cost >= 60, every non-endpoint route >= 22.
- Active routing: carried **V21 guarded router**; no new routing envelope claimed.
- Synthetic costs **3/4/6** remain model parameters, not empirical attacker prices.
- Merkle frontier/root persistence remains storage-only; carried shared-audit accounting remains **132 + 4*k messages/epoch**.

## V44 frontier

Bind every recursively expanded primitive root to explicit issuer/quorum/log/freshness evidence and re-run churn, split-log, delayed-propagation, and source-loss validation. Decompose verifier-visible lifetime into theft/exportability, detection, eviction, rotation, revocation publication, verifier consumption, stale authorization, and ceremony-validity stages. Continue searching for second-order common-control roots below cloud/PAM, HSM management, provider/build/CA, and operator employment/IAM; absent independence evidence fails closed.

## Reproducibility

Run in this directory:

```bash
python distributed_winloop_v43.py > /tmp/v43.json
python winloop_v43_validate.py
```

The standalone validator verifies the committed JSON result and SHA-256 manifest against the implementation and report.
