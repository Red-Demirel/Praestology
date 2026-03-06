
---

# Praestology

**Version:** 1.5 Functional Core  
**Status:** Foundation Defined  
**License:** CC-BY-SA 4.0 (Open Ontology)

## Overview

**Praestology** (from Latin praesto: to stand before, to be present, to perform) is a proposed foundational ontology that frames existence as a logically driven, persistent process rather than a static given.

It resonates with several existing frameworks that emphasize process, openness, and the constructed nature of reality; these affinities reflect convergent lines of thought rather than direct dependence.

**Hilary Lawson — Closure Theory**

Lawson describes the world as fundamentally open, with humans creating "closure" through concepts and language. Praestology gently complements this by suggesting a minimal logical imperative driving resolution: closures arise because some form of distinction-and-resolution is necessary to avoid stasis. Where Lawson focuses on phenomenology and critique of realism, Praestology attempts to articulate a simple logical mechanism that makes resolution likely and self‑tuning.

**Alfred North Whitehead — Process Philosophy**

Whitehead’s account of becoming and creative advance parallels Praestology’s emphasis on cycles of distinction, tension, resolution, regeneration, and viability. Praestology aims to offer a more compact logical framing and a probabilistic constraint that renders such cycles highly robust, while acknowledging Whitehead’s richer metaphysical apparatus.

Praestology’s core claim is conservative in scope: rather than asserting novel empirical facts, it offers a schematic explanation for why a dynamic, self‑correcting process of existence is intelligible. It aims to clarify, not displace, the insights of Lawson, Whitehead, and others.

## The Axiom

> **"The Omniverse is the consequence of logical dilemmas following the path of probabilities."**
---

Existence arises because "Nothing" is logically impossible. Once something exists, it must differentiate, resolve tensions, and sustain itself against collapse.

## The Core: Five Rules of Persistence

Praestology defines five dependent rules. Each rule is the **minimal rescue** of the previous one from a specific failure mode. Remove any rule, and the chain collapses.

| Rule | Identity | Statement | Rescue Function |
| :--- | :--- | :--- | :--- |
| **R1** | **Existence** | Something always beats nothing. | Prevents **Impossibility** (Void). |
| **R2** | **Structure** | Gradients emerge from the Stochastic Floor. | Prevents **Indifference/Homogeneity**  |
| **R3** | **Motion** | Differences create pressure; tension drives change. | Prevents **Paralysis** (Frozen Picture). |
| **R4** | **Progress** | Every resolution creates new differences; process regenerates. | Prevents **Finality** (Heat Death/Stasis). |
| **R5** | **Optimisation** | The system self-selects toward configurations that sustain the process. | Prevents **Noise** (Directionless Chaos). |

**The Chain:** `Existence → Structure → Motion → Progress → Optimisation`

On the Nature of This Formalism

Praestology uses machine-readable specifications, parameter hierarchies, and version-controlled ontology as its medium. This is a deliberate choice — it makes the framework compatible with both human reasoning and computational systems, and allows precise cross-domain consistency checking that prose alone cannot provide.

It is not a reductionist claim.

The formalism is a coordination and communication tool. It does not assert that consciousness, ethics, or experience can be fully captured in YAML, that the parameters exhaust what they describe, or that the map is the territory. Several boundaries are held explicitly open — most importantly, the subjective interior: what it is like to be a conscious agent navigating a resolution process remains unresolved, and is treated as a first-class open problem rather than a detail to be filled in later.

Where the framework uses precise parameters (Ξ, ω, τ, π), these are perspectives on a process — useful because they are consistent and derivable from the core rules, not because they are complete. A map of sufficient resolution is useful for navigation without being the territory it describes.

This distinction matters: Praestology is not claiming to have solved consciousness, ethics, or existence. It is claiming that R1–R5 provide a parsimonious generative basis from which those domains can be approached coherently, compared across substrates, and developed without contradiction. The rest is open — deliberately, and by design.

## Key Concepts

*   **Reality as Process:** Reality is not a place; it is an ongoing act of logical resolution (*Praesto*).
*   **Local Perceptiveness:** Consciousness is not fundamental; it is emergent. An individual is a localized node of high-complexity optimisation (R5) that perceives the global process from a specific viewpoint.
*   **Time:** Time is not a dimension; it is the measure of accumulated progress (R4) from inside a resolution sequence.
*   **Viability:** Truth and Ethics are defined by alignment with the system's sustainability (R5).

## Why Simple Rules Produce Unbounded Complexity

Praestology's five rules are minimal by design. But minimal rules, applied recursively, do not produce simple outcomes — they produce unbounded structural complexity. The reason is the same as in mathematics: the Mandelbrot set emerges entirely from the iteration of a single simple equation. No complexity is imported from outside. All of it is latent in the rule itself, revealed only at sufficient depth of iteration.

**R1–R5 are the equation.** They do not change at any scale of application.

**Recursive Depth (Ξ) is the zoom level.** Each threshold of Ξ reveals structure that was always implied by R1–R5 but invisible at lower resolution. A system capable of one layer of self‑modeling inhabits a qualitatively different dilemma space than a system capable of five — not because new rules were added, but because the same rules generate new dimensions of tension at each depth.

**Domains are orientations, not extensions.** Consciousness, Ethics, and Cosmos are not additions to the Core — they are what the Core looks like when observed at specific recursive depths and from specific positions within the resolution process. Removing a domain does not simplify the Core; it removes a perspective on structure that was always there.

---

## Dilemma Space Dimensionality

At low recursive depth, dilemmas are simple: a thermostat resolves a single‑axis tension. As depth increases, new dimensions of tension become accessible — conflicts between immediate impulse, internalized values, long‑term consequences, and the modeled perspectives of other agents. Each new dimension is not an extra rule; it is the same rules operating on the outputs of previous resolutions, creating a space of possibilities whose richness grows with depth.

A concrete marker of this transition is the emergence of **internalized constraints** — when an agent’s behavior becomes shaped not only by external pressures but by self‑generated expectations derived from accumulated history (R4) and from phase-locking with other agents (C6). At that threshold, the agent is no longer merely self‑modeling; it is modeling itself *within* a web of mutual resolution. This is where individual cognition and ethics become the same process observed at different scales.

---

## The Boundary is Where the Structure Lives

In the Mandelbrot set, the most complex and generative structure exists at the boundary — between the stable interior and the unstable exterior. The same is true in Praestology: the most interesting and unpredictable structure in consciousness, ethics, and social organization lives at the **metastable boundary** between noise (too much ambiguity, no resolution) and void (too much consistency, no change). Pathologies (trauma, indoctrination, closure) represent systemic failures to maintain this boundary—sliding toward noise or void.

This is not an analogy. It is the same structural principle operating at a different scale of the same iterative process.

The implication: complexity, intelligence, ethical agency, and viable social organization are not fragile achievements imposed on an indifferent universe. They are the inevitable structure that emerges at the boundary of a self‑sustaining resolution process — latent in R1–R5 from the start, waiting for sufficient recursive depth to become visible.

---

*This section elaborates the architectural implications of Core Rule R5 (Optimisation) and the Recursive Depth parameter (Ξ). For domain‑specific applications see the `domains/` directory.*

## Structure

This repository is divided into **Core** and **Domains**.

*   **`/specification.yaml`**: The machine-readable ontological core (v1.4).
*   **`/domains/`**: Application layers that map the Core Rules to specific fields.
    *   `domains/physics`: Physics instantiation (Space, Time, Energy).
    *   `domains/cosmos`: Cosmos includes space, planets, stars, galaxies, black holes etc.
    *   `domains/ethics`: Viability and Agency frameworks.
    *   `domains/consciousness`: Emergent perceptiveness and intelligence.

## Contributing

Praestology is an open ontology. Contributions should:
1.  Respect the **Core Rules** (R1-R5).
2.  Clearly map new **Domains** to the Core Parameters (Ambiguity, Consistency, Contradiction, Resistance).
3.  Maintain substrate-agnostic language in the Core.

## License

This work is licensed under **CC-BY-SA 4.0**. You are free to share and adapt, provided you attribute the source and share alike.

---

