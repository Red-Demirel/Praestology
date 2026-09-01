# Methodological Note: Variational Field Solution vs. Numerological Fitting

A persistent issue in theoretical physics is the presentation of closed-form
algebraic expressions — often involving π, e, or simple fractions — that match
physical constants without an underlying physical mechanism.

## The Central Distinction

A numerological formula matches a constant by selecting terms that happen
to give the right number. The mechanism is absent: the formula does not
explain *why* the constant has that value, only that a particular combination
of π-powers produces it.

A derived result produces the constant as a consequence of a physical
mechanism. The test is: would the computation have given the same number
if you hadn't known the target? If yes, it is derived. If the formula was
selected because it matches the target, it is numerological regardless of
how elegant it looks.

**SIM-004-v2 explicitly treats the π-series candidate (4π³ + π² + π = 137.036304)
as an empirical target to be tested, not as a baseline assumption.**

---

### 1. Independent Variational Extraction

The primary objective of SIM-004-v2 is to solve the Gross-Pitaevskii energy
functional under 720° Möbius boundary conditions:

```
E[ψ] = ∫ [ ħ²/(2m)|∇ψ|² + g|ψ|²/(1+|ψ|²/n_sat) ] dV
```

subject to:
```
ψ(r, φ+2π) = -ψ(r, φ)   [Möbius sign flip]
ψ(r, φ+4π) =  ψ(r, φ)   [720° return]
```

The angular frequency ratio Ω_rotor_numerical is extracted directly from the
numerical phase gradient of the field solution at the crossover point —
not assumed. The Calugareanu-White-Fuller writhe Wr is computed from the
equilibrium centreline geometry of the GP field — not fitted. The CCR ratio
CCR = (Wr · Ω_rotor) / Ω_embed is the output of the computation. Its
comparison to α⁻¹ = 137.036... is the test.

The mechanism is the GP variational problem under topological boundary
conditions. If the π-series value emerges from the computation, it is because
the field geometry requires it.

### 2. Strict Falsification Threshold

The candidate value 4π³ + π² + π serves purely as a benchmark.

If the FEM solution for Ω_rotor_numerical deviates from this value by more
than 2.22 ppm (the maximum allowed environmental Π_eff correction from the
established framework), the candidate relation is **falsified**. There is no
freedom to adjust the formula after the fact — the computation either produces
the value or it does not.

### 3. Multi-Variable Consistency

Unlike isolated numerological formulas, SIM-004-v2 feeds a continuous
topological pipeline. The writhe Wr produced by the equilibrium GP computation
must simultaneously:

- Yield CCR = α⁻¹ (SIM-004 itself)
- Serve as the reference unit against which the truncated S³ arc gives
  fractional charges ±2/3 and ±1/3 (SIM-001-v3)
- Provide the energy scale for the mutual linking calculation that recovers
  the proton-to-electron mass ratio 1836 (SIM-005-v2)

The multi-variable consistency requirement is the strongest evidence that
the approach is structural: the same topology must
produce the fine-structure constant, fractional quark charges, and the
proton-to-electron mass ratio from a single computation without free parameters.

---

## What Falsification Looks Like

The computation can fail in multiple distinct ways, each informative:

| Failure mode | Implication |
|---|---|
| No stable Möbius GP equilibrium | GP equation with this nonlinearity does not support 720° topology |
| Wr is irrational, no algebraic structure | CCR = topological writhe identification requires revision |
| CCR ≠ 137.036... by > 1% | Möbius topology is not the source of the fine-structure constant |
| Ω_rotor_numerical ≠ 4π³+π²+π by > 2.22 ppm | π-series candidate is falsified; different formula needed |
| SIM-001 gives non-rational Wr(quark)/Wr(electron) | Fractional charge from truncated S³ path requires revision |
| SIM-005 gives m_p/m_e ≠ 1836 | Proton mass excess is not from non-additive CCR_binding |

Each failure mode points to a specific structural revision — not a parameter
adjustment.

---

## Summary

Derivation is achieved through field action and boundary topology. The π-series candidate is a prediction to be tested.

If it fails, the framework learns something precise about where the mechanism
breaks down. If it succeeds, the mechanism behind a previously mysterious
constant is identified. Either outcome is scientifically valuable.

---

*This note applies to all simulation specifications in issues/foundational/
that involve comparison to known physical constants.*
