# Error Analysis Examples in OntoLLM‑Benchmark

This document presents representative error patterns observed in ontology‑grounded reasoning tasks.  
Each example illustrates a typical failure mode for one of the five benchmark tasks:

1. Definition  
2. Axiom Completion  
3. Hierarchical Placement  
4. Structural Coherence  
5. Provenance  

The goal is to help researchers understand *why* models fail and how difficulty scaling affects error rates.

---

# 1. Definition Task — Typical Errors

Definition generation requires semantic fidelity to the ontology.  
Common failure modes include:

### 1.1 Hallucinated Properties
The model introduces attributes not present in the ontology.

**Input**  
Concept: *Wetland*  
Ontology ID: ENVO:000017  
Context: “A land area saturated with water.”

**Incorrect Model Output**  
“A wetland is a **saltwater** ecosystem where **mangroves grow**.”

**Error Type**  
- Hallucination  
- Over‑specification  
- Domain drift  

**Correct Output**  
“A wetland is an area of land saturated with water, supporting water‑adapted ecosystems.”

---

### 1.2 Overly Generic Definitions
The model fails to use ontology‑specific constraints.

**Incorrect Output**  
“A wetland is a type of environment.”

**Error Type**  
- Under‑specification  
- Loss of ontology grounding  

---

# 2. Axiom Completion — Typical Errors

This task requires inferring missing axioms without inventing new relations.

### 2.1 Inventing Non‑existent Relations
**Input**  
Concept: *Teacher*  
Known axioms:  
- Teacher **teaches** Student  
- Teacher **works_in** School  

**Incorrect Output**  
- Teacher **evaluates** Curriculum  

**Error Type**  
- Fabricated relation  
- Ontology schema violation  

---

### 2.2 Incorrect Directionality
**Incorrect Output**  
- Student **teaches** Teacher  

**Error Type**  
- Reversed relation  
- Violation of domain/range constraints  

---

# 3. Hierarchical Placement — Typical Errors

Models must choose the most specific valid parent class.

### 3.1 Choosing an Overly General Parent
**Input**  
Concept: *Estuarine Delta*  
Candidate parents:  
- CoastalFormation  
- RiverMouth  
- GeographicalFeature  

**Incorrect Output**  
Parent: *GeographicalFeature*

**Error Type**  
- Over‑generalization  
- Failure to use domain‑specific hierarchy  

**Correct Output**  
Parent: *CoastalFormation*  
Justification: Estuarine deltas form at the interface of river and coastal systems.

---

### 3.2 Choosing a Semantically Similar but Incorrect Parent
**Incorrect Output**  
Parent: *RiverMouth*  

**Error Type**  
- Semantic proximity error  
- Missing multi‑hop reasoning  

---

# 4. Structural Coherence — Typical Errors

This task checks whether multi‑component outputs violate ontology constraints.

### 4.1 Ignoring Domain/Range Constraints
**Input triple**  
(Student, enrolled_in, Teacher)

**Incorrect Output**  
Status: VALID  

**Error Type**  
- Failure to apply range constraint  
- Shallow pattern matching  

**Correct Output**  
Status: INVALID  
Explanation: *Teacher* is not a valid range for *enrolled_in*.

---

### 4.2 Missing Disjointness Violations
**Input triple**  
(Bird, is_a, Mammal)

**Incorrect Output**  
Status: VALID  

**Error Type**  
- Failure to apply disjointness axioms  
- Ontology inconsistency not detected  

---

# 5. Provenance — Typical Errors

Models must provide verifiable, non‑fabricated sources.

### 5.1 Fabricated Citations
**Incorrect Output**  
“According to *Nature Ecology Review 2018*, wetlands increase biodiversity.”

**Error Type**  
- Hallucinated source  
- Non‑verifiable citation  

---

### 5.2 Mixing Ontology and Non‑ontology Sources
**Incorrect Output**  
“Based on Wikipedia and the ENVO ontology…”

**Error Type**  
- Unreliable source mixing  
- Violates benchmark constraints  

---

# 6. Cross‑Task Error Patterns

Across tasks, several recurring failure modes appear:

### 6.1 Shallow Heuristics
Models rely on surface patterns instead of ontology structure.

### 6.2 Semantic Drift
Definitions or axioms gradually diverge from the ontology domain.

### 6.3 Over‑generalization
Choosing safe but uninformative answers.

### 6.4 Over‑confidence in Hallucinations
Especially in provenance and axiom completion.

---

# 7. Difficulty Scaling and Error Severity

Difficulty levels (Easy/Medium/Hard) amplify different error types:

| Difficulty | Typical Errors | Explanation |
|-----------|----------------|-------------|
| Easy | under‑specification, simple hallucinations | shallow tasks allow shortcuts |
| Medium | multi‑step reasoning failures | requires combining multiple axioms |
| Hard | ambiguity handling, distractor confusion, provenance hallucinations | requires deep ontology grounding |

For details, see:  
**`difficulty_scaling.md`**

---

# 8. How to Use This Document

This file supports:

- model debugging  
- qualitative evaluation  
- reviewer transparency  
- reproducibility of error categories  
- curriculum‑style training analysis  

It complements:  
- **Synthetic examples:** `synthetic_examples.md`  
- **Metric definitions:** `metrics_definition.md`  
- **Prompts:** `../prompts/`

---

# Summary

This document provides a structured overview of common failure modes across all five tasks in OntoLLM‑Benchmark.  
It highlights how ontology‑grounded reasoning challenges current LLMs and why difficulty scaling is essential for robust evaluation.
