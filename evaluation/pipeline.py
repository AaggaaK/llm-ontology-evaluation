import json
import os
from typing import Dict, Any, List

from evaluation.metrics.sfs import compute_sfs
from evaluation.metrics.lci import compute_lci
from evaluation.metrics.ofs import compute_ofs_from_sets
from evaluation.metrics.pfs import compute_pfs
from evaluation.metrics.scs import compute_scs


def load_instances(path: str) -> List[Dict[str, Any]]:
    """Load benchmark instances from CSV-like JSON."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_model_outputs(path: str) -> Dict[str, Any]:
    """Load model outputs from JSON."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate_instance(instance: Dict[str, Any], output: Dict[str, Any]) -> Dict[str, float]:
    """
    Evaluate a single instance using all metrics.
    Expected fields in instance:
        - reference_text
        - ontology_relations
        - entailed_axioms
        - violated_axioms
        - valid_sources
        - invalid_sources
        - path_length
        - max_distance
    Expected fields in output:
        - generated_text
        - predicted_relations
        - predicted_sources
    """

    # SFS
    sfs = compute_sfs(
        generated=output.get("generated_text", ""),
        reference=instance.get("reference_text", "")
    )

    # LCI
    lci = compute_lci(
        entailed_axioms=instance.get("entailed_axioms", []),
        violated_axioms=instance.get("violated_axioms", [])
    )

    # OFS
    predicted_rel = set(output.get("predicted_relations", []))
    ontology_rel = set(instance.get("ontology_relations", []))
    ofs = compute_ofs_from_sets(predicted_rel, ontology_rel)

    # PFS
    pfs = compute_pfs(
        valid_sources=instance.get("valid_sources", []),
        invalid_sources=instance.get("invalid_sources", [])
    )

    # SCS
    scs = compute_scs(
        path_length=instance.get("path_length"),
        max_distance=instance.get("max_distance", 10)
    )

    return {
        "SFS": sfs,
        "LCI": lci,
        "OFS": ofs,
        "PFS": pfs,
        "SCS": scs
    }


def evaluate_domain(instances_path: str, outputs_path: str, save_path: str):
    """Evaluate all instances for a given domain and save results."""
    instances = load_instances(instances_path)
    outputs = load_model_outputs(outputs_path)

    results = []
    for inst in instances:
        inst_id = inst["id"]
        model_out = outputs.get(inst_id, {})
        metrics = evaluate_instance(inst, model_out)
        results.append({
            "id": inst_id,
            **metrics
        })

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved evaluation results to {save_path}")


def evaluate_all(domains: List[str], model_name: str):
    """Evaluate all domains for a given model."""
    for domain in domains:
        instances_path = f"benchmark/{domain}/instances.json"
        outputs_path = f"results/raw/{model_name}/{domain}.json"
        save_path = f"results/processed/{model_name}/{domain}_scores.json"

        evaluate_domain(instances_path, outputs_path, save_path)
