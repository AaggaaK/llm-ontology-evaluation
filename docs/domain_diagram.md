# Domain Diagram for OntoLLM‑Benchmark

The benchmark covers four ontology‑grounded domains.  
Each domain provides instances for all five tasks (Definition, Axiom Completion, Hierarchical Placement, Structural Coherence, Provenance).

Below is a high‑level ASCII diagram showing the structure and relationships between domains and tasks.

┌──────────────────────────┐
│      BIOMEDICAL          │
│  diseases, symptoms,     │
│  processes, organisms    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      EDUCATIONAL         │
│  roles, institutions,    │
│  learning processes      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│        GENERAL           │
│  everyday concepts,      │
│  commonsense categories  │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│     ENVIRONMENTAL        │
│  ecosystems, habitats,   │
│  natural formations      │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│        FIVE TASKS        │
│  Definition              │
│  Axiom Completion        │
│  Hierarchical Placement  │
│  Structural Coherence    │
│  Provenance              │
└──────────────────────────┘

---

## 1. Domain Overview

### Biomedical  
Covers diseases, biological processes, symptoms, organisms, and interactions.

### Educational  
Covers roles (Teacher, Student), institutions, learning processes, and academic structures.

### General  
Covers broad, everyday concepts used across ontologies (objects, events, categories).

### Environmental  
Covers ecosystems, habitats, natural formations, and environmental processes.

---

## 2. How Domains Connect to Tasks

All four domains support all five tasks:

- **Definition** — domain‑specific conceptual grounding  
- **Axiom Completion** — domain‑specific relations  
- **Hierarchical Placement** — domain‑specific taxonomies  
- **Structural Coherence** — domain‑specific structural constraints  
- **Provenance** — domain‑specific sources  

This ensures cross‑domain comparability and balanced difficulty scaling.

---

## 3. Related Documents

- **Difficulty scaling:** `difficulty_scaling.md`  
- **Error analysis examples:** `error_analysis_examples.md`  
- **Prompts:** `../prompts/`  
- **Metric definitions:** `metrics_definition.md`

---

# Summary

This diagram provides a high‑level overview of the four domains and their unified connection to the five ontology‑grounded tasks.  
It complements the benchmark overview and helps reviewers understand the structural design of OntoLLM‑Benchmark.
