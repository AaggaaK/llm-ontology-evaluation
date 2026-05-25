from typing import List

def compute_pfs(valid_sources: List[str], invalid_sources: List[str]) -> float:
    """
    Provenance Faithfulness Score (PFS):
    PFS = |valid_sources| / (|valid_sources| + |invalid_sources| + epsilon)
    """
    eps = 1e-8
    v = len(valid_sources)
    i = len(invalid_sources)
    denom = v + i + eps
    return float(v / denom)
