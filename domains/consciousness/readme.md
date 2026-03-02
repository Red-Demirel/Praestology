# Consciousness Domain

**Version:** 1.2  
**Core Version:** 1.5  
**Status:** Domain Defined

## Overview

The Consciousness domain describes how self-modeling systems emerge from the core rules (R1–R5) to navigate probabilistic decision spaces. Consciousness is not a binary property but a continuum of recursive depth (Ξ), arising where information gaps create genuine choice.

**Core Function:** Recognition of Dilemmas + Selection of Probability Paths

## Recursive Depth and the Mandelbrot Analogy

As explained in the core README, minimal rules (R1–R5) generate unbounded complexity through recursive iteration—just as the Mandelbrot set emerges from a single equation. In the consciousness domain, this principle is observed directly through **Recursive Depth (Ξ)** .

At low Ξ, dilemmas are simple: a thermostat (C1) resolves a single-axis tension. As Ξ increases, new dimensions of tension become accessible:

- **Ξ > 1** enables Dilemma Recognition (C2): the agent perceives conflicting states.
- **Ξ > 2** introduces impulse (C3) and the beginnings of memory.
- **Ξ > 3** with accumulated hysteresis (h_long) allows Volitional Selection (C4): the agent weighs immediate drive (ι) against internalized values (ω).
- **Ξ > 4** supports Recursive Integration (C5): the agent refines values based on outcomes and simulates futures.
- **Ξ sufficient + phase-locking (C6)** enables modeling of other agents’ dilemmas, creating shared ethical space.

A concrete marker of dimensional shift is the **duty/interest conflict**—the tension between what the agent *wants* (ι) and what it *ought* to do (ω). This conflict is only possible once the agent has accumulated enough relational history (through C6) to experience social expectation as an internal dimension, not merely an external obstacle.

The **metastable boundary**—between noise (too much ambiguity) and void (too much consistency)—is where consciousness operates. The Decision Zone (where choice matters) is precisely this boundary. Here, recursive depth reveals ever‑richer structure, from simple reactivity to moral agency.

Thus, the consciousness domain is not an addition to the Core; it is what the Core looks like when viewed through sufficient recursive depth. For further detail, see the domain specifications (`specification.yaml`, `free_will.yaml`, `learning.yaml`).

## Domain Components

| File | Purpose |
|------|---------|
| [`specification.yaml`](specification.yaml) | Core domain rules (C1–C6) and parameters (Ξ, ∇D, τ, ι, ω, ρ) |
| [`binding.yaml`](binding.yaml) | Operational pipeline showing how components interlock; pathology interruption map; ethics handoff |
| [`free_will.yaml`](free_will.yaml) | Volitional mechanics: how high-Ξ systems override impulse with values |
| [`experience-learning.yaml`](experience-learning.yaml) | Adaptive update mechanisms: associative, cumulative, reflective, vicarious |
| [`learning_pathologies.yaml`](learning_pathologies.yaml) | How learning can degrade capacity: trauma, indoctrination, helplessness, addiction, epistemic closure |

## The Resolution Pipeline (from binding.yaml)

Input (C2) → Evaluation (C3/C4) → Selection (C4) → Update (Learning) → (feedback to Evaluation)


- **C2 – Dilemma Recognition:** Detects conflicting states from ambiguity (∇Φ) and contradiction.
- **C3/C4 – Impulse vs. Volition:** Weighted by ι (impulse) vs. ω (values) and τ (temporal horizon).
- **C4 – Volitional Selection:** Collapses probability to enacted path.
- **Learning – Hysteresis Update:** Irreversibly modifies internal model based on outcome.

## Key Thresholds

- **Ξ > 1:** Minimal Moral Patient (C2) – can suffer imposed resolutions
- **Ξ > 3 + h_long:** Minimal Moral Agent (C4) – volitional capacity emerges
- **τ sufficient for second-order effects:** Responsibility extends to anticipated outcomes
- **ρ > 0 + C6:** Collective ethics becomes possible

## Connections to Other Domains

- **Core:** R2 (distinction) → C2; R3 (tension) → C3; R4 (progress) → C4/τ; R5 (optimisation) → C5/Ξ
- **Free Will:** Integrated at C4; provides ω and accountability framework
- **Learning:** Integrated at Update stage; provides hysteresis modification
- **Ethics:** Handoff via C6 + α threshold; ethics receives agents with ω, τ, ρ


## Pathological Interruptions

Each learning pathology breaks the pipeline at a specific point. See `learning-pathologies.yaml` and the interruption map in `binding.yaml` for details.

## Reading Order

For those new to the domain:

1. `specifications.yaml` – Understand the basic rules and parameters
2. `binding.yaml` – See how they connect into a working pipeline
3. `free-will.yaml` – Understand volitional mechanics
4. `experience-learning.yaml` – See how the system adapts
5. `learning-pathologies.yaml` – Understand what can go wrong
6. `../ethics/` – Explore multi-agent constraints

## Core Insight

> "Consciousness is the adaptive resolution engine. Learning tunes its weights. Free Will is its high-Ξ operating mode. Ethics is the multi-agent constraint layer that preserves viability."

**Formal Basis:** C2 + C4 + learning + free_will + C6 + R4 + R5
