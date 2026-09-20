# The Parameter & Variable Cascade across Depths

**Logical path:** core/parameter-cascade.md (Markdown-native)
**Version:** 1.2
**Status:** STRUCTURAL MAP — the classification and cascade are the framework's
claimed structure. Individual links are marked DERIVED / DEFINITIONAL /
CANDIDATE / OPEN.

**Changelog 1.1 → 1.2:**
§0 units adjudication declared ([Π_eff] = s⁻¹); η demoted from primitives,
ψ added, Π_eff split baseline/local; governance lanes declared.
§1 Π_eff baseline/local split; V_c operative-from-first-R5 note.
§2 cross-basis delivery; α⁻¹ → DERIVED-CANDIDATE; ω_Φ row (closure-indexed);
CCR instance table (band semantics resolved); χ_Φ units J·s.
§3 CCR_binding split ratio × E_scale; Welch chain made exact.
§4 threshold comparison made dimensionless (E_scale); magic numbers → Count.
§5 graph edges corrected; pivotal reading pre-committed.
§6 SIM-004-v2 row split unconditional/conditional.
§7 rows added and synced. §8 4b rewritten as carrier adjudication.
§9 "valid" → "unrefuted". §10 new (required syncs).

---

## §0 The Three Kinds of Quantity

Values in the framework are not one kind of thing. They fall into three
distinct categories, and the cascade only makes sense if these are held apart:

| Kind | Character | Examples | Tunable? |
|:---|:---|:---|:---|
| **Ratio** (dimensionless) | Derived from recurrence, closure, or topology | CCR⁰, Wr_eq, F, f_closure, α⁻¹, m_p/m_e | No — ratios all the way down |
| **Dimensional quantity** | Ratio × substrate primitive (Π_eff, c, ħ) | I_rot, E_Φ, ω_Φ, V_c, χ_Φ, η | No — inherits scale from substrate |
| **Relation** | Generative condition, not a value | v_{k+2} = v_{k+1} + v_k; Q* = R_k[Q*]; F[Q] = 0; D_{d+1} = Fix(Φ_d(D_d)) | N/A — these generate values |

**Why this matters:** ratios cannot be tuned because they are dimensionless
evaluations of structural features. Dimensional quantities inherit their scale
from substrate primitives, which are not free parameters either — they are
properties of the substrate. Relations generate the whole structure. No tier
has a place to put a free knob.

**Substrate primitives** (not derived, not tuned): **ψ** (the process field —
ontological ground; η = ∫R(ψ)dτ), **Π_eff,base** (the un-depleted baseline
rate), **c**, **ħ**, and the narrative choice of units.

**Units adjudication (declared):** **[Π_eff] = s⁻¹** — substrate process rate.
This resolves the fork across canon row 7, the Dirac μ candidates, and the
SIM-007 depth map in one decision. Consequences: χ_Φ = I_rot·ω_Φ carries
units **J·s** (F = χ_Φ∇Π_eff → J/m ✓); the Dirac mass term collapses to
μ = (mc/ħ)·(Π_eff/ω_Φ). Local Π_eff is **derived**, not primitive:
Π_eff,local = Π_eff,base − depletion(η) (depletion-as-absolute-pi-eff).

**Correction from v1.0/1.1:** η was listed as a substrate primitive. This is
the corpus's most-repeated regression: η is the committed integral of ψ —
derivative level, object- and environment-indexed. It is now a dimensional
row, not a primitive. ψ was absent and is now listed.

**Governance lanes (precedence):** terminology-canonical.yaml = what things
are *called*; this cascade = what things *are* (quantities, units, dependency
order); the session watch = what regresses; open-reconciliation-notes.yaml =
what is unresolved. Units live in exactly one place: here.

---

## §1 Depth D₋₁ → D₀: Pre-Vector Potential to Fixed Basis

**Primary relation:** v_{k+2} = v_{k+1} + v_k — the minimal two-step,
non-destructive memory recurrence.

**Emergent quantities:**

- **Scaling eigenvalues (φ, φ⁻¹)** — *Ratio (algebraic)*
  Roots of λ² − λ − 1 = 0. φ ≈ 1.618 governs the growth mode;
  φ⁻¹ ≈ 0.618 governs the transient decay.
  Status: **DERIVED** (d-minus-one-pre-vector-level.yaml §2)

- **Transient retention factor (CCR⁰ = φ⁻¹)** — *Ratio (algebraic); trajectory property*
  The fraction of open phase space carried forward per cycle.
  Status: **DERIVED** — unique band-compatible eigenvalue magnitude;
  the dynamics' own self-measurement at convergence.

- **Fixed spatial basis (D₀ = {e₁, e₂, e₃})** — *Relation (co-naturality)*
  Three independent vector directions, forced by the co-naturality of
  Cl(3,0) with 3D space. The count three is not produced by φ; it is a
  property of the algebra. φ characterizes the relaxation *rate* toward
  these fixed directions.
  Status: **ESTABLISHED** (co-naturality)

- **Substrate baseline rate (Π_eff,base)** — *Dimensional primitive*
  Present before any transition. The D₋₁ → D₀ transition establishes its
  *baseline value* in the un-depleted limit — a labelling convenience, not
  a production. Local Π_eff = Π_eff,base − depletion(η) is derived from
  this point onward.
  Status: **SUBSTRATE PRIMITIVE** (value possibly pinned — see §8 4b)

- **Viability filtering (V_c, qualitative)** — *Relation*
  R5 selection is operative from the first closure event: the non-resonance
  condition of this transition *is* the first viability filter. What begins
  here is the relation; its quantitative P_env form becomes operational at
  D₁ and higher, where compression matters.
  Status: **STRUCTURAL** from first R5 firing

---

## §2 Depth D₀ → D₁: Vector Basis to 1-Plane Closures (Electron, Photon)

**Primary operation:** cross-basis pairings of the converged grade-1 basis —
e₁∧e₂, e₂∧e₃, e₁∧e₃ (depth-0-as-process.yaml 1b) — under the B² = −1
boundary condition, yielding 720° Möbius vortex closures. Note: consecutive-
pair folding of a single chain is *not* the delivery mechanism (the chain's
bivector record alternates sign at constant magnitude; cross-basis pairings
of the fixed basis is the consistent route).

**Emergent quantities:**

- **Equilibrium writhe (Wr_eq = 3/2)** — *Ratio (topological)*
  CWF invariant of the equilibrium centerline. What is fixed: Lk = 2
  (isotopy) and Tw = 1/2 (Möbius framing, algebraic); Wr = Lk − Tw = 3/2
  follows for every boundary-respecting configuration — the subscript _eq
  concedes shape-dependence of the equilibrium choice.
  Status: **DERIVED** (CWF theorem + 720° boundary condition)

- **Closure yield (f_closure)** — *Ratio (geometric)*
  The S² integral of the closure indicator χ(B): f_closure = (1/4π) ∫ χ(B) dB.
  Status: **OPEN** — the SIM-004-v2 GP-solve target.

- **Fine-structure constant (α⁻¹)** — *Ratio (geometric)*
  α⁻¹ = 1 / (Wr_eq · f_closure). Wr_eq is fixed at 3/2; f_closure is the
  SIM-004-v2 target.
  Status: **DERIVED-CANDIDATE** — this is a falsifiable identification,
  not a definition. If SIM-004-v2's f_closure yields a different product,
  the identification fails. (Correction from v1.0/1.1, which marked it
  DEFINITIONAL — the one status wrong in the unsafe direction.)

- **Trapped rotational inertia (I_rot)** — *Dimensional*
  Internal rotational capacity stored in a 1-plane voluntary merge:
  m_e c² = ħ ω_z. Scale inherited from ħ and ω_z.
  I_rot is a property of the committed topology (canon row 3) — it does
  not itself vary with environment; environment enters via the carrier
  adjudication (§8 4b).
  Status: **STRUCTURAL** (rotor-to-ccr-transition.yaml); quantitative form
  depends on the local-explicit field equation (open).

- **Phase rate (ω_Φ)** — *Dimensional, closure-indexed*
  The phase-precession rate of a committed topology. **Not substrate-
  universal:** if ω_Φ were one universal rate, m = ħω_Φ/c² would be the
  same for every particle — contradicted by the mass spectrum this cascade
  catalogues. Each committed topology carries its own ω_Φ.
  Candidate identifications: ω_z = ω_Φ = ω_Compton,type. With E_Φ = ½I_rotω_Φ²
  and mc² = ħω_z this yields I_rot = 2m(ħ/mc)² — the factor-2 closes and
  E_Φ = mc² exactly.
  Status: **CANDIDATE** (identification open; consumed by E_Φ, χ_Φ, μ)

- **Phase energy capacity (E_Φ)** — *Dimensional*
  Total committed energy: E_Φ = (1/2) I_rot ω_Φ².
  Status: **DEFINITIONAL** given I_rot and ω_Φ.

- **Phase gradient coupling (χ_Φ)** — *Dimensional (units J·s)*
  χ_Φ = I_rot · ω_Φ. The committed topology's response strength to
  process-rate gradients: F_grav = −χ_Φ ∇Π_eff. Dimensional check under
  the declared units: (kg·m²·s⁻¹)·(s⁻¹·m⁻¹) = J/m = N ✓.
  **Placement correction (kept from v1.1):** χ_Φ emerges at D₁ alongside
  I_rot — the electron has gravitational response.
  Status: **DEFINITIONAL** given I_rot and ω_Φ.
  **Sync required:** canon row 7 (χ_Φ in kg) amended to J·s.

- **Closure viability threshold (V_c)** — *Dimensional (Pa)*
  Boundary condition P_int = V_c(P_env); environment-dependent; quantitative
  P_env form open (vc-from-pi-eff). Dimensionless comparisons (e.g. against
  the N=4 residual, §4) reduce through V̂_c ≡ V_c·V_ref/E_scale(d) — see
  E_scale below.
  Status: **STRUCTURAL**

- **Depth energy scale (E_scale(d))** — *Dimensional*
  The energy scale of a depth-d closure event, consumed by two reductions:
  orthogonality energy = CCR_binding × E_scale(2) (§3), and the
  dimensionless threshold V̂_c = V_c·V_ref/E_scale(d) (§4). Candidate
  identification: E_scale(d) = ħ·ω_Φ(type at depth d) — the quantum as the
  depth-local energy scale.
  Status: **CANDIDATE**

**CCR instances at this depth — three kinds, resolving the band ambiguity:**

| Instance | Value | Kind | Role |
|:---|:---|:---|:---|
| CCR_crit | 1 | relation boundary | closure threshold (rotor-to-ccr-transition.yaml); the band's upper edge — saturation, not "uncommitted" |
| CCR⁰ | φ⁻¹ | trajectory property | transient retention per cycle (§1) |
| CCR_electron | α | configuration property | the committed vortex's band cost — same structural kind as CCR_binding |

Band semantics (harmonized): stable band (0, 1); CCR → 1⁻ = saturation /
closure threshold; CCR → 0⁺ = rigidity. The apparent contradiction between
"CCR = 1 is uncommitted" (ccr v2.0) and "CCR¹ = 1 is the threshold" dissolves
once the instance kinds are separated.
**Sync required:** closure-configuration-ratio.yaml boundary_conditions sentence.

---

## §3 Depth D₁ → D₂: Multi-Plane Triality to Nucleons (Proton, Neutron)

**Primary operation:** combining three independent bivector strains under
full 3-plane orthogonality constraint F[Q] = 0.

**Emergent quantities:**

- **Orthogonality energy (CCR_binding × E_scale(2))** — *Ratio × energy scale*
  CCR_binding is a **dimensionless ratio** (the Wr-weighted phase-space cost
  evaluated at the triality configuration). The quantity entering the proton
  mass formula is the **product**: orthogonality energy = CCR_binding ×
  E_scale(2) [J]. The mass formula consumes the product:
  m_p c² = (3/2)·I_rot,quark·ω_Φ² + CCR_binding·E_scale(2).
  A dimensionless ratio cannot be added to an energy — the split is
  mandatory, not stylistic.
  Status: **OPEN** — SIM-005-v2 target.

- **Welch bound residual (F = 8/3)** — *Ratio (algebraic), exact anchor*
  The chain, stated exactly:
  1. On the bivector space Λ²(ℝ³) with positive-definite inner product:
     **{Bᵢ, Bⱼ} = −2⟨Bᵢ, Bⱼ⟩** — pure scalar, since Λ⁴(ℝ³) = 0. This
     identity is why the anticommutator functional *is* (4×) the
     squared-inner-product functional, and why Welch applies exactly
     rather than analogically.
  2. Welch bound (N=4 unit vectors, d=3): Σᵢ<ⱼ ⟨Bᵢ,Bⱼ⟩² ≥ N(N−d)/(2d) = 2/3,
     achieved uniquely by the regular tetrahedron (⟨Bᵢ,Bⱼ⟩ = −1/3 all pairs).
  3. F = Σᵢ<ⱼ ‖{Bᵢ,Bⱼ}‖² = 4·Σᵢ<ⱼ ⟨Bᵢ,Bⱼ⟩² ≥ 4·(2/3) = **8/3**.
  Status: **DERIVED** (SIM-007-v1 + Welch bound theorem — exact, no free
  parameters). The same chain predicts the N-scan residuals where tight
  frames exist (N=4: 8/3; N=6: 12; N=5, 7: strict bounds).

---

## §4 Depth D₂ → D₃: S⁷ Embedding to Heavy Nuclei

**Primary operation:** the F = 8/3 residual strain cannot be absorbed in
Cl(3,0), forcing a Hopf-level embedding into S⁷ topological linking.

**Emergent quantities:**

- **Environmental threshold shift (V̂_c at S⁷)** — *Dimensional, reduced*
  Under extreme substrate depletion (Π_eff,local → low, high P_env), the
  dimensionless threshold V̂_c = V_c·V_ref/E_scale(2) drops below the N=4
  residual 8/3, catalyzing heavy-element nuclear closures. (The v1.0/1.1
  phrasing "V_c drops below 8/3" compared a Pa-quantity to a dimensionless
  number; the reduction through E_scale is the operational form.)
  Status: **STRUCTURAL** — quantitative form depends on vc-from-pi-eff
  and SIM-006.

- **Magic numbers** — *Count (integer; degenerate ratio with unity reference)*
  The Steiner enumeration of viable S⁷ linking configurations. Counts are
  not ratios in the strict sense; recorded as the degenerate case
  (n : 1) so the three-kind taxonomy is not stretched silently.
  Status: **OPEN** — SIM-006-v1 target.

---

## §5 The Interdependence Structure: Graph, Not Chain

The cascade is often summarized as a linear chain:

> Recurrence → CCR⁰ → f_closure → α⁻¹ → I_rot → Mass Spectrum

This is misleading. The actual structure is a **graph** with parallel
outputs from shared geometry:

```
        Recurrence                        D₀ basis {e₁,e₂,e₃}
            │                             (fixed points of Φ₀;
            ▼                              co-natural count: 3)
      {φ, φ⁻¹}                                    │
            │                                     ▼
            ▼                             D₁ geometry
      CCR⁰ = φ⁻¹ ╍╍╍╍╍╍╍╍╍╍╍╍╍►          (720° Möbius vortex)
   [PIVOTAL — conditional edge;                 │
    reading pre-committed below]          ┌─────┼─────────────┐
                                          ▼     ▼             ▼
                                    Wr_eq = 3/2  f_closure   I_rot
                                      │           │            │
                                      └─────┬─────┘            │
                                            ▼                  │
                                α⁻¹ = 1/(Wr_eq · f_closure)    │
                                (parallel output of D₁         │
                                 geometry)                     │
                                                               │
                                               ┌───────────────┤
                                               ▼               ▼
                                     χ_Φ = I_rot·ω_Φ   E_Φ = ½I_rot·ω_Φ²
                                               └───────┬───────┘
                                                       ▼
                                              Mass spectrum
                                     (parallel outputs per closure
                                      type: electron, proton, ...)
```

**Key structural corrections:**

1. **α is not a precursor of I_rot.** Both are parallel outputs of the
   D₁ geometry. The same geometry that yields α also yields I_rot.
   (Graph edges corrected in v1.2 — v1.1's diagram drew the outputs
   pointing into D₁ geometry.)

2. **The CCR⁰ → f_closure link is the pivotal open derivation — and its
   reading is pre-committed.** Default prediction, from the framework's own
   trajectory/fixed-point doctrine: **the link is absent; the cascade
   splits.** f_closure is a fixed-point property of Φ₁; φ characterizes
   the relaxation toward D₀; fixed points carry no relaxation memory.
   Fingerprint *for* the link: **√5** (the eigenvalue gap — the
   discriminant of λ² − λ − 1) surfacing in f_closure would be the
   transient's fingerprint, evidence that the D₋₁ chain feeds forward.
   Both readings are written before SIM-004-v2 runs; either outcome is
   informative, neither is spinnable.

3. **The mass spectrum is not produced by I_rot alone.** It is the set of
   per-type costs (I_rot, ω_Φ per closure type). The *spectrum* comes from
   the variety; I_rot gives the *cost per type*.

4. **Parallel outputs are the rule, not the exception.** Where a summary
   reads "A → B → C," check whether the arrows are actually parallel
   readings of the same underlying structure.

---

## §6 Verification Scope: Per Depth Transition

Each depth transition has its own independent validation. Success at one
transition does not imply success at the next.

| Depth transition | Verification target | SIM | Validates unconditionally | Validates conditionally | Does NOT validate |
|:---|:---|:---|:---|:---|:---|
| D₀ → D₁ | Wr_eq, f_closure, α⁻¹ from geometry | SIM-004-v2 | Wr_eq, f_closure, the α⁻¹ identification | — | Proton, nucleus, higher depths |
| D₋₁ → D₀ | Recurrence, φ, φ⁻¹, CCR⁰ | (same run) | — | Recurrence, φ, φ⁻¹, CCR⁰ — **only if the pivotal link holds** (§5.2) | — |
| D₁ → D₂ | Proton mass gap from orthogonality energy | SIM-005-v2 | CCR_binding, triality closure | — | Nucleus, magic numbers, higher depths |
| D₁ → D₂ | N=4 residual F = 8/3 | SIM-007-v1 | Welch anchor, depth-3 forcing | — | S⁷ embedding details |
| D₂ → D₃ | Magic numbers from S⁷ Steiner enumeration | SIM-006-v1 | S⁷ embedding, nuclear shell structure | — | Higher depths |

**Correct scope statement:** *"SIM-004-v2 validates D₀ → D₁ unconditionally;
it validates D₋₁ → D₀ only through the pre-committed pivotal reading.
SIM-005, SIM-007, and SIM-006 validate successive transitions. Cumulative
success across all four would establish the full cascade with no free knobs.
Individual success validates only its own transition."*

"No free knobs" is a claim about the absence of tuning, not a claim that one
success proves all.

---

## §7 Summary Mapping Table

| Parameter / Variable | Depth transition | Kind | Interlocking dependence | Status |
|:---|:---|:---|:---|:---|
| **ψ** | (substrate) | Process field | Ontological ground; η = ∫R(ψ)dτ | PRIMITIVE |
| **Π_eff,base** | (substrate) | Dimensional primitive | Un-depleted baseline rate; **[s⁻¹] declared** | PRIMITIVE |
| **Π_eff,local** | all depths | Dimensional (derived) | = Π_eff,base − depletion(η) | DERIVED |
| **η** | from first R5 | Dimensional (derived) | Committed integral of ψ; depletes Π_eff | DERIVED (definition); object/environment-indexed |
| **c, ħ** | (substrate) | Dimensional primitives | Conversion constants | PRIMITIVE |
| **v_{k+2} = v_{k+1} + v_k** | — | Relation | Minimal two-step memory under non-destructive phase conservation | DERIVED |
| **φ, φ⁻¹** | D₋₁ → D₀ | Ratio (algebraic) | Roots of λ² − λ − 1 = 0 | DERIVED |
| **CCR⁰ = φ⁻¹** | D₋₁ → D₀ | Ratio (algebraic); trajectory | Unique band-compatible eigenvalue magnitude | DERIVED |
| **D₀ = {e₁, e₂, e₃}** | D₋₁ → D₀ | Relation | Co-naturality of Cl(3,0) with 3D space | ESTABLISHED |
| **B = eᵢ ∧ eⱼ (cross-basis)** | D₀ → D₁ | Relation | Outer product; B² = −1 boundary condition | DERIVED |
| **Wr_eq = 3/2** | D₀ → D₁ | Ratio (topological) | CWF: Lk = 2, Tw = 1/2 (Möbius framing) | DERIVED |
| **f_closure** | D₀ → D₁ | Ratio (geometric) | S² integral of closure indicator χ(B) | **OPEN** (SIM-004-v2) |
| **α⁻¹** | D₁ | Ratio (geometric) | = 1 / (Wr_eq · f_closure) | DERIVED-CANDIDATE (target 137.036) |
| **CCR_crit = 1** | any transition | Relation boundary | Closure threshold; band upper edge | ESTABLISHED (structure) |
| **CCR_electron = α** | D₁ | Ratio (configuration) | Band cost of committed vortex | DERIVED-CANDIDATE |
| **I_rot** | D₁ | Dimensional | Trapped rotational inertia of 1-plane merge; topology property (canon row 3) | STRUCTURAL |
| **ω_Φ** | D₁, per type | Dimensional (closure-indexed) | Phase rate; ω_z = ω_Φ = ω_Compton candidate; factor-2 closure | CANDIDATE |
| **E_Φ** | D₁ | Dimensional | = ½ I_rot ω_Φ² | DEFINITIONAL |
| **χ_Φ** | D₁ | Dimensional (J·s) | = I_rot · ω_Φ; F_grav = −χ_Φ∇Π_eff | DEFINITIONAL (canon row 7 sync required) |
| **V_c** | D₁ | Dimensional (Pa) | P_int = V_c(P_env); dimensionless form V̂_c via E_scale | STRUCTURAL |
| **E_scale(d)** | per depth | Dimensional | Depth-d closure energy scale; CCR_binding and V̂_c reductions | CANDIDATE |
| **CCR_binding** | D₁ → D₂ | Ratio (geometric) | Orthogonality energy = CCR_binding × E_scale(2) | **OPEN** (SIM-005-v2) |
| **F = 8/3** | D₂ | Ratio (algebraic) | Welch bound via {Bᵢ,Bⱼ} = −2⟨Bᵢ,Bⱼ⟩; tetrahedron | DERIVED |
| **S⁷ embedding** | D₂ → D₃ | Relation | Hopf-level embedding forced by F = 8/3 | STRUCTURAL |
| **V̂_c shift** | D₂ → D₃ | Dimensional (reduced) | Threshold drop catalyzing heavy-element closure | STRUCTURAL |
| **Magic numbers** | D₂ → D₃ | Count (degenerate ratio) | Steiner enumeration on S⁷ | **OPEN** (SIM-006-v1) |

---

## §8 Open Items, Ranked

1. **CCR⁰ → f_closure** — the pivotal open derivation, with the reading
   pre-committed (§5.2): default absent/cascade-splits; √5 in f_closure is
   the fingerprint for the link. **Priority: 1.**

2. **f_closure from SIM-004-v2** — the GP-solve target that closes the
   α⁻¹ identification. **Priority: 1.**

3. **CCR_binding × E_scale(2) from SIM-005-v2** — the proton mass gap as
   orthogonality energy. Closes D₁ → D₂. **Priority: 1.**

4. **V_c(P_env) functional form** — required for the D₂ → D₃ threshold
   shift and the gravity-threshold mechanism. **Priority: 2.**

4b. **Environmental carrier of inertial mass (consolidated; one item, one
    owner: dirac-as-grade-chain-closure.yaml #mu-dimensional-form).**
    I_rot is fixed (canon row 3); the open question is which carrier
    transports environment into effective mass:
    **(A) Π_eff enters μ directly:** μ = (mc/ħ)·(Π_eff/ω_Φ). Consequence:
    m_eff = m·(Π_eff/ω_Φ), and the weak equivalence principle becomes
    exact and structural — a = −2c²∇ln Π_eff, with I_rot and ω_Φ canceling
    (object-independent free fall). Deviations from EP enter only through
    object-indexed self-depletion — the structure's own η contribution to
    its local Π_eff (the self-energy analogue). Strong-field signature:
    effective mass drops in deep wells, but free fall stays universal.
    **(B) ω_Φ,type(Π_eff):** type-indexed response function. EP universality
    then hinges on type-universality of the response; composition-dependence
    of strong-field free fall is the discriminator between (A) and (B).
    **Over-constraint flag:** (A) + ω_z = ω_Φ + E_Φ = mc² together force
    **Π_eff,base = ω_Φ,electron** — the substrate baseline becomes pinned
    to a measurable (a no-free-knob consequence; holds only if all three
    candidate identifications hold).
    Bridges this cascade, commitment-depletion-duality.yaml, and
    gravity-and-ccr-threshold.yaml. **Priority: 2.**

5. **SIM-006 magic numbers** — S⁷ Steiner enumeration. Closes D₂ → D₃.
   **Priority: 2.**

6. **CCR² invariant-type** — determine whether the D₁ → D₂ invariant is
   combinatorial or index-theoretic, consistent with the
   algebraic → geometric → index-theoretic pattern. **Priority: 2.**

---

## §9 What This Establishes

**Established:**
- The cascade has three kinds of quantity (ratio, dimensional, relation),
  and no tier has a place to put a free knob.
- Ratios constrain ratios; dimensional quantities inherit from ratios plus
  substrate primitives; relations generate the whole structure.
- The recurrence v_{k+2} = v_{k+1} + v_k is derived from the geometric
  origin in d-minus-one-pre-vector-level.yaml §1.
- φ, φ⁻¹, CCR⁰ = φ⁻¹ follow algebraically from the recurrence.
- Wr_eq = 3/2 follows from fixed Lk = 2 and the Möbius framing Tw = 1/2.
- F = 8/3 is anchored exactly by the Welch bound (via the
  {Bᵢ,Bⱼ} = −2⟨Bᵢ,Bⱼ⟩ identity).
- ω_Φ is closure-indexed: a substrate-universal phase rate would give every
  particle the same mass, contradicting the spectrum this cascade catalogues.

**Structural (not yet verified):**
- The D₀ → D₁ geometry produces α⁻¹ ≈ 137.036 without free parameters
  (pending SIM-004-v2).
- The D₁ → D₂ chain produces the proton mass gap (pending SIM-005-v2).
- The D₂ → D₃ chain produces the nuclear magic numbers (pending SIM-006-v1).
- Weak EP exact and structural under the Π_eff carrier (§8 4b).

**Open:**
- The CCR⁰ → f_closure link — pivotal, reading pre-committed.
- The V_c(P_env) functional form.
- The CCR² invariant type.
- The environmental carrier adjudication (§8 4b).

**What is claimed without free knobs:**
- Each depth transition's outputs are fully constrained by the transition's
  own structural condition. No transition has an adjustable parameter.
- If each transition's SIM succeeds, the cascade is confirmed as a whole.
  If any transition fails, that transition (and its downstream) is refuted;
  upstream transitions remain **unrefuted** — with the caveat that, by §5's
  graph, downstream outputs consume upstream outputs, so a downstream
  failure is also evidence against the inputs it consumed.

---

## §10 Required Syncs (debts this revision creates)

1. **terminology-canonical.yaml row 7:** χ_Φ units kg → **J·s** (under the
   declared [Π_eff] = s⁻¹).
2. **closure-configuration-ratio.yaml v2.x:** boundary_conditions sentence —
   stable band (0,1); CCR → 1⁻ = saturation/closure threshold; CCR → 0⁺ =
   rigidity. Resolves the "uncommitted vs threshold" reading of CCR = 1.
3. **dirac-as-grade-chain-closure.yaml:** 4b ownership confirmed
   (mu-dimensional-form is the single owner of the carrier adjudication);
   μ-dimensional note adopts the collapsed form μ = (mc/ħ)(Π_eff/ω_Φ) as
   candidate (i′).
4. **mass-as-plane-independence.yaml:** proton formal_expression consumes
   CCR_binding × E_scale(2) (energy), not the bare ratio.
5. **depletion-as-absolute-pi-eff.yaml:** cross-reference the cascade's
   Π_eff,base/Π_eff,local split (same content, now catalogued).
