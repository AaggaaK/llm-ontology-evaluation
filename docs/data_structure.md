# Data Structure

Each domain contains:

- `instances.json` — benchmark instances
- `metadata.json` — domain metadata

## Instance fields

- `id`
- `task`
- `concept_label`
- `concept_id`
- `reference_text`
- `ontology_relations`
- `entailed_axioms`
- `violated_axioms`
- `valid_sources`
- `invalid_sources`
- `path_length`
- `max_distance`

These fields are consumed by the evaluation pipeline.
