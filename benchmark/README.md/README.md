# OntoLLM-Benchmark — Domain Instances

This folder contains all ontology-grounded benchmark instances used in the
OntoLLM unified evaluation framework (Section 5 of the paper).  
Each subfolder corresponds to one ontology domain and includes:

- `instances.json` — a set of 5 representative benchmark instances  
- `metadata.json` — domain description, ontology sources, and task coverage  

## Domains
- `biomedical/` — Gene Ontology, Cell Ontology, NCBI Taxonomy  
- `environmental/` — ENVO (Environment Ontology)  
- `educational/` — ESCO educational concepts  
- `general/` — Wikidata and WordNet common-sense concepts  

## Tasks
Each domain includes 5 instances covering the benchmark tasks:
- definition  
- axiom_completion  
- hierarchical_placement  
- structural_coherence  
- provenance  

These instances are used by the evaluation pipeline to compute all five
ontology-grounded metrics.
