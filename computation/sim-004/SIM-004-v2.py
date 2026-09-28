"""
SIM-004-v2 — Phase Interaction Trajectory formulation (integrated)
===================================================================
Praestology / Process Ontology
Specs: SPEC-009-RELATIONAL-OBSERVATIONAL-ARC
       SPEC-010-PHASE-INTERACTION-TRAJECTORY
       SPEC-011-SCALE-INVARIANT-TRAJECTORY

Summary
-------
α⁻¹ = 1 / (Wr_eq · f_closure)

where:
  Wr_eq     = 3/2          topologically fixed (CWF: Lk=2, Tw=1/2)
  f_closure = f_geom · f_eq  two-factor decomposition

  f_geom = 1/π             analytic — PIT line integral of |[B1,B2]|
                            over t ∈ [0,4π]. No free parameters.

  f_eq   = ξ / R_core      equilibrium correction factor — ratio of
                            healing length to vortex core radius.
                            Emerges from self-consistent GP solve.
                            This is the pivotal open computation.

Structural principles
---------------------
1. Scale invariance (SPEC-011): all parameters derive from Cl(3,0)
   algebra and topological anchors. No free constants.

2. Self-consistency: GP parameters (g, Λ, κ) are shape-functionals
   of the equilibrium (ρ*, B*), not external inputs. They satisfy:
     (g,Λ,κ) → GP solve → (ρ*,B*) → functionals → (g',Λ',κ')
   at the fixed point: (g,Λ,κ) = (g',Λ',κ'). Same structure as
   the depth recursion D_{d+1} = Fix(Φ_d(D_d)).

3. Trajectory interpretation (SPEC-009/010): the apparent S²
   envelope is the dynamical trajectory of B1/B2 interaction —
   analogous to the orbital envelope of a binary star system.
   f_closure is a 1D line integral, not a 2D surface integral.

4. Two-factor structure: f_closure = f_geom · f_eq separates the
   purely topological/algebraic contribution (f_geom = 1/π, exact)
   from the equilibrium shape contribution (f_eq, from GP solve).
   The missing factor ~65.4 must emerge entirely from f_eq.

Topological anchors (no free parameters after SPEC-011)
--------------------------------------------------------
  Tw    = 1/2     algebraic, Möbius half-twist
  Wr_eq = 3/2     CWF invariant (Lk=2, Tw=1/2)
  t ∈ [0,4π]     720° double cover
  f_geom = 1/π   analytic PIT integral (derived below)

Open items
----------
  PIVOT: f_eq = ξ/R_core from GP equilibrium — the only remaining
         unknown. Must give f_eq ≈ 65.4 / (4/3·π) ≈ 15.6 for the
         geometric bare value, or f_eq ≈ 15.6 · (1 - 2.2e-6) for
         CODATA (environmental CCR compression correction).

  See Section E for full diagnostics.

Dependencies: numpy, scipy (solve_bvp, interp1d)
"""

import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings("ignore")

# ── Physical targets ──────────────────────────────────────────────────────────
ALPHA_INV_CODATA      = 137.035999   # measured — lab Π_eff environment
ALPHA_INV_GEOMETRIC   = 137.036304   # CANDIDATE UNDER TEST — expression 4π³+π²+π
                                     # fits numerically but the spherical decomp-
                                     # osition it presupposes (S³/S²/S¹) is NOT
                                     # derived from the closure condition. Rotor
                                     # Haar-measure derivation required before this
                                     # is confirmed. Use as comparison target only.
WR_EQ                 = 3.0 / 2.0   # CWF topological invariant — established

# ── Section A : Möbius centreline and commutator intensity ────────────────────

def mobius_centreline(n_points=4000):
    """
    Scale-invariant Möbius centreline in bivector parameter space.

    Coordinates (b1,b2,b3) are bivector plane activations in Cl(3,0),
    not Cartesian spatial coordinates. No free amplitude parameters.

    Half-twist terms cos(t/2), sin(t/2) are algebraic (Tw=1/2).
    The 0.5 prefactor is the Möbius half-width = r/2, geometric.
    Physical scale emerges from GP closure condition (Section B).

    The apparent S² envelope is the dynamical trajectory of the
    B1/B2 interaction — not a physical surface (SPEC-009/010).
    """
    t    = np.linspace(0.0, 4.0 * np.pi, n_points, endpoint=False)
    b1   = (1.0 + 0.5 * np.cos(t / 2)) * np.cos(t)
    b2   = (1.0 + 0.5 * np.cos(t / 2)) * np.sin(t)
    b3   = 0.5 * np.sin(t / 2)
    norm = np.sqrt(b1**2 + b2**2 + b3**2)
    return b1/norm, b2/norm, b3/norm, t


def bivector_commutator_norm(t):
    """
    |[B1(t), B2(t)]| along the 720° Möbius trajectory.

    In Cl(3,0): [B1,B2] = 2sin(θ)·B3 where θ(t) = t/2
    (half-twist per full cycle — algebraic from Tw=1/2).

    |[B1,B2](t)| = 2|sin(t/2)| — but the 2 cancels in the
    normalisation by 4π, so the normalised integrand is |sin(t/2)|.

    Analytic integral:
      ∫_0^{4π} |sin(t/2)| dt = 4   (two half-periods, each = 2)
      f_geom = 4 / (4π) = 1/π      exact, no numerical error
    """
    return np.abs(np.sin(t / 2.0))


def compute_f_geom(n_points=8000):
    """
    f_geom = (1/4π) ∫_0^{4π} |[B1,B2](t)| dt = 1/π (analytic).

    Numerical integration provided as verification only.
    The analytic value is used in all subsequent computations.
    """
    t          = np.linspace(0.0, 4.0 * np.pi, n_points, endpoint=False)
    dt         = t[1] - t[0]
    f_numerical = np.sum(bivector_commutator_norm(t)) * dt / (4.0 * np.pi)
    f_analytic  = 1.0 / np.pi
    return f_numerical, f_analytic


def compute_writhe_numerical(b1, b2, b3, subsample=150):
    """
    Gauss double integral writhe — numerical check against Wr_eq=3/2.
    """
    n    = len(b1)
    step = max(1, n // subsample)
    xs, ys, zs = b1[::step], b2[::step], b3[::step]
    m    = len(xs)
    dx   = np.gradient(xs)
    dy   = np.gradient(ys)
    dz   = np.gradient(zs)
    wr   = 0.0
    for i in range(m):
        for j in range(i + 2, m):
            r  = np.array([xs[i]-xs[j], ys[i]-ys[j], zs[i]-zs[j]])
            rn = np.linalg.norm(r)
            if rn < 1e-10:
                continue
            t1 = np.array([dx[i], dy[i], dz[i]])
            t2 = np.array([dx[j], dy[j], dz[j]])
            wr += np.dot(np.cross(t1, t2), r) / rn**3
    return wr / (2.0 * np.pi) * (m / n)**2


# ── Section B : Self-consistent GP solve ─────────────────────────────────────

def gp_radial_solve(g_val, kappa_val, n_points=500, r_max=12.0):
    """
    Dimensionless saturating GP for vortex core, winding m=1.

    Equation (radial, in bivector parameter space):
      ψ'' + (1/r)ψ' - (1/r²)ψ + g·ψ·ln(1 + κ·ψ²) - μ·ψ = 0

    μ = g·ln(1 + κ) — self-consistent from background condition.

    The radial coordinate r is the Cl(3,0) norm deviation from the
    centreline: r = |‖B‖ - 1|. Dimensionless — physical Compton
    scale emerges from closure condition ω_z = μ = mc/ħ (not input).

    Boundary conditions:
      ψ(r→0) → r^m   (regularity, m=1 winding)
      ψ(r_max) = 1   (asymptotic normalisation)

    Returns: interpolated ψ(r) function, success flag
    """
    mu = g_val * np.log(1.0 + kappa_val)
    r  = np.linspace(1e-4, r_max, n_points)

    def ode(r, y):
        psi, dp = y
        psi = np.maximum(psi, 1e-12)
        d2p = (-(1.0 / r) * dp
               + (1.0 / r**2) * psi
               - g_val * psi * np.log(1.0 + kappa_val * psi**2)
               + mu * psi)
        return [dp, d2p]

    def bc(ya, yb):
        return [ya[0], yb[0] - 1.0]

    y0  = np.vstack([np.tanh(r), 1.0 / np.cosh(r)**2])
    sol = solve_bvp(ode, bc, r, y0, tol=1e-8, max_nodes=6000)

    if sol.success:
        return interp1d(sol.x, sol.y[0],
                        fill_value=(0.0, 1.0), bounds_error=False), True
    else:
        return interp1d(r, np.tanh(r),
                        fill_value=(0.0, 1.0), bounds_error=False), False


def shape_functionals(psi_fn, r_max=12.0, n_sample=600):
    """
    Extract GP parameters and geometric quantities as shape-functionals
    of the equilibrium density ρ*(r) = ψ*(r)².

    All quantities are derived from the equilibrium shape — not input.
    This implements the self-consistency condition:
      (g,Λ,κ) → GP solve → (ρ*,B*) → functionals → (g',Λ',κ')

    Functional forms:
      n_sat  = max(ρ*)           peak vortex core density
      κ      = 1/n_sat           saturation sharpness (κ·n_sat = 1 at core)
      g      = 1.0               held at unit (dimensionless reference)
      Λ      = g·ln(1+κ·n_sat)  energy scale at saturation transition
      ξ      = 1/√(2·g·n_sat)   healing length at saturation
      R_core = r at max(dρ*/dr)  vortex core radius (steepest density gradient)
      f_eq   = ξ / R_core        equilibrium correction factor

    f_eq is the quantity that, multiplied by f_geom=1/π, gives f_closure.
    Target: f_eq ≈ 65.4 for α⁻¹ ≈ 137 (see Section E diagnostics).
    """
    r     = np.linspace(1e-4, r_max, n_sample)
    psi   = psi_fn(r)
    rho   = psi**2

    n_sat  = float(np.max(rho))
    kappa  = 1.0 / max(n_sat, 1e-10)
    g      = 1.0
    Lambda = g * np.log(1.0 + kappa * n_sat)
    xi     = 1.0 / np.sqrt(max(2.0 * g * n_sat, 1e-12))

    # Vortex core radius: r at steepest density gradient
    drho   = np.abs(np.gradient(rho, r))
    R_core = float(r[np.argmax(drho)])
    R_core = max(R_core, 1e-6)

    # Equilibrium correction factor
    f_eq   = xi / R_core

    return {
        "g":      g,
        "kappa":  kappa,
        "Lambda": Lambda,
        "n_sat":  n_sat,
        "xi":     xi,
        "R_core": R_core,
        "f_eq":   f_eq,
    }


def self_consistent_solve(max_iter=30, tol=1e-6, verbose=True):
    """
    Self-consistent GP iteration: shape → parameters → shape.

    Same fixed-point structure as the depth recursion:
      D_{d+1} = Fix(Φ_d(D_d))
    Here: (g,Λ,κ) = Fix(shape_functionals(GP_solve(g,Λ,κ)))

    Damped update (α=0.5) for stability.
    g held at 1.0 (dimensionless reference unit — CCR¹=1 condition).
    Only κ iterated; Λ and ξ/R_core follow from κ and ρ*.
    """
    kappa = 1.0   # initial guess
    g     = 1.0

    if verbose:
        print("\n[B] Self-consistent GP parameter loop")
        print(f"    {'iter':>4}  {'κ':>12}  {'n_sat':>10}  "
              f"{'ξ':>10}  {'R_core':>10}  {'f_eq':>10}  {'GP':>8}")

    psi_fn  = None
    params  = None

    for i in range(max_iter):
        psi_fn, ok = gp_radial_solve(g, kappa)
        params     = shape_functionals(psi_fn)
        kappa_new  = params["kappa"]

        if verbose:
            status = "ok" if ok else "fallback"
            print(f"    {i+1:>4}  {kappa:>12.6f}  "
                  f"{params['n_sat']:>10.6f}  "
                  f"{params['xi']:>10.6f}  "
                  f"{params['R_core']:>10.6f}  "
                  f"{params['f_eq']:>10.6f}  "
                  f"{status:>8}")

        if abs(kappa_new - kappa) < tol:
            if verbose:
                print(f"    Converged at iteration {i+1}")
            break

        kappa = 0.5 * kappa + 0.5 * kappa_new   # damped update

    return psi_fn, params


# ── Section C : f_closure = f_geom · f_eq ────────────────────────────────────

def compute_f_closure(f_geom, f_eq):
    """
    f_closure = f_geom · f_eq

    f_geom = 1/π   (analytic PIT integral — Section A)
    f_eq   = ξ/R_core (equilibrium correction — Section B)

    The two-factor decomposition separates:
      - purely topological/algebraic contribution (f_geom)
      - equilibrium shape contribution (f_eq)

    α⁻¹ = 1 / (Wr_eq · f_geom · f_eq)
         = π / (1.5 · f_eq)⁻¹    [if f_geom = 1/π]
         → 137 requires f_eq ≈ 65.4 (see Section E)
    """
    return f_geom * f_eq


# ── Section D : Assembly ──────────────────────────────────────────────────────

def assemble(wr_eq, f_closure, params, f_geom, f_eq, verbose=True):
    alpha_inv      = 1.0 / (wr_eq * f_closure) if f_closure > 0 else float('inf')
    alpha_wave_inv = np.pi / wr_eq   # pre-R5 wave limit: f_eq → 1

    if verbose:
        print("\n[D] Assembly — two-stage structure")
        print()
        print(f"    Stage 1 — Wave / EM field regime (pre-R5 closure):")
        print(f"      f_geom = 1/π = {f_geom:.8f}")
        print(f"      Characterises the commutator interaction of bivector")
        print(f"      planes B1/B2 before any R5 firing — the wave-like,")
        print(f"      field-effective state of an indeterminate vector.")
        print(f"      Correlates with: 4π solid-angle normalisation in")
        print(f"      classical EM (Coulomb: e²/4πε₀r, radiation over 4π sr).")
        print(f"      ε₀ encodes vacuum Π_eff; 4π is the isotropic wave spread.")
        print(f"      α_wave⁻¹ = π / Wr_eq = {alpha_wave_inv:.6f}  (pre-closure limit)")
        print()
        print(f"    Stage 2 — Closure / committed vortex (post-R5):")
        print(f"      f_eq = ξ/R_core = {f_eq:.8f}")
        print(f"      Zeno-locking compresses R_core relative to healing")
        print(f"      length ξ. The committed vortex occupies a fraction")
        print(f"      f_eq of the wave-spread field volume.")
        print(f"      Closure correction factor: {1.0/f_eq:.4f}  (≈ 65.4 at target)")
        print()
        print(f"    Full result:")
        print(f"      α⁻¹ = π / (Wr_eq · f_eq)")
        print(f"          = 1 / (Wr_eq · f_geom · f_eq)")
        print(f"          = 1 / ({wr_eq} × {f_geom:.8f} × {f_eq:.8f})")
        print(f"          = {alpha_inv:.6f}")
        print()
        print(f"    Physical reading:")
        print(f"      α⁻¹ ≈ 2 (wave picture) × 65.4 (closure correction)")
        print(f"      The factor ~65.4 = 1/f_eq is the ratio of wave-spread")
        print(f"      field volume to committed vortex core volume.")
        print(f"      This is why α appears in both classical EM and QED —")
        print(f"      it is the same quantity seen from opposite sides of R5.")
        print()
        print(f"    Targets:")
        print(f"      Geometric bare : {ALPHA_INV_GEOMETRIC:.6f}  (no environment)")
        print(f"      CODATA         : {ALPHA_INV_CODATA:.6f}  (lab Π_eff depletion)")
        print(f"      Environmental Δ: {ALPHA_INV_GEOMETRIC - ALPHA_INV_CODATA:.6f}  "
              f"({(ALPHA_INV_GEOMETRIC-ALPHA_INV_CODATA)/ALPHA_INV_CODATA*1e6:.2f} ppm"
              f" — 3rd-body CCR compression, HYPOTHESIS)")
        dev = (alpha_inv - ALPHA_INV_GEOMETRIC) / ALPHA_INV_GEOMETRIC * 100
        print(f"      Current result : {alpha_inv:.6f}  ({dev:+.4f}% from geometric)")

    return alpha_inv, alpha_wave_inv


# ── Section E : Diagnostics ───────────────────────────────────────────────────

def diagnostics(f_geom, f_eq, params):
    """
    Full diagnostic output. Maps the gap between current f_eq
    and the target f_eq needed for α⁻¹ ≈ 137.
    """
    print("\n[E] Diagnostics")

    # Target f_eq values
    f_eq_for_geom = 1.0 / (WR_EQ * f_geom * ALPHA_INV_GEOMETRIC)
    f_eq_for_meas = 1.0 / (WR_EQ * f_geom * ALPHA_INV_CODATA)

    print(f"\n    f_geom = 1/π = {f_geom:.8f}  (analytic, exact)")
    print(f"    f_eq (current GP)       = {f_eq:.6f}")
    print(f"    f_eq needed (geometric) = {f_eq_for_geom:.6f}")
    print(f"    f_eq needed (CODATA)    = {f_eq_for_meas:.6f}")
    print(f"    Ratio (needed/current)  = {f_eq_for_geom/f_eq:.4f}")

    print(f"\n    Converged GP parameters:")
    for k, v in params.items():
        print(f"      {k:>8} = {v:.8f}")

    print(f"\n    CCR⁰ fingerprint check:")
    phi     = (1.0 + np.sqrt(5.0)) / 2.0
    ccr0    = 1.0 / phi   # φ⁻¹
    f_from_ccr0 = ccr0 / WR_EQ
    print(f"      CCR⁰ = φ⁻¹ = {ccr0:.8f}")
    print(f"      If CCR⁰→f_closure link holds:")
    print(f"        f_closure = CCR⁰/Wr_eq = {f_from_ccr0:.8f}")
    print(f"        α⁻¹ = {1/(WR_EQ * f_from_ccr0):.4f}  (≠ 137 — cascade splits)")
    print(f"      f_geom × f_eq (current) = {f_geom * f_eq:.8f}")
    print(f"      → CCR⁰ link is NOT the α⁻¹ path;")
    print(f"        α⁻¹ and I_rot are parallel outputs of D₁ geometry")

    # Analytic π-series target — CANDIDATE, wrong derivation direction if spherical
    f_eq_analytic = 2.0 / (3.0 * (4.0*np.pi**2 + np.pi + 1.0))
    print(f"\n    π-series candidate target (CANDIDATE — epistemic status from")
    print(f"    pi-structure-status.yaml §1-§2):")
    print(f"      Expression: α⁻¹ = 4π³+π²+π = {4*np.pi**3+np.pi**2+np.pi:.8f}")
    print(f"      Numerically matches ALPHA_INV_GEOMETRIC but the spherical")
    print(f"      decomposition (S³/S²/S¹) presupposed is NOT derived from")
    print(f"      the closure condition. Note: unit S³ volume = 2π², not 4π³;")
    print(f"      unit S² area = 4π, not π². Coefficients require non-unit")
    print(f"      radii with no geometric justification.")
    print(f"      Correct direction: derive rotor Haar measure from 720°")
    print(f"      closure condition → integrate → extract π-structure.")
    print(f"      Haar measure on SU(2): dμ = (1/2π²)sin²(θ/2)sin(φ)dθdφdψ")
    print(f"      with θ ∈ [0,4π] (720° restriction) + Möbius framing filter.")
    print(f"      If α⁻¹ candidate is correct:")
    print(f"        f_eq = 2/(3(4π²+π+1)) = {f_eq_analytic:.8f}")
    print(f"      Ratio (current f_eq / candidate): {f_eq/f_eq_analytic:.6f}")
    print(f"      (= 1.0 would support candidate — not confirm it;")
    print(f"       confirmation requires the Haar measure derivation)")
    print()
    print(f"    Two-stage EM interpretation (established):")
    print(f"      Stage 1 pre-R5 (wave): α_wave⁻¹ = π/Wr_eq = {np.pi/1.5:.4f}")
    print(f"        f_geom = 1/π is topologically established (PIT integral)")
    print(f"      Stage 2 closure:       factor = 1/f_eq = {1.0/f_eq:.4f}")
    print(f"        f_eq from Zeno solve — Haar measure derivation gives exact form")
    print(f"      α⁻¹ = π/(Wr_eq · f_eq) = {np.pi/(1.5*f_eq):.4f}")
    print()
    print(f"    OPEN (priority 1): rotor-measure-from-closure-condition")
    print(f"      Derive Haar measure restricted by 720° + Möbius framing.")
    print(f"      This is the prerequisite for deriving f_eq from first principles.")
    print(f"    Current ξ/R_core = {params['xi']:.6f}  (Zeno solve result)")
    print(f"\n    Environmental correction (geometric candidate → CODATA):")
    env_gap = (ALPHA_INV_GEOMETRIC - ALPHA_INV_CODATA) / ALPHA_INV_GEOMETRIC
    print(f"      Δα⁻¹/α⁻¹ = {env_gap:.2e}  "
          f"(2.2 ppm — 3rd-body CCR compression, HYPOTHESIS)")


# ── Main ──────────────────────────────────────────────────────────────────────

def run():
    print("=" * 64)
    print("SIM-004-v2 — Phase Interaction Trajectory (integrated)")
    print("=" * 64)
    print(f"\n  Wr_eq = {WR_EQ}  (CWF: Lk=2, Tw=1/2 — topologically fixed)")

    # A: centreline and f_geom
    print("\n[A] Möbius centreline + commutator integral")
    b1, b2, b3, t = mobius_centreline(4000)
    wr_num         = compute_writhe_numerical(b1, b2, b3)
    f_num, f_geom  = compute_f_geom()
    print(f"    Wr numerical (Gauss) = {wr_num:.4f}  "
          f"(target {WR_EQ:.4f})")
    print(f"    f_geom numerical     = {f_num:.8f}")
    print(f"    f_geom analytic      = 1/π = {f_geom:.8f}  ← used")

    # B: self-consistent GP
    psi_fn, params = self_consistent_solve(verbose=True)

    print(f"\n    Converged parameters:")
    for k, v in params.items():
        print(f"      {k:>8} = {v:.8f}")

    # C: f_closure
    f_eq      = params["f_eq"]
    f_closure = compute_f_closure(f_geom, f_eq)
    print(f"\n[C] f_closure = f_geom · f_eq")
    print(f"    = {f_geom:.8f} × {f_eq:.6f}")
    print(f"    = {f_closure:.8f}")

    # D: α⁻¹
    alpha_inv, alpha_wave_inv = assemble(WR_EQ, f_closure, params,
                                         f_geom, f_eq, verbose=True)

    # E: diagnostics
    diagnostics(f_geom, f_eq, params)

    print("\n" + "=" * 64)
    return {
        "alpha_inv": alpha_inv,
        "f_geom":    f_geom,
        "f_eq":      f_eq,
        "f_closure": f_closure,
        "wr_eq":     WR_EQ,
        "params":    params,
    }


if __name__ == "__main__":
    result = run()
