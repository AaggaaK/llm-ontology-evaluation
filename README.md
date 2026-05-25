# OntoLLM‑Benchmark

OntoLLM‑Benchmark is a unified, multidimensional evaluation suite for assessing ontology‑grounded generation in large language models (LLMs). It provides a structured, reproducible framework for measuring semantic, logical, structural, and provenance‑based correctness across multiple domains and tasks. The benchmark includes ontology‑derived instances, prompting templates, evaluation metrics, synthetic diagnostics, and a complete experimental pipeline.

The benchmark spans four ontology‑grounded domains (Biomedical, Educational, Environmental, General‑purpose) and provides three difficulty levels (Easy / Medium / Hard) for each task to support controlled reasoning evaluation.

---

## 1. Overview

OntoLLM‑Benchmark evaluates how well LLMs integrate and respect formal ontological structure.  
Unlike traditional NLP benchmarks that focus on surface similarity or triple‑level accuracy, this benchmark assesses:

- Semantic fidelity (SFS)
- Logical consistency (LCI)
- Ontology faithfulness (OFS)
- Provenance grounding (PFS)
- Structural coherence (SCS)

The benchmark includes five ontology‑grounded tasks:

1. Definition generation  
2. Axiom completion  
3. Hierarchical placement  
4. Structural coherence  
5. Provenance‑grounded explanation  

Each task is paired with gold‑standard reference knowledge extracted directly from the ontology.

---

## 2. Repository Structure
```
OntoLLM-Benchmark/
│
├── benchmark/          # Ontology-derived instances and metadata
├── prompts/            # Prompt templates for all tasks (E/M/H)
├── metrics/            # Implementations of SFS, LCI, OFS, PFS, SCS
├── evaluation/         # Unified scoring pipeline
├── scripts/            # Model execution, evaluation, aggregation, plotting
├── results/            # Generated outputs (created dynamically)
├── ontologies/         # Optional ontology files (may remain empty)
├── docs/               # Extended documentation and diagrams
├── requirements        # Python dependencies
├── CITATION.cff        # Citation metadata
└── LICENSE             # MIT license
```
### Key Documentation

- docs/benchmark_overview.md  
- docs/pipeline.md  
- docs/metric_definitions.md  
- docs/synthetic_examples.md  
- docs/domain_diagram.md  
- docs/difficulty_scaling.md  
- docs/error_analysis_examples.md  

---

## 3. Benchmark Tasks

### Definition Generation  
Generate an ontology‑aligned definition for a given concept identifier.

### Axiom Completion  
Complete missing superclass or relation axioms.

### Hierarchical Placement  
Propose the correct parent class or relational placement.

### Structural Coherence  
Determine whether a triple violates domain, range, disjointness, or hierarchy constraints.

### Provenance‑Grounded Explanation  
Justify a statement using verifiable evidence.

Each task includes ontology‑derived gold references, structured prompts, deterministic evaluation, and synthetic diagnostics.

---

## 4. Evaluation Metrics

OntoLLM‑Benchmark introduces five complementary metrics:

- Semantic Fidelity Score (SFS)  
- Logical Consistency Index (LCI)  
- Ontology Faithfulness Score (OFS)  
- Provenance Faithfulness Score (PFS)  
- Structural Coherence Score (SCS)

Formal definitions and examples:

- docs/metric_definitions.md  
- docs/synthetic_examples.md  
- docs/error_analysis_examples.md  

---

## 5. Domains and Ontologies

| Domain           | Ontologies        | Description |
|------------------|-------------------|-------------|
| Biomedical       | GO, CL            | Cellular processes, anatomy, molecular functions |
| Environmental    | ENVO              | Ecosystems, habitats, environmental processes |
| Educational      | ESCO              | Competences, skills, learning activities |
| General-purpose  | Wikidata, WordNet | Everyday concepts and artifacts |

Each domain folder contains `instances.json` and `metadata.json`.

---

## 6. Installation

### Requirements

- Python 3.10+  
- RDFlib  
- Owlready2  
- NumPy / SciPy  
- Matplotlib / Seaborn  
- SentenceTransformers  
- OpenAI / HuggingFace APIs (optional)

Install dependencies:
```
pip install -r requirements
```
The `results/` directory is generated automatically during evaluation.

---

## 7. Quickstart

### Run model inference
```
python scripts/run_model.py --model gpt-4o --domain biomedical
```
### Evaluate model outputs
```
python evaluation/pipeline.py --input results/gpt-4o_biomedical.json
```
### Aggregate results
```
python scripts/aggregate_results.py
```
### Generate plots
```
python scripts/generate_plots.py
```
---

## 8. Documentation

Extended documentation is available in the `docs/` directory:

- benchmark overview  
- pipeline description  
- metric definitions  
- synthetic examples  
- difficulty scaling  
- error analysis  

---

## 9. Citing OntoLLM‑Benchmark

If you use this benchmark in your research, please cite:
See CITATION.cff for full metadata.


---

## 10. License

This project is released under the MIT License.  
See `LICENSE` for details.

---

## Summary

OntoLLM‑Benchmark provides a principled, ontology‑grounded evaluation framework for LLMs.  
It supports multi‑domain, multi‑task, multi‑metric assessment with controlled difficulty scaling,  
synthetic diagnostics, and a complete reproducible pipeline.


