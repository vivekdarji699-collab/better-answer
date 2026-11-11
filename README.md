# Prompt Optimizer

A small Python CLI that takes your rough prompt, rewrites it into a clearer and more specific one using an AI model, and then sends the improved prompt to the model to get the final answer.

## How it works

1. You type a raw prompt.
2. The first model call rewrites it into a better prompt (without answering it).
3. The second model call answers the optimized prompt.

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com) installed and running
- Access to the `gemma4:31b-cloud` model (change `MODEL` in `main.py` to use another one)

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Type `exit` or `quit` to stop.

## Configuration

- **Model:** change the `MODEL` constant at the top of `main.py`.
- **Optimizer behavior:** edit `OPTIMIZER_PROMPT` in `main.py`.
