# Evaluation Pipeline

The evaluation pipeline integrates all benchmark components and corresponds to
the architecture described in **Appendix B** of the paper.  
It processes ontology‑derived instances, generates model outputs, computes all
five metrics, and aggregates results across domains.

---

## 1. Pipeline Steps

1. **Load benchmark instances**  
   `benchmark/<domain>/instances.json`

2. **Load raw model outputs**  
   `results/raw/<model>/<domain>.json`

3. **Compute all five metrics**  
   (SFS, LCI, OFS, PFS, SCS)

4. **Save processed scores**  
   `results/processed/<model>/<domain>_scores.json`

Difficulty scaling (E/M/H) is applied at the prompt‑generation stage.

---

## 2. Implementation Components

- `evaluation/pipeline.py` — core evaluation logic  
- `evaluation/metrics/` — metric implementations  
- `scripts/run_model.py` — model inference  
- `scripts/evaluate_model.py` — metric computation  
- `scripts/prepare_results.py` — aggregation  
- `scripts/generate_plots.py` — visualization  

---

## 3. Pipeline Diagram (ASCII)

The evaluation pipeline processes benchmark instances, generates model outputs,
computes all five ontology‑grounded metrics, aggregates results across domains,
and produces visualizations for analysis.

┌──────────────────────────┐
│      benchmark/          │
│  instances + metadata    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│        prompts/          │
│  task templates (E/M/H)  │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│      run_model.py        │
│  - loads instances       │
│  - loads prompts         │
│  - queries model         │
│  - saves raw outputs     │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│        results/          │
│   raw model generations  │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│    evaluate_model.py     │
│  - loads gold references │
│  - applies metrics       │
│  - produces scores       │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   prepare_results.py     │
│  - merges domain scores  │
│  - aggregates metrics    │
└─────────────┬────────────┘
│
▼
┌──────────────────────────┐
│   generate_plots.py      │
│  - visualizes results    │
│  - exports figures       │
└──────────────────────────┘

---

## 4. Related Documents

- **Data flow diagram:** `dataflow_diagram.md`  
- **Metric definitions:** `metrics_definition.md`  
- **Benchmark overview:** `benchmark_overview.md`  
- **Difficulty scaling:** `difficulty_scaling.md`  
- **Synthetic examples:** `synthetic_examples.md`

