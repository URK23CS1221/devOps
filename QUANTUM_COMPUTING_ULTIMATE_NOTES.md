# QUANTUM COMPUTING — ULTIMATE EXAM NOTES
### Based on Syllabus + Teacher Notes (John Watrous, IBM)
### Beginner-Friendly | Topic by Topic | Exam-Ready

---

# HOW TO USE THESE NOTES
- Read one module at a time
- Understand the concept first, then read the math
- Every topic has: Simple Explanation → Math → Example → Why It Matters
- At the end: Quick revision tables and exam answer templates

---

---

# MODULE 1 — INTRODUCTION TO QUANTUM MECHANICS
## (7 Hours)

---

## 1.1 What is Quantum Mechanics? (Start here)

Classical physics (Newton's laws) works for big things like balls and cars.
Quantum mechanics works for tiny things — electrons, photons, atoms.

Key differences from classical:
- A particle can be in TWO states at once (superposition)
- Particles can be "spookily connected" even far apart (entanglement)
- Measuring a quantum state CHANGES it
- Nature is fundamentally probabilistic at small scales

---

## 1.2 Mathematical Tools You Need

### Bra-Ket Notation (Dirac Notation)

This is the language of quantum mechanics. Learn it like a language.

| Symbol     | Name      | What it is                    | Example           |
|------------|-----------|-------------------------------|-------------------|
| |ψ⟩        | "Ket"     | Column vector = quantum state | |0⟩ = [1, 0]^T   |
| ⟨ψ|        | "Bra"     | Row vector (conjugate of ket) | ⟨0| = [1, 0]     |
| ⟨φ|ψ⟩     | "Bracket" | Inner product = a number      | ⟨0|0⟩ = 1        |
| |φ⟩⟨ψ|    | Outer product | A matrix              | |0⟩⟨0| = [[1,0],[0,0]] |

Standard basis for a qubit:
- |0⟩ = [1, 0]^T  ← column vector, represents classical "0"
- |1⟩ = [0, 1]^T  ← column vector, represents classical "1"

⟨0|0⟩ = 1, ⟨1|1⟩ = 1, ⟨0|1⟩ = 0, ⟨1|0⟩ = 0
(Standard basis is orthonormal)


### Inner Product

For two vectors |ψ⟩ = Σ αₐ|a⟩ and |φ⟩ = Σ βₐ|a⟩:

⟨ψ|φ⟩ = Σ αₐ* βₐ   (conjugate of first times second, summed)

Key properties:
1. ⟨ψ|φ⟩* = ⟨φ|ψ⟩  (conjugate symmetry)
2. ⟨ψ|α₁φ₁ + α₂φ₂⟩ = α₁⟨ψ|φ₁⟩ + α₂⟨ψ|φ₂⟩  (linear in second argument)
3. ⟨ψ|ψ⟩ ≥ 0, equals 0 only if |ψ⟩ = 0
4. ||ψ⟩||² = ⟨ψ|ψ⟩   (norm squared)

Example:
|φ⟩ = (1/2)|0⟩ + (√3/2)|1⟩
|ψ⟩ = (1/√2)|0⟩ − (1/√2)|1⟩
⟨ψ|φ⟩ = (1/√2)*(1/2) + (−1/√2)*(√3/2) = (1−√3)/(2√2) ≈ −0.26


### Cauchy-Schwarz Inequality

|⟨ψ|φ⟩|² ≤ ⟨ψ|ψ⟩ · ⟨φ|φ⟩

Or equivalently: |⟨ψ|φ⟩| ≤ ||ψ⟩|| · ||φ⟩||

Equality holds ONLY when |ψ⟩ and |φ⟩ are linearly dependent (one is a scalar multiple of the other).

EXAM SIGNIFICANCE: This is the mathematical foundation of Heisenberg's Uncertainty Principle. It says you cannot simultaneously know two incompatible observables to arbitrary precision. The "inner product" between two quantum states limits how much information you can extract.


### Orthogonality and Orthonormality

Two vectors are orthogonal if: ⟨ψ|φ⟩ = 0

A set {|ψ₁⟩, ..., |ψₘ⟩} is orthonormal if:
⟨ψⱼ|ψₖ⟩ = 1 if j=k, and 0 if j≠k

An orthonormal BASIS is an orthonormal set that spans the whole space.

Examples of orthonormal bases for 1 qubit:
- Standard basis: {|0⟩, |1⟩}
- Hadamard basis: {|+⟩, |−⟩} where |+⟩ = (|0⟩+|1⟩)/√2 and |−⟩ = (|0⟩−|1⟩)/√2
- Bell basis: {|φ⁺⟩, |φ⁻⟩, |ψ⁺⟩, |ψ⁻⟩} for 2 qubits


### Gram-Schmidt Process

PROBLEM: Given any set of vectors, how do you make them orthonormal?
SOLUTION: Gram-Schmidt process.

Step-by-step:
Given vectors v₁, v₂, v₃, ...

Step 1: e₁ = v₁ / ||v₁||   (normalize first vector)

Step 2: u₂ = v₂ − ⟨e₁|v₂⟩e₁   (subtract projection onto e₁)
        e₂ = u₂ / ||u₂||        (normalize)

Step 3: u₃ = v₃ − ⟨e₁|v₃⟩e₁ − ⟨e₂|v₃⟩e₂
        e₃ = u₃ / ||u₃||

EXAM SIGNIFICANCE: Quantum state spaces require orthonormal bases. If you start with any set of linearly independent vectors (like eigenvectors of a messy operator), Gram-Schmidt gives you a proper orthonormal basis. This ensures quantum states and measurements are mathematically consistent.


### Tensor Product (VERY IMPORTANT for multiple qubits)

For two column vectors |φ⟩ = [α₁, α₂]^T and |ψ⟩ = [β₁, β₂]^T:

|φ⟩ ⊗ |ψ⟩ = [α₁β₁, α₁β₂, α₂β₁, α₂β₂]^T   (4-dimensional vector)

In Dirac notation: |φ⟩ ⊗ |ψ⟩ = |φ⟩|ψ⟩ = |φψ⟩

Properties of tensor products:
- (|φ₁⟩ + |φ₂⟩) ⊗ |ψ⟩ = |φ₁⟩⊗|ψ⟩ + |φ₂⟩⊗|ψ⟩   (bilinear)
- (α|φ⟩) ⊗ |ψ⟩ = α(|φ⟩ ⊗ |ψ⟩)
- Scalar "floats freely": (α|φ⟩)⊗|ψ⟩ = |φ⟩⊗(α|ψ⟩) = α|φ⟩⊗|ψ⟩

For standard basis: |a⟩ ⊗ |b⟩ = |ab⟩

Example:
|0⟩ ⊗ |1⟩ = |01⟩ = [0, 1, 0, 0]^T
|1⟩ ⊗ |0⟩ = |10⟩ = [0, 0, 1, 0]^T

For compound system (X,Y) with classical state sets Σ and Γ:
Classical states = Σ × Γ = {(a,b) : a∈Σ, b∈Γ}

Example: 2 qubits → states are {00, 01, 10, 11}
Example: 3 qubits → states are {000, 001, 010, 011, 100, 101, 110, 111}

Tensor product of matrices:
(M ⊗ N)(|φ⟩ ⊗ |ψ⟩) = (M|φ⟩) ⊗ (N|ψ⟩)
→ Each operation acts on its own system independently


### Hermitian Operators (Observables)

An operator A is Hermitian if: A = A†   (equals its conjugate transpose)

A† means: transpose the matrix, then take complex conjugate of every entry.

WHY IT MATTERS: Physical observables (things you can measure) are represented by Hermitian operators. Hermitian operators have REAL eigenvalues — which makes sense because measurement results must be real numbers.

Example — Pauli matrices (all Hermitian AND unitary):

X = [[0, 1], [1, 0]]    (also written σₓ)
Y = [[0, -i], [i, 0]]   (also written σᵧ)
Z = [[1, 0], [0, -1]]   (also written σᵤ)
I = [[1, 0], [0, 1]]    (identity)

Check that X is Hermitian: X† = [[0,1],[1,0]]* transposed = [[0,1],[1,0]] = X ✓

Properties of Pauli matrices:
- X² = Y² = Z² = I
- XY = iZ,  YZ = iX,  ZX = iY
- XY ≠ YX  (they do NOT commute)


### Unitary Operators (Quantum Gates)

An operator U is unitary if: U†U = UU† = I

This means: U† = U⁻¹   (inverse equals conjugate transpose)

WHY IT MATTERS:
- All quantum gates must be unitary
- Unitary operations preserve inner products: ⟨Uφ|Uψ⟩ = ⟨φ|ψ⟩
- Unitary operations preserve norms (probabilities stay summing to 1)
- Reversible: you can always undo a unitary operation

UNITARY ↔ ORTHONORMAL COLUMNS/ROWS:
A matrix U is unitary if and only if:
- Its COLUMNS form an orthonormal basis, AND
- Its ROWS form an orthonormal basis

Tensor product of unitary operations:
If U acts on X and V acts on Y independently, combined action = U ⊗ V


### Projection Operators

A matrix Π is a projection if:
1. Π† = Π   (Hermitian)
2. Π² = Π   (idempotent — applying it twice = applying once)

If |ψ⟩ is a unit vector, then Π = |ψ⟩⟨ψ| is a projection.

Check: (|ψ⟩⟨ψ|)² = |ψ⟩⟨ψ|ψ⟩⟨ψ| = |ψ⟩(1)⟨ψ| = |ψ⟩⟨ψ| ✓

Completeness relation (very important):
If {|ψ₁⟩, ..., |ψₙ⟩} is an orthonormal basis, then:
Σₖ |ψₖ⟩⟨ψₖ| = I   (identity)

Examples:
P₀ = |0⟩⟨0| = [[1,0],[0,0]]
P₁ = |1⟩⟨1| = [[0,0],[0,1]]
P₀ + P₁ = I ✓


### Commutators

[A, B] = AB − BA

If [A, B] = 0: A and B commute → can be measured simultaneously
If [A, B] ≠ 0: A and B don't commute → cannot be measured simultaneously with arbitrary precision

Pauli commutators:
[X, Y] = 2iZ
[Y, Z] = 2iX
[Z, X] = 2iY

Position-momentum commutator:
[x̂, p̂] = iℏ  ← this is why position and momentum can't both be known exactly


### Heisenberg Uncertainty Principle

ΔA · ΔB ≥ ½|⟨[A, B]⟩|

For position and momentum:
Δx · Δp ≥ ℏ/2

IMPORTANT: This is NOT about measurement instrument imprecision. It is a fundamental property of nature. Even a perfect measurement cannot know both position and momentum exactly — because they don't commute.

DERIVATION IDEA: Uses Cauchy-Schwarz inequality on the quantum state.


### Polar Decomposition and Singular Values

Any matrix M can be written as: M = UJ

Where:
- U = unitary matrix
- J = positive semidefinite matrix = √(M†M)

Singular values of M = square roots of eigenvalues of M†M = {σ₁, σ₂, ..., σₙ}

In QM context:
- Polar decomposition shows how quantum operations can be broken into a "rotation" (U) and a "stretching" (J)
- Singular values tell us the "amount" of transformation in each direction
- Used to characterize quantum channels and state transformations
- Helps understand mixed states and the structure of quantum operations


---

## 1.3 Postulates of Quantum Mechanics

MEMORIZE THESE — they are the foundation of everything.

### Postulate 1 — State Space
Every quantum system is associated with a complex vector space (Hilbert space). The system's state is described by a unit vector |ψ⟩ in that space.

For a qubit: |ψ⟩ = α|0⟩ + β|1⟩, where |α|² + |β|² = 1

### Postulate 2 — Evolution
A closed (isolated) quantum system evolves by a unitary operator U:
|ψ'⟩ = U|ψ⟩

U must satisfy U†U = I. Different unitary operators correspond to different physical processes (gates).

### Postulate 3 — Measurement
When we perform a measurement described by operators {Mₘ}, where Σₘ Mₘ†Mₘ = I:

Probability of result m: P(m) = ⟨ψ|Mₘ†Mₘ|ψ⟩

Post-measurement state: Mₘ|ψ⟩ / √P(m)

For standard basis measurement:
P(measuring |0⟩) = |α|²
P(measuring |1⟩) = |β|²
After measuring 0: state collapses to |0⟩

### Postulate 4 — Composite Systems
If system A and system B are separate, the combined state space = tensor product.
State of (A,B) = |ψ_A⟩ ⊗ |ψ_B⟩  (if they're independent/unentangled)

If entangled, the combined state CANNOT be written as a tensor product.


---

## 1.4 Quantum Superposition Principle

A qubit can be in state:
|ψ⟩ = α|0⟩ + β|1⟩

α and β are complex amplitudes. They satisfy: |α|² + |β|² = 1

|α|² = probability of getting 0 on measurement
|β|² = probability of getting 1 on measurement

SUPERPOSITION ≠ "both at once":
More precisely: the qubit is in a state where measurement outcome is probabilistic.
Before measurement: undefined which state.
After measurement: collapses to |0⟩ or |1⟩.

Example:
|+⟩ = (1/√2)|0⟩ + (1/√2)|1⟩
|α|² = 1/2, |β|² = 1/2 → 50% each outcome

|−⟩ = (1/√2)|0⟩ − (1/√2)|1⟩
Same probabilities, but different phase (which matters for interference)


---

## 1.5 Bloch Sphere Representation

Any single qubit state can be written:
|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩

Parameters:
- θ (theta): polar angle, 0 ≤ θ ≤ π
- φ (phi): azimuthal angle, 0 ≤ φ < 2π

Key points on the sphere:
- North pole (θ=0): |0⟩
- South pole (θ=π): |1⟩
- Equator (θ=π/2, φ=0): |+⟩ = (|0⟩+|1⟩)/√2
- Equator (θ=π/2, φ=π): |−⟩ = (|0⟩-|1⟩)/√2

WHY USEFUL:
- Every possible qubit state is one point on this sphere
- Quantum gates = rotations of the sphere
- Measurement collapses the state to north or south pole
- Visualizes the difference between global and relative phase

GLOBAL vs RELATIVE PHASE:
e^(iγ)|ψ⟩ = |ψ⟩ physically (global phase unobservable)
α|0⟩ + e^(iφ)β|1⟩ ← relative phase φ IS observable (affects interference)


---

## 1.6 Density Operator (Mixed States)

PURE STATE: We know the exact state |ψ⟩.
Density operator: ρ = |ψ⟩⟨ψ|

MIXED STATE: Statistical uncertainty — we know it's one of several states with certain probabilities.
Density operator: ρ = Σᵢ pᵢ |ψᵢ⟩⟨ψᵢ|

where pᵢ are classical probabilities (Σpᵢ = 1), not quantum amplitudes.

Properties of any valid density operator:
1. Tr(ρ) = 1   (trace = 1)
2. ρ = ρ†      (Hermitian)
3. ρ ≥ 0       (positive semidefinite — all eigenvalues ≥ 0)

To check if state is pure or mixed:
- Pure: Tr(ρ²) = 1
- Mixed: Tr(ρ²) < 1

Example of mixed state:
Equal mixture of |0⟩ and |1⟩:
ρ = (1/2)|0⟩⟨0| + (1/2)|1⟩⟨1|
  = (1/2)[[1,0],[0,0]] + (1/2)[[0,0],[0,1]]
  = (1/2)[[1,0],[0,1]]
  = I/2

This is the maximally mixed state.
Tr(ρ²) = Tr(I/4) = 1/2 < 1 → mixed ✓

WHY IT MATTERS:
Mixed states arise in:
- Open quantum systems (interacting with environment)
- Subsystems of entangled systems
- When we have incomplete knowledge of preparation
- Quantum error correction analysis


---

---

# MODULE 2 — QUANTUM GATES AND CIRCUITS
## (7 Hours)

---

## 2.1 Spin and Qubits

SPIN: Particles have intrinsic angular momentum called spin.
Electron spin-1/2 has two states:
- Spin-up: |↑⟩ = |0⟩
- Spin-down: |↓⟩ = |1⟩

QUBIT: Quantum bit. The basic unit of quantum information.
|ψ⟩ = α|0⟩ + β|1⟩,  |α|² + |β|² = 1

Classical bit vs Qubit:
- Classical bit: either 0 OR 1 (never both)
- Qubit: α|0⟩ + β|1⟩ (superposition until measured)

Physical implementations of qubits:
- Electron spin
- Photon polarization
- Superconducting circuits (like IBM's quantum computers)
- Trapped ions


---

## 2.2 Single Qubit Gates

### Pauli Gates (MEMORIZE)

Pauli-X (NOT gate, bit flip):
X = [[0, 1], [1, 0]]
X|0⟩ = |1⟩,  X|1⟩ = |0⟩

Pauli-Y:
Y = [[0, -i], [i, 0]]
Y|0⟩ = i|1⟩,  Y|1⟩ = -i|0⟩

Pauli-Z (phase flip):
Z = [[1, 0], [0, -1]]
Z|0⟩ = |0⟩,  Z|1⟩ = -|1⟩

Identity:
I = [[1, 0], [0, 1]]
I|ψ⟩ = |ψ⟩

Properties (ALL Pauli gates):
- Hermitian: P† = P
- Unitary: PP† = I
- Self-inverse: P² = I
- Anticommute: XY = iZ = -YX

### Hadamard Gate (H)

H = (1/√2)[[1, 1], [1, -1]]

Action:
H|0⟩ = (1/√2)(|0⟩ + |1⟩) = |+⟩
H|1⟩ = (1/√2)(|0⟩ − |1⟩) = |−⟩

H|+⟩ = |0⟩
H|−⟩ = |1⟩

H² = I  (Hadamard is its own inverse)

WHY IMPORTANT: Creates superposition from a classical state. Used at the start of almost every quantum algorithm.

### Phase Gate (S) and T Gate

S = [[1, 0], [0, i]]     (phase gate, π/2 rotation)
S|0⟩ = |0⟩,  S|1⟩ = i|1⟩

T = [[1, 0], [0, e^(iπ/4)]]     (π/8 gate)
T|0⟩ = |0⟩,  T|1⟩ = e^(iπ/4)|1⟩

Note: T² = S,  S² = Z

T gate is important because: {H, T, CNOT} form a universal gate set for quantum computing. Without T gate (non-Clifford), you can't achieve quantum speedup (see Gottesman-Knill theorem later).

### Rotation Gates

Rₓ(θ) = cos(θ/2)I − i·sin(θ/2)X = [[cos(θ/2), -i·sin(θ/2)], [-i·sin(θ/2), cos(θ/2)]]
Rᵧ(θ) = cos(θ/2)I − i·sin(θ/2)Y = [[cos(θ/2), -sin(θ/2)], [sin(θ/2), cos(θ/2)]]
R_z(θ) = cos(θ/2)I − i·sin(θ/2)Z = [[e^(-iθ/2), 0], [0, e^(iθ/2)]]

These are rotations on the Bloch sphere by angle θ around x, y, z axes.


---

## 2.3 Multiple Qubit Gates

### CNOT Gate (Controlled-NOT)

CNOT acts on 2 qubits: Control + Target
Rule: If control = |1⟩, flip target. If control = |0⟩, do nothing.

In basis {|00⟩, |01⟩, |10⟩, |11⟩}:

CNOT = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 1, 0]]

Action:
CNOT|00⟩ = |00⟩
CNOT|01⟩ = |01⟩
CNOT|10⟩ = |11⟩
CNOT|11⟩ = |10⟩

Mathematical definition:
CNOT = |0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ X

WHY IMPORTANT: Creates entanglement. Combined with H, it creates Bell states.

Example — Creating Bell state:
Start: |00⟩
Apply H to first qubit: (1/√2)(|0⟩+|1⟩) ⊗ |0⟩ = (1/√2)(|00⟩+|10⟩)
Apply CNOT: (1/√2)(|00⟩+|11⟩) = |Φ⁺⟩ ← Bell state!

### Toffoli Gate (CCNOT)

3-qubit gate: 2 control qubits + 1 target.
Flips target ONLY when BOTH controls are |1⟩.

Truth table:
|000⟩ → |000⟩
|001⟩ → |001⟩
|010⟩ → |010⟩
|011⟩ → |011⟩
|100⟩ → |100⟩
|101⟩ → |101⟩
|110⟩ → |111⟩  ← target flipped
|111⟩ → |110⟩  ← target flipped

Mathematical definition:
Toffoli = |0⟩⟨0| ⊗ I ⊗ I + |1⟩⟨1| ⊗ (|0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ X)

WHY IMPORTANT: Toffoli is universal for classical computing. Any classical circuit can be built from Toffoli gates.

### SWAP Gate

Swaps two qubits:
SWAP|ab⟩ = |ba⟩

SWAP = [[1,0,0,0], [0,0,1,0], [0,1,0,0], [0,0,0,1]]

Action on Bell states:
SWAP|φ⁺⟩ = |φ⁺⟩
SWAP|φ⁻⟩ = |φ⁻⟩
SWAP|ψ⁺⟩ = |ψ⁺⟩
SWAP|ψ⁻⟩ = -|ψ⁻⟩

### Fredkin Gate (Controlled-SWAP)

3-qubit gate: 1 control + 2 targets.
SWAPS the two target qubits if control = |1⟩.
Also called controlled-SWAP.

### Controlled-U Gate (General)

Any unitary U can be "controlled":
Controlled-U = |0⟩⟨0| ⊗ I + |1⟩⟨1| ⊗ U

In block matrix form:
Controlled-U = [[I, 0], [0, U]]

Examples:
- Controlled-X = CNOT
- Controlled-Z = CZ gate
- Controlled-H = CH gate

Phase kickback (KEY CONCEPT for algorithms):
If |ψ⟩ is an eigenvector of U with eigenvalue e^(iφ):
U|ψ⟩ = e^(iφ)|ψ⟩

Then for controlled-U with control in superposition:
(1/√2)(|0⟩+|1⟩) ⊗ |ψ⟩
→ (1/√2)(|0⟩ + e^(iφ)|1⟩) ⊗ |ψ⟩

The PHASE KICKED BACK to the control qubit! This is the magic behind most quantum algorithms.


---

## 2.4 Quantum Circuit Model

Rules for quantum circuits:
- Horizontal lines = qubits (time flows LEFT to RIGHT)
- Boxes/symbols on lines = gates
- Measurement = meter symbol (⊠ or M in a box)
- Circuit is always ACYCLIC (no feedback loops)
- Information flows one direction only

Convention (Qiskit/IBM): qubits ordered bottom-to-top in diagram = left-to-right in tensor product.

Example circuit for creating |Φ⁺⟩ from |00⟩:
|0⟩ ─── H ─── ●  ───
                  |
|0⟩ ─────────── ⊕ ───

(H on top, CNOT with top as control)

### No-Cloning Theorem

STATEMENT: It is impossible to create an exact copy of an unknown quantum state.

PROOF: Suppose a cloning machine U exists such that:
U(|ψ⟩|0⟩) = |ψ⟩|ψ⟩  for any |ψ⟩

Take two states |φ⟩ and |ψ⟩:
U(|φ⟩|0⟩) = |φ⟩|φ⟩
U(|ψ⟩|0⟩) = |ψ⟩|ψ⟩

Take inner product of both sides:
⟨φ|ψ⟩⟨0|0⟩ = ⟨φ|ψ⟩²

So: ⟨φ|ψ⟩ = ⟨φ|ψ⟩²

This means ⟨φ|ψ⟩ = 0 or ⟨φ|ψ⟩ = 1 — only orthogonal or identical states can be cloned. Arbitrary states cannot. CONTRADICTION. ∎

WHY IT MATTERS: No-cloning ensures quantum cryptography is secure. It also means quantum information is fundamentally different from classical information (which can always be copied).


---

## 2.5 Measurements in Detail

### Standard Basis Measurement

Measure |ψ⟩ = Σₐ αₐ|a⟩:
- Probability of outcome a: |αₐ|² = |⟨a|ψ⟩|²
- Post-measurement state: |a⟩ (state collapses to that basis vector)

### Projective Measurement

Collection {Πₘ} where Σₘ Πₘ = I and each Πₘ is a projection.

When measured on state |ψ⟩:
1. Probability of outcome m: P(m) = ||Πₘ|ψ⟩||² = ⟨ψ|Πₘ|ψ⟩
2. Post-measurement state: Πₘ|ψ⟩ / ||Πₘ|ψ⟩||

Standard basis measurement is a special case with Πₐ = |a⟩⟨a|.

### Measuring Part of a Compound System

For state |ψ⟩ = Σₐ |a⟩ ⊗ |φₐ⟩ (written to group by first system):

If we measure only the first system (X):
- Probability of outcome a: P(a) = |||φₐ⟩||² = Σ_b |αₐb|²
- If outcome is a, state becomes: |a⟩ ⊗ (|φₐ⟩ / |||φₐ⟩||)

This is how entanglement creates correlations — measuring one qubit instantly affects what we know about the other.

Example:
State: |ψ⟩ = (1/√2)|00⟩ + (1/√2)|11⟩ = |Φ⁺⟩
Written as: (1/√2)|0⟩⊗|0⟩ + (1/√2)|1⟩⊗|1⟩
Measure first qubit:
- P(0) = ||(1/√2)|0⟩||² = 1/2 → state becomes |00⟩
- P(1) = ||(1/√2)|1⟩||² = 1/2 → state becomes |11⟩

### POVMs (Positive Operator-Valued Measures)

More general than projective measurements.
A POVM is a set of positive operators {Mₘ} satisfying Σₘ Mₘ = I.

Key difference from projective measurement:
- POVM elements don't need to be projectors (don't need Mₘ² = Mₘ)
- More outcomes are possible
- Used when we want to extract maximum information

Use case: Discriminating between two non-orthogonal states.

| Feature | Projective Measurement | POVM |
|---------|----------------------|------|
| Operators | Projectors (Π² = Π) | Positive operators (M ≥ 0) |
| Orthogonal? | Yes | Not necessarily |
| Post-state | Well-defined | May not preserve state cleanly |
| Use | Standard measurement | Optimal state discrimination |

Implementing POVMs: Any POVM can be implemented by adding ancilla qubits and doing a projective measurement on the larger system.

EXAM TIP for POVM design questions:
To discriminate states |ψ₁⟩ and |ψ₂⟩:
- If they're orthogonal: simple projective measurement works perfectly
- If non-orthogonal: POVM with 3 outcomes can work — one outcome is "don't know", but the other two give certainty


---

---

# MODULE 3 — ENTANGLEMENT AND QUANTUM PROTOCOLS
## (7 Hours)

---

## 3.1 Bell States

The four Bell states (maximally entangled 2-qubit states):

|Φ⁺⟩ = (1/√2)(|00⟩ + |11⟩)
|Φ⁻⟩ = (1/√2)(|00⟩ − |11⟩)
|Ψ⁺⟩ = (1/√2)(|01⟩ + |10⟩)
|Ψ⁻⟩ = (1/√2)(|01⟩ − |10⟩)

The Bell basis {|Φ⁺⟩, |Φ⁻⟩, |Ψ⁺⟩, |Ψ⁻⟩} is an orthonormal basis for 2-qubit space.

Creating |Φ⁺⟩:
1. Start with |00⟩
2. Apply H to first qubit: (1/√2)(|0⟩+|1⟩)|0⟩ = (1/√2)(|00⟩+|10⟩)
3. Apply CNOT: (1/√2)(|00⟩+|11⟩) = |Φ⁺⟩

ENTANGLED means: cannot be written as |a⟩⊗|b⟩ for any single-qubit states |a⟩ and |b⟩.

PROOF that |Φ⁺⟩ is entangled:
Suppose (1/√2)(|00⟩+|11⟩) = |φ⟩⊗|ψ⟩
Then: ⟨0|φ⟩⟨1|ψ⟩ = ⟨01|φ⊗ψ⟩ = 0
So either ⟨0|φ⟩=0 or ⟨1|ψ⟩=0
But: ⟨0|φ⟩⟨0|ψ⟩ = 1/√2 ≠ 0, so ⟨0|φ⟩ ≠ 0
And: ⟨1|φ⟩⟨1|ψ⟩ = 1/√2 ≠ 0, so ⟨1|ψ⟩ ≠ 0
CONTRADICTION. ∎

Other multi-qubit entangled states:
GHZ state (3 qubits): (1/√2)(|000⟩ + |111⟩)
W state (3 qubits): (1/√3)(|001⟩ + |010⟩ + |100⟩)


---

## 3.2 Bell Inequalities (CHSH Game)

The CHSH game is a way to test whether quantum mechanics violates classical predictions.

SETUP:
- Two players: Alice and Bob
- A referee gives Alice question x ∈ {0,1} and Bob question y ∈ {0,1}
- Alice answers a ∈ {0,1}, Bob answers b ∈ {0,1}
- They WIN if: a ⊕ b = x ∧ y  (XOR of answers = AND of questions)
- No communication allowed once game starts

WINNING CONDITION TABLE:
(x,y) | Required: a⊕b
(0,0) | a=b
(0,1) | a=b
(1,0) | a=b
(1,1) | a≠b

CLASSICAL LIMIT:
No deterministic strategy wins all 4 cases (check: need a(0)⊕b(0)=0, a(0)⊕b(1)=0, a(1)⊕b(0)=0, a(1)⊕b(1)=1 — adding these: 0=1, contradiction).
Best classical strategy wins 3/4 = 75% of the time.
Any probabilistic classical strategy can be viewed as a distribution over deterministic ones → still max 75%.

QUANTUM STRATEGY:
Alice and Bob share a Bell state |Φ⁺⟩.
Each applies a rotation based on their question, then measures.

Alice's rotations: U₀ if x=0, U_{π/4} if x=1
Bob's rotations: U_{π/8} if y=0, U_{-π/8} if y=1

QUANTUM WIN RATE: (2+√2)/4 ≈ 85.36% > 75%

SIGNIFICANCE:
- This EXPERIMENTALLY PROVES quantum mechanics is not explainable by "local hidden variables"
- The 2022 Nobel Prize in Physics was awarded for experiments confirming this (Aspect, Clauser, Zeilinger)
- Real-world implication: entanglement is a genuine resource, not just lack of knowledge


---

## 3.3 Monogamy of Entanglement

STATEMENT: If qubits A and B are maximally entangled, then A cannot be entangled with any third qubit C.

Intuition: Entanglement is like a "bond" — if A is fully bonded to B, it has nothing left for C.

MATHEMATICAL EXPRESSION (for qubits):
If (A,B) share maximal entanglement, entanglement(A,C) = 0.

More generally: E(A:B) + E(A:C) ≤ E(A:BC)

WHERE IT MATTERS:
- Quantum key distribution: If Eve intercepts and entangles with Alice's qubit, it reduces entanglement between Alice and Bob → detectable
- Quantum error correction: Cannot have unwanted entanglement with environment if qubits are entangled with each other
- No-cloning theorem: Another way to see why you can't clone — cloning would violate monogamy


---

## 3.4 Superdense Coding

GOAL: Alice wants to send 2 classical bits to Bob, but can only send 1 qubit.
RESOURCE: Alice and Bob share 1 e-bit (Bell pair |Φ⁺⟩) beforehand.
RESULT: 1 qubit + 1 ebit → 2 classical bits (impossible without ebit)

HOLEVO'S THEOREM says 1 qubit can carry at most 1 classical bit alone. Superdense coding beats this using entanglement.

PROTOCOL:
Pre-shared: |Φ⁺⟩ = (1/√2)(|00⟩+|11⟩). Alice has qubit A, Bob has qubit B.

Alice applies one operation to HER qubit A only:

| Bits (a,b) to send | Alice applies | Resulting joint state |
|---------------------|---------------|----------------------|
| (0,0)               | I (nothing)   | |Φ⁺⟩ = (1/√2)(|00⟩+|11⟩) |
| (0,1)               | Z             | |Φ⁻⟩ = (1/√2)(|00⟩-|11⟩) |
| (1,0)               | X             | |Ψ⁺⟩ = (1/√2)(|01⟩+|10⟩) |
| (1,1)               | iY (=ZX)      | |Ψ⁻⟩ = (1/√2)(|01⟩-|10⟩) |

Alice sends her qubit A to Bob.
Bob now has BOTH qubits.
Bob performs Bell measurement (CNOT then H on first qubit, then measure both):
- Gets outcome (a,b) perfectly.

WHY IT WORKS: The 4 Bell states are orthogonal → perfectly distinguishable.

EQUIVALENCE:
1 qubit of communication + 1 ebit ↔ 2 classical bits


---

## 3.5 Quantum Teleportation

GOAL: Alice wants to transmit an unknown quantum state |ψ⟩ = α|0⟩+β|1⟩ to Bob.
She can only send CLASSICAL bits (she doesn't know α and β).
RESOURCE: Pre-shared Bell pair |Φ⁺⟩.

WHY IT'S INTERESTING: The state itself (not the qubit) is teleported. Original is destroyed (No-cloning consistent).

SETUP:
- Alice has qubit Q in state |ψ⟩ (she wants to teleport)
- Alice has qubit A (her half of Bell pair)
- Bob has qubit B (his half of Bell pair)
- (A,B) in state |Φ⁺⟩

PROTOCOL STEPS:
1. Alice applies CNOT with Q as control, A as target
2. Alice applies H to Q
3. Alice measures both Q and A → gets classical bits (b, a) ∈ {00,01,10,11}
4. Alice sends (a,b) to Bob via classical channel
5. Bob applies corrections to his qubit B:
   - If a=1: apply X to B
   - If b=1: apply Z to B
   Now Bob's qubit B = α|0⟩+β|1⟩ = |ψ⟩ ✓

ANALYSIS TABLE:
Alice measures | Bob's B state | Bob applies | Final B
00             | α|0⟩+β|1⟩   | I (nothing) | α|0⟩+β|1⟩
01             | α|0⟩-β|1⟩   | Z           | α|0⟩+β|1⟩
10             | α|1⟩+β|0⟩   | X           | α|0⟩+β|1⟩
11             | α|1⟩-β|0⟩   | ZX          | α|0⟩+β|1⟩

Each case occurs with probability 1/4.

IMPORTANT POINTS:
- Alice's state is DESTROYED (No-cloning not violated)
- You need 2 classical bits + 1 ebit → teleport 1 qubit
- No faster-than-light communication (classical channel needed)
- Bob gets |ψ⟩ without Alice knowing what it is
- Teleportation + Superdense coding together show: 1 qubit + 1 ebit ↔ 2 classical bits


---

## 3.6 Quantum Key Distribution (BB84 Protocol)

GOAL: Establish a secret key between Alice and Bob that no eavesdropper can learn without detection.

SECURITY BASIS: Any eavesdropping disturbs the quantum states (Heisenberg uncertainty + No-cloning).

PROTOCOL:
1. Alice sends N qubits. For each qubit:
   - Randomly chooses basis: Z-basis {|0⟩,|1⟩} or X-basis {|+⟩,|-⟩}
   - Randomly chooses bit: 0 or 1
   - Encodes: bit 0 in Z → |0⟩, bit 1 in Z → |1⟩; bit 0 in X → |+⟩, bit 1 in X → |−⟩

2. Bob receives each qubit and:
   - Randomly chooses basis (Z or X) to measure
   - Records measurement result

3. Sifting (classical public channel):
   - Alice and Bob announce which BASES they used for each qubit (NOT the bits)
   - They KEEP only bits where they used the SAME basis (~50% kept)
   - Discard bits where bases differed (these are uncorrelated)

4. Error checking:
   - Sacrifice a random sample of kept bits (announce them publicly)
   - Calculate error rate (QBER = Quantum Bit Error Rate)
   - If error rate > threshold (~11%): abort → Eve was listening
   - If error rate OK: the remaining bits form the secret key

WHY EAVESDROPPING IS DETECTABLE:
- Eve must guess the basis to measure
- If Eve guesses wrong: she gets random result, re-sends disturbed state
- Bob then gets wrong state when he uses correct basis
- This shows up as ~25% error rate in the sample → detected
- Security is unconditional (based on laws of physics, not computational difficulty)


---

---

# MODULE 4 — QUANTUM ALGORITHMS I
## (8 Hours)

---

## 4.1 Query Complexity vs Circuit Complexity

CIRCUIT COMPLEXITY: Total number of gates in the circuit.

QUERY COMPLEXITY: How many times we need to call the black-box function (oracle) to solve a problem.
This is what we use to compare quantum vs classical algorithms for query problems.

ORACLE / BLACK BOX (Uf):
The input function f is accessed only through a query gate.

Classical oracle gate: f(x)
Quantum oracle gate: Uf|x⟩|y⟩ = |x⟩|y ⊕ f(x)⟩

Here ⊕ = XOR. The gate is always UNITARY regardless of f.

WHY USE XOR? Makes it unitary (reversible). The input x is preserved, and f(x) is XOR'd with y.

QUANTUM SPEEDUP SOURCE: By putting the input register in superposition before querying, we effectively evaluate f on all inputs at once. This "quantum parallelism" is what gives speedup.

---

## 4.2 Deutsch's Algorithm

PROBLEM: f: {0,1} → {0,1}. Is f constant (f(0)=f(1)) or balanced (f(0)≠f(1))?
Classical: Need 2 queries (must check both f(0) and f(1)).
Quantum: Only 1 query needed!

CIRCUIT:
|0⟩ → H → [Uf] → H → Measure
|1⟩ → H → [Uf]

STEP-BY-STEP ANALYSIS:
Initial: |0⟩|1⟩

After H on both:
|π₁⟩ = |−⟩|+⟩ = (1/√2)(|0⟩−|1⟩) ⊗ (1/√2)(|0⟩+|1⟩)
= (1/2)(|0⟩|0⟩ + |0⟩|1⟩ − |1⟩|0⟩ − |1⟩|1⟩)

KEY STEP — Phase Kickback:
Uf|−⟩|a⟩ = (−1)^f(a)|−⟩|a⟩

The phase (−1)^f(a) "kicks back" to the input register!

After Uf:
|π₂⟩ = |−⟩ ⊗ [(−1)^f(0)|0⟩ + (−1)^f(1)|1⟩] / √2

If f is constant (f(0)=f(1)):
= ±|−⟩|+⟩  (same sign, global phase)

If f is balanced (f(0)≠f(1)):
= ±|−⟩|−⟩  (opposite signs)

After H on second register:
|π₃⟩ = ±|−⟩|f(0)⊕f(1)⟩

Measure second qubit:
- Result 0 → f is CONSTANT
- Result 1 → f is BALANCED

CONCLUSION: 1 query = 1 circuit run → solved!


---

## 4.3 Deutsch-Jozsa Algorithm

PROBLEM: f: {0,1}ⁿ → {0,1}, promised to be either CONSTANT or BALANCED (exactly half 0s, half 1s). Which is it?
Classical: Need 2^(n-1)+1 queries worst case.
Quantum: 1 query!

CIRCUIT:
n |0⟩ qubits → Hⁿ → [Uf] → Hⁿ → Measure all n qubits
1 |1⟩ qubit  → H  → [Uf]

KEY MATH:
H^⊗n on |x⟩ gives: (1/√2ⁿ) Σᵧ (−1)^(x·y)|y⟩

where x·y = x₀y₀ ⊕ x₁y₁ ⊕ ... (binary dot product)

ANALYSIS:
After first Hⁿ: |−⟩ ⊗ (1/√2ⁿ)Σₓ|x⟩  (uniform superposition)
After Uf: |−⟩ ⊗ (1/√2ⁿ)Σₓ(−1)^f(x)|x⟩
After second Hⁿ: each y gets amplitude = (1/2ⁿ)Σₓ(−1)^(f(x)+x·y)

PROBABILITY of measuring all-zeros |0...0⟩:
p(0ⁿ) = |(1/2ⁿ)Σₓ(−1)^f(x)|²

IF f is CONSTANT (all same value):
(1/2ⁿ)Σₓ(−1)^f(x) = ±(1/2ⁿ)·2ⁿ = ±1
→ Probability = 1 (always measure 0ⁿ)

IF f is BALANCED (half 0s, half 1s):
Σₓ(−1)^f(x) = 0 (equal +1 and -1 terms cancel)
→ Probability = 0 (never measure 0ⁿ)

RESULT: Measure all n qubits:
- Get 00...0 → f is CONSTANT
- Get anything else → f is BALANCED

CLASSICAL COMPARISON: Probabilistic algorithm needs O(1) queries to be confident with high probability (making it less impressive than Deutsch-Jozsa sounds), but deterministically it needs 2^(n-1)+1.


---

## 4.4 Bernstein-Vazirani Algorithm

PROBLEM: f: {0,1}ⁿ → {0,1} where f(x) = s·x mod 2 for a SECRET string s. Find s.
Classical: Need n queries (one for each bit of s).
Quantum: 1 query!

SAME CIRCUIT as Deutsch-Jozsa!

|0⟩ⁿ → Hⁿ → [Uf] → Hⁿ → Measure = s

ANALYSIS:
After Hⁿ: uniform superposition
After Uf with f(x) = s·x: (1/√2ⁿ)Σₓ(−1)^(s·x)|x⟩
After Hⁿ: exactly |s⟩

PROOF: The amplitude of |y⟩ after second Hⁿ is:
(1/2ⁿ)Σₓ(−1)^(s·x+x·y) = (1/2ⁿ)Σₓ(−1)^((s⊕y)·x)
= 1 if y=s, and 0 otherwise (using properties of Hadamard)

So measuring gives s exactly! One query, perfect.

---

## 4.5 Simon's Algorithm

PROBLEM: f: {0,1}ⁿ → {0,1}ᵐ with promise that f(x) = f(y) iff x = y or x⊕y = s for a secret s.
When s = 0ⁿ: f is one-to-one (injective).
When s ≠ 0ⁿ: f is two-to-one with period s.
Goal: Find s.
Classical: Exponential queries O(2^(n/2)) by birthday paradox.
Quantum: O(n) queries and O(n) classical post-processing!

CIRCUIT (run n-1 times):
n |0⟩ → Hⁿ → [Uf] → Hⁿ → Measure → get string y
m |0⟩ → (ancilla for f output, measured but irrelevant)

ANALYSIS (one run):
1. Start: |0⟩ⁿ|0⟩ᵐ
2. After Hⁿ: (1/√2ⁿ)Σₓ|x⟩|0⟩
3. After Uf: (1/√2ⁿ)Σₓ|x⟩|f(x)⟩
4. Measure second register → get value f(x₀) for random x₀
   → First register collapses to: (1/√2)(|x₀⟩ + |x₀⊕s⟩)
5. After Hⁿ on first register: get y where y·s = 0 (mod 2)

Each run gives one linear constraint on s: y·s = 0
Run n-1 times → n-1 linearly independent equations
Solve the system classically → find s!

POST-PROCESSING: Gaussian elimination on the system of equations.

IMPORTANCE: Simon's algorithm directly inspired Shor's factoring algorithm!


---

## 4.6 Grover's Algorithm

PROBLEM: Unsorted database of N = 2ⁿ items. Find the one marked item.
Classical: O(N) queries on average.
Quantum: O(√N) queries. QUADRATIC speedup!

SETUP:
Oracle Uf: marks the target state |w⟩
Uf|x⟩ = −|x⟩ if x=w (flips sign/phase of marked state)
Uf|x⟩ = |x⟩ if x≠w

CIRCUIT (repeat ~(π/4)√N times):
n |0⟩ → Hⁿ → [Uf] → [D] → [Uf] → [D] → ... → Measure

Where D = Grover Diffusion Operator = 2|s⟩⟨s| − I (and |s⟩ is uniform superposition)
Implemented as: Hⁿ → Phase flip on |0...0⟩ → Hⁿ

HOW IT WORKS (amplitude amplification):
Start with |s⟩ = (1/√N)Σₓ|x⟩ (all equal amplitudes 1/√N)

Each Grover iteration:
1. Oracle: flip phase of |w⟩ (amplitude goes from +1/√N to -1/√N)
2. Diffusion: reflect around the average amplitude
   → Amplitude of |w⟩ increases, all others decrease slightly

After k iterations:
- Amplitude of |w⟩ ≈ sin((2k+1)θ) where sin(θ) = 1/√N
- Amplitude of others ≈ cos((2k+1)θ)/√(N-1)

Optimal number of iterations: k_opt ≈ (π/4)√N

At that point, probability of measuring |w⟩ ≈ 1.

EXAMPLE with N=4 (n=2 qubits), marked state = |11⟩:
After 1 Grover iteration, probability of |11⟩ ≈ 1 (exactly).

IMPORTANCE: Any problem that can be formulated as "search for a solution among N possibilities" gets a quadratic speedup. This includes NP-complete problems (but only quadratic speedup, not exponential).


---

---

# MODULE 5 — QUANTUM ALGORITHMS II
## (8 Hours)

---

## 5.1 Quantum Fourier Transform (QFT)

CLASSICAL DISCRETE FOURIER TRANSFORM (DFT):
Transforms signal from time domain to frequency domain.
For N-point DFT: N²operations (or N log N with FFT).

QUANTUM FOURIER TRANSFORM:
QFT_N |y⟩ = (1/√N) Σₓ₌₀^(N-1) e^(2πixy/N) |x⟩

For N = 2ⁿ qubits: Only O(n²) = O(log²N) gates needed!

FORMULA in shorthand: Using ωₙ = e^(2πi/N):
QFT_N |y⟩ = (1/√N) Σₓ ωₙ^(xy) |x⟩

EXAMPLES:
QFT₂ = H  (Hadamard gate!)

QFT₄ = (1/2) [[1, 1, 1, 1],
               [1, i, -1, -i],
               [1, -1, 1, -1],
               [1, -i, -1, i]]

PRODUCT FORMULA (key for circuit design):
QFT₂ₙ |j₁j₂...jₙ⟩ = (1/√2)(|0⟩+e^(2πi0.jₙ)|1⟩) ⊗
                       (1/√2)(|0⟩+e^(2πi0.jₙ₋₁jₙ)|1⟩) ⊗ ... ⊗
                       (1/√2)(|0⟩+e^(2πi0.j₁j₂...jₙ)|1⟩)

Where 0.j₁j₂...jₙ means binary fraction j₁/2 + j₂/4 + ... + jₙ/2ⁿ.

CIRCUIT for QFT₂ₙ:
Uses:
- n Hadamard gates (one per qubit)
- Controlled phase rotation gates Rₖ = [[1,0],[0,e^(2πi/2^k)]]
- SWAP gates to reverse bit order

Total gates: n(n+1)/2 = O(n²)

INVERSE QFT (IQFT):
QFT† (just reverse the circuit, negate all phases)
IQFT_N |x⟩ = (1/√N) Σᵧ e^(-2πixy/N) |y⟩


---

## 5.2 Quantum Phase Estimation (QPE)

PROBLEM: Given unitary U and one of its eigenvectors |ψ⟩:
U|ψ⟩ = e^(2πiθ)|ψ⟩
Find θ (the phase).

This is the CORE of Shor's algorithm. Eigenvalues of unitaries lie on unit circle → encoded as phases.

CIRCUIT (m control qubits for m bits of precision):
m |0⟩ qubits  → Hᵐ → Controlled-U¹, U², U⁴,...,U^(2^(m-1)) → IQFT → Measure = y
n |ψ⟩ qubits  → (target for controlled-U operations)

STEP-BY-STEP:
1. Apply Hᵐ to control register: (1/√2ᵐ)Σₓ|x⟩ ⊗ |ψ⟩
2. Apply controlled-U^k for each k: phase kicks back!
   Result: (1/√2ᵐ)Σₓ e^(2πiθx)|x⟩ ⊗ |ψ⟩
3. Apply IQFT to control register
4. Measure → get y ≈ θ·2ᵐ (in binary)

OUTPUT: y/2ᵐ ≈ θ

PRECISION: With m control qubits, get θ to m bits of precision.

WHEN EXACT: If θ = y/2ᵐ exactly for some integer y, the measurement gives y with certainty.
WHEN APPROXIMATE: The distribution peaks near the best approximation to θ.

PHASE KICKBACK (the magic step):
If U|ψ⟩ = e^(2πiθ)|ψ⟩, then controlled-U applied to |1⟩|ψ⟩:
= e^(2πiθ)|1⟩|ψ⟩
→ (1/√2)(|0⟩+|1⟩)|ψ⟩ becomes (1/√2)(|0⟩+e^(2πiθ)|1⟩)|ψ⟩
The phase θ is encoded in the control qubit!


---

## 5.3 Order Finding (Quantum Period Finding)

PROBLEM: Given a, N with gcd(a,N)=1, find the ORDER r = smallest positive integer with aʳ ≡ 1 (mod N).

CONNECTION TO PHASE ESTIMATION:
Define unitary: Mₐ|x⟩ = |ax mod N⟩

Eigenvectors of Mₐ are:
|uₛ⟩ = (1/√r) Σⱼ₌₀^(r-1) e^(-2πisj/r) |aʲ mod N⟩   for s = 0, 1, ..., r-1

Eigenvalues: Mₐ|uₛ⟩ = e^(2πis/r)|uₛ⟩

So if we do phase estimation on Mₐ with eigenvector |uₛ⟩:
→ We learn s/r

From multiple estimates of s/r for random s values, we can find r using the CONTINUED FRACTION ALGORITHM.

Convenient note: The equal superposition (1/√r)Σⱼ|aʲ mod N⟩ = (1/√r)Σₛ|uₛ⟩ can be prepared from |1⟩!


---

## 5.4 Shor's Algorithm (Factoring)

PROBLEM: Factor N = p × q (product of two large primes).
Classical: Best known algorithm is sub-exponential but still slow for large N.
Quantum: Polynomial time! Breaks RSA encryption.

FULL ALGORITHM:
1. If N is even → return factor 2 (classical)
2. If N = aᵇ for a≥1, b≥2 → return a (classical, check for perfect powers)
3. Choose random a, 1 < a < N
4. Compute g = gcd(a, N). If g ≠ 1 → return g (lucky classical factor!)
5. *** QUANTUM STEP: Find order r of a mod N (use quantum order finding)
6. If r is odd OR aʳ/² ≡ -1 (mod N) → go back to step 3 (try new a)
7. Compute gcd(aʳ/² − 1, N) and gcd(aʳ/² + 1, N)
8. At least one gives a non-trivial factor of N

WHY STEP 7 WORKS (Number Theory):
aʳ ≡ 1 (mod N)
→ (aʳ/²)² ≡ 1 (mod N)
→ (aʳ/² − 1)(aʳ/² + 1) ≡ 0 (mod N)
→ N divides the product
→ gcd(aʳ/² ± 1, N) gives factors (as long as aʳ/² ≢ ±1)

COMPLEXITY: O(log³N) quantum gates, O(log N) qubits. POLYNOMIAL!

EXAMPLE with N=15, a=7:
Orders of 7 mod 15:
7¹ = 7, 7² = 49 = 4, 7³ = 28 = 13, 7⁴ = 91 = 1
So r = 4 (even ✓)

7²/² = 7² = 49 ≡ 4 (mod 15). Is 4 ≡ -1 (mod 15)? -1 ≡ 14 (mod 15). No ✓

gcd(7² − 1, 15) = gcd(48, 15) = gcd(48, 15):
48 = 3×15 + 3 → gcd(15,3) = 3 ✓ (factor of 15!)

gcd(7² + 1, 15) = gcd(50, 15):
50 = 3×15 + 5 → gcd(15,5) = 5 ✓ (factor of 15!)

15 = 3 × 5 ✓


---

---

# MODULE 6 — QUANTUM APPLICATIONS
## (8 Hours)

---

## 6.1 Adiabatic Quantum Computing and Quantum Annealing

ADIABATIC THEOREM:
If a quantum system starts in the ground state (lowest energy state) of Hamiltonian H(t) and H(t) changes SLOWLY enough, the system stays in the ground state throughout.

"Slowly" means: Evolution time T >> 1/Δ²
where Δ = minimum energy gap between ground state and first excited state.

ADIABATIC QUANTUM COMPUTING (AQC):
1. Prepare easy initial Hamiltonian H₀ (ground state simple to make, e.g., |+⟩ⁿ)
2. Slowly change to problem Hamiltonian H_problem:
   H(t) = (1-t/T)H₀ + (t/T)H_problem
3. If T is large enough, system stays in ground state throughout
4. Ground state of H_problem = solution to computational problem

AQC is equivalent to quantum circuit model in computational power.

QUANTUM ANNEALING:
- Heuristic version of AQC (doesn't need to be perfectly adiabatic)
- Used in D-Wave machines
- Solves optimization problems → find minimum energy = optimal solution
- Can use quantum tunneling to escape local minima (unlike classical annealing)

ISING MODEL FORMULATION:
Many optimization problems mapped to minimize:
H = Σᵢⱼ Jᵢⱼ σᵢᶻσⱼᶻ + Σᵢ hᵢ σᵢᶻ

Where σᵢ = ±1 (spin variables).

Applications: logistics optimization, drug discovery, financial portfolio optimization, scheduling problems.


---

## 6.2 Quantum Error Correction

WHY NEEDED: Qubits are fragile. Interaction with environment causes DECOHERENCE — the quantum state is destroyed. Without error correction, quantum computers can't run long algorithms.

TYPES OF ERRORS:
- Bit flip error (X error): |0⟩ → |1⟩ or |1⟩ → |0⟩
- Phase flip error (Z error): |+⟩ → |−⟩ (changes sign of |1⟩ component)
- Both (Y error): combination of bit flip and phase flip

CHALLENGE: Cannot measure the qubit (destroys superposition). Cannot copy the qubit (No-cloning). So how?

SOLUTION: Encode 1 LOGICAL qubit in multiple PHYSICAL qubits.
Measure SYNDROMES (error indicators) without learning the state.

Syndrome = eigenvalue of a stabilizer operator, tells you WHAT error occurred but not WHAT the state is.

THRESHOLD THEOREM:
If physical error rate p < p_threshold (about 0.1-1%):
Adding more qubits makes the logical error rate DECREASE.
Can do arbitrarily long computation with polynomial overhead!


---

## 6.3 Stabilizer Formalism

A stabilizer is a Pauli operator S such that S|ψ⟩ = |ψ⟩ (the state is a +1 eigenstate).

For an [[n,k,d]] stabilizer code:
- n = physical qubits
- k = logical qubits encoded
- d = code distance (minimum weight of detectable/correctable errors)
- Needs n-k stabilizer generators

Instead of tracking the full 2ⁿ-dimensional state, track n-k stabilizers.
This is exponentially more efficient!

Correcting errors:
1. Measure the n-k stabilizers → get ±1 outcomes (syndrome)
2. Different error patterns → different syndromes
3. Apply correction based on syndrome table
4. State is restored without having measured its value!


---

## 6.4 Shor's 9-Qubit Error Correcting Code

First quantum error correcting code (Peter Shor, 1995).
Encodes 1 logical qubit in 9 physical qubits.
Corrects ANY single-qubit error.

LOGICAL STATES:
|0⟩_L = (1/2√2)(|000⟩+|111⟩)⊗(|000⟩+|111⟩)⊗(|000⟩+|111⟩)
|1⟩_L = (1/2√2)(|000⟩-|111⟩)⊗(|000⟩-|111⟩)⊗(|000⟩-|111⟩)

STRUCTURE:
- 3 groups of 3 qubits
- Each group of 3 corrects BIT FLIP errors (using 3-qubit repetition)
- The outer code corrects PHASE FLIP errors

ERROR CORRECTION:
1. Bit flip in any group: Detected by majority vote within that group
   (Compare qubit pairs with CNOT, measure ancillas)
2. Phase flip across groups: Detected by majority vote of groups
   (Compare group parities)
3. Combined (Y error): Corrected by handling bit and phase separately

SYNDROME MEASUREMENT: 6 stabilizers for bit flips (2 per group) + 2 stabilizers for phase flips = 8 total → 8 measurement outcomes → identifies which of 9 qubits had error and what type.


---

## 6.5 Steane's 7-Qubit Error Correcting Code

More efficient than Shor's code!
Encodes 1 logical qubit in 7 physical qubits.
Corrects any single-qubit error.
Based on the classical [7,4,3] Hamming code.

PROPERTIES:
- [[7,1,3]] code: 7 physical qubits, 1 logical qubit, distance 3
- Distance 3 means: corrects all errors of weight ≤ 1

LOGICAL STATES:
|0⟩_L = (1/√8) Σ_{c∈C} |c⟩  (sum over all codewords of classical Hamming code)
|1⟩_L = (1/√8) Σ_{c∈C} |c⊕1111111⟩

STABILIZERS: 6 stabilizers (3 X-type, 3 Z-type):
X-type: IIIXXXX, IXXIIXX, XIXIXIX
Z-type: IIIZZZZ, IZZIIZZ, ZIZIZIZ

Each stabilizer is measured → syndrome (3 bits for X errors, 3 bits for Z errors) → identifies error location exactly.

ADVANTAGES over Shor:
- Fewer physical qubits (7 vs 9)
- Transversal gates: logical H, CNOT, Pauli gates can be applied bit-by-bit (errors don't spread)
- Logical operations are straightforward to implement fault-tolerantly


---

## 6.6 Gottesman-Knill Theorem

STATEMENT: Any quantum circuit using only:
- Preparation of |0⟩ states
- Clifford gates: {H, S, CNOT, X, Y, Z, and composites}
- Pauli measurements (measuring in X, Y, or Z basis)

...can be EFFICIENTLY SIMULATED on a classical computer in polynomial time.

CLIFFORD GATES: Gates that map Pauli operators to Pauli operators under conjugation.
H, S, CNOT are the generators. They preserve the "Pauli group" structure.

WHY THIS MATTERS:
Clifford circuits are NOT enough for quantum speedup.

To get quantum advantage, you MUST use NON-CLIFFORD gates.
The most important non-Clifford gate: T = [[1,0],[0,e^(iπ/4)]]

Universal quantum computing = Clifford gates + T gate
T gates are expensive in fault-tolerant quantum computing (need magic state distillation).

PRACTICAL CONSEQUENCE: When designing quantum algorithms, the T-count (number of T gates) is a key resource metric.


---

## 6.7 Fault-Tolerant Quantum Computing

PROBLEM: Errors in quantum computers don't just affect individual qubits — they can SPREAD through entangling gates. A CNOT between one errored qubit and a clean qubit → 2 errored qubits. If this happens faster than error correction, the algorithm fails.

KEY PRINCIPLES OF FAULT-TOLERANCE:

1. TRANSVERSAL GATES: Apply logical gate by applying physical gate to corresponding qubits in different code blocks. Errors can't spread across a code block (each physical gate acts on at most one qubit per block). Transversal gates are naturally fault-tolerant.

2. THRESHOLD THEOREM: If physical error rate p < p_threshold:
   - Using a concatenated code (code of a code of a code...)
   - Logical error rate decreases DOUBLY EXPONENTIALLY with code levels
   - Arbitrary-length quantum computation is possible!
   - p_threshold ≈ 0.1% to 1% (depends on specific code and gates)

3. MAGIC STATE DISTILLATION: T gates can't be implemented transversally.
   Solution: Prepare many noisy "magic states" |T⟩ = T|+⟩
   Use error correction to distill a few clean magic states
   Use teleportation-based gadget to implement T gate from clean magic state

4. ERROR PROPAGATION RULES:
   - Pauli errors "commute through" Clifford gates (just transform)
   - Track how errors propagate as Pauli operators
   - Correct at the end if total error weight is within code's capacity

RESOURCE OVERHEAD: Fault-tolerant quantum computing requires ~1000 physical qubits per logical qubit (for current error correction schemes). This is why "1000-qubit quantum computers" are nowhere near being able to break RSA.


---

## 6.8 Quantum Machine Learning (QML)

Overview of how quantum computing intersects with ML:

### HHL Algorithm (Quantum Linear Systems)
Solves Ax = b for N×N matrix A.
Classical: O(N^2.38 · κ) (best known)
Quantum: O(poly(log N) · κ²) — exponential speedup (if conditions met!)
κ = condition number of A

Caveat: Loading classical data takes O(N) in general → may eliminate speedup.

### Variational Quantum Eigensolver (VQE)
Find ground state energy of a Hamiltonian H.
Hybrid classical-quantum algorithm:
1. Parameterize a quantum circuit U(θ)
2. Compute ⟨ψ(θ)|H|ψ(θ)⟩ on quantum computer
3. Optimize parameters θ classically (minimize energy)
4. Repeat until converged

Applications: Quantum chemistry, materials science.

### QAOA (Quantum Approximate Optimization Algorithm)
For combinatorial optimization problems (Max-Cut, TSP, etc.).
1. Encode problem in Hamiltonian H_C (cost)
2. Alternate between H_C and mixing Hamiltonian H_B
3. Circuit: e^(-iγH_C) e^(-iβH_B) repeated p times
4. Optimize angles γ, β classically
5. More layers (larger p) → better approximation

Advantage over classical: Not proven, but may have advantage for some problems.

### Quantum Neural Networks (QNNs)
Parameterized quantum circuits used as neural networks:
- Input: Encoded as quantum state
- Parameters: Rotation angles in gates
- Output: Measurement outcomes
- Training: Classical optimizer minimizes loss function

Key challenges:
- Barren plateaus: gradients vanish exponentially with system size
- No-cloning: cannot copy states freely
- Measurement: reduces quantum state to classical

### Quantum ML Summary

| Method | Classical | Quantum | Conditions |
|--------|-----------|---------|------------|
| Linear systems (HHL) | O(N^2.38) | O(log²N) | Sparse, low κ, quantum RAM |
| Principal component analysis | O(N²) | O(log N) | Quantum data |
| Grover search | O(N) | O(√N) | Any |
| Quantum kernel methods | O(N²) | O(N) | Quantum feature map advantage |


---

---

# QUICK REVISION — EXAM CHEATSHEET

---

## All Algorithms at a Glance

| Algorithm | Problem | Classical Queries | Quantum Queries | Key Tool |
|-----------|---------|-------------------|-----------------|----------|
| Deutsch | Constant/Balanced (n=1) | 2 | 1 | Phase kickback |
| Deutsch-Jozsa | Constant/Balanced (any n) | 2^(n-1)+1 | 1 | Interference |
| Bernstein-Vazirani | Find hidden string s | n | 1 | Interference |
| Simon's | Find XOR period | O(2^(n/2)) | O(n) | Interference + linear algebra |
| Grover | Unstructured search | O(N) | O(√N) | Amplitude amplification |
| Shor | Factoring N | exp(O(∛N)) | O(log³N) | QFT + Order finding |

---

## All Key Gates

| Gate | Matrix | Action | Type |
|------|--------|--------|------|
| X | [[0,1],[1,0]] | |0⟩↔|1⟩ | Clifford |
| Y | [[0,-i],[i,0]] | bit+phase flip | Clifford |
| Z | [[1,0],[0,-1]] | phase flip | Clifford |
| H | (1/√2)[[1,1],[1,-1]] | |0⟩→|+⟩, |1⟩→|−⟩ | Clifford |
| S | [[1,0],[0,i]] | phase by π/2 | Clifford |
| T | [[1,0],[0,e^(iπ/4)]] | phase by π/4 | NON-Clifford |
| CNOT | 4×4 | flip target if control=1 | Clifford |
| Toffoli | 8×8 | flip target if both controls=1 | NON-Clifford |

---

## Key Formulas

```
Qubit state:         |ψ⟩ = α|0⟩ + β|1⟩,     |α|²+|β|² = 1
Bloch sphere:        |ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩
Measurement prob:    P(a) = |⟨a|ψ⟩|² = |αₐ|²
Post-measurement:    |a⟩  (collapses to basis state)
Density operator:    ρ = Σᵢ pᵢ|ψᵢ⟩⟨ψᵢ|, Tr(ρ)=1
Commutator:          [A,B] = AB - BA
Uncertainty:         ΔA·ΔB ≥ ½|⟨[A,B]⟩|
Cauchy-Schwarz:      |⟨ψ|φ⟩|² ≤ ⟨ψ|ψ⟩·⟨φ|φ⟩
Oracle gate:         Uf|x⟩|y⟩ = |x⟩|y⊕f(x)⟩
Phase kickback:      Uf|−⟩|a⟩ = (−1)^f(a)|−⟩|a⟩
QFT formula:         QFT|y⟩ = (1/√N)Σₓ e^(2πixy/N)|x⟩
Grover iterations:   k ≈ (π/4)√N
Shor step:           gcd(aʳ/² ± 1, N)
```

---

## Important Theorems

1. No-Cloning Theorem: Cannot clone unknown quantum state
2. Cauchy-Schwarz Inequality: |⟨ψ|φ⟩|² ≤ ⟨ψ|ψ⟩⟨φ|φ⟩
3. Heisenberg Uncertainty: ΔA·ΔB ≥ ½|⟨[A,B]⟩|
4. Gottesman-Knill Theorem: Clifford circuits classically simulable
5. Threshold Theorem: Below error threshold, fault-tolerant QC possible
6. Adiabatic Theorem: Slow evolution stays in ground state
7. Bell/CHSH: Quantum correlations violate local hidden variable theories (max 2√2 ≈ 2.83 vs classical 2)
8. Holevo's Theorem: Max 1 classical bit per qubit (without entanglement)

---

## Error Correction Codes Compared

| Code | Physical Qubits | Logical Qubits | Corrects | Key Feature |
|------|----------------|----------------|---------|-------------|
| Shor 9-qubit | 9 | 1 | Any single qubit error | First QEC code |
| Steane 7-qubit | 7 | 1 | Any single qubit error | Transversal Clifford gates |
| 3-qubit bit flip | 3 | 1 | Bit flip only | Simple, educational |

---

---

# EXAM ANSWER STRATEGIES

---

## Question Type Templates

### For "Analyze/Explain how X works" (20 marks)
Structure your answer:
1. DEFINE the concept clearly (2-3 marks)
2. MATHEMATICAL FORMULATION — write the key equation or matrix (4-5 marks)
3. STEP-BY-STEP working or derivation (8-10 marks)
4. CONCRETE EXAMPLE with numbers (3-4 marks)
5. SIGNIFICANCE / WHY IT MATTERS (2-3 marks)

### For "Evaluate implications of X" (20 marks)
1. State what X is
2. Derive the key consequence / implication
3. Show examples of where implication applies
4. Discuss limitations or edge cases
5. Connect to practical relevance

### For "Apply X to Y" (10-20 marks)
Go step by step. Show intermediate states. Do not skip steps.

### For "Design a circuit for..." (10 marks)
1. Describe qubits and initial states
2. List gates in order with explanation of each
3. Verify the final state is correct
4. Brief comment on complexity

### For "Compare and contrast X and Y" (10 marks)
Make a clear table. Then write 2-3 sentences on key difference.

### For "Propose a novel quantum algorithm" (Compulsory, 20 marks)
Template:
1. STATE THE PROBLEM: Define the computational problem clearly (2 marks)
2. CLASSICAL APPROACH: What classical algorithms do and why they're slow (2 marks)
3. QUANTUM INSIGHT: Which quantum property (superposition/entanglement/interference) gives advantage (3 marks)
4. ALGORITHM STEPS: Step by step (6 marks)
   - State preparation
   - Key quantum operations
   - Measurement and post-processing
5. COMPLEXITY ANALYSIS: How many queries/gates? (3 marks)
6. CORRECTNESS: Why does it work? (2 marks)
7. LIMITATIONS: When might it fail? (2 marks)

Example answer sketch for genetic algorithm question:
PROBLEM: Combinatorial optimization over exponentially large search space (e.g., optimal protein folding, circuit design).
CLASSICAL: Genetic algorithms use random mutation and selection — O(N) per generation, thousands of generations.
QUANTUM INSIGHT: Use superposition to evaluate all candidate solutions simultaneously. Use Grover to amplify high-fitness solutions.
ALGORITHM:
- Encode population as superposition: Hⁿ|0⟩ = (1/√2ⁿ)Σ|x⟩
- Apply fitness oracle Uf to mark high-fitness individuals
- Apply Grover diffusion to amplify marked states
- Measure → get near-optimal solution
- Repeat for "evolution" with mutation operators
COMPLEXITY: O(√N) per "generation" vs O(N) classical → quadratic speedup in fitness evaluation.

---

## Memory Tricks

- "H creates superposition, CNOT creates entanglement"
- "Grover: √N not N" (square root speed up)
- "Shor: polynomial not exponential"
- "1 query for Deutsch, n queries classically"
- "Clifford = efficient classically (Gottesman-Knill), T = quantum power"
- "Teleport needs 2 classical bits + 1 ebit"
- "Superdense: 1 qubit + 1 ebit = 2 classical bits"
- "Bell inequality: classical max 3/4, quantum max (2+√2)/4 ≈ 0.854"
- "Monogamy: A entangled with B means A NOT entangled with C"

---

## Common Exam Pitfalls

1. Don't confuse α (amplitude) with |α|² (probability)
2. Phase matters! |+⟩ and |−⟩ have same probabilities but DIFFERENT phases
3. Measurement ALWAYS destroys superposition (unless measuring in the basis of the superposition)
4. CNOT table: rows are {00, 01, 10, 11}, target is SECOND qubit when control is FIRST
5. QFT is not the same as DFT — it acts on quantum amplitudes, not classical data
6. Shor's algorithm needs r to be even and aʳ/² ≢ -1 (mod N) — must restart if not
7. Gottesman-Knill: efficiently simulable ≠ useless. Clifford circuits are used for error correction!
8. No-Cloning does not prevent teleportation (original is destroyed)
9. Density operator Tr(ρ²) = 1 for PURE state, < 1 for MIXED state (not the other way)
10. Tensor product of n qubits has 2ⁿ dimensions — a 5-qubit system is 32-dimensional

---

**ALL THE BEST FOR YOUR EXAM! YOU'VE GOT EVERYTHING YOU NEED.**
