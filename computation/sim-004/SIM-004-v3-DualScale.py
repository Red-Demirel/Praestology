"""
SIM-004-v3-DualScale-Corrected
Dual-aspect closure architecture for α⁻¹ derivation.

CORRECTIONS APPLIED:
1. Envelope solver now explicitly receives and returns kappa, using mu = g*ln(1+kappa).
2. Operative solver velocity is now normalized to the 720° topological invariant 
   (total phase accumulation = 4π), resolving the arbitrary Jacobi parameter reference.
3. Shape-functional coupling between k and kappa is explicitly flagged as a heuristic 
   placeholder pending the full GP equilibrium derivation.
"""
import numpy as np
from scipy.special import ellipk
from scipy.integrate import solve_bvp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings("ignore")

# ── Constants ────────────────────────────────────────────────────────────────
WR_EQ              = 1.5
ALPHA_INV_GEOMETRIC = 137.036304   # 4π³ + π² + π
ALPHA_INV_CODATA    = 137.035999

# ── Section A: Operative solver (RCR / Jacobi-elliptic) ─────────────────────
def jacobi_sn_cn_dn(u, k, n=200):
    """Jacobi elliptic functions sn(u,k), cn(u,k), dn(u,k) via AGM."""
    if k < 1e-10:
        return np.sin(u), np.cos(u), np.ones_like(u)
    if k > 1.0 - 1e-10:
        tanhu = np.tanh(u)
        sechu = 1.0 / np.cosh(u)
        return tanhu, sechu, sechu
    
    a = np.ones(n+1)
    b = np.zeros(n+1)
    c = np.zeros(n+1)
    a[0] = 1.0
    b[0] = np.sqrt(1.0 - k*k)
    c[0] = k
    for i in range(n):
        a[i+1] = 0.5*(a[i] + b[i])
        b[i+1] = np.sqrt(a[i]*b[i])
        c[i+1] = 0.5*(a[i] - b[i])
        if abs(c[i+1]) < 1e-15:
            n = i+1
            break
            
    phi = (2**n) * a[n] * u
    for i in range(n, 0, -1):
        phi = 0.5*(phi + np.arcsin(c[i]*np.sin(phi)/a[i]))
        
    sn = np.sin(phi)
    cn = np.cos(phi)
    dn = np.sqrt(1.0 - k*k * sn**2)
    return sn, cn, dn

def operative_solver(k, n_points=2000):
    """
    Operative aspect: Jacobi-elliptic Dzhanibekov trajectory in Cl(3,0).
    CORRECTION: Velocity is now normalized to the 720° topological invariant.
    Total phase accumulation over the cycle is forced to exactly 4π.
    """
    K   = ellipk(k**2)
    period_720 = 4.0 * K          # one complete 720° cycle
    t = np.linspace(0.0, period_720, n_points, endpoint=False)
    dt = t[1] - t[0]
    
    sn, cn, dn = jacobi_sn_cn_dn(t, k)
    
    # Bivector trajectory
    b1 = sn * cn
    b2 = dn
    b3 = sn
    
    # Normalise to unit bivector sphere
    norm = np.sqrt(b1**2 + b2**2 + b3**2)
    norm = np.where(norm < 1e-12, 1e-12, norm)
    b1n, b2n, b3n = b1/norm, b2/norm, b3/norm
    
    # Unnormalized bivector phase velocity ||dB/dt||
    db1 = np.gradient(b1n, dt)
    db2 = np.gradient(b2n, dt)
    db3 = np.gradient(b3n, dt)
    omega_unnorm = np.sqrt(db1**2 + db2**2 + db3**2)
    
    # CORRECTION: Normalize velocity so total phase = 4π (720° double cover)
    total_phase = np.sum(omega_unnorm) * dt
    omega = omega_unnorm * (4.0 * np.pi / total_phase)
    
    # Barrier: maximum normalized omega (at the saddle-point flip)
    omega_flip = float(np.max(omega))
    
    # RCR: flip vs dwell ratio (using normalized omega)
    median_om = np.median(omega)
    flip_mask = omega > median_om
    dwell_mask = ~flip_mask
    mean_flip  = float(np.mean(omega[flip_mask]))  if flip_mask.any()  else omega_flip
    mean_dwell = float(np.mean(omega[dwell_mask])) if dwell_mask.any() else 1e-6
    RCR = mean_flip / max(mean_dwell, 1e-10)
    
    # f_geom: velocity-weighted sn² integral (using normalized omega)
    sn2 = sn**2
    numerator   = np.sum(omega * sn2) * dt
    denominator = np.sum(sn2) * dt
    f_geom = numerator / max(denominator, 1e-12)
    
    return omega_flip, RCR, f_geom, period_720

# ── Section B: Envelope solver (CCR / GP radial) ────────────────────────────

def envelope_solver(omega_flip, kappa, g=1.0, r_max=12.0, n_nodes=500):
    """
    Envelope aspect: GP radial profile with Ω_flip² centrifugal barrier.
    CORRECTION: Asymptotic boundary condition ψ_inf is computed from the
    GP equation's equilibrium condition, not hardcoded to 1.
    """
    mu = g * np.log(1.0 + kappa)
    
    # CORRECTION: Compute asymptotic ψ from the GP equilibrium condition
    # At large r: -Ω_flip²·ψ + g·ψ·ln(1+κ·ψ²) - μ·ψ = 0
    # Solving: ψ_inf = sqrt(((1+κ)·exp(Ω_flip²/g) - 1) / κ)
    psi_inf = np.sqrt((np.exp(omega_flip**2 / g) * (1.0 + kappa) - 1.0) / kappa)
    psi_inf = max(psi_inf, 1e-6)  # numerical safety
    
    r = np.linspace(1e-4, r_max, n_nodes)
    
    def ode(r, y):
        psi, dp = y
        psi = np.maximum(psi, 1e-14)
        barrier = (1.0/r**2 + omega_flip**2)
        d2p = (-1.0/r * dp
               + barrier * psi
               - g * psi * np.log(1.0 + kappa * psi**2)
               + mu * psi)
        return [dp, d2p]
    
    def bc(ya, yb):
        # CORRECTION: Outer boundary is ψ_inf, not 1
        return [ya[0], yb[0] - psi_inf]
    
    # Initial guess scaled to ψ_inf
    y0 = np.vstack([psi_inf * np.tanh(r), 
                    psi_inf / np.cosh(r)**2])
    sol = solve_bvp(ode, bc, r, y0, tol=1e-8, max_nodes=5000)
    
    if sol.success:
        psi_fn = interp1d(sol.x, sol.y[0], 
                          fill_value=(0.0, psi_inf), bounds_error=False)
    else:
        psi_fn = interp1d(r, psi_inf * np.tanh(r), 
                          fill_value=(0.0, psi_inf), bounds_error=False)
    
    # Shape functionals from equilibrium profile
    r_dense = np.linspace(1e-4, r_max, 2000)
    psi_vals = psi_fn(r_dense)
    rho_vals = psi_vals**2
    
    n_sat = float(np.max(rho_vals))
    n_sat = max(n_sat, 1e-6)
    
    # kappa_new from the actual asymptotic density
    kappa_new = 1.0 / n_sat
    
    xi = 1.0 / np.sqrt(2.0 * g * n_sat)
    
    # CORRECTION: R_core threshold scaled to ψ_inf
    # Physical meaning: r where density reaches 1/e of asymptotic value
    threshold = psi_inf / np.sqrt(np.e)
    cross = np.where(psi_vals >= threshold)[0]
    R_core = float(r_dense[cross[0]]) if len(cross) > 0 else xi
    R_core = max(R_core, 1e-10)
    
    f_eq = xi / R_core
    
    return f_eq, xi, R_core, n_sat, kappa_new, psi_inf, sol.success

# ── Section C: Self-consistent iteration ────────────────────────────────────
def self_consistent_dual(k_init=0.90, kappa_init=1.0, max_outer=25, max_inner=15,
                         tol_omega=1e-5, tol_kappa=1e-6):
    """
    Mutually coupled iteration.
    CORRECTION: kappa is now explicitly iterated and passed to the envelope solver.
    The k <-> kappa coupling remains a heuristic placeholder pending the full 
    shape-functional derivation from the GP equilibrium.
    """
    k = k_init
    kappa = kappa_init
    omega_flip_prev = None
    
    print(f"\n{'iter':>4}  {'k':>8}  {'Ω_flip':>10}  {'RCR':>8}  {'f_geom':>10}  {'f_eq':>10}  {'κ':>10}  {'GP':>6}")
    
    for outer in range(max_outer):
        # ── Operative solver ──
        omega_flip, RCR, f_geom, period = operative_solver(k)
        
        # ── Envelope solver (inner kappa loop) ──
        kappa_iter = kappa
        for inner in range(max_inner):
            f_eq, xi, R_core, n_sat, kappa_new, gp_ok = envelope_solver(omega_flip, kappa_iter)
            if abs(kappa_new - kappa_iter) < tol_kappa:
                kappa_iter = kappa_new
                break
            kappa_iter = 0.5 * kappa_iter + 0.5 * kappa_new  # damped update
            
        kappa = kappa_iter
        status = "ok" if gp_ok else "fb"
        
        # HEURISTIC PLACEHOLDER: Update k from κ. 
        # Larger κ (sharper saturation) → k closer to 1 (sharper flip).
        # TODO: Replace with actual shape-functional coupling derived from GP equilibrium.
        k_new = np.sqrt(1.0 - np.exp(-2.0 * kappa))
        k_new = np.clip(k_new, 0.01, 0.9999)
        
        alpha_inv = 1.0 / max(WR_EQ * f_geom * f_eq, 1e-12)
        
        print(f"  {outer+1:>3}  {k:>8.5f}  {omega_flip:>10.5f}  {RCR:>8.4f}  {f_geom:>10.6f}  {f_eq:>10.6f}  {kappa:>10.6f}  {status:>6}   α⁻¹={alpha_inv:.4f}")
        
        # Convergence check
        if omega_flip_prev is not None:
            if abs(omega_flip - omega_flip_prev) < tol_omega and abs(k_new - k) < tol_omega:
                print(f"\n  Converged at iteration {outer+1}")
                break
                
        omega_flip_prev = omega_flip
        k = 0.7 * k + 0.3 * k_new   # damped update
        
    return k, kappa, omega_flip, RCR, f_geom, f_eq, alpha_inv

# ── Section D: Assembly ──────────────────────────────────────────────────────
def run():
    print("=" * 68)
    print("SIM-004-v3-DualScale-Corrected")
    print("Envelope (CCR) / Operative (RCR) — two aspects, one closure")
    print("CORRECTIONS: Explicit kappa, 4π velocity normalization, heuristic k-coupling flagged")
    print("=" * 68)
    
    # Pre-scan
    print("\n[Pre-scan] f_geom vs k  (operative aspect, no GP)")
    print(f"  {'k':>6}  {'K(k)':>8}  {'Ω_flip':>10}  {'RCR':>8}  {'f_geom':>10}")
    for k_test in [0.50, 0.70, 0.80, 0.90, 0.95, 0.99]:
        of, rc, fg, _ = operative_solver(k_test)
        K = ellipk(k_test**2)
        print(f"  {k_test:>6.2f}  {K:>8.4f}  {of:>10.5f}  {rc:>8.4f}  {fg:>10.6f}")
        
    f_need_geom = 1.0 / (WR_EQ * ALPHA_INV_GEOMETRIC)
    f_need_meas = 1.0 / (WR_EQ * ALPHA_INV_CODATA)
    print(f"\n  Target product f_geom·f_eq for α⁻¹_geometric : {f_need_geom:.8f}")
    print(f"  Target product f_geom·f_eq for α⁻¹_CODATA    : {f_need_meas:.8f}")
    
    # Self-consistent dual iteration
    print("\n[Self-consistent iteration]")
    k, kappa, omega_flip, RCR, f_geom, f_eq, alpha_inv = self_consistent_dual(k_init=0.90, kappa_init=1.0)
    
    # Final result
    print("\n" + "=" * 68)
    print("FINAL RESULT")
    print("=" * 68)
    print(f"  Wr_eq           = {WR_EQ:.4f}   (topological invariant, CWF)")
    print(f"  k (elliptic)    = {k:.6f}")
    print(f"  κ (saturation)  = {kappa:.6f}")
    print(f"  Ω_flip (barrier)= {omega_flip:.6f}")
    print(f"  RCR             = {RCR:.6f}")
    print(f"  f_geom (RCR)    = {f_geom:.8f}")
    print(f"  f_eq   (CCR)    = {f_eq:.8f}")
    print(f"  f_geom · f_eq   = {f_geom*f_eq:.8f}")
    print(f"\n  α⁻¹ predicted   = {alpha_inv:.6f}")
    print(f"  α⁻¹ geometric   = {ALPHA_INV_GEOMETRIC:.6f}")
    print(f"  α⁻¹ CODATA      = {ALPHA_INV_CODATA:.6f}")
    
    ratio = alpha_inv / ALPHA_INV_GEOMETRIC
    print(f"\n  Ratio predicted/geometric = {ratio:.6f}")
    
    f_product = f_geom * f_eq
    f_target  = 1.0 / (WR_EQ * ALPHA_INV_GEOMETRIC)
    print(f"\n  Target f_geom·f_eq        = {f_target:.8f}")
    print(f"  Current f_geom·f_eq       = {f_product:.8f}")
    print(f"  Residual factor           = {f_target/max(f_product,1e-12):.6f}")
    
    print("\n" + "=" * 68)
    print("OPEN ITEMS after SIM-004-v3-Corrected:")
    print("  1. k↔κ coupling heuristic k²=1-exp(-2κ) MUST be replaced by the")
    print("     actual shape-functional relationship derived from the GP equilibrium.")
    print("  2. Tw=1/2 from second-order perturbation (Dzhanibekov §5)")
    print("  3. Tik self-energy correction −0.000305 (geometric→CODATA)")
    print("  4. Fredholm gap proof from logarithmic saturation term")
    print("=" * 68)
    
    return {
        "k": k, "kappa": kappa, "omega_flip": omega_flip,
        "RCR": RCR, "f_geom": f_geom, "f_eq": f_eq,
        "alpha_inv": alpha_inv, "ratio_to_geometric": ratio
    }

if __name__ == "__main__":
    results = run()
