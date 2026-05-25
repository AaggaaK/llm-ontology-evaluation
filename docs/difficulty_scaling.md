# Difficulty Scaling in OntoLLM‑Benchmark

Difficulty scaling is a core design principle of OntoLLM‑Benchmark.  
Each of the five ontology‑grounded tasks is provided in three difficulty levels:

- **Easy (E)** — foundational reasoning  
- **Medium (M)** — compositional reasoning  
- **Hard (H)** — multi‑step, ontology‑aware reasoning under ambiguity  

This document explains the rationale, structure, and design methodology behind the E/M/H scaling.

---

## 1. Why Difficulty Scaling?

Large language models exhibit highly non‑linear performance changes depending on:

- prompt complexity  
- number of reasoning steps  
- presence of distractors  
- ontology depth and branching factor  
- requirement for multi‑hop inference  

Difficulty scaling enables:

- **robustness analysis** across reasoning depths  
- **scaling‑law‑like evaluation** for ontology tasks  
- **fine‑grained comparison** between models  
- **controlled stress‑testing** of ontology‑aware reasoning  

It also aligns OntoLLM‑Benchmark with established benchmarks such as MMLU, BIG‑bench, and GSM8K.

---

## 2. Design Principles

Difficulty levels were constructed according to four principles:

### 2.1 Controlled Cognitive Load
Each level increases the number of reasoning steps required:

- Easy: 1–2 steps  
- Medium: 2–4 steps  
- Hard: 4+ steps with branching or ambiguity  

### 2.2 Ontology Depth & Breadth
Difficulty increases with:

- deeper class hierarchies  
- more axioms per entity  
- more cross‑domain references  
- more distractor classes  

### 2.3 Linguistic Complexity
Hard prompts introduce:

- paraphrasing  
- implicit references  
- multi‑sentence context  
- subtle contradictions  

### 2.4 Error Sensitivity
Hard tasks are designed so that:

- hallucinations are more likely  
- shallow heuristics fail  
- correct answers require ontology‑grounded reasoning  

---

## 3. Difficulty Levels

### 3.1 Easy (E)
**Goal:** Test basic ontology understanding.

Characteristics:
- shallow hierarchy (depth 1–2)  
- explicit definitions  
- no distractors  
- single‑step inference  
- minimal linguistic variation  

Example (Definition Task):  
“Provide a concise definition of the class *River* based on the ontology.”

---

### 3.2 Medium (M)
**Goal:** Test compositional reasoning.

Characteristics:
- moderate hierarchy (depth 2–3)  
- multiple axioms per entity  
- light distractors  
- 2–4 reasoning steps  
- paraphrased descriptions  

Example (Axiom Completion):  
“Given the axioms for *Wetland*, infer one additional property that must hold.”

---

### 3.3 Hard (H)
**Goal:** Test multi‑hop, ontology‑aware reasoning under ambiguity.

Characteristics:
- deep hierarchy (depth 3–5)  
- cross‑domain references  
- multiple distractors  
- implicit constraints  
- multi‑sentence context  
- requires verification or self‑correction  

Example (Hierarchical Placement):  
“Given the description of *Estuarine Delta*, determine its most specific parent class.  
Some details may be ambiguous or partially conflicting.”

---

## 4. Difficulty Comparison Table

| Task | Easy | Medium | Hard |
|------|------|--------|------|
| Definition | explicit, shallow | paraphrased, multi‑axiom | implicit, multi‑sentence |
| Axiom Completion | 1 missing axiom | 1–2 compositional axioms | multi‑hop inference |
| Hierarchical Placement | depth ≤2 | depth ≤3 | depth ≥4, distractors |
| Schema Validation | simple constraints | multi‑field constraints | conflicting constraints |
| Provenance | single source | multiple sources | ambiguous or incomplete sources |

---

## 5. How Difficulty Scaling Was Implemented

Difficulty levels were generated using a **controlled prompt engineering pipeline**:

1. Base prompt templates were created for each task.  
2. Linguistic and structural complexity was increased systematically.  
3. Ontology depth and distractors were added for M/H.  
4. Synthetic examples were validated manually.  
5. Hard prompts were stress‑tested on multiple LLMs to ensure non‑triviality.

This ensures that difficulty levels are:

- **consistent across tasks**  
- **predictable and measurable**  
- **aligned with ontology reasoning theory**  

---

## 6. How to Use Difficulty Levels

Difficulty scaling supports multiple evaluation modes:

- **Model scaling analysis** (small → large models)  
- **Reasoning robustness**  
- **Cross‑domain generalization**  
- **Error analysis**  
- **Curriculum‑style evaluation**  

For examples of how difficulty affects model behaviour, see:  
**`docs/error_analysis_examples.md`** (recommended).

---

## 7. Related Documents

- [Prompts folder](ca://s?q=Review_prompts_folder)  
- [Synthetic examples](ca://s?q=Generate_error_analysis_examples)  
- [Metric definitions](ca://s?q=Explain_metric_implementations)  
- [Pipeline documentation](ca://s?q=Review_pipeline_md)

---

# Summary

Difficulty scaling in OntoLLM‑Benchmark provides a principled, ontology‑aware way to evaluate LLM reasoning across increasing levels of complexity.  
It is essential for robustness, fairness, and scientific interpretability of results.
