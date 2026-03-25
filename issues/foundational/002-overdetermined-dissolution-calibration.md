# F02 — Overdetermined Dissolution Calibration Test (Priority 1)

**Status:** Open — Deliberate falsification gate  
**Priority:** 1 (blocks alpha computation and sextuple convergence closure)  
**Date:** 25 March 2026  
**Related files:**  
- `domains/physics/commitment-response-function.yaml`  
- `domains/physics/core-dynamical-equation.yaml`  
- `domains/physics/vortex-stabilization.yaml` (for topological_fatigue factor)

## Description

The dual R(Ψ) now contains an explicit dissolution kernel:

\[
R(\Psi) = \frac{g |\Psi|^2}{1 + \frac{|\Psi|^2}{n_{\rm sat}}} - \varepsilon \frac{|\Psi|^2}{1 + \tau_{\rm diss} |\Psi|^2} \cdot f(\nabla R, \text{topological\_fatigue})
\]

This kernel is constrained by **three independent empirical anchors** using only **two free parameters** (ε, τ_diss):

1. **Proton lifetime** > 10³⁴ years (topologically protected state — dissolution must be strongly suppressed).  
2. **¹⁴C half-life** ≈ 5730 years (weakly protected nuclear state — dissolution rate must match observation).  
3. **Cosmological renewal timescale** ~10–100 Gyr (void + black-hole processing must return sufficient potential to Praegress to prevent stasis while preserving Cs6 habitable-planet threshold).

## Purpose

This is an **intentional overdetermined test**.  
If no consistent solution exists in (ε, τ_diss) space that simultaneously satisfies all three constraints while preserving proton/electron stability and the sextuple constant convergence, the dissolution kernel form itself requires structural revision.  
Non-existence of solution is **not** a failure of the data or the core rules — it is a signal that the kernel must be refined (e.g., by making f(topological_fatigue) depend on additional invariants from vortex-stabilization.yaml or by splitting topological vs. non-topological channels).

## Acceptance criteria for closure

- A solution region is found that satisfies all three constraints within current experimental bounds, **or**  
- The kernel is revised (new functional form proposed and shown to be derivable from R1–R5) and the test is re-run successfully.

## Linked open derivations (from core-dynamical-equation.yaml)

- Derive explicit f(∇R, topological_fatigue) from vortex winding numbers.  
- Calibrate ε and τ_diss while preserving α computation pathway.  
- Verify consistency with black-hole processor dynamics and void accelerated leakage.

## Relation to core

This test operates entirely at the physics-domain instantiation level.  
R1–R5 remain invariant. The test protects the framework against hidden tuning and enforces the parsimony required by the formal constraint schema (S_k generated from S_{k-1}).

---

**This is issue #2 in /issues/foundational/**  
(After F01_axiom_circularity)

Ready to commit.
