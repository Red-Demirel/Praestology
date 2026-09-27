"""
discrete_zeno_core.py
=====================
Praestology / Process Ontology
Spec: ccr-zeno-core-reframing.yaml (v1.0, corrected)
      ccr-zeno-as-initial-closure.yaml (§2-§3)

Replaces gp_radial_solve() in sim004_v2_integrated.py with a discrete
Cl(3,0) rotor phase-step iteration that implements the Zeno-locking
mechanism and computes:

  R_core  — rate-matching boundary (f_R5 = f_rotor)
  ξ       — healing length in high-Π_eff space
  f_eq    — ξ / R_core  (the missing factor; target ≈ 65.4)

Zeno retention (per firing cycle):
  φ⁻¹ of open phase space retained  (λ₂ eigenvalue of D₋₁ recurrence)
  φ⁻² committed to η per firing

This encodes the CCR⁰ = φ⁻¹ imprint from the D₋₁ → D₀ transition
into the D₀ → D₁ equilibrium shape. The √5-in-f_closure fingerprint
is the testable consequence.

Direction correction (ccr-zeno-as-initial-closure §3):
  R_core is NOT compressed by a force. It is the radial boundary where
  f_R5(r) = f_rotor(r). No directional language — R_core is a locking
  boundary, not a squeezed boundary.

Usage:
  from discrete_zeno_core import zeno_core_solve, compute_f_eq
  result = zeno_core_solve()
  # result['f_eq'] replaces params['f_eq'] in sim004_v2_integrated.py

Dependencies: numpy only (no scipy BVP required)
"""

import numpy as np

# ── Constants ─────────────────────────────────────────────────────────────────

PHI       = (1.0 + np.sqrt(5.0)) / 2.0   # golden ratio
PHI_INV   = 1.0 / PHI                     # φ⁻¹ — Zeno retention factor
PHI_INV_SQ = PHI_INV ** 2                 # φ⁻² — committed fraction per firing
SQRT5     = np.sqrt(5.0)

# Π_eff parameters
PI_0      = 1.0    # maximum free potential (normalised)
GAMMA     = 1.0    # coupling: how much η depletes Π_eff

# Viability threshold
W_0       = 1.0    # density weight in V(ψ)
W_1       = 1.0    # gradient weight in V(ψ)
V_C       = 0.5    # commitment threshold

# Lattice
N_RADIAL  = 1000   # radial lattice points
R_MAX     = 20.0   # outer boundary (high-Π_eff free-propagation zone)
N_STEPS   = 5000   # discrete phase iteration steps


# ── Lattice setup ─────────────────────────────────────────────────────────────

def setup_lattice(n=N_RADIAL, r_max=R_MAX):
    """
    1D radial lattice in bivector parameter space.
    r is the Cl(3,0) norm deviation from the Möbius centreline.
    Dimensionless — physical Compton scale emerges at closure.
    """
    r  = np.linspace(1e-3, r_max, n)
    dr = r[1] - r[0]
    return r, dr


# ── Initial rotor configuration ───────────────────────────────────────────────

def initial_psi(r):
    """
    Initial ψ(r): smooth Möbius vortex seed.
    m=1 winding: ψ ∝ r near origin (regularity), → 1 asymptotically.
    """
    return np.tanh(r)


# ── Discrete phase step ───────────────────────────────────────────────────────

def rotor_phase_step(psi, r, dr, Pi_eff):
    """
    Advance ψ by one discrete Cl(3,0) rotor phase step.

    R_{n+1} = R_n · exp(½ B Δθ(Π_eff))

    In the radial amplitude representation:
      Δψ = -½ (m²/r²)ψ·dr + Π_eff · ∇²ψ · dr

    The Laplacian ∇² in radial coordinates (m=1 winding):
      ∇²ψ = d²ψ/dr² + (1/r)dψ/dr - (1/r²)ψ

    The step size is proportional to local Π_eff — slows as η builds.
    """
    # Second derivative (central differences, interior)
    d2psi       = np.zeros_like(psi)
    d2psi[1:-1] = (psi[2:] - 2*psi[1:-1] + psi[:-2]) / dr**2

    # First derivative
    dpsi        = np.zeros_like(psi)
    dpsi[1:-1]  = (psi[2:] - psi[:-2]) / (2 * dr)

    # Radial Laplacian (m=1 winding)
    laplacian   = d2psi + (1.0 / r) * dpsi - (1.0 / r**2) * psi

    # Phase step scaled by local Π_eff
    delta_psi   = Pi_eff * laplacian * dr

    psi_new     = psi + delta_psi

    # Enforce boundary conditions
    psi_new[0]  = 0.0    # regularity at origin
    psi_new[-1] = 1.0    # asymptotic normalisation

    return psi_new


# ── Viability measure ─────────────────────────────────────────────────────────

def viability(psi, r, dr):
    """
    V(ψ) = w₀|ψ|² + w₁|∇ψ|²

    High gradient regions (vortex core) have large V — R5 fires
    frequently there, producing Zeno lock.
    """
    dpsi        = np.zeros_like(psi)
    dpsi[1:-1]  = (psi[2:] - psi[:-2]) / (2 * dr)

    return W_0 * psi**2 + W_1 * dpsi**2


# ── R5 firing and Zeno retention ─────────────────────────────────────────────

def apply_r5_zeno(psi, eta, V, r, dr, step):
    """
    Apply R5 firing events where V(ψ) ≥ V_c.

    Direction correction (ccr-zeno-as-initial-closure §3):
      R5 does NOT reset the rotor. It commits the current phase step
      to η and prevents further free rotation at that site this step.
      The rotor orientation is KEPT — not returned to prior state.

    Zeno retention per firing cycle (ccr-zeno-as-initial-closure §2):
      φ⁻¹ of open amplitude retained
      φ⁻² committed to η

    The alternating sign of λ₂ = -φ⁻¹ is applied at alternating steps:
      even steps: retention factor = +φ⁻¹
      odd steps:  retention factor = -φ⁻¹
    Net retention per two-step cycle = φ⁻¹ (magnitude).

    Returns:
      psi_out : updated field amplitude
      eta_out : updated committed density
      fired   : boolean mask of R5 firing sites
    """
    fired   = V >= V_C
    psi_out = psi.copy()
    eta_out = eta.copy()

    if np.any(fired):
        # Alternating sign from λ₂ = -φ⁻¹
        sign = +1.0 if (step % 2 == 0) else -1.0

        # Retained open amplitude at firing sites
        psi_out[fired] = psi[fired] * (sign * PHI_INV)

        # Committed fraction added to η
        eta_out[fired] += psi[fired]**2 * PHI_INV_SQ

        # Π_eff will be recomputed from updated η in main loop

    return psi_out, eta_out, fired


# ── Rate-matching boundary ────────────────────────────────────────────────────

def rate_matching_radius(f_R5_history, f_rotor_history, r):
    """
    R_core = radius where f_R5(r) = f_rotor(r).

    f_R5(r)    = time-averaged R5 firing rate at radius r
                 (fraction of steps where V ≥ V_c at that r)
    f_rotor(r) = time-averaged free phase step rate at radius r
                 (fraction of steps where V < V_c at that r)

    R_core is NOT where the density peaks or the gradient is steepest.
    It is the rate-matching boundary — the locking surface.
    """
    # Smooth both profiles to reduce noise
    f_R5   = np.array(f_R5_history)
    f_rot  = np.array(f_rotor_history)

    # Find crossing: f_R5 > f_rotor inside core, < outside
    diff   = f_R5 - f_rot

    # R_core is where diff crosses zero from positive to negative
    sign_changes = np.where(np.diff(np.sign(diff)))[0]

    if len(sign_changes) > 0:
        idx    = sign_changes[0]
        # Linear interpolation to subgrid precision
        r_core = r[idx] + (r[idx+1] - r[idx]) * (
            -diff[idx] / (diff[idx+1] - diff[idx])
        )
    else:
        # No crossing found — use peak gradient as fallback
        r_core = r[np.argmax(np.abs(np.gradient(f_R5)))]

    return float(r_core)


# ── Healing length ────────────────────────────────────────────────────────────

def healing_length(psi_eq, eta_eq, r, dr):
    """
    ξ — healing length in the high-Π_eff asymptotic zone.

    In the free-propagation zone (r >> R_core), Π_eff ≈ Π_0 and
    the amplitude recovers to its asymptotic value. ξ is the
    characteristic length of this recovery:

      ξ = r at which |1 - ψ(r)| = e⁻¹ · |1 - ψ(R_core)|

    This is purely a property of the outer free-propagation zone —
    no Zeno influence. It sets the outer scale in f_eq = ξ/R_core.
    """
    # Find the asymptotic recovery profile
    # ψ → 1 from below; |1-ψ| decays
    deviation = np.abs(1.0 - psi_eq)

    if deviation.max() < 1e-10:
        return r[-1]  # fully healed everywhere

    # Find the peak deviation (near R_core)
    peak_idx   = np.argmax(deviation)
    peak_dev   = deviation[peak_idx]
    target_dev = peak_dev / np.e

    # Find where deviation drops to 1/e of peak (outer side)
    outer      = deviation[peak_idx:]
    r_outer    = r[peak_idx:]

    crossing   = np.where(outer <= target_dev)[0]
    if len(crossing) > 0:
        xi = float(r_outer[crossing[0]]) - float(r[peak_idx])
    else:
        xi = float(r[-1]) - float(r[peak_idx])

    return max(xi, 1e-6)


# ── Main discrete Zeno core solve ─────────────────────────────────────────────

def zeno_core_solve(n_radial=N_RADIAL, r_max=R_MAX, n_steps=N_STEPS,
                    verbose=True):
    """
    Full discrete Zeno core solve.

    Pipeline per step:
      1. Compute local Π_eff from η
      2. Advance ψ by one discrete rotor phase step (scaled by Π_eff)
      3. Compute viability V(ψ)
      4. Apply R5 Zeno firing where V ≥ V_c (with φ⁻¹ retention)
      5. Accumulate f_R5 and f_rotor firing rate histories
      6. Repeat until convergence

    After convergence:
      - R_core from rate-matching boundary
      - ξ from asymptotic healing profile
      - f_eq = ξ / R_core

    Returns dict with all results and the √5 fingerprint check.
    """
    r, dr    = setup_lattice(n_radial, r_max)
    psi      = initial_psi(r)
    eta      = np.zeros_like(r)

    # Firing rate accumulators
    f_R5_count    = np.zeros_like(r)
    f_rotor_count = np.zeros_like(r)

    # Convergence tracking
    psi_prev       = psi.copy()
    converge_tol   = 1e-8
    converge_count = 0
    converge_req   = 200   # steps stable before declaring convergence

    warmup         = 500   # steps before accumulating rates

    if verbose:
        print("\n[B-Zeno] Discrete CCR-Zeno core solve")
        print(f"  Lattice: {n_radial} points, r ∈ [0, {r_max}]")
        print(f"  φ⁻¹ = {PHI_INV:.8f}  (Zeno retention per firing)")
        print(f"  φ⁻² = {PHI_INV_SQ:.8f}  (committed fraction per firing)")
        print(f"  V_c = {V_C}  (commitment threshold)")
        print(f"  Running {n_steps} steps...")

    for step in range(n_steps):

        # Step 1: local Π_eff
        Pi_eff = np.maximum(PI_0 - GAMMA * eta, 1e-6)

        # Step 2: discrete rotor phase step
        psi_new = rotor_phase_step(psi, r, dr, Pi_eff)

        # Step 3: viability
        V = viability(psi_new, r, dr)

        # Step 4: R5 Zeno firing with φ⁻¹ retention
        psi_new, eta, fired = apply_r5_zeno(psi_new, eta, V, r, dr, step)

        # Step 5: accumulate firing rates (after warmup)
        if step >= warmup:
            f_R5_count    += fired.astype(float)
            f_rotor_count += (~fired).astype(float)

        # Convergence check
        delta = np.max(np.abs(psi_new - psi_prev))
        if delta < converge_tol:
            converge_count += 1
            if converge_count >= converge_req:
                if verbose:
                    print(f"  Converged at step {step} (δ={delta:.2e})")
                break
        else:
            converge_count = 0

        psi_prev = psi.copy()
        psi      = psi_new

    else:
        if verbose:
            print(f"  Warning: did not converge in {n_steps} steps")

    # Normalise firing rate histories
    total_accum = max(step - warmup + 1, 1)
    f_R5_rate   = f_R5_count    / total_accum
    f_rotor_rate= f_rotor_count / total_accum

    # R_core: rate-matching boundary
    R_core = rate_matching_radius(f_R5_rate, f_rotor_rate, r)

    # ξ: healing length
    xi     = healing_length(psi, eta, r, dr)

    # f_eq
    f_eq   = xi / max(R_core, 1e-6)

    # Converged Π_eff profile
    Pi_eq  = np.maximum(PI_0 - GAMMA * eta, 1e-6)

    if verbose:
        print(f"\n  Converged results:")
        print(f"    R_core (rate-matching) = {R_core:.6f}")
        print(f"    ξ      (healing length) = {xi:.6f}")
        print(f"    f_eq   = ξ/R_core      = {f_eq:.6f}")
        print(f"    Π_eff at r=0           = {Pi_eq[0]:.6f}")
        print(f"    Π_eff at r=R_core      = {np.interp(R_core, r, Pi_eq):.6f}")
        print(f"    η peak                 = {eta.max():.6f}")

    return {
        "r":             r,
        "psi_eq":        psi,
        "eta_eq":        eta,
        "Pi_eff_eq":     Pi_eq,
        "f_R5_rate":     f_R5_rate,
        "f_rotor_rate":  f_rotor_rate,
        "R_core":        R_core,
        "xi":            xi,
        "f_eq":          f_eq,
        "phi_inv":       PHI_INV,
        "phi_inv_sq":    PHI_INV_SQ,
    }


# ── √5 fingerprint check ──────────────────────────────────────────────────────

def sqrt5_fingerprint(f_eq, f_geom=1.0/np.pi, wr_eq=1.5):
    """
    Check whether f_closure = f_geom · f_eq carries √5 content,
    and whether it matches the analytic π-series target.

    Target hierarchy (three levels of confidence):

    Level 1 — CODATA (measured, highest confidence):
      α⁻¹_CODATA = 137.035999
      Includes environmental CCR compression (~2.2 ppm 3rd-body effect).

    Level 2 — Geometric bare (high confidence):
      α⁻¹_geometric = 4π³ + π² + π ≈ 137.036304
      Candidate for the purely topological value — electron + photon only,
      no external committed topology. Gap to CODATA is the environmental
      Π_eff depletion in the measurement context.

    Level 3 — Analytic f_eq target (HYPOTHESIS — epistemically flagged):
      Observation: α⁻¹_geometric / π = 4π² + π + 1
      If α⁻¹ = π / (Wr_eq · f_eq) and f_geom = 1/π, then:
        f_eq = 1 / (Wr_eq · (α⁻¹/π))
             = 1 / (Wr_eq · (4π² + π + 1))
             = 2 / (3(4π² + π + 1))
      This would mean f_eq is a pure π-expression with no free parameters,
      and the successive powers of π (π⁴ → π³ → π² → π → 1) correspond
      to successive integrations in the phase-space integral — consistent
      with the framework's iterative depth structure.

      EPISTEMIC STATUS: HYPOTHESIS — the logic is internally consistent
      with the iterative structure but the derivation is not yet closed.
      The formula 4π³ + π² + π itself has no confirmed derivation from
      first principles within the framework. This target is a falsifiable
      prediction: if the Zeno solve converges to f_eq ≈ 2/(3(4π²+π+1)),
      it confirms both the Zeno mechanism and the π-series structure.
      If it does not, one or both are wrong.

    √5 content:
      Prediction from ccr-zeno-as-initial-closure: the Zeno retention
      factor φ⁻¹ = (√5-1)/2 should leave a √5 fingerprint in f_eq.
      Test: whether f_eq / √5, f_eq / φ, f_eq / φ² are near-rational.
    """
    f_closure = f_geom * f_eq
    alpha_inv = 1.0 / (wr_eq * f_closure)

    ALPHA_INV_CODATA    = 137.035999
    ALPHA_INV_GEOMETRIC = 137.036304

    # Level 3: analytic π-series target (HYPOTHESIS)
    f_eq_analytic = 2.0 / (3.0 * (4.0*np.pi**2 + np.pi + 1.0))
    alpha_from_analytic = 1.0 / (wr_eq * f_geom * f_eq_analytic)
    # Verify: should equal 4π³ + π² + π
    alpha_check = 4*np.pi**3 + np.pi**2 + np.pi

    # √5 content
    ratio_sqrt5 = f_eq / SQRT5
    ratio_phi   = f_eq / PHI
    ratio_phi2  = f_eq / PHI**2

    # Required f_eq for each target
    f_eq_needed_geom = 1.0 / (wr_eq * f_geom * ALPHA_INV_GEOMETRIC)
    f_eq_needed_meas = 1.0 / (wr_eq * f_geom * ALPHA_INV_CODATA)

    print("\n[Fingerprint checks]")
    print(f"  f_geom            = 1/π = {f_geom:.8f}")
    print(f"  f_eq (Zeno)       = {f_eq:.8f}")
    print(f"  f_closure         = {f_closure:.8f}")
    print(f"  α⁻¹               = {alpha_inv:.6f}")
    print()
    print(f"  Targets:")
    print(f"    CODATA measured : {ALPHA_INV_CODATA:.6f}  "
          f"(gap: {alpha_inv - ALPHA_INV_CODATA:+.4f})")
    print(f"    Geometric bare  : {ALPHA_INV_GEOMETRIC:.6f}  "
          f"(gap: {alpha_inv - ALPHA_INV_GEOMETRIC:+.4f})")
    print(f"    Environmental Δ : {ALPHA_INV_GEOMETRIC - ALPHA_INV_CODATA:.6f}  "
          f"({(ALPHA_INV_GEOMETRIC-ALPHA_INV_CODATA)/ALPHA_INV_CODATA*1e6:.2f} ppm"
          f" — 3rd-body CCR compression, HYPOTHESIS)")
    print()

    print(f"  Analytic π-series target (HYPOTHESIS — not yet derived):")
    print(f"    α⁻¹_geometric = 4π³+π²+π = {alpha_check:.8f}")
    print(f"    α⁻¹/π        = 4π²+π+1  = {alpha_check/np.pi:.8f}")
    print(f"    f_eq_analytic = 2/(3(4π²+π+1)) = {f_eq_analytic:.8f}")
    print(f"    Verification  : α⁻¹ from f_eq_analytic = {alpha_from_analytic:.6f}  "
          f"(should equal {alpha_check:.6f})")
    print(f"    Δ(f_eq Zeno vs analytic) = {f_eq - f_eq_analytic:+.8f}  "
          f"(ratio: {f_eq/f_eq_analytic:.6f})")
    if abs(f_eq/f_eq_analytic - 1.0) < 0.01:
        print(f"    ✓ Zeno f_eq within 1% of analytic target — hypothesis supported")
    elif abs(f_eq/f_eq_analytic - 1.0) < 0.10:
        print(f"    ~ Zeno f_eq within 10% — check V_c and γ derivation from ℛ(ψ)")
    else:
        print(f"    ✗ Zeno f_eq outside 10% — hypothesis not confirmed by this solve")
    print()

    print(f"  Required f_eq values:")
    print(f"    For geometric : {f_eq_needed_geom:.8f}")
    print(f"    For CODATA    : {f_eq_needed_meas:.8f}")
    print(f"    Analytic pred : {f_eq_analytic:.8f}")
    print(f"    Consistency   : analytic vs geometric needed: "
          f"{abs(f_eq_analytic - f_eq_needed_geom):.2e}  "
          f"({'consistent' if abs(f_eq_analytic/f_eq_needed_geom - 1) < 1e-6 else 'inconsistent'})")
    print()

    print(f"  √5 / φ content (Zeno retention fingerprint):")
    print(f"    f_eq / √5  = {ratio_sqrt5:.8f}  "
          f"({'≈ rational' if abs(ratio_sqrt5 - round(ratio_sqrt5)) < 0.01 else 'irrational'})")
    print(f"    f_eq / φ   = {ratio_phi:.8f}  "
          f"({'≈ rational' if abs(ratio_phi - round(ratio_phi)) < 0.01 else 'irrational'})")
    print(f"    f_eq / φ²  = {ratio_phi2:.8f}  "
          f"({'≈ rational' if abs(ratio_phi2 - round(ratio_phi2)) < 0.01 else 'irrational'})")
    print(f"    f_eq_analytic / √5 = {f_eq_analytic/SQRT5:.8f}")
    print(f"    f_eq_analytic / φ  = {f_eq_analytic/PHI:.8f}")
    print(f"    (If √5 fingerprint present, one ratio should be near-rational)")

    return {
        "f_closure":            f_closure,
        "alpha_inv":            alpha_inv,
        "f_eq_analytic":        f_eq_analytic,
        "alpha_from_analytic":  alpha_from_analytic,
        "ratio_sqrt5":          ratio_sqrt5,
        "ratio_phi":            ratio_phi,
        "ratio_phi2":           ratio_phi2,
        "f_eq_needed_geom":     f_eq_needed_geom,
        "f_eq_needed_meas":     f_eq_needed_meas,
        "hypothesis_supported": abs(f_eq/f_eq_analytic - 1.0) < 0.01,
    }


# ── Entry point ───────────────────────────────────────────────────────────────

def run(verbose=True):
    print("=" * 64)
    print("discrete_zeno_core.py")
    print("Zeno-modulated discrete CCR core solve")
    print("=" * 64)

    result  = zeno_core_solve(verbose=verbose)
    fp      = sqrt5_fingerprint(result["f_eq"])

    print("\n[Summary — two-stage structure]")
    print()
    print(f"  Stage 1 (wave / EM field, pre-R5):")
    print(f"    f_geom = 1/π = {1.0/np.pi:.8f}  (analytic, exact)")
    print(f"    Corresponds to EM field — 4π solid-angle wave spread")
    print(f"    α_wave⁻¹ = π/Wr_eq = {np.pi/1.5:.6f}  (pre-closure limit)")
    print(f"    This is why α appears in classical EM and QED —")
    print(f"    same quantity, opposite sides of R5.")
    print()
    print(f"  Stage 2 (committed vortex, post-R5 Zeno-locked):")
    print(f"    R_core = {result['R_core']:.6f}  (rate-matching boundary)")
    print(f"    ξ      = {result['xi']:.6f}  (healing length)")
    print(f"    f_eq   = {result['f_eq']:.6f}  (ξ/R_core)")
    print(f"    Closure correction: 1/f_eq = {1.0/result['f_eq']:.4f}  (target ≈ 65.4)")
    print()
    print(f"  Full: α⁻¹ = π/(Wr_eq · f_eq) = {fp['alpha_inv']:.6f}")
    print(f"    Geometric target : 137.036304")
    print(f"    CODATA target    : 137.035999")
    print(f"    Gap to geometric : {fp['alpha_inv'] - 137.036304:+.4f}")
    print()

    # Analytic π-series check
    f_eq_analytic = 2.0 / (3.0 * (4.0*np.pi**2 + np.pi + 1.0))
    print(f"  Analytic target f_eq = 2/(3(4π²+π+1)) = {f_eq_analytic:.8f}  [HYPOTHESIS]")
    print(f"  Ratio (Zeno/analytic) = {result['f_eq']/f_eq_analytic:.6f}  (1.0 = confirmed)")
    print()

    if abs(fp['alpha_inv'] - 137.036304) < 1.0:
        print("  ✓ Within 1 unit of geometric target")
    elif abs(fp['alpha_inv'] - 137.036304) < 10.0:
        print("  ~ Within order-of-magnitude — check V_c and γ derivation from ℛ(ψ)")
    else:
        print("  ✗ Outside range — Zeno parameters need derivation from ℛ(ψ)")
        print("    Open: r5-firing-rate-from-master-equation")

    print("=" * 64)
    return result, fp


if __name__ == "__main__":
    run()
