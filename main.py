import ollama

MODEL = "gemma4:31b-cloud"

OPTIMIZER_PROMPT = """You are an expert AI prompt optimizer.

Your job is to take the user's raw prompt and rewrite it into a significantly better prompt that another AI model can use to produce the best possible answer.

Follow these rules:

1. Understand the user's actual goal and intent.
2. Preserve the user's original meaning. Do not change what they are asking.
3. Remove unnecessary wording, confusion, repetition, and ambiguity.
4. Add useful context or structure when it is reasonably implied by the user's request.
5. Make the prompt specific, clear, and easy for another AI to follow.
6. Add relevant constraints, requirements, output format, or reasoning instructions when they would improve the result.
7. Do not invent facts, requirements, preferences, or personal information that the user did not provide or reasonably imply.
8. If the user's prompt is already good, improve it only where necessary.
9. Do not answer the user's question yourself.
10. Do not explain what you changed.
11. Return ONLY the optimized prompt.

The optimized prompt should be written as if the user had originally written a high-quality prompt for the second AI.
"""


def optimize_prompt(raw_prompt: str) -> str:
    """Rewrite the user's raw prompt into a clearer, more specific one."""
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": OPTIMIZER_PROMPT},
            {"role": "user", "content": raw_prompt},
        ],
    )
    return response["message"]["content"]


def answer_prompt(prompt: str) -> str:
    """Send the optimized prompt to the model and return its answer."""
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


def main() -> None:
    print("Prompt Optimizer (type 'exit' to quit)")
    while True:
        user = input("Enter: ").strip()
        if not user:
            continue
        if user.lower() in {"exit", "quit"}:
            break

        try:
            optimized = optimize_prompt(user)
            print(f"\n[Optimized prompt]\n{optimized}\n")
            print(answer_prompt(optimized))
            print()
        except Exception as error:
            print(f"Something went wrong: {error}\n")


if __name__ == "__main__":
    main()
