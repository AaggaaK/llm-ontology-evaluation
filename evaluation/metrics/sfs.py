import numpy as np
from sentence_transformers import SentenceTransformer, util

_model = None

def get_model(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    global _model
    if _model is None:
        _model = SentenceTransformer(model_name)
    return _model

def compute_sfs(generated: str, reference: str) -> float:
    """
    Semantic Fidelity Score (SFS):
    cosine similarity between embeddings of generated and reference text.
    """
    model = get_model()
    emb_gen = model.encode(generated, convert_to_tensor=True)
    emb_ref = model.encode(reference, convert_to_tensor=True)
    score = util.cos_sim(emb_gen, emb_ref).item()
    return float(max(0.0, min(1.0, score)))
