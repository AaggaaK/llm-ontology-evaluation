# Data Flow Diagram for OntoLLM‑Benchmark

This diagram illustrates the full data flow in OntoLLM‑Benchmark, from
ontology-derived instances, through model prompting and evaluation, to
metric computation and final aggregated results.  
It corresponds to the pipeline described in **Appendix B** of the paper.

---

## 1. High‑level data flow

┌───────────────────────────────┐

│       ONTOLOGY SOURCES        │
│   (GO, ENVO, ESCO, Wikidata)  │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│   BENCHMARK INSTANCES (JSON)  │
│  benchmark/<domain>/instances │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│       PROMPT TEMPLATES        │
│ prompts/<task>/<difficulty>   │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│      MODEL GENERATION         │
│   scripts/run_model.py        │
└───────────────┬───────────────┘
│
▼
┌───────────────────────────────┐
│     RAW MODEL OUTPUTS         │
│   results/raw/<model>/<dom>   │
└───────────────┬───────────────┘
│
▼
┌────────────────────────┼────────────────────────┐
│                        │                        │
▼                        ▼                        ▼
┌───────────────┐        ┌───────────────┐        ┌───────────────┐
│  METRIC: SFS  │        │  METRIC: LCI  │        │  METRIC: SCS  │
│  semantics    │        │  logic        │        │  structure    │
└───────────────┘        └───────────────┘        └───────────────┘
│                        │                        │
▼                        ▼                        ▼
┌───────────────┐        ┌───────────────┐
│  METRIC: OFS  │        │  METRIC: PFS  │
│  ontology     │        │  provenance   │
└───────────────┘        └───────────────┘
│
▼
┌──────────────────────────────────────────┐
│     PROCESSED SCORES (per model/domain)  │
│ results/processed/<model>/<domain>.json  │
└──────────────────────────┬───────────────┘
│
▼
┌──────────────────────────────────────────┐
│        AGGREGATED BENCHMARK RESULTS      │
│   scripts/prepare_results.py / plots     │
└──────────────────────────────────────────┘


---

## 2. Explanation of the flow

- **Ontology sources → Instances**  
  Ontology classes, axioms, and metadata are transformed into structured benchmark instances.

- **Instances → Prompts**  
  Each instance is paired with a task‑specific prompt template (E/M/H difficulty).

- **Prompts → Model generation**  
  Models generate outputs for each task and domain.

- **Model outputs → Metrics**  
  Five metrics evaluate different correctness dimensions:
  - SFS — semantic fidelity  
  - LCI — logical consistency  
  - OFS — ontology faithfulness  
  - PFS — provenance grounding  
  - SCS — structural coherence  

- **Metrics → Processed scores**  
  Scores are saved per model and per domain.

- **Processed scores → Aggregated results**  
  Final tables, plots, and summaries are produced.

---

## 3. Related documents

- **Prompts:** `../prompts/`  
- **Metric definitions:** `metrics_definition.md`  
- **Metrics overview:** `metrics.md`  
- **Pipeline documentation:** `pipeline.md`  
- **Domain diagram:** `domain_diagram.md`  
- **Difficulty scaling:** `difficulty_scaling.md`  
