# Metric Diagram for OntoLLM‑Benchmark

This diagram shows how the five metrics relate to the benchmark tasks and to
different dimensions of ontology‑grounded correctness.

## 1. High‑level metric map

┌───────────────────────────────┐
│   ONTOLOGY‑GROUNDED OUTPUT    │
└───────────────┬───────────────┘
│
┌────────────────────────┼────────────────────────┐
│                        │                        │
▼                        ▼                        ▼
┌───────────────┐        ┌───────────────┐        ┌───────────────┐
│   SEMANTICS   │        │     LOGIC     │        │   STRUCTURE    │
│   (meaning)   │        │ (consistency) │        │ (constraints)  │
└──────┬────────┘        └──────┬────────┘        └──────┬────────┘
│                        │                        │
▼                        ▼                        ▼
┌───────────────┐        ┌───────────────┐        ┌───────────────┐
│      SFS      │        │      LCI      │        │      SCS      │
│   Semantic    │        │    Logical    │        │   Structural  │
│   Fidelity    │        │  Consistency  │        │   Coherence   │
└───────────────┘        └───────────────┘        └───────────────┘

┌───────────────────────────────┐
│   ONTOLOGY ALIGNMENT & TRACE  │
└───────────────┬───────────────┘
│
┌───────────────┼───────────────┐
│                               │
▼                               ▼
┌───────────────┐               ┌───────────────┐
│      OFS      │               │      PFS      │
│   Ontology    │               │   Provenance  │
│ Faithfulness  │               │ Faithfulness  │
└───────────────┘               └───────────────┘


---

## 2. Metrics and tasks

| Metric | Main focus                    | Strongly tied tasks                                  |
|--------|-------------------------------|------------------------------------------------------|
| SFS    | Semantic fidelity             | Definition, Axiom Completion                         |
| LCI    | Logical consistency           | Axiom Completion, Structural Coherence               |
| OFS    | Ontology faithfulness         | Hierarchical Placement, Axiom Completion             |
| PFS    | Provenance faithfulness       | Provenance                                           |
| SCS    | Structural coherence          | Hierarchical Placement, Structural Coherence         |

---

## 3. Relation to documents

- Formal definitions: `docs/metrics_definition.md`  
- Examples: `docs/synthetic_examples.md`  
- Failure modes: `docs/error_analysis_examples.md`  
- Tasks context: `docs/benchmark_overview.md`
