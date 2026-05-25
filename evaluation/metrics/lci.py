from typing import List

def compute_lci(entailed_axioms: List[str], violated_axioms: List[str]) -> float:
    """
    Logical Consistency Index (LCI):
    LCI = |entailed| / (|entailed| + |violated| + epsilon)
    """
    eps = 1e-8
    e = len(entailed_axioms)
    v = len(violated_axioms)
    denom = e + v + eps
    return float(e / denom)
