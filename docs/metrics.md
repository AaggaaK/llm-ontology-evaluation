# Metrics

OntoLLM‑Benchmark evaluates models along five complementary, theoretically grounded
dimensions of ontology‑aware correctness.  
Each metric corresponds to one of the five benchmark tasks and is implemented in
`evaluation/metrics/`.

---

## 1. Semantic Fidelity Score (SFS)
Measures how well the generated text preserves the meaning of the reference
definition using embedding‑based cosine similarity.

## 2. Logical Consistency Index (LCI)
Checks whether generated axioms respect ontology logic, including domain/range
constraints, disjointness, and directionality.

## 3. Ontology Faithfulness Score (OFS)
Evaluates whether predicted relations and structural assertions belong to the
ontology’s valid relation set and follow its schema.

## 4. Provenance Faithfulness Score (PFS)
Assesses whether cited sources are valid, authoritative, non‑hallucinated, and
consistent with the ontology domain.

## 5. Structural Coherence Score (SCS)
Measures whether multi‑component outputs (relations, triples, placements) are
structurally consistent with the ontology graph, including hierarchy, constraints,
and disjointness.

---

For detailed mathematical definitions, see **`metrics_definition.md`**.
