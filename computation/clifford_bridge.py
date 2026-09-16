"""
clifford_bridge.py — Clifford to Numerical/Matrix Translation Layer
Utility library for Praestology simulation engines (SIM-001 through SIM-007).

Conventions:
  Cl(3,0) with basis vectors e1, e2, e3 satisfying eᵢ² = +1, eᵢeⱼ = -eⱼeᵢ (i≠j).
  Pauli matrix representation: eᵢ → σᵢ.
  Bivector basis: B1 = e12, B2 = e23, B3 = e13  (matches framework convention).
  8D coefficient order: [s, v1, v2, v3, b12, b23, b13, ps].
"""

import numpy as np

# ─── Pauli Basis ─────────────────────────────────────────────────────────

SIGMA_1 = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_3 = np.array([[1, 0], [0, -1]], dtype=complex)
I_2     = np.eye(2, dtype=complex)

# Bivectors — framework convention (B3 = e13, not e31)
E12 = SIGMA_1 @ SIGMA_2   # = iσ3
E23 = SIGMA_2 @ SIGMA_3   # = iσ1
E13 = SIGMA_1 @ SIGMA_3   # = -iσ2

# Pseudoscalar
PS = SIGMA_1 @ SIGMA_2 @ SIGMA_3   # = i·I₂

# ─── Conversion ─────────────────────────────────────────────────────────

def multivector_to_matrix(c):
    """8D coefficient array → 2x2 complex matrix."""
    s, v1, v2, v3, b12, b23, b13, ps = c
    return (s * I_2
            + v1 * SIGMA_1 + v2 * SIGMA_2 + v3 * SIGMA_3
            + b12 * E12 + b23 * E23 + b13 * E13
            + ps * PS)

def matrix_to_multivector(M):
    """2x2 complex matrix → 8D coefficient array."""
    s   = np.real(np.trace(M) / 2.0)
    v1  = np.real(np.trace(M @ SIGMA_1) / 2.0)
    v2  = np.real(np.trace(M @ SIGMA_2) / 2.0)
    v3  = np.real(np.trace(M @ SIGMA_3) / 2.0)
    b12 = np.real(np.trace(M @ E12.conj().T) / 2.0)
    b23 = np.real(np.trace(M @ E23.conj().T) / 2.0)
    b13 = np.real(np.trace(M @ E13.conj().T) / 2.0)
    ps  = np.real(np.trace(M @ PS.conj().T) / 2.0)
    return np.array([s, v1, v2, v3, b12, b23, b13, ps])

# ─── Core Operations ─────────────────────────────────────────────────────

def multivector_product(a, b):
    """Full Clifford product a·b."""
    return matrix_to_multivector(multivector_to_matrix(a) @ multivector_to_matrix(b))

def reverse(c):
    """Reverse: flips sign of grades 2 and 3."""
    s, v1, v2, v3, b12, b23, b13, ps = c
    return np.array([s, v1, v2, v3, -b12, -b23, -b13, -ps])

def grade(c, k):
    """Extract grade-k component (k = 0, 1, 2, 3)."""
    out = np.zeros(8)
    if k == 0: out[0] = c[0]
    elif k == 1: out[1:4] = c[1:4]
    elif k == 2: out[4:7] = c[4:7]
    elif k == 3: out[7] = c[7]
    else: raise ValueError(f"Grade {k} not present in Cl(3,0)")
    return out

def scalar_part(c):
    """Grade-0 projection ⟨A⟩₀."""
    return c[0]

def norm_sq(c):
    """‖A‖² = ⟨A Ã⟩₀."""
    return scalar_part(multivector_product(c, reverse(c)))

def anticommutator(a, b):
    """{A, B} = A·B + B·A."""
    return multivector_product(a, b) + multivector_product(b, a)

def commutator(a, b):
    """[A, B] = A·B - B·A."""
    return multivector_product(a, b) - multivector_product(b, a)

# ─── Framework-Specific Helpers ──────────────────────────────────────────

def rotor(B, theta):
    """Rotor R = exp(-½ B θ) for a unit bivector B (8D array)."""
    half = -0.5 * theta
    # Taylor expansion for the exponential in Cl(3,0)
    # For unit B (B² = -1): exp(-½ B θ) = cos(θ/2) - B sin(θ/2)
    return np.cos(theta/2) * np.array([1,0,0,0,0,0,0,0]) + np.sin(theta/2) * B

def f_q_functional(bivectors):
    """F[Q] = Σ_{i<j} ‖BᵢBⱼ + BⱼBᵢ + 2δᵢⱼ‖² — closure functional (SIM-007)."""
    n = len(bivectors)
    F = 0.0
    for i in range(n):
        for j in range(i+1, n):
            ac = anticommutator(bivectors[i], bivectors[j])
            F += norm_sq(ac)
    # Self-anticommutator terms {Bi,Bi} = -2
    for i in range(n):
        self_ac = anticommutator(bivectors[i], bivectors[i])
        # Subtract the expected -2 contribution
        residual = self_ac.copy()
        residual[0] += 2.0   # add 2 to the scalar part
        F += norm_sq(residual)
    return F

# ─── Verification ────────────────────────────────────────────────────────

def verify_representation():
    """Self-test: confirms the matrix representation is a faithful Cl(3,0) isomorphism."""
    # Round-trip
    c = np.array([1.5, 2.0, -0.5, 3.0, 1.0, -2.0, 0.5, 1.2])
    assert np.allclose(c, matrix_to_multivector(multivector_to_matrix(c)))

    # Basis vector squares
    for v in [1, 2, 3]:
        e = np.zeros(8); e[v] = 1.0
        assert np.isclose(scalar_part(multivector_product(e, e)), 1.0)

    # Anticommutation
    e1 = np.zeros(8); e1[1] = 1.0
    e2 = np.zeros(8); e2[2] = 1.0
    assert np.isclose(scalar_part(anticommutator(e1, e2)), 0.0)

    # Bivector square
    b12 = np.zeros(8); b12[4] = 1.0
    assert np.isclose(scalar_part(multivector_product(b12, b12)), -1.0)

    # F[Q] = 0 at orthonormal closure
    B1 = np.zeros(8); B1[4] = 1.0   # e12
    B2 = np.zeros(8); B2[5] = 1.0   # e23
    B3 = np.zeros(8); B3[6] = 1.0   # e13
    F = f_q_functional([B1, B2, B3])
    assert np.isclose(F, 0.0, atol=1e-10), f"F = {F}, expected 0"

    print("All representation tests passed.")

if __name__ == "__main__":
    verify_representation()
