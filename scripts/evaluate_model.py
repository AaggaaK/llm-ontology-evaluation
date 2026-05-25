import argparse
import os
from evaluation.pipeline import evaluate_domain


def main(model_name: str, domain: str):
    """
    Evaluate model outputs for a single domain.
    """

    instances_path = f"benchmark/{domain}/instances.json"
    outputs_path = f"results/raw/{model_name}/{domain}.json"
    save_path = f"results/processed/{model_name}/{domain}_scores.json"

    print(f"Evaluating model '{model_name}' on domain '{domain}'...")
    print(f"- Instances: {instances_path}")
    print(f"- Raw outputs: {outputs_path}")
    print(f"- Saving scores to: {save_path}")

    evaluate_domain(instances_path, outputs_path, save_path)

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Model name, e.g. gpt-4o")
    parser.add_argument("--domain", type=str, required=True, help="Domain name, e.g. biomedical")
    args = parser.parse_args()

    main(args.model, args.domain)
