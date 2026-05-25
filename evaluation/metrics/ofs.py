from typing import List, Set

def compute_ofs(valid_relations: List[str], hallucinated_relations: List[str]) -> float:
    """
    Ontology Faithfulness Score (OFS):
    OFS = |valid_relations| / (|valid_relations| + |hallucinated_relations| + epsilon)
    """
    eps = 1e-8
    v = len(valid_relations)
    h = len(hallucinated_relations)
    denom = v + h + eps
    return float(v / denom)

def compute_ofs_from_sets(predicted: Set[str], ontology_relations: Set[str]) -> float:
    """
    Helper: predicted relations vs ontology relation set.
    """
    valid = predicted & ontology_relations
    hallucinated = predicted - ontology_relations
    return compute_ofs(list(valid), list(hallucinated))
