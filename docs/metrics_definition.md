# Metric Definitions

This document provides formal definitions of the five evaluation metrics used in
OntoLLM‑Benchmark. Each metric captures a distinct dimension of ontology‑grounded
generation quality and is implemented in `evaluation/metrics/`.

---

## 1. Semantic Fidelity Score (SFS)

**Goal:** Measure semantic similarity between the model‑generated text and the
reference ontology‑aligned description.

### Formal Definition

Let:
- \( g \) = embedding of the generated text  
- \( r \) = embedding of the reference text  



\[
\text{SFS}(g, r) = \frac{g \cdot r}{\|g\| \, \|r\|}
\]



### Range



\[
0 \leq \text{SFS} \leq 1
\]



### Interpretation
- **1.0** — perfect semantic alignment  
- **0.0** — no semantic similarity  

### Notes
Implemented using SentenceTransformers embeddings.

---

## 2. Logical Consistency Index (LCI)

**Goal:** Measure whether the generated axioms respect ontology schema constraints.

### Formal Definition

Let:
- \( A_g \) = set of generated axioms  
- \( A_v \subseteq A_g \) = axioms valid under ontology constraints  
- \( A_i \subseteq A_g \) = axioms violating constraints  



\[
\text{LCI} = \frac{|A_v|}{|A_g|}
\]



### Range



\[
0 \leq \text{LCI} \leq 1
\]



### Interpretation
- **1.0** — all axioms valid  
- **0.0** — all axioms invalid  

### Notes
Validation checks include:
- domain/range  
- disjointness  
- class hierarchy  

---

## 3. Ontology Faithfulness Score (OFS)

**Goal:** Measure whether generated relations belong to the ontology’s allowed relation set.

### Formal Definition

Let:
- \( R_g \) = set of relations used in the generated output  
- \( R_o \) = set of relations defined in the ontology  



\[
\text{OFS} = \frac{|R_g \cap R_o|}{|R_g|}
\]



### Range



\[
0 \leq \text{OFS} \leq 1
\]



### Interpretation
- **1.0** — all relations are ontology‑valid  
- **0.0** — none of the relations are valid  

### Notes
Penalizes hallucinated or non‑existent relations.

---

## 4. Provenance Faithfulness Score (PFS)

**Goal:** Measure whether cited sources are real, verifiable, and authoritative.

### Formal Definition

Let:
- \( S_g \) = set of sources cited by the model  
- \( S_v \subseteq S_g \) = subset of sources verified as real and authoritative  



\[
\text{PFS} = \frac{|S_v|}{|S_g|}
\]



### Range



\[
0 \leq \text{PFS} \leq 1
\]



### Interpretation
- **1.0** — all sources valid  
- **0.0** — all sources hallucinated  

### Notes
Verification uses ontology‑linked databases (GO, ENVO, ESCO, Wikidata).

---

## 5. Structural Coherence Score (SCS)

**Goal:** Measure whether the generated structural assertions (hierarchy, relations,
constraints) are coherent with the ontology graph.

### Formal Definition

Let:
- \( p \) = predicted parent class  
- \( p^\* \) = gold‑standard parent class  
- \( d(p, p^\*) \) = shortest path distance between predicted and gold parent  
- \( D_{\max} \) = maximum allowed distance in the ontology graph  



\[
\text{SCS} = 1 - \frac{d(p, p^\*)}{D_{\max}}
\]



### Range



\[
0 \leq \text{SCS} \leq 1
\]



### Interpretation
- **1.0** — structurally coherent output  
- **0.0** — structurally distant or invalid  

### Notes
Covers:
- hierarchical placement  
- domain/range violations  
- disjointness violations  
- multi‑component structural inconsistencies  

Distances computed using ontology graph traversal.

---

## Summary Table

| Metric | Dimension | Range | Perfect Score Means |
|--------|-----------|--------|----------------------|
| **SFS** | Semantic similarity | 0–1 | Text matches ontology meaning |
| **LCI** | Logical validity | 0–1 | All axioms valid |
| **OFS** | Relation correctness | 0–1 | All relations exist in ontology |
| **PFS** | Provenance validity | 0–1 | All sources verifiable |
| **SCS** | Structural coherence | 0–1 | Fully coherent with ontology graph |

---

For implementation details, see:  
- **`metrics.md`**  
- **`pipeline.md`**  
- **`data_structure.md`**
