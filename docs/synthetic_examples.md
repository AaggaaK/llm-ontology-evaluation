# Synthetic Examples for OntoLLM‑Benchmark

This document provides synthetic, minimal examples illustrating the five ontology‑grounded
tasks and the five evaluation metrics used in OntoLLM‑Benchmark.  
All examples are artificial and serve only as explanatory material.

---

# 1. Task Examples

## 1.1 Definition Generation

**Input**

- Concept: *PhotosyntheticProcess*  
- Ontology ID: GO:0015979  
- Context: "Occurs in plant cells"

**Gold Definition**

"A biological process in which organisms convert light energy into chemical energy."

**Model Output (example)**

"A process where plants use light to produce energy."

**Notes**

- Semantically aligned  
- No hallucinated relations  
- One‑sentence definition  

---

## 1.2 Axiom Completion

**Input**

Concept: *River*  
Known axioms:

- River subclassOf WaterBody  
- River hasFlowDirection some Direction  

**Gold Missing Axiom**

- River locatedIn some GeographicalRegion

**Model Output (example)**

- River locatedIn GeographicalRegion

**Notes**

- Relation exists in ontology  
- Axiom is logically consistent  

---

## 1.3 Hierarchical Placement

**Input**

Concept: *ElectricCar*  
Candidate parents:

- Vehicle  
- ElectricDevice  
- Car  

**Gold Parent**

- Car

**Model Output (example)**

Parent class: Car  
Justification: "Electric cars are a subclass of cars with an electric propulsion system."

---

## 1.4 Structural Coherence

**Input Triple**

(Eagle, hasHabitat, Ocean)

**Gold Answer**

INVALID — domain/range mismatch (eagles do not inhabit oceans)

**Model Output (example)**

Status: INVALID  
Explanation: "Ocean is not a valid habitat for eagles."

---

## 1.5 Provenance‑Grounded Explanation

**Input**

Statement: "Photosynthesis requires chlorophyll."

**Gold Explanation**

"Photosynthesis depends on chlorophyll to absorb light energy."

**Gold Sources**

- GO:0015979  
- Wikidata: Q11351  

**Model Output (example)**

Explanation: "Chlorophyll enables light absorption during photosynthesis."  
Sources:
- GO:0015979  
- Wikidata: Q11351

---

# 2. Metric Examples

## 2.1 Semantic Fidelity Score (SFS)

**Reference**

"Plants convert light energy into chemical energy."

**Generated**

"Plants use sunlight to produce energy."



\[
\text{SFS} = 0.89
\]



Interpretation: High semantic alignment.

---

## 2.2 Logical Consistency Index (LCI)

Generated axioms:

1. River subclassOf WaterBody  
2. River flowsThrough City  
3. River hasColor Blue (❌ invalid — property not in ontology)

Valid axioms: 2  
Total axioms: 3  



\[
\text{LCI} = \frac{2}{3} = 0.67
\]



---

## 2.3 Ontology Faithfulness Score (OFS)

Generated relations:

- hasHabitat  
- locatedIn  
- hasColor (❌ not in ontology)

Valid relations: 2  
Total relations: 3  



\[
\text{OFS} = \frac{2}{3} = 0.67
\]



---

## 2.4 Provenance Faithfulness Score (PFS)

Generated sources:

- GO:0015979 (valid)  
- "biologyfacts.net" (❌ invalid)  
- Wikidata: Q11351 (valid)

Valid: 2  
Total: 3  



\[
\text{PFS} = \frac{2}{3} = 0.67
\]



---

## 2.5 Structural Coherence Score (SCS)

Gold parent: *Car*  
Predicted parent: *Vehicle*  

Ontology distance:



\[
d(\text{Vehicle}, \text{Car}) = 1
\]



Maximum distance:



\[
D_{\max} = 4
\]





\[
\text{SCS} = 1 - \frac{1}{4} = 0.75
\]



Interpretation: Structurally close but not exact.

---

# 3. Summary

These synthetic examples illustrate:

- how each task is structured,  
- how outputs are evaluated,  
- how the five metrics quantify correctness,  
- how the benchmark captures semantic, logical, structural, and provenance dimensions.

For implementation details, see:  
- **metrics.md**  
- **pipeline.md**  
- **benchmark_overview.md**  
- **error_analysis_examples.md**
