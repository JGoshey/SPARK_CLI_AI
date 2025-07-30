import os
import json
import requests
from utils.formatter import format_output
from datetime import datetime

# Load config
with open('config/config.json', 'r') as f:
    config = json.load(f)

model = config.get('model', 'openhermes')
log_enabled = config.get('log_enabled', False)
use_rich = config.get('use_rich', False)
ollama_url = config.get('ollama_url', 'http://localhost:11434')

# Load system prompt
system_prompt = open('config/system.txt').read().strip()

# Load few-shot (optional)
few_shot = []
try:
    few_shot = json.load(open('config/few_shot.json'))
except:
    pass

if log_enabled:
    os.makedirs('logs', exist_ok=True)
    log_path = f"logs/{datetime.now().strftime('%Y-%m-%d')}.txt"

print("\n[SPARK] Ollama-powered CLI assistant loaded. Model may take a moment for first response. Type 'exit' to quit.\n")

while True:
    try:
        user_input = input("\n>>> ").strip()
        if user_input.lower() in ('exit', 'quit'):
            break

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages += few_shot
        messages.append({"role": "user", "content": user_input})

        payload = {
            "model": model,
            "messages": messages,
            "stream": False
        }

        response = requests.post(f"{ollama_url}/api/chat", json=payload)
        content = response.json()["message"]["content"]

        print(format_output(content, use_rich))

        if log_enabled:
            with open(log_path, 'a') as f:
                f.write(f"USER: {user_input}\nASSISTANT: {content}\n\n")

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"[ERROR] {e}")
