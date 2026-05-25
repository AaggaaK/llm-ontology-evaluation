from typing import Optional

def compute_scs(path_length: Optional[int], max_distance: int) -> float:
    """
    Structural Coherence Score (SCS):
    SCS = 1 - (d / max_distance), where d is ontology path length
    between generated and reference node. If no path: 0.0.
    """
    if path_length is None:
        return 0.0
    d = float(path_length)
    if max_distance <= 0:
        return 0.0
    score = 1.0 - (d / float(max_distance))
    return float(max(0.0, min(1.0, score)))
