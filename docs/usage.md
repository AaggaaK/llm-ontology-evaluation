# Usage Guide

This guide explains how to run models, evaluate outputs, aggregate results, and
generate visualizations using OntoLLM‑Benchmark.

---

## 1. Running a model

Runs inference for a selected model and domain using E/M/H prompt templates.

```
python scripts/run_model.py --model gpt-4o --domain biomedical
```

Outputs are saved to:
```
results/raw/<model>/<domain>.json
```
---

## 2. Evaluating results

Computes all five ontology‑grounded metrics (SFS, LCI, OFS, PFS, SCS).
```
python scripts/evaluate_model.py --model gpt-4o --domain biomedical
```

Processed scores are saved to:
```
results/processed/<model>/<domain>_scores.json
```


---

## 3. Running all domains

Runs inference across all four benchmark domains.
```
./scripts/run_all.sh gpt-4o
```

---

## 4. Merging results

Aggregates per‑domain scores into a unified benchmark summary.
```
python scripts/prepare_results.py
```

Outputs include:

- merged JSON summaries  
- CSV tables  
- domain‑level comparisons  

---

## 5. Generating plots

Produces visualizations for model comparison and metric analysis.
```
python scripts/generate_plots.py
```

Figures are exported to:
```
results/plots/
```
---

## 6. Related Documents

- **Benchmark overview:** `benchmark_overview.md`  
- **Pipeline:** `pipeline.md`  
- **Metrics:** `metrics.md`  
- **Metric definitions:** `metrics_definition.md`  
- **Difficulty scaling:** `difficulty_scaling.md`  
- **Synthetic examples:** `synthetic_examples.md`  

---

# Summary

This guide provides the essential commands for running models, computing metrics,
and generating benchmark outputs.  
It complements the pipeline and metric documentation and serves as the entry
point for using OntoLLM‑Benchmark in practice.

