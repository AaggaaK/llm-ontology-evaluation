#!/bin/bash

MODEL=$1

DOMAINS=("biomedical" "educational" "general" "environmental")

echo "Running model: $MODEL"

for DOMAIN in "${DOMAINS[@]}"; do
    echo "----------------------------------------"
    echo "Running domain: $DOMAIN"
    python scripts/run_model.py --model $MODEL --domain $DOMAIN
    python scripts/evaluate_model.py --model $MODEL --domain $DOMAIN
done

echo "All domains completed."
