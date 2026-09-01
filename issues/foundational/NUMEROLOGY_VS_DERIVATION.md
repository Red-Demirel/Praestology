# Methodological Note: Variational Field Solution vs. Numerological Fitting

A persistent issue in theoretical physics is the presentation of closed-form algebraic expressions—often involving $\pi$, $e$, or simple fractions—that match physical constants without an underlying physical mechanism. 

To maintain strict scientific rigor, **Issue #SIM-004-v2 explicitly treats the $\pi$-series candidate ($4\pi^3 + \pi^2 + \pi = 137.036304$) as an empirical target to be tested, NOT as a baseline assumption**[cite: 3].

### Key Distinctions in Our Approach

1. **Independent Variational Extraction:** The primary objective of `SIM-004-v2` is to solve the Gross-Pitaevskii (GP) energy functional under $720^\circ$ Möbius boundary conditions[cite: 3]:
   $$E[\psi] = \int \left[ \frac{\hbar^2}{2m}|\nabla\psi|^2 + \frac{g|\psi|^2}{1+|\psi|^2/n_{\text{sat}}} \right] dV$$
   The angular frequency ratio $\Omega_{\text{rotor\_numerical}}$ is extracted directly from the numerical phase gradient of the field[cite: 3].

2. **Strict Falsification Threshold:** The candidate value $4\pi^3 + \pi^2 + \pi$ serves purely as a benchmark[cite: 3]. If the finite element method (FEM) solution for $\Omega_{\text{rotor\_numerical}}$ deviates from this value by more than the environmental correction factor ($> 2.22\text{ ppm}$), the candidate relation is **falsified**[cite: 3].

3. **Multi-Variable Consistency:** Unlike isolated numerological formulas, `SIM-004-v2` feeds a continuous topological pipeline. The resulting writhe ($Wr$) must simultaneously yield valid fractional charges for open $S^3$ arcs (`SIM-001-v3`) and the correct mass ratio via Gauss mutual linking (`SIM-005-v2`).

Derivation is achieved through field action and boundary topology—not formula matching[cite: 3].
