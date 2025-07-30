#!/bin/bash

echo "[SPARK] Installing dependencies..."
pip install -r requirements.txt

echo "[SPARK] Pulling model from Ollama..."
ollama pull openhermes

echo "[SPARK] Launching assistant..."
python main.py