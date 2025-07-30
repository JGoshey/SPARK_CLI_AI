# SPARK AI customizable (Local LLM Template)

This is a minimalist, terminal-based AI assistant powered by a local GGUF model using `llama-cpp-python`.

# Features
Configurable system prompt and few-shot examples,
Clean terminal interface,
Logs conversations to `/logs`,
Easily forked and modified for your own builds

# Usage
```bash
pip install -r requirements.txt
python main.py
```

If perferred, use the included `start.bat` or `start.sh` launchers.

# Config
Edit `config/config.json` to:
Point to your `.gguf` model file,
Adjust temp, top_p, output tokens,
Enable/disable logging or rich output

# Dependencies
[llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
[rich](https://github.com/Textualize/rich) (optional but looks good)

# Exit
Built to be modified, enjoy. 