import json
import os
import matplotlib.pyplot as plt
import numpy as np


def load_scores(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def plot_domain_scores(model_name: str, domain: str):
    path = f"results/processed/{model_name}/{domain}_scores.json"
    scores = load_scores(path)

    metrics = ["SFS", "LCI", "OFS", "PFS", "SCS"]
    values = {m: [] for m in metrics}

    for inst in scores:
        for m in metrics:
            values[m].append(inst[m])

    means = [np.mean(values[m]) for m in metrics]

    plt.figure(figsize=(8, 4))
    plt.bar(metrics, means, color="steelblue")
    plt.ylim(0, 1)
    plt.title(f"{model_name} — {domain}")
    plt.ylabel("Score")
    plt.tight_layout()

    os.makedirs("results/figures", exist_ok=True)
    plt.savefig(f"results/figures/{model_name}_{domain}.png")
    plt.close()


if __name__ == "__main__":
    MODEL = "gpt-4o"
    DOMAINS = ["biomedical", "educational", "general", "environmental"]

    for d in DOMAINS:
        plot_domain_scores(MODEL, d)

    print("Figures saved to results/figures/")
