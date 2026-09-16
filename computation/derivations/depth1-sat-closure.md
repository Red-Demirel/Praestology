# Depth-1 SAT Closure (`depth1-sat-closure.py`)

## Overview
This derivation script validates the foundational bivector encoding for **NCH Depth-1 SAT problems** using $Cl(3,0)$ Geometric Algebra. It proves that Boolean constraint satisfaction can be mapped into multivector phase evaluations where satisfying assignments evaluate to an exact zero-residual fixed point ($F[Q] = 0$).

## Key Specifications & Mechanics
* **Capacity Limit:** Depth 1 is bounded by the three orthogonal bivector planes of $Cl(3,0)$ ($e_{12}, e_{23}, e_{13}$). It natively processes instances with $\le 3$ variables[cite: 9]. Larger instances require lifting to higher depths ($d \ge 2$) or partitioning[cite: 9].
* **Clause Penalty Construction:** Violated clauses evaluate to non-zero multivector residuals built from negated literal bivector products[cite: 9]. Satisfied clauses generate zero penalty[cite: 9].
* **Closure Functional ($F[Q]$):** Sums the clause penalties and computes the scalar norm squared ($\|A\|^2 = \langle A \tilde{A} \rangle_0$)[cite: 9, 10]. 
  * $F[Q] = 0 \iff$ The assignment satisfies all clauses[cite: 9].
  * $F[Q] > 0 \iff$ The assignment produces phase friction (unsatisfied constraints)[cite: 9].

## Success Criteria & Test Battery
1. **Boolean SAT Parity:** `test_encoding_matches_boolean_sat()` runs a 10-case battery comparing $F[Q] = 0$ verdicts directly against brute-force Boolean SAT truth tables[cite: 9].
2. **Algebraic Cancellation:** `test_F_Q_cancellation()` confirms that satisfied configurations result in exact algebraic zero-sum cancellation across multivector components, rather than float approximations[cite: 9].

## Upstream & Downstream Dependencies
* **Upstream:** `computation/clifford_bridge.py` (provides $Cl(3,0)$ matrix operations and multivector products)[cite: 9, 10].
* **Downstream Target:** Validates the baseline mechanism for `SIM-SAT-D1`, paving the way for the Depth-2 lift and `libnch_phase_solvers` integration[cite: 9].
