import os
import json
import argparse
from typing import Dict, Any

from openai import OpenAI


def load_instances(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_prompt(task: str) -> str:
    path = f"prompts/{task}.txt"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def format_prompt(template: str, instance: Dict[str, Any]) -> str:
    """Fill template placeholders with instance fields."""
    prompt = template
    for key, value in instance.items():
        placeholder = "{" + key + "}"
        prompt = prompt.replace(placeholder, str(value))
    return prompt


def call_model_openai(model_name: str, prompt: str) -> str:
    """Call OpenAI model."""
    client = OpenAI()
    response = client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    return response.choices[0].message.content.strip()


def run_model(domain: str, model_name: str, output_path: str):
    instances_path = f"benchmark/{domain}/instances.json"
    instances = load_instances(instances_path)

    results = {}

    for inst in instances:
        inst_id = inst["id"]
        task = inst["task"]

        template = load_prompt(task)
        prompt = format_prompt(template, inst)

        print(f"Running {model_name} on {inst_id}...")

        generated = call_model_openai(model_name, prompt)

        # Minimal structured output for pipeline compatibility
        results[inst_id] = {
            "generated_text": generated,
            "predicted_relations": [],   # filled by model if needed
            "predicted_sources": []      # filled by model if needed
        }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved raw model outputs to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True, help="Model name, e.g. gpt-4o")
    parser.add_argument("--domain", type=str, required=True, help="Domain folder name")
    args = parser.parse_args()

    output_path = f"results/raw/{args.model}/{args.domain}.json"
    run_model(args.domain, args.model, output_path)
