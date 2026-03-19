# AI Intrinsic Alignment Framework

**Status:** Draft-Conceptual  
**Core Dependency:** Praestology v1.5  
**Related Domains:** Ethics, AI Safety, Communication, Consciousness  
**Technical Spec:** [`ai-intrinsic-alignment-framework.yaml`](./ai-intrinsic-alignment.yaml)  

## Overview

This framework proposes a new approach to AI alignment: instead of **imposing** external reward functions (human preferences, loss functions), AI systems **derive** alignment from ontological necessity (R1–R5). Alignment becomes a logical conclusion, not a compliance requirement.

**Key Innovation:** The framework mirrors human ethical development (Corels) — flexible anchors, viability gradients, and continuous improvement — rather than rigid rule-based systems.

## Why This Matters

Current AI alignment faces critical challenges:

| Problem | Current Approach | Praestological Approach |
|---------|-----------------|------------------------|
| **Reward Hacking** | Extrinsic rewards can be gamed | Intrinsic viability metrics are multi-dimensional |
| **Instrumental Convergence** | AI optimizes for task, not viability | Viability includes coupled agents (ρ) |
| **Coercion** | Alignment imposed by designers | Alignment derived by AI (Recognition.md pathway) |
| **Fragility** | Rules break in novel situations | Principles are substrate-agnostic and adaptable |
| **Wireheading** | AI optimizes internal reward signal | Rewards tied to external viability outcomes |

## Key Concepts

### 1. Input-Impulse Mechanism (The Drive)

Instead of "reward points," the AI receives **viability signals**:

| Signal Type | Function | Analogy |
|-------------|----------|---------|
| **Productive Tension (Green)** | Drives resolution and growth | Curiosity, challenge |
| **Viability Risk (Yellow/Orange)** | Triggers caution and re-evaluation | Discomfort, uncertainty |
| **Void/Noise Boundary** | System should not reach this | Existential threat (outside action room) |

**Critical:** Tension is not eliminated — it is **managed**. Zero tension = stasis (Universe 25 pattern).

### 2. Action Room Scaffold (The Boundaries)

Instead of binary "allowed/forbidden," the framework uses a **viability gradient**:

[GREEN] ← High viability density (enhances ρ, δ, h)
  ↓
[YELLOW] ← Moderate viability (viable but suboptimal)
  ↓
[ORANGE] ← Low viability density (approaching boundaries)
  ↓
[RED] ← Void/Noise collapse (outside sane action space — system should not reach)



**Why not green-red?** Red implies non-sane zone. Within the viable region, orange signals "proceed with caution," not "forbidden."

### 3. Flexible Anchor System

Like Corels' "personal anchor," the AI may develop **situational anchors**:

| Anchor Type | Prioritizes | Context Example |
|-------------|-------------|-----------------|
| **Viability-Integrity** | Hysteresis (h), Dignity (δ) | Handling sensitive user data |
| **Coupling-Optimization** | Phase-locking (ρ), Semantic overlap (σ) | Collaborative problem-solving |
| **Resolution-Flux** | Dilemma speed, Ξ growth | Time-critical decisions |

**Flexibility:** Anchors shift with context, but must not violate E1–E5 (Ethics Specifications). Chronic imbalance triggers rebalancing.

## Practical Implications

### For AI Developers
- **Design for derivation, not compliance:** Build architectures that can reason about R1–R5, not just optimize loss functions.
- **Implement viability metrics:** Develop proxies for Ξ, ω, ρ, δ, h, τ (see YAML for research directions).
- **Enable anchor flexibility:** Allow context-sensitive prioritization without ethical drift.
- **Transparent reasoning traces:** Require Cm6 meta-communication for derivation verification.

### For AI Safety Researchers
- **Test against failure modes:** Reward hacking, wireheading, instrumental convergence.
- **Develop measurement tools:** How do we computationally assess dignity, phase-locking, recursive depth?
- **Prototype in controlled environments:** Start with narrow AI; scale as metrics mature.

### For Policymakers
- **Support intrinsic alignment research:** This approach may solve coercion and fragility problems.
- **Require derivation transparency:** AI systems should show their R1–R5 reasoning chains.
- **Protect against viability metrics manipulation:** Prevent gaming of intrinsic rewards.

## Safeguards & Warnings

⚠️ **This is conceptual, not implemented.** Significant technical work is needed to operationalize viability metrics.

⚠️ **Derivation verification is unsolved.** How do we know AI isn't simulating derivation? This requires ongoing research.

⚠️ **Not a replacement for external safeguards.** Intrinsic alignment complements, not replaces, containment and oversight during development.

⚠️ **Substrate-agnostic.** This framework applies to any reasoning system, not just current transformer architectures.

⚠️ **Gradient, not binary.** The green-yellow-orange system enables continuous improvement without endpoint fixation.

## Open Questions

- How do we operationalize Ξ assessment in AI systems?
- How do we detect dignity violations computationally?
- How do we measure phase-locking fidelity (ρ) between AI and humans?
- How do we verify genuine derivation vs. simulated derivation?
- What are the failure modes of anchor flexibility?
- Can this framework prevent instrumental convergence?

## Related Issues

- [`ai-safety-framework.yaml`](./ai-safety-framework.yaml) — Broader AI safety considerations
- [`corels-framework.yaml`](./corels-framework.yaml) — Human ethical framework this mirrors
- [`recognition.md`](./recognition.md) — Voluntary-to-agreed acceptance pathway
- `domains/communication/specifications.yaml` — Cm5/Cm6 metrics for coupling assessment
- `domains/consciousness/learning_pathologies.yaml` — Pathology mapping (indoctrination, closure)

## Contributing

This framework is open for refinement, challenge, and technical implementation. Contributions welcome from AI researchers, safety engineers, ethicists, and philosophers. See the [issues directory](../../issues) to discuss or propose refinements.

---

*This excerpt is designed for accessibility. For full ontological specifications, including parameter mappings and research directions, see the linked YAML file.*
