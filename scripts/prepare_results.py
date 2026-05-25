import json
import os
from typing import Dict, List


def load_scores(path: str) -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_results(model_name: str, domains: List[str], save_path: str):
    merged = {}

    for domain in domains:
        path = f"results/processed/{model_name}/{domain}_scores.json"
        if os.path.exists(path):
            merged[domain] = load_scores(path)
        else:
            print(f"Warning: missing file {path}")

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)

    print(f"Merged results saved to {save_path}")


if __name__ == "__main__":
    DOMAINS = ["biomedical", "educational", "general", "environmental"]
    MODEL = "gpt-4o"

    merge_results(MODEL, DOMAINS, f"results/merged/{MODEL}_all_domains.json")
